import pyeccodes.accessors as _


def load(h):

    h.alias('mars.fcmonth', 'marsForecastMonth')
    h.alias('mars.number', 'perturbationNumber')
    h.alias('mars.method', 'methodNumber')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

    h.unalias('mars.step')
