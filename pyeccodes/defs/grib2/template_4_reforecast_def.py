import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('YearOfModelVersion', 2))
    h.add(_.Unsigned('MonthOfModelVersion', 1))
    h.add(_.Unsigned('DayOfModelVersion', 1))
    h.add(_.Unsigned('HourOfModelVersion', 1))
    h.add(_.Unsigned('MinuteOfModelVersion', 1))
    h.add(_.Unsigned('SecondOfModelVersion', 1))
    h.add(_.G2date('modelVersionDate', _.Get('YearOfModelVersion'), _.Get('MonthOfModelVersion'), _.Get('DayOfModelVersion')))
    h.add(_.Time('modelVersionTime', _.Get('HourOfModelVersion'), _.Get('MinuteOfModelVersion'), _.Get('SecondOfModelVersion')))
    h.add(_.Constant('isHindcast', 1))
