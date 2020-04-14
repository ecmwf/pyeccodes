import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (107 - _.Get('section1Length'))))
    h.add(_.Transient('grib2LocalSectionNumber', 30))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Constant('wrongPadding', 1))
    h.add(_.Unsigned('perturbationNumber', 1))
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('oceanAtmosphereCoupling', 1))
    h.add(_.Pad('padding_loc27_1', 3))
    h.add(_.Unsigned('legBaseDate', 4))
    h.add(_.Unsigned('legBaseTime', 2))
    h.add(_.Unsigned('legNumber', 1))
    h.add(_.Unsigned('referenceDate', 4))
    h.add(_.Unsigned('climateDateFrom', 4))
    h.add(_.Unsigned('climateDateTo', 4))
    h.alias('mars._leg_number', 'legNumber')
    h.add(_.Pad('padding_loc27_2', 33))
