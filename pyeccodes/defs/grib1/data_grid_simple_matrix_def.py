import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('constantFieldHalfByte', 0))
    h.add(_.Unsigned('bitsPerValue', 1))
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
    h.add(_.Unsigned('octetAtWichPackedDataBegins', 2))
    h.add(_.Codeflag('extendedFlag', 1, "grib1/11-2.table"))
    h.add(_.Bit('matrixOfValues', _.Get('extendedFlag'), 3))
    h.add(_.Bit('secondaryBitmapPresent', _.Get('extendedFlag'), 2))
    h.add(_.Bit('secondOrderOfDifferentWidth', _.Get('extendedFlag'), 1))
    h.alias('secondOrderValuesDifferentWidths', 'secondOrderOfDifferentWidth')
    h.alias('secondaryBitMap', 'secondaryBitmapPresent')
    h.add(_.Unsigned('NR', 2))
    h.alias('firstDimension', 'NR')
    h.add(_.Unsigned('NC', 2))
    h.alias('secondDimension', 'NC')
    h.add(_.Codeflag('coordinateFlag1', 1, "grib1/12.table"))
    h.alias('firstDimensionCoordinateValueDefinition', 'coordinateFlag1')
    h.add(_.Unsigned('NC1', 1))
    h.alias('numberOfCoefficientsOrValuesUsedToSpecifyFirstDimensionCoordinateFunction', 'NC1')
    h.add(_.Codeflag('coordinateFlag2', 1, "grib1/12.table"))
    h.alias('secondDimensionCoordinateValueDefinition', 'coordinateFlag2')
    h.add(_.Unsigned('NC2', 1))
    h.alias('numberOfCoefficientsOrValuesUsedToSpecifySecondDimensionCoordinateFunction', 'NC2')
    h.add(_.Codeflag('physicalFlag1', 1, "grib1/13.table"))
    h.alias('firstDimensionPhysicalSignificance', 'physicalFlag1')
    h.add(_.Codeflag('physicalFlag2', 1, "grib1/13.table"))
    h.alias('secondDimensionPhysicalSignificance', 'physicalFlag2')
    h.add(_.Ibmfloat('coefsFirst', 4, _.Get('NC1')))
    h.add(_.Ibmfloat('coefsSecond', 4, _.Get('NC2')))
    h.alias('data.coefsFirst', 'coefsFirst')
    h.alias('data.coefsSecond', 'coefsSecond')
    h.add(_.Position('offsetBeforeData'))

    if (h.get_l('matrixOfValues') == 0):
        h.add(_.Constant('matrixBitmapsPresent', 0))
        h.add(_.Position('offsetBeforeData'))

        if h.get_l('bitmapPresent'):
            h.add(_.Constant('bitMapIndicator', 0))
            h.add(_.Data_g1simple_packing('codedValues', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee')))
            h.alias('data.packedValues', 'codedValues')
            h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor')))
        else:
            h.add(_.Constant('bitMapIndicator', 255))
            h.add(_.Data_g1simple_packing('values', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte')))
            h.alias('data.packedValues', 'values')

    else:
        h.add(_.Constant('matrixBitmapsPresent', 1))
        h.add(_.Constant('bitMapIndicator', 0))
        h.add(_.Constant('datumSize', (_.Get('NC') * _.Get('NR'))))
        h.add(_.Transient('secondaryBitmapsCount', (_.Get('octetAtWichPackedDataBegins') * _.Get('datumSize'))))
        h.add(_.Transient('secondaryBitmapsSize', (_.Get('secondaryBitmapsCount') / 8)))
        h.add(_.Position('offsetBBitmap'))
        h.add(_.G1bitmap('secondaryBitmaps', _.Get('dummy'), _.Get('missingValue'), _.Get('offsetBBitmap'), _.Get('secondaryBitmapsSize'), _.Get('dummy')))
        h.add(_.Position('offsetBeforeData'))
        h.add(_.Data_g1simple_packing('codedValues', _.Get('section4Length'), _.Get('offsetBeforeData'), _.Get('offsetSection4'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte')))
        h.alias('data.packedValues', 'codedValues')
        h.add(_.Constant('expandBy', (_.Get('NC') * _.Get('NR'))))
        h.add(_.Data_g1secondary_bitmap('secondaryBitmap', _.Get('bitmap'), _.Get('secondaryBitmaps'), _.Get('missingValue'), _.Get('expandBy'), _.Get('octetAtWichPackedDataBegins')))
        h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('secondaryBitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor')))

    h.add(_.Simple_packing_error('packingError', _.Get('bitsPerValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ibm')))
    h.add(_.Number_of_coded_values('numberOfCodedValues', _.Get('bitsPerValue'), _.Get('offsetBeforeData'), _.Get('offsetAfterData'), _.Get('halfByte'), _.Get('numberOfValues')))
    _.Template('common/statistics_grid.def').load(h)
