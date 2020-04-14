import pyeccodes.accessors as _


def load(h):

    h.add(_.Label('CPTEC local definition'))
    h.add(_.Codetable('localDefinitionNumber', 1, "grib1/localDefinitionNumber.7.table"))
    _.Template('grib1/local.7.[localDefinitionNumber:l].def').load(h)
    h.add(_.Section_padding('local_padding'))
