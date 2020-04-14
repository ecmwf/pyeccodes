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
    h.add(_.Transient('computeLaplacianOperator', 1))
    h.add(_.Codetable('biFourierSubTruncationType', 1, "5.25.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('biFourierPackingModeForAxes', 1, "5.26.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Constant('laplacianScalingFactorUnset', -2147483647))
    h.add(_.Signed('laplacianScalingFactor', 4))
    h.add(_.Scale('laplacianOperator', _.Get('laplacianScalingFactor'), _.Get('one'), _.Get('million'), _.Get('truncateLaplacian')))
    h.alias('data.laplacianOperator', 'laplacianOperator')
    h.add(_.Evaluate('laplacianOperatorIsSet', _.And((_.Get('laplacianScalingFactor') != _.Get('laplacianScalingFactorUnset')), _.Not(_.Get('computeLaplacianOperator')))))
    h.add(_.Unsigned('biFourierResolutionSubSetParameterN', 2))
    h.add(_.Unsigned('biFourierResolutionSubSetParameterM', 2))
    h.add(_.Unsigned('totalNumberOfValuesInUnpackedSubset', 4))
    h.add(_.Codetable('unpackedSubsetPrecision', 1, "5.7.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('precisionOfTheUnpackedSubset', 'unpackedSubsetPrecision')
