import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('shapeOfTheEarth', 1, "3.2.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('scaleFactorOfRadiusOfSphericalEarth', 1))
    h.add(_.Unsigned('scaledValueOfRadiusOfSphericalEarth', 4))
    h.add(_.Unsigned('scaleFactorOfEarthMajorAxis', 1))
    h.alias('scaleFactorOfMajorAxisOfOblateSpheroidEarth', 'scaleFactorOfEarthMajorAxis')
    h.add(_.Unsigned('scaledValueOfEarthMajorAxis', 4))
    h.alias('scaledValueOfMajorAxisOfOblateSpheroidEarth', 'scaledValueOfEarthMajorAxis')
    h.add(_.Unsigned('scaleFactorOfEarthMinorAxis', 1))
    h.alias('scaleFactorOfMinorAxisOfOblateSpheroidEarth', 'scaleFactorOfEarthMinorAxis')
    h.add(_.Unsigned('scaledValueOfEarthMinorAxis', 4))
    h.alias('scaledValueOfMinorAxisOfOblateSpheroidEarth', 'scaledValueOfEarthMinorAxis')
    h.alias('earthIsOblate', 'one')

    if (h.get_l('shapeOfTheEarth') == 0):
        h.add(_.Transient('radius', 6367470))
        h.alias('radiusOfTheEarth', 'radius')
        h.alias('radiusInMetres', 'radius')
        h.alias('earthIsOblate', 'zero')

    if (h.get_l('shapeOfTheEarth') == 1):
        h.add(_.From_scale_factor_scaled_value('radius', _.Get('scaleFactorOfRadiusOfSphericalEarth'), _.Get('scaledValueOfRadiusOfSphericalEarth')))
        h.alias('radiusOfTheEarth', 'radius')
        h.alias('radiusInMetres', 'radius')
        h.alias('earthIsOblate', 'zero')

    if (h.get_l('shapeOfTheEarth') == 6):
        h.add(_.Transient('radius', 6371229))
        h.alias('radiusOfTheEarth', 'radius')
        h.alias('radiusInMetres', 'radius')
        h.alias('earthIsOblate', 'zero')

    if (h.get_l('shapeOfTheEarth') == 8):
        h.add(_.Transient('radius', 6371200))
        h.alias('radiusOfTheEarth', 'radius')
        h.alias('radiusInMetres', 'radius')
        h.alias('earthIsOblate', 'zero')

    if (h.get_l('shapeOfTheEarth') == 2):
        h.add(_.Transient('earthMajorAxis', 6.37816e+06))
        h.add(_.Transient('earthMinorAxis', 6.35678e+06))
        h.alias('earthMajorAxisInMetres', 'earthMajorAxis')
        h.alias('earthMinorAxisInMetres', 'earthMinorAxis')

    if (h.get_l('shapeOfTheEarth') == 3):
        h.add(_.From_scale_factor_scaled_value('earthMajorAxis', _.Get('scaleFactorOfEarthMajorAxis'), _.Get('scaledValueOfEarthMajorAxis')))
        h.add(_.From_scale_factor_scaled_value('earthMinorAxis', _.Get('scaleFactorOfEarthMinorAxis'), _.Get('scaledValueOfEarthMinorAxis')))
        h.add(_.Divdouble('earthMajorAxisInMetres', _.Get('earthMajorAxis'), 0.001))
        h.add(_.Divdouble('earthMinorAxisInMetres', _.Get('earthMinorAxis'), 0.001))

    if (h.get_l('shapeOfTheEarth') == 7):
        h.add(_.From_scale_factor_scaled_value('earthMajorAxis', _.Get('scaleFactorOfEarthMajorAxis'), _.Get('scaledValueOfEarthMajorAxis')))
        h.add(_.From_scale_factor_scaled_value('earthMinorAxis', _.Get('scaleFactorOfEarthMinorAxis'), _.Get('scaledValueOfEarthMinorAxis')))
        h.alias('earthMajorAxisInMetres', 'earthMajorAxis')
        h.alias('earthMinorAxisInMetres', 'earthMinorAxis')

    if ((h.get_l('shapeOfTheEarth') == 4) or (h.get_l('shapeOfTheEarth') == 5)):
        h.add(_.Transient('earthMajorAxis', 6.37814e+06))
        h.add(_.Transient('earthMinorAxis', 6.35675e+06))
        h.alias('earthMajorAxisInMetres', 'earthMajorAxis')
        h.alias('earthMinorAxisInMetres', 'earthMinorAxis')

    if (h.get_l('shapeOfTheEarth') == 9):
        h.add(_.Transient('earthMajorAxis', 6.37756e+06))
        h.add(_.Transient('earthMinorAxis', 6.35626e+06))
        h.alias('earthMajorAxisInMetres', 'earthMajorAxis')
        h.alias('earthMinorAxisInMetres', 'earthMinorAxis')

    h.add(_.Unsigned('numberOfPointsAlongXAxis', 4))
    h.alias('Nx', 'numberOfPointsAlongXAxis')
    h.alias('Ni', 'Nx')
    h.add(_.Unsigned('numberOfPointsAlongYAxis', 4))
    h.alias('Ny', 'numberOfPointsAlongYAxis')
    h.alias('Nj', 'Ny')
    h.add(_.Signed('latitudeOfFirstGridPoint', 4))
    h.alias('La1', 'latitudeOfFirstGridPoint')
    h.add(_.Scale('latitudeOfFirstGridPointInDegrees', _.Get('latitudeOfFirstGridPoint'), _.Get('one'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfFirstGridPointInDegrees', 'latitudeOfFirstGridPointInDegrees')
    h.add(_.Signed('longitudeOfFirstGridPoint', 4))
    h.alias('La1', 'longitudeOfFirstGridPoint')
    h.add(_.Scale('longitudeOfFirstGridPointInDegrees', _.Get('longitudeOfFirstGridPoint'), _.Get('one'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfFirstGridPointInDegrees', 'longitudeOfFirstGridPointInDegrees')
    h.add(_.Signed('standardParallelInMicrodegrees', 4))
    h.alias('standardParallel', 'standardParallelInMicrodegrees')
    h.add(_.Scale('standardParallelInDegrees', _.Get('standardParallelInMicrodegrees'), _.Get('one'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.standardParallelInDegrees', 'standardParallelInDegrees')
    h.add(_.Signed('centralLongitudeInMicrodegrees', 4))
    h.alias('centralLongitude', 'centralLongitudeInMicrodegrees')
    h.add(_.Scale('centralLongitudeInDegrees', _.Get('centralLongitudeInMicrodegrees'), _.Get('one'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.centralLongitudeInDegrees', 'centralLongitudeInDegrees')
    h.add(_.Codeflag('resolutionAndComponentFlags', 1, "grib2/tables/[tablesVersion]/3.3.table"))
    h.add(_.Unsigned('xDirectionGridLengthInMillimetres', 4))
    h.alias('Dx', 'xDirectionGridLengthInMillimetres')
    h.add(_.Scale('xDirectionGridLengthInMetres', _.Get('xDirectionGridLengthInMillimetres'), _.Get('one'), _.Get('thousand'), _.Get('truncateDegrees')))
    h.alias('geography.xDirectionGridLengthInMetres', 'xDirectionGridLengthInMetres')
    h.add(_.Unsigned('yDirectionGridLengthInMillimetres', 4))
    h.alias('Dy', 'yDirectionGridLengthInMillimetres')
    h.add(_.Scale('yDirectionGridLengthInMetres', _.Get('yDirectionGridLengthInMillimetres'), _.Get('one'), _.Get('thousand'), _.Get('truncateDegrees')))
    h.alias('geography.yDirectionGridLengthInMetres', 'yDirectionGridLengthInMetres')
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
    h.add(_.Iterator('ITERATOR', _.Get('lambert_azimuthal_equal_area'), _.Get('numberOfPoints'), _.Get('missingValue'), _.Get('values'), _.Get('radius'), _.Get('Nx'), _.Get('Ny'), _.Get('latitudeOfFirstGridPointInDegrees'), _.Get('longitudeOfFirstGridPointInDegrees'), _.Get('standardParallel'), _.Get('centralLongitude'), _.Get('Dx'), _.Get('Dy'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('jPointsAreConsecutive'), _.Get('alternativeRowScanning')))
    h.add(_.Latlonvalues('latLonValues', _.Get('values')))
    h.alias('latitudeLongitudeValues', 'latLonValues')
    h.add(_.Latitudes('latitudes', _.Get('values'), 0))
    h.add(_.Longitudes('longitudes', _.Get('values'), 0))
    h.add(_.Latitudes('distinctLatitudes', _.Get('values'), 1))
    h.add(_.Longitudes('distinctLongitudes', _.Get('values'), 1))
