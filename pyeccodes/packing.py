# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .base import Accessor
from .expression import evaluate
import numpy as np
import math

from .data import Unsigned, Signed


class PackedData(Accessor):

    def __init__(self, name,
                 sectionLength,
                 offsetBeforeData,
                 offsetSection):

        super().__init__(name)

        self.sectionLength = sectionLength
        self.offsetSection = offsetSection
        self.offsetBeforeData = offsetBeforeData

    @property
    def length(self):
        sectionLength = evaluate(self.sectionLength, self.handle)
        offsetBeforeData = evaluate(self.offsetBeforeData, self.handle)
        offsetSection = evaluate(self.offsetSection, self.handle)
        return sectionLength - (offsetBeforeData - offsetSection)


MASK = (0x0, 0x1, 0x3, 0x7, 0xf, 0x1f, 0x3f, 0x7f, 0xff)


def unpack(data, bitsPerValue, numberOfCodedValues, skipBits=0):

    if bitsPerValue == 0:
        return np.zeros(numberOfCodedValues)

    if bitsPerValue in (8, 16, 32) and skipBits == 0:
        values = np.frombuffer(data, dtype=np.dtype('>u%d' % (bitsPerValue // 8,)), count=numberOfCodedValues)
    else:
        assert skipBits < 8
        values = np.empty(numberOfCodedValues, dtype=np.dtype('u4'))
        acc = 0
        bits = 0
        j = 0

        for i in range(0, numberOfCodedValues):

            while bits < bitsPerValue:
                acc <<= 8
                if skipBits:
                    acc |= data[j] & (0xff >> skipBits)
                    j += 1
                    bits += 8 - skipBits
                    skipBits = 0
                else:
                    acc |= data[j]
                    j += 1
                    bits += 8

            shift = bits - bitsPerValue
            values[i] = acc >> shift

            acc = acc & MASK[shift]
            bits -= bitsPerValue

    return values.astype('u4')


class SimplePacking(PackedData):

    def __init__(self, name,
                 sectionLength,
                 offsetBeforeData,
                 offsetSection,
                 unitsFactor,
                 unitsBias,
                 changingPrecision,
                 numberOfCodedValues,
                 bitsPerValue,
                 referenceValue,
                 binaryScaleFactor,
                 decimalScaleFactor,
                 optimizeScaleFactor,
                 halfByte=None,
                 packingType=None,
                 grid_ieee=None,
                 precision=None):
        super().__init__(name, sectionLength, offsetBeforeData, offsetSection)

        self.bitsPerValue = bitsPerValue
        self.referenceValue = referenceValue
        self.binaryScaleFactor = binaryScaleFactor
        self.decimalScaleFactor = decimalScaleFactor
        self.numberOfCodedValues = numberOfCodedValues

    def get(self, handle):
        bitsPerValue = evaluate(self.bitsPerValue, handle)
        referenceValue = evaluate(self.referenceValue, handle)
        binaryScaleFactor = evaluate(self.binaryScaleFactor, handle)
        decimalScaleFactor = evaluate(self.decimalScaleFactor, handle)
        numberOfCodedValues = evaluate(self.numberOfCodedValues, handle)

        if referenceValue is None:
            return None

        if bitsPerValue == 0:
            values = np.empty(numberOfCodedValues)
            values[:] = referenceValue
            return values

        data = handle._buffer[self.offset:]
        values = unpack(data, bitsPerValue, numberOfCodedValues)

        values = ((values * math.pow(2, binaryScaleFactor)) + referenceValue) * math.pow(10, -decimalScaleFactor)
        return values


class Data_g1simple_packing(SimplePacking):
    pass


class Data_g2simple_packing(SimplePacking):
    pass


class ComplexPacking(PackedData):

    def __init__(self, name,
                 sectionLength,
                 offsetBeforeData,
                 offsetSection,
                 unitsFactor,
                 unitsBias,
                 changingPrecision,
                 numberOfValues,
                 bitsPerValue,
                 referenceValue,
                 binaryScaleFactor,
                 decimalScaleFactor,
                 optimizeScaleFactor,
                 GRIBEXShBugPresent,
                 unpackedSubsetPrecision,
                 laplacianOperatorIsSet,
                 laplacianOperator,
                 subSetJ,
                 subSetK,
                 subSetM,
                 pentagonalResolutionParameterJ,
                 pentagonalResolutionParameterK,
                 pentagonalResolutionParameterM,
                 halfByte,  # numberOfValues for grib2
                 N=None,
                 packingType=None,
                 spectra_ieee=None,
                 precision=None):
        super().__init__(name, sectionLength, offsetBeforeData, offsetSection)


class Data_g1complex_packing(ComplexPacking):
    pass


class Data_g2complex_packing(ComplexPacking):
    pass


class SecondOrderPacking1(PackedData):

    def __init__(self, name,
                 sectionLength,
                 offsetBeforeData,
                 offsetSection,
                 unitsFactor,
                 unitsBias,
                 changingPrecision,
                 numberOfCodedValues,
                 bitsPerValue,
                 referenceValue,
                 binaryScaleFactor,
                 decimalScaleFactor,
                 optimizeScaleFactor,
                 halfByte,
                 packingType,
                 grid_ieee,
                 precision,
                 widthOfFirstOrderValues,
                 firstOrderValues,
                 N1,
                 N2,
                 numberOfGroups,
                 numberOfGroups_again,
                 numberOfSecondOrderPackedValues,
                 keyNotPresent,
                 groupWidths,
                 widthOfWidths,
                 groupLengths,
                 widthOfLengths=None,
                 NL=None,
                 SPD=None,
                 widthOfSPD=None,
                 orderOfSPD=None,
                 numberOfPoints=None):
        super().__init__(name, sectionLength, offsetBeforeData, offsetSection)


class Data_g1second_order_general_extended_packing(SecondOrderPacking1):
    pass


class Data_g1second_order_row_by_row_packing(SecondOrderPacking1):
    pass


class Data_g1second_order_general_packing(SecondOrderPacking1):
    pass


class SecondOrderPacking2(PackedData):
    def __init__(self, name,
                 sectionLength,
                 offsetBeforeData,
                 offsetSection,
                 numberOfValues,
                 bitsPerValue,
                 referenceValue,
                 binaryScaleFactor,
                 decimalScaleFactor,
                 typeOfOriginalFieldValues,
                 groupSplittingMethodUsed,
                 missingValueManagementUsed,
                 primaryMissingValueSubstitute,
                 secondaryMissingValueSubstitute,
                 numberOfGroupsOfDataValues,
                 referenceForGroupWidths,
                 numberOfBitsUsedForTheGroupWidths,
                 referenceForGroupLengths,
                 lengthIncrementForTheGroupLengths,
                 trueLengthOfLastGroup,
                 numberOfBitsForScaledGroupLengths,
                 orderOfSpatialDifferencing,
                 numberOfOctetsExtraDescriptors):
        super().__init__(name, sectionLength, offsetBeforeData, offsetSection)
        self.bitsPerValue = bitsPerValue
        self.binaryScaleFactor = binaryScaleFactor
        self.referenceValue = referenceValue
        self.numberOfValues = numberOfValues
        self.decimalScaleFactor = decimalScaleFactor
        self.numberOfGroupsOfDataValues = numberOfGroupsOfDataValues
        self.orderOfSpatialDifferencing = orderOfSpatialDifferencing
        self.numberOfOctetsExtraDescriptors = numberOfOctetsExtraDescriptors
        self.numberOfBitsUsedForTheGroupWidths = numberOfBitsUsedForTheGroupWidths
        self.numberOfBitsForScaledGroupLengths = numberOfBitsForScaledGroupLengths
        self.missingValueManagementUsed = missingValueManagementUsed
        self.trueLengthOfLastGroup = trueLengthOfLastGroup
        self.lengthIncrementForTheGroupLengths = lengthIncrementForTheGroupLengths
        self.referenceForGroupLengths = referenceForGroupLengths
        self.referenceForGroupWidths = referenceForGroupWidths


class Data_g22order_packing(SecondOrderPacking2):

    def get(self, handle):

        bitsPerValue = evaluate(self.bitsPerValue, handle)
        binaryScaleFactor = evaluate(self.binaryScaleFactor, handle)
        referenceValue = evaluate(self.referenceValue, handle)
        decimalScaleFactor = evaluate(self.decimalScaleFactor, handle)

        numberOfValues = evaluate(self.numberOfValues, handle)
        numberOfGroupsOfDataValues = evaluate(self.numberOfGroupsOfDataValues, handle)
        orderOfSpatialDifferencing = evaluate(self.orderOfSpatialDifferencing, handle)
        numberOfOctetsExtraDescriptors = evaluate(self.numberOfOctetsExtraDescriptors, handle)
        numberOfBitsUsedForTheGroupWidths = evaluate(self.numberOfBitsUsedForTheGroupWidths, handle)
        numberOfBitsForScaledGroupLengths = evaluate(self.numberOfBitsForScaledGroupLengths, handle)
        missingValueManagementUsed = evaluate(self.missingValueManagementUsed, handle)
        trueLengthOfLastGroup = evaluate(self.trueLengthOfLastGroup, handle)

        lengthIncrementForTheGroupLengths = evaluate(self.lengthIncrementForTheGroupLengths, handle)
        referenceForGroupLengths = evaluate(self.referenceForGroupLengths, handle)
        referenceForGroupWidths = evaluate(self.referenceForGroupWidths, handle)

        # TODO: suppet missing values
        assert missingValueManagementUsed == 0, "Second order packing missing values management not implemented"

        start = self.offset

        if orderOfSpatialDifferencing:
            # This should have been in the def file
            tmp = Unsigned(None, numberOfOctetsExtraDescriptors, orderOfSpatialDifferencing)
            tmp.offset = start
            extras = tmp.get(handle)

            start += orderOfSpatialDifferencing * numberOfOctetsExtraDescriptors

            tmp = Signed(None, numberOfOctetsExtraDescriptors)
            tmp.offset = start
            bias = tmp.get(handle)

            start += numberOfOctetsExtraDescriptors

        referenceValues = unpack(handle._buffer[start:], bitsPerValue, numberOfGroupsOfDataValues)

        start += (numberOfGroupsOfDataValues * bitsPerValue + 7) // 8
        widths = unpack(handle._buffer[start:], numberOfBitsUsedForTheGroupWidths, numberOfGroupsOfDataValues)
        widths = widths + referenceForGroupWidths

        start += (numberOfGroupsOfDataValues * numberOfBitsUsedForTheGroupWidths + 7) // 8
        lengths = unpack(handle._buffer[start:], numberOfBitsForScaledGroupLengths, numberOfGroupsOfDataValues)

        lengths = lengths * lengthIncrementForTheGroupLengths + referenceForGroupLengths

        lengths[numberOfGroupsOfDataValues - 1] = trueLengthOfLastGroup

        start += (numberOfGroupsOfDataValues * numberOfBitsForScaledGroupLengths + 7) // 8

        values = np.zeros(numberOfValues, dtype='i4')
        index = 0

        bit = 0
        j = 0
        for i in range(0, numberOfGroupsOfDataValues):
            data = handle._buffer[start + bit // 8:]
            group = unpack(data, widths[i], lengths[i], bit % 8) + referenceValues[i]
            values[index:index + lengths[i]] = group

            index += lengths[i]
            advance = lengths[i] * widths[i]
            bit += advance

        if orderOfSpatialDifferencing:
            assert orderOfSpatialDifferencing in (1, 2)

            assert orderOfSpatialDifferencing == 2

            if orderOfSpatialDifferencing == 2:
                p0 = extras[0]
                p1 = extras[1]
                j = 0

                while j < numberOfValues:
                    if np.isnan(values[j]):
                        j += 1
                    else:
                        values[j] = p0
                        j += 1
                        break

                while j < numberOfValues:
                    if np.isnan(values[j]):
                        j += 1
                    else:
                        values[j] = p1
                        j += 1
                        break

                while j < numberOfValues:
                    if not np.isnan(values[j]):
                        values[j] += 2 * p1 - p0 + bias
                        p0 = p1
                        p1 = values[j]
                    j += 1

        values = ((values * math.pow(2, binaryScaleFactor)) + referenceValue) * math.pow(10, -decimalScaleFactor)
        return values


class Data_jpeg2000_packing(PackedData):

    def __init__(self, name,
                 sectionLength,
                 offsetBeforeData,
                 offsetSection,
                 unitsFactor,
                 unitsBias,
                 changingPrecision,
                 numberOfCodedValues,
                 bitsPerValue,
                 referenceValue,
                 binaryScaleFactor,
                 decimalScaleFactor,
                 optimizeScaleFactor,
                 typeOfCompressionUsed,
                 targetCompressionRatio,
                 Nx,
                 Ny,
                 interpretationOfNumberOfPoints,
                 numberOfDataPoints,
                 scanningMode):
        super().__init__(name,
                         sectionLength,
                         offsetBeforeData,
                         offsetSection)

        self.bitsPerValue = bitsPerValue
        self.referenceValue = referenceValue
        self.binaryScaleFactor = binaryScaleFactor
        self.decimalScaleFactor = decimalScaleFactor
        self.numberOfCodedValues = numberOfCodedValues
        self.unitsFactor = unitsFactor
        self.unitsBias = unitsBias

    def get(self, handle):
        from io import BytesIO
        try:
            from PIL import Image  # pip3 install pillow
        except ModuleNotFoundError:
            raise NotImplementedError("Support for JPEG encoded GRIB requires the package 'pillow' to be installed")

        bitsPerValue = evaluate(self.bitsPerValue, handle)
        referenceValue = evaluate(self.referenceValue, handle)
        binaryScaleFactor = evaluate(self.binaryScaleFactor, handle)
        decimalScaleFactor = evaluate(self.decimalScaleFactor, handle)
        numberOfCodedValues = evaluate(self.numberOfCodedValues, handle)
        unitsFactor = evaluate(self.unitsFactor, handle)
        unitsBias = evaluate(self.unitsBias, handle)

        if bitsPerValue == 0:
            values = np.empty(numberOfCodedValues)
            values[:] = referenceValue
            return values

        data = handle._buffer[self.offset:]
        img = Image.open(BytesIO(data))
        values = np.array(img).flatten()

        assert numberOfCodedValues == len(values)
        assert values.dtype in (np.uint8, np.uint16)

        if values.dtype == np.uint8:
            width = 8
        if values.dtype == np.uint16:
            width = 16

        # There is a bug in PIL that returns np.uint8 for fields encoded
        # with 9 bits

        assert bitsPerValue <= width

        shift = width - bitsPerValue
        if shift > 0:
            values = np.right_shift(values, shift)

        values = ((values * math.pow(2, binaryScaleFactor)) + referenceValue) * math.pow(10, -decimalScaleFactor)

        if unitsFactor != 1:
            values *= values

        if unitsBias != 0:
            values += unitsBias

        return values


class Data_raw_packing(PackedData):

    def __init__(self, name,
                 sectionLength,
                 offsetBeforeData,
                 offsetSection,
                 numberOfValues,
                 precision):
        super().__init__(name, sectionLength, offsetBeforeData, offsetSection)
