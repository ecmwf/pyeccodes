import pyeccodes.accessors as _


def load(h):

    h.add(_.Ieeefloat('referenceValue', 4))
    h.add(_.Reference_value_error('referenceValueError', _.Get('referenceValue'), _.Get('ieee')))
    h.add(_.Signed('binaryScaleFactor', 2))
    h.add(_.Signed('decimalScaleFactor', 2))
    h.add(_.Transient('optimizeScaleFactor', 0))
    h.add(_.Unsigned('bitsPerValue', 1))
    h.alias('numberOfBits', 'bitsPerValue')
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')
    h.add(_.Unsigned('matrixBitmapsPresent', 1))
    h.alias('secondaryBitmapPresent', 'matrixBitmapsPresent')
    h.add(_.Unsigned('numberOfCodedValues', 4))
    h.add(_.Unsigned('firstDimension', 2))
    h.alias('NR', 'firstDimension')
    h.add(_.Unsigned('secondDimension', 2))
    h.alias('NC', 'secondDimension')
    h.add(_.Unsigned('firstDimensionCoordinateValueDefinition', 1))
    h.add(_.Unsigned('NC1', 1))
    h.alias('numberOfCoefficientsOrValuesUsedToSpecifyFirstDimensionCoordinateFunction', 'NC1')
    h.add(_.Unsigned('secondDimensionCoordinateValueDefinition', 1))
    h.add(_.Unsigned('NC2', 1))
    h.alias('numberOfCoefficientsOrValuesUsedToSpecifySecondDimensionCoordinateFunction', 'NC2')
    h.add(_.Unsigned('firstDimensionPhysicalSignificance', 1))
    h.add(_.Unsigned('secondDimensionPhysicalSignificance', 1))
    h.add(_.Ieeefloat('coefsFirst', 4, _.Get('NC1')))
    h.add(_.Ieeefloat('coefsSecond', 4, _.Get('NC2')))
    h.alias('data.coefsFirst', 'coefsFirst')
    h.alias('data.coefsSecond', 'coefsSecond')

    if (h.get_l('matrixBitmapsPresent') == 1):
        h.add(_.Constant('datumSize', (_.Get('NC') * _.Get('NR'))))
        h.add(_.Constant('secondaryBitmapsCount', (_.Get('numberOfValues') + 0)))
        h.add(_.Constant('secondaryBitmapsSize', (_.Get('secondaryBitmapsCount') / 8)))
        h.add(_.Transient('numberOfDataMatrices', (_.Get('numberOfDataPoints') / _.Get('datumSize'))))
        h.add(_.Position('offsetBBitmap'))
        h.add(_.G2bitmap('secondaryBitmaps', _.Get('dummy'), _.Get('missingValue'), _.Get('offsetBSection5'), _.Get('section5Length'), _.Get('numberOfCodedValues'), _.Get('dummy')))
        h.add(_.Data_g2secondary_bitmap('bitmap', _.Get('primaryBitmap'), _.Get('secondaryBitmaps'), _.Get('missingValue'), _.Get('datumSize'), _.Get('numberOfDataPoints')))

