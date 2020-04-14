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

    h.add(_.Unsigned('Ni', 4))
    h.alias('numberOfPointsAlongAParallel', 'Ni')
    h.alias('Nx', 'Ni')
    h.add(_.Unsigned('Nj', 4))
    h.alias('numberOfPointsAlongAMeridian', 'Nj')
    h.alias('Ny', 'Nj')
    h.alias('geography.Ni', 'Ni')
    h.alias('geography.Nj', 'Nj')
    h.add(_.Unsigned('basicAngleOfTheInitialProductionDomain', 4))
    h.add(_.Transient('mBasicAngle', (_.Get('basicAngleOfTheInitialProductionDomain') * _.Get('oneMillionConstant'))))
    h.add(_.Transient('angleMultiplier', 1))
    h.add(_.Transient('mAngleMultiplier', 1000000))
    pass  # when block
    h.add(_.Unsigned('subdivisionsOfBasicAngle', 4))
    h.add(_.Transient('angleDivisor', 1000000))
    pass  # when block
    h.add(_.Signed('latitudeOfFirstGridPoint', 4))
    h.alias('La1', 'latitudeOfFirstGridPoint')
    h.add(_.Signed('longitudeOfFirstGridPoint', 4))
    h.alias('Lo1', 'longitudeOfFirstGridPoint')
    h.add(_.Codeflag('resolutionAndComponentFlags', 1, "grib2/tables/[tablesVersion]/3.3.table"))
    h.add(_.Bit('resolutionAndComponentFlags1', _.Get('resolutionAndComponentFlags'), 7))
    h.add(_.Bit('resolutionAndComponentFlags2', _.Get('resolutionAndComponentFlags'), 6))
    h.add(_.Bit('iDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 5))
    h.add(_.Bit('jDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 4))
    h.add(_.Bit('uvRelativeToGrid', _.Get('resolutionAndComponentFlags'), 3))
    h.add(_.Bit('resolutionAndComponentFlags6', _.Get('resolutionAndComponentFlags'), 7))
    h.add(_.Bit('resolutionAndComponentFlags7', _.Get('resolutionAndComponentFlags'), 6))
    h.add(_.Bit('resolutionAndComponentFlags8', _.Get('resolutionAndComponentFlags'), 6))

    def ijDirectionIncrementGiven_inline_concept(h):
        def wrapped(h):

            iDirectionIncrementGiven = h.get_l('iDirectionIncrementGiven')
            jDirectionIncrementGiven = h.get_l('jDirectionIncrementGiven')

            if iDirectionIncrementGiven == 1 and jDirectionIncrementGiven == 1:
                return 1

            if iDirectionIncrementGiven == 1 and jDirectionIncrementGiven == 0:
                return 0

            if iDirectionIncrementGiven == 0 and jDirectionIncrementGiven == 1:
                return 0

            if iDirectionIncrementGiven == 0 and jDirectionIncrementGiven == 0:
                return 0

        return wrapped

    h.add(_.Concept('ijDirectionIncrementGiven', None, concepts=ijDirectionIncrementGiven_inline_concept(h)))

    h.alias('DiGiven', 'iDirectionIncrementGiven')
    h.alias('DjGiven', 'jDirectionIncrementGiven')
    h.add(_.Signed('latitudeOfLastGridPoint', 4))
    h.alias('La2', 'latitudeOfLastGridPoint')
    h.add(_.Signed('longitudeOfLastGridPoint', 4))
    h.alias('Lo2', 'longitudeOfLastGridPoint')
    h.add(_.Unsigned('iDirectionIncrement', 4))
    h.alias('Di', 'iDirectionIncrement')
    h.add(_.Unsigned('N', 4))
    h.alias('numberOfParallelsBetweenAPoleAndTheEquator', 'N')
    h.alias('geography.N', 'N')
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
    h.add(_.G2grid('g2grid', _.Get('latitudeOfFirstGridPoint'), _.Get('longitudeOfFirstGridPoint'), _.Get('latitudeOfLastGridPoint'), _.Get('longitudeOfLastGridPoint'), _.Get('iDirectionIncrement'), None, _.Get('basicAngleOfTheInitialProductionDomain'), _.Get('subdivisionsOfBasicAngle')))
    h.add(_.G2latlon('latitudeOfFirstGridPointInDegrees', _.Get('g2grid'), 0))
    h.alias('geography.latitudeOfFirstGridPointInDegrees', 'latitudeOfFirstGridPointInDegrees')
    h.add(_.G2latlon('longitudeOfFirstGridPointInDegrees', _.Get('g2grid'), 1))
    h.alias('geography.longitudeOfFirstGridPointInDegrees', 'longitudeOfFirstGridPointInDegrees')
    h.add(_.G2latlon('latitudeOfLastGridPointInDegrees', _.Get('g2grid'), 2))
    h.alias('geography.latitudeOfLastGridPointInDegrees', 'latitudeOfLastGridPointInDegrees')
    h.add(_.G2latlon('longitudeOfLastGridPointInDegrees', _.Get('g2grid'), 3))
    h.alias('geography.longitudeOfLastGridPointInDegrees', 'longitudeOfLastGridPointInDegrees')
    h.add(_.G2latlon('iDirectionIncrementInDegrees', _.Get('g2grid'), 4, _.Get('iDirectionIncrementGiven')))
    h.alias('geography.iDirectionIncrementInDegrees', 'iDirectionIncrementInDegrees')
    h.add(_.Global_gaussian('global', _.Get('N'), _.Get('Ni'), _.Get('iDirectionIncrement'), _.Get('latitudeOfFirstGridPoint'), _.Get('longitudeOfFirstGridPoint'), _.Get('latitudeOfLastGridPoint'), _.Get('longitudeOfLastGridPoint'), _.Get('PLPresent'), _.Get('pl'), _.Get('basicAngleOfTheInitialProductionDomain'), _.Get('subdivisionsOfBasicAngle')))
    h.alias('xFirst', 'longitudeOfFirstGridPointInDegrees')
    h.alias('yFirst', 'latitudeOfFirstGridPointInDegrees')
    h.alias('xLast', 'longitudeOfLastGridPointInDegrees')
    h.alias('yLast', 'latitudeOfLastGridPointInDegrees')
    h.alias('latitudeFirstInDegrees', 'latitudeOfFirstGridPointInDegrees')
    h.alias('longitudeFirstInDegrees', 'longitudeOfFirstGridPointInDegrees')
    h.alias('latitudeLastInDegrees', 'latitudeOfLastGridPointInDegrees')
    h.alias('longitudeLastInDegrees', 'longitudeOfLastGridPointInDegrees')
    h.alias('DiInDegrees', 'iDirectionIncrementInDegrees')

    if (h._missing('Ni') and (h.get_l('PLPresent') == 1)):
        h.add(_.Iterator('ITERATOR', _.Get('gaussian_reduced'), _.Get('numberOfPoints'), _.Get('missingValue'), _.Get('values'), _.Get('latitudeOfFirstGridPointInDegrees'), _.Get('longitudeOfFirstGridPointInDegrees'), _.Get('latitudeOfLastGridPointInDegrees'), _.Get('longitudeOfLastGridPointInDegrees'), _.Get('N'), _.Get('pl'), _.Get('Nj')))
        h.add(_.Nearest('NEAREST', _.Get('reduced'), _.Get('values'), _.Get('radius'), _.Get('Nj'), _.Get('pl')))
    else:
        h.add(_.Iterator('ITERATOR', _.Get('gaussian'), _.Get('numberOfPoints'), _.Get('missingValue'), _.Get('values'), _.Get('longitudeFirstInDegrees'), _.Get('DiInDegrees'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('latitudeFirstInDegrees'), _.Get('latitudeLastInDegrees'), _.Get('N'), _.Get('jScansPositively')))
        h.add(_.Nearest('NEAREST', _.Get('regular'), _.Get('values'), _.Get('radius'), _.Get('Ni'), _.Get('Nj')))

    h.add(_.Latlonvalues('latLonValues', _.Get('values')))
    h.alias('latitudeLongitudeValues', 'latLonValues')
    h.add(_.Latitudes('latitudes', _.Get('values'), 0))
    h.add(_.Longitudes('longitudes', _.Get('values'), 0))
    h.add(_.Latitudes('distinctLatitudes', _.Get('values'), 1))
    h.add(_.Longitudes('distinctLongitudes', _.Get('values'), 1))
    h.add(_.Octahedral_gaussian('isOctahedral', _.Get('N'), _.Get('Ni'), _.Get('PLPresent'), _.Get('pl')))
    h.add(_.Gaussian_grid_name('gaussianGridName', _.Get('N'), _.Get('Ni'), _.Get('isOctahedral')))
    h.alias('gridName', 'gaussianGridName')
    h.add(_.Number_of_points_gaussian('numberOfDataPointsExpected', _.Get('Ni'), _.Get('Nj'), _.Get('PLPresent'), _.Get('pl'), _.Get('N'), _.Get('latitudeOfFirstGridPointInDegrees'), _.Get('longitudeOfFirstGridPointInDegrees'), _.Get('latitudeOfLastGridPointInDegrees'), _.Get('longitudeOfLastGridPointInDegrees'), _.Get('zero')))
    h.add(_.Evaluate('legacyGaussSubarea', (_.Get('numberOfDataPoints') != _.Get('numberOfDataPointsExpected'))))
    h.add(_.Signed('latitudeOfSouthernPole', 4))
    h.alias('latitudeOfTheSouthernPoleOfProjection', 'latitudeOfSouthernPole')
    h.add(_.Unsigned('longitudeOfSouthernPole', 4))
    h.alias('longitudeOfTheSouthernPoleOfProjection', 'longitudeOfSouthernPole')
    h.add(_.Scale('latitudeOfSouthernPoleInDegrees', _.Get('latitudeOfSouthernPole'), _.Get('one'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfSouthernPoleInDegrees', 'latitudeOfSouthernPoleInDegrees')
    h.add(_.G2lon('longitudeOfSouthernPoleInDegrees', _.Get('longitudeOfSouthernPole')))
    h.alias('geography.longitudeOfSouthernPoleInDegrees', 'longitudeOfSouthernPoleInDegrees')
    h.add(_.Ieeefloat('angleOfRotation', 4))
    h.alias('geography.angleOfRotationInDegrees', 'angleOfRotation')
    h.alias('angleOfRotationOfProjection', 'angleOfRotation')
    h.alias('is_rotated_grid', 'one')
