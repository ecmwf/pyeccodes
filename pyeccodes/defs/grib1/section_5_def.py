import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection5'))
    h.add(_.Constant('section5Length', 4))
    h.add(_.Section_pointer('section5Pointer', _.Get('offsetSection5'), _.Get('section5Length'), 5))
    h.add(_.Ascii('7777', 4))
