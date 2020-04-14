import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetBSection5'))
    h.add(_.Position('offsetSection5'))
    h.add(_.Section_length('section5Length', 4))
    h.add(_.Section_pointer('section5', _.Get('offsetSection5'), _.Get('section5Length'), 5))
    h.add(_.Unsigned('numberOfSection', 1))
    h.add(_.Unsigned('numberOfValues', 4))
    h.alias('numberOfCodedValues', 'numberOfValues')
    h.alias('numberOfEffectiveValues', 'numberOfValues')
    h.add(_.Codetable('dataRepresentationTemplateNumber', 2, "5.0.table", _.Get('masterDir'), _.Get('localDir')))

    def packingType_inline_concept(h):
        def wrapped(h):

            dataRepresentationTemplateNumber = h.get_l('dataRepresentationTemplateNumber')

            if dataRepresentationTemplateNumber == 0:
                return 'grid_simple'

            spectralType = h.get_l('spectralType')
            spectralMode = h.get_l('spectralMode')

            if dataRepresentationTemplateNumber == 51 and spectralType == 1 and spectralMode == 1:
                return 'spectral_complex'

            if dataRepresentationTemplateNumber == 50 and spectralType == 1 and spectralMode == 1:
                return 'spectral_simple'

            if dataRepresentationTemplateNumber == 1:
                return 'grid_simple_matrix'

            if dataRepresentationTemplateNumber == 2:
                return 'grid_complex'

            if dataRepresentationTemplateNumber == 3:
                return 'grid_complex_spatial_differencing'

            if dataRepresentationTemplateNumber == 40000:
                return 'grid_jpeg'

            if dataRepresentationTemplateNumber == 40:
                return 'grid_jpeg'

            if dataRepresentationTemplateNumber == 40010:
                return 'grid_png'

            if dataRepresentationTemplateNumber == 41:
                return 'grid_png'

            if dataRepresentationTemplateNumber == 42:
                return 'grid_ccsds'

            if dataRepresentationTemplateNumber == 4:
                return 'grid_ieee'

            if dataRepresentationTemplateNumber == 50001:
                return 'grid_second_order'

            if dataRepresentationTemplateNumber == 50002:
                return 'grid_second_order'

            if dataRepresentationTemplateNumber == 50002:
                return 'grid_second_order_boustrophedonic'

            if dataRepresentationTemplateNumber == 50001:
                return 'grid_second_order_no_boustrophedonic'

            if dataRepresentationTemplateNumber == 50001:
                return 'grid_second_order_row_by_row'

            if dataRepresentationTemplateNumber == 50001:
                return 'grid_second_order_constant_width'

            if dataRepresentationTemplateNumber == 50001:
                return 'grid_second_order_general_grib1'

            orderOfSPD = h.get_l('orderOfSPD')

            if dataRepresentationTemplateNumber == 50001 and orderOfSPD == 0:
                return 'grid_second_order_no_SPD'

            if dataRepresentationTemplateNumber == 50001 and orderOfSPD == 1:
                return 'grid_second_order_SPD1'

            if dataRepresentationTemplateNumber == 50001 and orderOfSPD == 2:
                return 'grid_second_order_SPD2'

            if dataRepresentationTemplateNumber == 50001 and orderOfSPD == 3:
                return 'grid_second_order_SPD3'

            if dataRepresentationTemplateNumber == 50000:
                return 'spectral_ieee'

            if dataRepresentationTemplateNumber == 61:
                return 'grid_simple_log_preprocessing'

            if dataRepresentationTemplateNumber == 53 and spectralType == 2:
                return 'bifourier_complex'

        return wrapped

    h.add(_.Concept('packingType', 'unknown', concepts=packingType_inline_concept(h)))

    _.Template('grib2/template.5.[dataRepresentationTemplateNumber:l].def').load(h)
    h.alias('ls.packingType', 'packingType')
    h.alias('dataRepresentation', 'packingType')
    h.alias('typeOfPacking', 'packingType')
    h.add(_.Transient('representationMode', 0))
    h.add(_.Md5('md5Section5', _.Get('offsetSection5'), _.Get('section5Length')))
