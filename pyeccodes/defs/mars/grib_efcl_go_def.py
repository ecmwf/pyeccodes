import pyeccodes.accessors as _


def load(h):

    h.alias('mars.step', 'endStep')
    h.alias('mars.date', 'dateOfModelVersion')
    h.alias('mars.time', 'dataTime')
    h.alias('mars.hdate', 'dataDate')
    h.alias('mars.origin', 'inputOriginatingCentre')
    h.add(_.Sprintf('efas_model', "%s", _.Get('efas_post_proc')))
    h.alias('mars.model', 'efas_model')
