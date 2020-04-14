import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('dimensionType', 1, "grib2/dimensionType.table"))
    h.add(_.Unsigned('dimensionNumber', 2))
    h.alias('dimension', 'dimensionNumber')
    h.add(_.Unsigned('totalNumberOfdimensions', 2))
    h.alias('extraDimensionPresent', 'one')
