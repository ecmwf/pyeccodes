import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 207 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'vmax_10m_c'

        if table2Version == 207 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 'snow_gsp_c'

        if table2Version == 207 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 'tot_prec_c'

        if table2Version == 206 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'vmax_10m_s'

        if table2Version == 206 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 't_s_s'

        if table2Version == 206 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 'snow_gsp_s'

        if table2Version == 206 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'clch_s'

        if table2Version == 206 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 'clcm_s'

        if table2Version == 206 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'clcl_s'

        if table2Version == 206 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1:
            return 'clct_s'

        if table2Version == 206 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 'tot_prec_s'

        if table2Version == 206 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'v_10m_s'

        if table2Version == 206 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'u_10m_s'

        if table2Version == 206 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'td_2m_s'

        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if table2Version == 206 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'tmin_2m_s'

        if table2Version == 206 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'tmax_2m_s'

        if table2Version == 206 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 't_2m_s'

        localElementNumber = h.get_l('localElementNumber')

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 4:
            return 'synmsg_rad_cs_wv7.3'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 4:
            return 'synmsg_rad_cs_wv6.2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 4:
            return 'synmsg_rad_cs_ir9.7'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 4:
            return 'synmsg_rad_cs_ir8.7'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 4:
            return 'synmsg_rad_cs_ir3.9'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 4:
            return 'synmsg_rad_cs_ir13.4'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 4:
            return 'synmsg_rad_cs_ir12.1'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 4:
            return 'synmsg_rad_cs_ir10.8'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 3:
            return 'synmsg_rad_cl_wv7.3'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 3:
            return 'synmsg_rad_cl_wv6.2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 3:
            return 'synmsg_rad_cl_ir9.7'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 3:
            return 'synmsg_rad_cl_ir8.7'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 3:
            return 'synmsg_rad_cl_ir3.9'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 3:
            return 'synmsg_rad_cl_ir13.4'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 3:
            return 'synmsg_rad_cl_ir12.1'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 3:
            return 'synmsg_rad_cl_ir10.8'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 2:
            return 'synmsg_bt_cs_wv7.3'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 2:
            return 'synmsg_bt_cs_wv6.2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 2:
            return 'synmsg_bt_cs_ir9.7'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 2:
            return 'synmsg_bt_cs_ir3.9'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 2:
            return 'synmsg_bt_cs_ir13.4'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 2:
            return 'synmsg_bt_cs_ir12.1'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 2:
            return 'synmsg_bt_cs_ir10.8'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 2:
            return 'synmsg_bt_cs_ir8.7'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 1:
            return 'synmsg_bt_cl_wv7.3'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 1:
            return 'synmsg_bt_cl_wv6.2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 1:
            return 'synmsg_bt_cl_ir9.7'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 1:
            return 'synmsg_bt_cl_ir8.7'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 1:
            return 'synmsg_bt_cl_ir3.9'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 1:
            return 'synmsg_bt_cl_ir13.4'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 1:
            return 'synmsg_bt_cl_ir12.1'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 1:
            return 'synmsg_bt_cl_ir10.8'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 4:
            return 'synme7_rad_cs_wv6.4'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 4:
            return 'synme7_rad_cs_ir11.5'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 3:
            return 'synme7_rad_cl_wv6.4'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 3:
            return 'synme7_rad_cl_ir11.5'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 2:
            return 'synme7_bt_cs_wv6.4'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 2:
            return 'synme7_bt_cs_ir11.5'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 1:
            return 'synme7_bt_cl_wv6.4'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 1:
            return 'synme7_bt_cl_ir11.5'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 4:
            return 'synme6_rad_cs'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 3:
            return 'synme6_rad_cl'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 2:
            return 'synme6_bt_cs'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 1:
            return 'synme6_bt_cl'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 4:
            return 'synme5_rad_cs'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 3:
            return 'synme5_rad_cl'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 2:
            return 'synme5_bt_cs'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 1:
            return 'synme5_bt_cl'

        if table2Version == 204 and indicatorOfParameter == 16:
            return 'eia-ke'

        if table2Version == 204 and indicatorOfParameter == 15:
            return 'efa-ke'

        if table2Version == 204 and indicatorOfParameter == 14:
            return 'eia-om'

        if table2Version == 204 and indicatorOfParameter == 13:
            return 'efa-om'

        if table2Version == 204 and indicatorOfParameter == 12:
            return 'eia-t'

        if table2Version == 204 and indicatorOfParameter == 11:
            return 'efa-t'

        if table2Version == 204 and indicatorOfParameter == 10:
            return 'eia-rh'

        if table2Version == 204 and indicatorOfParameter == 9:
            return 'efa-rh'

        if table2Version == 204 and indicatorOfParameter == 8:
            return 'eia-fi'

        if table2Version == 204 and indicatorOfParameter == 7:
            return 'efa-fi'

        if table2Version == 204 and indicatorOfParameter == 6:
            return 'eia-v'

        if table2Version == 204 and indicatorOfParameter == 5:
            return 'efa-v'

        if table2Version == 204 and indicatorOfParameter == 4:
            return 'eia-u'

        if table2Version == 204 and indicatorOfParameter == 3:
            return 'efa-u'

        if table2Version == 204 and indicatorOfParameter == 2:
            return 'eia-ps'

        if table2Version == 204 and indicatorOfParameter == 1:
            return 'efa-ps'

        if table2Version == 203 and indicatorOfParameter == 204 and indicatorOfTypeOfLevel == 1:
            return 'clct_mod'

        if table2Version == 203 and indicatorOfParameter == 203 and indicatorOfTypeOfLevel == 1:
            return 'cldepth'

        if table2Version == 203 and indicatorOfParameter == 196 and indicatorOfTypeOfLevel == 100:
            return 'ice_grd'

        if table2Version == 203 and indicatorOfParameter == 157 and indicatorOfTypeOfLevel == 1:
            return 'ceiling'

        if table2Version == 203 and indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 100:
            return 'thetae'

        if table2Version == 203 and indicatorOfParameter == 140 and indicatorOfTypeOfLevel == 1:
            return 'ko'

        if table2Version == 203 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 100:
            return 'ptheta'

        if table2Version == 203 and indicatorOfParameter == 132 and indicatorOfTypeOfLevel == 100:
            return 'vp'

        if table2Version == 203 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 100:
            return 'up'

        if table2Version == 203 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 100:
            return 'ipv'

        if table2Version == 203 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 100:
            return 'fqn'

        if table2Version == 203 and indicatorOfParameter == 109 and indicatorOfTypeOfLevel == 100:
            return 'wdiv'

        if table2Version == 203 and indicatorOfParameter == 107 and indicatorOfTypeOfLevel == 101:
            return 'adrtg'

        if table2Version == 203 and indicatorOfParameter == 103 and indicatorOfTypeOfLevel == 101:
            return 'advor'

        if table2Version == 203 and indicatorOfParameter == 101 and indicatorOfTypeOfLevel == 100:
            return 'advorg'

        if table2Version == 203 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 1:
            return 'ww'

        if table2Version == 203 and indicatorOfParameter == 94 and indicatorOfTypeOfLevel == 1:
            return 'ccl_nn'

        if table2Version == 203 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 'ccl_gnd'

        if table2Version == 203 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 1:
            return 'cl_typ'

        if table2Version == 203 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 100:
            return 'vabs'

        if table2Version == 203 and indicatorOfParameter == 30 and indicatorOfTypeOfLevel == 110:
            return 'srh'

        if table2Version == 203 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 110:
            return 'w_shaer'

        if table2Version == 202 and indicatorOfParameter == 248 and indicatorOfTypeOfLevel == 1:
            return 'uv_max'

        if table2Version == 202 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'vdis_sso'

        if table2Version == 202 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'avdis_sso'

        if table2Version == 202 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'vstr_sso'

        if table2Version == 202 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'avstr_sso'

        if table2Version == 202 and indicatorOfParameter == 231 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'ustr_sso'

        if table2Version == 202 and indicatorOfParameter == 231 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'austr_sso'

        if table2Version == 202 and indicatorOfParameter == 229 and indicatorOfTypeOfLevel == 1:
            return 'ba-140w'

        if table2Version == 202 and indicatorOfParameter == 228 and indicatorOfTypeOfLevel == 1:
            return 'ba-140d'

        if table2Version == 202 and indicatorOfParameter == 227:
            return 'ba-140'

        if table2Version == 202 and indicatorOfParameter == 226 and indicatorOfTypeOfLevel == 1:
            return 'i-131ow'

        if table2Version == 202 and indicatorOfParameter == 225 and indicatorOfTypeOfLevel == 1:
            return 'i-131od'

        if table2Version == 202 and indicatorOfParameter == 224:
            return 'i-131o'

        if table2Version == 202 and indicatorOfParameter == 223 and indicatorOfTypeOfLevel == 1:
            return 'i-131gw'

        if table2Version == 202 and indicatorOfParameter == 222 and indicatorOfTypeOfLevel == 1:
            return 'i-131gd'

        if table2Version == 202 and indicatorOfParameter == 221:
            return 'i-131g'

        if table2Version == 202 and indicatorOfParameter == 220 and indicatorOfTypeOfLevel == 1:
            return 'xe-133w'

        if table2Version == 202 and indicatorOfParameter == 219 and indicatorOfTypeOfLevel == 1:
            return 'xe-133d'

        if table2Version == 202 and indicatorOfParameter == 218:
            return 'xe-133'

        if table2Version == 202 and indicatorOfParameter == 217 and indicatorOfTypeOfLevel == 1:
            return 'tr-2w'

        if table2Version == 202 and indicatorOfParameter == 216 and indicatorOfTypeOfLevel == 1:
            return 'tr-2d'

        if table2Version == 202 and indicatorOfParameter == 215:
            return 'tr-2'

        if table2Version == 202 and indicatorOfParameter == 214 and indicatorOfTypeOfLevel == 1:
            return 'kr-85w'

        if table2Version == 202 and indicatorOfParameter == 213 and indicatorOfTypeOfLevel == 1:
            return 'kr-85d'

        if table2Version == 202 and indicatorOfParameter == 212:
            return 'kr-85'

        if table2Version == 202 and indicatorOfParameter == 211 and indicatorOfTypeOfLevel == 1:
            return 'zr-95w'

        if table2Version == 202 and indicatorOfParameter == 210 and indicatorOfTypeOfLevel == 1:
            return 'zr-95d'

        if table2Version == 202 and indicatorOfParameter == 209:
            return 'zr-95'

        if table2Version == 202 and indicatorOfParameter == 208 and indicatorOfTypeOfLevel == 1:
            return 'te-132w'

        if table2Version == 202 and indicatorOfParameter == 207 and indicatorOfTypeOfLevel == 1:
            return 'te-132d'

        if table2Version == 202 and indicatorOfParameter == 206:
            return 'te-132'

        if table2Version == 202 and indicatorOfParameter == 205 and indicatorOfTypeOfLevel == 1:
            return 'cs-137w'

        if table2Version == 202 and indicatorOfParameter == 204 and indicatorOfTypeOfLevel == 1:
            return 'cs-137d'

        if table2Version == 202 and indicatorOfParameter == 203:
            return 'cs-137'

        if table2Version == 202 and indicatorOfParameter == 202 and indicatorOfTypeOfLevel == 1:
            return 'i-131aw'

        if table2Version == 202 and indicatorOfParameter == 201 and indicatorOfTypeOfLevel == 1:
            return 'i-131ad'

        if table2Version == 202 and indicatorOfParameter == 200:
            return 'i-131a'

        if table2Version == 202 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 1:
            return 'sr-90w'

        if table2Version == 202 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 1:
            return 'sr-90d'

        if table2Version == 202 and indicatorOfParameter == 197:
            return 'sr-90'

        if table2Version == 202 and indicatorOfParameter == 196 and indicatorOfTypeOfLevel == 1:
            return 'ru-103w'

        if table2Version == 202 and indicatorOfParameter == 195 and indicatorOfTypeOfLevel == 1:
            return 'ru-103d'

        if table2Version == 202 and indicatorOfParameter == 194:
            return 'ru-103'

        if table2Version == 202 and indicatorOfParameter == 180 and indicatorOfTypeOfLevel == 110:
            return 'o3'

        if table2Version == 202 and indicatorOfParameter == 123 and indicatorOfTypeOfLevel == 1:
            return 'zhd'

        if table2Version == 202 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 'zwd'

        if table2Version == 202 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1:
            return 'ztd'

        if table2Version == 202 and indicatorOfParameter == 120 and indicatorOfTypeOfLevel == 110:
            return 'ustr'

        if table2Version == 202 and indicatorOfParameter == 115 and indicatorOfTypeOfLevel == 1:
            return 'rlon'

        if table2Version == 202 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 1:
            return 'rlat'

        if table2Version == 202 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 1:
            return 'fc'

        if table2Version == 202 and indicatorOfParameter == 105 and indicatorOfTypeOfLevel == 1:
            return 'qvsflx'

        if table2Version == 202 and indicatorOfParameter == 104 and indicatorOfTypeOfLevel == 110:
            return 'dqvdt'

        if table2Version == 202 and indicatorOfParameter == 93 and timeRangeIndicator == 3:
            return 'aer_ss12'

        if table2Version == 202 and indicatorOfParameter == 93:
            return 'aer_ss'

        if table2Version == 202 and indicatorOfParameter == 92 and timeRangeIndicator == 3:
            return 'aer_bc12'

        if table2Version == 202 and indicatorOfParameter == 92:
            return 'aer_bc'

        if table2Version == 202 and indicatorOfParameter == 91 and timeRangeIndicator == 3:
            return 'aer_org12'

        if table2Version == 202 and indicatorOfParameter == 91:
            return 'aer_org'

        if table2Version == 202 and indicatorOfParameter == 86 and timeRangeIndicator == 3:
            return 'aer_dust12'

        if table2Version == 202 and indicatorOfParameter == 86:
            return 'aer_dust'

        if table2Version == 202 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 'aer_so412'

        if table2Version == 202 and indicatorOfParameter == 84:
            return 'aer_so4'

        if table2Version == 202 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'ndviratio'

        if table2Version == 202 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 'ndvi_mrat'

        if table2Version == 202 and indicatorOfParameter == 78 and timeRangeIndicator == 3:
            return 'ndvi_max'

        if table2Version == 202 and indicatorOfParameter == 77 and timeRangeIndicator == 3:
            return 'ndvi'

        if table2Version == 202 and indicatorOfParameter == 76 and indicatorOfTypeOfLevel == 1:
            return 'for_d'

        if table2Version == 202 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'for_e'

        bottomLevel = h.get_l('bottomLevel')
        topLevel = h.get_l('topLevel')

        if table2Version == 202 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 112 and bottomLevel == 100 and topLevel == 10:
            return 'wvar2'

        if table2Version == 202 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 'wvar1'

        if table2Version == 202 and indicatorOfParameter == 71:
            return 'oro_mod'

        if table2Version == 202 and indicatorOfParameter == 70 and indicatorOfTypeOfLevel == 1:
            return 'lai_mn'

        if table2Version == 202 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 1:
            return 'lai_mx'

        if table2Version == 202 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 1:
            return 'plcov_mn'

        if table2Version == 202 and indicatorOfParameter == 67 and indicatorOfTypeOfLevel == 1:
            return 'plcov_mx'

        if table2Version == 202 and indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1:
            return 'vio3'

        if table2Version == 202 and indicatorOfParameter == 64 and indicatorOfTypeOfLevel == 1:
            return 'hmo3'

        if table2Version == 202 and indicatorOfParameter == 62 and indicatorOfTypeOfLevel == 1:
            return 'rootdp'

        if table2Version == 202 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 'lai'

        if table2Version == 202 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1:
            return 'soiltyp'

        if table2Version == 202 and indicatorOfParameter == 56 and indicatorOfTypeOfLevel == 1 and level == 0 and timeRangeIndicator == 0:
            return 'emis_rad'

        if table2Version == 202 and indicatorOfParameter == 49 and indicatorOfTypeOfLevel == 1:
            return 'sso_sigma'

        if table2Version == 202 and indicatorOfParameter == 48 and indicatorOfTypeOfLevel == 1:
            return 'sso_theta'

        if table2Version == 202 and indicatorOfParameter == 47 and indicatorOfTypeOfLevel == 1:
            return 'sso_gamma'

        if table2Version == 202 and indicatorOfParameter == 46 and indicatorOfTypeOfLevel == 1:
            return 'sso_stdh'

        if table2Version == 202 and indicatorOfParameter == 45 and indicatorOfTypeOfLevel == 110:
            return 'dv_sso'

        if table2Version == 202 and indicatorOfParameter == 44 and indicatorOfTypeOfLevel == 110:
            return 'du_sso'

        if table2Version == 202 and indicatorOfParameter == 42 and level == 100:
            return 'ana_err_v'

        if table2Version == 202 and indicatorOfParameter == 41 and indicatorOfTypeOfLevel == 100:
            return 'ana_err_u'

        if table2Version == 202 and indicatorOfParameter == 40 and indicatorOfTypeOfLevel == 100:
            return 'ana_err_fi'

        if table2Version == 202 and indicatorOfParameter == 19:
            return 'sprd'

        if table2Version == 202 and indicatorOfParameter == 18:
            return 'tm02'

        if table2Version == 202 and indicatorOfParameter == 17:
            return 'tm01'

        if table2Version == 202 and indicatorOfParameter == 10:
            return 'tm10'

        if table2Version == 202 and indicatorOfParameter == 9:
            return 'pp1d'

        if table2Version == 202 and indicatorOfParameter == 8:
            return 'ppps'

        if table2Version == 202 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 102:
            return 'mpp_s'

        if table2Version == 202 and indicatorOfParameter == 7:
            return 'ppww'

        if table2Version == 202 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 102:
            return 'mwp_x'

        if table2Version == 202 and indicatorOfParameter == 4:
            return 'mwd'

        if table2Version == 201 and indicatorOfParameter == 243 and indicatorOfTypeOfLevel == 1:
            return 'qcvg_con'

        if table2Version == 201 and indicatorOfParameter == 241 and indicatorOfTypeOfLevel == 1:
            return 'cape_con'

        if table2Version == 201 and indicatorOfParameter == 240 and indicatorOfTypeOfLevel == 1:
            return 'mflx_con'

        if table2Version == 201 and indicatorOfParameter == 239:
            return 'resid_wso'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'totforce_s'

        if table2Version == 201 and indicatorOfParameter == 237:
            return 'tra_sum'

        if table2Version == 201 and indicatorOfParameter == 236:
            return 'evatra_sum'

        if table2Version == 201 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 110:
            return 'sotr_rad'

        if table2Version == 201 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 110:
            return 'dttdiv'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200:
            return 'dbz_cmax'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 110:
            return 'dbz'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 1:
            return 'dbz_850'

        if table2Version == 201 and indicatorOfParameter == 215 and indicatorOfTypeOfLevel == 1:
            return 't_ice'

        if table2Version == 201 and indicatorOfParameter == 212 and indicatorOfTypeOfLevel == 1:
            return 'prs_min'

        if table2Version == 201 and indicatorOfParameter == 203 and indicatorOfTypeOfLevel == 1:
            return 't_snow'

        if table2Version == 201 and indicatorOfParameter == 200 and indicatorOfTypeOfLevel == 1:
            return 'w_i'

        if table2Version == 201 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 111:
            return 'w_so_ice'

        if table2Version == 201 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 111:
            return 'w_so'

        if table2Version == 201 and indicatorOfParameter == 197 and indicatorOfTypeOfLevel == 111:
            return 't_so'

        if table2Version == 201 and indicatorOfParameter == 194 and indicatorOfTypeOfLevel == 100:
            return 'ru-103'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10 and timeRangeIndicator == 2:
            return 'vmax_10m'

        if table2Version == 201 and indicatorOfParameter == 173 and indicatorOfTypeOfLevel == 1:
            return 'mh'

        if table2Version == 201 and indicatorOfParameter == 171 and indicatorOfTypeOfLevel == 1:
            return 'tch'

        if table2Version == 201 and indicatorOfParameter == 170 and indicatorOfTypeOfLevel == 1:
            return 'tcm'

        if table2Version == 201 and indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 109:
            return 'tkvh'

        if table2Version == 201 and indicatorOfParameter == 153 and indicatorOfTypeOfLevel == 109:
            return 'tkvm'

        if table2Version == 201 and indicatorOfParameter == 152 and indicatorOfTypeOfLevel == 109:
            return 'tke'

        if table2Version == 201 and indicatorOfParameter == 149 and indicatorOfTypeOfLevel == 110:
            return 'ke'

        if table2Version == 201 and indicatorOfParameter == 148 and indicatorOfTypeOfLevel == 109:
            return 'tketens'

        if table2Version == 201 and indicatorOfParameter == 147:
            return 'tke_con'

        if table2Version == 201 and indicatorOfParameter == 146 and indicatorOfTypeOfLevel == 1:
            return 'cin_ml'

        if table2Version == 201 and indicatorOfParameter == 145 and indicatorOfTypeOfLevel == 1:
            return 'cape_ml'

        if table2Version == 201 and indicatorOfParameter == 144 and indicatorOfTypeOfLevel == 1:
            return 'cin_mu'

        if table2Version == 201 and indicatorOfParameter == 143 and indicatorOfTypeOfLevel == 1:
            return 'cape_mu'

        if table2Version == 201 and indicatorOfParameter == 142 and indicatorOfTypeOfLevel == 1:
            return 'sdi_2'

        if table2Version == 201 and indicatorOfParameter == 141 and indicatorOfTypeOfLevel == 1:
            return 'sdi_1'

        if table2Version == 201 and indicatorOfParameter == 139 and indicatorOfTypeOfLevel == 110:
            return 'pp'

        if table2Version == 201 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 1:
            return 'rho_snow'

        if table2Version == 201 and indicatorOfParameter == 132 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'grau_gsp'

        if table2Version == 201 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 1:
            return 'prg_gsp'

        if table2Version == 201 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 110:
            return 'dqi_gsp'

        if table2Version == 201 and indicatorOfParameter == 129 and indicatorOfTypeOfLevel == 1:
            return 'freshsnw'

        if table2Version == 201 and indicatorOfParameter == 127 and indicatorOfTypeOfLevel == 110:
            return 'dqc_gsp'

        if table2Version == 201 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 110:
            return 'dqv_gsp'

        if table2Version == 201 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 110:
            return 'dt_gsp'

        if table2Version == 201 and indicatorOfParameter == 123 and indicatorOfTypeOfLevel == 1:
            return 'rr_c'

        if table2Version == 201 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 'rr_f'

        if table2Version == 201 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'rain_con'

        if table2Version == 201 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1:
            return 'prs_con'

        if table2Version == 201 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1:
            return 'prr_con'

        if table2Version == 201 and indicatorOfParameter == 102 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'rain_gsp'

        if table2Version == 201 and indicatorOfParameter == 101 and indicatorOfTypeOfLevel == 1:
            return 'prs_gsp'

        if table2Version == 201 and indicatorOfParameter == 100 and indicatorOfTypeOfLevel == 1:
            return 'prr_gsp'

        if table2Version == 201 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 110:
            return 'q_sedim'

        if table2Version == 201 and indicatorOfParameter == 89 and indicatorOfTypeOfLevel == 110:
            return 'dqi_con'

        if table2Version == 201 and indicatorOfParameter == 88 and indicatorOfTypeOfLevel == 110:
            return 'dqc_con'

        if table2Version == 201 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 4:
            return 'snowlmt'

        if table2Version == 201 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 4:
            return 'hzerocl'

        if table2Version == 201 and indicatorOfParameter == 82 and indicatorOfTypeOfLevel == 1:
            return 'htop_dc'

        if table2Version == 201 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 110:
            return 'dv_con'

        if table2Version == 201 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 110:
            return 'du_con'

        if table2Version == 201 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 110:
            return 'dqv_con'

        if table2Version == 201 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 110:
            return 'dt_con'

        if table2Version == 201 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'top_con'

        if table2Version == 201 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1:
            return 'bas_con'

        if table2Version == 201 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 3:
            return 'htop_con'

        if table2Version == 201 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 2:
            return 'hbas_con'

        if table2Version == 201 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 110:
            return 'clw_con'

        if table2Version == 201 and indicatorOfParameter == 59 and indicatorOfTypeOfLevel == 3:
            return 'htop_sc'

        if table2Version == 201 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 2:
            return 'hbas_sc'

        if table2Version == 201 and indicatorOfParameter == 53:
            return 'clcl_8'

        if table2Version == 201 and indicatorOfParameter == 52:
            return 'clcm_8'

        if table2Version == 201 and indicatorOfParameter == 51:
            return 'clch_8'

        if table2Version == 201 and indicatorOfParameter == 44 and indicatorOfTypeOfLevel == 110:
            return 'qi_rad'

        if table2Version == 201 and indicatorOfParameter == 43 and indicatorOfTypeOfLevel == 110:
            return 'qc_rad'

        if table2Version == 201 and indicatorOfParameter == 42 and indicatorOfTypeOfLevel == 1:
            return 'tdiv_hum'

        if table2Version == 201 and indicatorOfParameter == 41 and indicatorOfTypeOfLevel == 1:
            return 'twater'

        if table2Version == 201 and indicatorOfParameter == 40:
            return 'tqg'

        if table2Version == 201 and indicatorOfParameter == 39 and indicatorOfTypeOfLevel == 110:
            return 'qg'

        if table2Version == 201 and indicatorOfParameter == 38 and indicatorOfTypeOfLevel == 1:
            return 'tqs'

        if table2Version == 201 and indicatorOfParameter == 37 and indicatorOfTypeOfLevel == 1:
            return 'tqr'

        if table2Version == 201 and indicatorOfParameter == 36 and indicatorOfTypeOfLevel == 110:
            return 'qs'

        if table2Version == 201 and indicatorOfParameter == 35 and indicatorOfTypeOfLevel == 110:
            return 'qr'

        if table2Version == 201 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 110:
            return 'qi'

        if table2Version == 201 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 110:
            return 'qc'

        if table2Version == 201 and indicatorOfParameter == 30 and indicatorOfTypeOfLevel == 110:
            return 'clc_sgs'

        if table2Version == 201 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 110:
            return 'clc'

        if table2Version == 201 and indicatorOfParameter == 21 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'rstom'

        if table2Version == 201 and indicatorOfParameter == 20 and timeRangeIndicator == 4:
            return 'dursun'

        if table2Version == 201 and indicatorOfParameter == 19 and indicatorOfTypeOfLevel == 111 and timeRangeIndicator == 3:
            return 'alhfl_pl'

        if table2Version == 201 and indicatorOfParameter == 18 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'alhfl_bs'

        if table2Version == 201 and indicatorOfParameter == 14 and indicatorOfTypeOfLevel == 110:
            return 'thhr_rad'

        if table2Version == 201 and indicatorOfParameter == 13 and indicatorOfTypeOfLevel == 110:
            return 'sohr_rad'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'pabs_rad'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'apab_s'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'avmfl_s'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'aumfl_s'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'ashfl_s'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'alhfl_s'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 0:
            return 'thbt_rad'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'athb_t'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 0:
            return 'sobt_rad'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'asob_t'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'thbs_rad'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'athb_s'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'sobs_rad'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'asob_s'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 'mpps'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'shps'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'mdps'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 'mpww'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'shww'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'mdww'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'swh'

        if table2Version == 2 and indicatorOfParameter == 92 and indicatorOfTypeOfLevel == 1:
            return 'h_ice'

        if table2Version == 2 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 'fr_ice'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and bottomLevel == 10 and topLevel == 0 and timeRangeIndicator == 4:
            return 'runoff_s'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and timeRangeIndicator == 4 and bottomLevel == 190 and topLevel == 10:
            return 'runoff_g_lm'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and timeRangeIndicator == 4 and bottomLevel == 100 and topLevel == 10:
            return 'runoff_g'

        if table2Version == 2 and indicatorOfParameter == 87 and indicatorOfTypeOfLevel == 1:
            return 'plcov'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 100 and topLevel == 10:
            return 'w_g2'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 10 and topLevel == 0:
            return 'w_g1'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 190 and topLevel == 100:
            return 'w_cl'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 't_s'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 9:
            return 't_m'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 41:
            return 't_cl_lm'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 36:
            return 't_cl'

        if table2Version == 2 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'albedo_b'

        if table2Version == 2 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 1:
            return 'alb_rad'

        if table2Version == 2 and indicatorOfParameter == 83 and indicatorOfTypeOfLevel == 1:
            return 'z0'

        if table2Version == 2 and indicatorOfParameter == 81 and indicatorOfTypeOfLevel == 1:
            return 'fr_land'

        if table2Version == 2 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'snow_gsp'

        if table2Version == 2 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'snow_con'

        if table2Version == 2 and indicatorOfParameter == 76 and indicatorOfTypeOfLevel == 1:
            return 'tqc'

        if table2Version == 2 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'clch'

        if table2Version == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 'clcm'

        if table2Version == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'clcl'

        if table2Version == 2 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 110:
            return 'clc_con'

        if table2Version == 2 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1:
            return 'clct'

        if table2Version == 2 and indicatorOfParameter == 66 and indicatorOfTypeOfLevel == 1:
            return 'h_snow'

        if table2Version == 2 and indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1:
            return 'w_snow'

        if table2Version == 2 and indicatorOfParameter == 63 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'prec_con'

        if table2Version == 2 and indicatorOfParameter == 62 and timeRangeIndicator == 4:
            return 'prec_gsp'

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'tot_prec'

        if table2Version == 2 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 1:
            return 'tqi'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'aevap_s'

        if table2Version == 2 and indicatorOfParameter == 54 and indicatorOfTypeOfLevel == 1:
            return 'tqv'

        if table2Version == 2 and indicatorOfParameter == 52:
            return 'relhum'

        if table2Version == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'relhum_2m'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'qv'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'qv_2m'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 1:
            return 'qv_s'

        if table2Version == 2 and indicatorOfParameter == 40:
            return 'w'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'omega'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'v_10m'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'u_10m'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 110:
            return 'sp'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'sp_10m'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 110:
            return 'dd'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'dd_10m'

        if table2Version == 2 and indicatorOfParameter == 30:
            return 'wvsp3'

        if table2Version == 2 and indicatorOfParameter == 29:
            return 'wvsp2'

        if table2Version == 2 and indicatorOfParameter == 28:
            return 'wvsp1'

        if table2Version == 2 and indicatorOfParameter == 21 and indicatorOfTypeOfLevel == 1:
            return 'dbz_max'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return 'td_2m_av'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'td_2m'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'tmin_2m'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'tmax_2m'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return 't_2m_cl'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return 't_2m_av'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 't_g'

        if table2Version == 2 and indicatorOfParameter == 10 and indicatorOfTypeOfLevel == 1:
            return 'to3'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 109:
            return 'hhl'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 1:
            return 'hsurf'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'fi'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 110:
            return 'fif'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 1:
            return 'fis'

        if table2Version == 2 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 1:
            return 'dpsdt'

        if table2Version == 2 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 102:
            return 'pmsl'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'p'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'ps'

    return wrapped
