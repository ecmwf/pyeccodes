import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection3'))
    h.add(_.Section_length('section3Length', 3))
    h.add(_.Section_pointer('section3Pointer', _.Get('offsetSection3'), _.Get('section3Length'), 3))
    h.add(_.Unsigned('numberOfUnusedBitsAtEndOfSection3', 1))
    h.alias('unusedBitsInBitmap', 'numberOfUnusedBitsAtEndOfSection3')
    h.add(_.Unsigned('tableReference', 2))
    h.add(_.Position('offsetBeforeBitmap'))
    h.add(_.G1bitmap('bitmap', _.Get('tableReference'), _.Get('missingValue'), _.Get('offsetSection3'), _.Get('section3Length'), _.Get('numberOfUnusedBitsAtEndOfSection3')))
    h.alias('geography.bitmap', 'bitmap')
    h.add(_.Position('offsetAfterBitmap'))
    h.add(_.Padtoeven('padding_sec3_1', _.Get('offsetSection3'), _.Get('section3Length')))
    h.add(_.Section_padding('section3Padding'))
    h.add(_.Md5('md5Section3', _.Get('offsetSection3'), _.Get('section3Length')))
