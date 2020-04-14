import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('lcwfvSuiteName', 2, "grib2/lcwfv_suiteName.table"))
    h.alias('mars.origin', 'lcwfvSuiteName')
