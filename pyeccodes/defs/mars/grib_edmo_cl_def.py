import pyeccodes.accessors as _


def load(h):

    h.unalias('mars.time')
    h.alias('mars.number', 'perturbationNumber')
