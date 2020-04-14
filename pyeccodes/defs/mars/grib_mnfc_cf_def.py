import pyeccodes.accessors as _


def load(h):

    h.alias('mars.method', 'methodNumber')
    h.alias('mars.origin', 'centre')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

