import pyeccodes.accessors as _


def load(h):

    h.add(_.Transient('conceptDir', "mars"))
    h.add(_.Concept('waveDomain', 'unknown', 'wave_domain.def', 'conceptDir', 'conceptDir', False))
    h.alias('mars.domain', 'waveDomain')
