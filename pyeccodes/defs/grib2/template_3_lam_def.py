import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('Nux', 4))
    h.alias('numberOfUsefulPointsAlongXAxis', 'Nux')
    h.add(_.Unsigned('Ncx', 4))
    h.alias('numberOfPointsAlongXAxisInCouplingArea', 'Ncx')
    h.add(_.Unsigned('Nuy', 4))
    h.alias('numberOfUsefulPointsAlongYAxis', 'Nuy')
    h.add(_.Unsigned('Ncy', 4))
    h.alias('numberOfPointsAlongYAxisInCouplingArea', 'Ncy')
