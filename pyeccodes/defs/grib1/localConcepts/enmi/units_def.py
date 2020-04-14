import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get('table2Version')
        indicatorOfParameter = h.get('indicatorOfParameter')

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 225:
            return 'J kg**-1'

        if table2Version == 1 and indicatorOfParameter == 228:
            return 'm s**-1'

    return wrapped
