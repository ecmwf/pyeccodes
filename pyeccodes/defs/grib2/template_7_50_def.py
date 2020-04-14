import pyeccodes.accessors as _


def load(h):

    h.add(_.Transient('numberOfValues', ((_.Get('J') + 1) * (_.Get('J') + 2))))
    h.add(_.Transient('numberOfPackedValues', (_.Get('numberOfValues') - 1)))
    h.add(_.Transient('numberOfValues', ((_.Get('J') + 1) * (_.Get('J') + 2))))
    h.add(_.Transient('numberOfPackedValues', (_.Get('numberOfValues') - 1)))
    h.add(_.Data_g2simple_packing('codedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfPackedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor')))
    h.add(_.Data_g2shsimple_packing('values', _.Get('codedValues'), _.Get('realPartOf00'), _.Get('numberOfValues')))
    h.add(_.Simple_packing_error('packingError', _.Get('bitsPerValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ieee')))
    h.add(_.Simple_packing_error('unpackedError', _.Get('zero'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ieee')))
    h.alias('x.packedValues', 'values')
    _.Template('common/statistics_spectral.def').load(h)
