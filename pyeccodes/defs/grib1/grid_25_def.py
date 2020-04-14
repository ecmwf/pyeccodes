import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('Ni', 72))
    h.add(_.Constant('Nj', 19))
    h.add(_.Constant('longitudeOfFirstGridPoint', 0))
    h.add(_.Constant('longitudeOfLastGridPoint', 355000))
    h.add(_.Constant('latitudeOfFirstGridPoint', 0))
    h.add(_.Constant('latitudeOfLastGridPoint', 90000))
    h.add(_.Constant('iDirectionIncrement', 5000))
    h.add(_.Constant('jDirectionIncrement', 5000))
    h.add(_.Constant('numberOfDataPoints', 1368))
    h.add(_.Constant('numberOfValues', 1297))
