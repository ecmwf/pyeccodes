import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('startOfHeaders'))
    h.add(_.Ascii('identifier', 4))
    h.alias('ls.identifier', 'identifier')
    h.add(_.Transient('missingValue', 9999))
    h.add(_.Constant('ieeeFloats', 0))
    _.Template('tide/section.1.def').load(h)
    _.Template('tide/mars_labeling.def').load(h)
    h.add(_.Position('endOfHeadersMarker'))
    h.add(_.Evaluate('lengthOfHeaders', (_.Get('endOfHeadersMarker') - _.Get('startOfHeaders'))))
    h.add(_.Md5('md5Headers', _.Get('startOfHeaders'), _.Get('lengthOfHeaders')))
    _.Template('tide/section.4.def').load(h)
    h.add(_.Ascii('endMark', 4))
    h.add(_.Position('totalLength'))
