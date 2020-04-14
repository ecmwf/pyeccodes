# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .base import NoSize, Accessor
from .expression import evaluate

import numpy as np


class Count_missing(NoSize):

    def __init__(self, name, bitmap, unusedBitsInBitmap, numberOfDataPoints):
        super().__init__(name)
        self.bitmap = bitmap
        self.unusedBitsInBitmap = unusedBitsInBitmap
        self.numberOfDataPoints = numberOfDataPoints

    def get(self, handle):
        bitmap = evaluate(self.bitmap, handle)

        if bitmap is None:
            return 0

        return evaluate(self.numberOfDataPoints, handle) - int(bitmap.sum())


class GXbitmap(Accessor):

    def __init__(self, name,
                 tableReference,
                 missingValue,
                 offsetSection,
                 sectionLength,
                 numberOfUnusedBitsAtEndOfSection=0,
                 numberOfDataPoints=None):
        super().__init__(name)
        self.sectionLength = sectionLength
        self.offsetSection = offsetSection
        self.numberOfUnusedBitsAtEndOfSection = numberOfUnusedBitsAtEndOfSection
        self.numberOfDataPoints = numberOfDataPoints

    @property
    def length(self):
        sectionLength = evaluate(self.sectionLength, self.handle)
        offsetSection = evaluate(self.offsetSection, self.handle)
        return sectionLength - (self.offset - offsetSection)

    def get(self, handle):
        numberOfUnusedBitsAtEndOfSection = evaluate(self.numberOfUnusedBitsAtEndOfSection, handle)
        data = handle._buffer[self.offset:]
        values = np.frombuffer(data, dtype=np.uint8, count=self.length)
        values = np.unpackbits(values)
        if numberOfUnusedBitsAtEndOfSection:
            values = np.resize(values, self.length * 8 - numberOfUnusedBitsAtEndOfSection)
        if self.numberOfDataPoints:
            numberOfDataPoints = evaluate(self.numberOfDataPoints, handle)
            values = np.resize(values, numberOfDataPoints)
        return values


class G1bitmap(GXbitmap):

    def __init__(self, name,
                 tableReference,
                 missingValue,
                 offsetSection,
                 sectionLength,
                 numberOfUnusedBitsAtEndOfSection):
        super().__init__(name,
                         tableReference,
                         missingValue,
                         offsetSection,
                         sectionLength,
                         numberOfUnusedBitsAtEndOfSection=numberOfUnusedBitsAtEndOfSection)


class G2bitmap(GXbitmap):

    def __init__(self, name,
                 tableReference,
                 missingValue,
                 offsetSection,
                 sectionLength,
                 numberOfDataPoints):
        super().__init__(name,
                         tableReference,
                         missingValue,
                         offsetSection,
                         sectionLength,
                         numberOfDataPoints=numberOfDataPoints)


class Data_apply_bitmap(NoSize):

    def __init__(self, name, codedValues, bitmap, missingValue, binaryScaleFactor, numberOfDataPoints=None, numberOfValues=None):
        super().__init__(name)
        self.codedValues = codedValues
        self.bitmap = bitmap
        self.missingValue = missingValue
        self.binaryScaleFactor = binaryScaleFactor

    def get(self, handle):

        # print(self.bitmap)

        # TODO: grib2 alwats call apply_bitmap with bitmap undefined
        # if not handle._defined(self.bitmap):
        #     return evaluate(self.codedValues, handle)

        codedValues = evaluate(self.codedValues, handle)
        bitmap = evaluate(self.bitmap, handle)

        if bitmap is None:
            return codedValues

        if codedValues is None:
            return codedValues

        # missingValue = evaluate(self.missingValue, handle)
        missingValue = np.NaN

        values = np.empty(bitmap.shape)
        values[:] = missingValue

        j = 0
        for i in range(0, len(bitmap)):
            if bitmap[i]:
                values[i] = codedValues[j]
                j += 1

        return values
