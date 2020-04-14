import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('suiteName', 2, "grib2/crra_suiteName.table"))
    h.alias('crraSuiteID', 'suiteName')
