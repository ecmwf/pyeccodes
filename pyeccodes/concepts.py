# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .base import NoSize
from .templates import Concepts
import os
# from .expression import evaluate


class VisitConcept:

    def __init__(self, concepts, dont_fail):
        self.concepts = concepts

    def __call__(self, handle):
        for c in self.concepts:
            result = c(handle)
            if result is not None:
                return result
        return None


class Concept(NoSize):

    def __init__(self, name,
                 default,
                 basename=None,
                 master=None,
                 local=None,
                 dont_fail=None,
                 concepts=None):
        super().__init__(name)
        self._concepts = None
        self.default = default
        self.basename = basename
        self.master = master
        self._concepts = concepts
        self.local = local
        self.dont_fail = dont_fail

    def paths(self, handle):
        basename = self.basename
        master = handle.get(self.master)
        local = handle.get(self.local)

        if (master or local) and basename:
            paths = []
            if local:
                paths += [os.path.join(local, basename)]

            if master:
                paths += [os.path.join(master, basename)]
            return tuple(paths)

        return (basename,)

    def concepts(self, handle):
        if self._concepts is None:
            paths = self.paths(handle)
            self._concepts = VisitConcept([Concepts(path, True).load(handle) for path in paths], self.dont_fail)
        return self._concepts

    def get(self, handle):
        value = self.concepts(handle)(handle)
        if value is None:
            value = handle.accessor(self.default).get(handle)
        return value

    def extra_info(self):
        return self.paths(self.handle)
