import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get('table2Version')
        indicatorOfParameter = h.get('indicatorOfParameter')

        if table2Version == 128 and indicatorOfParameter == 141:
            return 'm of water equivalent'

        if table2Version == 174 and indicatorOfParameter == 96:
            return 'm s**-1'

    return wrapped
