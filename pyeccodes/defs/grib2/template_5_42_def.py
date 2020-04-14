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
    h.add(_.Codetable('typeOfOriginalFieldValues', 1, "5.1.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('ccsdsFlags', 1))
    h.alias('ccsdsCompressionOptionsMask', 'ccsdsFlags')
    h.add(_.Bit('AEC_DATA_SIGNED_OPTION_MASK', _.Get('ccsdsFlags'), 0))
    h.add(_.Bit('AEC_DATA_3BYTE_OPTION_MASK', _.Get('ccsdsFlags'), 1))
    h.add(_.Bit('AEC_DATA_MSB_OPTION_MASK', _.Get('ccsdsFlags'), 2))
    h.add(_.Bit('AEC_DATA_PREPROCESS_OPTION_MASK', _.Get('ccsdsFlags'), 3))
    h.add(_.Bit('AEC_RESTRICTED_OPTION_MASK', _.Get('ccsdsFlags'), 4))
    h.add(_.Bit('AEC_PAD_RSI_OPTION_MASK', _.Get('ccsdsFlags'), 5))
    h.add(_.Unsigned('ccsdsBlockSize', 1))
    h.add(_.Unsigned('ccsdsRsi', 2))
    h.alias('referenceSampleInterval', 'ccsdsRsi')
