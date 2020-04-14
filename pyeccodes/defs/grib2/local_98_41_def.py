import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('isFillup', 1))
    h.alias('local.isFillup', 'isFillup')
    h.add(_.Unsigned('yearOfForecast', 2))
    h.add(_.Unsigned('monthOfForecast', 1))
    h.add(_.Unsigned('dayOfForecast', 1))
    h.add(_.Unsigned('hourOfForecast', 1))
    h.add(_.Unsigned('minuteOfForecast', 1))
    h.add(_.Constant('secondOfForecast', 0))
    h.add(_.G2date('dateOfForecast', _.Get('yearOfForecast'), _.Get('monthOfForecast'), _.Get('dayOfForecast')))
    h.add(_.Time('timeOfForecast', _.Get('hourOfForecast'), _.Get('minuteOfForecast'), _.Get('secondOfForecast')))
    h.add(_.Julian_day('julianForecastDay', _.Get('dateOfForecast'), _.Get('hourOfForecast'), _.Get('minuteOfForecast'), _.Get('secondOfForecast')))
    h.add(_.Transient('diffInDays', (_.Get('julianForecastDay') - _.Get('julianDay'))))
    h.add(_.Transient('diffInHours', (((_.Get('diffInDays') * 1440) + 0.5) / 60)))
    h.add(_.Round('_anoffset', _.Get('diffInHours'), 10))
    h.add(_.Transient('anoffset', _.Get('_anoffset')))
    h.alias('local.anoffset', 'anoffset')
    h.add(_.Unsigned('anoffsetFirst', 2))
    h.add(_.Unsigned('anoffsetLast', 2))
    h.add(_.Unsigned('anoffsetFrequency', 2))
    h.add(_.Transient('is_efas', 1))
    h.add(_.Transient('lsdate_bug', 1))

    def efas_post_proc_inline_concept(h):
        def wrapped(h):

            typeOfPostProcessing = h.get_l('typeOfPostProcessing')

            if typeOfPostProcessing == 0:
                return 'unknown'

            if typeOfPostProcessing == 1:
                return 'lisflood'

            if typeOfPostProcessing == 2:
                return 'lisflood_eric'

            if typeOfPostProcessing == 3:
                return 'lisflood_season'

            if typeOfPostProcessing == 4:
                return 'lisflood_merged'

            if typeOfPostProcessing == 51:
                return 'ericha'

            if typeOfPostProcessing == 101:
                return 'htessel_lisflood'

            if typeOfPostProcessing == 102:
                return 'htessel_eric'

            if typeOfPostProcessing == 103:
                return 'htessel_camaflood'

            if typeOfPostProcessing == 152:
                return 'epic'

            dummy = h.get_l('dummy')

            if dummy == 1:
                return 'unknown'

        return wrapped

    h.add(_.Concept('efas_post_proc', None, concepts=efas_post_proc_inline_concept(h)))

    h.add(_.Unsigned('yearOfModelVersion', 2))
    h.add(_.Unsigned('monthOfModelVersion', 1))
    h.add(_.Unsigned('dayOfModelVersion', 1))
    h.add(_.Unsigned('hourOfModelVersion', 1))
    h.add(_.Unsigned('minuteOfModelVersion', 1))
    h.add(_.Constant('secondOfModelVersion', 0))
    h.add(_.G2date('dateOfModelVersion', _.Get('yearOfModelVersion'), _.Get('monthOfModelVersion'), _.Get('dayOfModelVersion')))
    h.add(_.Time('timeOfModelVersion', _.Get('hourOfModelVersion'), _.Get('minuteOfModelVersion'), _.Get('secondOfModelVersion')))
