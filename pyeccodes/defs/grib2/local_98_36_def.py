import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('offsetToEndOf4DvarWindow', 2))
    h.add(_.Unsigned('lengthOf4DvarWindow', 2))
    h.alias('anoffset', 'offsetToEndOf4DvarWindow')
