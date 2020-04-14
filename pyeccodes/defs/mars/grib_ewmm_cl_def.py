import pyeccodes.accessors as _


def load(h):

    h.unalias('mars.step')
    h.alias('mars.number', 'perturbationNumber')
