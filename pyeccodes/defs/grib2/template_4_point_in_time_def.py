import pyeccodes.accessors as _


def load(h):

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
