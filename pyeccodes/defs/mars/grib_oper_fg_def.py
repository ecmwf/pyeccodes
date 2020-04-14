import pyeccodes.accessors as _


def load(h):

    if (h.get_l('centre') == 98):
        h.add(_.Validity_date('fgDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('endStep')))
        h.add(_.Validity_time('fgTime', _.Get('dataDate'), _.Get('dataTime'), _.Get('endStep')))
        h.alias('mars.date', 'fgDate')
        h.alias('mars.time', 'fgTime')

