import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('suiteName', 2, "grib2/tigge_suiteName.table"))
    h.alias('tiggeSuiteID', 'suiteName')
