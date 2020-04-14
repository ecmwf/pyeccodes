import pyeccodes.accessors as _


def load(h):

    h.add(_.Section_length('section1Length', 3))
    h.add(_.Unsigned('gribTablesVersionNo', 1))
    h.add(_.StringCodetable('centre', 1, "common/c-1.table"))
    h.alias('ls.centre', 'centre')
    h.alias('identificationOfOriginatingGeneratingCentre', 'centre')
    h.add(_.Unsigned('generatingProcessIdentifier', 1))
    h.add(_.Unsigned('gridDefinition', 1))
    h.add(_.Codeflag('flag', 1, "grib1/1.table"))
    h.add(_.Codetable('indicatorOfParameter', 1, "grib1/2.[centre:l].[gribTablesVersionNo:l].table"))
    h.add(_.Codetable('indicatorOfTypeOfLevel', 1, "grib1/3.table"))
    h.add(_.Codetable('heightPressureEtcOfLevels', 2, "grib1/3.table"))
    h.alias('ls.levelType', 'indicatorOfTypeOfLevel')
    h.add(_.Unsigned('yearOfCentury', 1))
    h.add(_.Unsigned('month', 1))
    h.add(_.Unsigned('day', 1))
    h.add(_.Unsigned('hour', 1))
    h.add(_.Unsigned('minute', 1))
    h.add(_.Transient('second', 0))
    h.add(_.Budgdate('dataDate', _.Get('yearOfCentury'), _.Get('month'), _.Get('day')))
    h.alias('ls.date', 'dataDate')
    h.add(_.Time('dataTime', _.Get('hour'), _.Get('minute'), _.Get('second')))
    h.alias('ls.time', 'dataTime')
    h.add(_.Julian_day('julianDay', _.Get('dataDate'), _.Get('hour'), _.Get('minute'), _.Get('second')))
    h.add(_.Codetable('indicatorOfUnitOfTimeRange', 1, "grib1/4.table"))
    h.add(_.Unsigned('periodOfTime', 1))
    h.alias('P1', 'periodOfTime')
    h.add(_.Unsigned('periodOfTimeIntervals', 1))
    h.alias('P2', 'periodOfTimeIntervals')
    h.add(_.Codetable('timeRangeIndicator', 1, "grib1/5.table"))
    h.add(_.TransientCodetable('stepUnits', 1, "grib2/tables/1/4.4.table"))

    def stepType_inline_concept(h):
        def wrapped(h):

            timeRangeIndicator = h.get_l('timeRangeIndicator')

            if timeRangeIndicator == 1:
                return 'instant'

            if timeRangeIndicator == 10:
                return 'instant'

            if timeRangeIndicator == 0:
                return 'instant'

            if timeRangeIndicator == 3:
                return 'avg'

            if timeRangeIndicator == 4:
                return 'accum'

            if timeRangeIndicator == 2:
                return 'max'

            if timeRangeIndicator == 2:
                return 'min'

            if timeRangeIndicator == 5:
                return 'diff'

            if timeRangeIndicator == 2:
                return 'rms'

            if timeRangeIndicator == 2:
                return 'sd'

            if timeRangeIndicator == 2:
                return 'cov'

            if timeRangeIndicator == 2:
                return 'ratio'

        return wrapped

    h.add(_.Concept('stepType', None, concepts=stepType_inline_concept(h)))

    h.add(_.G1step_range('stepRange', _.Get('P1'), _.Get('P2'), _.Get('timeRangeIndicator'), _.Get('indicatorOfUnitOfTimeRange'), _.Get('stepUnits'), _.Get('stepType')))
    h.alias('ls.stepRange', 'stepRange')
    h.add(_.Long_vector('startStep', _.Get('stepRange'), 0))
    h.add(_.Long_vector('endStep', _.Get('stepRange'), 1))
    h.add(_.G1step_range('stepRangeInHours', _.Get('P1'), _.Get('P2'), _.Get('timeRangeIndicator'), _.Get('indicatorOfUnitOfTimeRange'), _.Get('one'), _.Get('stepType')))
    h.add(_.Long_vector('startStepInHours', _.Get('stepRangeInHours'), 0))
    h.add(_.Long_vector('endStepInHours', _.Get('stepRangeInHours'), 1))
    h.add(_.Constant('paramId', 0))
    h.alias('parameter', 'paramId')
    h.alias('ls.parameter', 'parameter')
    h.add(_.Section_padding('section1Padding'))
