import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (56 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 1))
    h.add(_.StringCodetable('marsModel', 2, "mars/model.[centre:l].table"))
    h.alias('mars.model', 'marsModel')
    h.add(_.StringCodetable('marsDomain', 2, "mars/domain.[centre:l].table"))
    h.alias('mars.domain', 'marsDomain')
    h.add(_.Pad('padding_local40_1', 1))
