import pyeccodes.accessors as _


def load(h):

    h.alias('mars.origin', 'centre')
    h.alias('mars.method', 'methodNumber')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

