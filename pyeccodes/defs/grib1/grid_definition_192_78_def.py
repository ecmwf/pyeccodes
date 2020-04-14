import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('n2', 2))
    h.add(_.Unsigned('n3', 2))
    h.add(_.Unsigned('nd', 3))
    h.alias('numberOfDiamonds', 'nd')
    h.alias('Nj', 'nd')
    h.add(_.Unsigned('Ni', 3))
    h.add(_.Codeflag('numberingOrderOfDiamonds', 1, "grib1/grid.192.78.3.9.table"))
    h.add(_.Signed('latitudeOfIcosahedronPole', 4))
    h.add(_.Unsigned('longitudeOfIcosahedronPole', 4))
    h.add(_.Unsigned('longitudeOfFirstDiamondCenterLine', 4))
    h.add(_.Unsigned('reservedOctet', 1))
    h.add(_.Codeflag('scanningModeForOneDiamond', 1, "grib1/grid.192.78.3.10.table"))
    h.add(_.Transient('numberOfPoints', ((_.Get('nd') * (_.Get('Ni') + 1)) * (_.Get('Ni') + 1))))
    h.alias('numberOfDataPoints', 'numberOfPoints')
    h.add(_.Number_of_values('numberOfValues', _.Get('values'), _.Get('bitsPerValue'), _.Get('numberOfDataPoints'), _.Get('bitmapPresent'), _.Get('bitmap'), _.Get('numberOfCodedValues')))
