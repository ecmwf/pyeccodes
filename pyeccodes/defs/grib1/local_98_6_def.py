import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Pad('padding_loc6_1', 2))
    h.add(_.Unsigned('dateSSTFieldUsed', 3))
    h.add(_.Unsigned('typeOfSSTFieldUsed', 1))
    h.add(_.Unsigned('countOfICEFieldsUsed', 1))

    with h.list('ICEFieldsUsed'):
        for i in range(0, h.get_l('countOfICEFieldsUsed')):
            h.add(_.Unsigned('dateOfIceFieldUsed', 3))
            h.add(_.Unsigned('satelliteNumber', 1))
    h.add(_.Constant('GRIBEXSection1Problem', ((56 + (_.Get('countOfICEFieldsUsed') * 3)) - _.Get('section1Length'))))
