import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('localDefinitionNumber', 1, "grib1/localDefinitionNumber.214.table"))
    _.Template('grib1/local.214.[localDefinitionNumber:l].def').load(h)
