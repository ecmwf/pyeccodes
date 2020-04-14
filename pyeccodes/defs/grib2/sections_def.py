import pyeccodes.accessors as _


def load(h):

    h.add(_.Lookup('sectionNumber', 1, 4))

    if ((h.get_l('sectionNumber') == 1) or h._new()):
        h.add(_.Position('sectionPosition'))
        _.Template('grib2/section.1.def').load(h)

    h.add(_.Lookup('sectionNumber', 1, 4))
    h.add(_.Transient('grib2LocalSectionPresent', 0))
    h.alias('section2Used', 'zero')
    h.alias('setLocalDefinition', 'grib2LocalSectionPresent')
    h.add(_.Transient('deleteLocalDefinition', 0))

    if (((h.get_l('sectionNumber') == 2) or (h.get_l('grib2LocalSectionPresent') > 0)) and (h.get_l('deleteLocalDefinition') == 0)):
        h.add(_.Position('sectionPosition'))
        _.Template('grib2/section.2.def').load(h)

    h.alias('localUsePresent', 'section2Used')
    h.add(_.Lookup('sectionNumber', 1, 4))

    if ((h.get_l('sectionNumber') == 3) or h._new()):
        h.add(_.Position('sectionPosition'))
        _.Template('grib2/section.3.def').load(h)

    h.add(_.Lookup('sectionNumber', 1, 4))

    if ((h.get_l('sectionNumber') == 4) or h._new()):
        h.add(_.Position('sectionPosition'))
        _.Template('grib2/section.4.def').load(h)

    h.add(_.Position('endOfHeadersMarker'))
    h.add(_.Evaluate('lengthOfHeaders', (_.Get('endOfHeadersMarker') - _.Get('startOfHeaders'))))
    h.add(_.Md5('md5Headers', _.Get('startOfHeaders'), _.Get('lengthOfHeaders')))
    h.add(_.Lookup('sectionNumber', 1, 4))

    if ((h.get_l('sectionNumber') == 5) or h._new()):
        h.add(_.Position('sectionPosition'))
        _.Template('grib2/section.5.def').load(h)

    h.add(_.Lookup('sectionNumber', 1, 4))

    if ((h.get_l('sectionNumber') == 6) or h._new()):
        h.add(_.Position('sectionPosition'))
        _.Template('grib2/section.6.def').load(h)

    h.add(_.Lookup('sectionNumber', 1, 4))

    if ((h.get_l('sectionNumber') == 7) or h._new()):
        h.add(_.Position('sectionPosition'))
        _.Template('grib2/section.7.def').load(h)

