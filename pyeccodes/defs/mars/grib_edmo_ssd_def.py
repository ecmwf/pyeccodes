import pyeccodes.accessors as _


def load(h):

    h.add(_.G1verificationdate('verificationDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('startStep')))
    h.alias('mars.date', 'verificationDate')
    h.alias('mars.step', 'endStep')

    if (h.get_l('class') != 3):
        h.unalias('mars.time')
        h.unalias('mars.step')

    h.alias('mars.instrument', 'instrumentType')
    h.alias('mars.ident', 'satelliteNumber')
    h.alias('mars.number', 'perturbationNumber')
