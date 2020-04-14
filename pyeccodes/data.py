# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

import numpy as np
from .base import Accessor
from .expression import evaluate


class DataAccessor(Accessor):

    def __init__(self, name, size, count=1):
        super().__init__(name)
        self.size = size
        self.count = count

    @property
    def length(self):
        return evaluate(self.size * self.count, self.handle)

    @property
    def class_name(self):
        size = self.size
        count = self.count
        if count == 1:
            return "%s[%s]" % (self.__class__.__name__, size)
        else:
            return "%s[%sx%s]" % (self.__class__.__name__, size, count)


class Ascii(DataAccessor):

    def __init__(self, name, size):
        super().__init__(name, size)

    def get(self, handle):
        return bytes(handle._buffer[self.offset: self.offset + self.size])


MISSING_UNSIGNED = {
    1: 0xff,
    2: 0xffff,
    3: 0xffffff,
    4: 0xffffffff,
    8: 0xffffffffffffffff
}


class Unsigned(DataAccessor):

    def __init__(self, name, size, count=1):
        super().__init__(name, size, count)
        self.missing = MISSING_UNSIGNED[size]

    def get(self, handle):

        count = evaluate(self.count, handle)
        data = handle._buffer[self.offset:]

        if count == 1:
            result = 0
            for i in range(self.size):
                result = result * 256 + int(data[i])
            return None if result == self.missing else result

        if self.size in (1, 2, 4):
            return np.frombuffer(data, dtype=np.dtype('>i%d' % (self.size,)), count=count)

        array = []
        start = 0
        for j in range(count):
            result = 0
            for i in range(self.size):
                result = result * 256 + int(data[start + i])
            array.append(result)
            start += self.size
        return np.array(array)


MISSING_SIGNED = {
    1: -0x7f,
    2: -0x7fff,
    3: -0x7fffff,
    4: -0x7fffffff,
}


class Signed(DataAccessor):

    def __init__(self, name, size, count=1):
        super().__init__(name, size, count)
        self.missing = MISSING_SIGNED[size]

    def get(self, handle):

        count = evaluate(self.count, handle)
        assert count == 1

        sign = 1
        result = 0
        for i in range(0, self.size):
            n = int(handle._buffer[self.offset + i])
            if i == 0:
                if n >= 128:
                    sign = -1
                    n -= 128
            result = result * 256 + n

        result = result * sign

        return None if result == self.missing else result


ibm = [1.0] * 128
e = 1
for i in range(1, 58):
    e *= 16.0
    ibm[i + 70] = e
e = 1
for i in range(1, 71):
    e /= 16.0
    ibm[70 - i] = e


class Ibmfloat(Unsigned):

    def __init__(self, name, size, count=1):
        super().__init__(name, size, count)

    def get(self, handle):
        assert self.count == 1

        x = super().get(handle)
        if x is None:
           return None

        s = x & 0x80000000
        c = (x & 0x7f000000) >> 24
        m = (x & 0x00ffffff)

        if c == 0 and m <= 1:
            return 0

        val = m * ibm[c]
        if s:
            val = -val

        return val


class Ieeefloat(DataAccessor):

    def __init__(self, name, size, count=1):
        super().__init__(name, size, count)

    def get(self, handle):
        count = evaluate(self.count, handle)
        assert self.size in (4, 8)
        values = np.frombuffer(handle._buffer[self.offset:], dtype=np.dtype('>f%d' % (self.size,)), count=count)
        if count == 1:
            return values[0]
        else:
            return values


class Bytes(DataAccessor):
    def __init__(self, name, size):
        super().__init__(name, size)
