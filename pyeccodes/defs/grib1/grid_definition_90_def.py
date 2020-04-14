import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 90))
    h.add(_.Unsigned('Nx', 2))
    h.alias('numberOfPointsAlongXAxis', 'Nx')
    h.alias('Ni', 'Nx')
    h.alias('geography.Nx', 'Nx')
    h.add(_.Unsigned('Ny', 2))
    h.alias('numberOfPointsAlongYAxis', 'Ny')
    h.alias('Nj', 'Ny')
    h.alias('geography.Ny', 'Ny')
    h.add(_.Signed('latitudeOfSubSatellitePoint', 3))
    h.add(_.Scale('latitudeOfSubSatellitePointInDegrees', _.Get('latitudeOfSubSatellitePoint'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfSubSatellitePointInDegrees', 'latitudeOfSubSatellitePointInDegrees')
    h.alias('Lap', 'latitudeOfSubSatellitePoint')
    h.add(_.Signed('longitudeOfSubSatellitePoint', 3))
    h.add(_.Scale('longitudeOfSubSatellitePointInDegrees', _.Get('longitudeOfSubSatellitePoint'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfSubSatellitePointInDegrees', 'longitudeOfSubSatellitePointInDegrees')
    h.alias('Lap', 'longitudeOfSubSatellitePoint')
    h.add(_.Codeflag('resolutionAndComponentFlags', 1, "grib1/7.table"))
    h.add(_.Bit('ijDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 7))
    h.alias('iDirectionIncrementGiven', 'ijDirectionIncrementGiven')
    h.alias('jDirectionIncrementGiven', 'ijDirectionIncrementGiven')
    h.alias('DiGiven', 'ijDirectionIncrementGiven')
    h.alias('DjGiven', 'ijDirectionIncrementGiven')
    h.add(_.Bit('earthIsOblate', _.Get('resolutionAndComponentFlags'), 6))

    if h.get_l('earthIsOblate'):
        h.add(_.Transient('earthMajorAxis', 6.37816e+06))
        h.add(_.Transient('earthMinorAxis', 6.35678e+06))
        h.alias('earthMajorAxisInMetres', 'earthMajorAxis')
        h.alias('earthMinorAxisInMetres', 'earthMinorAxis')

    h.add(_.Bit('resolutionAndComponentFlags3', _.Get('resolutionAndComponentFlags'), 5))
    h.add(_.Bit('resolutionAndComponentFlags4', _.Get('resolutionAndComponentFlags'), 4))
    h.add(_.Bit('uvRelativeToGrid', _.Get('resolutionAndComponentFlags'), 3))
    h.add(_.Bit('resolutionAndComponentFlags6', _.Get('resolutionAndComponentFlags'), 2))
    h.add(_.Bit('resolutionAndComponentFlags7', _.Get('resolutionAndComponentFlags'), 1))
    h.add(_.Bit('resolutionAndComponentFlags8', _.Get('resolutionAndComponentFlags'), 0))
    h.add(_.Unsigned('dx', 3))
    h.alias('geography.dx', 'dx')
    h.add(_.Unsigned('dy', 3))
    h.alias('geography.dy', 'dy')
    h.add(_.Unsigned('XpInGridLengths', 2))
    h.alias('geography.XpInGridLengths', 'XpInGridLengths')
    h.add(_.Unsigned('YpInGridLengths', 2))
    h.alias('geography.YpInGridLengths', 'YpInGridLengths')
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

    h.add(_.Unsigned('orientationOfTheGrid', 3))
    h.add(_.Scale('orientationOfTheGridInDegrees', _.Get('orientationOfTheGrid'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.orientationOfTheGridInDegrees', 'orientationOfTheGridInDegrees')
    h.add(_.Unsigned('NrInRadiusOfEarth', 3))
    h.alias('altitudeOfTheCameraFromTheEarthsCentreMeasuredInUnitsOfTheEarthsRadius', 'NrInRadiusOfEarth')
    h.add(_.Unsigned('Xo', 2))
    h.alias('xCoordinateOfOriginOfSectorImage', 'Xo')
    h.alias('geography.Xo', 'Xo')
    h.add(_.Unsigned('Yo', 2))
    h.alias('yCoordinateOfOriginOfSectorImage', 'Yo')
    h.alias('geography.Yo', 'Yo')

    if (h.get_l('centre') != 98):
        h.add(_.Pad('padding_grid90_1', 6))

    h.add(_.Number_of_points('numberOfDataPoints', _.Get('Ni'), _.Get('Nj'), _.Get('PLPresent'), _.Get('pl')))
    h.alias('numberOfPoints', 'numberOfDataPoints')
    h.add(_.Number_of_values('numberOfValues', _.Get('values'), _.Get('bitsPerValue'), _.Get('numberOfDataPoints'), _.Get('bitmapPresent'), _.Get('bitmap'), _.Get('numberOfCodedValues')))
