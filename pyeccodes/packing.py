# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .base import Accessor
from .expression import evaluate
import numpy as np
import math


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

        # print("=========", self.sectionLength, sectionLength, offsetBeforeData, offsetSection)

        return sectionLength - (offsetBeforeData - offsetSection)


MASK = (0x0, 0x1, 0x3, 0x7, 0xf, 0x1f, 0x3f, 0x7f, 0xff)


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

        data = handle._buffer[self.offset:]
        if bitsPerValue in (8, 16, 32):
            values = np.frombuffer(data, dtype=np.dtype('>i%d' % (bitsPerValue // 8)), count=numberOfCodedValues)
        else:
            values = np.empty(numberOfCodedValues, dtype=np.dtype('i4'))
            acc = 0
            bits = 0
            j = 0
            for i in range(0, numberOfCodedValues):

                while bits < bitsPerValue:
                    acc <<= 8
                    acc |= data[j]
                    j += 1
                    bits += 8

                shift = bits - bitsPerValue
                values[i] = acc >> shift

                acc = acc & MASK[shift]
                bits -= bitsPerValue

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


class Data_g22order_packing(SecondOrderPacking2):
    pass


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
        super().__init__(name, sectionLength, offsetBeforeData, offsetSection)


class Data_raw_packing(PackedData):

    def __init__(self, name,
                 sectionLength,
                 offsetBeforeData,
                 offsetSection,
                 numberOfValues,
                 precision):
        super().__init__(name, sectionLength, offsetBeforeData, offsetSection)
