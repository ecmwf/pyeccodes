import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get('discipline')
        parameterCategory = h.get('parameterCategory')
        parameterNumber = h.get('parameterNumber')
        scaledValueOfFirstFixedSurface = h.get('scaledValueOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get('typeOfStatisticalProcessing')
        is_uerra = h.get('is_uerra')
        typeOfFirstFixedSurface = h.get('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get('scaleFactorOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 15 and typeOfStatisticalProcessing == 2 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1:
            return 201

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and typeOfStatisticalProcessing == 3:
            return 202

        indicatorOfUnitForTimeRange = h.get('indicatorOfUnitForTimeRange')
        lengthOfTimeRange = h.get('lengthOfTimeRange')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 121

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 122

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1:
            return 167

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15:
            return 168

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1:
            return 260242

    return wrapped
