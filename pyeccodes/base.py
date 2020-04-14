# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.


class Accessor:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s(%s)" % (self.class_name, self.name)

    @property
    def class_name(self):
        return self.__class__.__name__

    @property
    def handle(self):
        return self._handle()

    def get_l(self, handle):
        result = self.get(handle)
        return None if result is None else int(result)

    def get_s(self, handle):
        result = self.get(handle)
        return None if result is None else str(result)

    def get_d(self, handle):
        return float(self.get(handle))

    def extra_info(self):
        return ""

    def dump(self, handle):
        try:
            v = self.get(handle)
        except Exception as e:
            v = "ERROR %s" % (e,)

        aliases = handle.aliases(self)
        if aliases:
            aliases = " [%s]" % (",".join(aliases),)
        else:
            aliases = ""

        print('[%s,%s] %s = %s%s' % (self.offset, self.offset + self.length, self, v, aliases))


class NoSize(Accessor):
    length = 0


class ListAccessor(NoSize):

    def __init__(self, name):
        super().__init__(name)
        self._list = []

    def add(self, accessor):
        accessor.name = "%s[%d]" % (accessor.name, len(self._list) + 1)
        self._list.append(accessor)

    def get(self, handle):
        result = tuple(a.get(handle) for a in self._list)
        return result[0] if len(result) == 1 else result
