import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get('discipline')
        parameterCategory = h.get('parameterCategory')
        parameterNumber = h.get('parameterNumber')
        typeOfFirstFixedSurface = h.get('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get('scaledValueOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get('typeOfStatisticalProcessing')
        is_uerra = h.get('is_uerra')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and typeOfStatisticalProcessing == 2 and is_uerra == 1:
            return 'mx2t'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15:
            return 'mn2t'

        indicatorOfUnitForTimeRange = h.get('indicatorOfUnitForTimeRange')
        lengthOfTimeRange = h.get('lengthOfTimeRange')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'mx2t6'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'mn2t6'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1:
            return '2t'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15:
            return '2d'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1:
            return '2r'

    return wrapped
