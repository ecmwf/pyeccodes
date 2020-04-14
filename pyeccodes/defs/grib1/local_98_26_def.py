import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (69 - _.Get('section1Length'))))
    h.add(_.Transient('localFlag', 2))
    _.Template('grib1/mars_labeling.def').load(h)
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 26))

    if (h.get_s('stepType') == "instant"):
        h.alias('productDefinitionTemplateNumber', 'epsPoint')
    else:
        h.alias('productDefinitionTemplateNumber', 'epsContinous')

    h.add(_.Constant('wrongPadding', 1))
    h.add(_.Unsigned('number', 1))
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Unsigned('referenceDate', 4))
    h.add(_.Unsigned('climateDateFrom', 4))
    h.add(_.Unsigned('climateDateTo', 4))
    h.add(_.Pad('padding_loc26_1', 6))
    h.alias('perturbationNumber', 'number')
    h.alias('local.referenceDate', 'referenceDate')
    h.alias('local.climateDateFrom', 'climateDateFrom')
    h.alias('local.climateDateTo', 'climateDateTo')
