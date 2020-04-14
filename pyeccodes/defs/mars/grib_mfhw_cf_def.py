import pyeccodes.accessors as _


def load(h):

    h.alias('mars.method', 'methodNumber')
    h.alias('mars.origin', 'centre')
    h.alias('mars.refdate', 'referenceDate')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

