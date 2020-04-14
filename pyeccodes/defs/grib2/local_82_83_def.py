import pyeccodes.accessors as _


def load(h):

    h.add(_.StringCodetable('marsClass', 1, "mars/eswi/class.table"))
    h.add(_.StringCodetable('marsType', 1, "mars/eswi/type.table"))
    h.add(_.StringCodetable('marsStream', 2, "mars/eswi/stream.table"))
    h.add(_.Ksec1expver('experimentVersionNumber', 4))
    h.add(_.Pad('reservedNeedNotBePresent', 2))
    h.add(_.StringCodetable('marsModel', 1, "mars/eswi/model.table"))
    h.add(_.Codetable('matchSort', 1, "grib1/localConcepts/eswi/sort.table"))
    h.add(_.Codetable('matchTimeRepres', 1, "grib1/localConcepts/eswi/timerepres.table"))
    h.add(_.Codetable('matchLandType', 1, "grib1/localConcepts/eswi/landtype.table"))
    h.add(_.Codetable('matchAerosolBinNumber', 2, "grib1/localConcepts/eswi/aerosolbinnumber.table"))
    h.add(_.Unsigned('meanSize', 2))
