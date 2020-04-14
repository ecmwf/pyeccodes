import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDescriptionSectionPresent', 1))
    h.add(_.Position('offsetSection3'))
    h.add(_.Section_length('section3Length', 4))
    h.add(_.Section_pointer('section3Pointer', _.Get('offsetSection3'), _.Get('section3Length'), 3))
    h.add(_.Unsigned('numberOfSection', 1))
    h.add(_.Codetable('sourceOfGridDefinition', 1, "3.0.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('numberOfDataPoints', 4))
    h.alias('numberOfPoints', 'numberOfDataPoints')
    h.add(_.Unsigned('numberOfOctectsForNumberOfPoints', 1))
    h.add(_.Codetable('interpretationOfNumberOfPoints', 1, "3.11.table", _.Get('masterDir'), _.Get('localDir')))

    if (h.get_l('numberOfOctectsForNumberOfPoints') == 0):
        h.add(_.Transient('PLPresent', 0))
    else:
        h.add(_.Transient('PLPresent', 1))

    h.add(_.Codetable('gridDefinitionTemplateNumber', 2, "3.1.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_title('gridDefinitionDescription', _.Get('gridDefinitionTemplateNumber')))
    h.alias('is_rotated_grid', 'zero')
    _.Template('grib2/template.3.[gridDefinitionTemplateNumber:l].def').load(h)

    if h.get_l('PLPresent'):

        if (h.get_l('numberOfOctectsForNumberOfPoints') == 1):
            h.add(_.Unsigned('pl', 1, _.Get('Nj')))

        if (h.get_l('numberOfOctectsForNumberOfPoints') == 2):
            h.add(_.Unsigned('pl', 2, _.Get('Nj')))

        if (h.get_l('numberOfOctectsForNumberOfPoints') == 3):
            h.add(_.Unsigned('pl', 3, _.Get('Nj')))

        h.alias('geography.pl', 'pl')

    pass  # when block
    h.add(_.Section_padding('section3Padding'))

    def gridType_inline_concept(h):
        def wrapped(h):

            gridDefinitionTemplateNumber = h.get_l('gridDefinitionTemplateNumber')
            PLPresent = h.get_l('PLPresent')

            if gridDefinitionTemplateNumber == 0 and PLPresent == 0:
                return 'regular_ll'

            if gridDefinitionTemplateNumber == 0 and PLPresent == 1:
                return 'reduced_ll'

            if gridDefinitionTemplateNumber == 1 and PLPresent == 0:
                return 'rotated_ll'

            if gridDefinitionTemplateNumber == 2 and PLPresent == 0:
                return 'stretched_ll'

            if gridDefinitionTemplateNumber == 3 and PLPresent == 0:
                return 'stretched_rotated_ll'

            if gridDefinitionTemplateNumber == 10 and PLPresent == 0:
                return 'mercator'

            if gridDefinitionTemplateNumber == 12 and PLPresent == 0:
                return 'transverse_mercator'

            if gridDefinitionTemplateNumber == 20 and PLPresent == 0:
                return 'polar_stereographic'

            if gridDefinitionTemplateNumber == 30 and PLPresent == 0:
                return 'lambert'

            if gridDefinitionTemplateNumber == 31 and PLPresent == 0:
                return 'albers'

            if gridDefinitionTemplateNumber == 40 and PLPresent == 0:
                return 'regular_gg'

            numberOfOctectsForNumberOfPoints = h.get_l('numberOfOctectsForNumberOfPoints')
            iDirectionIncrementGiven = h.get_l('iDirectionIncrementGiven')
            numberOfPointsAlongAParallel = h.get_l('numberOfPointsAlongAParallel')

            if gridDefinitionTemplateNumber == 40 and PLPresent == 1 and numberOfOctectsForNumberOfPoints == 2 and iDirectionIncrementGiven == 0 and numberOfPointsAlongAParallel == h._missing():
                return 'reduced_gg'

            if gridDefinitionTemplateNumber == 41 and PLPresent == 0:
                return 'rotated_gg'

            if gridDefinitionTemplateNumber == 41 and PLPresent == 1 and numberOfOctectsForNumberOfPoints == 2 and iDirectionIncrementGiven == 0 and numberOfPointsAlongAParallel == h._missing():
                return 'reduced_rotated_gg'

            if gridDefinitionTemplateNumber == 42 and PLPresent == 0:
                return 'stretched_gg'

            if gridDefinitionTemplateNumber == 42 and PLPresent == 1 and numberOfOctectsForNumberOfPoints == 2 and iDirectionIncrementGiven == 0 and numberOfPointsAlongAParallel == h._missing():
                return 'reduced_stretched_gg'

            if gridDefinitionTemplateNumber == 43 and PLPresent == 0:
                return 'stretched_rotated_gg'

            if gridDefinitionTemplateNumber == 43 and PLPresent == 1 and numberOfOctectsForNumberOfPoints == 2 and iDirectionIncrementGiven == 0 and numberOfPointsAlongAParallel == h._missing():
                return 'reduced_stretched_rotated_gg'

            if gridDefinitionTemplateNumber == 41 and PLPresent == 0:
                return 'regular_rotated_gg'

            if gridDefinitionTemplateNumber == 42 and PLPresent == 0:
                return 'regular_stretched_gg'

            if gridDefinitionTemplateNumber == 43 and PLPresent == 0:
                return 'regular_stretched_rotated_gg'

            if gridDefinitionTemplateNumber == 50 and PLPresent == 0:
                return 'sh'

            if gridDefinitionTemplateNumber == 51 and PLPresent == 0:
                return 'rotated_sh'

            if gridDefinitionTemplateNumber == 52 and PLPresent == 0:
                return 'stretched_sh'

            if gridDefinitionTemplateNumber == 53 and PLPresent == 0:
                return 'stretched_rotated_sh'

            if gridDefinitionTemplateNumber == 90 and PLPresent == 0:
                return 'space_view'

            if gridDefinitionTemplateNumber == 100 and PLPresent == 0:
                return 'triangular_grid'

            if gridDefinitionTemplateNumber == 101 and PLPresent == 0:
                return 'unstructured_grid'

            if gridDefinitionTemplateNumber == 110 and PLPresent == 0:
                return 'equatorial_azimuthal_equidistant'

            if gridDefinitionTemplateNumber == 120 and PLPresent == 0:
                return 'azimuth_range'

            if gridDefinitionTemplateNumber == 130 and PLPresent == 0:
                return 'irregular_latlon'

            if gridDefinitionTemplateNumber == 140 and PLPresent == 0:
                return 'lambert_azimuthal_equal_area'

            if gridDefinitionTemplateNumber == 1000 and PLPresent == 0:
                return 'cross_section'

            if gridDefinitionTemplateNumber == 1100 and PLPresent == 0:
                return 'Hovmoller'

            if gridDefinitionTemplateNumber == 1200 and PLPresent == 0:
                return 'time_section'

            if gridDefinitionTemplateNumber == 33 and PLPresent == 0:
                return 'lambert_lam'

            if gridDefinitionTemplateNumber == 13 and PLPresent == 0:
                return 'mercator_lam'

            if gridDefinitionTemplateNumber == 23 and PLPresent == 0:
                return 'polar_stereographic_lam'

            if gridDefinitionTemplateNumber == 63 and PLPresent == 0:
                return 'lambert_bf'

            if gridDefinitionTemplateNumber == 61 and PLPresent == 0:
                return 'mercator_bf'

            if gridDefinitionTemplateNumber == 62 and PLPresent == 0:
                return 'polar_stereographic_bf'

            if PLPresent == 0:
                return 'unknown'

            if PLPresent == 1:
                return 'unknown_PLPresent'

        return wrapped

    h.add(_.Concept('gridType', None, concepts=gridType_inline_concept(h)))

    h.alias('ls.gridType', 'gridType')
    h.alias('geography.gridType', 'gridType')
    h.alias('typeOfGrid', 'gridType')
    h.add(_.Md5('md5Section3', _.Get('offsetSection3'), _.Get('section3Length')))
    h.alias('md5GridSection', 'md5Section3')
