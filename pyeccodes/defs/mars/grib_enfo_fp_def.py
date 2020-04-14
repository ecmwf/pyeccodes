import pyeccodes.accessors as _


def load(h):

    if (h.get_l('startStep') == h.get_l('endStep')):
        h.alias('mars.step', 'endStep')
    else:

        if ((h.get_l('paramId') == 131228) and (h.get_l('class') == 1)):

            if (h.get_l('startStep') == (h.get_l('endStep') - 24)):
                h.alias('mars.step', 'endStep')
            else:
                h.add(_.Transient('patch_precip_fp', 24))
                h.add(_.G1step_range('stepRange', _.Get('P1'), _.Get('P2'), _.Get('timeRangeIndicator'), _.Get('unitOfTimeRange'), _.Get('stepUnits'), _.Get('stepType'), _.Get('patch_precip_fp')))
                h.alias('mars.step', 'stepRange')

        else:
            h.alias('mars.step', 'stepRange')

    h.alias('mars.number', 'forecastProbabilityNumber')
