import pyeccodes.accessors as _


def load(h):

    h.alias('mars.number', 'perturbationNumber')
    h.unalias('mars.step')
    h.add(_.Evaluate('forecastPeriodFrom', (_.Get('verifyingMonth') / 1000)))
    h.add(_.Evaluate('forecastPeriodTo', (_.Get('verifyingMonth') % 1000)))
    h.add(_.Sprintf('forecastPeriod', "%d-%d", _.Get('forecastPeriodFrom'), _.Get('forecastPeriodTo')))
    h.alias('mars.fcperiod', 'forecastPeriod')
    h.alias('mars.method', 'methodNumber')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

