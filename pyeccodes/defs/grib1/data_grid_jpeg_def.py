import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('bitsPerValue', 1))
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
    h.add(_.Constant('constantFieldHalfByte', 8))
    h.add(_.Position('offsetBeforeData'))

    if (h.get_l('bitmapPresent') or not (h.get_l('GDSPresent'))):
        h.add(_.Constant('bitMapIndicator', 0))
        h.add(_.Data_g1simple_packing('codedValues', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision')))
        h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor')))
        h.alias('data.packedValues', 'codedValues')
    else:
        h.add(_.Constant('bitMapIndicator', 255))
        h.add(_.Data_g1simple_packing('values', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision')))
        h.alias('data.packedValues', 'values')

    h.add(_.Number_of_coded_values('numberOfCodedValues', _.Get('bitsPerValue'), _.Get('offsetBeforeData'), _.Get('offsetAfterData'), _.Get('halfByte'), _.Get('numberOfValues')))
    h.add(_.Simple_packing_error('packingError', _.Get('bitsPerValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ibm')))
    h.add(_.Simple_packing_error('unpackedError', _.Get('zero'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ieee')))
    _.Template('common/statistics_grid.def').load(h)
