import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('typeOfCalendar', 1, "1.6.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Signed('numberOfTensOfThousandsOfYearsOfOffset', 2))
    h.alias('paleontologicalOffset', 'numberOfTensOfThousandsOfYearsOfOffset')
