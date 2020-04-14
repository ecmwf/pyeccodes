import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (60 - _.Get('section1Length'))))
    h.add(_.Transient('localFlag', 1))
    _.Template('grib1/mars_labeling.def').load(h)
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 15))

    if (h.get_s('stepType') == "instant"):
        h.alias('productDefinitionTemplateNumber', 'one')
    else:
        h.alias('productDefinitionTemplateNumber', 'eleven')

    h.add(_.Unsigned('perturbationNumber', 2))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('systemNumber', 2))
    h.add(_.Unsigned('methodNumber', 2))
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 2))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Pad('padding_loc15_1', 3))
    h.alias('origin', 'centre')
    h.alias('number', 'perturbationNumber')
    h.alias('total', 'numberOfForecastsInEnsemble')
    h.alias('system', 'systemNumber')
    h.alias('method', 'methodNumber')
    h.alias('local.perturbationNumber', 'perturbationNumber')
    h.alias('local.systemNumber', 'systemNumber')
    h.alias('local.methodNumber', 'methodNumber')
