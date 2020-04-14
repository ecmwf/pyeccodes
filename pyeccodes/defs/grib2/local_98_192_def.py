import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('numberOfLocalDefinitions', 1))

    if (h.get_l('numberOfLocalDefinitions') == 2):
        h.add(_.Unsigned('subLocalDefinitionNumber1', 1))
        _.Template('grib2/local.98.[subLocalDefinitionNumber1].def').load(h)
        h.add(_.Unsigned('subLocalDefinitionNumber2', 1))
        _.Template('grib2/local.98.[subLocalDefinitionNumber2].def').load(h)

