import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('localDefinitionNumber', 1, "grib1/localDefinitionNumber.82.table"))
    _.Template('grib1/local.82.[localDefinitionNumber:l].def').load(h)
    _.Template('grib1/ls_labeling.82.def').load(h)
    _.Template('grib1/mars_labeling.82.def').load(h)
    _.Template('mars/eswi/grib1.[stream:s].[type:s].def', True).load(h)
