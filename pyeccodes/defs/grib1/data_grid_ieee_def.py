import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('bitsPerValue', 1))
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
    h.add(_.Codetable('precision', 1, "grib1/precision.table"))
    h.add(_.Position('offsetBeforeData'))

    if (h.get_l('bitmapPresent') or not (h.get_l('GDSPresent'))):
        h.add(_.Constant('bitMapIndicator', 0))
        h.add(_.Data_raw_packing('codedValues', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('numberOfCodedValues'), _.Get('precision')))
        h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor')))
        h.alias('data.packedValues', 'codedValues')
    else:
        h.add(_.Constant('bitMapIndicator', 255))
        h.add(_.Data_raw_packing('values', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('numberOfCodedValues'), _.Get('precision')))
        h.alias('data.packedValues', 'values')

    h.add(_.Number_of_values_data_raw_packing('numberOfCodedValues', _.Get('values'), _.Get('precision')))
    _.Template('common/statistics_grid.def').load(h)
