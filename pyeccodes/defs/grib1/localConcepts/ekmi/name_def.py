import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 1 and indicatorOfParameter == 224:
            return 'Convective inhibition'

        if table2Version == 1 and indicatorOfParameter == 225:
            return 'Convective available potential energy'

        if table2Version == 1 and indicatorOfParameter == 228:
            return '10 metre wind gust'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'Total precipitation'

    return wrapped
