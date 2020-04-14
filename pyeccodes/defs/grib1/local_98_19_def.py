import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Constant('GRIBEXSection1Problem', (80 - _.Get('section1Length'))))
    h.add(_.Unsigned('number', 1))
    h.alias('perturbationNumber', 'number')
    h.add(_.Unsigned('ensembleSize', 1))
    h.alias('totalNumber', 'ensembleSize')
    h.add(_.Sprintf('quantile', "%s:%s", _.Get('number'), _.Get('ensembleSize')))
    h.add(_.Unsigned('versionNumberOfExperimentalSuite', 1))
    h.alias('powerOfTenUsedToScaleClimateWeight', 'versionNumberOfExperimentalSuite')
    h.add(_.Unsigned('implementationDateOfModelCycle', 4))
    h.alias('weightAppliedToClimateMonth1', 'implementationDateOfModelCycle')
    h.add(_.Unsigned('numberOfReforecastYearsInModelClimate', 3))
    h.alias('firstMonthUsedToBuildClimateMonth1', 'numberOfReforecastYearsInModelClimate')
    h.add(_.Unsigned('numberOfDaysInClimateSamplingWindow', 3))
    h.alias('lastMonthUsedToBuildClimateMonth1', 'numberOfDaysInClimateSamplingWindow')
    h.add(_.Unsigned('sampleSizeOfModelClimate', 3))
    h.alias('firstMonthUsedToBuildClimateMonth2', 'sampleSizeOfModelClimate')
    h.add(_.Unsigned('versionOfModelClimate', 3))
    h.alias('lastMonthUsedToBuildClimateMonth2', 'versionOfModelClimate')
    h.add(_.Unsigned('efiOrder', 1))
    h.add(_.Pad('padding_loc19_2', 11))
