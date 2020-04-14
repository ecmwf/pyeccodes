# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .handle import Handle
import os
import mmap


class SingleMessage:

    def __init__(self, offset, length):
        self.offset = offset
        self.length = length

    def message(self, reader):
        reader.seek(self.offset)
        return reader.read(self.length), self.offset, self.length


class MultiMessage:

    def __init__(self, offset, sections):
        self.offset = offset
        self.sections = [(None, None)] * 9
        for k, v in sections.items():
            self.sections[k] = v

    def message(self, reader):
        buf = bytearray(0)
        for pos, size in self.sections:
            if pos is not None:
                reader.seek(self.offset + pos)
                buf += reader.read(size)

        # Update header size
        size = len(buf)
        n = 15
        while size > 0:
            buf[n] = size % 256
            size //= 256
            n -= 1

        return buf, self.offset, len(buf)


class GribReader:

    messages = []

    def get(self, count):
        n = 0
        for i in range(0, count):
            n = n * 256 + int(self.read(1)[0])
        return n

    def at(self, index, count=1):
        here = self.tell()
        self.seek(self.offset + index)
        n = self.get(count)
        self.seek(here)
        return n

    def next_buffer(self):

        while len(self.messages) == 0:
            self.offset = self.tell()
            code = self.read(4)
            if len(code) < 4:
                return None, self.offset, 0

            if code != b'GRIB':
                self.seek(self.offset + 1)
                continue

            length = self.get(3)
            edition = self.get(1)

            if edition == 1:
                if length & 0x800000:
                    sec1len = self.get(3)
                    self.skip(sec1len - 3)
                    flags = self.at(15)

                    if flags & (1 << 7):
                        sec2len = self.get(3)
                        self.skip(sec2len - 3)

                    if flags & (1 << 6):
                        sec3len = self.get(3)
                        self.skip(sec3len - 3)

                    sec4len = self.get(3)
                    self.skip(sec4len - 3)

                    if sec4len < 120:
                        length &= 0x7fffff
                        length *= 120
                        length -= sec4len
                        length += 4

                self.messages = [SingleMessage(self.offset, length)]

            if edition == 2:
                length = self.get(8)
                # Crawl sections for multi-grib messages
                pos = 16
                sections = {0: (0, 16), 8: (length - 4, 4)}

                while pos < length - 5:
                    self.seek(self.offset + pos)
                    seclen = self.get(4)
                    secnum = self.get(1)

                    if secnum == 6:
                        #  Special case for inherited bitmaps
                        bitmap = self.get(1)
                        if bitmap == 254:
                            assert 6 in sections
                            pos += seclen
                            continue

                    sections[secnum] = (pos, seclen)

                    if secnum == 7:
                        self.messages.append(MultiMessage(self.offset, sections))

                    pos += seclen

                if len(self.messages) == 1:
                    # Switch bach to single-message for speed
                    self.messages = [SingleMessage(self.offset, length)]

            assert edition in (1, 2), "Unsupported GRIB edition %s" % (edition,)

        message = self.messages.pop(0)
        return message.message(self)


class MmapReader(GribReader):

    def __init__(self, path):
        self.f = os.open(path, os.O_RDONLY)
        self.buffer = mmap.mmap(self.f, 0, prot=mmap.PROT_READ)
        self.pos = 0
        self.size = len(self.buffer)

    def tell(self):
        return self.pos

    def seek(self, pos):
        self.pos = pos

    def skip(self, count):
        self.pos = min(self.pos + count, self.size)

    def read(self, count):
        start = self.pos
        end = min(self.pos + count, self.size)
        self.pos = end
        return self.buffer[start:end]

    def __del__(self):
        self.buffer.close()
        os.close(self.f)


class FileReader(GribReader):

    def __init__(self, f):
        assert 'b' in f.mode, "Files must be open in binary mode"
        self.f = f
        self.offset = f.tell()

    def skip(self, count):
        self.f.seek(count, 1)

    def seek(self, where):
        self.f.seek(where)

    def tell(self):
        return self.f.tell()

    def read(self, count):
        return self.f.read(count)


class UserFileReader(FileReader):
    pass


class OwnedFileReader(FileReader):

    def __init__(self, path):
        super().__init__(open(path, 'rb'))

    def __del__(self):
        self.f.close()


class Reader:

    def __init__(self, path, debug=False):

        # This must be a file
        if hasattr(path, 'read') and hasattr(path, 'seek'):
            self._reader = FileReader(path)
        else:
            self._reader = OwnedFileReader(path)

        self.debug = debug
        self.count = 0
        self.compat = False

    def __iter__(self):
        return self

    def __next__(self):
        h = self.next_handle()
        if h is None:
            raise StopIteration()
        return h

    def next_handle(self):

        self._buffer, self.offset, self.length = self._reader.next_buffer()
        self._reader.seek(self.offset + self.length)

        if self._buffer is None:
            return None

        self.count += 1

        self.buffer = memoryview(self._buffer)

        h = Handle(self.buffer, self.debug)
        h.offset = self.offset
        h.count = self.count
        h.reader = self  # So we don't unmap the file

        assert h.get('7777') == b'7777', "Missing 7777 at end of message, found %s" % (h.get('7777'), )
        return h
