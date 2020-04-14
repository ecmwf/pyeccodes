import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('typeOfOriginalFieldValues', 1, "5.1.table", _.Get('masterDir'), _.Get('localDir')))
