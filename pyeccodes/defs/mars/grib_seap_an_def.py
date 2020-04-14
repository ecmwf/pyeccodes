import pyeccodes.accessors as _


def load(h):

    if (h.get_l('class') == 9):
        h.alias('mars.origin', 'centre')

