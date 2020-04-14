import pyeccodes.accessors as _


def load(h):

    h.add(_.Ieeefloat('referenceValue', 4))
    h.add(_.Reference_value_error('referenceValueError', _.Get('referenceValue'), _.Get('ieee')))
    h.add(_.Signed('binaryScaleFactor', 2))
    h.add(_.Signed('decimalScaleFactor', 2))
    h.add(_.Transient('optimizeScaleFactor', 0))
    h.add(_.Unsigned('bitsPerValue', 1))

    if h.get_l('bitsPerValue'):
        h.add(_.Unsigned('widthOfFirstOrderValues', 1))
        h.add(_.Unsigned('numberOfGroups', 4))
        h.add(_.Unsigned('numberOfSecondOrderPackedValues', 4))
        h.add(_.Unsigned('widthOfWidths', 1))
        h.add(_.Unsigned('widthOfLengths', 1))
        h.add(_.Unsigned('orderOfSPD', 1))

        if h.get_l('orderOfSPD'):
            h.add(_.Unsigned('widthOfSPD', 1))
            h.add(_.Spd('SPD', _.Get('widthOfSPD'), _.Get('orderOfSPD')))


