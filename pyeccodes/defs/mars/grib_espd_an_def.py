import pyeccodes.accessors as _


def load(h):

    h.alias('mars.date', 'dataDate')
    h.alias('mars.time', 'dataTime')

    if (h.get_s('class') == "od"):
        h.alias('mars.origin', 'centre')

    if (h.get_s('class') == "e2"):
        h.alias('mars.origin', 'centre')

    if (h.get_s('class') == "em"):
        h.alias('mars.origin', 'centre')

    h.add(_.Sprintf('marsGrid', "%g/%g", _.Get('iDirectionIncrementInDegrees'), _.Get('jDirectionIncrementInDegrees')))
    h.alias('mars.grid', 'marsGrid')
    h.alias('mars.number', 'perturbationNumber')
