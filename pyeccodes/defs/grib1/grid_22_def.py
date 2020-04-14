import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('Ni', 37))
    h.add(_.Constant('Nj', 37))
    h.add(_.Constant('longitudeOfFirstGridPoint', -180000))
    h.add(_.Constant('longitudeOfLastGridPoint', 0))
    h.add(_.Constant('latitudeOfFirstGridPoint', 0))
    h.add(_.Constant('latitudeOfLastGridPoint', 90000))
    h.add(_.Constant('iDirectionIncrement', 5000))
    h.add(_.Constant('jDirectionIncrement', 2500))
    h.add(_.Constant('numberOfDataPoints', 1369))
    h.add(_.Constant('numberOfValues', 1333))
