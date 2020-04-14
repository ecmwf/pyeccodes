# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .expression import evaluate
from .data import Unsigned
from .base import NoSize


def g1_message_size(handle, totalLength, section4Length, section4Offset):

    totalLength = evaluate(totalLength, handle, 'r')
    section4Length = evaluate(section4Length, handle, 'r')

    if section4Length < 120 and (totalLength & 0x800000):

        totalLength &= 0x7fffff
        totalLength *= 120
        totalLength -= section4Length
        totalLength += 4

        section4Length = totalLength - section4Offset - 4

    return (totalLength, section4Length)


class G1_message_length(Unsigned):

    def __init__(self, name, length, section4Length):
        super().__init__(name, length)
        self.section4Length = section4Length

    def get_r(self, handle):  # 'r' is for raw
        return super().get(handle)

    def get(self, handle):
        (totalLength, section4Length) = g1_message_size(handle,
                                                        super().get(handle),
                                                        self.section4Length,
                                                        0)
        return totalLength


class G1_section4_length(Unsigned):

    def __init__(self, name, size, totalLength):
        super().__init__(name, size)
        self.size = size
        self.totalLength = totalLength

    def get_r(self, handle):  # 'r' is for raw
        return super().get(handle)

    def get(self, handle):
        (totalLength, section4Length) = g1_message_size(handle,
                                                        self.totalLength,
                                                        super().get(handle),
                                                        self.offset)
        return section4Length


class G1_half_byte_codeflag(Unsigned):

    def __init__(self, name):
        super().__init__(name, 1)

    def get(self, handle):
        return super().get(handle) & 0xf

    @property
    def length(self):
        return 0


class G1date(NoSize):

    def __init__(self, name, century, year, month, day):
        super().__init__(name)
        self.century = century
        self.year = year
        self.month = month
        self.day = day

    def get(self, handle):
        century = evaluate(self.century, handle)
        year = evaluate(self.year, handle)
        month = evaluate(self.month, handle)
        day = evaluate(self.day, handle)
        return ((century - 1) * 100 + year) * 10000 + month * 100 + day


class Mars_param(NoSize):

    def __init__(self, name, paramId, table, param):
        super().__init__(name)
        self.paramId = paramId
        self.table = table
        self.param = param

    def get(self, handle):
        return "%s.%s" % (evaluate(self.param, handle), evaluate(self.table, handle))


class G1step_range(NoSize):

    def __init__(self, name,
                 p1,
                 p2,
                 timeRangeIndicator,
                 unitOfTimeRange,
                 stepUnits,
                 stepType):
        super().__init__(name)
        self.p1 = p1
        self.p2 = p2
        self.timeRangeIndicator = timeRangeIndicator
        self.unitOfTimeRange = unitOfTimeRange
        self.stepUnits = stepUnits
        self.stepType = stepType

    def get(self, handle):
        p1 = evaluate(self.p1, handle)
        p2 = evaluate(self.p2, handle)
        timeRangeIndicator = evaluate(self.timeRangeIndicator, handle)
        unitOfTimeRange = evaluate(self.unitOfTimeRange, handle)
        stepUnits = evaluate(self.stepUnits, handle)
        stepType = evaluate(self.stepType, handle)

        assert unitOfTimeRange == 1
        if stepType == 'instant':
            # assert p1 <= p2, (stepType, p1, p2)
            return (p1, p1)

        return (p1, p2)

