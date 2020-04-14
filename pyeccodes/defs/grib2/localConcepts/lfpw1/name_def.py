import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'Total convective Precipitation'

    return wrapped
