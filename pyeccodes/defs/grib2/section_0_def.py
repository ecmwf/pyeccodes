import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection0'))
    h.add(_.Constant('section0Length', 16))
    h.add(_.Ascii('identifier', 4))
    h.add(_.Unsigned('reserved', 2))
    h.add(_.Codetable('discipline', 1, "0.0.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('editionNumber', 1))
    h.alias('ls.edition', 'editionNumber')
    h.add(_.Section_length('totalLength', 8))
    h.add(_.Position('startOfHeaders'))
    h.add(_.Section_pointer('section0Pointer', _.Get('offsetSection0'), _.Get('section0Length'), 0))
