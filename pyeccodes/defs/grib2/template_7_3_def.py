import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetBeforeData'))
    h.add(_.Data_g22order_packing('codedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('numberOfValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('typeOfOriginalFieldValues'), _.Get('groupSplittingMethodUsed'), _.Get('missingValueManagementUsed'), _.Get('primaryMissingValueSubstitute'), _.Get('secondaryMissingValueSubstitute'), _.Get('numberOfGroupsOfDataValues'), _.Get('referenceForGroupWidths'), _.Get('numberOfBitsUsedForTheGroupWidths'), _.Get('referenceForGroupLengths'), _.Get('lengthIncrementForTheGroupLengths'), _.Get('trueLengthOfLastGroup'), _.Get('numberOfBitsForScaledGroupLengths'), _.Get('orderOfSpatialDifferencing'), _.Get('numberOfOctetsExtraDescriptors')))
    h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor'), _.Get('numberOfDataPoints'), _.Get('numberOfValues')))
    h.alias('data.packedValues', 'codedValues')
    _.Template('common/statistics_grid.def').load(h)
