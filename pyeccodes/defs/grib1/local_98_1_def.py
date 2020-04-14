import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (52 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Pad('padding_local1_1', 1))
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 1))

    if (h.get_s('stepType') == "instant"):

        if ((h.get_s('type') == "em") or (h.get_s('type') == "es")):
            h.alias('productDefinitionTemplateNumber', 'epsStatisticsPoint')
        else:

            if (h.get_l('numberOfForecastsInEnsemble') != 0):

                if (((h.get_l('perturbationNumber') / 2) * 2) == h.get_l('perturbationNumber')):
                    h.alias('typeOfEnsembleForecast', 'two')
                else:
                    h.alias('typeOfEnsembleForecast', 'three')

                h.alias('productDefinitionTemplateNumber', 'epsPoint')
            else:
                h.alias('productDefinitionTemplateNumber', 'zero')

    else:

        if ((h.get_s('type') == "em") or (h.get_s('type') == "es")):
            h.alias('productDefinitionTemplateNumber', 'epsStatisticsContinous')
        else:

            if (h.get_l('numberOfForecastsInEnsemble') != 0):

                if (((h.get_l('perturbationNumber') / 2) * 2) == h.get_l('perturbationNumber')):
                    h.alias('typeOfEnsembleForecast', 'two')
                else:
                    h.alias('typeOfEnsembleForecast', 'three')

                h.alias('productDefinitionTemplateNumber', 'epsContinous')
            else:
                h.alias('productDefinitionTemplateNumber', 'eight')

