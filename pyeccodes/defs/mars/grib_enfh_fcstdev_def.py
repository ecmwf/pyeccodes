import pyeccodes.accessors as _


def load(h):

    h.alias('mars.step', 'stepRange')
    h.alias('mars.date', 'referenceDate')
    h.alias('mars.hdate', 'dataDate')
    h.alias('mars.number', 'perturbationNumber')
