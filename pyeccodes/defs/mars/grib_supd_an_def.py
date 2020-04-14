import pyeccodes.accessors as _


def load(h):

    if (h.get_l('localDefinitionNumber') == 35):
        h.alias('mars.date', 'dataDate')
        h.alias('mars.time', 'dataTime')
    else:
        h.alias('mars.date', 'dateOfAnalysis')
        h.alias('mars.time', 'timeOfAnalysis')

    if (h.get_s('class') == "od"):
        h.alias('mars.origin', 'centre')

    if ((h.get_l('editionNumber') == 2) and (h.get_l('localDefinitionNumber') == 11)):
        h.alias('mars.origin', 'originatingCentreOfAnalysis')

    h.add(_.Sprintf('marsGrid', "%g/%g", _.Get('iDirectionIncrementInDegrees'), _.Get('jDirectionIncrementInDegrees')))
    h.alias('mars.grid', 'marsGrid')
