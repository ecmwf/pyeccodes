# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.


from .data import Unsigned
from .expression import evaluate
from .templates import Table
from .base import NoSize

import os

TABLES = {}


def load_table(paths, handle):

    result = TABLES.get(paths)
    if result is None:
        result = {}
        for path in paths:
            for row in Table(path, True).load(handle):
                result[row['code']] = row
        TABLES[path] = result
    return result


class CodetableMixin:

    def paths(self, handle):

        basename = evaluate(self.basename, handle)
        master = evaluate(self.master, handle)
        local = evaluate(self.local, handle)

        if (master or local) and basename:
            paths = []
            if master:
                paths += [os.path.join(master, basename)]
            if local:
                paths += [os.path.join(local, basename)]
            return tuple(paths)

        return (basename,)

    def table(self, handle):
        if self._table is None:
            self._table = load_table(self.paths(handle), handle)
            assert self._table is not None, self.path(handle)
        return self._table

    def get_l(self, handle):
        return self.code(handle)

    def get_s(self, handle):
        return str(self.element(handle).get('abbr'))

    def title(self, handle):
        return self.element(handle).get('title')

    def units(self, handle):
        return self.element(handle).get('units')

    def element(self, handle):
        code = self.code(handle)
        # assert self.table(handle).get(code), (code, self.paths(handle), self.table(handle))
        return self.table(handle).get(code, {})


class UnsignedCodetableMixin(Unsigned):

    def __init__(self, name, length, basename, master=None, local=None):
        super().__init__(name, length)
        self.basename = basename
        self._table = None
        self.master = master
        self.local = local

    def code(self, handle):
        return super().get(handle)


class Codetable(UnsignedCodetableMixin, CodetableMixin):

    def get_s(self, handle):
        return CodetableMixin.get_s(self, handle)

    def get(self, handle):
        return CodetableMixin.get_l(self, handle)


class StringCodetable(UnsignedCodetableMixin, CodetableMixin):

    def get_l(self, handle):
        return CodetableMixin.get_l(self, handle)

    def get(self, handle):
        return CodetableMixin.get_s(self, handle)


class NoSizeCodetable(NoSize, CodetableMixin):

    def __init__(self, name, index, path):
        super().__init__(name)
        self.index = index
        self.path = path

    def path(self, handle):
        return evaluate(self._path, handle)

    def code(self, handle):
        return evaluate(self.index, help)


class TransientCodetable(NoSizeCodetable):

    def get_s(self, handle):
        return CodetableMixin.get_s(self, handle)

    def get(self, handle):
        return CodetableMixin.get_l(self, handle)


class StringTransientCodetable(NoSizeCodetable):

    def get_l(self, handle):
        return CodetableMixin.get_l(self, handle)

    def get(self, handle):
        return CodetableMixin.get_l(self, handle)


class Codeflag(Unsigned):

    def __init__(self, name, length, path, *ignore):
        super().__init__(name, length)
        self.path = path

    # def get(self, handle):
    #     print(self.path)
    #     return super().get(handle)


class Codetable_title(NoSize):

    def __init__(self, name, table):
        super().__init__(name)
        self.table = table

    def get(self, handle):
        return handle.accessor(self.table.name).title(handle)


class Codetable_units(NoSize):

    def __init__(self, name, table):
        super().__init__(name)
        self.table = table

    def get(self, handle):
        return handle.accessor(self.table.name).units(handle)
