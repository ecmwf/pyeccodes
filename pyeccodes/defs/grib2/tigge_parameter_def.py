import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106:
            return 228171

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 132

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'default'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 131

        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')
        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')
        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and scaledValueOfLowerLimit == 20 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 131063

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and scaledValueOfLowerLimit == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 131062

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 228228

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 136

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228164

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 146

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 177

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 176

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 147

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 8 and typeOfStatisticalProcessing == 1:
            return 179

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 100:
            return 130

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 134

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103:
            return 167

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3:
            return 122

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 121

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103:
            return 168

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 189

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 100:
            return 133

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106:
            return 228139

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106:
            return 228039

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 228144

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 228141

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 235

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 171034

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 320 and typeOfFirstFixedSurface == 107:
            return 60

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 6 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 109:
            return 3

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 228002

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 101:
            return 151

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 49

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 172

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfFirstFixedSurface == 100:
            return 156

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106:
            return 228170

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228001

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 59

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and productDefinitionTemplateNumber == 9 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and scaledValueOfLowerLimit == 25 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 131071

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and productDefinitionTemplateNumber == 9 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and scaledValueOfLowerLimit == 15 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 131070

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103:
            return 166

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103:
            return 165

    return wrapped
