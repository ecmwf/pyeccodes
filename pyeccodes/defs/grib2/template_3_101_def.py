import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('shapeOfTheEarth', 1, "3.2.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('numberOfGridUsed', 3))
    h.add(_.Unsigned('numberOfGridInReference', 1))
    h.add(_.Bytes('uuidOfHGrid', 16))
