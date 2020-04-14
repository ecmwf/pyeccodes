import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('startOfHeaders'))
    h.add(_.Ascii('identifier', 4))
    h.alias('ls.identifier', 'identifier')
    h.add(_.Transient('missingValue', 9999))
    h.add(_.Constant('ieeeFloats', 0))
    h.add(_.Constant('zero', 0))
    _.Template('diag/section.1.def').load(h)
    _.Template('diag/section.4.def').load(h)
    h.add(_.Ascii('endMark', 4))
    h.add(_.Position('totalLength'))
