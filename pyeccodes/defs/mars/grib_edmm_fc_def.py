import pyeccodes.accessors as _


def load(h):

    h.add(_.G1verificationdate('verificationDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('endStep')))
    h.add(_.G1monthlydate('monthlyVerificationDate', _.Get('verificationDate')))
    h.alias('mars.date', 'monthlyVerificationDate')
    h.add(_.Evaluate('verificationYear', (_.Get('verificationDate') / 10000)))
    h.add(_.Evaluate('monthlyVerificationYear', (_.Get('monthlyVerificationDate') / 10000)))
    h.add(_.Evaluate('verificationMonth', ((_.Get('verificationDate') / 100) % 100)))
    h.add(_.Evaluate('monthlyVerificationMonth', ((_.Get('monthlyVerificationDate') / 100) % 100)))
    h.alias('monthlyVerificationTime', 'validityTime')

    if ((((((((h.get_s('class') == "em") or (h.get_s('class') == "e2")) or (h.get_s('class') == "ea")) or (h.get_s('class') == "ep")) or (h.get_s('class') == "rd")) or (h.get_s('class') == "mc")) or (h.get_s('class') == "et")) or (h.get_s('class') == "l5")):
        h.alias('mars.step', 'endStep')
    else:
        h.alias('mars.step', 'startStep')

    h.alias('mars.number', 'perturbationNumber')
