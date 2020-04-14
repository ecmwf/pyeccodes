import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('ieeeFloats', 0))
    h.add(_.Transient('eps', 0))
    h.add(_.Constant('two', 1))
    h.add(_.Constant('three', 1))
    h.add(_.Constant('eight', 8))
    h.add(_.Constant('eleven', 11))
    h.add(_.Constant('epsPoint', 1))
    h.add(_.Constant('epsContinous', 11))
    h.add(_.Constant('epsStatisticsPoint', 2))
    h.add(_.Constant('epsStatisticsContinous', 12))
    h.add(_.Headers_only('headersOnly'))
    h.add(_.Gts_header('gts_header'))
    h.add(_.Gts_header('gts_TTAAii', 20, 6))
    h.add(_.Gts_header('gts_CCCC', 27, 4))
    h.add(_.Gts_header('gts_ddhh00', 32, 6))
    h.add(_.Ascii('identifier', 4))
    h.add(_.Constant('offsetSection0', 0))
    h.add(_.Constant('section0Length', 8))
    h.add(_.Section_pointer('section0Pointer', _.Get('offsetSection0'), _.Get('section0Length'), 0))
    h.add(_.G1_message_length('totalLength', 3, _.Get('section4Length')))
    h.add(_.Position('startOfHeaders'))
    h.add(_.Unsigned('editionNumber', 1))
    _.Template('grib1/section.1.def').load(h)
    h.alias('ls.edition', 'editionNumber')
    h.add(_.Bit('gridDescriptionSectionPresent', _.Get('section1Flags'), 7))
    h.add(_.Gds_is_present('GDSPresent', _.Get('gridDescriptionSectionPresent'), _.Get('gridDefinition'), _.Get('bitmapPresent'), _.Get('values')))
    h.add(_.Bit('bitmapPresent', _.Get('section1Flags'), 6))
    h.alias('bitmapSectionPresent', 'bitmapPresent')
    h.alias('geography.bitmapPresent', 'bitmapPresent')
    h.alias('missingValuesPresent', 'bitmapPresent')
    h.add(_.Transient('angleSubdivisions', 1000))

    if h.get_l('gridDescriptionSectionPresent'):
        _.Template('grib1/section.2.def').load(h)
    else:
        _.Template('grib1/predefined_grid.def').load(h)

    h.add(_.Position('endOfHeadersMarker'))
    h.add(_.Evaluate('lengthOfHeaders', (_.Get('endOfHeadersMarker') - _.Get('startOfHeaders'))))
    h.add(_.Md5('md5Headers', _.Get('startOfHeaders'), _.Get('lengthOfHeaders')))

    if not (h.get_l('headersOnly')):
        h.add(_.Transient('missingValue', 9999))

        if h.get_l('bitmapPresent'):
            _.Template('grib1/section.3.def').load(h)
        else:
            h.add(_.Constant('tableReference', 0))

        _.Template('grib1/section.4.def').load(h)
        _.Template('grib1/section.5.def').load(h)

