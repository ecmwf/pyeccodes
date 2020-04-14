import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('iterationNumber', 1))
    h.alias('number', 'iterationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Unsigned('sensitiveAreaDomain', 1))
    h.add(_.Unsigned('diagnosticNumber', 1))
    h.alias('local.iterationNumber', 'iterationNumber')
    h.alias('local.numberOfForecastsInEnsemble', 'numberOfForecastsInEnsemble')
    h.alias('local.sensitiveAreaDomain', 'sensitiveAreaDomain')
    h.alias('local.diagnosticNumber', 'diagnosticNumber')
    h.alias('iteration', 'iterationNumber')
    h.alias('diagnostic', 'diagnosticNumber')
