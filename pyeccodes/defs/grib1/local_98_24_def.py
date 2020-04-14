import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (56 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('satelliteIdentifier', 2))
    h.alias('mars.ident', 'satelliteIdentifier')
    h.add(_.Unsigned('instrumentIdentifier', 2))
    h.alias('mars.instrument', 'instrumentIdentifier')
    h.add(_.Unsigned('channelNumber', 2))
    h.alias('mars.channel', 'channelNumber')
    h.add(_.Unsigned('functionCode', 1))
