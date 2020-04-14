import pyeccodes.accessors as _


def load(h):

    h.add(_.G1verificationdate('verificationDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('endStep')))
    h.add(_.G1monthlydate('monthlyVerificationDate', _.Get('verificationDate')))
    h.alias('mars.date', 'monthlyVerificationDate')
    h.add(_.Evaluate('verificationYear', (_.Get('verificationDate') / 10000)))
    h.add(_.Evaluate('monthlyVerificationYear', (_.Get('monthlyVerificationDate') / 10000)))
    h.add(_.Evaluate('verificationMonth', ((_.Get('verificationDate') / 100) % 100)))
    h.add(_.Evaluate('monthlyVerificationMonth', ((_.Get('monthlyVerificationDate') / 100) % 100)))
    h.unalias('mars.time')
    h.unalias('mars.step')
