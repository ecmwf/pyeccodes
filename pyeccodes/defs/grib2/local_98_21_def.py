import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('forecastOrSingularVectorNumber', 2))
    h.add(_.Unsigned('numberOfIterations', 2))
    h.add(_.Unsigned('numberOfSingularVectorsComputed', 2))
    h.add(_.Unsigned('normAtInitialTime', 1))
    h.add(_.Unsigned('normAtFinalTime', 1))
    h.add(_.Unsigned('multiplicationFactorForLatLong', 4))
    h.add(_.Signed('northWestLatitudeOfVerficationArea', 4))
    h.add(_.Signed('northWestLongitudeOfVerficationArea', 4))
    h.add(_.Signed('southEastLatitudeOfVerficationArea', 4))
    h.add(_.Signed('southEastLongitudeOfVerficationArea', 4))
    h.add(_.Unsigned('accuracyMultipliedByFactor', 4))
    h.add(_.Unsigned('numberOfSingularVectorsEvolved', 2))
    h.add(_.Signed('NINT_LOG10_RITZ', 4))
    h.add(_.Signed('NINT_RITZ_EXP', 4))
    h.add(_.Unsigned('optimisationTime', 1))
    h.alias('mars.opttime', 'optimisationTime')
    h.add(_.Unsigned('forecastLeadTime', 1))
    h.alias('mars.leadtime', 'forecastLeadTime')
    h.add(_.Ascii('marsDomain', 1))
    h.add(_.Unsigned('methodNumber', 2))
    h.add(_.Unsigned('shapeOfVerificationArea', 1))
    h.alias('mars.domain', 'marsDomain')
