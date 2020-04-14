import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('typeOfEnsembleForecast', 1, "4.6.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')

    if ((((((((h.get_l('productionStatusOfProcessedData') == 4) or (h.get_l('productionStatusOfProcessedData') == 5)) or (h.get_l('productionStatusOfProcessedData') == 6)) or (h.get_l('productionStatusOfProcessedData') == 7)) or (h.get_l('productionStatusOfProcessedData') == 8)) or (h.get_l('productionStatusOfProcessedData') == 9)) or (h.get_l('productionStatusOfProcessedData') == 10)) or (h.get_l('productionStatusOfProcessedData') == 11)):
        h.alias('mars.number', 'perturbationNumber')

