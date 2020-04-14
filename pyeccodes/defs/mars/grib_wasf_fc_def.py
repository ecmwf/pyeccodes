import pyeccodes.accessors as _


def load(h):

    h.alias('mars.number', 'perturbationNumber')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

    if (h.get_s('class') == "me"):
        h.alias('mars.system', 'systemNumber')

    if (h.get_s('class') == "en"):
        h.alias('mars.system', 'systemNumber')

    h.alias('mars.method', 'methodNumber')
