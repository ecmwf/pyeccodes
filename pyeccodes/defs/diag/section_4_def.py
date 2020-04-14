import pyeccodes.accessors as _


def load(h):

    h.add(_.Section_length('section4Length', 3))
    h.add(_.Unsigned('reserved1', 1))
    h.add(_.Codeflag('missingDataFlag', 1, "grib1/1.table"))
    h.add(_.Unsigned('numberOfBytesPerInteger', 1))
    h.add(_.Unsigned('reserved', 2))
    h.add(_.Unsigned('numberOfCharacters', 3))
    h.alias('numberOfChars', 'numberOfCharacters')
    h.add(_.Unsigned('numberOfFloats', 3))
    h.add(_.Unsigned('numberOfIntegers', 3))
    h.alias('numberOfInts', 'numberOfIntegers')
    h.add(_.Unsigned('numberOfLogicals', 3))
    h.add(_.Unsigned('numberOfReservedBytes', 3))
    h.add(_.Unsigned('reserved', 4))
    h.add(_.Unsigned('reserved', 4))
    h.add(_.Unsigned('reserved', 1))
    h.add(_.Ibmfloat('floatValues', 4, _.Get('numberOfFloats')))
    h.alias('floatVal', 'floatValues')

    if h.get_l('numberOfIntegers'):
        h.add(_.Signed('integerValues', 4, _.Get('numberOfIntegers')))

    if h.get_l('numberOfCharacters'):
        h.add(_.StringUnsigned('charValues', 1, _.Get('numberOfCharacters')))

    h.add(_.Section_padding('padding'))
