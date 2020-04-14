import pyeccodes.accessors as _


def load(h):

    h.add(_.Dirty('dirty_statistics', _.Get('computeStatistics')))
    pass  # when block
    h.add(_.Statistics('computeStatistics', _.Get('missingValue'), _.Get('values')))
    h.add(_.Vector('maximum', _.Get('computeStatistics'), 0))
    h.add(_.Vector('minimum', _.Get('computeStatistics'), 1))
    h.add(_.Vector('average', _.Get('computeStatistics'), 2))
    h.add(_.Count_missing('numberOfMissing', _.Get('bitmap'), _.Get('unusedBitsInBitmap'), _.Get('numberOfDataPoints')))
    h.add(_.Vector('standardDeviation', _.Get('computeStatistics'), 4))
    h.add(_.Vector('skewness', _.Get('computeStatistics'), 5))
    h.add(_.Vector('kurtosis', _.Get('computeStatistics'), 6))
    h.add(_.Vector('isConstant', _.Get('computeStatistics'), 7))
    h.alias('numberOfMissingValues', 'numberOfMissing')
    h.alias('statistics.avg', 'average')
    h.alias('statistics.max', 'maximum')
    h.alias('statistics.min', 'minimum')
    h.alias('statistics.sd', 'standardDeviation')
    h.alias('statistics.skew', 'skewness')
    h.alias('statistics.kurt', 'kurtosis')
    h.alias('statistics.const', 'isConstant')
