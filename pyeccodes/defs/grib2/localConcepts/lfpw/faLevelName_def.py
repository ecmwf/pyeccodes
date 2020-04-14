import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

        if typeOfFirstFixedSurface == 255 and typeOfSecondFixedSurface == 255:
            return 'default'

        ZLBASE = h.get_l('ZLBASE')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

        if ZLBASE == 0.15 and parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255:
            return 'KB'

        if ZLBASE == 0.15 and parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255:
            return 'KT'

        if parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255:
            return 'T'

        if parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 109 and typeOfSecondFixedSurface == 255:
            return 'V'

        ZLMULT = h.get_l('ZLMULT')

        if ZLMULT == 0.01 and parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 255:
            return 'P'

        if parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfSecondFixedSurface == 255:
            return 'H'

        if parameterCategory == 255 and parameterNumber == 255 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 119 and typeOfSecondFixedSurface == 255:
            return 'S'

    return wrapped
