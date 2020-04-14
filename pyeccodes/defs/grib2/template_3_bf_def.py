import pyeccodes.accessors as _


def load(h):

    h.add(_.Label('BiFourier coefficients'))
    h.add(_.Constant('biFourierCoefficients', 1))
    h.add(_.Codetable('spectralType', 1, "3.6.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('spectralDataRepresentationType', 'spectralType')
    h.add(_.Unsigned('biFourierResolutionParameterN', 4))
    h.add(_.Unsigned('biFourierResolutionParameterM', 4))
    h.add(_.Codetable('biFourierTruncationType', 1, "3.25.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('Lx', 8))
    h.alias('geography.LxInMetres', 'Lx')
    h.add(_.Unsigned('Lux', 8))
    h.alias('geography.LuxInMetres', 'Lux')
    h.add(_.Unsigned('Lcx', 8))
    h.alias('geography.LcxInMetres', 'Lcx')
    h.add(_.Unsigned('Ly', 8))
    h.alias('geography.LyInMetres', 'Ly')
    h.add(_.Unsigned('Luy', 8))
    h.alias('geography.LuyInMetres', 'Luy')
    h.add(_.Unsigned('Lcy', 8))
    h.alias('geography.LcyInMetres', 'Lcy')
