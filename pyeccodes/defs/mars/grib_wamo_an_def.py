import pyeccodes.accessors as _


def load(h):

    h.alias('mars.step', 'startStep')
    h.alias('monthlyVerificationTime', 'validityTime')
    h.alias('monthlyVerificationDate', 'dataDate')
