import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('bitsPerValue', 1))
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
    h.add(_.Ibmfloat('realPart', 4))
    h.add(_.Position('offsetBeforeData'))
    h.add(_.Transient('P', 0))

    if h._gribex_mode_on():
        h.add(_.Transient('computeLaplacianOperator', 0))
    else:
        h.add(_.Transient('computeLaplacianOperator', 1))

    h.add(_.Data_g1simple_packing('codedValues', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte')))
    h.add(_.Data_g1shsimple_packing('values', _.Get('codedValues'), _.Get('realPart')))
    h.alias('data.packedValues', 'values')
    h.add(_.G1number_of_coded_values_sh_simple('numberOfCodedValues', _.Get('bitsPerValue'), _.Get('offsetBeforeData'), _.Get('offsetAfterData'), _.Get('halfByte'), _.Get('numberOfValues')))
    _.Template('common/statistics_spectral.def').load(h)
