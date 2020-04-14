import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (62 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('intervalBetweenTimes', 1))
    h.add(_.Constant('numberOfIntegers', 12))
    h.add(_.Unsigned('unsignedIntegers', 1, _.Get('numberOfIntegers')))
