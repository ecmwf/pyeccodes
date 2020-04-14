import pyeccodes.accessors as _


def load(h):

    h.add(_.StringCodetable('marsClass', 2, "mars/class.table"))
    h.add(_.StringCodetable('marsType', 2, "mars/type.table"))
    h.add(_.StringCodetable('marsStream', 2, "mars/stream.table"))
    h.add(_.Ksec1expver('experimentVersionNumber', 4))
    h.add(_.G2_mars_labeling('class', 0, _.Get('marsClass'), _.Get('marsType'), _.Get('marsStream'), _.Get('experimentVersionNumber'), _.Get('typeOfProcessedData'), _.Get('productDefinitionTemplateNumber'), _.Get('stepType'), _.Get('derivedForecast'), _.Get('typeOfGeneratingProcess')))
    h.add(_.G2_mars_labeling('type', 1, _.Get('marsClass'), _.Get('marsType'), _.Get('marsStream'), _.Get('experimentVersionNumber'), _.Get('typeOfProcessedData'), _.Get('productDefinitionTemplateNumber'), _.Get('stepType'), _.Get('derivedForecast'), _.Get('typeOfGeneratingProcess')))
    h.add(_.G2_mars_labeling('stream', 2, _.Get('marsClass'), _.Get('marsType'), _.Get('marsStream'), _.Get('experimentVersionNumber'), _.Get('typeOfProcessedData'), _.Get('productDefinitionTemplateNumber'), _.Get('stepType'), _.Get('derivedForecast'), _.Get('typeOfGeneratingProcess')))
    h.alias('ls.dataType', 'marsType')
    h.alias('mars.class', 'class')
    h.alias('mars.type', 'type')
    h.alias('mars.stream', 'stream')
    h.alias('mars.expver', 'experimentVersionNumber')
    h.alias('mars.domain', 'globalDomain')
