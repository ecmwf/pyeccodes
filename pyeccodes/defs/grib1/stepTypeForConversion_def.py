import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        dummy = h.get_l('dummy')

        if dummy == 0:
            return 'unknown'

    return wrapped
