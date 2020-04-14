import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 201 and indicatorOfParameter == 233:
            return 'Geopotential Height'

        if table2Version == 201 and indicatorOfParameter == 235:
            return 'Geopotential'

        if table2Version == 201 and indicatorOfParameter == 81:
            return 'Land-sea mask'

        if table2Version == 201 and indicatorOfParameter == 232:
            return 'Large-scale precipitation'

        if table2Version == 201 and indicatorOfParameter == 206:
            return '10 metre wind gust'

        if table2Version == 201 and indicatorOfParameter == 166:
            return '10 metre V wind component'

        if table2Version == 201 and indicatorOfParameter == 165:
            return '10 metre U wind component'

        if table2Version == 201 and indicatorOfParameter == 167:
            return '2 metre temperature'

        if table2Version == 201 and indicatorOfParameter == 168:
            return '2 metre dewpoint temperature'

        if table2Version == 201 and indicatorOfParameter == 208:
            return 'Total precipitation'

        if table2Version == 201 and indicatorOfParameter == 243:
            return 'Convective inhibition'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'Convective available potential energy'

        if table2Version == 201 and indicatorOfParameter == 151:
            return 'Mean sea level pressure'

    return wrapped
