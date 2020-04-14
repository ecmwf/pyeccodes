import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('baseDateEPS', 4))
    h.add(_.Unsigned('baseTimeEPS', 2))
    h.add(_.Unsigned('numberOfRepresentativeMember', 1))
    h.add(_.Unsigned('numberOfMembersInCluster', 1))
    h.add(_.Unsigned('totalInitialConditions', 1))
