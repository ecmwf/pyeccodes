import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Unsigned('perturbationNumber', 1))
    h.alias('number', 'perturbationNumber')
    h.add(_.Unsigned('numberOfForecastsInEnsemble', 1))
    h.add(_.Ascii('************_EXPERIMENT_************', 4))
    h.add(_.Ascii('Experiment_Identifier', 8))
    h.add(_.Ascii('Sub-Experiment_Identifier', 8))
    h.add(_.Ascii('************_PRODUCT_***************', 4))
    h.add(_.Unsigned('Original_CodeTable_2_Version_Number', 1))
    h.add(_.Unsigned('Original_Parameter_Iden_CodeTable2', 1))
    h.add(_.Ascii('Original_Parameter_Identifier', 8))
    h.add(_.Ascii('Product_Identifier', 8))
    h.add(_.Unsigned('Threshold_Or_Distribution_0_no_1_yes', 2))
    h.add(_.Ascii('Threshold_Or_Distribution_Units', 4))
    h.add(_.Unsigned('At_least__Or_Distribut_Proportion_Of', 4))
    h.add(_.Unsigned('Less_Than_Or_To_Overall_Distribution', 4))
    h.add(_.Pad('padding_loc244_1', 40))
    h.add(_.Ascii('************_ENSEMBLE_**************', 4))
    h.add(_.Unsigned('Number_Combination_Ensembles_1_none', 2))
    h.add(_.Unsigned('Show_Combination_Ensem_E2_0_no_1_yes', 1))
    h.add(_.Unsigned('Show_Combination_Ensem_E3_0_no_1_yes', 1))
    h.add(_.Unsigned('Show_Combination_Ensem_E4_0_no_1_yes', 1))
    h.add(_.Pad('padding_loc244_2', 7))
    h.add(_.Unsigned('Total_Number_Members_Used', 2))
    h.add(_.Unsigned('Total_Number_Members_Possible', 2))
    h.add(_.Unsigned('Total_Number_Members_Missing', 2))
    h.add(_.Unsigned('Ensemble_Combination_Number', 2))
    h.add(_.Ascii('Ensemble_Identifier', 8))
    h.add(_.Unsigned('Local_Number_Members_Used', 2))
    h.add(_.Unsigned('Local_Number_Members_Possible', 2))
    h.add(_.Unsigned('Local_Number_Members_Missing', 2))

    with h.list('listMembersUsed'):
        for i in range(0, h.get_l('Local_Number_Members_Used')):
            h.add(_.Ascii('Used_Model_LBC', 4))

    with h.list('listMembersMissing'):
        for i in range(0, h.get_l('Local_Number_Members_Missing')):
            h.add(_.Ascii('Missing_Model_LBC', 4))

    if (h.get_l('Show_Combination_Ensem_E2_0_no_1_yes') == 1):
        h.add(_.Unsigned('Ensemble_Combinat_Number_0_none_E2', 2))
        h.add(_.Ascii('Ensemble_Identifier_E2', 8))
        h.add(_.Unsigned('Local_Number_Members_Used_E2', 2))
        h.add(_.Unsigned('Local_Number_Members_Possible_E2', 2))
        h.add(_.Unsigned('Local_Number_Members_Missing_E2', 2))
        h.add(_.Unsigned('Date_E2', 3))
        h.add(_.Unsigned('Hour_E2', 1))
        h.add(_.Unsigned('Minute_E2', 1))
        h.add(_.Unsigned('Time_Range_One_E2', 2))
        h.add(_.Unsigned('Time_Range_Two_E2', 2))

        with h.list('listMembersUsed2'):
            for i in range(0, h.get_l('Local_Number_Members_Used_E2')):
                h.add(_.Ascii('Used_Model_LBC_E2', 4))

        with h.list('listMembersMissing2'):
            for i in range(0, h.get_l('Local_Number_Members_Missing_E2')):
                h.add(_.Ascii('Missing_Model_LBC_E2', 4))

    if (h.get_l('Show_Combination_Ensem_E3_0_no_1_yes') == 1):
        h.add(_.Unsigned('Ensemble_Combinat_Number_0_none_E3', 2))
        h.add(_.Ascii('Ensemble_Identifier_E3', 8))
        h.add(_.Unsigned('Local_Number_Members_Used_E3', 2))
        h.add(_.Unsigned('Local_Number_Members_Possible_E3', 2))
        h.add(_.Unsigned('Local_Number_Members_Missing_E3', 2))
        h.add(_.Unsigned('Date_E3', 3))
        h.add(_.Unsigned('Hour_E3', 1))
        h.add(_.Unsigned('Minute_E3', 1))
        h.add(_.Unsigned('Time_Range_One_E3', 2))
        h.add(_.Unsigned('Time_Range_Two_E3', 2))

        with h.list('listMembersUsed3'):
            for i in range(0, h.get_l('Local_Number_Members_Used_E3')):
                h.add(_.Ascii('Used_Model_LBC_E3', 4))

        with h.list('listMembersMissing3'):
            for i in range(0, h.get_l('Local_Number_Members_Missing_E3')):
                h.add(_.Ascii('Missing_Model_LBC_E3', 4))

    if (h.get_l('Show_Combination_Ensem_E4_0_no_1_yes') == 1):
        h.add(_.Unsigned('Ensemble_Combinat_Number_0_none_E4', 2))
        h.add(_.Ascii('Ensemble_Identifier_E4', 8))
        h.add(_.Unsigned('Local_Number_Members_Used_E4', 2))
        h.add(_.Unsigned('Local_Number_Members_Possible_E4', 2))
        h.add(_.Unsigned('Local_Number_Members_Missing_E4', 2))
        h.add(_.Unsigned('Date_E4', 3))
        h.add(_.Unsigned('Hour_E4', 1))
        h.add(_.Unsigned('Minute_E4', 1))
        h.add(_.Unsigned('Time_Range_One_E4', 2))
        h.add(_.Unsigned('Time_Range_Two_E4', 2))

        with h.list('listMembersUsed4'):
            for i in range(0, h.get_l('Local_Number_Members_Used_E4')):
                h.add(_.Ascii('Used_Model_LBC_E4', 4))

        with h.list('listMembersMissing4'):
            for i in range(0, h.get_l('Local_Number_Members_Missing_E4')):
                h.add(_.Ascii('Missing_Model_LBC_E4', 4))

    h.add(_.Ascii('*********_EXTRA_DATA_***************', 4))
    h.add(_.Unsigned('Extra_Data_FreeFormat_0_none', 2))
    h.add(_.Position('offsetFreeFormData'))
    h.add(_.Unsigned('freeFormData', 1, _.Get('Extra_Data_FreeFormat_0_none')))
    h.add(_.Padtomultiple('padding_loc244_3', _.Get('offsetSection1'), 80))
