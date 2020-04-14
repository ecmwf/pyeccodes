import pyeccodes.accessors as _


def load(h):

    h.alias('mars.number', 'forecastOrSingularVectorNumber')
    h.alias('mars.origin', 'centre')

    if (h.get_l('class') == 9):
        h.alias('mars.number', 'forecastOrSingularVectorNumber')
        h.alias('mars.method', 'methodNumber')

