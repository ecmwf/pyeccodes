import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('ECMWF', 98))
    h.add(_.Constant('ECMWF_s', "ecmf"))
    h.add(_.Constant('WMO', 0))
    h.add(_.Constant('conceptsMasterDir', "grib1"))
    h.add(_.Constant('conceptsLocalDirECMF', "grib1/localConcepts/ecmf"))
    h.add(_.Constant('conceptsLocalDirAll', "grib1/localConcepts/[centre:s]"))
    h.add(_.Constant('tablesMasterDir', "grib1"))
    h.add(_.Constant('tablesLocalDir', "grib1/local/[centre:s]"))
    h.add(_.Transient('productionStatusOfProcessedData', 0))
    h.add(_.Position('offsetSection1'))
    h.add(_.Section_length('section1Length', 3))
    h.add(_.Section_pointer('section1Pointer', _.Get('offsetSection1'), _.Get('section1Length'), 1))
    h.add(_.Constant('wrongPadding', 0))
    h.add(_.Unsigned('table2Version', 1))
    h.alias('gribTablesVersionNo', 'table2Version')
    h.add(_.StringCodetable('centre', 1, "common/c-1.table"))
    h.alias('identificationOfOriginatingGeneratingCentre', 'centre')
    h.add(_.Codetable_title('centreDescription', _.Get('centre')))
    h.alias('parameter.centre', 'centre')
    h.alias('originatingCentre', 'centre')
    h.alias('ls.centre', 'centre')
    h.add(_.Unsigned('generatingProcessIdentifier', 1))
    h.alias('generatingProcessIdentificationNumber', 'generatingProcessIdentifier')
    h.alias('process', 'generatingProcessIdentifier')
    h.add(_.Unsigned('gridDefinition', 1))
    h.add(_.Codeflag('section1Flags', 1, "grib1/1.table"))
    h.alias('centreForTable2', 'centre')
    h.add(_.Codetable('indicatorOfParameter', 1, "grib1/2.[centreForTable2:l].[table2Version:l].table"))
    h.add(_.Codetable_title('parameterName', _.Get('indicatorOfParameter')))
    h.add(_.Codetable_units('parameterUnits', _.Get('indicatorOfParameter')))
    h.add(_.StringCodetable('indicatorOfTypeOfLevel', 1, "3.table", _.Get('tablesLocalDir'), _.Get('tablesMasterDir')))
    h.alias('levelType', 'indicatorOfTypeOfLevel')
    h.add(_.Transient('pressureUnits', "hPa"))
    h.add(_.Concept('typeOfLevelECMF', 'unknown', 'typeOfLevel.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', True))
    h.add(_.Concept('typeOfLevel', 'typeOfLevelECMF', 'typeOfLevel.def', 'conceptsMasterDir', 'conceptsLocalDirAll', True))
    h.alias('vertical.typeOfLevel', 'typeOfLevel')
    pass  # when block
    h.alias('ls.typeOfLevel', 'typeOfLevel')

    if ((((((((((((h.get_l('indicatorOfTypeOfLevel') == 101) or (h.get_l('indicatorOfTypeOfLevel') == 104)) or (h.get_l('indicatorOfTypeOfLevel') == 106)) or (h.get_l('indicatorOfTypeOfLevel') == 108)) or (h.get_l('indicatorOfTypeOfLevel') == 110)) or (h.get_l('indicatorOfTypeOfLevel') == 112)) or (h.get_l('indicatorOfTypeOfLevel') == 114)) or (h.get_l('indicatorOfTypeOfLevel') == 116)) or (h.get_l('indicatorOfTypeOfLevel') == 120)) or (h.get_l('indicatorOfTypeOfLevel') == 121)) or (h.get_l('indicatorOfTypeOfLevel') == 128)) or (h.get_l('indicatorOfTypeOfLevel') == 141)):
        h.add(_.Unsigned('topLevel', 1))
        h.add(_.Unsigned('bottomLevel', 1))
        h.add(_.Sprintf('levels', "%d-%d", _.Get('topLevel'), _.Get('bottomLevel')))
        h.alias('ls.levels', 'levels')
        h.alias('vertical.level', 'topLevel')
        h.alias('vertical.topLevel', 'topLevel')
        h.alias('vertical.bottomLevel', 'bottomLevel')
    else:
        h.add(_.Unsigned('level', 2))

        if (h.get_l('indicatorOfTypeOfLevel') == 210):
            h.add(_.Scale('marsLevel', _.Get('level'), _.Get('oneConstant'), _.Get('hundred')))
            h.alias('mars.levelist', 'marsLevel')

        h.alias('vertical.level', 'level')
        h.alias('vertical.topLevel', 'level')
        h.alias('vertical.bottomLevel', 'level')
        h.alias('ls.level', 'level')
        h.alias('lev', 'level')

    if (((((h.get_l('indicatorOfTypeOfLevel') == 109) or (h.get_l('indicatorOfTypeOfLevel') == 100)) or (h.get_l('indicatorOfTypeOfLevel') == 110)) or (h.get_l('indicatorOfTypeOfLevel') == 113)) or (h.get_l('indicatorOfTypeOfLevel') == 117)):
        h.alias('mars.levelist', 'level')

    h.add(_.Unsigned('yearOfCentury', 1))
    h.add(_.Unsigned('month', 1))
    h.add(_.Unsigned('day', 1))
    h.add(_.Unsigned('hour', 1))
    h.add(_.Unsigned('minute', 1))
    h.add(_.Transient('second', 0))
    h.add(_.Codetable('unitOfTimeRange', 1, "grib1/4.table"))
    h.alias('unitOfTime', 'unitOfTimeRange')
    h.alias('indicatorOfUnitOfTimeRange', 'unitOfTimeRange')
    h.add(_.Unsigned('P1', 1))
    h.add(_.Unsigned('P2', 1))
    h.add(_.Codetable('timeRangeIndicator', 1, "5.table", _.Get('tablesLocalDir'), _.Get('tablesMasterDir')))
    h.add(_.Unsigned('numberIncludedInAverage', 2))
    h.add(_.Bits('mybits', _.Get('numberIncludedInAverage'), 0, 12))
    h.add(_.Unsigned('numberMissingFromAveragesOrAccumulations', 1))
    h.add(_.Unsigned('centuryOfReferenceTimeOfData', 1))
    h.add(_.Codetable('subCentre', 1, "grib1/0.[centre].table"))

    if (h.get_l('table2Version') >= 128):

        if ((h.get_l('centre') != 98) and (h.get_l('subCentre') == 98)):
            h.alias('centreForTable2', 'subCentre')
        else:
            h.alias('centreForTable2', 'centre')

    else:
        h.alias('centreForTable2', 'WMO')

    h.add(_.Concept('paramIdECMF', 'defaultParameter', 'paramId.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('paramId', 'paramIdECMF', 'paramId.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('cfNameECMF', 'defaultName', 'cfName.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('cfName', 'cfNameECMF', 'cfName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('cfVarNameECMF', 'defaultName', 'cfVarName.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('cfVarName', 'cfVarNameECMF', 'cfVarName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('unitsECMF', 'defaultName', 'units.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('units', 'unitsECMF', 'units.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Concept('nameECMF', 'defaultName', 'name.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('name', 'nameECMF', 'name.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.add(_.Signed('decimalScaleFactor', 2))
    h.add(_.Transient('setLocalDefinition', 0))
    h.add(_.Transient('optimizeScaleFactor', 0))
    h.add(_.G1date('dataDate', _.Get('centuryOfReferenceTimeOfData'), _.Get('yearOfCentury'), _.Get('month'), _.Get('day')))
    h.add(_.Evaluate('year', (_.Get('dataDate') / 10000)))
    h.add(_.Time('dataTime', _.Get('hour'), _.Get('minute'), _.Get('second')))
    h.add(_.Julian_day('julianDay', _.Get('dataDate'), _.Get('hour'), _.Get('minute'), _.Get('second')))
    h.add(_.TransientCodetable('stepUnits', 1, "stepUnits.table"))
    h.add(_.Concept('stepType', 'timeRangeIndicator', 'stepType.def', 'conceptsMasterDir', 'conceptsLocalDirAll', True))

    if (h.get_s('stepType') == "instant"):
        h.alias('productDefinitionTemplateNumber', 'zero')
    else:
        h.alias('productDefinitionTemplateNumber', 'eight')

    h.add(_.G1step_range('stepRange', _.Get('P1'), _.Get('P2'), _.Get('timeRangeIndicator'), _.Get('unitOfTimeRange'), _.Get('stepUnits'), _.Get('stepType')))
    h.add(_.Long_vector('startStep', _.Get('stepRange'), 0))
    h.add(_.Long_vector('endStep', _.Get('stepRange'), 1))
    h.alias('stepInHours', 'endStep')
    h.alias('ls.stepRange', 'stepRange')
    h.alias('ls.dataDate', 'dataDate')
    h.alias('mars.step', 'endStep')
    h.alias('mars.date', 'dataDate')
    h.alias('mars.levtype', 'indicatorOfTypeOfLevel')
    h.alias('mars.time', 'dataTime')
    h.add(_.Mars_param('marsParam', _.Get('paramId'), _.Get('gribTablesVersionNo'), _.Get('indicatorOfParameter')))
    h.alias('mars.param', 'marsParam')

    if ((h.get_l('centre') == 34) and (h.get_l('subCentre') == 241)):
        h.alias('mars.param', 'paramId')

        if (h.get_l('indicatorOfTypeOfLevel') == 101):
            h.add(_.Constant('sfc_levtype', "sfc"))
            h.alias('mars.levtype', 'sfc_levtype')


    h.add(_.Validity_date('validityDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('step'), _.Get('stepUnits')))
    h.alias('time.validityDate', 'validityDate')
    h.add(_.Validity_time('validityTime', _.Get('dataDate'), _.Get('dataTime'), _.Get('step'), _.Get('stepUnits')))
    h.alias('time.validityTime', 'validityTime')
    h.add(_.Transient('deleteLocalDefinition', 0))

    if ((((h.get_l('section1Length') > 40) or h._new()) or (h.get_l('setLocalDefinition') > 0)) and (h.get_l('deleteLocalDefinition') == 0)):
        h.add(_.Constant('localUsePresent', 1))
        h.alias('grib2LocalSectionPresent', 'present')

        if ((h.get_l('centre') == h.get_l('ECMWF')) or ((h.get_l('centre') != h.get_l('ECMWF')) and (h.get_l('subCentre') == h.get_l('ECMWF')))):
            h.add(_.Pad('reservedNeedNotBePresent', 12))
            h.add(_.Codetable('localDefinitionNumber', 1, "grib1/localDefinitionNumber.98.table"))
            _.Template('grib1/local.98.[localDefinitionNumber:l].def', True).load(h)

            if h._changed('localDefinitionNumber'):

                if (not (h._new()) and (h.get_l('localDefinitionNumber') != 4)):
                    h.add(_.Section_padding('localExtensionPadding'))


            _.Template('mars/grib.[stream:s].[type:s].def', True).load(h)
        else:

            if (not (h._new()) or h.get_l('setLocalDefinition')):
                h.add(_.Pad('reservedNeedNotBePresent', 12))
                _.Template('grib1/local.[centre:l].def', True).load(h)
                h.add(_.Section_padding('localExtensionPadding'))

    else:
        h.add(_.Constant('localUsePresent', 0))

    h.add(_.Section_padding('section1Padding'))
    h.add(_.Concept('shortNameECMF', 'defaultShortName', 'shortName.def', 'conceptsMasterDir', 'conceptsLocalDirECMF', False))
    h.add(_.Concept('shortName', 'shortNameECMF', 'shortName.def', 'conceptsMasterDir', 'conceptsLocalDirAll', False))
    h.alias('ls.shortName', 'shortName')
    h.add(_.Ifs_param('ifsParam', _.Get('paramId'), _.Get('type')))
    h.alias('parameter.paramId', 'paramId')
    h.alias('parameter.shortName', 'shortName')
    h.alias('parameter.units', 'units')
    h.alias('parameter.name', 'name')
    h.alias('parameter', 'paramId')
    h.alias('short_name', 'shortName')
    h.alias('time.stepRange', 'stepRange')
    h.alias('time.stepUnits', 'stepUnits')
    h.alias('time.dataDate', 'dataDate')
    h.alias('time.dataTime', 'dataTime')
    h.alias('time.startStep', 'startStep')
    h.alias('time.endStep', 'endStep')
    h.alias('time.stepType', 'stepType')
    h.add(_.Concept('stepTypeForConversion', 'unknown', 'stepTypeForConversion.def', 'conceptsMasterDir', 'conceptsLocalDirAll', True))

    if (h.get_s('stepTypeForConversion') == "accum"):
        h.alias('productDefinitionTemplateNumber', 'eight')

    h.add(_.Md5('md5Section1', _.Get('offsetSection1'), _.Get('section1Length')))
    h.add(_.Md5('md5Product', _.Get('offsetSection1'), _.Get('section1Length'), _.Get('gridDefinition'), _.Get('section1Flags'), _.Get('decimalScaleFactor')))
