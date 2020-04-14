import pyeccodes.accessors as _


def load(h):

    h.alias('mars.step', 'endStep')
    h.alias('mars.date', 'dateOfForecast')
    h.alias('mars.time', 'timeOfForecast')
    h.alias('mars.origin', 'inputOriginatingCentre')
    h.alias('mars.anoffset', 'anoffset')
    h.add(_.Sprintf('efas_model', "%s", _.Get('efas_post_proc')))
    h.alias('mars.model', 'efas_model')
