import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 1))
    _.Template('grib1/grid_definition_latlon.def').load(h)
    h.add(_.Ascii('zeros', 4))
    h.add(_.Signed('latitudeOfSouthernPole', 3))
    h.add(_.Scale('latitudeOfSouthernPoleInDegrees', _.Get('latitudeOfSouthernPole'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfSouthernPoleInDegrees', 'latitudeOfSouthernPoleInDegrees')
    h.add(_.Signed('longitudeOfSouthernPole', 3))
    h.add(_.Scale('longitudeOfSouthernPoleInDegrees', _.Get('longitudeOfSouthernPole'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfSouthernPoleInDegrees', 'longitudeOfSouthernPoleInDegrees')
    h.add(_.Ibmfloat('angleOfRotationInDegrees', 4))
    h.alias('geography.angleOfRotationInDegrees', 'angleOfRotationInDegrees')
    h.alias('angleOfRotation', 'angleOfRotationInDegrees')
    h.alias('is_rotated_grid', 'one')
