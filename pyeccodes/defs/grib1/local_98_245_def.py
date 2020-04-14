import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.add(_.Ascii('Model_Identifier', 8))
    h.add(_.Ascii('LBC_Initial_Conditions', 8))
    h.add(_.Ascii('Model_LBC_Member_Identifier', 4))
    h.add(_.Ascii('Model_Additional_Information', 8))
    h.add(_.Pad('padding_loc245_1', 20))
    h.add(_.Unsigned('Extra_Data_FreeFormat_0_none', 2))
    h.add(_.Position('offsetFreeFormData'))
    h.add(_.Unsigned('freeFormData', 1, _.Get('Extra_Data_FreeFormat_0_none')))
    h.add(_.Padtomultiple('padding_loc245_2', _.Get('offsetSection1'), 80))
