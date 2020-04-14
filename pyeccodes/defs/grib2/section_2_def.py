import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection2'))
    h.add(_.Section_length('section2Length', 4))
    h.add(_.Section_pointer('section2Pointer', _.Get('offsetSection2'), _.Get('section2Length'), 2))
    h.add(_.Unsigned('numberOfSection', 1))
    h.alias('tiggeSuiteID', 'zero')
    h.add(_.Transient('addEmptySection2', 0))

    if (h.get_l('addEmptySection2') == 0):

        if ((h.get_l('grib2LocalSectionPresent') == 1) or ((h.get_l('section2Length') > 5) or h._new())):
            h.alias('section2Used', 'one')

            if ((h.get_l('productionStatusOfProcessedData') == 4) or (h.get_l('productionStatusOfProcessedData') == 5)):
                h.add(_.Codetable('tiggeLocalVersion', 2, "grib2/tiggeLocalVersion.table"))
                _.Template('grib2/local.tigge.[tiggeLocalVersion:l].def').load(h)

            if ((h.get_l('productionStatusOfProcessedData') == 10) or (h.get_l('productionStatusOfProcessedData') == 11)):
                h.add(_.Codetable('crraLocalVersion', 2, "grib2/crraLocalVersion.table"))
                _.Template('grib2/local.crra.[crraLocalVersion:l].def').load(h)

            h.add(_.Codetable('grib2LocalSectionNumber', 2, "grib2/grib2LocalSectionNumber.[centreForLocal:l].table"))

            if (h.get_l('grib2LocalSectionNumber') != 0):
                _.Template('grib2/local.[centreForLocal:l].def', True).load(h)
            else:
                h.add(_.Constant('deleteLocalDefinition', 1))

            h.add(_.Position('offsetAfterCentreLocalSection'))


    h.add(_.Section_padding('section2Padding'))
