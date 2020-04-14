import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('domain', "g"))
    h.add(_.Constant('param', "127.128"))
    h.add(_.Constant('second', 0))
    h.add(_.Constant('step', 0))
    h.add(_.Constant('levtype', "ml"))
    h.add(_.Constant('levelist', 1))
    h.add(_.Budgdate('date', _.Get('yearOfCentury'), _.Get('month'), _.Get('day')))
    h.alias('ls.step', 'step')
    h.alias('ls.date', 'date')
    h.add(_.Time('time', _.Get('hour'), _.Get('minute'), _.Get('second')))
    h.alias('mars.step', 'step')
    h.alias('mars.date', 'date')
    h.alias('mars.time', 'time')
    h.alias('mars.levtype', 'levtype')
    h.alias('mars.param', 'param')
    h.alias('mars.levelist', 'levelist')
