import pyeccodes.accessors as _


def load(h):

    h.add(_.Transient('bitsPerValue', 0))
    h.add(_.Transient('referenceValue', 0))
    h.add(_.Transient('binaryScaleFactor', 0))
    h.add(_.Transient('decimalScaleFactor', 0))
    h.alias('numberOfBits', 'bitsPerValue')
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
    h.add(_.Codetable('precision', 1, "5.7.table", _.Get('masterDir'), _.Get('localDir')))
