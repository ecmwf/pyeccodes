import pyeccodes.accessors as _


def load(h):

    h.alias('ls.dataType', 'marsType')

    if (h.get_l('localDefinitionNumber') == 83):
        h.add(_.Concept('timerepres', 'unknown', 'timeRepresConcept.def', 'conceptsLocalDirAll', 'conceptsMasterDir', True))
        h.alias('ls.timerepres', 'timerepres')
        h.add(_.Concept('sort', 'unknown', 'sortConcept.def', 'conceptsLocalDirAll', 'conceptsMasterDir', True))
        h.alias('ls.sort', 'sort')
        h.add(_.Concept('landtype', 'unknown', 'landTypeConcept.def', 'conceptsLocalDirAll', 'conceptsMasterDir', True))
        h.alias('ls.landtype', 'landtype')
        h.add(_.Concept('aerosolbinnumber', 'unknown', 'aerosolConcept.def', 'conceptsLocalDirAll', 'conceptsMasterDir', True))
        h.alias('ls.aerosolbinnumber', 'aerosolbinnumber')

