import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('clusterIdentifier', 1))
    h.alias('number', 'clusterIdentifier')
    h.add(_.Unsigned('NH', 1))
    h.add(_.Unsigned('NL', 1))
    h.add(_.Unsigned('totalNumberOfClusters', 1))
    h.alias('totalNumber', 'totalNumberOfClusters')
    h.add(_.Codetable('clusteringMethod', 1, "4.8.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('northernLatitudeOfClusterDomain', 4))
    h.add(_.Unsigned('southernLatitudeOfClusterDomain', 4))
    h.add(_.Unsigned('easternLongitudeOfClusterDomain', 4))
    h.add(_.Unsigned('westernLongitudeOfClusterDomain', 4))
    h.add(_.Unsigned('numberOfForecastsInTheCluster', 1))
    h.alias('NC', 'numberOfForecastsInTheCluster')
    h.add(_.Unsigned('scaleFactorOfStandardDeviation', 1))
    h.alias('scaleFactorOfStandardDeviationInTheCluster', 'scaleFactorOfStandardDeviation')
    h.add(_.Unsigned('scaledValueOfStandardDeviation', 4))
    h.alias('scaledValueOfStandardDeviationInTheCluster', 'scaledValueOfStandardDeviation')
    h.add(_.Unsigned('scaleFactorOfDistanceFromEnsembleMean', 1))
    h.add(_.Unsigned('scaledValueOfDistanceFromEnsembleMean', 4))
