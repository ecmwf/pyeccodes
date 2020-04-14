import pyeccodes.accessors as _


def load(h):

    h.add(_.Transient('defaultFaFieldName', ""))
    h.add(_.Transient('defaultFaLevelName', ""))
    h.add(_.Transient('defaultFaModelName', ""))
    h.add(_.Concept('faFieldName', 'defaultFaFieldName', 'faFieldName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.alias('ls.faFieldName', 'faFieldName')
    h.add(_.Concept('faLevelName', 'defaultFaLevelName', 'faLevelName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.alias('ls.faLevelName', 'faLevelName')
    h.add(_.Concept('faModelName', 'defaultFaModelName', 'faModelName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.alias('ls.faModelName', 'faModelName')
    h.add(_.Transient('LSTCUM', 0))
    h.add(_.Transient('ZLMULT', 1))
    h.add(_.Transient('ZLBASE', 0))
    h.add(_.Transient('CLNOMA', ""))
    h.add(_.Transient('INGRIB', 0))
    h.add(_.Transient('LLCOSP', 0))
    h.add(_.Transient('INBITS', 0))
    h.add(_.Transient('FMULTM', 1))
    h.add(_.Transient('FMULTE', 0))
