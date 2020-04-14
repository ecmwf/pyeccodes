import pyeccodes.accessors as _


def load(h):

    h.alias('mars.fcmonth', 'marsForecastMonth')
    h.unalias('mars.step')
    h.alias('mars.method', 'methodNumber')
    h.alias('mars.number', 'perturbationNumber')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

