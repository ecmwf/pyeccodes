import pyeccodes.accessors as _


def load(h):

    _.Template('grib2/mars_labeling.def').load(h)
    h.add(_.Transient('productDefinitionTemplateNumberInternal', -1))
    h.add(_.Local_definition('localDefinitionNumber', _.Get('grib2LocalSectionNumber'), _.Get('productDefinitionTemplateNumber'), _.Get('productDefinitionTemplateNumberInternal'), _.Get('type'), _.Get('stream'), _.Get('class'), _.Get('eps'), _.Get('stepType'), _.Get('derivedForecast')))
    h.add(_.G2_eps('eps', _.Get('productDefinitionTemplateNumber'), _.Get('type'), _.Get('stream'), _.Get('stepType'), _.Get('derivedForecast')))
    _.Template('grib2/local.98.[grib2LocalSectionNumber:l].def', True).load(h)
    h.add(_.Position('offsetAfterLocalSection'))
    h.add(_.Transient('addExtraLocalSection', 0))
    h.add(_.Transient('deleteExtraLocalSection', 0))
    h.add(_.Evaluate('extraLocalSectionPresent', (((_.Get('section2Length') - _.Get('offsetAfterLocalSection')) + _.Get('offsetSection2')) > 0)))

    if ((h.get_l('extraLocalSectionPresent') or h.get_l('addExtraLocalSection')) and not (h.get_l('deleteExtraLocalSection'))):
        h.add(_.Codetable('extraLocalSectionNumber', 2, "grib2/grib2LocalSectionNumber.[centreForLocal:l].table"))
        _.Template('grib2/local.98.[extraLocalSectionNumber:l].def').load(h)

