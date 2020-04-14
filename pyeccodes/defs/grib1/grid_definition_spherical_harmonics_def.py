import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('J', 2))
    h.alias('pentagonalResolutionParameterJ', 'J')
    h.alias('geography.J', 'J')
    h.add(_.Unsigned('K', 2))
    h.alias('pentagonalResolutionParameterK', 'K')
    h.alias('geography.K', 'K')
    h.add(_.Unsigned('M', 2))
    h.alias('pentagonalResolutionParameterM', 'M')
    h.alias('geography.M', 'M')
    h.add(_.Constant('_T', -1))
    h.add(_.Spectral_truncation('numberOfValues', _.Get('J'), _.Get('K'), _.Get('M'), _.Get('_T')))
    h.alias('numberOfPoints', 'numberOfValues')
    h.alias('numberOfDataPoints', 'numberOfValues')
    h.add(_.Codetable('representationType', 1, "grib1/9.table"))
    h.add(_.Codetable('representationMode', 1, "grib1/10.table"))
    h.add(_.Pad('padding_grid50_1', 18))
    h.add(_.Constant('Nj', 0))
