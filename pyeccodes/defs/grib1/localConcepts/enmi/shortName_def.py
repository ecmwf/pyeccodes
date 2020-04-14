import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 1 and indicatorOfParameter == 228:
            return 'gust'

        if table2Version == 1 and indicatorOfParameter == 225:
            return 'cape'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'tp'

    return wrapped
