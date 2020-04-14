import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get('table2Version')
        indicatorOfParameter = h.get('indicatorOfParameter')

        if table2Version == 128 and indicatorOfParameter == 141:
            return 260056

        if table2Version == 174 and indicatorOfParameter == 96:
            return 3096

    return wrapped
