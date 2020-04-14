# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.


from .base import NoSize
from .expression import evaluate

import numpy as np

from .templates import Values

CACHE = {}


def gaussian_latitudes(N, handle):
    result = CACHE.get(N)
    if result is None:
        result = np.array(Values('gaussians/%s' % (N,)).load(handle))
        CACHE[N] = result
    return result


class Global_gaussian(NoSize):

    def __init__(self, name,
                 N,
                 Ni,
                 iDirectionIncrement,
                 latitudeOfFirstGridPoint,
                 longitudeOfFirstGridPoint,
                 latitudeOfLastGridPoint,
                 longitudeOfLastGridPoint,
                 PLPresent,
                 pl,
                 basicAngleOfTheInitialProductionDomain=None,
                 subdivisionsOfBasicAngle=None):
        super().__init__(name)


class Number_of_points_gaussian(NoSize):

    def __init__(self, name,
                 Ni,
                 Nj,
                 PLPresent,
                 pl,
                 N,
                 latitudeOfFirstGridPointInDegrees,
                 longitudeOfFirstGridPointInDegrees,
                 latitudeOfLastGridPointInDegrees,
                 longitudeOfLastGridPointInDegrees,
                 legacy):
        super().__init__(name)
        self.N = N
        self.Ni = Ni
        self.PLPresent = PLPresent
        self.pl = pl

    # def get(self, handle):
    #     N = evaluate(self.N, handle)
    #     print(gaussian_latitudes(N, handle))


class Octahedral_gaussian(NoSize):

    def __init__(self, name, N, Ni, PLPresent, pl):
        super().__init__(name)
        self.PLPresent = PLPresent
        self.pl = pl

    def get(self, handle):
        PLPresent = evaluate(self.PLPresent, handle)
        if not PLPresent:
            return 0

        pl = evaluate(self.pl, handle)
        assert len(pl) % 2 == 0
        north = pl[:len(pl) // 2]
        south = pl[len(pl) // 2:]
        north = north[1:] - north[:-1]
        south = south[1:] - south[:-1]
        return np.all(north == 4) and np.all(south == -4)


class Gaussian_grid_name(NoSize):

    def __init__(self, name, N, Ni, isOctahedral):
        super().__init__(name)
        self.N = N
        self.Ni = Ni
        self.isOctahedral = isOctahedral

    def get(self, handle):
        N = evaluate(self.N, handle)
        Ni = evaluate(self.Ni, handle)

        if Ni is not None:
            return 'N%s' % (N,)

        isOctahedral = evaluate(self.isOctahedral, handle)
        if isOctahedral:
            return 'O%s' % (N,)

        return 'R%s' % (N,)
