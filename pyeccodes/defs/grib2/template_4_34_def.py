import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('dataRepresentationType', 90))
    h.add(_.Codetable('parameterCategory', 1, "4.1.[discipline:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('parameterNumber', 1, "4.2.[discipline:l].[parameterCategory:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_units('parameterUnits', _.Get('parameterNumber')))
    h.add(_.Codetable_title('parameterName', _.Get('parameterNumber')))
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
    h.add(_.Step_in_units('startStep', _.Get('forecastTime'), _.Get('indicatorOfUnitOfTimeRange'), _.Get('stepUnits')))
    h.add(_.G2end_step('endStep', _.Get('startStep'), _.Get('stepUnits')))
    h.alias('step', 'startStep')
    h.alias('marsStep', 'startStep')
    h.alias('mars.step', 'startStep')
    h.alias('marsStartStep', 'startStep')
    h.alias('marsEndStep', 'endStep')
    h.add(_.G2step_range('stepRange', _.Get('startStep')))
    h.alias('ls.stepRange', 'stepRange')

    def stepTypeInternal_inline_concept(h):
        def wrapped(h):

            dummy = h.get_l('dummy')

            if dummy == 1:
                return 'instant'

        return wrapped

    h.add(_.Concept('stepTypeInternal', None, concepts=stepTypeInternal_inline_concept(h)))

    h.alias('time.stepType', 'stepType')
    h.alias('time.stepRange', 'stepRange')
    h.alias('time.stepUnits', 'stepUnits')
    h.alias('time.dataDate', 'dataDate')
    h.alias('time.dataTime', 'dataTime')
    h.alias('time.startStep', 'startStep')
    h.alias('time.endStep', 'endStep')
    h.add(_.Validity_date('validityDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('step'), _.Get('stepUnits')))
    h.alias('time.validityDate', 'validityDate')
    h.add(_.Validity_time('validityTime', _.Get('dataDate'), _.Get('dataTime'), _.Get('step'), _.Get('stepUnits')))
    h.alias('time.validityTime', 'validityTime')
    h.add(_.Constant('typeOfLevel', "surface"))
    h.add(_.Constant('levelType', "surface"))
    h.add(_.Constant('level', 0))
    h.add(_.Unsigned('NB', 1))
    h.alias('numberOfContributingSpectralBands', 'NB')

    with h.list('listOfContributingSpectralBands'):
        for i in range(0, h.get_l('numberOfContributingSpectralBands')):
            h.add(_.Unsigned('satelliteSeries', 2))
            h.add(_.Unsigned('satelliteNumber', 2))
            h.add(_.Unsigned('instrumentType', 2))
            h.add(_.Unsigned('scaleFactorOfCentralWaveNumber', 1))
            h.add(_.Unsigned('scaledValueOfCentralWaveNumber', 4))
    h.add(_.Codetable('typeOfEnsembleForecast', 1, "4.6.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')

    if ((((((((h.get_l('productionStatusOfProcessedData') == 4) or (h.get_l('productionStatusOfProcessedData') == 5)) or (h.get_l('productionStatusOfProcessedData') == 6)) or (h.get_l('productionStatusOfProcessedData') == 7)) or (h.get_l('productionStatusOfProcessedData') == 8)) or (h.get_l('productionStatusOfProcessedData') == 9)) or (h.get_l('productionStatusOfProcessedData') == 10)) or (h.get_l('productionStatusOfProcessedData') == 11)):
        h.alias('mars.number', 'perturbationNumber')

    h.add(_.Unsigned('yearOfEndOfOverallTimeInterval', 2))
    h.add(_.Unsigned('monthOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('dayOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('hourOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('minuteOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('secondOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('numberOfTimeRange', 1))
    h.alias('n', 'numberOfTimeRange')
    h.add(_.Unsigned('numberOfMissingInStatisticalProcess', 4))
    h.alias('totalNumberOfDataValuesMissingInStatisticalProcess', 'numberOfMissingInStatisticalProcess')

    with h.list('statisticalProcessesList'):
        for i in range(0, h.get_l('numberOfTimeRange')):
            h.add(_.Codetable('typeOfStatisticalProcessing', 1, "4.10.table", _.Get('masterDir'), _.Get('localDir')))
            h.add(_.Codetable('typeOfTimeIncrement', 1, "4.11.table", _.Get('masterDir'), _.Get('localDir')))
            h.alias('typeOfTimeIncrementBetweenSuccessiveFieldsUsedInTheStatisticalProcessing', 'typeOfTimeIncrement')
            h.add(_.Codetable('indicatorOfUnitForTimeRange', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
            h.add(_.Unsigned('lengthOfTimeRange', 4))
            h.add(_.Codetable('indicatorOfUnitForTimeIncrement', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
            h.add(_.Unsigned('timeIncrement', 4))
            h.alias('timeIncrementBetweenSuccessiveFields', 'timeIncrement')

    if ((h.get_l('numberOfTimeRange') == 1) or (h.get_l('numberOfTimeRange') == 2)):

        def stepTypeInternal_inline_concept(h):
            def wrapped(h):

                typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

                if typeOfStatisticalProcessing == 255:
                    return 'instant'

                typeOfTimeIncrement = h.get_l('typeOfTimeIncrement')

                if typeOfStatisticalProcessing == 0 and typeOfTimeIncrement == 2:
                    return 'avg'

                if typeOfStatisticalProcessing == 0 and typeOfTimeIncrement == 3:
                    return 'avg'

                if typeOfStatisticalProcessing == 0 and typeOfTimeIncrement == 1:
                    return 'avgd'

                if typeOfStatisticalProcessing == 1 and typeOfTimeIncrement == 2:
                    return 'accum'

                if typeOfStatisticalProcessing == 2:
                    return 'max'

                if typeOfStatisticalProcessing == 3:
                    return 'min'

                if typeOfStatisticalProcessing == 4:
                    return 'diff'

                if typeOfStatisticalProcessing == 5:
                    return 'rms'

                if typeOfStatisticalProcessing == 6:
                    return 'sd'

                if typeOfStatisticalProcessing == 7:
                    return 'cov'

                if typeOfStatisticalProcessing == 8:
                    return 'sdiff'

                if typeOfStatisticalProcessing == 9:
                    return 'ratio'

                if typeOfStatisticalProcessing == 10:
                    return 'stdanom'

                if typeOfStatisticalProcessing == 11:
                    return 'sum'

            return wrapped

        h.add(_.Concept('stepTypeInternal', None, concepts=stepTypeInternal_inline_concept(h)))

        h.add(_.Step_in_units('startStep', _.Get('forecastTime'), _.Get('indicatorOfUnitOfTimeRange'), _.Get('stepUnits'), _.Get('indicatorOfUnitForTimeRange'), _.Get('lengthOfTimeRange')))
        h.add(_.G2end_step('endStep', _.Get('startStep'), _.Get('stepUnits'), _.Get('year'), _.Get('month'), _.Get('day'), _.Get('hour'), _.Get('minute'), _.Get('second'), _.Get('yearOfEndOfOverallTimeInterval'), _.Get('monthOfEndOfOverallTimeInterval'), _.Get('dayOfEndOfOverallTimeInterval'), _.Get('hourOfEndOfOverallTimeInterval'), _.Get('minuteOfEndOfOverallTimeInterval'), _.Get('secondOfEndOfOverallTimeInterval'), _.Get('indicatorOfUnitForTimeRange'), _.Get('lengthOfTimeRange'), _.Get('typeOfTimeIncrement'), _.Get('numberOfTimeRange')))
        h.add(_.G2step_range('stepRange', _.Get('startStep'), _.Get('endStep')))
    else:
        h.add(_.Constant('stepType', "multiple steps"))
        h.add(_.Constant('stepTypeInternal', "multiple steps"))
        h.add(_.Constant('endStep', "unavailable"))
        h.add(_.Constant('startStep', "unavailable"))
        h.add(_.Constant('stepRange', "unavailable"))

    h.alias('ls.stepRange', 'stepRange')
    h.alias('mars.step', 'endStep')
    h.alias('time.stepType', 'stepType')
    h.alias('time.stepRange', 'stepRange')
    h.alias('time.stepUnits', 'stepUnits')
    h.alias('time.dataDate', 'dataDate')
    h.alias('time.dataTime', 'dataTime')
    h.alias('time.startStep', 'startStep')
    h.alias('time.endStep', 'endStep')
    h.add(_.Validity_date('validityDate', _.Get('date'), _.Get('dataTime'), _.Get('step'), _.Get('stepUnits'), _.Get('yearOfEndOfOverallTimeInterval'), _.Get('monthOfEndOfOverallTimeInterval'), _.Get('dayOfEndOfOverallTimeInterval')))
    h.alias('time.validityDate', 'validityDate')
    h.add(_.Validity_time('validityTime', _.Get('date'), _.Get('dataTime'), _.Get('step'), _.Get('stepUnits'), _.Get('hourOfEndOfOverallTimeInterval'), _.Get('minuteOfEndOfOverallTimeInterval')))
    h.alias('time.validityTime', 'validityTime')
    h.alias('instrument', 'instrumentType')
    h.alias('ident', 'satelliteNumber')
