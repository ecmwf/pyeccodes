import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('localDefinitionNumber', 1, "grib1/localDefinitionNumber.[centre:l].table"))
    _.Template('grib1/local.[centre:l].[localDefinitionNumber:l].def').load(h)
