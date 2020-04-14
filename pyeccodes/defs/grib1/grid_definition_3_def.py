import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 30))
    _.Template('grib1/grid_definition_lambert.def').load(h)
