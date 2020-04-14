import pyeccodes.accessors as _


def load(h):

    h.add(_.Signed('latitudeOfThePoleOfStretching', 4))
    h.add(_.Signed('longitudeOfThePoleOfStretching', 4))
    h.add(_.Scale('latitudeOfStretchingPoleInDegrees', _.Get('latitudeOfThePoleOfStretching'), _.Get('oneConstant'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfStretchingPoleInDegrees', 'latitudeOfStretchingPoleInDegrees')
    h.add(_.Scale('longitudeOfStretchingPoleInDegrees', _.Get('longitudeOfThePoleOfStretching'), _.Get('oneConstant'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfStretchingPoleInDegrees', 'longitudeOfStretchingPoleInDegrees')
    h.add(_.Unsigned('stretchingFactorScaled', 4))
    h.add(_.Scale('stretchingFactor', _.Get('stretchingFactorScaled'), _.Get('oneConstant'), _.Get('grib2divider')))
    h.alias('geography.stretchingFactor', 'stretchingFactor')
