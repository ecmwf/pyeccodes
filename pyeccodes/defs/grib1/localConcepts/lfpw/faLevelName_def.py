import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        indicatorOfParameter = h.get('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get('indicatorOfTypeOfLevel')
        table2Version = h.get('table2Version')

        if indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 105 and table2Version == 255:
            return 'H'

        ZLMULT = h.get('ZLMULT')

        if ZLMULT == 0.01 and indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 100 and table2Version == 255:
            return 'P'

        if ZLMULT == 100 and indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 117 and table2Version == 255:
            return 'V'

        ZLBASE = h.get('ZLBASE')

        if ZLBASE == 15 and ZLMULT == 100 and indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 115 and table2Version == 255:
            return 'KT'

        if ZLBASE == 15 and ZLMULT == 100 and indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 115 and table2Version == 255:
            return 'KB'

        if indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 255 and table2Version == 255:
            return 'default'

    return wrapped
