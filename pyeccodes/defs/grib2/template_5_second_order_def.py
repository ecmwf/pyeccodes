import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('groupSplitting', 1, "5.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('missingValueManagement', 1, "5.5.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('primaryMissingValue', 4))
    h.add(_.Unsigned('secondaryMissingValue', 4))
    h.add(_.Unsigned('numberOfGroups', 4))
    h.alias('NG', 'numberOfGroups')
    h.add(_.Unsigned('referenceOfWidths', 1))
    h.add(_.Unsigned('widthOfWidths', 1))
    h.add(_.Unsigned('referenceOfLengths', 4))
    h.add(_.Unsigned('incrementOfLengths', 1))
    h.add(_.Unsigned('trueLengthOfLastGroup', 4))
    h.add(_.Unsigned('widthOfLengths', 1))
