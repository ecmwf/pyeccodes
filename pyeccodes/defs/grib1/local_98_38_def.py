import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (56 - _.Get('section1Length'))))
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 38))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('iterationNumber', 1))
    h.add(_.Unsigned('totalNumberOfIterations', 1))
    h.alias('iteration', 'iterationNumber')
    h.alias('local.iterationNumber', 'iterationNumber')
    h.alias('local.totalNumberOfIterations', 'totalNumberOfIterations')
    h.add(_.Unsigned('offsetToEndOf4DvarWindow', 2))
    h.add(_.Unsigned('lengthOf4DvarWindow', 2))
    h.alias('anoffset', 'offsetToEndOf4DvarWindow')
    h.add(_.Pad('padding_loc38_1', 1))
