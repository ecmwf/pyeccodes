import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('systemNumber', 2))
    h.add(_.Unsigned('methodNumber', 2))
    h.alias('local.systemNumber', 'systemNumber')
    h.alias('local.methodNumber', 'methodNumber')
