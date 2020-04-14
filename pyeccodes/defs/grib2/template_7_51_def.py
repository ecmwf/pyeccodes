import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXShBugPresent', 0))
    h.add(_.Constant('sphericalHarmonics', 1))
    h.add(_.Constant('complexPacking', 1))
    h.add(_.Data_g2complex_packing('codedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('GRIBEXShBugPresent'), _.Get('unpackedSubsetPrecision'), _.Get('laplacianOperatorIsSet'), _.Get('laplacianOperator'), _.Get('subSetJ'), _.Get('subSetK'), _.Get('subSetM'), _.Get('pentagonalResolutionParameterJ'), _.Get('pentagonalResolutionParameterK'), _.Get('pentagonalResolutionParameterM'), _.Get('numberOfValues')))
    h.add(_.Data_sh_packed('packedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('GRIBEXShBugPresent'), _.Get('unpackedSubsetPrecision'), _.Get('laplacianOperatorIsSet'), _.Get('laplacianOperator'), _.Get('subSetJ'), _.Get('subSetK'), _.Get('subSetM'), _.Get('pentagonalResolutionParameterJ'), _.Get('pentagonalResolutionParameterK'), _.Get('pentagonalResolutionParameterM')))
    h.alias('data.packedValues', 'packedValues')
    h.add(_.Data_sh_unpacked('unpackedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('GRIBEXShBugPresent'), _.Get('unpackedSubsetPrecision'), _.Get('laplacianOperatorIsSet'), _.Get('laplacianOperator'), _.Get('subSetJ'), _.Get('subSetK'), _.Get('subSetM'), _.Get('pentagonalResolutionParameterJ'), _.Get('pentagonalResolutionParameterK'), _.Get('pentagonalResolutionParameterM')))
    h.alias('data.unpackedValues', 'unpackedValues')
    h.add(_.Simple_packing_error('packingError', _.Get('bitsPerValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ieee')))
    h.add(_.Simple_packing_error('unpackedError', _.Get('zero'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ieee')))
    h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor'), _.Get('numberOfDataPoints'), _.Get('numberOfValues')))
    _.Template('common/statistics_spectral.def').load(h)
