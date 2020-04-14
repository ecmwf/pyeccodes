import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (58 - _.Get('section1Length'))))
    h.add(_.Constant('probPoint', 5))
    h.add(_.Constant('probContinous', 9))

    if (((h.get_l('timeRangeIndicator') == 3) or (h.get_l('timeRangeIndicator') == 4)) or (h.get_l('timeRangeIndicator') == 5)):
        h.alias('productDefinitionTemplateNumber', 'probContinous')
    else:
        h.alias('productDefinitionTemplateNumber', 'probPoint')

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('forecastProbabilityNumber', 1))
    h.add(_.Unsigned('totalNumberOfForecastProbabilities', 1))
    h.add(_.Signed('localDecimalScaleFactor', 1))
    h.add(_.Unsigned('thresholdIndicator', 1))
    h.add(_.Signed('lowerThreshold', 2))
    h.add(_.Signed('upperThreshold', 2))

    if (h.get_l('thresholdIndicator') == 1):
        h.add(_.Transient('probabilityType', 3))
        h.add(_.Transient('scaleFactorOfLowerLimit', _.Get('localDecimalScaleFactor')))
        h.add(_.Transient('scaledValueOfLowerLimit', _.Get('lowerThreshold')))
        h.add(_.Transient('scaleFactorOfUpperLimit', h._missing()))
        h.add(_.Transient('scaledValueOfUpperLimit', h._missing()))

    if (h.get_l('thresholdIndicator') == 2):
        h.add(_.Transient('probabilityType', 4))
        h.add(_.Transient('scaleFactorOfLowerLimit', h._missing()))
        h.add(_.Transient('scaledValueOfLowerLimit', h._missing()))
        h.add(_.Transient('scaleFactorOfUpperLimit', _.Get('localDecimalScaleFactor')))
        h.add(_.Transient('scaledValueOfUpperLimit', _.Get('upperThreshold')))

    if (h.get_l('thresholdIndicator') == 3):
        h.add(_.Transient('probabilityType', 2))
        h.add(_.Transient('scaleFactorOfLowerLimit', _.Get('localDecimalScaleFactor')))
        h.add(_.Transient('scaledValueOfLowerLimit', _.Get('lowerThreshold')))
        h.add(_.Transient('scaleFactorOfUpperLimit', _.Get('localDecimalScaleFactor')))
        h.add(_.Transient('scaledValueOfUpperLimit', _.Get('upperThreshold')))

    h.add(_.Pad('padding_loc5_1', 1))
    h.alias('number', 'forecastProbabilityNumber')
    h.alias('totalNumber', 'totalNumberOfForecastProbabilities')
