import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('N2', 2))
    h.add(_.Unsigned('codedNumberOfFirstOrderPackedValues', 2))
    h.add(_.Unsigned('numberOfSecondOrderPackedValues', 2))
    h.add(_.Unsigned('extraValues', 1))
    h.add(_.Evaluate('numberOfGroups', (_.Get('codedNumberOfFirstOrderPackedValues') + (65536 * _.Get('extraValues')))))
    h.add(_.Unsigned('groupWidths', 1, _.Get('numberOfGroups')))
    h.add(_.Second_order_bits_per_value('bitsPerValue', _.Get('values'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor')))
    h.add(_.Position('offsetBeforeData'))

    if h.get_l('bitmapPresent'):
        h.add(_.Data_g1second_order_general_packing('codedValues', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision'), _.Get('widthOfFirstOrderValues'), _.Get('N1'), _.Get('N2'), _.Get('numberOfGroups'), _.Get('numberOfSecondOrderPackedValues'), _.Get('extraValues'), _.Get('Ni'), _.Get('Nj'), _.Get('pl'), _.Get('jPointsAreConsecutive'), _.Get('bitmap'), _.Get('groupWidths')))
        h.alias('data.packedValues', 'codedValues')

        if h.get_l('boustrophedonicOrdering'):

            if h.get_l('GRIBEX_boustrophedonic'):
                h.add(_.Data_apply_boustrophedonic_bitmap('preBitmapValues', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor'), _.Get('numberOfRows'), _.Get('numberOfColumns'), _.Get('numberOfPoints')))
            else:
                h.add(_.Data_apply_bitmap('preBitmapValues', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor')))

            h.add(_.Data_apply_boustrophedonic('values', _.Get('preBitmapValues'), _.Get('numberOfRows'), _.Get('numberOfColumns'), _.Get('numberOfPoints'), _.Get('pl')))
        else:
            h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor')))

    else:

        if h.get_l('boustrophedonicOrdering'):
            h.add(_.Data_g1second_order_general_packing('values', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision'), _.Get('widthOfFirstOrderValues'), _.Get('N1'), _.Get('N2'), _.Get('numberOfGroups'), _.Get('numberOfSecondOrderPackedValues'), _.Get('extraValues'), _.Get('Ni'), _.Get('Nj'), _.Get('pl'), _.Get('jPointsAreConsecutive'), _.Get('bitmap'), _.Get('groupWidths')))
            h.add(_.Data_apply_boustrophedonic('values', _.Get('codedValues'), _.Get('numberOfRows'), _.Get('numberOfColumns'), _.Get('numberOfPoints'), _.Get('pl')))
        else:
            h.add(_.Data_g1second_order_general_packing('values', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision'), _.Get('widthOfFirstOrderValues'), _.Get('N1'), _.Get('N2'), _.Get('numberOfGroups'), _.Get('numberOfSecondOrderPackedValues'), _.Get('extraValues'), _.Get('Ni'), _.Get('Nj'), _.Get('pl'), _.Get('jPointsAreConsecutive'), _.Get('bitmap'), _.Get('groupWidths')))

        h.alias('data.packedValues', 'values')

    h.add(_.Transient('numberOfCodedValues', _.Get('numberOfSecondOrderPackedValues')))
    h.add(_.Simple_packing_error('packingError', _.Get('bitsPerValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ibm')))
    _.Template('common/statistics_grid.def').load(h)
