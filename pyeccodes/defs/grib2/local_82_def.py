import pyeccodes.accessors as _


def load(h):

    h.alias('localDefinitionNumber', 'grib2LocalSectionNumber')
    _.Template('grib2/local.[centreForLocal:l].[grib2LocalSectionNumber:l].def').load(h)
    _.Template('grib2/mars_labeling.82.def').load(h)
    _.Template('mars/eswi/grib2.[stream:s].[type:s].def', True).load(h)
    _.Template('grib2/ls_labeling.82.def').load(h)
    h.add(_.Position('offsetAfterLocalSection'))
