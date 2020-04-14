import pyeccodes.accessors as _


def load(h):

    h.add(_.Transient('timeRangeIndicator', 0))
    h.add(_.Position('offsetSection4'))
    h.add(_.Section_length('section4Length', 4))
    h.add(_.Section_pointer('section4Pointer', _.Get('offsetSection4'), _.Get('section4Length'), 4))
    h.add(_.Unsigned('numberOfSection', 1))
    h.add(_.Unsigned('NV', 2))
    h.alias('numberOfVerticalCoordinateValues', 'NV')
    h.alias('numberOfCoordinatesValues', 'NV')
    h.alias('numberOfVerticalGridDescriptors', 'NV')
    h.add(_.Transient('neitherPresent', 0))

    if ((h.get_l('centre') == 7) or (h.get_l('centre') == 46)):
        h.alias('disableGrib1LocalSection', 'one')

    h.add(_.Codetable('productDefinitionTemplateNumber', 2, "4.0.table", _.Get('masterDir'), _.Get('localDir')))

    if (h.get_l('section2Used') == 1):
        pass  # when block

    h.add(_.Transient('genVertHeightCoords', 0))
    _.Template('grib2/template.4.[productDefinitionTemplateNumber:l].def').load(h)

    if (h._defined('marsStream') and h._defined('marsType')):
        _.Template('mars/grib.[marsStream:s].[marsType:s].def', True).load(h)

    _.Template('grib2/parameters.def').load(h)

    if h._defined('typeOfFirstFixedSurface'):

        if (h.get_l('typeOfFirstFixedSurface') == 150):
            h.add(_.Transient('genVertHeightCoords', 1))
            h.add(_.Transient('PVPresent', 0))


    if h.get_l('genVertHeightCoords'):
        h.add(_.Ieeefloat('nlev', 4))
        h.add(_.Ieeefloat('numberOfVGridUsed', 4))
        h.add(_.Bytes('uuidOfVGrid', 16))
        h.alias('numberOfVerticalCoordinateValues', 'nlev')
        h.alias('numberOfCoordinatesValues', 'nlev')
        h.alias('numberOfVerticalGridDescriptors', 'nlev')
    else:

        if (h.get_l('NV') == 0):
            h.add(_.Transient('PVPresent', 0))
        else:
            h.add(_.Transient('PVPresent', 1))

        if (h.get_l('PVPresent') or (h.get_l('NV') > 0)):
            h.add(_.Ieeefloat('pv', 4, _.Get('numberOfCoordinatesValues')))
            h.alias('vertical.pv', 'pv')

        def deletePV_inline_concept(h):
            def wrapped(h):

                PVPresent = h.get_l('PVPresent')
                NV = h.get_l('NV')

                if PVPresent == 0 and NV == 0:
                    return 1

            return wrapped

        h.add(_.Concept('deletePV', 'unknown', concepts=deletePV_inline_concept(h)))

    h.add(_.Md5('md5Section4', _.Get('offsetSection4'), _.Get('section4Length')))
