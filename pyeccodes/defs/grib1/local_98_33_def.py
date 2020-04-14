import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Constant('GRIBEXSection1Problem', 0))
    h.add(_.Unsigned('yearOfReference', 1))
    h.add(_.Unsigned('monthOfReference', 1))
    h.add(_.Unsigned('dayOfReference', 1))
    h.add(_.Unsigned('hourOfReference', 1))
    h.add(_.Unsigned('minuteOfReference', 1))
    h.add(_.Unsigned('centuryOfReference', 1))
    h.add(_.Transient('secondsOfReference', 0))
    h.add(_.Unsigned('numberOfForcasts', 1))

    if h.get_l('numberOfForcasts'):
        h.add(_.Unsigned('forecastSteps', 3, _.Get('numberOfForcasts')))

    h.add(_.Unsigned('numberOfAnalysis', 1))

    if h.get_l('numberOfAnalysis'):
        h.add(_.Signed('analysisOffsets', 3, _.Get('numberOfAnalysis')))

    h.add(_.G1date('dateOfReference', _.Get('centuryOfReference'), _.Get('yearOfReference'), _.Get('monthOfReference'), _.Get('dayOfReference')))
    h.add(_.Time('timeOfReference', _.Get('hourOfReference'), _.Get('minuteOfReference'), _.Get('secondsOfReference')))
