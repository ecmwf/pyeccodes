import pyeccodes.accessors as _


def load(h):

    h.unalias('mars.param')
    h.unalias('mars.levtype')
    h.alias('mars.domain', 'globalDomain')
