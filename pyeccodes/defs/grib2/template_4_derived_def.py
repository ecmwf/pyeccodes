import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('derivedForecast', 1, "4.7.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
