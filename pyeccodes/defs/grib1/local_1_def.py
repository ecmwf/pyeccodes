import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('localDefinitionNumber', 1))
    _.Template('grib1/local.98.[localDefinitionNumber:l].def').load(h)
