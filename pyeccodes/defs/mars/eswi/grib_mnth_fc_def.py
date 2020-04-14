import pyeccodes.accessors as _


def load(h):

    h.add(_.G1verificationdate('verificationDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('endStep')))
    h.add(_.G1monthlydate('monthlyVerificationDate', _.Get('verificationDate')))
    h.alias('mars.date', 'monthlyVerificationDate')
    h.alias('mars.step', 'startStep')
