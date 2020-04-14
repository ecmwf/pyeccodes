import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (120 - _.Get('section1Length'))))
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 18))

    if (h.get_s('stepType') == "instant"):
        h.alias('productDefinitionTemplateNumber', 'epsPoint')
    else:
        h.alias('productDefinitionTemplateNumber', 'epsContinous')

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Codetable('dataOrigin', 1, "common/c-1.table"))
    h.alias('origin', 'dataOrigin')
    h.add(_.Ascii('modelIdentifier', 4))
    h.add(_.Unsigned('consensusCount', 1))
    h.add(_.Pad('padding_loc18_1', 3))

    with h.list('consensus'):
        for i in range(0, h.get_l('consensusCount')):
            h.add(_.Ascii('ccccIdentifiers', 4))
    h.add(_.Padto('padding_loc18_2', (_.Get('offsetSection1') + 120)))
    h.alias('local.dataOrigin', 'dataOrigin')
    h.alias('local.modelIdentifier', 'modelIdentifier')
    h.alias('local.consensusCount', 'consensusCount')
