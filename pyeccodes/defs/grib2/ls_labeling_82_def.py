import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('g1conceptsMasterDir', "grib1"))
    h.add(_.Constant('g1conceptsLocalDirAll', "grib1/localConcepts/[centre:s]"))
    h.alias('ls.dataType', 'marsType')

    if (h.get_l('localDefinitionNumber') == 83):
        h.add(_.Concept('timerepres', 'unknown', 'timeRepresConcept.def', 'g1conceptsLocalDirAll', 'g1conceptsMasterDir', True))
        h.alias('ls.timerepres', 'timerepres')
        h.add(_.Concept('sort', 'unknown', 'sortConcept.def', 'g1conceptsLocalDirAll', 'g1conceptsMasterDir', True))
        h.alias('ls.sort', 'sort')
        h.add(_.Concept('landtype', 'unknown', 'landTypeConcept.def', 'g1conceptsLocalDirAll', 'g1conceptsMasterDir', True))
        h.alias('ls.landtype', 'landtype')
        h.add(_.Concept('aerosolbinnumber', 'unknown', 'aerosolConcept.def', 'g1conceptsLocalDirAll', 'g1conceptsMasterDir', True))
        h.alias('ls.aerosolbinnumber', 'aerosolbinnumber')

