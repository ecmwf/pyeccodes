from .base import NoSize
from .expression import evaluate


def date_to_julian(year, month, day):

    if month > 2:
        m1 = month - 3
        y1 = year
    else:
        m1 = month + 9
        y1 = year - 1

    a = 146097 * (y1 // 100) // 4
    d = y1 % 100
    b = 1461 * d // 4
    c = (153 * m1 + 2) // 5 + day + 1721119
    j1 = a + b + c

    return j1


def julian_to_date(jdate):

    x = 4 * jdate - 6884477
    y = (x // 146097) * 100
    e = x % 146097
    d = e // 4

    x = 4 * d + 3
    y = (x // 1461) + y
    e = x % 1461
    d = e // 4 + 1

    x = 5 * d - 3
    m = x // 153 + 1
    e = x % 153
    d = e // 5 + 1

    if m < 11:
        month = m + 2
    else:
        month = m - 10

    day = d
    year = y + m // 11

    return year * 10000 + month * 100 + day


def date_to_julian_yyyymmdd(yyyymmdd):
    return date_to_julian(yyyymmdd // 10000, (yyyymmdd % 10000) // 100, yyyymmdd % 100)


class Julian_day(NoSize):

    def __init__(self, name, date, hour, minute, second):
        super().__init__(name)
        self.date = date
        self.hour = hour
        self.minute = minute
        self.second = second

    def get(self, handle):
        date = evaluate(self.date, handle)
        hour = evaluate(self.hour, handle)
        minute = evaluate(self.minute, handle)
        second = evaluate(self.second, handle)

        offset = (hour - 12) * 3600 + minute * 60 + second

        return date_to_julian_yyyymmdd(date) + float(offset) / (24.0 * 60.0 * 60.0)


class ValidDateTime(NoSize):

    def __init__(self, name, date, time, step, units,
                 yearOfEndOfOverallTimeInterval=None,
                 monthOfEndOfOverallTimeInterval=None,
                 dayOfEndOfOverallTimeInterval=None):
        super().__init__(name)
        self.date = date
        self.time = time
        self.step = step
        self.units = units

        self.yearOfEndOfOverallTimeInterval = yearOfEndOfOverallTimeInterval
        self.monthOfEndOfOverallTimeInterval = monthOfEndOfOverallTimeInterval
        self.dayOfEndOfOverallTimeInterval = dayOfEndOfOverallTimeInterval

    def get(self, handle):
        date = evaluate(self.date, handle)
        time = evaluate(self.time, handle)
        step = evaluate(self.step, handle)
        units = evaluate(self.units, handle)

        assert self.yearOfEndOfOverallTimeInterval is None
        assert self.monthOfEndOfOverallTimeInterval is None
        assert self.dayOfEndOfOverallTimeInterval is None

        assert units == 1
        if step is None:
            step = 0

        hour = time // 100
        minute = time % 100

        assert minute == 0

        j = date_to_julian_yyyymmdd(date) * 24 + hour + step

        time = (j % 24) * 100
        date = julian_to_date(j // 24)

        return (date, time)


class Validity_date(ValidDateTime):

    def get(self, handle):
        return super().get(handle)[0]


class Validity_time(ValidDateTime):

    def get_s(self, handle):
        return "%04d" % (self.get(handle),)

    def get(self, handle):
        return super().get(handle)[1]


class G2date(NoSize):

    def __init__(self, name, year, month, day):
        super().__init__(name)
        self.year = year
        self.month = month
        self.day = day

    def get(self, handle):
        year = evaluate(self.year, handle)
        month = evaluate(self.month, handle)
        day = evaluate(self.day, handle)
        return year * 10000 + month * 100 + day


class Time(NoSize):

    def __init__(self, name, hour, minute, second):
        super().__init__(name)
        self.hour = hour
        self.minute = minute
        self.second = second

    def get(self, handle):
        hour = evaluate(self.hour, handle)
        minute = evaluate(self.minute, handle)
        second = evaluate(self.second, handle)
        assert second == 0
        return hour * 100 + minute
