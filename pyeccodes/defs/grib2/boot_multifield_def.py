import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('grib2divider', 1000000))
    h.add(_.Transient('missingValue', 9999))
    h.add(_.Constant('ieeeFloats', 1))
    h.add(_.Ascii('identifier', 4))
    h.add(_.Ascii('reserved', 2))
    h.add(_.Codetable('discipline', 1, "grib2/0.0.table"))
    h.add(_.Unsigned('editionNumber', 1))
    h.add(_.Section_length('totalLength', 8))
    _.Template('grib2/sections.def').load(h)
    h.add(_.Lookup('endOfProduct', 4, 0))

    if (h.get_l('endOfProduct') != 926365495):
        _.Template('grib2/sections.def').load(h)

    _.Template('grib2/section.8.def').load(h)
