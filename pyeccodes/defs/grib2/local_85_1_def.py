import pyeccodes.accessors as _


def load(h):

    h.add(_.Transient('defaultFaFieldName', ""))
    h.add(_.Transient('defaultFaLevelName', ""))
    h.add(_.Transient('defaultFaModelName', ""))
    h.add(_.Concept('faFieldName', 'defaultFaFieldName', 'faFieldName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('faLevelName', 'defaultFaLevelName', 'faLevelName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('faModelName', 'defaultFaModelName', 'faModelName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Transient('LSTCUM', 0))
    h.add(_.Transient('ZLMULT', 1))
    h.add(_.Transient('ZLBASE', 0))
    h.add(_.Ascii('CLNOMA', 16))
    h.add(_.Unsigned('INGRIB', 8))
    h.add(_.Unsigned('LLCOSP', 8))
    h.add(_.Unsigned('INBITS', 8))
    h.add(_.Signed('FMULTM', 8))
    h.add(_.Signed('FMULTE', 8))
