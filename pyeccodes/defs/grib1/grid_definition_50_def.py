import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 50))
    _.Template('grib1/grid_definition_spherical_harmonics.def').load(h)
