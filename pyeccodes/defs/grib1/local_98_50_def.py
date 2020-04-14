import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', (300 - _.Get('section1Length'))))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.alias('totalNumber', 'numberOfForecastsInEnsemble')
    h.add(_.Unsigned('modelIdentifier', 1))
    h.add(_.Signed('latitudeOfNorthWestCornerOfArea', 4))
    h.add(_.Signed('longitudeOfNorthWestCornerOfArea', 4))
    h.add(_.Signed('latitudeOfSouthEastCornerOfArea', 4))
    h.add(_.Signed('longitudeOfSouthEastCornerOfArea', 4))
    h.add(_.Unsigned('originalParameterNumber', 1))
    h.add(_.Unsigned('originalParameterTableNumber', 1))
    h.add(_.Pad('padding_loc50_1', 46))
    h.add(_.Ascii('optionalData', 184))
