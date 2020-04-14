import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get('table2Version')
        indicatorOfParameter = h.get('indicatorOfParameter')

        if table2Version == 128 and indicatorOfParameter == 141:
            return 'Snow Depth'

        if table2Version == 174 and indicatorOfParameter == 96:
            return 'V-component of ice drift'

    return wrapped
