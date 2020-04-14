import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('numberOfTimeSteps', 4))
    h.alias('NT', 'numberOfTimeSteps')
    h.add(_.Codetable('unitOfOffsetFromReferenceTime', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('offsetFromReferenceOfFirstTime', 4))
    h.add(_.Codetable('typeOfTimeIncrement', 1, "4.11.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('unitOfTimeIncrement', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('timeIncrement', 4))
    h.add(_.Unsigned('year', 2))
    h.add(_.Unsigned('month', 1))
    h.add(_.Unsigned('day', 1))
    h.add(_.Unsigned('hour', 1))
    h.add(_.Unsigned('minute', 1))
    h.add(_.Unsigned('second', 1))
    h.add(_.Unsigned('numberOfVerticalPoints', 2))
    h.add(_.Codetable('physicalMeaningOfVerticalCoordinate', 1, "3.15.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('verticalCoordinate', 1, "3.21.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('NC', 2))
