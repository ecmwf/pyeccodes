import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        table2Version = h.get_l('table2Version')

        if indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 255 and table2Version == 255:
            return 'default'

        ZLBASE = h.get_l('ZLBASE')
        ZLMULT = h.get_l('ZLMULT')

        if ZLBASE == 15 and ZLMULT == 100 and indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 115 and table2Version == 255:
            return 'KB'

        if ZLBASE == 15 and ZLMULT == 100 and indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 115 and table2Version == 255:
            return 'KT'

        if ZLMULT == 100 and indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 117 and table2Version == 255:
            return 'V'

        if ZLMULT == 0.01 and indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 100 and table2Version == 255:
            return 'P'

        if indicatorOfParameter == 255 and indicatorOfTypeOfLevel == 105 and table2Version == 255:
            return 'H'

    return wrapped
