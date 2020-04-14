import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('bitsPerValue', 1))
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
    h.add(_.Constant('PUnset', -32767))
    h.add(_.Unsigned('N', 2))
    h.add(_.Signed('P', 2))
    h.add(_.Unsigned('JS', 1))
    h.add(_.Unsigned('KS', 1))
    h.add(_.Unsigned('MS', 1))
    h.alias('subSetJ', 'JS')
    h.alias('subSetK', 'KS')
    h.alias('subSetM', 'MS')
    h.add(_.Constant('GRIBEXShBugPresent', 1))

    if h._gribex_mode_on():
        h.add(_.Transient('computeLaplacianOperator', 0))
    else:
        h.add(_.Transient('computeLaplacianOperator', 1))

    h.add(_.Scale('laplacianOperator', _.Get('P'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateLaplacian')))
    h.alias('data.laplacianOperator', 'laplacianOperator')
    h.add(_.Evaluate('laplacianOperatorIsSet', _.And((_.Get('P') != _.Get('PUnset')), _.Not(_.Get('computeLaplacianOperator')))))

    if h.get_l('localUsePresent'):

        if h._changed('localDefinitionNumber'):
            h.add(_.Transient('TS', 0))
            h.add(_.Spectral_truncation('TScalc', _.Get('JS'), _.Get('KS'), _.Get('MS'), _.Get('TS')))
            h.add(_.Octect_number('Nassigned', _.Get('N'), (4 * _.Get('TScalc'))))


    h.add(_.Position('offsetBeforeData'))
    h.add(_.Data_g1complex_packing('values', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('GRIBEXShBugPresent'), _.Get('ieeeFloats'), _.Get('laplacianOperatorIsSet'), _.Get('laplacianOperator'), _.Get('subSetJ'), _.Get('subSetK'), _.Get('subSetM'), _.Get('pentagonalResolutionParameterJ'), _.Get('pentagonalResolutionParameterK'), _.Get('pentagonalResolutionParameterM'), _.Get('halfByte'), _.Get('N'), _.Get('packingType'), _.Get('spectral_ieee'), _.Get('precision')))
    h.add(_.Data_sh_packed('packedValues', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('GRIBEXShBugPresent'), _.Get('ieeeFloats'), _.Get('laplacianOperatorIsSet'), _.Get('laplacianOperator'), _.Get('subSetJ'), _.Get('subSetK'), _.Get('subSetM'), _.Get('pentagonalResolutionParameterJ'), _.Get('pentagonalResolutionParameterK'), _.Get('pentagonalResolutionParameterM')))
    h.alias('data.packedValues', 'packedValues')
    h.add(_.Data_sh_unpacked('unpackedValues', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('GRIBEXShBugPresent'), _.Get('ieeeFloats'), _.Get('laplacianOperatorIsSet'), _.Get('laplacianOperator'), _.Get('subSetJ'), _.Get('subSetK'), _.Get('subSetM'), _.Get('pentagonalResolutionParameterJ'), _.Get('pentagonalResolutionParameterK'), _.Get('pentagonalResolutionParameterM')))
    h.alias('data.unpackedValues', 'unpackedValues')
    h.add(_.Simple_packing_error('packingError', _.Get('bitsPerValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ibm')))
    h.add(_.Simple_packing_error('unpackedError', _.Get('zero'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ibm')))
    h.add(_.G1number_of_coded_values_sh_complex('numberOfCodedValues', _.Get('bitsPerValue'), _.Get('offsetBeforeData'), _.Get('offsetAfterData'), _.Get('halfByte'), _.Get('numberOfValues'), _.Get('subSetJ'), _.Get('subSetK'), _.Get('subSetM')))
    _.Template('common/statistics_spectral.def').load(h)
