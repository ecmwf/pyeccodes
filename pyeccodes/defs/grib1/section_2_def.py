import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection2'))
    h.add(_.Section_length('section2Length', 3))
    h.add(_.Section_pointer('section2Pointer', _.Get('offsetSection2'), _.Get('section2Length'), 2))
    h.add(_.Transient('radius', 6367470))
    h.alias('radiusOfTheEarth', 'radius')
    h.alias('radiusInMetres', 'radius')
    h.add(_.Transient('shapeOfTheEarth', 6))
    h.add(_.Unsigned('numberOfVerticalCoordinateValues', 1))
    h.add(_.Constant('neitherPresent', 255))
    h.alias('NV', 'numberOfVerticalCoordinateValues')
    h.alias('numberOfCoordinatesValues', 'numberOfVerticalCoordinateValues')
    h.add(_.Unsigned('pvlLocation', 1))
    h.add(_.Codetable('dataRepresentationType', 1, "grib1/6.table"))
    h.add(_.Codetable_title('gridDefinitionDescription', _.Get('dataRepresentationType')))
    h.alias('is_rotated_grid', 'zero')

    if (h.get_l('dataRepresentationType') < 192):
        _.Template('grib1/grid_definition_[dataRepresentationType:l].def').load(h)
    else:
        _.Template('grib1/grid_definition_[dataRepresentationType:l].[centre:l].def').load(h)

    h.add(_.Position('endGridDefinition'))
    h.add(_.Position('offsetBeforePV'))
    h.add(_.Transient('PVPresent', (_.Get('NV') > 0)))

    if (h.get_l('pvlLocation') != h.get_l('neitherPresent')):
        h.add(_.Padto('padding_sec2_2', ((_.Get('offsetSection2') + _.Get('pvlLocation')) - 1)))
    else:
        h.add(_.Padto('padding_sec2_2', (_.Get('offsetSection2') + 32)))

    if h.get_l('PVPresent'):
        h.add(_.Ibmfloat('pv', 4, _.Get('NV')))
        h.alias('vertical.pv', 'pv')

    h.add(_.Position('offsetBeforePL'))
    h.add(_.Transient('PLPresent', _.And((_.Get('section2Length') > (_.Get('offsetBeforePL') - _.Get('offsetSection2'))), (_.Get('section2Length') >= (((_.Get('Nj') * 2) + _.Get('offsetBeforePL')) - _.Get('offsetSection2'))))))

    if h.get_l('PLPresent'):
        h.add(_.Constant('numberOfOctectsForNumberOfPoints', 2))
        h.add(_.Constant('interpretationOfNumberOfPoints', 1))
        h.add(_.Unsigned('pl', 2, _.Get('Nj')))
        h.alias('geography.pl', 'pl')

    if ((h.get_l('PVPresent') == 0) and (h.get_l('PLPresent') == 0)):
        h.add(_.Padto('padding_sec2_1', (_.Get('offsetSection2') + 32)))

    pass  # when block
    pass  # when block
    h.alias('reducedGrid', 'PLPresent')

    def deletePV_inline_concept(h):
        def wrapped(h):

            PVPresent = h.get_l('PVPresent')
            NV = h.get_l('NV')

            if PVPresent == 0 and NV == 0:
                return 1

        return wrapped

    h.add(_.Concept('deletePV', 'unknown', concepts=deletePV_inline_concept(h)))

    h.add(_.Padtoeven('padding_sec2_3', _.Get('offsetSection2'), _.Get('section2Length')))
    h.add(_.Md5('md5Section2', _.Get('offsetSection2'), _.Get('section2Length')))
    h.alias('md5GridSection', 'md5Section2')
