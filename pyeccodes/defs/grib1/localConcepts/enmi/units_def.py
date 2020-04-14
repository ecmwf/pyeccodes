import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 1 and indicatorOfParameter == 228:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 225:
            return 'J kg**-1'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'kg m**-2'

    return wrapped
