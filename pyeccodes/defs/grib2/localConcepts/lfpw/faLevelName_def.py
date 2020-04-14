import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        parameterCategory = h.get('parameterCategory')
        parameterNumber = h.get('parameterNumber')
        scaleFactorOfFirstFixedSurface = h.get('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get('scaledValueOfFirstFixedSurface')
        typeOfFirstFixedSurface = h.get('typeOfFirstFixedSurface')
        typeOfSecondFixedSurface = h.get('typeOfSecondFixedSurface')

        if parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 119 and typeOfSecondFixedSurface == 255:
            return 'S'

        if parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfSecondFixedSurface == 255:
            return 'H'

        ZLMULT = h.get('ZLMULT')

        if ZLMULT == 0.01 and parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 255:
            return 'P'

        if parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 109 and typeOfSecondFixedSurface == 255:
            return 'V'

        if parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255:
            return 'T'

        ZLBASE = h.get('ZLBASE')

        if ZLBASE == 0.15 and parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255:
            return 'KT'

        if ZLBASE == 0.15 and parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255:
            return 'KB'

        if typeOfFirstFixedSurface == 255 and typeOfSecondFixedSurface == 255:
            return 'default'

    return wrapped
