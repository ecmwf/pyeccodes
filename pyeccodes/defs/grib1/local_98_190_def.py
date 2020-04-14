import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', 0))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Pad('padding_loc190_1', 2))
    h.add(_.Unsigned('numberOfLocalDefinitions', 1))

    if (h.get_l('numberOfLocalDefinitions') == 1):
        h.add(_.Unsigned('localDefNumberOne', 1))
        h.add(_.Unsigned('numberOfBytesInLocalDefinition', 2))
        _.Template('grib1/local.[centre:l].[localDefNumberOne:l].def').load(h)

    if (h.get_l('numberOfLocalDefinitions') == 2):
        h.add(_.Unsigned('localDefNumberOne', 1))
        h.add(_.Unsigned('numberOfBytesInLocalDefinition', 2))
        h.add(_.Unsigned('localDefNumberTwo', 1))
        h.add(_.Unsigned('numberOfBytesInLocalDefinition', 2))
        _.Template('grib1/local.[centre:l].[localDefNumberOne:l].def').load(h)
        h.add(_.Unsigned('spare2', 4))
        _.Template('grib1/local.[centre:l].[localDefNumberTwo:l].def').load(h)

