import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1:
            return 260242

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15:
            return 168

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1:
            return 167

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')
        lengthOfTimeRange = h.get_l('lengthOfTimeRange')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 122

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 121

        is_uerra = h.get_l('is_uerra')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and typeOfStatisticalProcessing == 3:
            return 202

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 15 and typeOfStatisticalProcessing == 2 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1:
            return 201

    return wrapped
