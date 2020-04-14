# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

import weakref
from collections import OrderedDict
from .base import ListAccessor

from .templates import Template


UNSET = object()


class List:

    def __init__(self, handle, name):
        self.name = name
        self.handle = handle
        self._index = 0
        self.accessors = OrderedDict()

    def __enter__(self):
        assert self.handle._list is None
        self.handle._list = self
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.handle._list = None
        for a in self.accessors.values():
            self.handle.add(a)

    def add(self, accessor):
        if accessor.name not in self.accessors:
            self.accessors[accessor.name] = ListAccessor(accessor.name)
        owner = self.accessors[accessor.name]
        owner.add(accessor)


class Handle:

    def __init__(self, buffer, debug=False):

        super().__init__()

        self._buffer = buffer
        self._offset = 0
        self._keys = OrderedDict()
        self._list = None
        self._cache = {}
        self._aliases = OrderedDict()

        self.debug = debug

        Template("boot.def").load(self)

    def _new(self):
        return False

    def _changed(self, *ignore):
        return False

    def _missing(self, *ignore):
        return None

    def _gribex_mode_on(self):
        return False

    def _defined(self, name):
        return name in self._keys

    def _add(self, accessor):
        # print("DECACHE")
        self._cache = {}
        self._keys[accessor.name] = accessor

    def _get(self, name):

        name = self._aliases.get(name, name)

        accessor = self._keys.get(name)
        if accessor is None:
            for alias, target in self._aliases.items():
                if '.' in alias:
                    _, n = alias.split('.')
                    if n == name:
                        accessor = self._keys.get(target)

        return accessor

    def raw(self, name):
        return self._get(name).raw(self)

    def get(self, name, kind=None):
        accessor = self._get(name)
        if accessor is None:
            return None

        value = self._cache.get((name, kind), UNSET)
        # print("GET", name, kind, 'CACHE', value is not UNSET)

        if value is UNSET:

            if kind:
                value = getattr(accessor, 'get_' + kind)(self)
            else:
                value = accessor.get(self)

            # print("CACHE", name, kind, value)
            self._cache[(name, kind)] = value

        return value

    def get_l(self, name):
        return self.get(name, 'l')

    def get_d(self, name):
        return self.get(name, 'd')

    def get_s(self, name):
        return self.get(name, 's')

    def get_r(self, name):  # 'r' is for raw
        return self.get(name, 'r')

    def add(self, accessor):

        # assert '.' not in accessor.name

        if self._list:
            self._list.add(accessor)

        accessor._handle = weakref.ref(self)
        accessor.offset = self._offset
        self._offset += accessor.length
        if self.debug:
            try:
                v = accessor.get(self)
            except Exception:
                v = '?'
            print('ADD [%s,%s] %s = %s' % (accessor.offset, accessor.offset + accessor.length, accessor, v))
        self._add(accessor)

    def set(self, name, value):
        old = self._get(name)
        self._keys[name] = old.set(value)

    def dump(self):
        for a in self._keys.values():
            a.dump(self)

    def lookup(self, klass):
        return [x for x in self._keys.values() if isinstance(x, klass)]

    def accessor(self, name):
        return self._get(name)

    def list(self, name):
        return List(self, name)

    def alias(self, name, target):
        self._aliases[name] = target

    def unalias(self, name):
        self._aliases.pop(name, None)

    def aliases(self, accessor):
        return [name for name, target in self._aliases.items() if target == accessor.name]

    def namespace(self, space):
        space = space + '.'
        return [name for name in self._aliases.keys() if name.startswith(space)] +\
               [name for name in self._keys.keys() if name.startswith(space)]

    def all_keys(self):
        return list(self._keys.keys()) + list(self._aliases.keys())
