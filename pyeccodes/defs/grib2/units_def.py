import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2'

        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106:
            return 'kg m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1:
            return 'kg m**-3'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        is_tigge = h.get_l('is_tigge')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and is_tigge == 1:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and is_tigge == 1:
            return 'kg m**-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'kg m**-3'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'J kg**-1'

        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')
        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')
        scaleFactorOfLowerLimit = h.get_l('scaleFactorOfLowerLimit')
        probabilityType = h.get_l('probabilityType')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 2 and scaledValueOfLowerLimit == 20 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and scaleFactorOfLowerLimit == 0 and scaleFactorOfFirstFixedSurface == 0 and probabilityType == 3:
            return '%'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and probabilityType == 3 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == 0 and typeOfStatisticalProcessing == 2 and scaledValueOfLowerLimit == 15 and scaledValueOfFirstFixedSurface == 10:
            return '%'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'J'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'W m**-3 sr**-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'W m**-1 sr**-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'W m**-2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16:
            return 'kg m**-2'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 's**-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'kg m**-3'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 'kg kg**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 'K'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'kg m**-2'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 's**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 's**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 's**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 's**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 's**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'm**2 s**-2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return '~'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return '~'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return '~'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 'Pa'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return '~'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return '~'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 'K m**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2:
            return 'Pa s**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return '%'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 's'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'Degree true'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return 's**-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 8:
            return 'Degree'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 'Degree'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 'm s**-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 'm s**-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 'Code table 4.219'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 'm'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 'kg m**-2 s**-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 'kg m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 16:
            return 'm**3 m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 15:
            return 'm**3 m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 14:
            return 'kg m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 13:
            return 'm**3 m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12:
            return 'kg m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 11:
            return 'm**3 m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 10:
            return 'm**3 m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 9:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 8:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 7:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 5:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 4:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 3:
            return 'kg m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 2:
            return 'kg m**-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 1:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 'm**3 m**-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 'm**3 m**-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 19:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 's m**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 'm s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 'kg m**-2 s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 10:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 'code table (4.212)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 'kg**-2 s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'Proportion'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return '%'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return '%'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return '(code table 4.216)'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return '(code table 4.215)'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 's'

        if discipline == 0 and parameterCategory == 190 and parameterNumber == 0:
            return 'CCITTIA5'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 17:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 'code table (4.211)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 'code table (4.210)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 'code table (4.209)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 'code table (4.208)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'code table (4.207)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 6:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 5:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 'code table (4.206)'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 8:
            return 'Bq s m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 7:
            return 'Bq s m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 6:
            return 'Bq s m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 5:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 4:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 3:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 2:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 1:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 0:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 'dB'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 'kg m**-1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 'dB'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 'DU'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0:
            return 'DU'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'code table (4.205)'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 21:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 19:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 18:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 17:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 16:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 15:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 10:
            return 'code table (4.204)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 9:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 8:
            return 'code table (4.203)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pa'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 's**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 57:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 48:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 47:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 38:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return '(Code table 4.222)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return '(Code table 4.222)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return '(Code table 4.222)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return '(Code table 4.222)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 'code table (4.202)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 29:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 28:
            return 'kg m**-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 27:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 21:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 20:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 19:
            return 'code table (4.201)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18:
            return 'kg m**-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 17:
            return 'day'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'Pa'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 14:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 's'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'J m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return '(0 - 1)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'gpm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 's**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 101:
            return 'Pa'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 's**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'Pa s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'm**2 s**-2'

        is_uerra = h.get_l('is_uerra')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')
        lengthOfTimeRange = h.get_l('lengthOfTimeRange')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'K m**2 kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pa'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'm**2 s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'm**2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 20 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and productDefinitionTemplateNumber == 9:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 10 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and scaleFactorOfLowerLimit == 0:
            return '%'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 34:
            return 'kg m**-2'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 21 and typeOfSecondFixedSurface == 160 and typeOfFirstFixedSurface == 160 and scaledValueOfSecondFixedSurface == 300 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 0:
            return 'psu'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 29315 and scaleFactorOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'm'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3 and typeOfFirstFixedSurface == 160:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 160:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 's'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'Degree true'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'K'

        if discipline == 20 and parameterCategory == 2 and parameterNumber == 0:
            return 'Person m**-2'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 9:
            return 'Fraction'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 8:
            return 'Number m**-2'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 7:
            return 'Fraction'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 6:
            return 'Fraction'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 5:
            return 'Fraction'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 4:
            return 'Fraction'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 3:
            return 'Bites per day per person'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 2:
            return 'Bites per day per person'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 1:
            return 'Fraction'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 0:
            return 'Fraction'

        if discipline == 20 and parameterCategory == 0 and parameterNumber == 1:
            return 'K'

        if discipline == 20 and parameterCategory == 0 and parameterNumber == 0:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 23:
            return 'dimensionless'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 22:
            return 'dimensionless'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 21:
            return 'dimensionless'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 20:
            return 'dimensionless'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 19:
            return 'm s**-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17:
            return 'W m**-1 sr**-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16:
            return 'W m**-1 sr**-1'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 11:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 10:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 9:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 8:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 7:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 5:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 9:
            return 'Code table 4.223'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 8:
            return 'Code table 4.218'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 'Code table 4.217'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 5:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 4:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 3:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 0:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14:
            return 'K'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 16 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 177:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 8 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 53 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'J m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 27:
            return 'm'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 16:
            return 'kg m**-2 s**-1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 26:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 8:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 53:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 52:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18:
            return 'K'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 28:
            return 'm**2/3 s**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 29:
            return 'm**2/3 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 121:
            return 'Proportion'

        is_efas = h.get_l('is_efas')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and is_efas == 1 and lengthOfTimeRange == 24:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and is_efas == 1 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 24 and is_uerra == 0 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and lengthOfTimeRange == 6 and is_uerra == 0 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 13 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 14:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 13:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'Degree true'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return '%'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 21:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return '%'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 9:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 8:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 25:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7 and lengthOfTimeRange == 24 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'm**3 s**-1'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7 and lengthOfTimeRange == 6 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0:
            return 'm**3 s**-1'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 15:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 14:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 13:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 24:
            return 'K'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 3:
            return 'Integer'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 2:
            return '(0 - 1)'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 12:
            return 'm**3'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 11:
            return 'm**3'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7:
            return 'm**3 s**-1'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 10:
            return 'm**3 s**-1 m**-1'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 13:
            return 'm**2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20 and typeOfStatisticalProcessing == 0:
            return 'm**2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 0:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 30 and typeOfStatisticalProcessing == 0:
            return 'kg m**-3 s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 29 and typeOfStatisticalProcessing == 0:
            return 'kg m**-3 s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 28 and typeOfStatisticalProcessing == 0:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 27 and typeOfStatisticalProcessing == 0:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 40 and typeOfStatisticalProcessing == 0:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 39 and typeOfStatisticalProcessing == 0:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 108 and typeOfStatisticalProcessing == 0:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 26 and typeOfStatisticalProcessing == 0:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 25 and typeOfStatisticalProcessing == 0:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 24 and typeOfStatisticalProcessing == 0:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 23 and typeOfStatisticalProcessing == 0:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 22 and typeOfStatisticalProcessing == 0:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 200:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 200 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 200 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 33:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfSecondFixedSurface == 10 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and scaleFactorOfSecondFixedSurface == 1 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaledValueOfSecondFixedSurface == 10 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg m**-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and scaleFactorOfSecondFixedSurface == 1 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg m**-3'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6 and typeOfFirstFixedSurface == 1:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 3 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 6 and typeOfSecondFixedSurface == 8:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 3:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 120:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 119:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 118:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and lengthOfTimeRange == 1 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 1:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 93 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return '%'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 19 and lengthOfTimeRange == 6 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfSecondFixedSurface == 8:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 37:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 36:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 19:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 94:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 93:
            return '%'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and is_uerra == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 3:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20 and scaledValueOfFirstFixedSurface == 27315 and scaleFactorOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20 and scaledValueOfFirstFixedSurface == 26315 and scaleFactorOfFirstFixedSurface == 2:
            return 'm'

        aerosolType = h.get_l('aerosolType')
        is_aerosol = h.get_l('is_aerosol')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and aerosolType == 62003 and is_aerosol == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and aerosolType == 62003 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and is_aerosol == 1 and aerosolType == 62003:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 62003 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 62003 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        scaledValueOfFirstWavelength = h.get_l('scaledValueOfFirstWavelength')
        typeOfWavelengthInterval = h.get_l('typeOfWavelengthInterval')
        scaleFactorOfFirstWavelength = h.get_l('scaleFactorOfFirstWavelength')
        is_aerosol_optical = h.get_l('is_aerosol_optical')
        typeOfSizeInterval = h.get_l('typeOfSizeInterval')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and scaledValueOfFirstWavelength == 55 and typeOfWavelengthInterval == 11 and aerosolType == 62003 and scaleFactorOfFirstWavelength == 8 and is_aerosol_optical == 1 and typeOfSizeInterval == 255:
            return 'dimensionless'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfWavelengthInterval == 11 and aerosolType == 62004 and typeOfSizeInterval == 255 and scaleFactorOfFirstWavelength == 8 and is_aerosol_optical == 1 and scaledValueOfFirstWavelength == 55:
            return 'dimensionless'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and is_aerosol == 1 and aerosolType == 62003:
            return 'kg kg**-1'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and scaledValueOfFirstFixedSurface == 1 and typeOfFirstFixedSurface == 169 and typeOfSecondFixedSurface == 255 and scaleFactorOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 3 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'psu'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 15 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 'K'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 18 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == -2 and productDefinitionTemplateNumber == 9 and probabilityType == 0 and typeOfStatisticalProcessing == 10:
            return '%'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 10 and scaleFactorOfLowerLimit == 1 and scaledValueOfLowerLimit == -15 and productDefinitionTemplateNumber == 9 and probabilityType == 0:
            return '%'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and probabilityType == 0 and typeOfStatisticalProcessing == 10 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == -1 and productDefinitionTemplateNumber == 9:
            return '%'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 10 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 2:
            return '%'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfLowerLimit == 1 and scaledValueOfLowerLimit == 15 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 10:
            return '%'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfLowerLimit == 1 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 10 and scaleFactorOfLowerLimit == 0:
            return '%'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and probabilityType == 3 and typeOfStatisticalProcessing == 2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 10 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 103:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 50 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 25 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 32:
            return '(0 - 1)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 84:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 83:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and is_uerra == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 1 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 37:
            return 'N m**-2 s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 38:
            return 'N m**-2 s'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'J m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 32:
            return 's**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfFirstFixedSurface == 103 and is_uerra == 1 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2:
            return 'm s**-1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0:
            return '~'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 'kg m**-3'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return '(0 - 1)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 45:
            return 's**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 31:
            return '~'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 28:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 200 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and is_uerra == 1:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and probabilityType == 3 and scaledValueOfLowerLimit == 3 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == -2:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 200 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 150 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and scaleFactorOfLowerLimit == 0:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 100 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 80 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and scaledValueOfLowerLimit == 60 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 40 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 5 and productDefinitionTemplateNumber == 9:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 1:
            return '%'

    return wrapped
