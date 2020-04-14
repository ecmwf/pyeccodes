import pyeccodes.accessors as _


def load(h):

    h.add(_.Dirty('dirty_statistics', _.Get('computeStatistics')))
    pass  # when block
    h.add(_.Statistics_spectral('computeStatistics', _.Get('values'), _.Get('J'), _.Get('K'), _.Get('M'), _.Get('JS')))
    h.add(_.Vector('average', _.Get('computeStatistics'), 0))
    h.add(_.Vector('energyNorm', _.Get('computeStatistics'), 1))
    h.add(_.Vector('standardDeviation', _.Get('computeStatistics'), 2))
    h.add(_.Vector('isConstant', _.Get('computeStatistics'), 3))
    h.alias('statistics.avg', 'average')
    h.alias('statistics.enorm', 'energyNorm')
    h.alias('statistics.sd', 'standardDeviation')
    h.alias('statistics.const', 'isConstant')
