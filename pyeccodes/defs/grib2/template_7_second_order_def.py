import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetBeforeData'))
    h.add(_.Constant('orderOfSpatialDifferencing', 0))
    h.add(_.Constant('numberOfOctetsExtraDescriptors', 0))
    h.add(_.Data_g2second_order_packing('codedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision'), _.Get('widthOfFirstOrderValues'), _.Get('firstOrderValues'), _.Get('N1'), _.Get('N2'), _.Get('numberOfGroups'), _.Get('codedNumberOfGroups'), _.Get('numberOfSecondOrderPackedValues'), _.Get('extraValues'), _.Get('groupWidths'), _.Get('widthOfWidths'), _.Get('groupLengths'), _.Get('widthOfLengths'), _.Get('NL'), _.Get('SPD'), _.Get('widthOfSPD'), _.Get('orderOfSPD'), _.Get('numberOfPoints')))
    h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor'), _.Get('numberOfDataPoints'), _.Get('numberOfValues')))
    h.alias('data.packedValues', 'codedValues')
    _.Template('common/statistics_grid.def').load(h)
