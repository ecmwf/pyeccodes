import pyeccodes.accessors as _


def load(h):

    h.add(_.G1verificationdate('verificationDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('startStep')))
    h.alias('mars.date', 'verificationDate')
    h.alias('mars.step', 'startStep')
