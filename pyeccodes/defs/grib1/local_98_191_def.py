import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Pad('padding_loc191_1', 2))
    h.add(_.Unsigned('formatVersionMajorNumber', 1))
    h.add(_.Unsigned('formatVersionMinorNumber', 1))
    h.add(_.Unsigned('originalSubCentreIdentifier', 1))
    h.alias('mars.levelist', 'level')
    h.add(_.Pad('padding_loc191_2', 4))
    h.add(_.Unsigned('numberOfBytesOfFreeFormatData', 2))
    h.add(_.Position('offsetFreeFormData'))
    h.add(_.Unsigned('freeFormData', 1, _.Get('numberOfBytesOfFreeFormatData')))
    h.add(_.Padtomultiple('padding_loc191_3', _.Get('offsetFreeFormData'), 80))
    h.add(_.Position('offsetAfterPadding'))
    h.add(_.Constant('GRIBEXSection1Problem', ((_.Get('offsetAfterPadding') - _.Get('offsetFreeFormData')) % 80)))
