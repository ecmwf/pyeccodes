import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('oceanAtmosphereCoupling', 1))
    h.add(_.Unsigned('legBaseDate', 4))
    h.add(_.Unsigned('legBaseTime', 2))
    h.add(_.Unsigned('legNumber', 1))
    h.add(_.Unsigned('referenceDate', 4))
    h.add(_.Unsigned('climateDateFrom', 4))
    h.add(_.Unsigned('climateDateTo', 4))
    h.alias('local.oceanAtmosphereCoupling', 'oceanAtmosphereCoupling')
    h.alias('local.legBaseDate', 'legBaseDate')
    h.alias('local.legBaseTime', 'legBaseTime')
    h.alias('local.legNumber', 'legNumber')
    h.alias('local.referenceDate', 'referenceDate')
    h.alias('local.climateDateFrom', 'climateDateFrom')
    h.alias('local.climateDateTo', 'climateDateTo')
    h.alias('mars._leg_number', 'legNumber')
