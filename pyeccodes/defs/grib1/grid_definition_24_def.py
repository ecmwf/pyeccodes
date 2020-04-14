import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 42))
    _.Template('grib1/grid_definition_gaussian.def').load(h)
    h.add(_.Signed('latitudeOfStretchingPole', 3))
    h.add(_.Signed('longitudeOfStretchingPole', 3))
    h.add(_.Scale('latitudeOfStretchingPoleInDegrees', _.Get('latitudeOfStretchingPole'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfStretchingPoleInDegrees', 'latitudeOfStretchingPoleInDegrees')
    h.add(_.Scale('longitudeOfStretchingPoleInDegrees', _.Get('longitudeOfStretchingPole'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfStretchingPoleInDegrees', 'longitudeOfStretchingPoleInDegrees')
    h.add(_.Ibmfloat('stretchingFactor', 4))
    h.alias('geography.stretchingFactor', 'stretchingFactor')
