import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (1080 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Unsigned('channelNumber', 1))
    h.alias('mars.channel', 'channelNumber')
    h.add(_.Unsigned('scalingFactorForFrequencies', 4))
    h.alias('integerScalingFactorAppliedToFrequencies', 'scalingFactorForFrequencies')
    h.add(_.Unsigned('numberOfFrequencies', 1))
    h.alias('totalNumberOfFrequencies', 'numberOfFrequencies')
    h.alias('Nf', 'numberOfFrequencies')
    h.add(_.Pad('padding_loc37_1', 3))
    h.add(_.Unsigned('listOfScaledFrequencies', 4, _.Get('numberOfFrequencies')))
    h.add(_.Unsigned('offsetToEndOf4DvarWindow', 2))
    h.add(_.Unsigned('lengthOf4DvarWindow', 2))
    h.alias('anoffset', 'offsetToEndOf4DvarWindow')
    h.add(_.Padto('padding_loc37_2', (_.Get('offsetSection1') + 1080)))
