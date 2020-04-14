import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (106 - _.Get('section1Length'))))
    h.add(_.Transient('localFlag', 3))
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 30))
    _.Template('grib1/mars_labeling.def').load(h)

    if (h.get_s('stepType') == "instant"):

        if ((h.get_s('type') == "em") or (h.get_s('type') == "es")):
            h.alias('productDefinitionTemplateNumber', 'epsStatisticsPoint')
        else:
            h.alias('productDefinitionTemplateNumber', 'epsPoint')

    else:

        if ((h.get_s('type') == "em") or (h.get_s('type') == "es")):
            h.alias('productDefinitionTemplateNumber', 'epsStatisticsContinous')
        else:
            h.alias('productDefinitionTemplateNumber', 'epsContinous')

    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Unsigned('oceanAtmosphereCoupling', 1))
    h.add(_.Pad('padding_loc30_1', 3))
    h.add(_.Unsigned('legBaseDate', 4))
    h.add(_.Unsigned('legBaseTime', 2))
    h.add(_.Unsigned('legNumber', 1))
    h.add(_.Unsigned('referenceDate', 4))
    h.add(_.Unsigned('climateDateFrom', 4))
    h.add(_.Unsigned('climateDateTo', 4))
    h.alias('local.oceanAtmosphereCoupling', 'oceanAtmosphereCoupling')
    h.alias('local.legBaseDate', 'legBaseDate')
    h.alias('local.legBaseTime', 'legBaseTime')
    h.alias('local.legNumber', 'legNumber')
    h.alias('local.referenceDate', 'referenceDate')
    h.alias('local.climateDateFrom', 'climateDateFrom')
    h.alias('local.climateDateTo', 'climateDateTo')
    h.alias('mars._leg_number', 'legNumber')
    h.add(_.Pad('padding_loc30_2', 32))
