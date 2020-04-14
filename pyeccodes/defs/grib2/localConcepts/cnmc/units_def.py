import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        instrumentType = h.get_l('instrumentType')
        satelliteSeries = h.get_l('satelliteSeries')
        scaledValueOfCentralWaveNumber = h.get_l('scaledValueOfCentralWaveNumber')
        satelliteNumber = h.get_l('satelliteNumber')
        typeOfGeneratingProcess = h.get_l('typeOfGeneratingProcess')

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 136986 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 83333:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 1250000 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 1666666 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 625000:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and scaledValueOfCentralWaveNumber == 2000000 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333:
            return 'Numeric'

        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 198 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 198 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 198 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and scaledValueOfFirstFixedSurface == 10:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197 and typeOfFirstFixedSurface == 106:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfGeneratingProcess == 197 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 100 and scaledValueOfSecondFixedSurface == 400 and typeOfSecondFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197 and scaleFactorOfSecondFixedSurface == -2:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaledValueOfSecondFixedSurface == 800 and typeOfSecondFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400 and typeOfFirstFixedSurface == 100:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197 and scaledValueOfFirstFixedSurface == 800 and typeOfFirstFixedSurface == 100:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 3 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 136986 and satelliteNumber == 72:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 82644 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 136986 and satelliteNumber == 72:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72 and instrumentType == 207:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 82644 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 136986:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and scaledValueOfCentralWaveNumber == 82644 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 136986 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 82644 and satelliteNumber == 72:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 54:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 54:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 54:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 53:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteNumber == 53 and instrumentType == 205 and satelliteSeries == 331:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 53 and instrumentType == 205 and satelliteSeries == 331:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 52:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteNumber == 52 and instrumentType == 205 and satelliteSeries == 331:
            return 'W m sr m**-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 52:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 52 and instrumentType == 205 and satelliteSeries == 331:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Pa s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfGeneratingProcess == 199 and typeOfStatisticalProcessing == 5:
            return 'Pa s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfGeneratingProcess == 199 and typeOfStatisticalProcessing == 5:
            return '%'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfGeneratingProcess == 199 and typeOfStatisticalProcessing == 5:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'Pa'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return '~'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 107 and scaleFactorOfFirstFixedSurface == -2:
            return 'Pa'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14 and typeOfFirstFixedSurface == 107:
            return 'K m**2 kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 25 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 's**-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 105:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return '~'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfFirstFixedSurface == 1:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 227:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 226:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 225:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 224:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 223:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 222:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 221:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 220:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 219:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 218:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 217:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 216:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 215:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 214:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 213:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 212:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 211:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 210:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 209:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 208:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 207:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 206:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 205:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 204:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 203:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 202:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 201:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 200:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 199:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 198:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 197:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 196:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 195:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 194:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 193:
            return 'Bq m**-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 192:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 200 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'Degree E'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'Degree N'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 's**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 's**-1 m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 's**-1'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 196 and typeOfStatisticalProcessing == 0:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 196:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195 and typeOfStatisticalProcessing == 0:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194 and typeOfStatisticalProcessing == 0:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192 and typeOfStatisticalProcessing == 0:
            return '~'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 2:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 30 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 29 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and scaledValueOfSecondFixedSurface == 100 and typeOfSecondFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2 and typeOfStatisticalProcessing == 7 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 106:
            return 'kg**2 m**-4'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and scaledValueOfSecondFixedSurface == 10 and typeOfSecondFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2 and typeOfStatisticalProcessing == 7 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 106:
            return 'kg**2 m**-4'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 3:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'Pa'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'Pa'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 32 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21 and typeOfFirstFixedSurface == 1:
            return 'radians'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfGeneratingProcess == 7 and typeOfStatisticalProcessing == 6:
            return 'gpm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 199:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 198:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 197:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 196:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 195:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 194:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 194 and typeOfFirstFixedSurface == 101:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 193:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 193 and typeOfFirstFixedSurface == 101:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 192:
            return 'Degree true'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206 and typeOfFirstFixedSurface == 1:
            return 's**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 10:
            return 'dB'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'dB'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'dB'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16 and typeOfFirstFixedSurface == 1:
            return 's m**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 'K'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 'Bq m**-3'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 19 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'm**2 s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 31 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm**2 s**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 24:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 192:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 192:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 193:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 193:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 's**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 's**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 1:
            return 'kg m**-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return '~'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 200 and typeOfFirstFixedSurface == 4:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27 and typeOfFirstFixedSurface == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193 and typeOfFirstFixedSurface == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192 and typeOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 78 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 74:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 's m**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'W m**-2'

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

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == -2 and typeOfStatisticalProcessing == 1 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 10:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 190 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 100 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 100 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2 and scaleFactorOfFirstFixedSurface == -2:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == -2 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 10 and typeOfFirstFixedSurface == 106:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 190 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 9 and scaleFactorOfFirstFixedSurface == -2:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 41:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 36:
            return 'K'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return '(0 - 1)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == -2:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 400 and scaleFactorOfSecondFixedSurface == -2 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 800:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 800 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'Pa s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'degrees'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10:
            return 'degrees'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return '~'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return '~'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return '~'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2:
            return '~'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 0 and scaleFactorOfFirstFixedSurface == 0:
            return '~'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 3 and scaleFactorOfFirstFixedSurface == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 2 and scaleFactorOfFirstFixedSurface == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 9 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'Dobson'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'Pa s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 101:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Pa'

        is_s2s = h.get_l('is_s2s')
        subCentre = h.get_l('subCentre')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and is_s2s == 1 and typeOfFirstFixedSurface == 103 and subCentre == 102:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0 and subCentre == 102 and is_s2s == 1:
            return '(0 - 1)'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return '(0 - 1)'

    return wrapped
