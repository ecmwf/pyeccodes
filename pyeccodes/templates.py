# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

import re
import importlib


def empty_concept(handle):
    pass


class Module:

    def __init__(self, pattern, dont_fail=False):
        self.pattern = pattern
        self.matches = list(re.finditer(r'\[[^[]*\]', self.pattern))
        self.dont_fail = dont_fail
        # self.dont_fail = False

    def load(self, handle):
        path = []

        last = 0
        for m in self.matches:
            a, b = m.span()
            path.append(self.pattern[last:a])
            p = self.pattern[a:b][1:-1]
            if ':' in p:
                name, kind = p.split(':')
            else:
                name, kind = p, 'l'
            path.append(str(handle.get(name, kind)))
            last = b

        path.append(self.pattern[last:])

        path = ''.join(path)
        if handle.debug:
            print("LOAD", path, self.pattern)

        path = path.replace('.', '_').replace('-', '_').replace('/', '.')
        module = 'pyeccodes.defs.%s' % (path,)

        try:
            module = importlib.import_module(module)
        except ModuleNotFoundError:
            if handle.debug:
                print("LOAD fail")
            if self.dont_fail:
                return self.failed_to_load(handle)
            else:
                raise
        return getattr(module, "load")(handle)


class Template(Module):

    def failed_to_load(self, handle):
        pass


class Table(Module):

    def failed_to_load(self, handle):
        return []


class Concepts(Module):

    def failed_to_load(self, handle):
        return empty_concept


class Values(Module):
    pass
