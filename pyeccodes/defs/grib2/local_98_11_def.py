import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('yearOfAnalysis', 2))
    h.add(_.Unsigned('monthOfAnalysis', 1))
    h.add(_.Unsigned('dayOfAnalysis', 1))
    h.add(_.Unsigned('hourOfAnalysis', 1))
    h.add(_.Unsigned('minuteOfAnalysis', 1))
    h.add(_.StringCodetable('originatingCentreOfAnalysis', 2, "common/c-1.table"))
    h.add(_.Unsigned('subcentreOfAnalysis', 2))
    h.add(_.Constant('secondsOfAnalysis', 0))
    h.add(_.G2date('dateOfAnalysis', _.Get('yearOfAnalysis'), _.Get('monthOfAnalysis'), _.Get('dayOfAnalysis')))
    h.add(_.Time('timeOfAnalysis', _.Get('hourOfAnalysis'), _.Get('minuteOfAnalysis'), _.Get('secondsOfAnalysis')))
    h.alias('date', 'dateOfAnalysis')
    h.alias('time', 'timeOfAnalysis')
