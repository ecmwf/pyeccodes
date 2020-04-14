import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('Ni', 2))
    h.alias('numberOfPointsAlongFirstAxis', 'Ni')
    h.alias('Nx', 'Ni')
    h.add(_.Unsigned('Nj', 2))
    h.alias('numberOfPointsAlongSecondAxis', 'Nj')
    h.alias('Nx', 'Nj')
    h.add(_.Signed('latitudeOfFirstGridPoint', 3))
    h.add(_.Scale('latitudeOfFirstGridPointInDegrees', _.Get('latitudeOfFirstGridPoint'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfFirstGridPointInDegrees', 'latitudeOfFirstGridPointInDegrees')
    h.alias('La1', 'latitudeOfFirstGridPoint')
    h.add(_.Codeflag('scanningMode', 1, "grib1/8.table"))
    h.add(_.Bit('iScansNegatively', _.Get('scanningMode'), 7))
    h.add(_.Bit('jScansPositively', _.Get('scanningMode'), 6))
    h.add(_.Bit('jPointsAreConsecutive', _.Get('scanningMode'), 5))
    h.add(_.Constant('alternativeRowScanning', 0))
    h.add(_.Transient('iScansPositively', _.Not(_.Get('iScansNegatively'))))
    h.alias('geography.iScansNegatively', 'iScansNegatively')
    h.alias('geography.jScansPositively', 'jScansPositively')
    h.alias('geography.jPointsAreConsecutive', 'jPointsAreConsecutive')
    h.add(_.Bit('scanningMode4', _.Get('scanningMode'), 4))
    h.add(_.Bit('scanningMode5', _.Get('scanningMode'), 3))
    h.add(_.Bit('scanningMode6', _.Get('scanningMode'), 2))
    h.add(_.Bit('scanningMode7', _.Get('scanningMode'), 1))
    h.add(_.Bit('scanningMode8', _.Get('scanningMode'), 0))
    h.add(_.Change_scanning_direction('swapScanningX', _.Get('values'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('xFirst'), _.Get('xLast'), _.Get('x')))
    h.alias('swapScanningLon', 'swapScanningX')
    h.add(_.Change_scanning_direction('swapScanningY', _.Get('values'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('yFirst'), _.Get('yLast'), _.Get('y')))
    h.alias('swapScanningLat', 'swapScanningY')

    if h.get_l('jPointsAreConsecutive'):
        h.alias('numberOfRows', 'Ni')
        h.alias('numberOfColumns', 'Nj')
    else:
        h.alias('numberOfRows', 'Nj')
        h.alias('numberOfColumns', 'Ni')

    h.add(_.Number_of_points('numberOfDataPoints', _.Get('Ni'), _.Get('Nj'), _.Get('PLPresent'), _.Get('pl')))
    h.alias('numberOfPoints', 'numberOfDataPoints')
    h.add(_.Number_of_values('numberOfValues', _.Get('values'), _.Get('bitsPerValue'), _.Get('numberOfDataPoints'), _.Get('bitmapPresent'), _.Get('bitmap'), _.Get('numberOfCodedValues')))
