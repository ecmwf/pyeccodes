import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 174 and indicatorOfParameter == 96:
            return 3096

        if table2Version == 128 and indicatorOfParameter == 141:
            return 260056

    return wrapped
