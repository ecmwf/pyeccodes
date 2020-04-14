# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .base import NoSize
from .templates import Concepts, empty_concept
import os


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

    def path(self, handle):
        if (self.master or self.local) and self.basename:
            path = self.local if self.local else self.master
            return os.path.join(handle.get(path), self.basename)

    def concepts(self, handle):
        if self._concepts is None:
            path = self.path(handle)
            if path:
                self._concepts = Concepts(path, self.dont_fail).load(handle)
            else:
                return empty_concept
        return self._concepts

    def get(self, handle):
        value = self.concepts(handle)(handle)
        if value is None:
            value = handle.accessor(self.default).get(handle)
        return value
