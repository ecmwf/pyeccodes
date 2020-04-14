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
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 83333:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 1250000 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Obser. Sat. Meteosat sec. generation Albedo (scaled)'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 1666666 and satelliteNumber == 72 and typeOfGeneratingProcess == 8:
            return 'Obser. Sat. Meteosat sec. generation Albedo (scaled)'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 625000:
            return 'Obser. Sat. Meteosat sec. generation Albedo (scaled)'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and scaledValueOfCentralWaveNumber == 2000000 and satelliteNumber == 72 and typeOfGeneratingProcess == 8 and instrumentType == 207 and satelliteSeries == 333:
            return 'Obser. Sat. Meteosat sec. generation Albedo (scaled)'

        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 198 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2:
            return 'calibrated forecast, wind speed (gust)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 198 and typeOfStatisticalProcessing == 1:
            return 'calibrated forecast, large-scale snowfall rate w.e.'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 198 and typeOfStatisticalProcessing == 1:
            return 'calibrated forecast, total precipitation rate'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and scaledValueOfFirstFixedSurface == 10:
            return 'smoothed forecast, wind speed (gust)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197 and typeOfFirstFixedSurface == 106:
            return 'smoothed forecast, soil temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfGeneratingProcess == 197 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'smoothed forecast, large-scale snowfall rate w.e.'

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 400 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197 and scaleFactorOfSecondFixedSurface == -2:
            return 'smoothed forecast, cloud cover high'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 800 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400:
            return 'smoothed forecast, cloud cover medium'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 1 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197 and scaledValueOfFirstFixedSurface == 800:
            return 'smoothed forecast, cloud cover low'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, total cloud cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197 and typeOfStatisticalProcessing == 1:
            return 'smoothed forecast, total precipitation rate'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0:
            return 'smoothed forecast, v comp. of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'smoothed forecast, u comp. of wind'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103:
            return 'smoothed forecast, dew point temp.'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 3 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103:
            return 'smoothed forecast, minimum temp.'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103:
            return 'smoothed forecast, maximum temp.'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == 0:
            return 'smoothed forecast, temperature'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 136986 and satelliteNumber == 72:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 82644 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 136986 and satelliteNumber == 72:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72 and instrumentType == 207:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 82644 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 136986:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and scaledValueOfCentralWaveNumber == 82644 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 136986 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 161290 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 103092 and satelliteNumber == 72:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 114942 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 256410 and satelliteNumber == 72:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 74626 and satelliteNumber == 72:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and satelliteSeries == 333 and scaledValueOfCentralWaveNumber == 82644 and satelliteNumber == 72:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 92592 and satelliteNumber == 72 and instrumentType == 207 and satelliteSeries == 333:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 54:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 54:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 54:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 53:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteNumber == 53 and instrumentType == 205 and satelliteSeries == 331:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 53 and instrumentType == 205 and satelliteSeries == 331:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 52:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteNumber == 52 and instrumentType == 205 and satelliteSeries == 331:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 52:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 52 and instrumentType == 205 and satelliteSeries == 331:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return 'Monthly Mean of RMS of difference IA-AN of kinetic energy'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'Monthly Mean of RMS of difference FG-AN of kinetic energy'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of vert.velocity (pressure)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfGeneratingProcess == 199 and typeOfStatisticalProcessing == 5:
            return 'Monthly Mean of RMS of difference FG-AN of vert.velocity (pressure)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'Monthly Mean of RMS of difference FG-AN of temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return 'Monthly Mean of RMS of difference IA-AN of relative humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfGeneratingProcess == 199 and typeOfStatisticalProcessing == 5:
            return 'Monthly Mean of RMS of difference FG-AN of relative humidity'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of geopotential'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'Monthly Mean of RMS of difference FG-AN of geopotential'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return 'Monthly Mean of RMS of difference IA-AN of v-component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'Monthly Mean of RMS of difference FG-AN of v-component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of u-component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfGeneratingProcess == 199 and typeOfStatisticalProcessing == 5:
            return 'Monthly Mean of RMS of difference FG-AN of u-component of wind'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return 'Monthly Mean of RMS of difference IA-AN of pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'Monthly Mean of RMS of difference FG-AN of pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199 and typeOfFirstFixedSurface == 1:
            return 'modified cloud cover for media'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198 and typeOfFirstFixedSurface == 1:
            return 'modified cloud depth for media'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'Icing Grade (1=LGT,2=MOD,3=SEV)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13 and typeOfFirstFixedSurface == 1:
            return 'Ceiling'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'Aequivalentpotentielle Temperatur'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'KO index'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 107 and scaleFactorOfFirstFixedSurface == -2:
            return 'Druck einer isentropen Flaeche'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14 and typeOfFirstFixedSurface == 107:
            return 'Isentrope potentielle Vorticity'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 25 and typeOfFirstFixedSurface == 1:
            return 'weather interpretation (WMO)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfFirstFixedSurface == 1:
            return 'Konv.-U-Grenze-nn   Hoehe der Konvektionsuntergrenze ueber nn'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'absolute vorticity advection'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'storm relative helicity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 105:
            return 'wind shear'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 'UV_Index_Maximum_W  UV_Index clouded (W), daily maximum'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfFirstFixedSurface == 1:
            return 'Gravity wave dissipation (vertical integral)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'Gravity wave dissipation (vertical integral)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'v-momentum flux due to SSO-effects'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'v-momentum flux due to SSO-effects'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'u-momentum flux due to SSO-effects'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'u-momentum flux due to SSO-effects'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 227:
            return 'Ba140  - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 226:
            return 'Ba140 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 225:
            return 'Air concentration of Barium 40'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 224:
            return 'I131o  - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 223:
            return 'I131o  - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 222:
            return 'I131o  - concentration'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 221:
            return 'I131g  - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 220:
            return 'Xe133  - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 219:
            return 'I131g - concentration'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 218:
            return 'Xe133  - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 217:
            return 'Xe133  - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 216:
            return 'Air concentration of Xenon 133 (Xe133  - concentration)'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 215:
            return 'TRACER - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 214:
            return 'TRACER - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 213:
            return 'TRACER - concentration'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 212:
            return 'Kr85-wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 211:
            return 'Kr85-dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 210:
            return 'Air concentration of Krypton 85  (Kr85-concentration)'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 209:
            return 'Zr95-wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 208:
            return 'Zr95-dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 207:
            return 'Air concentration of Zirconium 95 (Zr95-concentration)'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 206:
            return 'Te132-wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 205:
            return 'Te132-dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 204:
            return 'Air concentration of Tellurium 132 (Te132-concentration)'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 203:
            return 'Cs137-wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 202:
            return 'Cs137-dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 201:
            return 'Cs137-concentration'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 200:
            return 'I131-wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 199:
            return 'I131-dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 198:
            return 'I131-concentration'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 197:
            return 'Sr90-wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 196:
            return 'Sr90-dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 195:
            return 'Air concentration of Strontium 90'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 194:
            return 'Ru103-wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 193:
            return 'Ru103-dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 192:
            return 'Air concentration of Ruthenium 103 (Ru103- concentration)'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Ozone Mixing Ratio'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'Delay of the GPS signal trough dry atmos.'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'Delay of the GPS signal trough wet atmos.'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'Delay of the GPS signal trough the (total) atm.'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 200 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Friction velocity'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'geographical longitude'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'geographical latitude'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'Coriolis parameter'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 'water vapor flux'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'tendency of specific humidity'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 196 and typeOfStatisticalProcessing == 0:
            return 'Sea salt aerosol (12M)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 196:
            return 'Sea salt aerosol'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195 and typeOfStatisticalProcessing == 0:
            return 'Black carbon aerosol (12M)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195:
            return 'Black carbon aerosol'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194 and typeOfStatisticalProcessing == 0:
            return 'Organic aerosol (12M)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194:
            return 'Organic aerosol'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 'Total soil dust aerosol (12M)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193:
            return 'Total soil dust aerosol'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192 and typeOfStatisticalProcessing == 0:
            return 'Total sulfate aerosol (12M)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192:
            return 'Total sulfate aerosol'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'ratio of monthly mean NDVI (normalized differential vegetation index) to annual maximum'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ratio of monthly mean NDVI (normalized differential vegetation index) to annual maximum'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 2:
            return 'normalized differential vegetation index (NDVI)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31:
            return 'normalized differential vegetation index'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 30 and typeOfFirstFixedSurface == 1:
            return 'deciduous forest'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 29 and typeOfFirstFixedSurface == 1:
            return 'evergreen forest'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and typeOfStatisticalProcessing == 7 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10:
            return 'variance of soil moisture content (10-100)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 10 and scaleFactorOfFirstFixedSurface == -2 and typeOfStatisticalProcessing == 7 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0:
            return 'variance of soil moisture content (0-10)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'Orographie + Land-Meer-Verteilung'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 1:
            return 'Min Leaf area index'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2:
            return 'Max Leaf area index'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 3:
            return 'Plant covering degree in the quiescent phas'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1:
            return 'Plant covering degree in the vegetation phase'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'vertically integrated ozone content (climatological)'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'height of ozone maximum (climatological)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 32 and typeOfFirstFixedSurface == 1:
            return 'root depth of vegetation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfFirstFixedSurface == 1:
            return 'Leaf area index'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Soil Type'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196 and typeOfFirstFixedSurface == 1:
            return 'surface emissivity'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 1:
            return 'Slope of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21 and typeOfFirstFixedSurface == 1:
            return 'Angle of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24 and typeOfFirstFixedSurface == 1:
            return 'Anisotropy of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 1:
            return 'Standard deviation of sub-grid scale orography'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'meridional wind tendency due to subgrid scale oro.'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'zonal wind tendency due to subgrid scale oro.'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 'analysis error(standard deviation), v-comp. of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 'analysis error(standard deviation), u-comp. of wind'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfGeneratingProcess == 7 and typeOfStatisticalProcessing == 6:
            return 'analysis error(standard deviation), geopotential(gpm)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 199:
            return 'total directional spread'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 198:
            return 'total Tm2 period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 197:
            return 'total Tm1 period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 196:
            return 'total wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 195:
            return 'total wave peak period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 194:
            return 'swell peak period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 194 and typeOfFirstFixedSurface == 101:
            return 'swell mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 193:
            return 'wind sea peak period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 193 and typeOfFirstFixedSurface == 101:
            return 'wind sea mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 192:
            return 'total wave direction'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206 and typeOfFirstFixedSurface == 1:
            return 'moisture convergence for Kuo-type closure'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'Convective Available Potential Energy'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205 and typeOfFirstFixedSurface == 1:
            return 'Massflux at convective cloud base'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'residuum of soil moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'total forcing at soil surface'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'total transpiration from all soil layers'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'sum of contributions to evaporation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Effective transmissivity of solar radiation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'unknown'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 10:
            return 'Base reflectivity (cmax)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Base reflectivity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'Base reflectivity'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8 and typeOfFirstFixedSurface == 1:
            return 'sea Ice Temperature'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16 and typeOfFirstFixedSurface == 1:
            return 'Minimal Stomatal Resistance'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'Snow temperature (top of snow)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and typeOfFirstFixedSurface == 1:
            return 'Plant Canopy Surface Water'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2:
            return 'soil ice content (multilayers)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 'Column-integrated Soil Moisture (multilayers)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 'Soil Temperature (multilayers)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 'Air concentration of Ruthenium 103'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2:
            return 'maximum Wind 10m'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'mixed layer depth'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 19 and typeOfFirstFixedSurface == 1:
            return 'Turbulent transfer coefficient for heat (and Moisture)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29 and typeOfFirstFixedSurface == 1:
            return 'Turbulent transfer coefficient for impulse'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Turbulent diffusion coefficient for heat (and moisture)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 31 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Turbulent diffusioncoefficient for momentum'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Turbulent Kinetic Energy'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Kinetic Energy'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Tendency of turbulent kinetic energy'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 24:
            return 'Convective turbulent kinetic enery'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 192:
            return 'Convective Inhibition, mean layer'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 192:
            return 'Convective Available Potential Energy, mean layer'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 193:
            return 'Convective Inhibition, most unstable'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 193:
            return 'Convective Available Potential Energy, most unstable'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'supercell detection index 2 (only rot. up drafts)'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'supercell detection index 1 (rot. up+down drafts)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Pressure perturbation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 1:
            return 'Snow density'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Graupel (snow pellets) precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1:
            return 'Graupel (snow pellets) precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'tendency of specific cloud ice content due to grid scale precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 'Fresh snow factor (weighting function for albedo indicating freshness of snow)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'tendency of specific cloud liquid water content due to grid scale precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Specific humitiy tendency due to grid scale precipitation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Temperature tendency due to grid scale precipation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'snow amount, grid-scale plus convective'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'rain amount, grid-scale plus convective'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Convective rain rate (s)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfFirstFixedSurface == 1:
            return 'Convective snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfFirstFixedSurface == 1:
            return 'Convective rain rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Large scale rain rate (s)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfFirstFixedSurface == 1:
            return 'Large scale snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfFirstFixedSurface == 1:
            return 'Large scale rain rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Specific content of precipitation particles (needed for water loadin)g'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'tendency of  specific cloud ice content due to convection'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Tendency of specific cloud liquid water content due to conversion'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204:
            return 'Height of snow fall limit'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 200 and typeOfFirstFixedSurface == 4:
            return 'height of 0 degree celsius level code 0,3,6 ?'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196 and typeOfFirstFixedSurface == 1:
            return 'height of top of dry convection'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'meridional wind tendency due to convection'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'zonal wind tendency due to convection'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Specific humitiy tendency due to convection'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Temperature tendency due to convection'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 'top index (vertical level) of main convective cloud (i)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'base index (vertical level) of main convective cloud (i)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27 and typeOfFirstFixedSurface == 3:
            return 'Height of Convective Cloud Top (i)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfFirstFixedSurface == 2:
            return 'Height of Convective Cloud Base (i)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'specific cloud water content, convective cloud'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193 and typeOfFirstFixedSurface == 3:
            return 'cloud top above msl, shallow convection'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192 and typeOfFirstFixedSurface == 2:
            return 'cloud base above msl, shallow convection'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'subgridscale cloud ice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'subgrid scale cloud water'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'vertical integral of divergence of total water content (s)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 78 and typeOfFirstFixedSurface == 1:
            return 'Total Column integrated water (all components incl. precipitation)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 74:
            return 'Total column integrated grauple'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Grauple'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'Total column integrated snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'Total column integrated rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Snow mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Rain mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Cloud Ice Mixing Ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Cloud Mixing Ratio'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Non-Convective Cloud Cover, grid scale'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Cloud cover'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 'Stomatal Resistance'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1:
            return 'Sunshine'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 'Latent heat flux from plants'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Latent heat flux from bare soil'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Thermal radiation heating rate'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Solar radiation heating rate'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'Photosynthetically active radiation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'Photosynthetically active radiation (m) (at the surface)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'Momentum Flux, V-Component (m)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Momentum Flux, U-Component (m)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Sensible Heat Net Flux (m)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'Latent Heat Net Flux (m)'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 0:
            return 'Net long wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 0:
            return 'Net long wave radiation flux (m) (on the model top)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 0:
            return 'Net short wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 0:
            return 'Net short wave radiation flux (m) (on the model top)'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'Net long wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'Net long wave radiation flux (m) (at the surface)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'Net short wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'Net short wave radiation flux (m) (at the surface)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 'Mean period of swell waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'Significant height of swell waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'Direction of swell waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'Mean period of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'Significant height of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'Direction of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'Significant height of combined wind waves and swell'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'sea Ice Thickness'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Sea Ice Cover ( 0= free, 1=cover)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == -2 and typeOfStatisticalProcessing == 1 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 10:
            return 'Water Runoff (s)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and typeOfStatisticalProcessing == 1 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 190 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2:
            return 'Water Runoff (10-190)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and typeOfStatisticalProcessing == 1 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 100 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2:
            return 'Water Runoff (10-100)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'Plant cover'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 100 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2 and scaleFactorOfFirstFixedSurface == -2:
            return 'Column-integrated Soil Moisture (2) 10-100cm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == -2 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 10:
            return 'Column-integrated Soil Moisture (1) 0 -10 cm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 190 and scaledValueOfFirstFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2:
            return 'Column-integrated Soil Moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2:
            return 'Soil Temperature'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 9 and scaleFactorOfFirstFixedSurface == -2:
            return 'Soil Temperature'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 41:
            return 'Soil Temperature (41 cm depth)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 36:
            return 'Soil Temperature  ( 36 cm depth, vv=0h)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Albedo (in short-wave)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'Albedo (in short-wave)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'Surface Roughness length Surface Roughness'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Land Cover (1=land, 0=sea)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Large-Scale snowfall rate water equivalent (s)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Convective Snowfall rate water equivalent (s)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69 and typeOfFirstFixedSurface == 1:
            return 'Total Column-Integrated Cloud Water'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == -2:
            return 'Cloud Cover (0 - 400 hPa)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaledValueOfFirstFixedSurface == 400 and scaleFactorOfSecondFixedSurface == -2 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800:
            return 'Cloud Cover (400 - 800 hPa)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 800 and scaleFactorOfFirstFixedSurface == -2 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100:
            return 'Cloud Cover (800 hPa - Soil)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Convective Cloud Cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'Total Cloud Cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 'Snow Depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 'Snow depth water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1:
            return 'Convective Precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1:
            return 'Large-Scale Precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Total Precipitation rate (S)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70 and typeOfFirstFixedSurface == 1:
            return 'Total Column-Integrated Cloud Ice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Evaporation (s)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64 and typeOfFirstFixedSurface == 1:
            return 'Total column integrated water vapour'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'Relative Humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0:
            return '2m Relative Humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'Specific Humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2:
            return 'Specific Humidity (2m)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Specific Humidity (S)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'Vertical Velocity (Geometric) (w)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'Vertical Velocity (Pressure) ( omega=dp/dt )'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'V component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10:
            return 'V component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'U component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10:
            return 'U component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Wind speed (SP)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0:
            return 'Wind speed (SP_10M)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'Wind Direction (DD)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10:
            return 'Wind Direction (DD_10M)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'Wave spectra (3)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'Wave spectra (2)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'Wave spectra (1)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2:
            return 'Radar spectra (1)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 0 and scaleFactorOfFirstFixedSurface == 0:
            return '2m Dew Point Temperature (AV)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 3 and scaleFactorOfFirstFixedSurface == 0:
            return 'Min 2m Temperature (i)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 2 and scaleFactorOfFirstFixedSurface == 0:
            return 'Max 2m Temperature (i)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'Temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 9 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'Climat. temperature, 2m Temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Temperature (G)'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'Total Column Integrated Ozone'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Geometric Height of the layer limits above sea level(NN)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'Geometric Height of the earths surface above sea level'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'Geopotential'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'Geopotential (full lev)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'Geopotential (S)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'Pressure Tendency (S)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 101:
            return 'Pressure Reduced to MSL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pressure'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Pressure (S) (not reduced)'

        is_s2s = h.get_l('is_s2s')
        subCentre = h.get_l('subCentre')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and is_s2s == 1 and typeOfFirstFixedSurface == 103 and subCentre == 102:
            return '2 metre dewpoint temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2 metre dewpoint temperature'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0 and subCentre == 102 and is_s2s == 1:
            return 'Sea ice area fraction'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'Sea ice area fraction'

    return wrapped
