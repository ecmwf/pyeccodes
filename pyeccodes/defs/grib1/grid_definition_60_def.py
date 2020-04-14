import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 51))
    _.Template('grib1/grid_definition_spherical_harmonics.def').load(h)
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
