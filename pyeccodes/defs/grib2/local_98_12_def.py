import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('systemNumber', 2))
    h.add(_.Unsigned('methodNumber', 2))
    h.alias('local.systemNumber', 'systemNumber')
    h.alias('local.methodNumber', 'methodNumber')
    h.add(_.Unsigned('indexingDate', 4))
    h.add(_.Unsigned('indexingTime', 2))
    h.alias('mars.date', 'indexingDate')
    h.alias('mars.time', 'indexingTime')
    h.add(_.Pad('padding_loc12_1', 50))
