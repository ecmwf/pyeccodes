import pyeccodes.accessors as _


def load(h):

    h.add(_.Label('subhourly'))
    h.alias('defaultStepUnits', 'indicatorOfUnitOfTimeRange')
