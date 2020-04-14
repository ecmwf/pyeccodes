import pyeccodes.accessors as _


def load(h):

    h.alias('mars.iteration', 'iterationNumber')
    h.alias('mars.diagnostic', 'diagnosticNumber')
    h.alias('mars.domain', 'globalDomain')
