import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection1'))
    h.add(_.Section_length('section1Length', 4))
    h.add(_.Section_pointer('section1Pointer', _.Get('offsetSection1'), _.Get('section1Length'), 1))
    h.add(_.Unsigned('numberOfSection', 1))
    h.add(_.StringCodetable('centre', 2, "common/c-11.table"))
    h.alias('identificationOfOriginatingGeneratingCentre', 'centre')
    h.add(_.Codetable_title('centreDescription', _.Get('centre')))
    h.alias('parameter.centre', 'centre')
    h.alias('ls.centre', 'centre')
    h.alias('originatingCentre', 'centre')
    h.add(_.Unsigned('subCentre', 2))

    if (h.get_l('subCentre') == 98):
        h.alias('centreForLocal', 'subCentre')
    else:
        h.alias('centreForLocal', 'centre')

    h.add(_.Codetable('tablesVersion', 1, "grib2/tables/1.0.table"))
    h.alias('gribMasterTablesVersionNumber', 'tablesVersion')
    h.add(_.Transient('masterDir', "grib2/tables/[tablesVersion]"))

    if (h.get_l('tablesVersion') > h.get_l('tablesVersionLatest')):
        h.add(_.Transient('masterDir', "grib2/tables/[tablesVersionLatest]"))

    pass  # when block
    h.add(_.Codetable('localTablesVersion', 1, "grib2/tables/local/[centreForLocal]/1.1.table"))
    h.alias('versionNumberOfGribLocalTables', 'localTablesVersion')
    h.add(_.Transient('localDir', ""))

    if ((h.get_l('localTablesVersion') != 0) and (h.get_l('localTablesVersion') != 255)):
        h.add(_.Transient('localDir', "grib2/tables/local/[centre]/[localTablesVersion]"))

    h.add(_.Codetable('significanceOfReferenceTime', 1, "1.2.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('year', 2))
    h.add(_.Unsigned('month', 1))
    h.add(_.Unsigned('day', 1))
    h.add(_.Unsigned('hour', 1))
    h.add(_.Unsigned('minute', 1))
    h.add(_.Unsigned('second', 1))
    h.add(_.G2date('dataDate', _.Get('year'), _.Get('month'), _.Get('day')))
    h.alias('mars.date', 'dataDate')
    h.alias('ls.date', 'dataDate')
    h.add(_.Julian_day('julianDay', _.Get('dataDate'), _.Get('hour'), _.Get('minute'), _.Get('second')))
    h.add(_.Time('dataTime', _.Get('hour'), _.Get('minute'), _.Get('second')))
    h.alias('mars.time', 'dataTime')
    h.add(_.Codetable('productionStatusOfProcessedData', 1, "1.3.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.StringCodetable('typeOfProcessedData', 1, "1.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('ls.dataType', 'typeOfProcessedData')
    h.add(_.Md5('md5Section1', _.Get('offsetSection1'), _.Get('section1Length')))
    h.add(_.Select_step_template('selectStepTemplateInterval', _.Get('productDefinitionTemplateNumber'), 0))
    h.add(_.Select_step_template('selectStepTemplateInstant', _.Get('productDefinitionTemplateNumber'), 1))
    h.add(_.Transient('stepTypeInternal', "instant"))

    def stepType_inline_concept(h):
        def wrapped(h):

            selectStepTemplateInstant = h.get_l('selectStepTemplateInstant')
            stepTypeInternal = h.get_s('stepTypeInternal')

            if selectStepTemplateInstant == 1 and stepTypeInternal == "instant":
                return 'instant'

            selectStepTemplateInterval = h.get_l('selectStepTemplateInterval')

            if selectStepTemplateInterval == 1 and stepTypeInternal == "avg":
                return 'avg'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "avgd":
                return 'avgd'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "accum":
                return 'accum'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "max":
                return 'max'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "min":
                return 'min'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "diff":
                return 'diff'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "sdiff":
                return 'sdiff'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "rms":
                return 'rms'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "sd":
                return 'sd'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "cov":
                return 'cov'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "ratio":
                return 'ratio'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "stdanom":
                return 'stdanom'

            if selectStepTemplateInterval == 1 and stepTypeInternal == "sum":
                return 'sum'

        return wrapped

    h.add(_.Concept('stepType', None, concepts=stepType_inline_concept(h)))

    h.add(_.G2_chemical('is_chemical', _.Get('productDefinitionTemplateNumber'), _.Get('stepType'), 0))
    h.add(_.G2_chemical('is_chemical_distfn', _.Get('productDefinitionTemplateNumber'), _.Get('stepType'), 1))
    h.add(_.G2_aerosol('is_aerosol', _.Get('productDefinitionTemplateNumber'), _.Get('stepType'), 0))
    h.add(_.G2_aerosol('is_aerosol_optical', _.Get('productDefinitionTemplateNumber'), _.Get('stepType'), 1))
    h.add(_.Transient('setCalendarId', 0))
    h.add(_.Transient('deleteCalendarId', 0))
    h.alias('calendarIdPresent', 'zero')

    if (((h.get_l('section1Length') > 21) or (h.get_l('setCalendarId') > 0)) and (h.get_l('deleteCalendarId') == 0)):
        h.alias('calendarIdPresent', 'present')
        h.add(_.StringCodetable('calendarIdentificationTemplateNumber', 2, "1.5.table", _.Get('masterDir'), _.Get('localDir')))
        _.Template('grib2/template.1.[calendarIdentificationTemplateNumber:l].def').load(h)

    def is_uerra_inline_concept(h):
        def wrapped(h):

            productionStatusOfProcessedData = h.get_l('productionStatusOfProcessedData')

            if productionStatusOfProcessedData == 10:
                return 1

            if productionStatusOfProcessedData == 11:
                return 1

            if productionStatusOfProcessedData == 9:
                return 1

            if productionStatusOfProcessedData == 8:
                return 1

            dummy = h.get_l('dummy')

            if dummy == 1:
                return 0

        return wrapped

    h.add(_.Concept('is_uerra', 'zero', concepts=is_uerra_inline_concept(h)))

