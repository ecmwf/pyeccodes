import pyeccodes.accessors as _


def load(h):

    h.add(_.Transient('dummyc', 0))
    h.add(_.Constant('conceptsMasterDir', "grib2"))
    h.add(_.Constant('conceptsLocalDirAll', "grib2/localConcepts/[centre:s]"))
    h.add(_.Constant('conceptsLocalDirECMF', "grib2/localConcepts/ecmf"))
    h.add(_.Concept('paramIdECMF', 'defaultParameter', 'paramId.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('paramId', 'paramIdECMF', 'paramId.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('shortNameECMF', 'defaultShortName', 'shortName.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('shortName', 'shortNameECMF', 'shortName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.alias('ls.shortName', 'shortName')
    h.add(_.Concept('unitsECMF', 'defaultName', 'units.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('units', 'unitsECMF', 'units.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('nameECMF', 'defaultName', 'name.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('name', 'nameECMF', 'name.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('cfNameECMF', 'defaultShortName', 'cfName.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('cfName', 'cfNameECMF', 'cfName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('cfVarNameECMF', 'defaultShortName', 'cfVarName.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('cfVarName', 'cfVarNameECMF', 'cfVarName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('modelName', 'defaultName', 'modelName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    _.Template('grib2/products_[productionStatusOfProcessedData].def', True).load(h)
    h.add(_.Ifs_param('ifsParam', _.Get('paramId'), _.Get('type')))
