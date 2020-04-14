import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get('table2Version')
        indicatorOfParameter = h.get('indicatorOfParameter')

        if table2Version == 1 and indicatorOfParameter == 61:
            return 94001061

        if table2Version == 1 and indicatorOfParameter == 228:
            return 94001228

        if table2Version == 1 and indicatorOfParameter == 225:
            return 94001225

        if table2Version == 1 and indicatorOfParameter == 224:
            return 94001224

    return wrapped
