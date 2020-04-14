import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('n2', 1))
    h.add(_.Unsigned('n3', 1))
    h.add(_.Unsigned('Ni', 2))
    h.add(_.Unsigned('nd', 1))
    h.alias('numberOfDiamonds', 'nd')
    h.add(_.Signed('latitudeOfThePolePoint', 4))
    h.add(_.Scale('latitudeOfThePolePointInDegrees', _.Get('latitudeOfThePolePoint'), _.Get('one'), _.Get('grib2divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfThePolePointInDegrees', 'latitudeOfThePolePointInDegrees')
    h.add(_.Unsigned('longitudeOfThePolePoint', 4))
    h.add(_.G2lon('longitudeOfThePolePointInDegrees', _.Get('longitudeOfThePolePoint')))
    h.alias('geography.longitudeOfThePolePointInDegrees', 'longitudeOfThePolePointInDegrees')
    h.add(_.Unsigned('longitudeOfFirstDiamondCentreLine', 4))
    h.add(_.G2lon('longitudeOfFirstDiamondCentreLineInDegrees', _.Get('longitudeOfFirstDiamondCentreLine')))
    h.alias('geography.longitudeOfFirstDiamondCentreLineInDegrees', 'longitudeOfFirstDiamondCentreLineInDegrees')
    h.add(_.Codetable('gridPointPosition', 1, "3.8.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codeflag('numberingOrderOfDiamonds', 1, "grib2/tables/[tablesVersion]/3.9.table"))
    h.add(_.Codeflag('scanningModeForOneDiamond', 1, "grib2/tables/[tablesVersion]/3.10.table"))
    h.add(_.Unsigned('totalNumberOfGridPoints', 4))
    h.alias('nt', 'totalNumberOfGridPoints')
