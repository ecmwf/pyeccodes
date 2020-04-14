import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('sphericalHarmonics', 1))
    h.add(_.Unsigned('J', 4))
    h.alias('pentagonalResolutionParameterJ', 'J')
    h.alias('geography.J', 'J')
    h.add(_.Unsigned('K', 4))
    h.alias('pentagonalResolutionParameterK', 'K')
    h.alias('geography.K', 'K')
    h.add(_.Unsigned('M', 4))
    h.alias('pentagonalResolutionParameterM', 'M')
    h.alias('geography.M', 'M')
    h.add(_.Codetable('spectralType', 1, "3.6.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('spectralDataRepresentationType', 'spectralType')
    h.add(_.Codetable('spectralMode', 1, "3.7.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('spectralDataRepresentationMode', 'spectralMode')
    h.add(_.Signed('latitudeOfThePoleOfStretching', 4))
    h.add(_.Signed('longitudeOfThePoleOfStretching', 4))
    h.add(_.Scale('latitudeOfStretchingPoleInDegrees', _.Get('latitudeOfThePoleOfStretching'), _.Get('oneConstant'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfStretchingPoleInDegrees', 'latitudeOfStretchingPoleInDegrees')
    h.add(_.Scale('longitudeOfStretchingPoleInDegrees', _.Get('longitudeOfThePoleOfStretching'), _.Get('oneConstant'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfStretchingPoleInDegrees', 'longitudeOfStretchingPoleInDegrees')
    h.add(_.Unsigned('stretchingFactorScaled', 4))
    h.add(_.Scale('stretchingFactor', _.Get('stretchingFactorScaled'), _.Get('oneConstant'), _.Get('grib2divider')))
    h.alias('geography.stretchingFactor', 'stretchingFactor')
