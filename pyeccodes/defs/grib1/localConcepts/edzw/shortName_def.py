import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 202 and indicatorOfParameter == 39:
            return 'SKC'

        if table2Version == 202 and indicatorOfParameter == 37:
            return 'ECHOTOPinM'

        if table2Version == 202 and indicatorOfParameter == 36:
            return 'ECHOTOP'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 'RELV'

        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200 and timeRangeIndicator == 2:
            return 'DBZ_CTMAX'

        if table2Version == 201 and indicatorOfParameter == 196 and timeRangeIndicator == 2:
            return 'LPI_MAX'

        if table2Version == 201 and indicatorOfParameter == 234:
            return 'DBZCMP_SIM'

        if table2Version == 201 and indicatorOfParameter == 235:
            return 'DBZCMP_OBS'

        if table2Version == 201 and indicatorOfParameter == 48 and indicatorOfTypeOfLevel == 200 and timeRangeIndicator == 2:
            return 'TCOND_MAX'

        if table2Version == 201 and indicatorOfParameter == 49 and timeRangeIndicator == 2:
            return 'TCOND10_MX'

        if table2Version == 203 and indicatorOfParameter == 37 and timeRangeIndicator == 2:
            return 'W_CTMAX'

        if table2Version == 203 and indicatorOfParameter == 36 and timeRangeIndicator == 2:
            return 'VORW_CTMAX'

        if table2Version == 203 and indicatorOfParameter == 35 and timeRangeIndicator == 2:
            return 'UH_MAX'

        if table2Version == 201 and indicatorOfParameter == 196:
            return 'LPI'

        if table2Version == 202 and indicatorOfParameter == 34:
            return 'AHF'

        if table2Version == 202 and indicatorOfParameter == 33:
            return 'FR_PAVED'

        if table2Version == 201 and indicatorOfParameter == 196:
            return 'LPI'

        if table2Version == 3 and indicatorOfParameter == 149:
            return 'GUST_10M_UK'

        if table2Version == 3 and indicatorOfParameter == 148:
            return 'ORO_UK'

        if table2Version == 201 and indicatorOfParameter == 25 and timeRangeIndicator == 4:
            return 'ACCTHD_S'

        if table2Version == 201 and indicatorOfParameter == 25 and timeRangeIndicator == 3:
            return 'ATHD_S'

        if table2Version == 201 and indicatorOfParameter == 25:
            return 'THDS_RAD'

        if table2Version == 3 and indicatorOfParameter == 162:
            return 'FL_E'

        if table2Version == 3 and indicatorOfParameter == 152:
            return 'WBFL_E'

        if table2Version == 3 and indicatorOfParameter == 151:
            return 'CEILING_E'

        if table2Version == 3 and indicatorOfParameter == 207:
            return 'CFRAC'

        if table2Version == 3 and indicatorOfParameter == 140:
            return 'PREC_CON_E'

        if table2Version == 3 and indicatorOfParameter == 138:
            return 'FOGFRAC_E'

        if table2Version == 3 and indicatorOfParameter == 40:
            return 'W'

        if table2Version == 202 and indicatorOfParameter == 120:
            return 'USTR'

        if table2Version == 250 and indicatorOfParameter == 20:
            return 'RH_MIX_EC'

        if table2Version == 202 and indicatorOfParameter == 233 and timeRangeIndicator == 3:
            return 'AVDIS_SSO'

        if table2Version == 204 and indicatorOfParameter == 46:
            return 'RADAR_FQ'

        if table2Version == 203 and indicatorOfParameter == 77:
            return 'RADAR_FS'

        if table2Version == 203 and indicatorOfParameter == 76:
            return 'RADAR_RH'

        if table2Version == 203 and indicatorOfParameter == 75:
            return 'RADAR_RE'

        if table2Version == 203 and indicatorOfParameter == 73:
            return 'RADAR_RS'

        if table2Version == 203 and indicatorOfParameter == 72:
            return 'RADAR_RQ'

        if table2Version == 202 and indicatorOfParameter == 232 and timeRangeIndicator == 1:
            return 'AVSTR_SSO'

        if table2Version == 202 and indicatorOfParameter == 231 and timeRangeIndicator == 1:
            return 'AUSTR_SSO'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1:
            return 'VMFL_S'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1:
            return 'UMFL_S'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1:
            return 'SWDIFUS_RAD'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1:
            return 'SWDIFDS_RAD'

        if table2Version == 201 and indicatorOfParameter == 151:
            return 'EDR'

        if table2Version == 203 and indicatorOfParameter == 71:
            return 'PREC'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'STRF'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'VPOT'

        if table2Version == 3 and indicatorOfParameter == 98:
            return 'ICED'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 'ICED'

        if table2Version == 2 and indicatorOfParameter == 98:
            return 'ICED'

        if table2Version == 2 and indicatorOfParameter == 13:
            return 'PT'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'TOT_PREC'

        if table2Version == 1 and indicatorOfParameter == 71:
            return 'CLCT'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'W_SNOW'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'H_SNOW'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'T_S'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'W_CL'

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'OROG'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 'IMGD'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'WMIXE'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'AVMFL_S'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'AUMFL_S'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'SWRAD'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'LWRAD'

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'GRAD'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'SWAVR'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'LWAVR'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'NLWRT'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'ASOB_T'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'ATHB_S'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'ASOB_S'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 'SWP'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'DIRSW'

        if table2Version == 1 and indicatorOfParameter == 106:
            return 'MPTS'

        if table2Version == 1 and indicatorOfParameter == 105:
            return 'SHTS'

        if table2Version == 1 and indicatorOfParameter == 104:
            return 'MDTS'

        if table2Version == 1 and indicatorOfParameter == 103:
            return 'MPWW'

        if table2Version == 1 and indicatorOfParameter == 102:
            return 'SHWW'

        if table2Version == 1 and indicatorOfParameter == 101:
            return 'MDWW'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'SWH'

        if table2Version == 1 and indicatorOfParameter == 97:
            return 'ICEG'

        if table2Version == 1 and indicatorOfParameter == 96:
            return 'VICED'

        if table2Version == 1 and indicatorOfParameter == 95:
            return 'UICE'

        if table2Version == 1 and indicatorOfParameter == 94:
            return 'SICED'

        if table2Version == 1 and indicatorOfParameter == 93:
            return 'DICED'

        if table2Version == 1 and indicatorOfParameter == 92:
            return 'H_ICE'

        if table2Version == 1 and indicatorOfParameter == 91:
            return 'FR_ICE'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'DEN'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 'S'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'W_CL'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'DSLM'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'T_SEA'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'BLI'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'MTHA'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'MTHD'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'TTHDP'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'MLD'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'SRWEQ'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'ACPCP'

        if table2Version == 1 and indicatorOfParameter == 60:
            return 'TSTM'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'PRATE'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'SATD'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'VP'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'TQV'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'MIXR'

        if table2Version == 1 and indicatorOfParameter == 50:
            return 'VCURR'

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'UCURR'

        if table2Version == 1 and indicatorOfParameter == 48:
            return 'SPC'

        if table2Version == 1 and indicatorOfParameter == 47:
            return 'DIRC'

        if table2Version == 1 and indicatorOfParameter == 46:
            return 'VVCSH'

        if table2Version == 1 and indicatorOfParameter == 45:
            return 'VUCSH'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 'ABSD'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 'ABSV'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 'SGCVV'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'MNTSF'

        if table2Version == 1 and indicatorOfParameter == 31:
            return 'DD'

        if table2Version == 1 and indicatorOfParameter == 30:
            return 'WVSP3'

        if table2Version == 1 and indicatorOfParameter == 29:
            return 'WVSP2'

        if table2Version == 1 and indicatorOfParameter == 28:
            return 'WVSP1'

        if table2Version == 1 and indicatorOfParameter == 27:
            return 'GPA'

        if table2Version == 1 and indicatorOfParameter == 26:
            return 'PRESA'

        if table2Version == 1 and indicatorOfParameter == 25:
            return 'TA'

        if table2Version == 1 and indicatorOfParameter == 24:
            return 'PLI'

        if table2Version == 1 and indicatorOfParameter == 23:
            return 'RDSP3'

        if table2Version == 1 and indicatorOfParameter == 22:
            return 'RDSP2'

        if table2Version == 1 and indicatorOfParameter == 21:
            return 'DBZ_MAX'

        if table2Version == 1 and indicatorOfParameter == 20:
            return 'VIS'

        if table2Version == 1 and indicatorOfParameter == 19:
            return 'LAPSE_RATE'

        if table2Version == 1 and indicatorOfParameter == 18:
            return 'DEPR'

        if table2Version == 1 and indicatorOfParameter == 17:
            return 'TD'

        if table2Version == 1 and indicatorOfParameter == 16:
            return 'TMIN'

        if table2Version == 1 and indicatorOfParameter == 15:
            return 'TMAX'

        if table2Version == 1 and indicatorOfParameter == 14:
            return 'PAPT'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'HSTDV'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'HSURF'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'ICAHT'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'DPSDT'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'TQC'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'PREC_GSP'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'SNOW_GSP'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'SNOW_CON'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'TO3'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'RUNOFF'

        if table2Version == 1 and indicatorOfParameter == 87:
            return 'PLCOV'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'BTMP'

        if table2Version == 1 and indicatorOfParameter == 75:
            return 'CLCH'

        if table2Version == 1 and indicatorOfParameter == 74:
            return 'CLCM'

        if table2Version == 1 and indicatorOfParameter == 73:
            return 'CLCL'

        if table2Version == 1 and indicatorOfParameter == 72:
            return 'CLC_CON'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'AEVAP_S'

        if table2Version == 1 and indicatorOfParameter == 84:
            return 'ALBEDO_B'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'Z0'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'FR_LAND'

        if table2Version == 1 and indicatorOfParameter == 44:
            return 'RDIV'

        level = h.get_l('level')

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'T_2M'

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'V_10M'

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'U_10M'

        if table2Version == 1 and indicatorOfParameter == 52:
            return 'RELHUM'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'GH'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'PMSL'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'ALHFL_S'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'ASHFL_S'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'BLD'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 'VORTIC_W'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'OMEGA'

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'PS'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'QV'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'V'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'U'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 'T'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'FIS'

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'TMIN_2M'

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'TMAX_2M'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'P'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'SP'

        if table2Version == 3 and indicatorOfParameter == 13:
            return 'PT'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'PT'

        if table2Version == 2 and indicatorOfParameter == 85:
            return 'T_S'

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'OROG'

        if table2Version == 2 and indicatorOfParameter == 127:
            return 'IMGD'

        if table2Version == 2 and indicatorOfParameter == 126:
            return 'WMIXE'

        if table2Version == 2 and indicatorOfParameter == 125:
            return 'AVMFL_S'

        if table2Version == 2 and indicatorOfParameter == 124:
            return 'AUMFL_S'

        if table2Version == 2 and indicatorOfParameter == 120:
            return 'SWRAD'

        if table2Version == 2 and indicatorOfParameter == 119:
            return 'LWRAD'

        if table2Version == 2 and indicatorOfParameter == 116:
            return 'SWAVR'

        if table2Version == 2 and indicatorOfParameter == 115:
            return 'LWAVR'

        if table2Version == 2 and indicatorOfParameter == 114:
            return 'NLWRT'

        if table2Version == 2 and indicatorOfParameter == 113:
            return 'ASOB_T'

        if table2Version == 2 and indicatorOfParameter == 112:
            return 'ATHB_S'

        if table2Version == 2 and indicatorOfParameter == 111:
            return 'ASOB_S'

        if table2Version == 2 and indicatorOfParameter == 110:
            return 'SWP'

        if table2Version == 2 and indicatorOfParameter == 109:
            return 'DIRSW'

        if table2Version == 2 and indicatorOfParameter == 99:
            return 'SNOW'

        if table2Version == 2 and indicatorOfParameter == 97:
            return 'ICEG'

        if table2Version == 2 and indicatorOfParameter == 96:
            return 'VICED'

        if table2Version == 2 and indicatorOfParameter == 95:
            return 'UICE'

        if table2Version == 2 and indicatorOfParameter == 94:
            return 'SICED'

        if table2Version == 2 and indicatorOfParameter == 93:
            return 'DICED'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'W_CL'

        if table2Version == 2 and indicatorOfParameter == 82:
            return 'DSLM'

        if table2Version == 2 and indicatorOfParameter == 77:
            return 'BLI'

        if table2Version == 2 and indicatorOfParameter == 70:
            return 'MTHA'

        if table2Version == 2 and indicatorOfParameter == 69:
            return 'MTHD'

        if table2Version == 2 and indicatorOfParameter == 68:
            return 'TTHDP'

        if table2Version == 2 and indicatorOfParameter == 67:
            return 'MLD'

        if table2Version == 2 and indicatorOfParameter == 64:
            return 'SRWEQ'

        if table2Version == 2 and indicatorOfParameter == 63:
            return 'ACPCP'

        if table2Version == 2 and indicatorOfParameter == 60:
            return 'TSTM'

        if table2Version == 2 and indicatorOfParameter == 59:
            return 'PRATE'

        if table2Version == 2 and indicatorOfParameter == 56:
            return 'SATD'

        if table2Version == 2 and indicatorOfParameter == 55:
            return 'VP'

        if table2Version == 2 and indicatorOfParameter == 53:
            return 'MIXR'

        if table2Version == 2 and indicatorOfParameter == 50:
            return 'VCURR'

        if table2Version == 2 and indicatorOfParameter == 49:
            return 'UCURR'

        if table2Version == 2 and indicatorOfParameter == 48:
            return 'SPC'

        if table2Version == 2 and indicatorOfParameter == 47:
            return 'DIRC'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 'VVCSH'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 'VUCSH'

        if table2Version == 2 and indicatorOfParameter == 42:
            return 'ABSD'

        if table2Version == 2 and indicatorOfParameter == 38:
            return 'SGCVV'

        if table2Version == 3 and indicatorOfParameter == 37:
            return 'MNTSF'

        if table2Version == 2 and indicatorOfParameter == 37:
            return 'MNTSF'

        if table2Version == 2 and indicatorOfParameter == 27:
            return 'GPA'

        if table2Version == 2 and indicatorOfParameter == 26:
            return 'PRESA'

        if table2Version == 2 and indicatorOfParameter == 25:
            return 'TA'

        if table2Version == 2 and indicatorOfParameter == 24:
            return 'PLI'

        if table2Version == 2 and indicatorOfParameter == 23:
            return 'RDSP3'

        if table2Version == 2 and indicatorOfParameter == 22:
            return 'RDSP2'

        if table2Version == 2 and indicatorOfParameter == 20:
            return 'VIS'

        if table2Version == 2 and indicatorOfParameter == 18:
            return 'DEPR'

        if table2Version == 2 and indicatorOfParameter == 17:
            return 'TD'

        if table2Version == 2 and indicatorOfParameter == 16:
            return 'TMIN'

        if table2Version == 2 and indicatorOfParameter == 15:
            return 'TMAX'

        if table2Version == 3 and indicatorOfParameter == 14:
            return 'PAPT'

        if table2Version == 2 and indicatorOfParameter == 14:
            return 'PAPT'

        if table2Version == 3 and indicatorOfParameter == 9:
            return 'HSTDV'

        if table2Version == 2 and indicatorOfParameter == 9:
            return 'HSTDV'

        if table2Version == 2 and indicatorOfParameter == 8:
            return 'HSURF'

        if table2Version == 2 and indicatorOfParameter == 90:
            return 'RUNOFF'

        if table2Version == 2 and indicatorOfParameter == 118:
            return 'BTMP'

        if table2Version == 2 and indicatorOfParameter == 75:
            return 'CLCH'

        if table2Version == 2 and indicatorOfParameter == 74:
            return 'CLCM'

        if table2Version == 2 and indicatorOfParameter == 73:
            return 'CLCL'

        if table2Version == 2 and indicatorOfParameter == 57:
            return 'AEVAP_S'

        if table2Version == 2 and indicatorOfParameter == 121:
            return 'ALHFL_S'

        if table2Version == 2 and indicatorOfParameter == 122:
            return 'ASHFL_S'

        if table2Version == 2 and indicatorOfParameter == 123:
            return 'BLD'

        if table2Version == 3 and indicatorOfParameter == 61:
            return 'TOT_PREC'

        if table2Version == 3 and indicatorOfParameter == 71:
            return 'CLCT'

        if table2Version == 3 and indicatorOfParameter == 65:
            return 'W_SNOW'

        if table2Version == 3 and indicatorOfParameter == 66:
            return 'H_SNOW'

        if table2Version == 3 and indicatorOfParameter == 85:
            return 'T_S'

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'OROG'

        if table2Version == 3 and indicatorOfParameter == 127:
            return 'IMGD'

        if table2Version == 3 and indicatorOfParameter == 126:
            return 'WMIXE'

        if table2Version == 3 and indicatorOfParameter == 125:
            return 'AVMFL_S'

        if table2Version == 3 and indicatorOfParameter == 124:
            return 'AUMFL_S'

        if table2Version == 3 and indicatorOfParameter == 120:
            return 'SWRAD'

        if table2Version == 3 and indicatorOfParameter == 119:
            return 'LWRAD'

        if table2Version == 3 and indicatorOfParameter == 117:
            return 'GRAD'

        if table2Version == 3 and indicatorOfParameter == 116:
            return 'SWAVR'

        if table2Version == 3 and indicatorOfParameter == 115:
            return 'LWAVR'

        if table2Version == 3 and indicatorOfParameter == 114:
            return 'NLWRT'

        if table2Version == 3 and indicatorOfParameter == 113:
            return 'ASOB_T'

        if table2Version == 3 and indicatorOfParameter == 112:
            return 'ATHB_S'

        if table2Version == 3 and indicatorOfParameter == 111:
            return 'ASOB_S'

        if table2Version == 3 and indicatorOfParameter == 110:
            return 'SWP'

        if table2Version == 3 and indicatorOfParameter == 109:
            return 'DIRSW'

        if table2Version == 3 and indicatorOfParameter == 106:
            return 'MPTS'

        if table2Version == 3 and indicatorOfParameter == 105:
            return 'SHTS'

        if table2Version == 3 and indicatorOfParameter == 104:
            return 'MDTS'

        if table2Version == 3 and indicatorOfParameter == 103:
            return 'MPWW'

        if table2Version == 3 and indicatorOfParameter == 102:
            return 'SHWW'

        if table2Version == 3 and indicatorOfParameter == 101:
            return 'MDWW'

        if table2Version == 3 and indicatorOfParameter == 100:
            return 'SWH'

        if table2Version == 3 and indicatorOfParameter == 99:
            return 'SNOM'

        if table2Version == 3 and indicatorOfParameter == 97:
            return 'ICEG'

        if table2Version == 3 and indicatorOfParameter == 96:
            return 'VICED'

        if table2Version == 3 and indicatorOfParameter == 95:
            return 'UICE'

        if table2Version == 3 and indicatorOfParameter == 94:
            return 'SICED'

        if table2Version == 3 and indicatorOfParameter == 93:
            return 'DICED'

        if table2Version == 3 and indicatorOfParameter == 92:
            return 'H_ICE'

        if table2Version == 3 and indicatorOfParameter == 91:
            return 'FR_ICE'

        if table2Version == 3 and indicatorOfParameter == 89:
            return 'DEN'

        if table2Version == 3 and indicatorOfParameter == 88:
            return 'S'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'W_CL'

        if table2Version == 3 and indicatorOfParameter == 82:
            return 'DSLM'

        if table2Version == 3 and indicatorOfParameter == 80:
            return 'T_SEA'

        if table2Version == 3 and indicatorOfParameter == 77:
            return 'BLI'

        if table2Version == 3 and indicatorOfParameter == 70:
            return 'MTHA'

        if table2Version == 3 and indicatorOfParameter == 69:
            return 'MTHD'

        if table2Version == 3 and indicatorOfParameter == 68:
            return 'TTHDP'

        if table2Version == 3 and indicatorOfParameter == 67:
            return 'MLD'

        if table2Version == 3 and indicatorOfParameter == 64:
            return 'SRWEQ'

        if table2Version == 3 and indicatorOfParameter == 63:
            return 'ACPCP'

        if table2Version == 3 and indicatorOfParameter == 60:
            return 'TSTM'

        if table2Version == 3 and indicatorOfParameter == 59:
            return 'PRATE'

        if table2Version == 3 and indicatorOfParameter == 56:
            return 'SATD'

        if table2Version == 3 and indicatorOfParameter == 55:
            return 'VP'

        if table2Version == 3 and indicatorOfParameter == 54:
            return 'TQV'

        if table2Version == 3 and indicatorOfParameter == 53:
            return 'MIXR'

        if table2Version == 3 and indicatorOfParameter == 50:
            return 'VCURR'

        if table2Version == 3 and indicatorOfParameter == 49:
            return 'UCURR'

        if table2Version == 3 and indicatorOfParameter == 48:
            return 'SPC'

        if table2Version == 3 and indicatorOfParameter == 47:
            return 'DIRC'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 'VVCSH'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 'VUCSH'

        if table2Version == 3 and indicatorOfParameter == 42:
            return 'ABSD'

        if table2Version == 3 and indicatorOfParameter == 41:
            return 'ABSV'

        if table2Version == 3 and indicatorOfParameter == 38:
            return 'SGCVV'

        if table2Version == 3 and indicatorOfParameter == 31:
            return 'DD'

        if table2Version == 3 and indicatorOfParameter == 30:
            return 'WVSP3'

        if table2Version == 3 and indicatorOfParameter == 29:
            return 'WVSP2'

        if table2Version == 3 and indicatorOfParameter == 28:
            return 'WVSP1'

        if table2Version == 3 and indicatorOfParameter == 27:
            return 'GPA'

        if table2Version == 3 and indicatorOfParameter == 26:
            return 'PRESA'

        if table2Version == 3 and indicatorOfParameter == 25:
            return 'TA'

        if table2Version == 3 and indicatorOfParameter == 24:
            return 'PLI'

        if table2Version == 3 and indicatorOfParameter == 23:
            return 'RDSP3'

        if table2Version == 3 and indicatorOfParameter == 22:
            return 'RDSP2'

        if table2Version == 3 and indicatorOfParameter == 21:
            return 'DBZ_MAX'

        if table2Version == 3 and indicatorOfParameter == 20:
            return 'VIS'

        if table2Version == 3 and indicatorOfParameter == 19:
            return 'LAPSE_RATE'

        if table2Version == 3 and indicatorOfParameter == 18:
            return 'DEPR'

        if table2Version == 3 and indicatorOfParameter == 17:
            return 'TD'

        if table2Version == 3 and indicatorOfParameter == 16:
            return 'TMIN'

        if table2Version == 3 and indicatorOfParameter == 15:
            return 'TMAX'

        if table2Version == 3 and indicatorOfParameter == 8:
            return 'HSURF'

        if table2Version == 3 and indicatorOfParameter == 5:
            return 'ICAHT'

        if table2Version == 3 and indicatorOfParameter == 3:
            return 'DPSDT'

        if table2Version == 3 and indicatorOfParameter == 123:
            return 'BLD'

        if table2Version == 3 and indicatorOfParameter == 118:
            return 'BTMP'

        if table2Version == 3 and indicatorOfParameter == 12:
            return 'VTMP'

        if table2Version == 2 and indicatorOfParameter == 12:
            return 'VTMP'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'VTMP'

        if table2Version == 3 and indicatorOfParameter == 76:
            return 'TQC'

        if table2Version == 3 and indicatorOfParameter == 62:
            return 'PREC_GSP'

        if table2Version == 3 and indicatorOfParameter == 79:
            return 'SNOW_GSP'

        if table2Version == 3 and indicatorOfParameter == 78:
            return 'SNOW_CON'

        if table2Version == 3 and indicatorOfParameter == 10:
            return 'TO3'

        if table2Version == 3 and indicatorOfParameter == 90:
            return 'RUNOFF'

        if table2Version == 3 and indicatorOfParameter == 87:
            return 'PLCOV'

        if table2Version == 3 and indicatorOfParameter == 75:
            return 'CLCH'

        if table2Version == 3 and indicatorOfParameter == 74:
            return 'CLCM'

        if table2Version == 3 and indicatorOfParameter == 73:
            return 'CLCL'

        if table2Version == 3 and indicatorOfParameter == 72:
            return 'CLC_CON'

        if table2Version == 3 and indicatorOfParameter == 57:
            return 'AEVAP_S'

        if table2Version == 3 and indicatorOfParameter == 84:
            return 'ALBEDO_B'

        if table2Version == 3 and indicatorOfParameter == 83:
            return 'Z0'

        if table2Version == 3 and indicatorOfParameter == 81:
            return 'FR_LAND'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'T_2M'

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'V_10M'

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'U_10M'

        if table2Version == 3 and indicatorOfParameter == 52:
            return 'RELHUM'

        if table2Version == 3 and indicatorOfParameter == 7:
            return 'GH'

        if table2Version == 3 and indicatorOfParameter == 44:
            return 'RDIV'

        if table2Version == 3 and indicatorOfParameter == 2:
            return 'PMSL'

        if table2Version == 3 and indicatorOfParameter == 121:
            return 'ALHFL_S'

        if table2Version == 3 and indicatorOfParameter == 122:
            return 'ASHFL_S'

        if table2Version == 3 and indicatorOfParameter == 43:
            return 'VORTIC_W'

        if table2Version == 3 and indicatorOfParameter == 39:
            return 'OMEGA'

        if table2Version == 3 and indicatorOfParameter == 51:
            return 'QV'

        if table2Version == 3 and indicatorOfParameter == 34:
            return 'V'

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'PS'

        if table2Version == 3 and indicatorOfParameter == 33:
            return 'U'

        if table2Version == 3 and indicatorOfParameter == 11:
            return 'T'

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'TMIN_2M'

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'TMAX_2M'

        if table2Version == 3 and indicatorOfParameter == 6:
            return 'FIS'

        if table2Version == 3 and indicatorOfParameter == 4:
            return 'POT_VORTIC'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'POT_VORTIC'

        if table2Version == 3 and indicatorOfParameter == 1:
            return 'P'

        if table2Version == 3 and indicatorOfParameter == 32:
            return 'SP'

        if table2Version == 3 and indicatorOfParameter == 36:
            return 'VPOT'

        if table2Version == 3 and indicatorOfParameter == 35:
            return 'STRF'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 'T_G'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1:
            return 'SWDIRS_RAD'

        if table2Version == 202 and indicatorOfParameter == 38:
            return 'SKT'

        if table2Version == 2 and indicatorOfParameter == 36:
            return 'VPOT'

        if table2Version == 2 and indicatorOfParameter == 35:
            return 'STRF'

        if table2Version == 2 and indicatorOfParameter == 88:
            return 'SALT_LK'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 'SHFL_S'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1:
            return 'LHFL_S'

        if table2Version == 202 and indicatorOfParameter == 129:
            return 'ALB_DIF'

        if table2Version == 202 and indicatorOfParameter == 129 and timeRangeIndicator == 3:
            return 'ALB_DIF12'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 1:
            return 'QV_S'

        if table2Version == 254 and indicatorOfParameter == 254:
            return 'DUMMY_254'

        if table2Version == 254 and indicatorOfParameter == 253:
            return 'DUMMY_253'

        if table2Version == 254 and indicatorOfParameter == 252:
            return 'DUMMY_252'

        if table2Version == 254 and indicatorOfParameter == 251:
            return 'DUMMY_251'

        if table2Version == 254 and indicatorOfParameter == 250:
            return 'DUMMY_250'

        if table2Version == 254 and indicatorOfParameter == 249:
            return 'DUMMY_249'

        if table2Version == 254 and indicatorOfParameter == 248:
            return 'DUMMY_248'

        if table2Version == 254 and indicatorOfParameter == 247:
            return 'DUMMY_247'

        if table2Version == 254 and indicatorOfParameter == 246:
            return 'DUMMY_246'

        if table2Version == 254 and indicatorOfParameter == 245:
            return 'DUMMY_245'

        if table2Version == 254 and indicatorOfParameter == 244:
            return 'DUMMY_244'

        if table2Version == 254 and indicatorOfParameter == 243:
            return 'DUMMY_243'

        if table2Version == 254 and indicatorOfParameter == 242:
            return 'DUMMY_242'

        if table2Version == 254 and indicatorOfParameter == 241:
            return 'DUMMY_241'

        if table2Version == 254 and indicatorOfParameter == 240:
            return 'DUMMY_240'

        if table2Version == 254 and indicatorOfParameter == 239:
            return 'DUMMY_239'

        if table2Version == 254 and indicatorOfParameter == 238:
            return 'DUMMY_238'

        if table2Version == 254 and indicatorOfParameter == 237:
            return 'DUMMY_237'

        if table2Version == 254 and indicatorOfParameter == 236:
            return 'DUMMY_236'

        if table2Version == 254 and indicatorOfParameter == 235:
            return 'DUMMY_235'

        if table2Version == 254 and indicatorOfParameter == 234:
            return 'DUMMY_234'

        if table2Version == 254 and indicatorOfParameter == 233:
            return 'DUMMY_233'

        if table2Version == 254 and indicatorOfParameter == 232:
            return 'DUMMY_232'

        if table2Version == 254 and indicatorOfParameter == 231:
            return 'DUMMY_231'

        if table2Version == 254 and indicatorOfParameter == 230:
            return 'DUMMY_230'

        if table2Version == 254 and indicatorOfParameter == 229:
            return 'DUMMY_229'

        if table2Version == 254 and indicatorOfParameter == 228:
            return 'DUMMY_228'

        if table2Version == 254 and indicatorOfParameter == 227:
            return 'DUMMY_227'

        if table2Version == 254 and indicatorOfParameter == 226:
            return 'DUMMY_226'

        if table2Version == 254 and indicatorOfParameter == 225:
            return 'DUMMY_225'

        if table2Version == 254 and indicatorOfParameter == 224:
            return 'DUMMY_224'

        if table2Version == 254 and indicatorOfParameter == 223:
            return 'DUMMY_223'

        if table2Version == 254 and indicatorOfParameter == 222:
            return 'DUMMY_222'

        if table2Version == 254 and indicatorOfParameter == 221:
            return 'DUMMY_221'

        if table2Version == 254 and indicatorOfParameter == 220:
            return 'DUMMY_220'

        if table2Version == 254 and indicatorOfParameter == 219:
            return 'DUMMY_219'

        if table2Version == 254 and indicatorOfParameter == 218:
            return 'DUMMY_218'

        if table2Version == 254 and indicatorOfParameter == 217:
            return 'DUMMY_217'

        if table2Version == 254 and indicatorOfParameter == 216:
            return 'DUMMY_216'

        if table2Version == 254 and indicatorOfParameter == 215:
            return 'DUMMY_215'

        if table2Version == 254 and indicatorOfParameter == 214:
            return 'DUMMY_214'

        if table2Version == 254 and indicatorOfParameter == 213:
            return 'DUMMY_213'

        if table2Version == 254 and indicatorOfParameter == 212:
            return 'DUMMY_212'

        if table2Version == 254 and indicatorOfParameter == 211:
            return 'DUMMY_211'

        if table2Version == 254 and indicatorOfParameter == 210:
            return 'DUMMY_210'

        if table2Version == 254 and indicatorOfParameter == 209:
            return 'DUMMY_209'

        if table2Version == 254 and indicatorOfParameter == 208:
            return 'DUMMY_208'

        if table2Version == 254 and indicatorOfParameter == 207:
            return 'DUMMY_207'

        if table2Version == 254 and indicatorOfParameter == 206:
            return 'DUMMY_206'

        if table2Version == 254 and indicatorOfParameter == 205:
            return 'DUMMY_205'

        if table2Version == 254 and indicatorOfParameter == 204:
            return 'DUMMY_204'

        if table2Version == 254 and indicatorOfParameter == 203:
            return 'DUMMY_203'

        if table2Version == 254 and indicatorOfParameter == 202:
            return 'DUMMY_202'

        if table2Version == 254 and indicatorOfParameter == 201:
            return 'DUMMY_201'

        if table2Version == 254 and indicatorOfParameter == 200:
            return 'DUMMY_200'

        if table2Version == 254 and indicatorOfParameter == 199:
            return 'DUMMY_199'

        if table2Version == 254 and indicatorOfParameter == 198:
            return 'DUMMY_198'

        if table2Version == 254 and indicatorOfParameter == 197:
            return 'DUMMY_197'

        if table2Version == 254 and indicatorOfParameter == 196:
            return 'DUMMY_196'

        if table2Version == 254 and indicatorOfParameter == 195:
            return 'DUMMY_195'

        if table2Version == 254 and indicatorOfParameter == 194:
            return 'DUMMY_194'

        if table2Version == 254 and indicatorOfParameter == 193:
            return 'DUMMY_193'

        if table2Version == 254 and indicatorOfParameter == 192:
            return 'DUMMY_192'

        if table2Version == 254 and indicatorOfParameter == 191:
            return 'DUMMY_191'

        if table2Version == 254 and indicatorOfParameter == 190:
            return 'DUMMY_190'

        if table2Version == 254 and indicatorOfParameter == 189:
            return 'DUMMY_189'

        if table2Version == 254 and indicatorOfParameter == 188:
            return 'DUMMY_188'

        if table2Version == 254 and indicatorOfParameter == 187:
            return 'DUMMY_187'

        if table2Version == 254 and indicatorOfParameter == 186:
            return 'DUMMY_186'

        if table2Version == 254 and indicatorOfParameter == 185:
            return 'DUMMY_185'

        if table2Version == 254 and indicatorOfParameter == 184:
            return 'DUMMY_184'

        if table2Version == 254 and indicatorOfParameter == 183:
            return 'DUMMY_183'

        if table2Version == 254 and indicatorOfParameter == 182:
            return 'DUMMY_182'

        if table2Version == 254 and indicatorOfParameter == 181:
            return 'DUMMY_181'

        if table2Version == 254 and indicatorOfParameter == 180:
            return 'DUMMY_180'

        if table2Version == 254 and indicatorOfParameter == 179:
            return 'DUMMY_179'

        if table2Version == 254 and indicatorOfParameter == 178:
            return 'DUMMY_178'

        if table2Version == 254 and indicatorOfParameter == 177:
            return 'DUMMY_177'

        if table2Version == 254 and indicatorOfParameter == 176:
            return 'DUMMY_176'

        if table2Version == 254 and indicatorOfParameter == 175:
            return 'DUMMY_175'

        if table2Version == 254 and indicatorOfParameter == 174:
            return 'DUMMY_174'

        if table2Version == 254 and indicatorOfParameter == 173:
            return 'DUMMY_173'

        if table2Version == 254 and indicatorOfParameter == 172:
            return 'DUMMY_172'

        if table2Version == 254 and indicatorOfParameter == 171:
            return 'DUMMY_171'

        if table2Version == 254 and indicatorOfParameter == 170:
            return 'DUMMY_170'

        if table2Version == 254 and indicatorOfParameter == 169:
            return 'DUMMY_169'

        if table2Version == 254 and indicatorOfParameter == 168:
            return 'DUMMY_168'

        if table2Version == 254 and indicatorOfParameter == 167:
            return 'DUMMY_167'

        if table2Version == 254 and indicatorOfParameter == 166:
            return 'DUMMY_166'

        if table2Version == 254 and indicatorOfParameter == 165:
            return 'DUMMY_165'

        if table2Version == 254 and indicatorOfParameter == 164:
            return 'DUMMY_164'

        if table2Version == 254 and indicatorOfParameter == 163:
            return 'DUMMY_163'

        if table2Version == 254 and indicatorOfParameter == 162:
            return 'DUMMY_162'

        if table2Version == 254 and indicatorOfParameter == 161:
            return 'DUMMY_161'

        if table2Version == 254 and indicatorOfParameter == 160:
            return 'DUMMY_160'

        if table2Version == 254 and indicatorOfParameter == 159:
            return 'DUMMY_159'

        if table2Version == 254 and indicatorOfParameter == 158:
            return 'DUMMY_158'

        if table2Version == 254 and indicatorOfParameter == 157:
            return 'DUMMY_157'

        if table2Version == 254 and indicatorOfParameter == 156:
            return 'DUMMY_156'

        if table2Version == 254 and indicatorOfParameter == 155:
            return 'DUMMY_155'

        if table2Version == 254 and indicatorOfParameter == 154:
            return 'DUMMY_154'

        if table2Version == 254 and indicatorOfParameter == 153:
            return 'DUMMY_153'

        if table2Version == 254 and indicatorOfParameter == 152:
            return 'DUMMY_152'

        if table2Version == 254 and indicatorOfParameter == 151:
            return 'DUMMY_151'

        if table2Version == 254 and indicatorOfParameter == 150:
            return 'DUMMY_150'

        if table2Version == 254 and indicatorOfParameter == 149:
            return 'DUMMY_149'

        if table2Version == 254 and indicatorOfParameter == 148:
            return 'DUMMY_148'

        if table2Version == 254 and indicatorOfParameter == 147:
            return 'DUMMY_147'

        if table2Version == 254 and indicatorOfParameter == 146:
            return 'DUMMY_146'

        if table2Version == 254 and indicatorOfParameter == 145:
            return 'DUMMY_145'

        if table2Version == 254 and indicatorOfParameter == 144:
            return 'DUMMY_144'

        if table2Version == 254 and indicatorOfParameter == 143:
            return 'DUMMY_143'

        if table2Version == 254 and indicatorOfParameter == 142:
            return 'DUMMY_142'

        if table2Version == 254 and indicatorOfParameter == 141:
            return 'DUMMY_141'

        if table2Version == 254 and indicatorOfParameter == 140:
            return 'DUMMY_140'

        if table2Version == 254 and indicatorOfParameter == 139:
            return 'DUMMY_139'

        if table2Version == 254 and indicatorOfParameter == 138:
            return 'DUMMY_138'

        if table2Version == 254 and indicatorOfParameter == 137:
            return 'DUMMY_137'

        if table2Version == 254 and indicatorOfParameter == 136:
            return 'DUMMY_136'

        if table2Version == 254 and indicatorOfParameter == 135:
            return 'DUMMY_135'

        if table2Version == 254 and indicatorOfParameter == 134:
            return 'DUMMY_134'

        if table2Version == 254 and indicatorOfParameter == 133:
            return 'DUMMY_133'

        if table2Version == 254 and indicatorOfParameter == 132:
            return 'DUMMY_132'

        if table2Version == 254 and indicatorOfParameter == 131:
            return 'DUMMY_131'

        if table2Version == 254 and indicatorOfParameter == 130:
            return 'DUMMY_130'

        if table2Version == 254 and indicatorOfParameter == 129:
            return 'DUMMY_129'

        if table2Version == 254 and indicatorOfParameter == 128:
            return 'DUMMY_128'

        if table2Version == 254 and indicatorOfParameter == 127:
            return 'DUMMY_127'

        if table2Version == 254 and indicatorOfParameter == 126:
            return 'DUMMY_126'

        if table2Version == 254 and indicatorOfParameter == 125:
            return 'DUMMY_125'

        if table2Version == 254 and indicatorOfParameter == 124:
            return 'DUMMY_124'

        if table2Version == 254 and indicatorOfParameter == 123:
            return 'DUMMY_123'

        if table2Version == 254 and indicatorOfParameter == 122:
            return 'DUMMY_122'

        if table2Version == 254 and indicatorOfParameter == 121:
            return 'DUMMY_121'

        if table2Version == 254 and indicatorOfParameter == 120:
            return 'DUMMY_120'

        if table2Version == 254 and indicatorOfParameter == 119:
            return 'DUMMY_119'

        if table2Version == 254 and indicatorOfParameter == 118:
            return 'DUMMY_118'

        if table2Version == 254 and indicatorOfParameter == 117:
            return 'DUMMY_117'

        if table2Version == 254 and indicatorOfParameter == 116:
            return 'DUMMY_116'

        if table2Version == 254 and indicatorOfParameter == 115:
            return 'DUMMY_115'

        if table2Version == 254 and indicatorOfParameter == 114:
            return 'DUMMY_114'

        if table2Version == 254 and indicatorOfParameter == 113:
            return 'DUMMY_113'

        if table2Version == 254 and indicatorOfParameter == 112:
            return 'DUMMY_112'

        if table2Version == 254 and indicatorOfParameter == 111:
            return 'DUMMY_111'

        if table2Version == 254 and indicatorOfParameter == 110:
            return 'DUMMY_110'

        if table2Version == 254 and indicatorOfParameter == 109:
            return 'DUMMY_109'

        if table2Version == 254 and indicatorOfParameter == 108:
            return 'DUMMY_108'

        if table2Version == 254 and indicatorOfParameter == 107:
            return 'DUMMY_107'

        if table2Version == 254 and indicatorOfParameter == 106:
            return 'DUMMY_106'

        if table2Version == 254 and indicatorOfParameter == 105:
            return 'DUMMY_105'

        if table2Version == 254 and indicatorOfParameter == 104:
            return 'DUMMY_104'

        if table2Version == 254 and indicatorOfParameter == 103:
            return 'DUMMY_103'

        if table2Version == 254 and indicatorOfParameter == 102:
            return 'DUMMY_102'

        if table2Version == 254 and indicatorOfParameter == 101:
            return 'DUMMY_101'

        if table2Version == 254 and indicatorOfParameter == 100:
            return 'DUMMY_100'

        if table2Version == 254 and indicatorOfParameter == 99:
            return 'DUMMY_99'

        if table2Version == 254 and indicatorOfParameter == 98:
            return 'DUMMY_98'

        if table2Version == 254 and indicatorOfParameter == 97:
            return 'DUMMY_97'

        if table2Version == 254 and indicatorOfParameter == 96:
            return 'DUMMY_96'

        if table2Version == 254 and indicatorOfParameter == 95:
            return 'DUMMY_95'

        if table2Version == 254 and indicatorOfParameter == 94:
            return 'DUMMY_94'

        if table2Version == 254 and indicatorOfParameter == 93:
            return 'DUMMY_93'

        if table2Version == 254 and indicatorOfParameter == 92:
            return 'DUMMY_92'

        if table2Version == 254 and indicatorOfParameter == 91:
            return 'DUMMY_91'

        if table2Version == 254 and indicatorOfParameter == 90:
            return 'DUMMY_90'

        if table2Version == 254 and indicatorOfParameter == 89:
            return 'DUMMY_89'

        if table2Version == 254 and indicatorOfParameter == 88:
            return 'DUMMY_88'

        if table2Version == 254 and indicatorOfParameter == 87:
            return 'DUMMY_87'

        if table2Version == 254 and indicatorOfParameter == 86:
            return 'DUMMY_86'

        if table2Version == 254 and indicatorOfParameter == 85:
            return 'DUMMY_85'

        if table2Version == 254 and indicatorOfParameter == 84:
            return 'DUMMY_84'

        if table2Version == 254 and indicatorOfParameter == 83:
            return 'DUMMY_83'

        if table2Version == 254 and indicatorOfParameter == 82:
            return 'DUMMY_82'

        if table2Version == 254 and indicatorOfParameter == 81:
            return 'DUMMY_81'

        if table2Version == 254 and indicatorOfParameter == 80:
            return 'DUMMY_80'

        if table2Version == 254 and indicatorOfParameter == 79:
            return 'DUMMY_79'

        if table2Version == 254 and indicatorOfParameter == 78:
            return 'DUMMY_78'

        if table2Version == 254 and indicatorOfParameter == 77:
            return 'DUMMY_77'

        if table2Version == 254 and indicatorOfParameter == 76:
            return 'DUMMY_76'

        if table2Version == 254 and indicatorOfParameter == 75:
            return 'DUMMY_75'

        if table2Version == 254 and indicatorOfParameter == 74:
            return 'DUMMY_74'

        if table2Version == 254 and indicatorOfParameter == 73:
            return 'DUMMY_73'

        if table2Version == 254 and indicatorOfParameter == 72:
            return 'DUMMY_72'

        if table2Version == 254 and indicatorOfParameter == 71:
            return 'DUMMY_71'

        if table2Version == 254 and indicatorOfParameter == 70:
            return 'DUMMY_70'

        if table2Version == 254 and indicatorOfParameter == 69:
            return 'DUMMY_69'

        if table2Version == 254 and indicatorOfParameter == 68:
            return 'DUMMY_68'

        if table2Version == 254 and indicatorOfParameter == 67:
            return 'DUMMY_67'

        if table2Version == 254 and indicatorOfParameter == 66:
            return 'DUMMY_66'

        if table2Version == 254 and indicatorOfParameter == 65:
            return 'DUMMY_65'

        if table2Version == 254 and indicatorOfParameter == 64:
            return 'DUMMY_64'

        if table2Version == 254 and indicatorOfParameter == 63:
            return 'DUMMY_63'

        if table2Version == 254 and indicatorOfParameter == 62:
            return 'DUMMY_62'

        if table2Version == 254 and indicatorOfParameter == 61:
            return 'DUMMY_61'

        if table2Version == 254 and indicatorOfParameter == 60:
            return 'DUMMY_60'

        if table2Version == 254 and indicatorOfParameter == 59:
            return 'DUMMY_59'

        if table2Version == 254 and indicatorOfParameter == 58:
            return 'DUMMY_58'

        if table2Version == 254 and indicatorOfParameter == 57:
            return 'DUMMY_57'

        if table2Version == 254 and indicatorOfParameter == 56:
            return 'DUMMY_56'

        if table2Version == 254 and indicatorOfParameter == 55:
            return 'DUMMY_55'

        if table2Version == 254 and indicatorOfParameter == 54:
            return 'DUMMY_54'

        if table2Version == 254 and indicatorOfParameter == 53:
            return 'DUMMY_53'

        if table2Version == 254 and indicatorOfParameter == 52:
            return 'DUMMY_52'

        if table2Version == 254 and indicatorOfParameter == 51:
            return 'DUMMY_51'

        if table2Version == 254 and indicatorOfParameter == 50:
            return 'DUMMY_50'

        if table2Version == 254 and indicatorOfParameter == 49:
            return 'DUMMY_49'

        if table2Version == 254 and indicatorOfParameter == 48:
            return 'DUMMY_48'

        if table2Version == 254 and indicatorOfParameter == 47:
            return 'DUMMY_47'

        if table2Version == 254 and indicatorOfParameter == 46:
            return 'DUMMY_46'

        if table2Version == 254 and indicatorOfParameter == 45:
            return 'DUMMY_45'

        if table2Version == 254 and indicatorOfParameter == 44:
            return 'DUMMY_44'

        if table2Version == 254 and indicatorOfParameter == 43:
            return 'DUMMY_43'

        if table2Version == 254 and indicatorOfParameter == 42:
            return 'DUMMY_42'

        if table2Version == 254 and indicatorOfParameter == 41:
            return 'DUMMY_41'

        if table2Version == 254 and indicatorOfParameter == 40:
            return 'DUMMY_40'

        if table2Version == 254 and indicatorOfParameter == 39:
            return 'DUMMY_39'

        if table2Version == 254 and indicatorOfParameter == 38:
            return 'DUMMY_38'

        if table2Version == 254 and indicatorOfParameter == 37:
            return 'DUMMY_37'

        if table2Version == 254 and indicatorOfParameter == 36:
            return 'DUMMY_36'

        if table2Version == 254 and indicatorOfParameter == 35:
            return 'DUMMY_35'

        if table2Version == 254 and indicatorOfParameter == 34:
            return 'DUMMY_34'

        if table2Version == 254 and indicatorOfParameter == 33:
            return 'DUMMY_33'

        if table2Version == 254 and indicatorOfParameter == 32:
            return 'DUMMY_32'

        if table2Version == 254 and indicatorOfParameter == 31:
            return 'DUMMY_31'

        if table2Version == 254 and indicatorOfParameter == 30:
            return 'DUMMY_30'

        if table2Version == 254 and indicatorOfParameter == 29:
            return 'DUMMY_29'

        if table2Version == 254 and indicatorOfParameter == 28:
            return 'DUMMY_28'

        if table2Version == 254 and indicatorOfParameter == 27:
            return 'DUMMY_27'

        if table2Version == 254 and indicatorOfParameter == 26:
            return 'DUMMY_26'

        if table2Version == 254 and indicatorOfParameter == 25:
            return 'DUMMY_25'

        if table2Version == 254 and indicatorOfParameter == 24:
            return 'DUMMY_24'

        if table2Version == 254 and indicatorOfParameter == 23:
            return 'DUMMY_23'

        if table2Version == 254 and indicatorOfParameter == 22:
            return 'DUMMY_22'

        if table2Version == 254 and indicatorOfParameter == 21:
            return 'DUMMY_21'

        if table2Version == 254 and indicatorOfParameter == 20:
            return 'DUMMY_20'

        if table2Version == 254 and indicatorOfParameter == 19:
            return 'DUMMY_19'

        if table2Version == 254 and indicatorOfParameter == 18:
            return 'DUMMY_18'

        if table2Version == 254 and indicatorOfParameter == 17:
            return 'DUMMY_17'

        if table2Version == 254 and indicatorOfParameter == 16:
            return 'DUMMY_16'

        if table2Version == 254 and indicatorOfParameter == 15:
            return 'DUMMY_15'

        if table2Version == 254 and indicatorOfParameter == 14:
            return 'DUMMY_14'

        if table2Version == 254 and indicatorOfParameter == 13:
            return 'DUMMY_13'

        if table2Version == 254 and indicatorOfParameter == 12:
            return 'DUMMY_12'

        if table2Version == 254 and indicatorOfParameter == 11:
            return 'DUMMY_11'

        if table2Version == 254 and indicatorOfParameter == 10:
            return 'DUMMY_10'

        if table2Version == 254 and indicatorOfParameter == 9:
            return 'DUMMY_9'

        if table2Version == 254 and indicatorOfParameter == 8:
            return 'DUMMY_8'

        if table2Version == 254 and indicatorOfParameter == 7:
            return 'DUMMY_7'

        if table2Version == 254 and indicatorOfParameter == 6:
            return 'DUMMY_6'

        if table2Version == 254 and indicatorOfParameter == 5:
            return 'DUMMY_5'

        if table2Version == 254 and indicatorOfParameter == 4:
            return 'DUMMY_4'

        if table2Version == 254 and indicatorOfParameter == 3:
            return 'DUMMY_3'

        if table2Version == 254 and indicatorOfParameter == 2:
            return 'DUMMY_2'

        if table2Version == 254 and indicatorOfParameter == 1:
            return 'DUMMY_1'

        if table2Version == 242 and indicatorOfParameter == 252:
            return 'VSOILS0'

        if table2Version == 242 and indicatorOfParameter == 251:
            return 'VSOILS'

        if table2Version == 242 and indicatorOfParameter == 74:
            return 'VSOILC0'

        if table2Version == 242 and indicatorOfParameter == 73:
            return 'VSOILB0'

        if table2Version == 242 and indicatorOfParameter == 72:
            return 'VSOILA0'

        if table2Version == 242 and indicatorOfParameter == 35:
            return 'VSOILC'

        if table2Version == 242 and indicatorOfParameter == 34:
            return 'VSOILB'

        if table2Version == 2 and indicatorOfParameter == 19:
            return 'LAPSE_RATE'

        if table2Version == 242 and indicatorOfParameter == 33:
            return 'VSOILA'

        if table2Version == 201 and indicatorOfParameter == 90:
            return 'HTOP_THERM'

        if table2Version == 201 and indicatorOfParameter == 211:
            return 'ATM_RSTC'

        if table2Version == 201 and indicatorOfParameter == 157:
            return 'DTKE_CON'

        if table2Version == 201 and indicatorOfParameter == 156:
            return 'DTKE_HSH'

        if table2Version == 201 and indicatorOfParameter == 155:
            return 'DTKE_SSO'

        if table2Version == 210 and indicatorOfParameter == 34:
            return 'TAUX'

        if table2Version == 210 and indicatorOfParameter == 33:
            return 'TAU'

        if table2Version == 210 and indicatorOfParameter == 32:
            return 'FG'

        if table2Version == 210 and indicatorOfParameter == 31:
            return 'FZRAX'

        if table2Version == 210 and indicatorOfParameter == 30:
            return 'FZRA'

        if table2Version == 210 and indicatorOfParameter == 29:
            return 'FZ'

        if table2Version == 210 and indicatorOfParameter == 28:
            return 'BLSN8'

        if table2Version == 210 and indicatorOfParameter == 27:
            return 'BLSN6'

        if table2Version == 210 and indicatorOfParameter == 26:
            return 'RA70'

        if table2Version == 210 and indicatorOfParameter == 25:
            return 'RA40'

        if table2Version == 210 and indicatorOfParameter == 24:
            return 'RA25'

        if table2Version == 210 and indicatorOfParameter == 23:
            return 'TSXX'

        if table2Version == 210 and indicatorOfParameter == 22:
            return 'TSX'

        if table2Version == 210 and indicatorOfParameter == 21:
            return 'TS'

        if table2Version == 210 and indicatorOfParameter == 20:
            return 'TN10'

        if table2Version == 210 and indicatorOfParameter == 19:
            return 'TN00'

        if table2Version == 210 and indicatorOfParameter == 18:
            return 'SN25'

        if table2Version == 210 and indicatorOfParameter == 17:
            return 'SN10'

        if table2Version == 210 and indicatorOfParameter == 16:
            return 'SN05'

        if table2Version == 210 and indicatorOfParameter == 15:
            return 'SN01'

        if table2Version == 210 and indicatorOfParameter == 14:
            return 'SN005'

        if table2Version == 210 and indicatorOfParameter == 13:
            return 'SN001'

        if table2Version == 210 and indicatorOfParameter == 12:
            return 'SN00'

        if table2Version == 210 and indicatorOfParameter == 11:
            return 'SH50'

        if table2Version == 210 and indicatorOfParameter == 10:
            return 'SH25'

        if table2Version == 210 and indicatorOfParameter == 9:
            return 'SH10'

        if table2Version == 210 and indicatorOfParameter == 8:
            return 'FX75'

        if table2Version == 210 and indicatorOfParameter == 7:
            return 'FX63'

        if table2Version == 210 and indicatorOfParameter == 6:
            return 'FX55'

        if table2Version == 210 and indicatorOfParameter == 5:
            return 'FX47'

        if table2Version == 210 and indicatorOfParameter == 4:
            return 'FX40'

        if table2Version == 210 and indicatorOfParameter == 3:
            return 'FX33'

        if table2Version == 210 and indicatorOfParameter == 2:
            return 'FX27'

        if table2Version == 210 and indicatorOfParameter == 1:
            return 'FX25'

        if table2Version == 2 and indicatorOfParameter == 117:
            return 'GRAD'

        if table2Version == 203 and indicatorOfParameter == 2:
            return 'GH_10GPM'

        if table2Version == 2 and indicatorOfParameter == 5:
            return 'ICAHT'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'SNOW_MELT'

        if table2Version == 204 and indicatorOfParameter == 71:
            return 'ELD'

        if table2Version == 204 and indicatorOfParameter == 70:
            return 'EDP'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 1 and level == 2:
            return 'TMIN_2M'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 1 and level == 2:
            return 'TMAX_2M'

        topLevel = h.get_l('topLevel')
        bottomLevel = h.get_l('bottomLevel')

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 7 and bottomLevel == 50:
            return 'W_G4'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 7:
            return 'W_G3'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 112:
            return 'T_S_L'

        localElementNumber = h.get_l('localElementNumber')

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 2 and indicatorOfTypeOfLevel == 112 and topLevel == 0:
            return 'WCOV1'

        if table2Version == 203 and indicatorOfParameter == 10:
            return 'PPP'

        if table2Version == 202 and indicatorOfParameter == 119:
            return 'LNPS'

        if table2Version == 202 and indicatorOfParameter == 117:
            return 'SST_IC'

        if table2Version == 202 and indicatorOfParameter == 101:
            return 'TIDAL'

        if table2Version == 201 and indicatorOfParameter == 231:
            return 'FE1'

        if table2Version == 201 and indicatorOfParameter == 83:
            return 'TOP_DCON'

        if table2Version == 2 and indicatorOfParameter == 44:
            return 'RDIV'

        if table2Version == 2 and indicatorOfParameter == 7:
            return 'GH'

        if table2Version == 203 and indicatorOfParameter == 146:
            return 'CATIX'

        if table2Version == 203 and indicatorOfParameter == 128:
            return 'FRONTOF'

        if table2Version == 203 and indicatorOfParameter == 127:
            return 'DIVQS'

        if table2Version == 203 and indicatorOfParameter == 126:
            return 'DIVQN'

        if table2Version == 203 and indicatorOfParameter == 125:
            return 'QVS'

        if table2Version == 203 and indicatorOfParameter == 123:
            return 'DIVQ'

        if table2Version == 203 and indicatorOfParameter == 118:
            return 'FRONTO'

        if table2Version == 203 and indicatorOfParameter == 117:
            return 'DIVQSGEO'

        if table2Version == 203 and indicatorOfParameter == 116:
            return 'DIVQNGEO'

        if table2Version == 203 and indicatorOfParameter == 115:
            return 'QVSGEO'

        if table2Version == 203 and indicatorOfParameter == 114:
            return 'QVNGEO'

        if table2Version == 203 and indicatorOfParameter == 113:
            return 'DIVGEO'

        if table2Version == 203 and indicatorOfParameter == 112:
            return 'QVY'

        if table2Version == 203 and indicatorOfParameter == 111:
            return 'QVX'

        if table2Version == 203 and indicatorOfParameter == 105:
            return 'FORCOMEGA'

        if table2Version == 203 and indicatorOfParameter == 100:
            return 'VORG'

        if table2Version == 203 and indicatorOfParameter == 119:
            return 'PVP'

        if table2Version == 2 and indicatorOfParameter == 63 and timeRangeIndicator == 5:
            return 'PREC_CON_D'

        if table2Version == 2 and indicatorOfParameter == 89:
            return 'DEN'

        if table2Version == 2 and indicatorOfParameter == 4:
            return 'POT_VORTIC'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 'VORTIC_W'

        if table2Version == 202 and indicatorOfParameter == 134:
            return 'VORTIC_V'

        if table2Version == 202 and indicatorOfParameter == 133:
            return 'VORTIC_U'

        if table2Version == 203 and indicatorOfParameter == 205:
            return 'WW_0-9'

        if table2Version == 203 and indicatorOfParameter == 194:
            return 'DIS_CODE'

        if table2Version == 203 and indicatorOfParameter == 193:
            return 'DID_CODE'

        if table2Version == 203 and indicatorOfParameter == 192:
            return 'PIS_CODE'

        if table2Version == 203 and indicatorOfParameter == 191:
            return 'PID_CODE'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'DISC_SIG_CODE'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'DISC_VERT_CODE'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'DISC_TOP_HFT'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'DISC_SIG_TOP_HFT'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'DISC_SIG_BASE_HFT'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'DISC_BASE_HFT'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'DIDC_MAX_CODE'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'DIDC_VERT_CODE'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'DIDC_TOP_HFT'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'DIDC_MAX_TOP_HFT'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'DIDC_MAX_BASE_HFT'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'DIDC_BASE_HFT'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'PISC_SIG_CODE'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'PISC_VERT_CODE'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'PISC_TOP_HFT'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'PISC_SIG_TOP_HFT'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'PISC_SIG_BASE_HFT'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'PISC_BASE_HFT'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'PIDC_MAX_CODE'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'PIDC_VERT_CODE'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'PIDC_TOP_HFT'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'PIDC_MAX_TOP_HFT'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'PIDC_MAX_BASE_HFT'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'PIDC_BASE_HFT'

        if table2Version == 201 and indicatorOfParameter == 94:
            return 'H_B1_LK'

        if table2Version == 201 and indicatorOfParameter == 192:
            return 'T_B1_LK'

        if table2Version == 201 and indicatorOfParameter == 91:
            return 'C_T_LK'

        if table2Version == 201 and indicatorOfParameter == 95:
            return 'H_ML_LK'

        if table2Version == 201 and indicatorOfParameter == 191:
            return 'T_BOT_LK'

        if table2Version == 201 and indicatorOfParameter == 193:
            return 'T_WML_LK'

        if table2Version == 201 and indicatorOfParameter == 194:
            return 'T_MNW_LK'

        if table2Version == 201 and indicatorOfParameter == 190:
            return 'T_BS_LK'

        if table2Version == 201 and indicatorOfParameter == 93:
            return 'DP_BS_LK'

        if table2Version == 201 and indicatorOfParameter == 92:
            return 'GAMSO_LK'

        if table2Version == 201 and indicatorOfParameter == 97:
            return 'FETCH_LK'

        if table2Version == 201 and indicatorOfParameter == 96:
            return 'DEPTH_LK'

        if table2Version == 202 and indicatorOfParameter == 55:
            return 'FR_LAKE'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'ASWDIFU_S'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'ASWDIFD_S'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'ASWDIR_S'

        if table2Version == 201 and indicatorOfParameter == 42 and timeRangeIndicator == 0:
            return 'TDIV_HUM'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'ASWDIFU_S'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'ASWDIFD_S'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'ASWDIR_S'

        if table2Version == 203 and indicatorOfParameter == 58:
            return 'CLO'

        if table2Version == 203 and indicatorOfParameter == 57:
            return 'SUL_PROB'

        if table2Version == 2 and indicatorOfParameter == 41:
            return 'ABSV'

        if table2Version == 203 and indicatorOfParameter == 61:
            return 'T_SEA_C'

        if table2Version == 2 and indicatorOfParameter == 80:
            return 'T_SEA'

        if table2Version == 203 and indicatorOfParameter == 60:
            return 'PT1M'

        if table2Version == 203 and indicatorOfParameter == 93:
            return 'C_TYPE'

        if table2Version == 202 and indicatorOfParameter == 249:
            return 'UVI_MAX_H'

        if table2Version == 202 and indicatorOfParameter == 247:
            return 'TOT_O3'

        if table2Version == 202 and indicatorOfParameter == 243:
            return 'UVI_MAX_CS'

        if table2Version == 202 and indicatorOfParameter == 242:
            return 'UVI_CL_COR'

        if table2Version == 202 and indicatorOfParameter == 241:
            return 'UVI_B_CS'

        if table2Version == 202 and indicatorOfParameter == 240:
            return 'UVI_CS_COR'

        if table2Version == 208 and indicatorOfParameter == 236:
            return 'W_FRSTR_06'

        if table2Version == 208 and indicatorOfParameter == 232:
            return 'W_FR_01'

        if table2Version == 208 and indicatorOfParameter == 213:
            return 'U_SVWSK_12'

        if table2Version == 208 and indicatorOfParameter == 212:
            return 'W_SVW_12'

        if table2Version == 208 and indicatorOfParameter == 199:
            return 'U_GEWSW_01'

        if table2Version == 208 and indicatorOfParameter == 198:
            return 'W_GEWSK_01'

        if table2Version == 208 and indicatorOfParameter == 197:
            return 'W_GEW_01'

        if table2Version == 208 and indicatorOfParameter == 191:
            return 'W_GLEIS_01'

        if table2Version == 208 and indicatorOfParameter == 139:
            return 'E_ORK_01'

        if table2Version == 208 and indicatorOfParameter == 138:
            return 'U_ORK_01'

        if table2Version == 208 and indicatorOfParameter == 137:
            return 'U_ORKAR_01'

        if table2Version == 208 and indicatorOfParameter == 136:
            return 'W_STMSW_01'

        if table2Version == 208 and indicatorOfParameter == 134:
            return 'W_STM_01'

        if table2Version == 208 and indicatorOfParameter == 132:
            return 'W_WND_01'

        if table2Version == 208 and indicatorOfParameter == 77:
            return 'E_SF_12'

        if table2Version == 208 and indicatorOfParameter == 75:
            return 'U_SFSK_12'

        if table2Version == 208 and indicatorOfParameter == 74:
            return 'W_SF_12'

        if table2Version == 208 and indicatorOfParameter == 72:
            return 'W_SFL_12'

        if table2Version == 208 and indicatorOfParameter == 71:
            return 'U_SFSK_06'

        if table2Version == 208 and indicatorOfParameter == 70:
            return 'W_SF_06'

        if table2Version == 208 and indicatorOfParameter == 69:
            return 'W_SFL_06'

        if table2Version == 208 and indicatorOfParameter == 32:
            return 'E_DR_12'

        if table2Version == 208 and indicatorOfParameter == 29:
            return 'U_DRRER_12'

        if table2Version == 208 and indicatorOfParameter == 26:
            return 'W_DRR_12'

        if table2Version == 208 and indicatorOfParameter == 17:
            return 'U_SKRRH_06'

        if table2Version == 208 and indicatorOfParameter == 14:
            return 'W_SKRR_06'

        if table2Version == 208 and indicatorOfParameter == 3:
            return 'U_SKRRH_01'

        if table2Version == 208 and indicatorOfParameter == 1:
            return 'W_SKRR_01'

        if table2Version == 201 and indicatorOfParameter == 132 and timeRangeIndicator == 0:
            return 'GRAU_GSP'

        if table2Version == 201 and indicatorOfParameter == 113 and timeRangeIndicator == 1:
            return 'RAIN_CON'

        if table2Version == 201 and indicatorOfParameter == 102 and timeRangeIndicator == 1:
            return 'RAIN_GSP'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'APAB_S'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'AVMFL_S'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'AUMFL_S'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'ASHFL_S'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'ALHFL_S'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 1:
            return 'TOT_PREC'

        if table2Version == 2 and indicatorOfParameter == 78 and timeRangeIndicator == 1:
            return 'SNOW_CON'

        if table2Version == 2 and indicatorOfParameter == 79 and timeRangeIndicator == 1:
            return 'SNOW_GSP'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'ATHB_S'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'ASOB_S'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 1:
            return 'ATHB_T'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 1:
            return 'ASOB_T'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 2:
            return 'TMIN_2M'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 2:
            return 'TMAX_2M'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'AEVAP_S'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 10:
            return 'VMAX_10M'

        if table2Version == 2 and indicatorOfParameter == 78 and timeRangeIndicator == 0:
            return 'SNOW_CON'

        if table2Version == 201 and indicatorOfParameter == 113 and timeRangeIndicator == 0:
            return 'RAIN_CON'

        if table2Version == 2 and indicatorOfParameter == 79 and timeRangeIndicator == 0:
            return 'SNOW_GSP'

        if table2Version == 201 and indicatorOfParameter == 102 and timeRangeIndicator == 0:
            return 'RAIN_GSP'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 0:
            return 'TOT_PREC'

        if table2Version == 203 and indicatorOfParameter == 56 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'TMIN_2M_L'

        if table2Version == 203 and indicatorOfParameter == 55 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'TMAX_2M_L'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 5:
            return 'TOT_PREC_D'

        if table2Version == 207 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'VMAX_10M_C'

        if table2Version == 207 and indicatorOfParameter == 79:
            return 'SNOW_GSP_C'

        if table2Version == 207 and indicatorOfParameter == 61:
            return 'TOT_PREC_C'

        if table2Version == 206 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'VMAX_10M_S'

        if table2Version == 206 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 'T_S_S'

        if table2Version == 206 and indicatorOfParameter == 79:
            return 'SNOW_GSP_S'

        if table2Version == 206 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'CLCH_S'

        if table2Version == 206 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 'CLCM_S'

        if table2Version == 206 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'CLCL_S'

        if table2Version == 206 and indicatorOfParameter == 71:
            return 'CLCT_S'

        if table2Version == 206 and indicatorOfParameter == 61:
            return 'TOT_PREC_S'

        if table2Version == 206 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'V_10M_S'

        if table2Version == 206 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'U_10M_S'

        if table2Version == 206 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'TD_2M_S'

        if table2Version == 206 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'TMIN_2M_S'

        if table2Version == 206 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'TMAX_2M_S'

        if table2Version == 206 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'T_2M_S'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'SYNMSG_RAD_CS_WV7.3'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'SYNMSG_RAD_CS_WV6.2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'SYNMSG_RAD_CS_IR9.7'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'SYNMSG_RAD_CS_IR8.7'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'SYNMSG_RAD_CS_IR3.9'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'SYNMSG_RAD_CS_IR13.4'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'SYNMSG_RAD_CS_IR12.1'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'SYNMSG_RAD_CS_IR10.8'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'SYNMSG_RAD_CL_WV7.3'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'SYNMSG_RAD_CL_WV6.2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'SYNMSG_RAD_CL_IR9.7'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'SYNMSG_RAD_CL_IR8.7'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'SYNMSG_RAD_CL_IR3.9'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'SYNMSG_RAD_CL_IR13.4'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'SYNMSG_RAD_CL_IR12.1'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'SYNMSG_RAD_CL_IR10.8'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'SYNMSG_BT_CS_WV7.3'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'SYNMSG_BT_CS_WV6.2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'SYNMSG_BT_CS_IR9.7'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'SYNMSG_BT_CS_IR3.9'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'SYNMSG_BT_CS_IR13.4'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'SYNMSG_BT_CS_IR12.1'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'SYNMSG_BT_CS_IR10.8'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'SYNMSG_BT_CS_IR8.7'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'SYNMSG_BT_CL_WV7.3'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'SYNMSG_BT_CL_WV6.2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'SYNMSG_BT_CL_IR9.7'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'SYNMSG_BT_CL_IR8.7'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'SYNMSG_BT_CL_IR3.9'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'SYNMSG_BT_CL_IR13.4'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'SYNMSG_BT_CL_IR12.1'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'SYNMSG_BT_CL_IR10.8'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'SYNME7_RAD_CS_WV6.4'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'SYNME7_RAD_CS_IR11.5'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'SYNME7_RAD_CL_WV6.4'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'SYNME7_RAD_CL_IR11.5'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'SYNME7_BT_CS_WV6.4'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'SYNME7_BT_CS_IR11.5'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'SYNME7_BT_CL_WV6.4'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'SYNME7_BT_CL_IR11.5'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222:
            return 'SYNME6_RAD_CS'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222:
            return 'SYNME6_RAD_CL'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222:
            return 'SYNME6_BT_CS'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222:
            return 'SYNME6_BT_CL'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222:
            return 'SYNME5_RAD_CS'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222:
            return 'SYNME5_RAD_CL'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222:
            return 'SYNME5_BT_CS'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222:
            return 'SYNME5_BT_CL'

        if table2Version == 204 and indicatorOfParameter == 16:
            return 'EIA-KE'

        if table2Version == 204 and indicatorOfParameter == 15:
            return 'EFA-KE'

        if table2Version == 204 and indicatorOfParameter == 14:
            return 'EIA-OM'

        if table2Version == 204 and indicatorOfParameter == 13:
            return 'EFA-OM'

        if table2Version == 204 and indicatorOfParameter == 12:
            return 'EIA-T'

        if table2Version == 204 and indicatorOfParameter == 11:
            return 'EFA-T'

        if table2Version == 204 and indicatorOfParameter == 10:
            return 'EIA-RH'

        if table2Version == 204 and indicatorOfParameter == 9:
            return 'EFA-RH'

        if table2Version == 204 and indicatorOfParameter == 8:
            return 'EIA-FI'

        if table2Version == 204 and indicatorOfParameter == 7:
            return 'EFA-FI'

        if table2Version == 204 and indicatorOfParameter == 6:
            return 'EIA-V'

        if table2Version == 204 and indicatorOfParameter == 5:
            return 'EFA-V'

        if table2Version == 204 and indicatorOfParameter == 4:
            return 'EIA-U'

        if table2Version == 204 and indicatorOfParameter == 3:
            return 'EFA-U'

        if table2Version == 204 and indicatorOfParameter == 2:
            return 'EIA-PS'

        if table2Version == 204 and indicatorOfParameter == 1:
            return 'EFA-PS'

        if table2Version == 203 and indicatorOfParameter == 204:
            return 'CLCT_MOD'

        if table2Version == 203 and indicatorOfParameter == 203:
            return 'CLDEPTH'

        if table2Version == 203 and indicatorOfParameter == 196:
            return 'ICE_GRD'

        if table2Version == 203 and indicatorOfParameter == 157:
            return 'CEILING'

        if table2Version == 203 and indicatorOfParameter == 154:
            return 'THETAE'

        if table2Version == 203 and indicatorOfParameter == 140:
            return 'KO'

        if table2Version == 203 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 100:
            return 'PTHETA'

        if table2Version == 203 and indicatorOfParameter == 132:
            return 'VP'

        if table2Version == 203 and indicatorOfParameter == 131:
            return 'UP'

        if table2Version == 203 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 100:
            return 'IPV'

        if table2Version == 203 and indicatorOfParameter == 124:
            return 'QVN'

        if table2Version == 203 and indicatorOfParameter == 109:
            return 'WDIV'

        if table2Version == 203 and indicatorOfParameter == 107:
            return 'ADRTG'

        if table2Version == 203 and indicatorOfParameter == 103:
            return 'ADVOR'

        if table2Version == 203 and indicatorOfParameter == 101:
            return 'ADVORG'

        if table2Version == 203 and indicatorOfParameter == 99:
            return 'WW'

        if table2Version == 203 and indicatorOfParameter == 94 and indicatorOfTypeOfLevel == 1:
            return 'CCL_NN'

        if table2Version == 203 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 'CCL_GND'

        if table2Version == 203 and indicatorOfParameter == 90:
            return 'CL_TYP'

        if table2Version == 203 and indicatorOfParameter == 33:
            return 'VABS'

        if table2Version == 203 and indicatorOfParameter == 30:
            return 'SRH'

        if table2Version == 203 and indicatorOfParameter == 29:
            return 'W_SHAER'

        if table2Version == 202 and indicatorOfParameter == 248:
            return 'UVI_MAX_CL'

        if table2Version == 202 and indicatorOfParameter == 233:
            return 'VDIS_SSO'

        if table2Version == 202 and indicatorOfParameter == 233 and timeRangeIndicator == 1:
            return 'AVDIS_SSO'

        if table2Version == 202 and indicatorOfParameter == 232:
            return 'VSTR_SSO'

        if table2Version == 202 and indicatorOfParameter == 232 and timeRangeIndicator == 3:
            return 'AVSTR_SSO'

        if table2Version == 202 and indicatorOfParameter == 231:
            return 'USTR_SSO'

        if table2Version == 202 and indicatorOfParameter == 231 and timeRangeIndicator == 3:
            return 'AUSTR_SSO'

        if table2Version == 202 and indicatorOfParameter == 229:
            return 'Ba-140w'

        if table2Version == 202 and indicatorOfParameter == 228:
            return 'Ba-140d'

        if table2Version == 202 and indicatorOfParameter == 227:
            return 'Ba-140'

        if table2Version == 202 and indicatorOfParameter == 226:
            return 'I-131ow'

        if table2Version == 202 and indicatorOfParameter == 225:
            return 'I-131od'

        if table2Version == 202 and indicatorOfParameter == 224:
            return 'I-131o'

        if table2Version == 202 and indicatorOfParameter == 223:
            return 'I-131gw'

        if table2Version == 202 and indicatorOfParameter == 222:
            return 'I-131gd'

        if table2Version == 202 and indicatorOfParameter == 221:
            return 'I-131g'

        if table2Version == 202 and indicatorOfParameter == 220:
            return 'Xe-133w'

        if table2Version == 202 and indicatorOfParameter == 219:
            return 'Xe-133d'

        if table2Version == 202 and indicatorOfParameter == 218:
            return 'Xe-133'

        if table2Version == 202 and indicatorOfParameter == 217:
            return 'Tr-2w'

        if table2Version == 202 and indicatorOfParameter == 216:
            return 'Tr-2d'

        if table2Version == 202 and indicatorOfParameter == 215:
            return 'Tr-2'

        if table2Version == 202 and indicatorOfParameter == 214:
            return 'Kr-85w'

        if table2Version == 202 and indicatorOfParameter == 213:
            return 'Kr-85d'

        if table2Version == 202 and indicatorOfParameter == 212:
            return 'Kr-85'

        if table2Version == 202 and indicatorOfParameter == 211:
            return 'Zr-95w'

        if table2Version == 202 and indicatorOfParameter == 210:
            return 'Zr-95d'

        if table2Version == 202 and indicatorOfParameter == 209:
            return 'Zr-95'

        if table2Version == 202 and indicatorOfParameter == 208:
            return 'Te-132w'

        if table2Version == 202 and indicatorOfParameter == 207:
            return 'Te-132d'

        if table2Version == 202 and indicatorOfParameter == 206:
            return 'Te-132'

        if table2Version == 202 and indicatorOfParameter == 205:
            return 'Cs-137w'

        if table2Version == 202 and indicatorOfParameter == 204:
            return 'Cs-137d'

        if table2Version == 202 and indicatorOfParameter == 203:
            return 'Cs-137'

        if table2Version == 202 and indicatorOfParameter == 202:
            return 'I-131aw'

        if table2Version == 202 and indicatorOfParameter == 201:
            return 'I-131ad'

        if table2Version == 202 and indicatorOfParameter == 200:
            return 'I-131a'

        if table2Version == 202 and indicatorOfParameter == 199:
            return 'Sr-90w'

        if table2Version == 202 and indicatorOfParameter == 198:
            return 'Sr-90d'

        if table2Version == 202 and indicatorOfParameter == 197:
            return 'Sr-90'

        if table2Version == 202 and indicatorOfParameter == 196:
            return 'Ru-103w'

        if table2Version == 202 and indicatorOfParameter == 195:
            return 'Ru-103d'

        if table2Version == 202 and indicatorOfParameter == 194:
            return 'Ru-103'

        if table2Version == 202 and indicatorOfParameter == 180:
            return 'O3'

        if table2Version == 202 and indicatorOfParameter == 123:
            return 'ZHD'

        if table2Version == 202 and indicatorOfParameter == 122:
            return 'ZWD'

        if table2Version == 202 and indicatorOfParameter == 121:
            return 'ZTD'

        if table2Version == 202 and indicatorOfParameter == 115:
            return 'RLON'

        if table2Version == 202 and indicatorOfParameter == 114:
            return 'RLAT'

        if table2Version == 202 and indicatorOfParameter == 113:
            return 'FC'

        if table2Version == 202 and indicatorOfParameter == 105:
            return 'QVSFLX'

        if table2Version == 202 and indicatorOfParameter == 104:
            return 'DQVDT'

        if table2Version == 202 and indicatorOfParameter == 93 and timeRangeIndicator == 3:
            return 'AER_SS12'

        if table2Version == 202 and indicatorOfParameter == 93:
            return 'AER_SS'

        if table2Version == 202 and indicatorOfParameter == 92 and timeRangeIndicator == 3:
            return 'AER_BC12'

        if table2Version == 202 and indicatorOfParameter == 92:
            return 'AER_BC'

        if table2Version == 202 and indicatorOfParameter == 91 and timeRangeIndicator == 3:
            return 'AER_ORG12'

        if table2Version == 202 and indicatorOfParameter == 91:
            return 'AER_ORG'

        if table2Version == 202 and indicatorOfParameter == 86 and timeRangeIndicator == 3:
            return 'AER_DUST12'

        if table2Version == 202 and indicatorOfParameter == 86:
            return 'AER_DUST'

        if table2Version == 202 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 'AER_SO412'

        if table2Version == 202 and indicatorOfParameter == 84:
            return 'AER_SO4'

        if table2Version == 202 and indicatorOfParameter == 79 and timeRangeIndicator == 0:
            return 'NDVIRATIO'

        if table2Version == 202 and indicatorOfParameter == 79 and timeRangeIndicator == 3:
            return 'NDVI_MRAT'

        if table2Version == 202 and indicatorOfParameter == 78 and timeRangeIndicator == 0:
            return 'NDVI_MAX'

        if table2Version == 202 and indicatorOfParameter == 77 and timeRangeIndicator == 3:
            return 'NDVI'

        if table2Version == 202 and indicatorOfParameter == 76:
            return 'FOR_D'

        if table2Version == 202 and indicatorOfParameter == 75:
            return 'FOR_E'

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 2 and indicatorOfTypeOfLevel == 112:
            return 'WVAR2'

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 1 and indicatorOfTypeOfLevel == 112 and topLevel == 0:
            return 'WVAR1'

        if table2Version == 202 and indicatorOfParameter == 71:
            return 'ORO_MOD'

        if table2Version == 202 and indicatorOfParameter == 70:
            return 'LAI_MN'

        if table2Version == 202 and indicatorOfParameter == 69:
            return 'LAI_MX'

        if table2Version == 202 and indicatorOfParameter == 68:
            return 'PLCOV_MN'

        if table2Version == 202 and indicatorOfParameter == 67:
            return 'PLCOV_MX'

        if table2Version == 202 and indicatorOfParameter == 65:
            return 'VIO3'

        if table2Version == 202 and indicatorOfParameter == 64:
            return 'HMO3'

        if table2Version == 202 and indicatorOfParameter == 62:
            return 'ROOTDP'

        if table2Version == 202 and indicatorOfParameter == 61:
            return 'LAI'

        if table2Version == 202 and indicatorOfParameter == 57:
            return 'SOILTYP'

        if table2Version == 202 and indicatorOfParameter == 56:
            return 'EMIS_RAD'

        if table2Version == 202 and indicatorOfParameter == 49:
            return 'SSO_SIGMA'

        if table2Version == 202 and indicatorOfParameter == 48:
            return 'SSO_THETA'

        if table2Version == 202 and indicatorOfParameter == 47:
            return 'SSO_GAMMA'

        if table2Version == 202 and indicatorOfParameter == 46:
            return 'SSO_STDH'

        if table2Version == 202 and indicatorOfParameter == 45:
            return 'DV_SSO'

        if table2Version == 202 and indicatorOfParameter == 44:
            return 'DU_SSO'

        if table2Version == 202 and indicatorOfParameter == 42:
            return 'ANA_ERR_V'

        if table2Version == 202 and indicatorOfParameter == 41:
            return 'ANA_ERR_U'

        if table2Version == 202 and indicatorOfParameter == 40:
            return 'ANA_ERR_FI'

        if table2Version == 202 and indicatorOfParameter == 19:
            return 'SPRD'

        if table2Version == 202 and indicatorOfParameter == 18:
            return 'TM02'

        if table2Version == 202 and indicatorOfParameter == 17:
            return 'TM01'

        if table2Version == 202 and indicatorOfParameter == 10:
            return 'TM10'

        if table2Version == 202 and indicatorOfParameter == 9:
            return 'PP1D'

        if table2Version == 202 and indicatorOfParameter == 8:
            return 'PPWW'

        if table2Version == 202 and indicatorOfParameter == 7:
            return 'PPTS'

        if table2Version == 202 and indicatorOfParameter == 4:
            return 'MWD'

        if table2Version == 201 and indicatorOfParameter == 243:
            return 'QCVG_CON'

        if table2Version == 201 and indicatorOfParameter == 241:
            return 'CAPE_CON'

        if table2Version == 201 and indicatorOfParameter == 240 and indicatorOfTypeOfLevel == 1:
            return 'MFLX_CON'

        if table2Version == 201 and indicatorOfParameter == 239:
            return 'RESID_WSO'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'TOTFORCE_S'

        if table2Version == 201 and indicatorOfParameter == 237:
            return 'TRA_SUM'

        if table2Version == 201 and indicatorOfParameter == 236:
            return 'EVATRA_SUM'

        if table2Version == 201 and indicatorOfParameter == 233:
            return 'SOTR_RAD'

        if table2Version == 201 and indicatorOfParameter == 232:
            return 'DTTDIV'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200:
            return 'DBZ_CMAX'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 110:
            return 'DBZ'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 1:
            return 'DBZ_850'

        if table2Version == 201 and indicatorOfParameter == 215:
            return 'T_ICE'

        if table2Version == 201 and indicatorOfParameter == 212:
            return 'RSMIN'

        if table2Version == 201 and indicatorOfParameter == 203:
            return 'T_SNOW'

        if table2Version == 201 and indicatorOfParameter == 200:
            return 'W_I'

        if table2Version == 201 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 111:
            return 'W_SO_ICE'

        if table2Version == 201 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 111:
            return 'W_SO'

        if table2Version == 201 and indicatorOfParameter == 197 and indicatorOfTypeOfLevel == 111:
            return 'T_SO'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'VMAX_10M'

        if table2Version == 201 and indicatorOfParameter == 173:
            return 'MH'

        if table2Version == 201 and indicatorOfParameter == 171:
            return 'TCH'

        if table2Version == 201 and indicatorOfParameter == 170:
            return 'TCM'

        if table2Version == 201 and indicatorOfParameter == 154:
            return 'TKVH'

        if table2Version == 201 and indicatorOfParameter == 153:
            return 'TKVM'

        if table2Version == 201 and indicatorOfParameter == 152:
            return 'TKE'

        if table2Version == 201 and indicatorOfParameter == 149:
            return 'KE'

        if table2Version == 201 and indicatorOfParameter == 148:
            return 'TKETENS'

        if table2Version == 201 and indicatorOfParameter == 147:
            return 'TKE_CON'

        if table2Version == 201 and indicatorOfParameter == 146 and indicatorOfTypeOfLevel == 1:
            return 'CIN_ML'

        if table2Version == 201 and indicatorOfParameter == 145 and indicatorOfTypeOfLevel == 1:
            return 'CAPE_ML'

        if table2Version == 201 and indicatorOfParameter == 144 and indicatorOfTypeOfLevel == 1:
            return 'CIN_MU'

        if table2Version == 201 and indicatorOfParameter == 143 and indicatorOfTypeOfLevel == 1:
            return 'CAPE_MU'

        if table2Version == 201 and indicatorOfParameter == 142:
            return 'SDI_2'

        if table2Version == 201 and indicatorOfParameter == 141:
            return 'SDI_1'

        if table2Version == 201 and indicatorOfParameter == 139:
            return 'PP'

        if table2Version == 201 and indicatorOfParameter == 133:
            return 'RHO_SNOW'

        if table2Version == 201 and indicatorOfParameter == 132:
            return 'GRAU_GSP'

        if table2Version == 201 and indicatorOfParameter == 131:
            return 'PRG_GSP'

        if table2Version == 201 and indicatorOfParameter == 130:
            return 'DQI_GSP'

        if table2Version == 201 and indicatorOfParameter == 129:
            return 'FRESHSNW'

        if table2Version == 201 and indicatorOfParameter == 127:
            return 'DQC_GSP'

        if table2Version == 201 and indicatorOfParameter == 125:
            return 'DQV_GSP'

        if table2Version == 201 and indicatorOfParameter == 124:
            return 'DT_GSP'

        if table2Version == 201 and indicatorOfParameter == 123:
            return 'TOT_SNOW'

        if table2Version == 201 and indicatorOfParameter == 122:
            return 'TOT_RAIN'

        if table2Version == 201 and indicatorOfParameter == 113:
            return 'RAIN_CON'

        if table2Version == 201 and indicatorOfParameter == 112:
            return 'PRS_CON'

        if table2Version == 201 and indicatorOfParameter == 111:
            return 'PRR_CON'

        if table2Version == 201 and indicatorOfParameter == 102:
            return 'RAIN_GSP'

        if table2Version == 201 and indicatorOfParameter == 101:
            return 'PRS_GSP'

        if table2Version == 201 and indicatorOfParameter == 100:
            return 'PRR_GSP'

        if table2Version == 201 and indicatorOfParameter == 99:
            return 'Q_SEDIM'

        if table2Version == 201 and indicatorOfParameter == 89:
            return 'DQI_CON'

        if table2Version == 201 and indicatorOfParameter == 88:
            return 'DQC_CON'

        if table2Version == 201 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 4:
            return 'SNOWLMT'

        if table2Version == 201 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 4:
            return 'HZEROCL'

        if table2Version == 201 and indicatorOfParameter == 82 and indicatorOfTypeOfLevel == 1:
            return 'HTOP_DC'

        if table2Version == 201 and indicatorOfParameter == 79:
            return 'DV_CON'

        if table2Version == 201 and indicatorOfParameter == 78:
            return 'DU_CON'

        if table2Version == 201 and indicatorOfParameter == 75:
            return 'DQV_CON'

        if table2Version == 201 and indicatorOfParameter == 74:
            return 'DT_CON'

        if table2Version == 201 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'TOP_CON'

        if table2Version == 201 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1:
            return 'BAS_CON'

        if table2Version == 201 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 3:
            return 'HTOP_CON'

        if table2Version == 201 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 2:
            return 'HBAS_CON'

        if table2Version == 201 and indicatorOfParameter == 61:
            return 'CLW_CON'

        if table2Version == 201 and indicatorOfParameter == 59 and indicatorOfTypeOfLevel == 3:
            return 'HTOP_SC'

        if table2Version == 201 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 2:
            return 'HBAS_SC'

        if table2Version == 201 and indicatorOfParameter == 53:
            return 'CLCL_8'

        if table2Version == 201 and indicatorOfParameter == 52:
            return 'CLCM_8'

        if table2Version == 201 and indicatorOfParameter == 51:
            return 'CLCH_8'

        if table2Version == 201 and indicatorOfParameter == 44:
            return 'QI_RAD'

        if table2Version == 201 and indicatorOfParameter == 43:
            return 'QC_RAD'

        if table2Version == 201 and indicatorOfParameter == 42:
            return 'TDIV_HUM'

        if table2Version == 201 and indicatorOfParameter == 41:
            return 'TWATER'

        if table2Version == 201 and indicatorOfParameter == 40:
            return 'TQG'

        if table2Version == 201 and indicatorOfParameter == 39:
            return 'QG'

        if table2Version == 201 and indicatorOfParameter == 38:
            return 'TQS'

        if table2Version == 201 and indicatorOfParameter == 37:
            return 'TQR'

        if table2Version == 201 and indicatorOfParameter == 36:
            return 'QS'

        if table2Version == 201 and indicatorOfParameter == 35:
            return 'QR'

        if table2Version == 201 and indicatorOfParameter == 33:
            return 'QI'

        if table2Version == 201 and indicatorOfParameter == 31:
            return 'QC'

        if table2Version == 201 and indicatorOfParameter == 30:
            return 'CLC_SGS'

        if table2Version == 201 and indicatorOfParameter == 29:
            return 'CLC'

        if table2Version == 201 and indicatorOfParameter == 21 and timeRangeIndicator == 0:
            return 'RSTOM'

        if table2Version == 201 and indicatorOfParameter == 20 and timeRangeIndicator == 4:
            return 'SUNSHHRS'

        if table2Version == 201 and indicatorOfParameter == 19 and indicatorOfTypeOfLevel == 111 and timeRangeIndicator == 3:
            return 'ALHFL_PL'

        if table2Version == 201 and indicatorOfParameter == 18 and timeRangeIndicator == 3:
            return 'ALHFL_BS'

        if table2Version == 201 and indicatorOfParameter == 14:
            return 'THHR_RAD'

        if table2Version == 201 and indicatorOfParameter == 13:
            return 'SOHR_RAD'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1:
            return 'PABS_RAD'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'APAB_S'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'AVMFL_S'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'AUMFL_S'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'ASHFL_S'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'ALHFL_S'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8:
            return 'THBT_RAD'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'ATHB_T'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8:
            return 'SOBT_RAD'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'ASOB_T'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1:
            return 'THBS_RAD'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'ATHB_S'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1:
            return 'SOBS_RAD'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'ASOB_S'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 'MPTS'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'SHTS'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'MDTS'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 'MPWW'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'SHWW'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'MDWW'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'SWH'

        if table2Version == 2 and indicatorOfParameter == 92:
            return 'H_ICE'

        if table2Version == 2 and indicatorOfParameter == 91:
            return 'FR_ICE'

        if table2Version == 2 and indicatorOfParameter == 90 and topLevel == 0:
            return 'RUNOFF_S'

        if table2Version == 2 and indicatorOfParameter == 90 and topLevel == 10:
            return 'RUNOFF_G'

        if table2Version == 2 and indicatorOfParameter == 87:
            return 'PLCOV'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and bottomLevel == 100:
            return 'W_G2'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 'W_G1'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 100 and bottomLevel == 190:
            return 'W_CL'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111:
            return 'T_S'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 9:
            return 'T_M'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 41:
            return 'T_CL_LM'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 36:
            return 'T_CL'

        if table2Version == 2 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 'ALBEDO_B'

        if table2Version == 2 and indicatorOfParameter == 84:
            return 'ALB_RAD'

        if table2Version == 2 and indicatorOfParameter == 83:
            return 'Z0'

        if table2Version == 2 and indicatorOfParameter == 81:
            return 'FR_LAND'

        if table2Version == 2 and indicatorOfParameter == 79:
            return 'SNOW_GSP'

        if table2Version == 2 and indicatorOfParameter == 78:
            return 'SNOW_CON'

        if table2Version == 2 and indicatorOfParameter == 76:
            return 'TQC'

        if table2Version == 2 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'CLCH'

        if table2Version == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 'CLCM'

        if table2Version == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'CLCL'

        if table2Version == 2 and indicatorOfParameter == 72:
            return 'CLC_CON'

        if table2Version == 2 and indicatorOfParameter == 71:
            return 'CLCT'

        if table2Version == 2 and indicatorOfParameter == 66:
            return 'H_SNOW'

        if table2Version == 2 and indicatorOfParameter == 65:
            return 'W_SNOW'

        if table2Version == 2 and indicatorOfParameter == 63 and timeRangeIndicator == 4:
            return 'PREC_CON'

        if table2Version == 2 and indicatorOfParameter == 62 and timeRangeIndicator == 4:
            return 'PREC_GSP'

        if table2Version == 2 and indicatorOfParameter == 61:
            return 'TOT_PREC'

        if table2Version == 2 and indicatorOfParameter == 58:
            return 'TQI'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1:
            return 'AEVAP_S'

        if table2Version == 2 and indicatorOfParameter == 54:
            return 'TQV'

        if table2Version == 2 and indicatorOfParameter == 52:
            return 'RELHUM'

        if table2Version == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'RELHUM_2M'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'QV'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'QV_2M'

        if table2Version == 2 and indicatorOfParameter == 40:
            return 'W'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'OMEGA'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'V'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'V_10M'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'U'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'U_10M'

        if table2Version == 2 and indicatorOfParameter == 32:
            return 'SP'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'SP_10M'

        if table2Version == 2 and indicatorOfParameter == 31:
            return 'DD'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'DD_10M'

        if table2Version == 2 and indicatorOfParameter == 30:
            return 'WVSP3'

        if table2Version == 2 and indicatorOfParameter == 29:
            return 'WVSP2'

        if table2Version == 2 and indicatorOfParameter == 28:
            return 'WVSP1'

        if table2Version == 2 and indicatorOfParameter == 21:
            return 'DBZ_MAX'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 'TD_2M_AV'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'TD_2M'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'TMIN_2M'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'TMAX_2M'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 'T'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 'T_2M_CL'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 'T_2M_AV'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'T_2M'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 'T_G'

        if table2Version == 2 and indicatorOfParameter == 10:
            return 'TO3'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 109:
            return 'HHL'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 1:
            return 'HSURF'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'FI'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 110:
            return 'FIF'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 1:
            return 'FIS'

        if table2Version == 2 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 1:
            return 'DPSDT'

        if table2Version == 2 and indicatorOfParameter == 2:
            return 'PMSL'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'P'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'PS'

    return wrapped
