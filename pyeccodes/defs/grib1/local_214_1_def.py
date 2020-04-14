import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))

    if (h.get_l('perturbationNumber') != 0):
        h.alias('number', 'perturbationNumber')

    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.add(_.Pad('padding_local1_1', 1))
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 1))

    if (h.get_s('stepType') == "instant"):

        if (h.get_l('numberOfForecastsInEnsemble') != 0):
            h.alias('productDefinitionTemplateNumber', 'epsPoint')

    else:

        if (h.get_l('numberOfForecastsInEnsemble') != 0):
            h.alias('productDefinitionTemplateNumber', 'epsContinous')

