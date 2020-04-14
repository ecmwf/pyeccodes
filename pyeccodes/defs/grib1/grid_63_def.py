import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('Ni', 91))
    h.add(_.Constant('Nj', 46))
    h.add(_.Constant('longitudeOfFirstGridPoint', 0))
    h.add(_.Constant('longitudeOfLastGridPoint', 180000))
    h.add(_.Constant('latitudeOfFirstGridPoint', -90000))
    h.add(_.Constant('latitudeOfLastGridPoint', 0))
    h.add(_.Constant('iDirectionIncrement', 2000))
    h.add(_.Constant('jDirectionIncrement', 2000))
    h.add(_.Constant('numberOfDataPoints', 4186))
    h.add(_.Constant('numberOfValues', 4096))
