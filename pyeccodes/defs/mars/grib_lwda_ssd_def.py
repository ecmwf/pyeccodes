import pyeccodes.accessors as _


def load(h):

    h.alias('mars.step', 'endStep')
    h.alias('mars.anoffset', 'offsetToEndOf4DvarWindow')
    h.alias('mars.instrument', 'instrumentType')
    h.alias('mars.ident', 'satelliteNumber')
