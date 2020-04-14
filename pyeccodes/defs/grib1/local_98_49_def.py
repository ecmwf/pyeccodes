import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 49))

    if (h.get_s('stepType') == "instant"):
        h.alias('productDefinitionTemplateNumber', 'zero')
    else:
        h.alias('productDefinitionTemplateNumber', 'eight')

    h.add(_.Constant('GRIBEXSection1Problem', (56 - _.Get('section1Length'))))
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('mars.number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.add(_.Unsigned('modelErrorType', 1))
    h.add(_.Unsigned('offsetToEndOf4DvarWindow', 2))
    h.add(_.Unsigned('lengthOf4DvarWindow', 2))
    h.alias('anoffset', 'offsetToEndOf4DvarWindow')
    h.alias('local.perturbationNumber', 'perturbationNumber')
    h.alias('local.numberOfForecastsInEnsemble', 'numberOfForecastsInEnsemble')
    h.alias('local.modelErrorType', 'modelErrorType')
