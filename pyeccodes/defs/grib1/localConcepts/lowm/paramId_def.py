import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 201 and indicatorOfParameter == 233:
            return 156

        if table2Version == 201 and indicatorOfParameter == 235:
            return 129

        if table2Version == 201 and indicatorOfParameter == 81:
            return 172

        if table2Version == 201 and indicatorOfParameter == 232:
            return 3062

        if table2Version == 201 and indicatorOfParameter == 206:
            return 228028

        if table2Version == 201 and indicatorOfParameter == 166:
            return 166

        if table2Version == 201 and indicatorOfParameter == 165:
            return 165

        if table2Version == 201 and indicatorOfParameter == 167:
            return 167

        if table2Version == 201 and indicatorOfParameter == 168:
            return 168

        if table2Version == 201 and indicatorOfParameter == 208:
            return 228228

        if table2Version == 201 and indicatorOfParameter == 243:
            return 228001

        if table2Version == 201 and indicatorOfParameter == 238:
            return 59

        if table2Version == 201 and indicatorOfParameter == 151:
            return 151

    return wrapped
