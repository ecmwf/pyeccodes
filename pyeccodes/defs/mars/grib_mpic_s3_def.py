import pyeccodes.accessors as _


def load(h):

    h.add(_.G1day_of_the_year_date('dayOfTheYearDate', _.Get('centuryOfReferenceTimeOfData'), _.Get('yearOfCentury'), _.Get('month'), _.Get('day')))
    h.alias('mars.date', 'dayOfTheYearDate')
