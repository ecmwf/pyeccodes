# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

import numpy as np
from .expression import evaluate


class Iterator:

    def __init__(self,
                 handle,
                 numberOfPoints,
                 missingValue,
                 values,
                 longitudeFirstInDegrees,
                 DiInDegrees,
                 Ni,
                 Nj,
                 iScansNegatively,
                 latitudeFirstInDegrees,
                 DjInDegrees,
                 jScansPositively,
                 jPointsAreConsecutive):
        self.handle = handle
        self.numberOfPoints = numberOfPoints
        self.missingValue = missingValue
        self.values = values
        self.longitudeFirstInDegrees = longitudeFirstInDegrees
        self.DiInDegrees = DiInDegrees
        self.Ni = Ni
        self.Nj = Nj
        self.iScansNegatively = iScansNegatively
        self.latitudeFirstInDegrees = latitudeFirstInDegrees
        self.DjInDegrees = DjInDegrees
        self.jScansPositively = jScansPositively
        self.jPointsAreConsecutive = jPointsAreConsecutive


def LatlonIteratorGen(latlon):

    lat = latlon.latitudeFirstInDegrees
    lon = latlon.longitudeFirstInDegrees

    Ni = latlon.Ni

    Di = latlon.DiInDegrees
    Dj = latlon.DjInDegrees

    i = 0

    for v in latlon.values:
        # yield (lat, lon, v)
        yield (lat, lon, v)

        i += 1
        if i == Ni:
            i = 0
            lon = latlon.longitudeFirstInDegrees
            lat -= Dj
        else:
            lon += Di


class LatlonIterator(Iterator):

    def __iter__(self):
        # TODO: Should be passed as a key
        assert not self.handle.get('is_rotated_grid')

        assert not self.iScansNegatively
        assert not self.jScansPositively
        assert not self.jPointsAreConsecutive

        self.gen = LatlonIteratorGen(self)

        return self

    def __next__(self):
        return next(self.gen)

    def distinct_latitudes(self):
        if self.Nj is None:
            return None
        result = np.arange(self.latitudeFirstInDegrees, self.latitudeFirstInDegrees - self.Nj * self.DjInDegrees, -self.DjInDegrees)
        assert len(result) == self.Nj
        return result

    def distinct_longitudes(self):
        if self.Ni is None:
            return None
        result = np.arange(self.longitudeFirstInDegrees, self.longitudeFirstInDegrees + self.Ni * self.DiInDegrees, self.DiInDegrees)
        assert len(result) == self.Ni
        return result


ITERATORS = {
    'latlon': LatlonIterator,
}
