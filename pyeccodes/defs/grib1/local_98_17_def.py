import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.add(_.Unsigned('dateOfSSTFieldUsed', 3))
    h.add(_.Unsigned('typeOfSSTFieldUsed', 1))
    h.add(_.Unsigned('countOfICEFieldsUsed', 1))
    h.add(_.Position('offsetICEFieldsUsed'))

    with h.list('ICEFieldsUsed'):
        for i in range(0, h.get_l('countOfICEFieldsUsed')):
            h.add(_.Unsigned('dateOfIceFieldUsed', 3))
            h.add(_.Unsigned('satelliteNumber', 1))
    h.add(_.Padtomultiple('padding_loc17_2', _.Get('offsetICEFieldsUsed'), 40))
    h.add(_.Position('offsetAfterPadding'))
    h.add(_.Constant('GRIBEXSection1Problem', ((_.Get('offsetAfterPadding') - _.Get('offsetICEFieldsUsed')) % 40)))
