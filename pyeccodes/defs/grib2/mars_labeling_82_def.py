import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('conceptsMasterMarsDir', "mars"))
    h.add(_.Constant('conceptsLocalMarsDirAll', "mars/[centre:s]"))
    h.alias('mars.class', 'marsClass')
    h.alias('mars.type', 'marsType')
    h.alias('mars.stream', 'marsStream')
    h.alias('mars.model', 'marsModel')
    h.alias('mars.expver', 'experimentVersionNumber')
    h.alias('mars.domain', 'globalDomain')

    if (h.get_l('localDefinitionNumber') == 83):
        h.alias('mars.sort', 'matchSort')
        h.alias('mars.timerepres', 'matchTimeRepres')
        h.alias('mars.landtype', 'matchLandType')
        h.alias('mars.aerosolbinnumber', 'matchAerosolBinNumber')
        h.add(_.Concept('matchAerosolPacking', 'unknown', 'aerosolPackingConcept.def', 'conceptsLocalMarsDirAll', 'conceptsMasterMarsDir', True))
        h.alias('mars.aerosolpacking', 'matchAerosolPacking')

