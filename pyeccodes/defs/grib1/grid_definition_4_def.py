import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 40))
    _.Template('grib1/grid_definition_gaussian.def').load(h)
