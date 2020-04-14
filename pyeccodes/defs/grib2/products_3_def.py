import pyeccodes.accessors as _


def load(h):

    h.alias('parameter', 'paramId')
    h.alias('mars.param', 'paramId')
    h.alias('parameter.paramId', 'paramId')
    h.alias('parameter.shortName', 'shortName')
    h.alias('parameter.units', 'units')
    h.alias('parameter.name', 'name')
