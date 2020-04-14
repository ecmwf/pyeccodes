import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 53))
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
    h.add(_.Signed('latitudeOfStretchingPole', 3))
    h.add(_.Signed('longitudeOfStretchingPole', 3))
    h.add(_.Scale('latitudeOfStretchingPoleInDegrees', _.Get('latitudeOfStretchingPole'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfStretchingPoleInDegrees', 'latitudeOfStretchingPoleInDegrees')
    h.add(_.Scale('longitudeOfStretchingPoleInDegrees', _.Get('longitudeOfStretchingPole'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfStretchingPoleInDegrees', 'longitudeOfStretchingPoleInDegrees')
    h.add(_.Ibmfloat('stretchingFactor', 4))
    h.alias('geography.stretchingFactor', 'stretchingFactor')
