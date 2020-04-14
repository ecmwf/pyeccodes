import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('localDefinitionNumber', 1, "grib1/localDefinitionNumber.34.table"))
    _.Template('grib1/local.34.[localDefinitionNumber:l].def').load(h)
    _.Template('mars/grib.[stream:s].[type:s].def', True).load(h)
