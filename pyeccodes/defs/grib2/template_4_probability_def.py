import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('forecastProbabilityNumber', 1))
    h.add(_.Unsigned('totalNumberOfForecastProbabilities', 1))
    h.add(_.Codetable('probabilityType', 1, "4.9.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_title('probabilityTypeName', _.Get('probabilityType')))
    h.add(_.Signed('scaleFactorOfLowerLimit', 1))
    h.add(_.Signed('scaledValueOfLowerLimit', 4))
    h.add(_.From_scale_factor_scaled_value('lowerLimit', _.Get('scaleFactorOfLowerLimit'), _.Get('scaledValueOfLowerLimit')))
    h.add(_.Signed('scaleFactorOfUpperLimit', 1))
    h.add(_.Signed('scaledValueOfUpperLimit', 4))
    h.add(_.From_scale_factor_scaled_value('upperLimit', _.Get('scaleFactorOfUpperLimit'), _.Get('scaledValueOfUpperLimit')))
