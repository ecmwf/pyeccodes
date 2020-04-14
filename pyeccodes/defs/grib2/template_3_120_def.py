import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('numberOfDataBinsAlongRadials', 4))
    h.alias('Nb', 'numberOfDataBinsAlongRadials')
    h.add(_.Unsigned('numberOfRadials', 4))
    h.alias('Nr', 'numberOfRadials')
    h.add(_.Signed('latitudeOfCentrePoint', 4))
    h.alias('La1', 'latitudeOfCentrePoint')
    h.add(_.Scale('latitudeOfCentrePointInDegrees', _.Get('latitudeOfCentrePoint'), _.Get('one'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfCentrePointInDegrees', 'latitudeOfCentrePointInDegrees')
    h.alias('La1InDegrees', 'latitudeOfCentrePointInDegrees')
    h.add(_.Unsigned('longitudeOfCentrePoint', 4))
    h.alias('Lo1', 'longitudeOfCentrePoint')
    h.add(_.Scale('longitudeOfCentrePointInDegrees', _.Get('longitudeOfCentrePoint'), _.Get('one'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfCentrePointInDegrees', 'longitudeOfCentrePointInDegrees')
    h.alias('Lo1InDegrees', 'longitudeOfCentrePointInDegrees')
    h.add(_.Unsigned('spacingOfBinsAlongRadials', 4))
    h.alias('Dx', 'spacingOfBinsAlongRadials')
    h.add(_.Unsigned('offsetFromOriginToInnerBound', 4))
    h.alias('Dstart', 'offsetFromOriginToInnerBound')
    h.add(_.Codeflag('scanningMode', 1, "grib2/tables/[tablesVersion]/3.4.table"))
    h.add(_.Bit('iScansNegatively', _.Get('scanningMode'), 7))
    h.add(_.Bit('jScansPositively', _.Get('scanningMode'), 6))
    h.add(_.Bit('jPointsAreConsecutive', _.Get('scanningMode'), 5))
    h.add(_.Bit('alternativeRowScanning', _.Get('scanningMode'), 4))

    if h.get_l('jPointsAreConsecutive'):
        h.alias('numberOfRows', 'Ni')
        h.alias('numberOfColumns', 'Nj')
    else:
        h.alias('numberOfRows', 'Nj')
        h.alias('numberOfColumns', 'Ni')

    h.alias('geography.iScansNegatively', 'iScansNegatively')
    h.alias('geography.jScansPositively', 'jScansPositively')
    h.alias('geography.jPointsAreConsecutive', 'jPointsAreConsecutive')
    h.add(_.Transient('iScansPositively', _.Not(_.Get('iScansNegatively'))))
    h.add(_.Bit('scanningMode5', _.Get('scanningMode'), 3))
    h.add(_.Bit('scanningMode6', _.Get('scanningMode'), 2))
    h.add(_.Bit('scanningMode7', _.Get('scanningMode'), 1))
    h.add(_.Bit('scanningMode8', _.Get('scanningMode'), 0))
    h.add(_.Change_scanning_direction('swapScanningX', _.Get('values'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('xFirst'), _.Get('xLast'), _.Get('x')))
    h.alias('swapScanningLon', 'swapScanningX')
    h.add(_.Change_scanning_direction('swapScanningY', _.Get('values'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('yFirst'), _.Get('yLast'), _.Get('y')))
    h.alias('swapScanningLat', 'swapScanningY')

    with h.list('radials'):
        for i in range(0, h.get_l('numberOfRadials')):
            h.add(_.Signed('startingAzimuth', 2))
            h.alias('Azi', 'startingAzimuth')
            h.add(_.Signed('azimuthalWidth', 2))
            h.alias('Adelta', 'azimuthalWidth')
