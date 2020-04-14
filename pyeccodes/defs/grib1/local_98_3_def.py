import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (52 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Constant('operStream', "oper"))
    h.alias('mars.stream', 'operStream')
    h.add(_.Unsigned('band', 1))
    h.alias('mars.obstype', 'band')
    h.add(_.Sprintf('marsIdent', "%d", _.Get('indicatorOfTypeOfLevel')))
    h.alias('mars.ident', 'marsIdent')
    h.add(_.Unsigned('functionCode', 1))
    h.add(_.Pad('padding_loc3_1', 1))
