import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get('table2Version')
        indicatorOfParameter = h.get('indicatorOfParameter')

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'Total precipitation'

        if table2Version == 1 and indicatorOfParameter == 228:
            return '10 metre wind gust'

        if table2Version == 1 and indicatorOfParameter == 225:
            return 'Convective available potential energy'

        if table2Version == 1 and indicatorOfParameter == 224:
            return 'Convective inhibition'

    return wrapped
