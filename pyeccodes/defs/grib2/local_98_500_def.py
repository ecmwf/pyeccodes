import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('observationType', 2, "grib2/tables/local/ecmf/obstat.2.0.table"))
    h.add(_.Codetable('codeType', 2, "grib2/tables/local/ecmf/obstat.3.0.table"))
    h.add(_.Codetable('varno', 2, "grib2/tables/local/ecmf/obstat.varno.table"))
    h.add(_.Codetable('reportType', 2, "grib2/tables/local/ecmf/obstat.reporttype.table"))
    h.add(_.Unsigned('phase', 1))
    h.add(_.Codetable('platform', 2, "grib2/tables/local/ecmf/obstat.4.0.table"))
    h.add(_.Codetable('instrument', 2, "grib2/tables/local/ecmf/obstat.5.0.table"))
    h.add(_.Codetable('dataStream', 2, "grib2/tables/local/ecmf/obstat.6.0.table"))
    h.add(_.Codetable('observationDiagnostic', 2, "grib2/tables/local/ecmf/obstat.9.0.table"))
    h.add(_.Codetable('dataSelection', 2, "grib2/tables/local/ecmf/obstat.10.0.table"))
    h.add(_.Unsigned('scanPosition', 2))
    h.add(_.Codetable('mask', 1, "grib2/tables/local/ecmf/obstat.8.0.table"))
