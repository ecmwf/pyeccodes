import pyeccodes.accessors as _


def load(h):

    h.alias('mars.fcmonth', 'forecastMonth')
    h.unalias('mars.step')
    h.alias('mars.date', 'referenceDate')
