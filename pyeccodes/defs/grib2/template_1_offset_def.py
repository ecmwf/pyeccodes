import pyeccodes.accessors as _


def load(h):

    h.add(_.Signed('numberOfTensOfThousandsOfYearsOfOffset', 2))
    h.alias('paleontologicalOffset', 'numberOfTensOfThousandsOfYearsOfOffset')
