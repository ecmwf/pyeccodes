import pyeccodes.accessors as _


def load(h):

    h.add(_.Ieeefloat('referenceValue', 4))
    h.add(_.Reference_value_error('referenceValueError', _.Get('referenceValue'), _.Get('ieee')))
    h.add(_.Signed('binaryScaleFactor', 2))
    h.add(_.Signed('decimalScaleFactor', 2))
    h.add(_.Transient('optimizeScaleFactor', 0))
    h.add(_.Unsigned('bitsPerValue', 1))
    h.alias('numberOfBits', 'bitsPerValue')
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
    h.add(_.Codetable('typeOfOriginalFieldValues', 1, "5.1.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('groupSplittingMethodUsed', 1, "5.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('missingValueManagementUsed', 1, "5.5.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('primaryMissingValueSubstitute', 4))
    h.add(_.Unsigned('secondaryMissingValueSubstitute', 4))
    h.add(_.Unsigned('numberOfGroupsOfDataValues', 4))
    h.alias('NG', 'numberOfGroupsOfDataValues')
    h.add(_.Unsigned('referenceForGroupWidths', 1))
    h.add(_.Unsigned('numberOfBitsUsedForTheGroupWidths', 1))
    h.add(_.Unsigned('referenceForGroupLengths', 4))
    h.add(_.Unsigned('lengthIncrementForTheGroupLengths', 1))
    h.add(_.Unsigned('trueLengthOfLastGroup', 4))
    h.add(_.Unsigned('numberOfBitsForScaledGroupLengths', 1))
    h.alias('numberOfBitsUsedForTheScaledGroupLengths', 'numberOfBitsForScaledGroupLengths')
