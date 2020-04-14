import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get('discipline')
        parameterCategory = h.get('parameterCategory')
        parameterNumber = h.get('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'Total convective Precipitation'

    return wrapped
