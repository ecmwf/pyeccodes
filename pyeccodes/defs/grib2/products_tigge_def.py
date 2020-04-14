import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('marsClass', "ti"))
    h.add(_.Constant('marsModel', "glob"))
    h.alias('is_tigge', 'one')
    h.alias('tigge_short_name', 'shortName')
    h.alias('short_name', 'shortName')
    h.alias('parameter', 'paramId')
    h.alias('tigge_name', 'name')
    h.alias('parameter.paramId', 'paramId')
    h.alias('parameter.shortName', 'shortName')
    h.alias('parameter.units', 'units')
    h.alias('parameter.name', 'name')

    if (h.get_s('levtype') == "sfc"):
        h.unalias('mars.levelist')

    h.alias('mars.expver', 'marsExpver')
    h.alias('mars.class', 'marsClass')
    h.alias('mars.param', 'paramId')
    h.alias('mars.model', 'marsModel')
    h.alias('mars.origin', 'centre')

    if (h.get_l('section2Used') == 1):
        h.add(_.Constant('marsLamModel', "lam"))
        h.alias('mars.model', 'marsLamModel')
        h.alias('mars.origin', 'tiggeSuiteID')
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
