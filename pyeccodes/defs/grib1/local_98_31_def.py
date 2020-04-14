import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (240 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Unsigned('forecastMonth', 2))
    h.add(_.Unsigned('dateOfForecastRun', 4))
    h.alias('referenceDate', 'dateOfForecastRun')
    h.add(_.Unsigned('numberOfModels', 1))
    h.add(_.Pad('padding_local1_31', 42))

    with h.list('listOfModelIdentifiers'):
        for i in range(0, h.get_l('numberOfModels')):
            h.add(_.Codetable('modelIdentifier', 2, "common/c-1.table"))
    h.add(_.Padto('padding_sec1_loc', (_.Get('offsetSection1') + 240)))
    h.alias('number', 'perturbationNumber')
    h.alias('total', 'numberOfForecastsInEnsemble')
