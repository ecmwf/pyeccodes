import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        dummy = h.get('dummy')

        if dummy == 0:
            return 'unknown'

    return wrapped
