import pyeccodes.accessors as _


def load(h):

    h.alias('mars.number', 'perturbationNumber')
    h.alias('mars.origin', 'centre')
    h.add(_.G1fcperiod('forecastperiod', _.Get('P1'), _.Get('P2'), _.Get('timeRangeIndicator'), _.Get('indicatorOfUnitOfTimeRange')))
    h.alias('mars.fcperiod', 'forecastperiod')
    h.unalias('mars.step')
    h.alias('mars.method', 'methodNumber')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

