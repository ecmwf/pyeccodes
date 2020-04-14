import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('parameterCategory', 1, "4.1.[discipline:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('parameterNumber', 1, "4.2.[discipline:l].[parameterCategory:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_units('parameterUnits', _.Get('parameterNumber')))
    h.add(_.Codetable_title('parameterName', _.Get('parameterNumber')))
    h.add(_.Codetable('constituentType', 2, "4.230.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('numberOfModeOfDistribution', 2))
    h.add(_.Unsigned('modeNumber', 2))
    h.add(_.Codetable('typeOfDistributionFunction', 2, "4.240.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('numberOfDistributionFunctionParameters', 1))
    h.alias('NP', 'numberOfDistributionFunctionParameters')

    with h.list('listOfDistributionFunctionParameter'):
        for i in range(0, h.get_l('numberOfDistributionFunctionParameters')):
            h.add(_.Signed('scaleFactorOfDistributionFunctionParameter', 1))
            h.add(_.Unsigned('scaledValueOfDistributionFunctionParameter', 4))
    h.add(_.Codetable('typeOfGeneratingProcess', 1, "4.3.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('backgroundProcess', 1))
    h.alias('backgroundGeneratingProcessIdentifier', 'backgroundProcess')
    h.add(_.Unsigned('generatingProcessIdentifier', 1))
    h.add(_.Unsigned('hoursAfterDataCutoff', 2))
    h.alias('hoursAfterReferenceTimeOfDataCutoff', 'hoursAfterDataCutoff')
    h.add(_.Unsigned('minutesAfterDataCutoff', 1))
    h.alias('minutesAfterReferenceTimeOfDataCutoff', 'minutesAfterDataCutoff')
    h.add(_.Codetable('indicatorOfUnitOfTimeRange', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('defaultStepUnits', 'one')
    _.Template('grib2/localConcepts/[centre:s]/default_step_units.def', True).load(h)
    h.add(_.TransientCodetable('stepUnits', 1, "stepUnits.table"))
    h.add(_.Signed('forecastTime', 4))
    h.add(_.StringCodetable('typeOfFirstFixedSurface', 1, "4.5.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_units('unitsOfFirstFixedSurface', _.Get('typeOfFirstFixedSurface')))
    h.add(_.Codetable_title('nameOfFirstFixedSurface', _.Get('typeOfFirstFixedSurface')))
    h.add(_.Signed('scaleFactorOfFirstFixedSurface', 1))
    h.add(_.Unsigned('scaledValueOfFirstFixedSurface', 4))
    h.add(_.Codetable('typeOfSecondFixedSurface', 1, "4.5.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_units('unitsOfSecondFixedSurface', _.Get('typeOfSecondFixedSurface')))
    h.add(_.Codetable_title('nameOfSecondFixedSurface', _.Get('typeOfSecondFixedSurface')))
    h.add(_.Signed('scaleFactorOfSecondFixedSurface', 1))
    h.add(_.Unsigned('scaledValueOfSecondFixedSurface', 4))
    h.add(_.Transient('pressureUnits', "hPa"))

    def typeOfLevel_inline_concept(h):
        def wrapped(h):

            typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
            typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

            if typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 255:
                return 'surface'

            if typeOfFirstFixedSurface == 2 and typeOfSecondFixedSurface == 255:
                return 'cloudBase'

            if typeOfFirstFixedSurface == 3 and typeOfSecondFixedSurface == 255:
                return 'cloudTop'

            if typeOfFirstFixedSurface == 4 and typeOfSecondFixedSurface == 255:
                return 'isothermZero'

            if typeOfFirstFixedSurface == 5 and typeOfSecondFixedSurface == 255:
                return 'adiabaticCondensation'

            if typeOfFirstFixedSurface == 6 and typeOfSecondFixedSurface == 255:
                return 'maxWind'

            if typeOfFirstFixedSurface == 7 and typeOfSecondFixedSurface == 255:
                return 'tropopause'

            if typeOfFirstFixedSurface == 8 and typeOfSecondFixedSurface == 255:
                return 'nominalTop'

            if typeOfFirstFixedSurface == 9 and typeOfSecondFixedSurface == 255:
                return 'seaBottom'

            if typeOfFirstFixedSurface == 10 and typeOfSecondFixedSurface == 255:
                return 'atmosphere'

            if typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255:
                return 'isothermal'

            pressureUnits = h.get_s('pressureUnits')

            if typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 255 and pressureUnits == "Pa":
                return 'isobaricInPa'

            if typeOfFirstFixedSurface == 100 and pressureUnits == "hPa" and typeOfSecondFixedSurface == 255:
                return 'isobaricInhPa'

            if typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100:
                return 'isobaricLayer'

            if typeOfFirstFixedSurface == 101 and typeOfSecondFixedSurface == 255:
                return 'meanSea'

            if typeOfFirstFixedSurface == 102 and typeOfSecondFixedSurface == 255:
                return 'heightAboveSea'

            if typeOfFirstFixedSurface == 102 and typeOfSecondFixedSurface == 102:
                return 'heightAboveSeaLayer'

            if typeOfFirstFixedSurface == 103 and typeOfSecondFixedSurface == 255:
                return 'heightAboveGround'

            if typeOfFirstFixedSurface == 103 and typeOfSecondFixedSurface == 103:
                return 'heightAboveGroundLayer'

            if typeOfFirstFixedSurface == 104 and typeOfSecondFixedSurface == 255:
                return 'sigma'

            if typeOfFirstFixedSurface == 104 and typeOfSecondFixedSurface == 104:
                return 'sigmaLayer'

            if typeOfFirstFixedSurface == 105 and typeOfSecondFixedSurface == 255:
                return 'hybrid'

            if typeOfFirstFixedSurface == 118 and typeOfSecondFixedSurface == 255:
                return 'hybridHeight'

            if typeOfFirstFixedSurface == 105 and typeOfSecondFixedSurface == 105:
                return 'hybridLayer'

            if typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 255:
                return 'depthBelowLand'

            if typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106:
                return 'depthBelowLandLayer'

            if typeOfFirstFixedSurface == 107 and typeOfSecondFixedSurface == 255:
                return 'theta'

            if typeOfFirstFixedSurface == 107 and typeOfSecondFixedSurface == 107:
                return 'thetaLayer'

            if typeOfFirstFixedSurface == 108 and typeOfSecondFixedSurface == 255:
                return 'pressureFromGround'

            if typeOfFirstFixedSurface == 108 and typeOfSecondFixedSurface == 108:
                return 'pressureFromGroundLayer'

            if typeOfFirstFixedSurface == 109 and typeOfSecondFixedSurface == 255:
                return 'potentialVorticity'

            if typeOfFirstFixedSurface == 111 and typeOfSecondFixedSurface == 255:
                return 'eta'

            if typeOfFirstFixedSurface == 151 and typeOfSecondFixedSurface == 255:
                return 'soil'

            if typeOfFirstFixedSurface == 151 and typeOfSecondFixedSurface == 151:
                return 'soilLayer'

            genVertHeightCoords = h.get_l('genVertHeightCoords')
            NV = h.get_l('NV')

            if genVertHeightCoords == 1 and typeOfFirstFixedSurface == 150 and NV == 6:
                return 'generalVertical'

            if genVertHeightCoords == 1 and typeOfFirstFixedSurface == 150 and typeOfSecondFixedSurface == 150 and NV == 6:
                return 'generalVerticalLayer'

            if typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255:
                return 'depthBelowSea'

            if typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
                return 'entireAtmosphere'

            if typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 9:
                return 'entireOcean'

            if typeOfFirstFixedSurface == 114 and typeOfSecondFixedSurface == 255:
                return 'snow'

            if typeOfFirstFixedSurface == 114 and typeOfSecondFixedSurface == 114:
                return 'snowLayer'

            scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
            scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

            if typeOfFirstFixedSurface == 160 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 255:
                return 'oceanSurface'

            if typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160:
                return 'oceanLayer'

            if typeOfFirstFixedSurface == 169 and typeOfSecondFixedSurface == 255:
                return 'mixedLayerDepth'

        return wrapped

    h.add(_.Concept('typeOfLevel', 'unknown', concepts=typeOfLevel_inline_concept(h)))

    h.alias('vertical.typeOfLevel', 'typeOfLevel')
    h.alias('levelType', 'typeOfFirstFixedSurface')

    if (h.get_l('typeOfSecondFixedSurface') == 255):
        h.add(_.G2level('level', _.Get('typeOfFirstFixedSurface'), _.Get('scaleFactorOfFirstFixedSurface'), _.Get('scaledValueOfFirstFixedSurface'), _.Get('pressureUnits')))
        h.add(_.Transient('bottomLevel', _.Get('level')))
        h.add(_.Transient('topLevel', _.Get('level')))
    else:
        h.add(_.G2level('topLevel', _.Get('typeOfFirstFixedSurface'), _.Get('scaleFactorOfFirstFixedSurface'), _.Get('scaledValueOfFirstFixedSurface'), _.Get('pressureUnits')))
        h.add(_.G2level('bottomLevel', _.Get('typeOfSecondFixedSurface'), _.Get('scaleFactorOfSecondFixedSurface'), _.Get('scaledValueOfSecondFixedSurface'), _.Get('pressureUnits')))
        h.alias('level', 'topLevel')

    h.alias('ls.level', 'level')
    h.alias('vertical.level', 'level')
    h.alias('vertical.bottomLevel', 'bottomLevel')
    h.alias('vertical.topLevel', 'topLevel')
    h.alias('extraDim', 'zero')

    if h._defined('extraDimensionPresent'):

        if h.get_l('extraDimensionPresent'):
            h.alias('extraDim', 'one')


    if h.get_l('extraDim'):
        h.alias('mars.levelist', 'dimension')
        h.alias('mars.levtype', 'dimensionType')
    else:
        h.add(_.Transient('tempPressureUnits', _.Get('pressureUnits')))

        if not ((h.get_s('typeOfLevel') == "surface")):

            if (h.get_s('tempPressureUnits') == "Pa"):
                h.add(_.Scale('marsLevel', _.Get('level'), _.Get('one'), _.Get('hundred')))
                h.alias('mars.levelist', 'marsLevel')
            else:
                h.alias('mars.levelist', 'level')


        h.alias('mars.levtype', 'typeOfFirstFixedSurface')

        if (h.get_s('levtype') == "sfc"):
            h.unalias('mars.levelist')

    if ((h.get_l('typeOfFirstFixedSurface') == 151) and (h.get_l('typeOfSecondFixedSurface') == 151)):
        h.alias('mars.levelist', 'bottomLevel')

    h.alias('ls.typeOfLevel', 'typeOfLevel')
    h.add(_.Unsigned('yearOfEndOfOverallTimeInterval', 2))
    h.add(_.Unsigned('monthOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('dayOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('hourOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('minuteOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('secondOfEndOfOverallTimeInterval', 1))
    h.add(_.Unsigned('numberOfTimeRange', 1))
    h.alias('n', 'numberOfTimeRange')
    h.add(_.Unsigned('numberOfMissingInStatisticalProcess', 4))
    h.alias('totalNumberOfDataValuesMissingInStatisticalProcess', 'numberOfMissingInStatisticalProcess')

    with h.list('statisticalProcessesList'):
        for i in range(0, h.get_l('numberOfTimeRange')):
            h.add(_.Codetable('typeOfStatisticalProcessing', 1, "4.10.table", _.Get('masterDir'), _.Get('localDir')))
            h.add(_.Codetable('typeOfTimeIncrement', 1, "4.11.table", _.Get('masterDir'), _.Get('localDir')))
            h.alias('typeOfTimeIncrementBetweenSuccessiveFieldsUsedInTheStatisticalProcessing', 'typeOfTimeIncrement')
            h.add(_.Codetable('indicatorOfUnitForTimeRange', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
            h.add(_.Unsigned('lengthOfTimeRange', 4))
            h.add(_.Codetable('indicatorOfUnitForTimeIncrement', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
            h.add(_.Unsigned('timeIncrement', 4))
            h.alias('timeIncrementBetweenSuccessiveFields', 'timeIncrement')

    if ((h.get_l('numberOfTimeRange') == 1) or (h.get_l('numberOfTimeRange') == 2)):

        def stepTypeInternal_inline_concept(h):
            def wrapped(h):

                typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

                if typeOfStatisticalProcessing == 255:
                    return 'instant'

                typeOfTimeIncrement = h.get_l('typeOfTimeIncrement')

                if typeOfStatisticalProcessing == 0 and typeOfTimeIncrement == 2:
                    return 'avg'

                if typeOfStatisticalProcessing == 0 and typeOfTimeIncrement == 3:
                    return 'avg'

                if typeOfStatisticalProcessing == 0 and typeOfTimeIncrement == 1:
                    return 'avgd'

                if typeOfStatisticalProcessing == 1 and typeOfTimeIncrement == 2:
                    return 'accum'

                if typeOfStatisticalProcessing == 2:
                    return 'max'

                if typeOfStatisticalProcessing == 3:
                    return 'min'

                if typeOfStatisticalProcessing == 4:
                    return 'diff'

                if typeOfStatisticalProcessing == 5:
                    return 'rms'

                if typeOfStatisticalProcessing == 6:
                    return 'sd'

                if typeOfStatisticalProcessing == 7:
                    return 'cov'

                if typeOfStatisticalProcessing == 8:
                    return 'sdiff'

                if typeOfStatisticalProcessing == 9:
                    return 'ratio'

                if typeOfStatisticalProcessing == 10:
                    return 'stdanom'

                if typeOfStatisticalProcessing == 11:
                    return 'sum'

            return wrapped

        h.add(_.Concept('stepTypeInternal', None, concepts=stepTypeInternal_inline_concept(h)))

        h.add(_.Step_in_units('startStep', _.Get('forecastTime'), _.Get('indicatorOfUnitOfTimeRange'), _.Get('stepUnits'), _.Get('indicatorOfUnitForTimeRange'), _.Get('lengthOfTimeRange')))
        h.add(_.G2end_step('endStep', _.Get('startStep'), _.Get('stepUnits'), _.Get('year'), _.Get('month'), _.Get('day'), _.Get('hour'), _.Get('minute'), _.Get('second'), _.Get('yearOfEndOfOverallTimeInterval'), _.Get('monthOfEndOfOverallTimeInterval'), _.Get('dayOfEndOfOverallTimeInterval'), _.Get('hourOfEndOfOverallTimeInterval'), _.Get('minuteOfEndOfOverallTimeInterval'), _.Get('secondOfEndOfOverallTimeInterval'), _.Get('indicatorOfUnitForTimeRange'), _.Get('lengthOfTimeRange'), _.Get('typeOfTimeIncrement'), _.Get('numberOfTimeRange')))
        h.add(_.G2step_range('stepRange', _.Get('startStep'), _.Get('endStep')))
    else:
        h.add(_.Constant('stepType', "multiple steps"))
        h.add(_.Constant('stepTypeInternal', "multiple steps"))
        h.add(_.Constant('endStep', "unavailable"))
        h.add(_.Constant('startStep', "unavailable"))
        h.add(_.Constant('stepRange', "unavailable"))

    h.alias('ls.stepRange', 'stepRange')
    h.alias('mars.step', 'endStep')
    h.alias('time.stepType', 'stepType')
    h.alias('time.stepRange', 'stepRange')
    h.alias('time.stepUnits', 'stepUnits')
    h.alias('time.dataDate', 'dataDate')
    h.alias('time.dataTime', 'dataTime')
    h.alias('time.startStep', 'startStep')
    h.alias('time.endStep', 'endStep')
    h.add(_.Validity_date('validityDate', _.Get('date'), _.Get('dataTime'), _.Get('step'), _.Get('stepUnits'), _.Get('yearOfEndOfOverallTimeInterval'), _.Get('monthOfEndOfOverallTimeInterval'), _.Get('dayOfEndOfOverallTimeInterval')))
    h.alias('time.validityDate', 'validityDate')
    h.add(_.Validity_time('validityTime', _.Get('date'), _.Get('dataTime'), _.Get('step'), _.Get('stepUnits'), _.Get('hourOfEndOfOverallTimeInterval'), _.Get('minuteOfEndOfOverallTimeInterval')))
    h.alias('time.validityTime', 'validityTime')
