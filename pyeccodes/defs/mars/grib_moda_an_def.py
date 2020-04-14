import pyeccodes.accessors as _


def load(h):

    h.alias('mars.step', 'startStep')
    h.alias('monthlyVerificationTime', 'zero')
    h.alias('monthlyVerificationDate', 'dataDate')

    if (h.get_l('class') != 3):
        h.unalias('mars.time')
        h.unalias('mars.step')

