import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (328 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('clusterNumber', 1))
    h.alias('number', 'clusterNumber')
    h.add(_.Unsigned('totalNumberOfClusters', 1))
    h.alias('totalNumber', 'totalNumberOfClusters')
    h.add(_.Pad('padding_loc2_1', 1))
    h.add(_.Unsigned('clusteringMethod', 1))
    h.add(_.Unsigned('startTimeStep', 2))
    h.add(_.Unsigned('endTimeStep', 2))
    h.add(_.Signed('northernLatitudeOfDomain', 3))
    h.add(_.Signed('westernLongitudeOfDomain', 3))
    h.add(_.Signed('southernLatitudeOfDomain', 3))
    h.add(_.Signed('easternLongitudeOfDomain', 3))
    h.add(_.Ascii('clusteringDomain', 1))
    h.add(_.Unsigned('operationalForecastCluster', 1))
    h.add(_.Unsigned('controlForecastCluster', 1))
    h.add(_.Unsigned('representativeMember', 1))
    h.add(_.Codetable('climatologicalRegime', 1, "grib1/regime.table"))
    h.add(_.Unsigned('numberOfForecastsInCluster', 1))

    if (h.get_l('numberOfForecastsInCluster') > 0):
        h.add(_.Unsigned('ensembleForecastNumbers', 1, _.Get('numberOfForecastsInCluster')))

    h.add(_.Padto('padding_loc2_2', (_.Get('offsetSection1') + 328)))
    h.alias('mars.number', 'clusterNumber')
    h.alias('mars.domain', 'clusteringDomain')
