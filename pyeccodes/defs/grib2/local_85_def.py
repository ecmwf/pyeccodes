import pyeccodes.accessors as _


def load(h):

    h.alias('localDefinitionNumber', 'grib2LocalSectionNumber')
    _.Template('grib2/local.[centreForLocal:l].[grib2LocalSectionNumber:l].def').load(h)
    h.add(_.Position('offsetAfterLocalSection'))
