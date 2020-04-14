import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('parameterCategory', 1, "4.1.[discipline:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('parameterNumber', 1, "4.2.[discipline:l].[parameterCategory:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_units('parameterUnits', _.Get('parameterNumber')))
    h.add(_.Codetable_title('parameterName', _.Get('parameterNumber')))
    h.add(_.Codetable('aerosolType', 2, "4.233.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('typeOfSizeInterval', 1, "4.91.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('typeOfIntervalForFirstAndSecondSize', 'typeOfSizeInterval')
    h.add(_.Signed('scaleFactorOfFirstSize', 1))
    h.add(_.Signed('scaledValueOfFirstSize', 4))
    h.add(_.Signed('scaleFactorOfSecondSize', 1))
    h.add(_.Signed('scaledValueOfSecondSize', 4))
    h.add(_.Codetable('typeOfGeneratingProcess', 1, "4.3.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('backgroundProcess', 1))
    h.alias('backgroundGeneratingProcessIdentifier', 'backgroundProcess')
    h.add(_.Unsigned('generatingProcessIdentifier', 1))
    h.add(_.Unsigned('hoursAfterDataCutoff', 2))
    h.alias('hoursAfterReferenceTimeOfDataCutoff', 'hoursAfterDataCutoff')
    h.add(_.Unsigned('minutesAfterDataCutoff', 1))
    h.alias('minutesAfterReferenceTimeOfDataCutoff', 'minutesAfterDataCutoff')
    h.add(_.Codetable('indicatorOfUnitOfTimeRange', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('defaultStepUnits', 'one')
    _.Template('grib2/localConcepts/[centre:s]/default_step_units.def', True).load(h)
    h.add(_.TransientCodetable('stepUnits', 1, "stepUnits.table"))
    h.add(_.Signed('forecastTime', 4))
