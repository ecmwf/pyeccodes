import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (79 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Constant('wrongPadding', 1))
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Unsigned('baseDateEPS', 4))
    h.add(_.Unsigned('baseTimeEPS', 2))
    h.add(_.Unsigned('numberOfRepresentativeMember', 1))
    h.add(_.Unsigned('numberOfMembersInCluster', 1))
    h.add(_.Unsigned('totalInitialConditions', 1))
    h.add(_.Pad('padding_loc28_1', 19))
