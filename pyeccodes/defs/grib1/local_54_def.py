import pyeccodes.accessors as _


def load(h):

    h.add(_.Label('CMC local definition (Canada)'))
    h.add(_.Unsigned('applicationIdentifier', 1))
    h.add(_.Unsigned('type', 1))
    h.add(_.Unsigned('identificationNumber', 1))
    h.add(_.Unsigned('productIdentifier', 1))
    h.add(_.Unsigned('spatialSmoothingOfProduct', 1))
    h.add(_.Unsigned('isotopeIdentificationNumber', 2))
