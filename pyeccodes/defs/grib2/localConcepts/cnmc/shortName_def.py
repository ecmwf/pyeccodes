import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        scaledValueOfCentralWaveNumber = h.get_l('scaledValueOfCentralWaveNumber')
        typeOfGeneratingProcess = h.get_l('typeOfGeneratingProcess')
        satelliteSeries = h.get_l('satelliteSeries')
        satelliteNumber = h.get_l('satelliteNumber')
        instrumentType = h.get_l('instrumentType')

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfCentralWaveNumber == 136986 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 'obsmsg_bt_wv7.3'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'obsmsg_bt_wv6.2'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092 and typeOfGeneratingProcess == 8:
            return 'obsmsg_bt_ir9.7'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'obsmsg_bt_ir8.7'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfCentralWaveNumber == 256410 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 'obsmsg_bt_ir3.9'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'obsmsg_bt_ir13.4'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 83333 and typeOfGeneratingProcess == 8:
            return 'obsmsg_bt_ir12.0'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'obsmsg_bt_ir10.8'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and scaledValueOfCentralWaveNumber == 1250000 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 'obsmsg_alb_vis0.8'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1666666:
            return 'obsmsg_alb_vis0.6'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 625000 and typeOfGeneratingProcess == 8:
            return 'obsmsg_alb_nir1.6'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 2000000 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'obsmsg_alb_hrv'

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 198 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'vmax_10m_c'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfGeneratingProcess == 198 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'snow_gsp_c'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 198:
            return 'tot_prec_c'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103:
            return 'vmax_10m_s'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197:
            return 't_s_s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197:
            return 'snow_gsp_s'

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0:
            return 'clch_s'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400:
            return 'clcm_s'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 800 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == -2:
            return 'clcl_s'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197:
            return 'clct_s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197:
            return 'tot_prec_s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfGeneratingProcess == 197 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'v_10m_s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197 and typeOfFirstFixedSurface == 103:
            return 'u_10m_s'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'td_2m_s'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'tmin_2m_s'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'tmax_2m_s'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 't_2m_s'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and scaledValueOfCentralWaveNumber == 136986 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 'synmsg_rad_cs_wv7.3'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'synmsg_rad_cs_wv6.2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'synmsg_rad_cs_ir9.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942 and satelliteSeries == 333:
            return 'synmsg_rad_cs_ir8.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'synmsg_rad_cs_ir3.9'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'synmsg_rad_cs_ir13.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'synmsg_rad_cs_ir12.1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'synmsg_rad_cs_ir10.8'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 136986 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 'synmsg_rad_cl_wv7.3'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 161290 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 'synmsg_rad_cl_wv6.2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'synmsg_rad_cl_ir9.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942 and satelliteSeries == 333:
            return 'synmsg_rad_cl_ir8.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'synmsg_rad_cl_ir3.9'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'synmsg_rad_cl_ir13.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'synmsg_rad_cl_ir12.1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'synmsg_rad_cl_ir10.8'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'synmsg_bt_cs_wv7.3'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290 and satelliteSeries == 333:
            return 'synmsg_bt_cs_wv6.2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'synmsg_bt_cs_ir9.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and scaledValueOfCentralWaveNumber == 256410 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 'synmsg_bt_cs_ir3.9'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'synmsg_bt_cs_ir13.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'synmsg_bt_cs_ir12.1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and scaledValueOfCentralWaveNumber == 92592 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 'synmsg_bt_cs_ir10.8'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'synmsg_bt_cs_ir8.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986 and satelliteSeries == 333 and satelliteNumber == 72:
            return 'synmsg_bt_cl_wv7.3'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'synmsg_bt_cl_wv6.2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092 and satelliteSeries == 333:
            return 'synmsg_bt_cl_ir9.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'synmsg_bt_cl_ir8.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'synmsg_bt_cl_ir3.9'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'synmsg_bt_cl_ir13.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'synmsg_bt_cl_ir12.1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'synmsg_bt_cl_ir10.8'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 'synme7_rad_cs_wv6.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 'synme7_rad_cs_ir11.5'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 'synme7_rad_cl_wv6.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 'synme7_rad_cl_ir11.5'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteNumber == 54 and instrumentType == 205 and satelliteSeries == 331:
            return 'synme7_bt_cs_wv6.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 'synme7_bt_cs_ir11.5'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 54:
            return 'synme7_bt_cl_wv6.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 'synme7_bt_cl_ir11.5'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'synme6_rad_cs'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'synme6_rad_cl'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 53:
            return 'synme6_bt_cs'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'synme6_bt_cl'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteNumber == 52 and instrumentType == 205 and satelliteSeries == 331:
            return 'synme5_rad_cs'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'synme5_rad_cl'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'synme5_bt_cs'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 52:
            return 'synme5_bt_cl'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'eia-ke'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'efa-ke'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'eia-om'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'efa-om'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'eia-t'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 199 and typeOfStatisticalProcessing == 5:
            return 'efa-t'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'eia-rh'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'efa-rh'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'eia-fi'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'efa-fi'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'eia-v'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'efa-v'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'eia-u'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 'efa-u'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'eia-ps'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfGeneratingProcess == 199 and typeOfStatisticalProcessing == 5:
            return 'efa-ps'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199 and typeOfFirstFixedSurface == 1:
            return 'clct_mod'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198 and typeOfFirstFixedSurface == 1:
            return 'cldepth'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'ice_grd'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13 and typeOfFirstFixedSurface == 1:
            return 'ceiling'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'thetae'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'ko'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 107 and scaleFactorOfFirstFixedSurface == -2:
            return 'ptheta'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14 and typeOfFirstFixedSurface == 107:
            return 'ipv'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 25 and typeOfFirstFixedSurface == 1:
            return 'ww'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfFirstFixedSurface == 1:
            return 'ccl_nn'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'vabs'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'srh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 105:
            return 'w_shaer'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 'uv_max'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfFirstFixedSurface == 1:
            return 'vdis_sso'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'avdis_sso'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'vstr_sso'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'avstr_sso'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'ustr_sso'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'austr_sso'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 227:
            return 'ba-140w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 226:
            return 'ba-140d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 225:
            return 'ba-140'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 224:
            return 'i-131ow'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 223:
            return 'i-131od'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 222:
            return 'i-131o'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 221:
            return 'i-131gw'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 220:
            return 'i-131gd'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 219:
            return 'i-131g'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 218:
            return 'xe-133w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 217:
            return 'xe-133d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 216:
            return 'xe-133'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 215:
            return 'tr-2w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 214:
            return 'tr-2d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 213:
            return 'tr-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 212:
            return 'kr-85w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 211:
            return 'kr-85d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 210:
            return 'kr-85'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 209:
            return 'zr-95w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 208:
            return 'zr-95d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 207:
            return 'zr-95'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 206:
            return 'te-132w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 205:
            return 'te-132d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 204:
            return 'te-132'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 203:
            return 'cs-137w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 202:
            return 'cs-137d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 201:
            return 'cs-137'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 200:
            return 'i-131aw'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 199:
            return 'i-131ad'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 198:
            return 'i-131a'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 197:
            return 'sr-90w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 196:
            return 'sr-90d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 195:
            return 'sr-90'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 194:
            return 'ru-103w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 193:
            return 'ru-103d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 192:
            return 'ru-103'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'o3'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'zhd'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'zwd'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'ztd'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 200 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'ustr'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'rlon'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'rlat'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'fc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 'qvsflx'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'dqvdt'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 196 and typeOfStatisticalProcessing == 0:
            return 'aer_ss12'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 196:
            return 'aer_ss'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195 and typeOfStatisticalProcessing == 0:
            return 'aer_bc12'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195:
            return 'aer_bc'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194 and typeOfStatisticalProcessing == 0:
            return 'aer_org12'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194:
            return 'aer_org'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 'aer_dust12'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193:
            return 'aer_dust'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192 and typeOfStatisticalProcessing == 0:
            return 'aer_so412'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192:
            return 'aer_so4'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'ndviratio'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'ndvi_mrat'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 2:
            return 'ndvi_max'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31:
            return 'ndvi'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 30 and typeOfFirstFixedSurface == 1:
            return 'for_d'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 29 and typeOfFirstFixedSurface == 1:
            return 'for_e'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 100 and typeOfStatisticalProcessing == 7 and scaleFactorOfFirstFixedSurface == -2:
            return 'wvar2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 10 and typeOfStatisticalProcessing == 7 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0:
            return 'wvar1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'oro_mod'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 3:
            return 'lai_mn'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1:
            return 'lai_mx'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 1:
            return 'plcov_mn'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1:
            return 'plcov_mx'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'vio3'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'hmo3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 32 and typeOfFirstFixedSurface == 1:
            return 'rootdp'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfFirstFixedSurface == 1:
            return 'lai'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'soiltyp'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196 and typeOfFirstFixedSurface == 1:
            return 'emis_rad'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 1:
            return 'sso_sigma'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21 and typeOfFirstFixedSurface == 1:
            return 'sso_theta'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24 and typeOfFirstFixedSurface == 1:
            return 'sso_gamma'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 1:
            return 'sso_stdh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'dv_sso'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'du_sso'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 'ana_err_v'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfGeneratingProcess == 7 and typeOfStatisticalProcessing == 6:
            return 'ana_err_u'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 'ana_err_fi'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 199:
            return 'sprd'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 198:
            return 'tm02'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 197:
            return 'tm01'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 196:
            return 'tm10'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 195:
            return 'pp1d'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 194:
            return 'ppps'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 194 and typeOfFirstFixedSurface == 101:
            return 'mpp_s'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 193:
            return 'ppww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 193 and typeOfFirstFixedSurface == 101:
            return 'mwp_x'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 192:
            return 'mwd'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206 and typeOfFirstFixedSurface == 1:
            return 'qcvg_con'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'cape_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205 and typeOfFirstFixedSurface == 1:
            return 'mflx_con'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'resid_wso'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'totforce_s'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'tra_sum'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'evatra_sum'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'sotr_rad'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'dttdiv'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 10:
            return 'dbz_cmax'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dbz'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'dbz_850'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8 and typeOfFirstFixedSurface == 1:
            return 't_ice'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16 and typeOfFirstFixedSurface == 1:
            return 'prs_min'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 't_snow'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and typeOfFirstFixedSurface == 1:
            return 'w_i'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2:
            return 'w_so_ice'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2:
            return 'w_so'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2:
            return 't_so'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 'ru-103'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 10 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 'vmax_10m'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'mh'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 19 and typeOfFirstFixedSurface == 1:
            return 'tch'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29 and typeOfFirstFixedSurface == 1:
            return 'tcm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'tkvh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 31 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'tkvm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'tke'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'ke'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'tketens'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 24:
            return 'tke_con'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 192:
            return 'cin_ml'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 192:
            return 'cape_ml'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 193:
            return 'cin_mu'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 193:
            return 'cape_mu'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 'sdi_2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'sdi_1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'pp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 1:
            return 'rho_snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'grau_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1:
            return 'prg_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dqi_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 'freshsnw'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dqc_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'dqv_gsp'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dt_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'rr_c'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'rr_f'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'rain_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfFirstFixedSurface == 1:
            return 'prs_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfFirstFixedSurface == 1:
            return 'prr_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'rain_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfFirstFixedSurface == 1:
            return 'prs_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfFirstFixedSurface == 1:
            return 'prr_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'q_sedim'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dqi_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dqc_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204:
            return 'snowlmt'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 200 and typeOfFirstFixedSurface == 4:
            return 'hzerocl'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196 and typeOfFirstFixedSurface == 1:
            return 'htop_dc'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dv_con'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'du_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dqv_con'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dt_con'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 'top_con'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'bas_con'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27 and typeOfFirstFixedSurface == 3:
            return 'htop_con'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfFirstFixedSurface == 2:
            return 'hbas_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'clw_con'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193 and typeOfFirstFixedSurface == 3:
            return 'htop_sc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192 and typeOfFirstFixedSurface == 2:
            return 'hbas_sc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'qi_rad'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'qc_rad'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 'tdiv_hum'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 78 and typeOfFirstFixedSurface == 1:
            return 'twater'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 74:
            return 'tqg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'qg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'tqs'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'tqr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'qs'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'qr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 'qi'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'qc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'clc_sgs'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'clc'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 'rstom'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1:
            return 'dursun'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106 and typeOfStatisticalProcessing == 0:
            return 'alhfl_pl'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'alhfl_bs'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'thhr_rad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'sohr_rad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'pabs_rad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'apab_s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'avmfl_s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'aumfl_s'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'ashfl_s'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'alhfl_s'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 0:
            return 'thbt_rad'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 0:
            return 'athb_t'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 0:
            return 'sobt_rad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 0:
            return 'asob_t'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'thbs_rad'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'athb_s'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'sobs_rad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'asob_s'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 'mpps'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'shps'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'mdps'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'mpww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'shww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'mdww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'swh'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'h_ice'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'fr_ice'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2 and typeOfStatisticalProcessing == 1 and scaledValueOfSecondFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2:
            return 'runoff_s'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and typeOfStatisticalProcessing == 1 and scaledValueOfSecondFixedSurface == 190 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == -2:
            return 'runoff_g_lm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and typeOfStatisticalProcessing == 1 and scaledValueOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == -2:
            return 'runoff_g'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'plcov'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 100:
            return 'w_g2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2:
            return 'w_g1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 190 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2:
            return 'w_cl'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0:
            return 't_s'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaledValueOfFirstFixedSurface == 9 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 't_m'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaledValueOfFirstFixedSurface == 41 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 't_cl_lm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaledValueOfFirstFixedSurface == 36 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 't_cl'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 'albedo_b'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'alb_rad'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'z0'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'fr_land'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'snow_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'snow_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69 and typeOfFirstFixedSurface == 1:
            return 'tqc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 400 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2:
            return 'clch'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 800 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400 and scaleFactorOfFirstFixedSurface == -2:
            return 'clcm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 800 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 100:
            return 'clcl'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'clc_con'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'clct'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 'h_snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 'w_snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1:
            return 'prec_con'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1:
            return 'prec_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'tot_prec'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70 and typeOfFirstFixedSurface == 1:
            return 'tqi'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'aevap_s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64 and typeOfFirstFixedSurface == 1:
            return 'tqv'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'relhum'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'relhum_2m'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'qv'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0:
            return 'qv_2m'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'qv_s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'w'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'omega'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'v'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0:
            return 'v_10m'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'u'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'u_10m'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'sp'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10:
            return 'sp_10m'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'dd'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0:
            return 'dd_10m'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'wvsp3'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'wvsp2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'wvsp1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2:
            return 'dbz_max'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'td_2m_av'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3:
            return 'tmin_2m'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 'tmax_2m'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 't'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 0 and typeOfGeneratingProcess == 9:
            return 't_2m_cl'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 't_g'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'to3'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'hhl'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'hsurf'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'fi'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 'fif'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'fis'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'dpsdt'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 101:
            return 'pmsl'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'p'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'ps'

        is_s2s = h.get_l('is_s2s')
        subCentre = h.get_l('subCentre')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and is_s2s == 1 and subCentre == 102 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return '2d'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return '2d'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0 and is_s2s == 1 and subCentre == 102:
            return 'ci'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'ci'

    return wrapped
