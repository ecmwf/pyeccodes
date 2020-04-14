import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get('discipline')
        parameterCategory = h.get('parameterCategory')
        parameterNumber = h.get('parameterNumber')
        typeOfSecondFixedSurface = h.get('typeOfSecondFixedSurface')
        typeOfFirstFixedSurface = h.get('typeOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 94001224

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 94001225

    return wrapped