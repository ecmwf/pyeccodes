import pyeccodes.accessors as _


def load(h):

    h.alias('mars.step', 'stepRange')
    h.add(_.Sprintf('marsQuantile', "%d:%d", _.Get('perturbationNumber'), _.Get('numberOfForecastsInEnsemble')))
    h.alias('mars.quantile', 'marsQuantile')
