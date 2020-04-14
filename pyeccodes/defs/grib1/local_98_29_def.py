import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (960 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('clusterNumber', 1))
    h.alias('number', 'clusterNumber')
    h.add(_.Unsigned('totalNumberOfClusters', 1))
    h.alias('totalNumber', 'totalNumberOfClusters')
    h.add(_.Pad('padding_loc29_1', 1))
    h.add(_.Unsigned('clusteringMethod', 1))
    h.add(_.Signed('northernLatitudeOfDomain', 3))
    h.add(_.Signed('westernLongitudeOfDomain', 3))
    h.add(_.Signed('southernLatitudeOfDomain', 3))
    h.add(_.Signed('easternLongitudeOfDomain', 3))
    h.add(_.Unsigned('numberOfForecastsInCluster', 1))
    h.add(_.Unsigned('numberOfParametersUsedForClustering', 1))
    h.add(_.Unsigned('numberOfPressureLevelsUsedForClustering', 1))
    h.add(_.Unsigned('numberOfStepsUsedForClustering', 1))
    h.add(_.Pad('padding_loc29_2', 10))

    with h.list('listOfEnsembleForecastNumbers'):
        for i in range(0, h.get_l('numberOfForecastsInCluster')):
            h.add(_.Unsigned('baseDateEPS', 4))
            h.add(_.Unsigned('baseTimeEPS', 2))
            h.add(_.Unsigned('number', 1))

    with h.list('listOfParametersUsedForClustering'):
        for i in range(0, h.get_l('numberOfParametersUsedForClustering')):
            h.add(_.Unsigned('parameterCode', 1))
            h.add(_.Unsigned('tableCode', 1))
    h.add(_.Unsigned('pressureLevel', 2, _.Get('numberOfPressureLevelsUsedForClustering')))
    h.add(_.Unsigned('stepForClustering', 2, _.Get('numberOfStepsUsedForClustering')))
    h.add(_.Padto('padding_loc29_3', (_.Get('offsetSection1') + 960)))
    h.alias('number', 'clusterNumber')
