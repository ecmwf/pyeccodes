import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 201 and indicatorOfParameter == 233:
            return 'gh'

        if table2Version == 201 and indicatorOfParameter == 235:
            return 'z'

        if table2Version == 201 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 201 and indicatorOfParameter == 232:
            return 'lsp'

        if table2Version == 201 and indicatorOfParameter == 206:
            return 'gust'

        if table2Version == 201 and indicatorOfParameter == 166:
            return '10v'

        if table2Version == 201 and indicatorOfParameter == 165:
            return '10u'

        if table2Version == 201 and indicatorOfParameter == 167:
            return '2t'

        if table2Version == 201 and indicatorOfParameter == 168:
            return '2d'

        if table2Version == 201 and indicatorOfParameter == 208:
            return 'tp'

        if table2Version == 201 and indicatorOfParameter == 243:
            return 'cin'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'cape'

        if table2Version == 201 and indicatorOfParameter == 151:
            return 'msl'

    return wrapped
