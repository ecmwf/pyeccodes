def load(h):
    return ({'abbr': 'Active', 'code': 1, 'title': 'Active data'},
            {'abbr': 'All', 'code': 2, 'title': 'All data'},
            {'abbr': 'Non_Active', 'code': 3, 'title': 'Not Active data'},
            {'abbr': 'Best_Active', 'code': 4, 'title': 'Best active wind'},
            {'abbr': 'Used', 'code': 5, 'title': 'Used data'},
            {'abbr': 'VarQC_Rej', 'code': 6, 'title': 'VarQC rejected data'},
            {'abbr': 'Blacklisted', 'code': 7, 'title': 'Blacklisted data'},
            {'abbr': 'Failed', 'code': 8, 'title': 'Failed data'},
            {'abbr': 'Passed_FgCheck', 'code': 9, 'title': 'Data that passed FG check'},
            {'abbr': 'Non_Rejected', 'code': 10, 'title': 'All non rejected data'},
            {'abbr': 'VarBC_Passive', 'code': 11, 'title': 'VarBC passive channels'},
            {'abbr': 'Failed_FG_Non_Black',
             'code': 12,
             'title': 'Data failed FG check but not blacklisted'},
            {'abbr': 'Failed_FG_VarQC_Rej',
             'code': 13,
             'title': 'Data failed FG check and VARQC rejected'},
            {'abbr': 'QI_LE_20', 'code': 20, 'title': 'AMVs with QI <= 20'},
            {'abbr': 'QI_LE_66', 'code': 21, 'title': 'AMVs with 20 < QI <=65'},
            {'abbr': 'QI_GE_65', 'code': 22, 'title': 'AMVs with QI > 65'},
            {'abbr': 'QI_GE_80', 'code': 23, 'title': 'AMVs with QI > 80'},
            {'abbr': 'QI_GE_90', 'code': 24, 'title': 'AMVs with QI > 90'},
            {'abbr': 'Clear_LE_70%WV_80%IR',
             'code': 30,
             'title': 'CSR data with clear fraction < 70 % (WV) and < 80 %',
             'units': 'IR'},
            {'abbr': 'Clear_GE_70%WV_80%IR',
             'code': 31,
             'title': 'CSR data with clear fraction >= 70 % (WV) and >= 80 %',
             'units': 'IR'},
            {'abbr': 'Clear_100%',
             'code': 32,
             'title': 'CSR data completely clear',
             'units': 'according to IR window channel'},
            {'abbr': 'Clear_GE_40%WV',
             'code': 33,
             'title': 'CSR data with clear fraction >= 40 %',
             'units': 'WV'},
            {'abbr': 'Clear_GE_70%WV',
             'code': 34,
             'title': 'CSR data with clear fraction >= 70 %',
             'units': 'WV'},
            {'abbr': 'Clear_100%WV',
             'code': 35,
             'title': 'CSR data completely clear',
             'units': 'according to WV channel'},
            {'abbr': 'Clear', 'code': 40, 'title': 'Clear'},
            {'abbr': 'Used_Clear', 'code': 41, 'title': 'Used clear data'},
            {'abbr': 'Used_Cloudy_Rainy',
             'code': 42,
             'title': 'Used cloudy and rainy data'},
            {'abbr': 'All_Cloudy_Rainy', 'code': 43, 'title': 'All cloudy and rainy data'},
            {'abbr': 'Used_ObsCld_FGClr',
             'code': 44,
             'title': 'Used Obs cloudy and FG clear'},
            {'abbr': 'Used_ObsClr_FGCld',
             'code': 45,
             'title': 'Used Obs clear and FG cloudy'},
            {'abbr': 'Good_ozone', 'code': 50, 'title': 'Good ozone data'},
            {'abbr': 'Daytime', 'code': 51, 'title': 'Day time data'},
            {'abbr': 'Nighttime', 'code': 52, 'title': 'Night time data'})
