import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('section8Length', 4))
    h.add(_.Position('offsetSection8'))
    h.add(_.Ascii('7777', 4))
    h.add(_.Section_pointer('section8Pointer', _.Get('offsetSection8'), _.Get('section8Length'), 8))
