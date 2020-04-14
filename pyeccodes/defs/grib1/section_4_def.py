import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection4'))
    h.add(_.G1_section4_length('section4Length', 3, _.Get('totalLength')))
    h.add(_.Section_pointer('section4Pointer', _.Get('offsetSection4'), _.Get('section4Length'), 4))
    h.add(_.G1_half_byte_codeflag('halfByte'))
    h.add(_.Codeflag('dataFlag', 1, "grib1/11.table"))
    h.add(_.Signed('binaryScaleFactor', 2))
    h.add(_.Ibmfloat('referenceValue', 4))
    h.add(_.Reference_value_error('referenceValueError', _.Get('referenceValue'), _.Get('ibm')))
    h.add(_.Bit('sphericalHarmonics', _.Get('dataFlag'), 7))
    h.add(_.Bit('complexPacking', _.Get('dataFlag'), 6))
    h.add(_.Bit('integerPointValues', _.Get('dataFlag'), 5))
    h.add(_.Bit('additionalFlagPresent', _.Get('dataFlag'), 4))

    if (h.get_l('complexPacking') and (h.get_l('sphericalHarmonics') == 0)):
        h.add(_.Unsigned('widthOfFirstOrderValues', 1))
        h.add(_.Unsigned('N1', 2))
        h.add(_.Codeflag('extendedFlag', 1, "grib1/11-2.table"))
        h.add(_.Bit('matrixOfValues', _.Get('extendedFlag'), 6))
        h.add(_.Bit('secondaryBitmapPresent', _.Get('extendedFlag'), 5))
        h.add(_.Bit('secondOrderOfDifferentWidth', _.Get('extendedFlag'), 4))
        h.add(_.Bit('generalExtended2ordr', _.Get('extendedFlag'), 3))
        h.add(_.Bit('boustrophedonicOrdering', _.Get('extendedFlag'), 2))
        h.add(_.Bit('twoOrdersOfSPD', _.Get('extendedFlag'), 1))
        h.add(_.Bit('plusOneinOrdersOfSPD', _.Get('extendedFlag'), 0))
        h.add(_.Evaluate('orderOfSPD', (_.Get('plusOneinOrdersOfSPD') + (2 * _.Get('twoOrdersOfSPD')))))
        h.alias('secondaryBitmap', 'secondaryBitmapPresent')
        h.alias('boustrophedonic', 'boustrophedonicOrdering')
    else:
        h.add(_.Transient('orderOfSPD', 2))
        h.add(_.Transient('boustrophedonic', 0))

    h.add(_.Transient('hideThis', 0))

    def packingType_inline_concept(h):
        def wrapped(h):

            sphericalHarmonics = h.get_l('sphericalHarmonics')
            complexPacking = h.get_l('complexPacking')
            additionalFlagPresent = h.get_l('additionalFlagPresent')

            if sphericalHarmonics == 0 and complexPacking == 0 and additionalFlagPresent == 0:
                return 'grid_simple'

            integerPointValues = h.get_l('integerPointValues')

            if sphericalHarmonics == 0 and complexPacking == 0 and integerPointValues == 1 and additionalFlagPresent == 1:
                return 'grid_ieee'

            if sphericalHarmonics == 1 and complexPacking == 1 and additionalFlagPresent == 0:
                return 'spectral_complex'

            representationMode = h.get_l('representationMode')

            if sphericalHarmonics == 1 and complexPacking == 0 and additionalFlagPresent == 0 and representationMode == 1:
                return 'spectral_simple'

            hideThis = h.get_l('hideThis')

            if sphericalHarmonics == 1 and complexPacking == 1 and additionalFlagPresent == 0 and hideThis == 1:
                return 'spectral_ieee'

            if sphericalHarmonics == 0 and complexPacking == 0 and additionalFlagPresent == 1:
                return 'grid_simple_matrix'

            secondOrderOfDifferentWidth = h.get_l('secondOrderOfDifferentWidth')
            matrixOfValues = h.get_l('matrixOfValues')
            secondaryBitmapPresent = h.get_l('secondaryBitmapPresent')
            generalExtended2ordr = h.get_l('generalExtended2ordr')

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 0:
                return 'grid_second_order_row_by_row'

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 0 and matrixOfValues == 0 and secondaryBitmapPresent == 1 and generalExtended2ordr == 0:
                return 'grid_second_order_constant_width'

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 1 and generalExtended2ordr == 0:
                return 'grid_second_order_general_grib1'

            plusOneinOrdersOfSPD = h.get_l('plusOneinOrdersOfSPD')
            twoOrdersOfSPD = h.get_l('twoOrdersOfSPD')

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 1 and plusOneinOrdersOfSPD == 0 and twoOrdersOfSPD == 0:
                return 'grid_second_order_no_SPD'

            boustrophedonic = h.get_l('boustrophedonic')

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 1 and plusOneinOrdersOfSPD == 0 and twoOrdersOfSPD == 1 and boustrophedonic == 1:
                return 'grid_second_order'

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 1 and plusOneinOrdersOfSPD == 0 and twoOrdersOfSPD == 1 and boustrophedonic == 0:
                return 'grid_second_order'

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 1 and plusOneinOrdersOfSPD == 0 and twoOrdersOfSPD == 1 and boustrophedonic == 0:
                return 'grid_second_order_no_boustrophedonic'

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 1 and plusOneinOrdersOfSPD == 0 and twoOrdersOfSPD == 1 and boustrophedonic == 1:
                return 'grid_second_order_boustrophedonic'

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 1 and plusOneinOrdersOfSPD == 1 and twoOrdersOfSPD == 0:
                return 'grid_second_order_SPD1'

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 1 and plusOneinOrdersOfSPD == 0 and twoOrdersOfSPD == 1:
                return 'grid_second_order_SPD2'

            if sphericalHarmonics == 0 and complexPacking == 1 and secondOrderOfDifferentWidth == 1 and matrixOfValues == 0 and secondaryBitmapPresent == 0 and generalExtended2ordr == 1 and plusOneinOrdersOfSPD == 1 and twoOrdersOfSPD == 1:
                return 'grid_second_order_SPD3'

            if sphericalHarmonics == 0 and complexPacking == 0 and additionalFlagPresent == 0:
                return 'grid_jpeg'

            if sphericalHarmonics == 0 and complexPacking == 0 and additionalFlagPresent == 0:
                return 'grid_png'

            if sphericalHarmonics == 0 and complexPacking == 0 and additionalFlagPresent == 0:
                return 'grid_ccsds'

            if sphericalHarmonics == 0 and complexPacking == 0 and additionalFlagPresent == 0:
                return 'grid_simple_log_preprocessing'

        return wrapped

    h.add(_.Concept('packingType', None, concepts=packingType_inline_concept(h)))

    h.alias('ls.packingType', 'packingType')
    h.alias('typeOfPacking', 'packingType')

    if (h.get_l('binaryScaleFactor') == -32767):
        h.add(_.Unsigned('bitsPerValue', 1))
        h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
        h.add(_.Constant('dataRepresentationTemplateNumber', 0))
        h.add(_.Constant('bitMapIndicator', 0))
        h.add(_.Position('offsetBeforeData'))
        h.add(_.Transient('numberOfCodedValues', _.Get('numberOfPoints')))
        h.add(_.Data_dummy_field('values', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision'), _.Get('missingValue'), _.Get('numberOfPoints'), _.Get('bitmap')))
    else:
        _.Template('grib1/data.[packingType:s].def').load(h)

    h.add(_.Position('offsetAfterData'))
    h.add(_.Transient('dataLength', ((_.Get('offsetAfterData') - _.Get('offsetBeforeData')) / 8)))

    if (h.get_l('bitmapPresent') == 1):
        h.alias('numberOfEffectiveValues', 'numberOfDataPoints')
    else:
        h.alias('numberOfEffectiveValues', 'numberOfCodedValues')

    if h.get_l('sphericalHarmonics'):
        h.alias('numberOfEffectiveValues', 'numberOfValues')

    h.add(_.Decimal_precision('changeDecimalPrecision', _.Get('bitsPerValue'), _.Get('decimalScaleFactor'), _.Get('changingPrecision'), _.Get('values')))
    h.add(_.Decimal_precision('decimalPrecision', _.Get('bitsPerValue'), _.Get('decimalScaleFactor'), _.Get('changingPrecision')))
    h.alias('setDecimalPrecision', 'changeDecimalPrecision')
    h.add(_.Bits_per_value('bitsPerValueAndRepack', _.Get('values'), _.Get('bitsPerValue')))
    h.alias('setBitsPerValue', 'bitsPerValueAndRepack')
    h.add(_.Scale_values('scaleValuesBy', _.Get('values'), _.Get('missingValue')))
    h.add(_.Offset_values('offsetValuesBy', _.Get('values'), _.Get('missingValue')))

    def gridType_inline_concept(h):
        def wrapped(h):

            dataRepresentationType = h.get_l('dataRepresentationType')
            sphericalHarmonics = h.get_l('sphericalHarmonics')
            PLPresent = h.get_l('PLPresent')

            if dataRepresentationType == 0 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'regular_ll'

            Ni = h.get_l('Ni')

            if dataRepresentationType == 0 and sphericalHarmonics == 0 and PLPresent == 1 and Ni == h._missing():
                return 'reduced_ll'

            if dataRepresentationType == 1 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'mercator'

            if dataRepresentationType == 3 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'lambert'

            if dataRepresentationType == 5 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'polar_stereographic'

            if dataRepresentationType == 6 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'UTM'

            if dataRepresentationType == 7 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'simple_polyconic'

            if dataRepresentationType == 8 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'albers'

            if dataRepresentationType == 8 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'miller'

            if dataRepresentationType == 10 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'rotated_ll'

            if dataRepresentationType == 20 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'stretched_ll'

            if dataRepresentationType == 30 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'stretched_rotated_ll'

            if dataRepresentationType == 4 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'regular_gg'

            if dataRepresentationType == 14 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'rotated_gg'

            if dataRepresentationType == 24 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'stretched_gg'

            if dataRepresentationType == 34 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'stretched_rotated_gg'

            numberOfPointsAlongAParallel = h.get_l('numberOfPointsAlongAParallel')
            iDirectionIncrement = h.get_l('iDirectionIncrement')
            ijDirectionIncrementGiven = h.get_l('ijDirectionIncrementGiven')

            if dataRepresentationType == 4 and sphericalHarmonics == 0 and PLPresent == 1 and numberOfPointsAlongAParallel == h._missing() and iDirectionIncrement == h._missing() and ijDirectionIncrementGiven == 0:
                return 'reduced_gg'

            if dataRepresentationType == 14 and sphericalHarmonics == 0 and PLPresent == 1 and numberOfPointsAlongAParallel == h._missing() and iDirectionIncrement == h._missing() and ijDirectionIncrementGiven == 0:
                return 'reduced_rotated_gg'

            if dataRepresentationType == 24 and sphericalHarmonics == 0 and PLPresent == 1 and numberOfPointsAlongAParallel == h._missing() and iDirectionIncrement == h._missing() and ijDirectionIncrementGiven == 0:
                return 'reduced_stretched_gg'

            if dataRepresentationType == 34 and sphericalHarmonics == 0 and PLPresent == 1 and numberOfPointsAlongAParallel == h._missing() and iDirectionIncrement == h._missing() and ijDirectionIncrementGiven == 0:
                return 'reduced_stretched_rotated_gg'

            if dataRepresentationType == 14 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'regular_rotated_gg'

            if dataRepresentationType == 24 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'regular_stretched_gg'

            if dataRepresentationType == 34 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'regular_stretched_rotated_gg'

            if dataRepresentationType == 50 and sphericalHarmonics == 1 and PLPresent == 0:
                return 'sh'

            if dataRepresentationType == 60 and sphericalHarmonics == 1 and PLPresent == 0:
                return 'rotated_sh'

            if dataRepresentationType == 70 and sphericalHarmonics == 1 and PLPresent == 0:
                return 'stretched_sh'

            if dataRepresentationType == 80 and sphericalHarmonics == 1 and PLPresent == 0:
                return 'stretched_rotated_sh'

            if dataRepresentationType == 90 and sphericalHarmonics == 0 and PLPresent == 0:
                return 'space_view'

            if PLPresent == 0:
                return 'unknown'

            if PLPresent == 1:
                return 'unknown_PLPresent'

        return wrapped

    h.add(_.Concept('gridType', None, concepts=gridType_inline_concept(h)))

    h.alias('ls.gridType', 'gridType')
    h.alias('geography.gridType', 'gridType')
    h.alias('typeOfGrid', 'gridType')
    h.add(_.Size('getNumberOfValues', _.Get('values')))

    if ((h.get_l('complexPacking') == 0) or (h.get_l('sphericalHarmonics') == 1)):
        h.add(_.Padtoeven('padding_sec4_1', _.Get('offsetSection4'), _.Get('section4Length')))

    h.add(_.Md5('md5Section4', _.Get('offsetSection4'), _.Get('section4Length')))
    h.alias('md5DataSection', 'md5Section4')
