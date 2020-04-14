# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

import weakref
import mmap
import os
from collections import OrderedDict
from .base import ListAccessor
import numpy as np

from .templates import Template

# TODO: remove me
np.set_printoptions(threshold=64)

UNSET = object()


class List:

    def __init__(self, handle, name):
        self.name = name
        self.handle = handle
        self._index = 0
        self.accessors = OrderedDict()

    def __enter__(self):
        assert self.handle._list is None
        self.handle._list = self
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.handle._list = None
        for a in self.accessors.values():
            self.handle.add(a)

    def add(self, accessor):
        if accessor.name not in self.accessors:
            self.accessors[accessor.name] = ListAccessor(accessor.name)
        owner = self.accessors[accessor.name]
        owner.add(accessor)


class Handle:

    def __init__(self, buffer, debug=False):

        super().__init__()

        self._buffer = buffer
        self._offset = 0
        self._keys = OrderedDict()
        self._list = None
        self._cache = {}
        self._aliases = OrderedDict()

        self.debug = debug

        Template("boot.def").load(self)

    def _new(self):
        return False

    def _changed(self, *ignore):
        return False

    def _missing(self, *ignore):
        # TODO
        return False

    def _gribex_mode_on(self):
        return False

    def _defined(self, name):
        return name in self._keys

    def _add(self, accessor):
        self._cache = {}
        self._keys[accessor.name] = accessor

    def _get(self, name):

        name = self._aliases.get(name, name)

        return self._keys.get(name)

    def raw(self, name):
        return self._get(name).raw(self)

    def get(self, name, kind=None):
        accessor = self._get(name)
        if accessor is None:
            return None

        value = self._cache.get((name, kind), UNSET)

        if value is UNSET:

            if kind:
                value = getattr(accessor, 'get_' + kind)(self)
            else:
                value = accessor.get(self)

            self._cache[(name, kind)] = value

        return value

    def get_l(self, name):
        return self.get(name, 'l')

    def get_d(self, name):
        return self.get(name, 'd')

    def get_s(self, name):
        return self.get(name, 's')

    def get_r(self, name):  # 'r' is for raw
        return self.get(name, 'r')

    def add(self, accessor):

        # assert '.' not in accessor.name

        if self._list:
            self._list.add(accessor)

        accessor._handle = weakref.ref(self)
        accessor.offset = self._offset
        self._offset += accessor.length
        if self.debug:
            try:
                v = accessor.get(self)
            except Exception:
                v = '?'
            print('ADD [%s,%s] %s = %s' % (accessor.offset, accessor.offset + accessor.length, accessor, v))
        self._add(accessor)

    def set(self, name, value):
        old = self._get(name)
        self._keys[name] = old.set(value)

    def dump(self):
        for a in self._keys.values():
            a.dump(self)

    def lookup(self, klass):
        return [x for x in self._keys.values() if isinstance(x, klass)]

    def accessor(self, name):
        return self._get(name)

    def list(self, name):
        return List(self, name)

    def alias(self, name, target):
        self._aliases[name] = target

    def unalias(self, name):
        self._aliases.pop(name, None)

    def aliases(self, accessor):
        return [name for name, target in self._aliases.items() if target == accessor.name]


class GribReader:

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

        while True:
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

                if (sec4len < 120):
                    length &= 0x7fffff
                    length *= 120
                    length -= sec4len
                    length += 4

            else:
                length = self.get(8)

            self.seek(self.offset)
            return self.read(length), self.offset, length


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

        if self._buffer is None:
            return None

        self.count += 1

        self.buffer = memoryview(self._buffer)

        h = Handle(self.buffer, self.debug)
        h.offset = self.offset
        h.count = self.count
        h.reader = self  # So we don't unmap the file

        assert h.get('7777') == b'7777'
        return h
