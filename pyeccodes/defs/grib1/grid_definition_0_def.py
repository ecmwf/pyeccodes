import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('gridDefinitionTemplateNumber', 0))
    _.Template('grib1/grid_definition_latlon.def').load(h)
    h.add(_.Ascii('zeros', 4))
