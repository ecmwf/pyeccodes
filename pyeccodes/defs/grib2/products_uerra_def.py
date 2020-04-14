import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('marsClass', "ur"))
    h.alias('tigge_short_name', 'shortName')
    h.alias('short_name', 'shortName')
    h.alias('parameter', 'paramId')
    h.alias('tigge_name', 'name')
    h.alias('parameter.paramId', 'paramId')
    h.alias('parameter.shortName', 'shortName')
    h.alias('parameter.units', 'units')
    h.alias('parameter.name', 'name')

    if (h.get_l('typeOfFirstFixedSurface') == 103):

        if (h.get_l('level') > 10):
            h.add(_.Constant('heightLevelName', "hl"))
            h.alias('mars.levtype', 'heightLevelName')
            h.alias('mars.levelist', 'level')


    if (h.get_l('typeOfFirstFixedSurface') == 118):
        h.add(_.Constant('levTypeName', "ml"))
        h.alias('mars.levtype', 'levTypeName')

    if ((h.get_l('typeOfFirstFixedSurface') == 151) and (h.get_l('typeOfSecondFixedSurface') == 151)):
        h.alias('level', 'bottomLevel')

    h.alias('mars.expver', 'marsExpver')
    h.alias('mars.class', 'marsClass')
    h.alias('mars.param', 'paramId')
    h.alias('mars.origin', 'centre')

    def marsType_inline_concept(h):
        def wrapped(h):

            typeOfProcessedData = h.get_l('typeOfProcessedData')

            if typeOfProcessedData == 1:
                return 'fc'

            if typeOfProcessedData == 1:
                return 9

            if typeOfProcessedData == 0:
                return 'an'

            if typeOfProcessedData == 0:
                return 2

            centre = h.get_l('centre')
            typeOfGeneratingProcess = h.get_l('typeOfGeneratingProcess')
            generatingProcessIdentifier = h.get_l('generatingProcessIdentifier')

            if centre == 82 and typeOfGeneratingProcess == 0 and generatingProcessIdentifier == 50:
                return 'oi'

            if centre == 82 and typeOfGeneratingProcess == 0 and generatingProcessIdentifier == 50:
                return 4

            dummyc = h.get_l('dummyc')

            if dummyc == 0:
                return 'default'

        return wrapped

    h.add(_.Concept('marsType', None, concepts=marsType_inline_concept(h)))

    def marsStream_inline_concept(h):
        def wrapped(h):

            productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')

            if productDefinitionTemplateNumber == 8:
                return 'oper'

            if productDefinitionTemplateNumber == 0:
                return 'oper'

            if productDefinitionTemplateNumber == 11:
                return 'enda'

            if productDefinitionTemplateNumber == 1:
                return 'enda'

            dummyc = h.get_l('dummyc')

            if dummyc == 0:
                return 'default'

        return wrapped

    h.add(_.Concept('marsStream', None, concepts=marsStream_inline_concept(h)))

    h.alias('mars.stream', 'marsStream')
    h.alias('mars.type', 'marsType')
