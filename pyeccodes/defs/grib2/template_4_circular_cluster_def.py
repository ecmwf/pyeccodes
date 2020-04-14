import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('clusterIdentifier', 1))
    h.alias('number', 'clusterIdentifier')
    h.add(_.Unsigned('numberOfClusterHighResolution', 1))
    h.add(_.Unsigned('numberOfClusterLowResolution', 1))
    h.add(_.Unsigned('totalNumberOfClusters', 1))
    h.alias('totalNumber', 'totalNumberOfClusters')
    h.add(_.Codetable('clusteringMethod', 1, "4.8.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('latitudeOfCentralPointInClusterDomain', 4))
    h.add(_.Unsigned('longitudeOfCentralPointInClusterDomain', 4))
    h.add(_.Unsigned('radiusOfClusterDomain', 4))
    h.add(_.Unsigned('numberOfForecastsInTheCluster', 1))
    h.alias('NC', 'numberOfForecastsInTheCluster')
    h.add(_.Unsigned('scaleFactorOfStandardDeviation', 1))
    h.alias('scaleFactorOfStandardDeviationInTheCluster', 'scaleFactorOfStandardDeviation')
    h.add(_.Unsigned('scaledValueOfStandardDeviation', 4))
    h.alias('scaledValueOfStandardDeviationInTheCluster', 'scaledValueOfStandardDeviation')
    h.add(_.Unsigned('scaleFactorOfDistanceFromEnsembleMean', 1))
    h.add(_.Unsigned('scaleFactorOfDistanceFromEnsembleMean', 4))
