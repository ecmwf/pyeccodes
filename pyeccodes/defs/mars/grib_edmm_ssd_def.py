import pyeccodes.accessors as _


def load(h):

    h.alias('mars.instrument', 'instrumentType')
    h.alias('mars.ident', 'satelliteNumber')
    h.alias('mars.number', 'perturbationNumber')
