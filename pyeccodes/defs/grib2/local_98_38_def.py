import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('iterationNumber', 1))
    h.alias('number', 'iterationNumber')
    h.add(_.Unsigned('totalNumberOfIterations', 1))
    h.alias('totalNumber', 'totalNumberOfIterations')
    h.alias('iteration', 'iterationNumber')
    h.alias('local.iterationNumber', 'iterationNumber')
    h.alias('local.totalNumberOfIterations', 'totalNumberOfIterations')
    h.add(_.Unsigned('offsetToEndOf4DvarWindow', 2))
    h.add(_.Unsigned('lengthOf4DvarWindow', 2))
    h.alias('anoffset', 'offsetToEndOf4DvarWindow')
