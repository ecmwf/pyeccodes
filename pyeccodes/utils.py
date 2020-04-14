# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .expression import evaluate
from .base import NoSize
import hashlib
import os

from .defs import VERSION


class Library_version(NoSize):

    def get(self, handle):
        return VERSION


class Getenv(NoSize):

    def __init__(self, name, var, default):
        super().__init__(name)
        self.value = int(os.environ.get(var, default))

    def get(self, handle):
        return self.value


class Sprintf(NoSize):

    def __init__(self, name, format, *args):
        super().__init__(name)
        self.format = format
        self.args = args

    def get(self, handle):
        return format % tuple(evaluate(x, handle) for x in self.args)


class Scale(NoSize):

    def __init__(self, name, value, multiplier, divisor, truncating):
        super().__init__(name)
        self.value = value
        self.multiplier = multiplier
        self.divisor = divisor
        self.truncating = truncating

    def get(self, handle):
        value = evaluate(self.value, handle)
        multiplier = evaluate(self.multiplier, handle)
        divisor = evaluate(self.divisor, handle)
        truncating = evaluate(self.truncating, handle)
        result = float(value) * float(multiplier) / float(divisor)
        if truncating:
            result = int(result)
        return result


class Evaluate(NoSize):

    def __init__(self, name, what):
        super().__init__(name)
        self.what = what

    def get(self, handle):
        return int(evaluate(self.what, handle))


class Md5(NoSize):

    def __init__(self, name, offset, size, *blacklist):
        super().__init__(name)
        self.offset = offset
        self.size = size
        self.blacklist = blacklist

    def get(self, handle):
        offset = evaluate(self.offset, handle)
        size = evaluate(self.size, handle)

        assert len(self.blacklist) == 0, self.blacklist

        # TODO: use black list

        md5 = hashlib.md5()
        md5.update(handle._buffer[offset:offset + size])
        return md5.hexdigest()


class VectorAccessor(NoSize):

    def __init__(self, name, accessor, index):
        super().__init__(name)
        self.accessor = accessor
        self.index = index

    def get(self, handle):
        accessor = evaluate(self.accessor, handle)
        index = evaluate(self.index, handle)
        return accessor[index]

    def __repr__(self):
        return "%s(%s,%s[%s])" % (self.__class__.__name__.split('.')[-1],
                                  self.name,
                                  self.accessor,
                                  self.index)


class Vector(VectorAccessor):
    pass


class Long_vector(VectorAccessor):
    pass


class Size(NoSize):

    def __init__(self, name, accessor):
        super().__init__(name)
        self.accessor = accessor

    # def get(self, handle):
    #     # accessor = evaluate(self.accessor, handle)
    #     accessor = handle.get(self.accessor)
    #     assert False, (accessor, accessor.count)
    #     return evaluate(accessor.count, handle)

    def __repr__(self):
        return "Size(%s,%s)" % (self.name, self.accessor)
