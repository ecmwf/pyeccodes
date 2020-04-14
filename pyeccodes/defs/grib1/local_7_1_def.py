import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('type', 1))
    h.add(_.Unsigned('identificationNumber', 1))
    h.add(_.Unsigned('productIdentifier', 1))
    h.add(_.Unsigned('spatialSmoothingOfProduct', 1))
    h.add(_.Constant('sectionLengthLimitForProbability', 45))

    if (h.get_l('section1Length') > h.get_l('sectionLengthLimitForProbability')):
        h.add(_.Unsigned('probProductDefinition', 1))
        h.add(_.Unsigned('probabilityType', 1))
        h.add(_.Unsigned('lowerLimit', 4))
        h.add(_.Unsigned('upperLimit', 4))
        h.add(_.Pad('padding_local_7_1', 5))

    h.add(_.Constant('sectionLengthLimitForEnsembles', 60))

    if (h.get_l('section1Length') > h.get_l('sectionLengthLimitForEnsembles')):
        h.add(_.Unsigned('ensembleSize', 1))
        h.add(_.Unsigned('clusterSize', 1))
        h.add(_.Unsigned('numberOfClusters', 1))
        h.add(_.Unsigned('clusteringMethod', 1))
        h.add(_.Signed('northLatitudeOfCluster', 3))
        h.add(_.Signed('southLatitudeOfCluster', 3))
        h.add(_.Signed('westLongitudeOfCluster', 3))
        h.add(_.Signed('eastLongitudeOfCluster', 3))
        h.add(_.Unsigned('clusterMember1', 1))
        h.add(_.Unsigned('clusterMember2', 1))
        h.add(_.Unsigned('clusterMember3', 1))
        h.add(_.Unsigned('clusterMember4', 1))
        h.add(_.Unsigned('clusterMember5', 1))
        h.add(_.Unsigned('clusterMember6', 1))
        h.add(_.Unsigned('clusterMember7', 1))
        h.add(_.Unsigned('clusterMember8', 1))
        h.add(_.Unsigned('clusterMember9', 1))
        h.add(_.Unsigned('clusterMember10', 1))

