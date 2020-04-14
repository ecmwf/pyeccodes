import pyeccodes.accessors as _


def load(h):

    h.add(_.Section_length('section1Length', 3))
    h.add(_.Unsigned('gribTablesVersionNo', 1))
    h.add(_.Codetable('centre', 1, "common/c-1.table"))
    h.alias('ls.centre', 'centre')
    h.add(_.Unsigned('generatingProcessIdentifier', 1))
    h.add(_.Unsigned('gridDefinition', 1))
    h.add(_.Codeflag('flag', 1, "grib1/1.table"))
    h.add(_.Codetable('indicatorOfParameter', 1, "grib1/2.[centre:l].[gribTablesVersionNo:l].table"))
    h.add(_.StringCodetable('indicatorOfTypeOfLevel', 1, "grib1/3.table"))
    h.alias('ls.levelType', 'indicatorOfTypeOfLevel')
    h.add(_.Codetable('heightPressureEtcOfLevels', 2, "grib1/3.table"))
    h.add(_.Unsigned('yearOfCentury', 1))
    h.add(_.Unsigned('month', 1))
    h.add(_.Unsigned('day', 1))
    h.add(_.Unsigned('hour', 1))
    h.add(_.Unsigned('minute', 1))
    h.add(_.Codetable('indicatorOfUnitOfTimeRange', 1, "grib1/4.table"))
    h.add(_.Unsigned('periodOfTime', 1))
    h.alias('P1', 'periodOfTime')
    h.add(_.Unsigned('periodOfTimeIntervals', 1))
