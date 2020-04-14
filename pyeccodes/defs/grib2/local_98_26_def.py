import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('referenceDate', 4))
    h.add(_.Unsigned('climateDateFrom', 4))
    h.add(_.Unsigned('climateDateTo', 4))
    h.alias('local.referenceDate', 'referenceDate')
    h.alias('local.climateDateFrom', 'climateDateFrom')
    h.alias('local.climateDateTo', 'climateDateTo')
