import pyeccodes.accessors as _


def load(h):

    h.alias('mars.origin', 'centre')
    h.add(_.G1fcperiod('forecastperiod', _.Get('P1'), _.Get('P2'), _.Get('timeRangeIndicator'), _.Get('indicatorOfUnitOfTimeRange')))
    h.alias('mars.fcperiod', 'forecastperiod')
    h.add(_.Sprintf('marsQuantile', "%d:%d", _.Get('perturbationNumber'), _.Get('numberOfForecastsInEnsemble')))
    h.alias('mars.quantile', 'marsQuantile')
    h.unalias('mars.step')
    h.unalias('mars.number')
    h.alias('mars.method', 'methodNumber')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

