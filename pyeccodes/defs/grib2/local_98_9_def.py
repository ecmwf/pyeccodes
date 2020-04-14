import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('forecastOrSingularVectorNumber', 2))
    h.add(_.Constant('perturbedType', 60))

    if (h.get_l('type') != h.get_l('perturbedType')):
        h.add(_.Unsigned('numberOfIterations', 2))
        h.add(_.Unsigned('numberOfSingularVectorsComputed', 2))
        h.add(_.Unsigned('normAtInitialTime', 1))
        h.add(_.Unsigned('normAtFinalTime', 1))
        h.add(_.Unsigned('multiplicationFactorForLatLong', 4))
        h.add(_.Signed('northWestLatitudeOfLPOArea', 4))
        h.add(_.Signed('northWestLongitudeOfLPOArea', 4))
        h.add(_.Signed('southEastLatitudeOfLPOArea', 4))
        h.add(_.Signed('southEastLongitudeOfLPOArea', 4))
        h.add(_.Unsigned('accuracyMultipliedByFactor', 4))
        h.add(_.Unsigned('numberOfSingularVectorsEvolved', 2))
        h.add(_.Signed('NINT_LOG10_RITZ', 4))
        h.add(_.Signed('NINT_RITZ_EXP', 4))
        h.alias('local.numberOfIterations', 'numberOfIterations')
        h.alias('local.numberOfSingularVectorsComputed', 'numberOfSingularVectorsComputed')
        h.alias('local.normAtInitialTime', 'normAtInitialTime')
        h.alias('local.normAtFinalTime', 'normAtFinalTime')
        h.alias('local.multiplicationFactorForLatLong', 'multiplicationFactorForLatLong')
        h.alias('local.northWestLatitudeOfLPOArea', 'northWestLatitudeOfLPOArea')
        h.alias('local.northWestLongitudeOfLPOArea', 'northWestLongitudeOfLPOArea')
        h.alias('local.southEastLatitudeOfLPOArea', 'southEastLatitudeOfLPOArea')
        h.alias('local.southEastLongitudeOfLPOArea', 'southEastLongitudeOfLPOArea')
        h.alias('local.accuracyMultipliedByFactor', 'accuracyMultipliedByFactor')
        h.alias('local.numberOfSingularVectorsEvolved', 'numberOfSingularVectorsEvolved')
        h.alias('local.NINT_LOG10_RITZ', 'NINT_LOG10_RITZ')
        h.alias('local.NINT_RITZ_EXP', 'NINT_RITZ_EXP')

