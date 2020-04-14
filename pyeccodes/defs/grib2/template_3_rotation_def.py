import pyeccodes.accessors as _


def load(h):

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
