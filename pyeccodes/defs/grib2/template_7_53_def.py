import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('biFourierCoefficients', 1))
    h.add(_.Constant('complexPacking', 1))
    h.add(_.Data_g2bifourier_packing('codedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('unpackedSubsetPrecision'), _.Get('laplacianOperatorIsSet'), _.Get('laplacianOperator'), _.Get('biFourierTruncationType'), _.Get('biFourierResolutionSubSetParameterN'), _.Get('biFourierResolutionSubSetParameterM'), _.Get('biFourierResolutionParameterN'), _.Get('biFourierResolutionParameterM'), _.Get('biFourierSubTruncationType'), _.Get('biFourierPackingModeForAxes'), _.Get('biFourierMakeTemplate'), _.Get('totalNumberOfValuesInUnpackedSubset'), _.Get('numberOfValues')))
    h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor'), _.Get('numberOfDataPoints'), _.Get('numberOfValues')))
