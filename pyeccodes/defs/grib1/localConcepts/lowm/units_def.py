import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 201 and indicatorOfParameter == 233:
            return 'gpm'

        if table2Version == 201 and indicatorOfParameter == 235:
            return 'm**2 s**-2'

        if table2Version == 201 and indicatorOfParameter == 81:
            return 'Proportion'

        if table2Version == 201 and indicatorOfParameter == 232:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 206:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 166:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 165:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 208:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 243:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 151:
            return 'Pa'

    return wrapped
