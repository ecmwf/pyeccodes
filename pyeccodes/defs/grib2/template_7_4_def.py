import pyeccodes.accessors as _


def load(h):

    h.add(_.Data_raw_packing('codedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('numberOfValues'), _.Get('precision')))
    h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor'), _.Get('numberOfDataPoints'), _.Get('numberOfValues')))
    h.alias('data.packedValues', 'codedValues')
    _.Template('common/statistics_grid.def').load(h)
