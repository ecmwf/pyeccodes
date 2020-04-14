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
