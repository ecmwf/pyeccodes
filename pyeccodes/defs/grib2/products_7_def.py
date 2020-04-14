import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('marsExpver', "test"))
    h.add(_.Constant('marsClass', "s2"))
    h.add(_.Constant('marsModel', "glob"))
    h.alias('is_s2s', 'one')
    h.alias('parameter.paramId', 'paramId')
    h.alias('parameter.shortName', 'shortName')
    h.alias('parameter.units', 'units')
    h.alias('parameter.name', 'name')
    h.alias('mars.expver', 'marsExpver')
    h.alias('mars.class', 'marsClass')
    h.alias('mars.param', 'paramId')
    h.alias('mars.model', 'marsModel')

    if ((h.get_s('centre') == "cnmc") and (h.get_l('subCentre') == 102)):
        h.add(_.Constant('cnmc_isac', "isac"))
        h.alias('mars.origin', 'cnmc_isac')
    else:
        h.alias('mars.origin', 'centre')

    h.unalias('mars.domain')

    def marsType_inline_concept(h):
        def wrapped(h):

            typeOfProcessedData = h.get_l('typeOfProcessedData')

            if typeOfProcessedData == 2:
                return 'fc'

            if typeOfProcessedData == 2:
                return 9

            if typeOfProcessedData == 3:
                return 'cf'

            if typeOfProcessedData == 3:
                return 10

            if typeOfProcessedData == 4:
                return 'pf'

            if typeOfProcessedData == 4:
                return 11

            dummyc = h.get_l('dummyc')

            if dummyc == 0:
                return 'default'

        return wrapped

    h.add(_.Concept('marsType', None, concepts=marsType_inline_concept(h)))

    def marsStream_inline_concept(h):
        def wrapped(h):

            typeOfProcessedData = h.get_l('typeOfProcessedData')

            if typeOfProcessedData == 0:
                return 'oper'

            if typeOfProcessedData == 2:
                return 'oper'

            if typeOfProcessedData == 3:
                return 'enfo'

            if typeOfProcessedData == 4:
                return 'enfo'

            if typeOfProcessedData == 8:
                return 'enfo'

            dummyc = h.get_l('dummyc')

            if dummyc == 0:
                return 'default'

        return wrapped

    h.add(_.Concept('marsStream', None, concepts=marsStream_inline_concept(h)))

    h.alias('mars.stream', 'marsStream')
    h.alias('mars.type', 'marsType')

    if (h.get_s('stepType') == "avg"):
        h.alias('mars.step', 'stepRange')

    if (h.get_l('isHindcast') == 1):
        h.add(_.Constant('theHindcastMarsStream', "enfh"))
        h.alias('mars.stream', 'theHindcastMarsStream')
        h.alias('mars.hdate', 'dataDate')
        h.alias('mars.date', 'modelVersionDate')
        h.alias('mars.time', 'modelVersionTime')

    def is_ocean2d_param_inline_concept(h):
        def wrapped(h):

            discipline = h.get_l('discipline')
            typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
            scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
            scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
            typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

            if discipline == 10 and typeOfFirstFixedSurface == 160 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 255:
                return 1

            if discipline == 10 and typeOfFirstFixedSurface == 20 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 29315 and typeOfSecondFixedSurface == 255:
                return 1

            if discipline == 10 and typeOfFirstFixedSurface == 169 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 255:
                return 1

            scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
            scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

            if discipline == 10 and typeOfFirstFixedSurface == 160 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 160 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300:
                return 1

            dummy = h.get_l('dummy')

            if dummy == 1:
                return 0

        return wrapped

    h.add(_.Concept('is_ocean2d_param', 'zero', concepts=is_ocean2d_param_inline_concept(h)))

    def is_ocean3d_param_inline_concept(h):
        def wrapped(h):

            discipline = h.get_l('discipline')
            typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
            typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

            if discipline == 10 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160:
                return 1

            scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
            scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
            scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
            scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

            if discipline == 10 and typeOfFirstFixedSurface == 160 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 160 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300:
                return 0

            dummy = h.get_l('dummy')

            if dummy == 1:
                return 0

        return wrapped

    h.add(_.Concept('is_ocean3d_param', 'zero', concepts=is_ocean3d_param_inline_concept(h)))

    if h.get_l('is_ocean2d_param'):
        h.add(_.Constant('oceanLevName', "o2d"))
        h.alias('mars.levtype', 'oceanLevName')
        h.unalias('mars.levelist')

    if h.get_l('is_ocean3d_param'):
        h.add(_.Constant('oceanLevName', "o3d"))
        h.alias('mars.levtype', 'oceanLevName')
        h.unalias('mars.levelist')

