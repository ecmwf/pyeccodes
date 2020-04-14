import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('numberOfCategories', 1))

    with h.list('categories'):
        for i in range(0, h.get_l('numberOfCategories')):
            h.add(_.Codetable('categoryType', 1, "4.91.table", _.Get('masterDir'), _.Get('localDir')))
            h.add(_.Unsigned('codeFigure', 1))
            h.add(_.Unsigned('scaleFactorOfLowerLimit', 1))
            h.add(_.Unsigned('scaledValueOfLowerLimit', 4))
            h.add(_.Unsigned('scaleFactorOfUpperLimit', 1))
            h.add(_.Unsigned('scaledValueOfUpperLimit', 4))
