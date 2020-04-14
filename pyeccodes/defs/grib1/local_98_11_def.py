import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (72 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('classOfAnalysis', 1))
    h.add(_.Unsigned('typeOfAnalysis', 1))
    h.add(_.Unsigned('streamOfAnalysis', 2))
    h.add(_.Ksec1expver('experimentVersionNumberOfAnalysis', 4))
    h.add(_.Unsigned('yearOfAnalysis', 1))
    h.add(_.Unsigned('monthOfAnalysis', 1))
    h.add(_.Unsigned('dayOfAnalysis', 1))
    h.add(_.Unsigned('hourOfAnalysis', 1))
    h.add(_.Unsigned('minuteOfAnalysis', 1))
    h.add(_.Unsigned('centuryOfAnalysis', 1))
    h.add(_.Unsigned('originatingCentreOfAnalysis', 1))
    h.add(_.Unsigned('subcentreOfAnalysis', 1))
    h.add(_.Pad('padding_local11_1', 7))
    h.add(_.Constant('secondsOfAnalysis', 0))
    h.add(_.G1date('dateOfAnalysis', _.Get('centuryOfAnalysis'), _.Get('yearOfAnalysis'), _.Get('monthOfAnalysis'), _.Get('dayOfAnalysis')))
    h.add(_.Time('timeOfAnalysis', _.Get('hourOfAnalysis'), _.Get('minuteOfAnalysis'), _.Get('secondsOfAnalysis')))
    h.alias('date', 'dateOfAnalysis')
    h.alias('time', 'timeOfAnalysis')
