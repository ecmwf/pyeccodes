# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .base import Accessor, NoSize
from .expression import evaluate


class Position(NoSize):

    def __init__(self, name):
        super().__init__(name)

    def get(self, handle):
        return self.offset


class Section_pointer(NoSize):

    def __init__(self, name, sectionOffset, sectionLength, sectionNumber):
        super().__init__(name)
        self.sectionOffset = sectionOffset
        self.sectionLength = sectionLength
        self.sectionNumber = sectionNumber

    def get(self, handle):
        return (evaluate(self.sectionNumber, handle),
                evaluate(self.sectionOffset, handle),
                evaluate(self.sectionLength, handle))


class Padding(Accessor):

    def __init__(self, name):
        super().__init__(name)
        self._padding = None

    def get(self, handle):
        return (self.length, handle._buffer[self.offset: self.offset + self.length])

    @property
    def length(self):
        # We cache as we don't want the padding to be adjusted
        if self._padding is None:
            self._padding = self.padding()
            if self._padding is None or self._padding < 0:
                self._padding = 0
        return self._padding


class Pad(Padding):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def padding(self):
        return evaluate(self.size, self.handle)


class Padto(Padding):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def padding(self):
        size = evaluate(self.size - self.offset, self.handle)
        return size


class Padtoeven(Padding):

    def __init__(self, name, section_offset, section_length):
        super().__init__(name)
        self.section_offset = section_offset
        self.section_length = section_length

    def padding(self):
        length = evaluate(self.section_offset, self.handle) + evaluate(self.section_length, self.handle)
        return length % 2


class Padtomultiple(Padding):

    def __init__(self, name, begin, mutiple):
        super().__init__(name)
        self.begin = begin
        self.mutiple = mutiple

    def padding(self):
        begin = evaluate(self.begin, self.handle)
        multiple = evaluate(self.mutiple, self.handle)

        padding = self.offset - begin
        padding = ((padding + multiple - 1) // multiple) * multiple - padding

        return multiple if padding == 0 else padding


class Section_padding(Padding):

    def __init__(self, name):
        super().__init__(name)

    def padding(self):
        sections = self.handle.lookup(Section_pointer)
        number, offset, length = sections[-1].get(self.handle)
        padding = length - self.offset + offset
        return padding if padding > 0 else 0
