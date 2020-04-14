import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 235:
            return 'HSNOW_MAX'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'SKC'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 235:
            return 'RAPA_SPPT'

        constituentType = h.get_l('constituentType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62101:
            return 'BETUsaisn'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62200:
            return 'AMBRfe'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62200:
            return 'AMBRsaisl'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62200:
            return 'AMBRsaisa'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62200:
            return 'AMBRsaisn'

        typeOfGeneratingProcess = h.get_l('typeOfGeneratingProcess')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'AMBRtthre'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'AMBRtthrs'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62200:
            return 'AMBRctsum'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'AMBRhcem'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62200:
            return 'AMBRsdes'

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62200:
            return 'AMBRress'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62200:
            return 'AMBRresn'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62200:
            return 'AMBRreso'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62300:
            return 'POACfe'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62300:
            return 'POACsaisl'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62300:
            return 'POACsaisa'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62300:
            return 'POACsaisn'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'POACtthre'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'POACtthrs'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62300:
            return 'POACctsum'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'POAChcem'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62300:
            return 'POACsdes'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62300:
            return 'POACress'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62300:
            return 'POACresn'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62300:
            return 'POACreso'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62100:
            return 'ALNUfe'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62100:
            return 'ALNUsaisl'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62100:
            return 'ALNUsaisa'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62100:
            return 'ALNUsaisn'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'ALNUtthre'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'ALNUtthrs'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62100:
            return 'ALNUctsum'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'ALNUhcem'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62100:
            return 'ALNUsdes'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62100:
            return 'ALNUress'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62100:
            return 'ALNUresn'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62100:
            return 'ALNUreso'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62101:
            return 'BETUfe'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62101:
            return 'BETUsaisl'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62101:
            return 'BETUsaisa'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'BETUtthre'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'BETUtthrs'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62101:
            return 'BETUctsum'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'BETUhcem'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62101:
            return 'BETUsdes'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62101:
            return 'BETUress'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62101:
            return 'BETUresn'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62101:
            return 'BETUreso'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'EVAP_PL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 234:
            return 'RCLD'

        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 205 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'VGUST_CON_10M'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 4:
            return 'T_MRT'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192 and typeOfStatisticalProcessing == 2:
            return 'LPI_MAX'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 207 and typeOfStatisticalProcessing == 2:
            return 'W_CTMAX'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 206 and typeOfStatisticalProcessing == 2:
            return 'VORW_CTMAX'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 203:
            return 'USTAR_THRES'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 2:
            return 'SLO_ANG'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 3:
            return 'SLO_ASP'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 1:
            return 'HORIZON'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 0:
            return 'SKYVIEW'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 234:
            return 'ALB_SEAICE'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'AHF'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'FR_PAVED'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 2:
            return 'THLQTCOV'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 1:
            return 'QTQTCOV'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 0:
            return 'THLTHLCOV'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 192 and typeOfFirstFixedSurface == 10:
            return 'RADIONUC_AC_VI'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 202:
            return 'WSHEAR_DIFF'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 201:
            return 'WSHEAR_INT'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 28:
            return 'WDIV_3D'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 27:
            return 'RELV_ADV_G'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 26:
            return 'RELV_G'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 'UTCI_SHADOW'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 195 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'T_2M_SNOWC'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 199:
            return 'SWISS_WE'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 198:
            return 'SWISS_SN'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 2:
            return 'SWISS12'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 1:
            return 'SWISS00'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 233:
            return 'SNOW_PERCENT'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 12:
            return 'SIGMAZ'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 11:
            return 'SIGMAY'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 10:
            return 'SIGMAX'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 9:
            return 'SIGMAW'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 8:
            return 'SIGMAV'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 7:
            return 'SIGMAU'

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 197 and typeOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 3:
            return 'PDIFF_CON'

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ATHD_S_TS'

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 2 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ATHD_S_TG'

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ATHD_S_T2M'

        if discipline == 215 and parameterCategory == 19 and parameterNumber == 0:
            return 'LUM'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 194:
            return 'LFC_ML'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 6:
            return 'LAGTIMEZ'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 5:
            return 'LAGTIMEY'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 4:
            return 'LAGTIMEX'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 3:
            return 'LAGTIMEW'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 2:
            return 'LAGTIMEV'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 1:
            return 'LAGTIMEU'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 205:
            return 'ASOD_SvW'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 204:
            return 'ASOD_SvS'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 203:
            return 'ASOD_SvN'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 202:
            return 'ASOD_SvE'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 201:
            return 'ASOD_SH'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'ENTH_2M'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 'ENTH'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 206 and typeOfFirstFixedSurface == 1:
            return 'DURSUN_R'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 205 and typeOfStatisticalProcessing == 11 and typeOfFirstFixedSurface == 1:
            return 'DURSUN_M'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'DDCLASS_10M'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 0:
            return 'DDCLASS'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194 and typeOfFirstFixedSurface == 10:
            return 'DCI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 232:
            return 'CONV_PERCENT'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 231:
            return 'CLI_RATIO'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 233:
            return 'CAT_DTI'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 232:
            return 'CAT_DVT'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 29:
            return 'WDEF_H'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 231:
            return 'CAT_TI2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 230:
            return 'CAT_TI1'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 197:
            return 'BOAGAW_SN'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 196:
            return 'BOAGAW_WE'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 195:
            return 'BOAGAE_SN'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 194:
            return 'BOAGAE_WE'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 201:
            return 'ASWDIR_SH'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 0:
            return 'ADEDO2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 229:
            return 'EDPP'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 196:
            return 'HMIN10CL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 230 and typeOfStatisticalProcessing == 1:
            return 'RD_SNOW'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192:
            return 'LPI'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 228:
            return 'EDP_MAX_LFIR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 227:
            return 'DENH'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 204:
            return 'DENI'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 203:
            return 'DENC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 226:
            return 'DENG'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 225:
            return 'DENS'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 224:
            return 'DENR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 223:
            return 'NDHAIL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 222:
            return 'NDGRAUPEL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 221:
            return 'NDSNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 219:
            return 'NCHAIL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 218:
            return 'NCGRAUPEL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 217:
            return 'NCSNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 229:
            return 'NDRAIN'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 228:
            return 'NCRAIN'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 201:
            return 'PFRQ'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 200 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'SMI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 220:
            return 'RH_MIX_EC'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 193:
            return 'AW'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 197 and typeOfStatisticalProcessing == 1:
            return 'RADAR_FQ'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 196 and typeOfStatisticalProcessing == 1:
            return 'RADAR_FS'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 195 and typeOfStatisticalProcessing == 1:
            return 'RADAR_RH'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 194 and typeOfStatisticalProcessing == 1:
            return 'RADAR_RE'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 193 and typeOfStatisticalProcessing == 1:
            return 'RADAR_RS'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'RADAR_RQ'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfFirstFixedSurface == 1:
            return 'SWDIFDS_RAD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 216:
            return 'TQI_DIA'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 215:
            return 'TQC_DIA'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 214:
            return 'TQV_DIA'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 213:
            return 'QI_DIA'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 212:
            return 'QC_DIA'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 211:
            return 'QV_DIA'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 198:
            return 'RAD_HEIGHT'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 197:
            return 'RAD_BL'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 196:
            return 'RAD_QUAL'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 195:
            return 'RAD_PRECIP'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 227:
            return 'EDR'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 226:
            return 'EDP_MAX_UUIR'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 225:
            return 'EDP_MAX_LUIR'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 224:
            return 'EDP_MAX_UFIR'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 223:
            return 'ALB_NI'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 223 and typeOfStatisticalProcessing == 0:
            return 'ALB_NI12'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 222:
            return 'ALB_UV'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 222 and typeOfStatisticalProcessing == 0:
            return 'ALB_UV12'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfFirstFixedSurface == 1:
            return 'SWDIRS_RAD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 210 and typeOfFirstFixedSurface == 114:
            return 'WLIQ_SNOW_M'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 254:
            return 'DUMMY_254'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 253:
            return 'DUMMY_253'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 252:
            return 'DUMMY_252'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 251:
            return 'DUMMY_251'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 250:
            return 'DUMMY_250'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 249:
            return 'DUMMY_249'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 248:
            return 'DUMMY_248'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 247:
            return 'DUMMY_247'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 246:
            return 'DUMMY_246'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 245:
            return 'DUMMY_245'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 244:
            return 'DUMMY_244'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 243:
            return 'DUMMY_243'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 242:
            return 'DUMMY_242'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 241:
            return 'DUMMY_241'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 240:
            return 'DUMMY_240'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 239:
            return 'DUMMY_239'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 238:
            return 'DUMMY_238'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 237:
            return 'DUMMY_237'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 236:
            return 'DUMMY_236'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 235:
            return 'DUMMY_235'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 234:
            return 'DUMMY_234'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 233:
            return 'DUMMY_233'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 232:
            return 'DUMMY_232'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 231:
            return 'DUMMY_231'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 230:
            return 'DUMMY_230'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 229:
            return 'DUMMY_229'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 228:
            return 'DUMMY_228'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 227:
            return 'DUMMY_227'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 226:
            return 'DUMMY_226'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 225:
            return 'DUMMY_225'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 224:
            return 'DUMMY_224'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 223:
            return 'DUMMY_223'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 222:
            return 'DUMMY_222'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 221:
            return 'DUMMY_221'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 220:
            return 'DUMMY_220'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 219:
            return 'DUMMY_219'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 218:
            return 'DUMMY_218'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 217:
            return 'DUMMY_217'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 216:
            return 'DUMMY_216'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 215:
            return 'DUMMY_215'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 214:
            return 'DUMMY_214'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 213:
            return 'DUMMY_213'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 212:
            return 'DUMMY_212'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 211:
            return 'DUMMY_211'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 210:
            return 'DUMMY_210'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 209:
            return 'DUMMY_209'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 208:
            return 'DUMMY_208'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 207:
            return 'DUMMY_207'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 206:
            return 'DUMMY_206'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 205:
            return 'DUMMY_205'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 204:
            return 'DUMMY_204'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 203:
            return 'DUMMY_203'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 202:
            return 'DUMMY_202'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 201:
            return 'DUMMY_201'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 200:
            return 'DUMMY_200'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 199:
            return 'DUMMY_199'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 198:
            return 'DUMMY_198'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 197:
            return 'DUMMY_197'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 196:
            return 'DUMMY_196'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 195:
            return 'DUMMY_195'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 194:
            return 'DUMMY_194'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 193:
            return 'DUMMY_193'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 192:
            return 'DUMMY_192'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 191:
            return 'DUMMY_191'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 190:
            return 'DUMMY_190'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 189:
            return 'DUMMY_189'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 188:
            return 'DUMMY_188'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 187:
            return 'DUMMY_187'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 186:
            return 'DUMMY_186'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 185:
            return 'DUMMY_185'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 184:
            return 'DUMMY_184'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 183:
            return 'DUMMY_183'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 182:
            return 'DUMMY_182'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 181:
            return 'DUMMY_181'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 180:
            return 'DUMMY_180'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 179:
            return 'DUMMY_179'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 178:
            return 'DUMMY_178'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 177:
            return 'DUMMY_177'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 176:
            return 'DUMMY_176'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 175:
            return 'DUMMY_175'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 174:
            return 'DUMMY_174'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 173:
            return 'DUMMY_173'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 172:
            return 'DUMMY_172'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 171:
            return 'DUMMY_171'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 170:
            return 'DUMMY_170'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 169:
            return 'DUMMY_169'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 168:
            return 'DUMMY_168'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 167:
            return 'DUMMY_167'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 166:
            return 'DUMMY_166'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 165:
            return 'DUMMY_165'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 164:
            return 'DUMMY_164'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 163:
            return 'DUMMY_163'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 162:
            return 'DUMMY_162'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 161:
            return 'DUMMY_161'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 160:
            return 'DUMMY_160'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 159:
            return 'DUMMY_159'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 158:
            return 'DUMMY_158'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 157:
            return 'DUMMY_157'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 156:
            return 'DUMMY_156'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 155:
            return 'DUMMY_155'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 154:
            return 'DUMMY_154'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 153:
            return 'DUMMY_153'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 152:
            return 'DUMMY_152'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 151:
            return 'DUMMY_151'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 150:
            return 'DUMMY_150'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 149:
            return 'DUMMY_149'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 148:
            return 'DUMMY_148'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 147:
            return 'DUMMY_147'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 146:
            return 'DUMMY_146'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 145:
            return 'DUMMY_145'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 144:
            return 'DUMMY_144'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 143:
            return 'DUMMY_143'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 142:
            return 'DUMMY_142'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 141:
            return 'DUMMY_141'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 140:
            return 'DUMMY_140'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 139:
            return 'DUMMY_139'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 138:
            return 'DUMMY_138'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 137:
            return 'DUMMY_137'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 136:
            return 'DUMMY_136'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 135:
            return 'DUMMY_135'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 134:
            return 'DUMMY_134'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 133:
            return 'DUMMY_133'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 132:
            return 'DUMMY_132'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 131:
            return 'DUMMY_131'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 130:
            return 'DUMMY_130'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 129:
            return 'DUMMY_129'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 128:
            return 'DUMMY_128'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 127:
            return 'DUMMY_127'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 126:
            return 'DUMMY_126'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 125:
            return 'DUMMY_125'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 124:
            return 'DUMMY_124'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 123:
            return 'DUMMY_123'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 122:
            return 'DUMMY_122'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 121:
            return 'DUMMY_121'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 120:
            return 'DUMMY_120'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 119:
            return 'DUMMY_119'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 118:
            return 'DUMMY_118'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 117:
            return 'DUMMY_117'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 116:
            return 'DUMMY_116'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 115:
            return 'DUMMY_115'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 114:
            return 'DUMMY_114'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 113:
            return 'DUMMY_113'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 112:
            return 'DUMMY_112'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 111:
            return 'DUMMY_111'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 110:
            return 'DUMMY_110'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 109:
            return 'DUMMY_109'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 108:
            return 'DUMMY_108'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 107:
            return 'DUMMY_107'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 106:
            return 'DUMMY_106'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 105:
            return 'DUMMY_105'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 104:
            return 'DUMMY_104'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 103:
            return 'DUMMY_103'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 102:
            return 'DUMMY_102'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 101:
            return 'DUMMY_101'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 100:
            return 'DUMMY_100'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 99:
            return 'DUMMY_99'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 98:
            return 'DUMMY_98'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 97:
            return 'DUMMY_97'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 96:
            return 'DUMMY_96'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 95:
            return 'DUMMY_95'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 94:
            return 'DUMMY_94'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 93:
            return 'DUMMY_93'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 92:
            return 'DUMMY_92'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 91:
            return 'DUMMY_91'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 90:
            return 'DUMMY_90'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 89:
            return 'DUMMY_89'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 88:
            return 'DUMMY_88'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 87:
            return 'DUMMY_87'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 86:
            return 'DUMMY_86'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 85:
            return 'DUMMY_85'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 84:
            return 'DUMMY_84'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 83:
            return 'DUMMY_83'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 82:
            return 'DUMMY_82'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 81:
            return 'DUMMY_81'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 80:
            return 'DUMMY_80'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 79:
            return 'DUMMY_79'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 78:
            return 'DUMMY_78'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 77:
            return 'DUMMY_77'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 76:
            return 'DUMMY_76'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 75:
            return 'DUMMY_75'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 74:
            return 'DUMMY_74'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 73:
            return 'DUMMY_73'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 72:
            return 'DUMMY_72'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 71:
            return 'DUMMY_71'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 70:
            return 'DUMMY_70'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 69:
            return 'DUMMY_69'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 68:
            return 'DUMMY_68'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 67:
            return 'DUMMY_67'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 66:
            return 'DUMMY_66'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 65:
            return 'DUMMY_65'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 64:
            return 'DUMMY_64'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 63:
            return 'DUMMY_63'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 62:
            return 'DUMMY_62'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 61:
            return 'DUMMY_61'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 60:
            return 'DUMMY_60'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 59:
            return 'DUMMY_59'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 58:
            return 'DUMMY_58'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 57:
            return 'DUMMY_57'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 56:
            return 'DUMMY_56'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 55:
            return 'DUMMY_55'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 54:
            return 'DUMMY_54'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 53:
            return 'DUMMY_53'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 52:
            return 'DUMMY_52'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 51:
            return 'DUMMY_51'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 50:
            return 'DUMMY_50'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 49:
            return 'DUMMY_49'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 48:
            return 'DUMMY_48'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 47:
            return 'DUMMY_47'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 46:
            return 'DUMMY_46'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 45:
            return 'DUMMY_45'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 44:
            return 'DUMMY_44'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 43:
            return 'DUMMY_43'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 42:
            return 'DUMMY_42'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 41:
            return 'DUMMY_41'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 40:
            return 'DUMMY_40'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 39:
            return 'DUMMY_39'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 38:
            return 'DUMMY_38'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 37:
            return 'DUMMY_37'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 36:
            return 'DUMMY_36'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 35:
            return 'DUMMY_35'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 34:
            return 'DUMMY_34'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 33:
            return 'DUMMY_33'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 32:
            return 'DUMMY_32'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 31:
            return 'DUMMY_31'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 30:
            return 'DUMMY_30'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 29:
            return 'DUMMY_29'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 28:
            return 'DUMMY_28'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 27:
            return 'DUMMY_27'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 26:
            return 'DUMMY_26'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 25:
            return 'DUMMY_25'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 24:
            return 'DUMMY_24'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 23:
            return 'DUMMY_23'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 22:
            return 'DUMMY_22'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 21:
            return 'DUMMY_21'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 20:
            return 'DUMMY_20'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 19:
            return 'DUMMY_19'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 18:
            return 'DUMMY_18'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 17:
            return 'DUMMY_17'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 16:
            return 'DUMMY_16'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 15:
            return 'DUMMY_15'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 14:
            return 'DUMMY_14'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 13:
            return 'DUMMY_13'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 12:
            return 'DUMMY_12'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 11:
            return 'DUMMY_11'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 10:
            return 'DUMMY_10'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 9:
            return 'DUMMY_9'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 8:
            return 'DUMMY_8'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 7:
            return 'DUMMY_7'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 6:
            return 'DUMMY_6'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 5:
            return 'DUMMY_5'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 4:
            return 'DUMMY_4'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 3:
            return 'DUMMY_3'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 2:
            return 'DUMMY_2'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 1:
            return 'DUMMY_1'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 252:
            return 'VSOILS0'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 251:
            return 'VSOILS'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 74:
            return 'VSOILC0'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 73:
            return 'VSOILB0'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 72:
            return 'VSOILA0'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 35:
            return 'VSOILC'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 34:
            return 'VSOILB'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 33:
            return 'VSOILA'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 197:
            return 'HTOP_THERM'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 200:
            return 'ATM_RSTC'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 218:
            return 'DTKE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 219:
            return 'DTKE_CON'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 221:
            return 'DTKE_HSH'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 220:
            return 'DTKE_SSO'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 14 and typeOfGeneratingProcess == 5:
            return 'TAUX'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 13 and typeOfGeneratingProcess == 5:
            return 'TAU'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 12 and typeOfGeneratingProcess == 5:
            return 'FG'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 'FZRAX'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 10 and typeOfGeneratingProcess == 5:
            return 'FZRA'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 9 and typeOfGeneratingProcess == 5:
            return 'FZ'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 8 and typeOfGeneratingProcess == 5:
            return 'BLSN8'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 7 and typeOfGeneratingProcess == 5:
            return 'BLSN6'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 6 and typeOfGeneratingProcess == 5:
            return 'RA70'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 5 and typeOfGeneratingProcess == 5:
            return 'RA40'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 4 and typeOfGeneratingProcess == 5:
            return 'RA25'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 3 and typeOfGeneratingProcess == 5:
            return 'TSXX'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 2 and typeOfGeneratingProcess == 5:
            return 'TSX'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 1 and typeOfGeneratingProcess == 5:
            return 'TS'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 209 and typeOfStatisticalProcessing == 1:
            return 'RR_SNOW'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 217:
            return 'ELD'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 216:
            return 'EDP'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 198 and typeOfGeneratingProcess == 6:
            return 'WCOV'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197 and typeOfGeneratingProcess == 6:
            return 'WVAR'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 195:
            return 'PPP'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 192:
            return 'SST_IC'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 192:
            return 'TIDAL'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 202:
            return 'TOP_DCON'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 22:
            return 'CATIX'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 21:
            return 'FRONTOF'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 20:
            return 'DIVQS'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 19:
            return 'DIVQN'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 18:
            return 'QVS'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 17:
            return 'DIVQ'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 16:
            return 'FRONTO'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 15:
            return 'DIVQSGEO'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 14:
            return 'DIVQNGEO'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 13:
            return 'QVSGEO'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 12:
            return 'QVNGEO'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 11:
            return 'DIVGEO'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 10:
            return 'QVY'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 9:
            return 'QVX'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 8:
            return 'FORCOMEGA'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 7:
            return 'VORG'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 23:
            return 'PVP'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 199:
            return 'VORTIC_V'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 198:
            return 'VORTIC_U'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 192:
            return 'CL_TOP_TEMP'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 192:
            return 'CL_TYPE_SAT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 209:
            return 'WW_0-9'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208 and typeOfGeneratingProcess == 0:
            return 'DIS_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207 and typeOfGeneratingProcess == 0:
            return 'DID_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208 and typeOfGeneratingProcess == 2:
            return 'PIS_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207 and typeOfGeneratingProcess == 2:
            return 'PID_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206 and typeOfGeneratingProcess == 0:
            return 'DISC_SIG_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205 and typeOfGeneratingProcess == 0:
            return 'DISC_VERT_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204 and typeOfGeneratingProcess == 0:
            return 'DISC_TOP_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203 and typeOfGeneratingProcess == 0:
            return 'DISC_SIG_TOP_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202 and typeOfGeneratingProcess == 0:
            return 'DISC_SIG_BASE_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201 and typeOfGeneratingProcess == 0:
            return 'DISC_BASE_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200 and typeOfGeneratingProcess == 0:
            return 'DIDC_MAX_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199 and typeOfGeneratingProcess == 0:
            return 'DIDC_VERT_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198 and typeOfGeneratingProcess == 0:
            return 'DIDC_TOP_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197 and typeOfGeneratingProcess == 0:
            return 'DIDC_MAX_TOP_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196 and typeOfGeneratingProcess == 0:
            return 'DIDC_MAX_BASE_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195 and typeOfGeneratingProcess == 0:
            return 'DIDC_BASE_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206 and typeOfGeneratingProcess == 2:
            return 'PISC_SIG_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205 and typeOfGeneratingProcess == 2:
            return 'PISC_VERT_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204 and typeOfGeneratingProcess == 2:
            return 'PISC_TOP_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203 and typeOfGeneratingProcess == 2:
            return 'PISC_SIG_TOP_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202 and typeOfGeneratingProcess == 2:
            return 'PISC_SIG_BASE_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201 and typeOfGeneratingProcess == 2:
            return 'PISC_BASE_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200 and typeOfGeneratingProcess == 2:
            return 'PIDC_MAX_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199 and typeOfGeneratingProcess == 2:
            return 'PIDC_VERT_CODE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198 and typeOfGeneratingProcess == 2:
            return 'PIDC_TOP_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197 and typeOfGeneratingProcess == 2:
            return 'PIDC_MAX_TOP_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196 and typeOfGeneratingProcess == 2:
            return 'PIDC_MAX_BASE_HFT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195 and typeOfGeneratingProcess == 2:
            return 'PIDC_BASE_HFT'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ASWDIFD_S'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ASWDIR_S'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 2:
            return 'CLO'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 3:
            return 'SUL_PROB'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 1:
            return 'PT1M'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 201:
            return 'C_TYPE'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 194 and typeOfStatisticalProcessing == 2:
            return 'UVI_MAX_H'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 197:
            return 'UVI_CL_COR'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 196:
            return 'UVI_B_CS'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 195:
            return 'UVI_CS_COR'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 236 and typeOfStatisticalProcessing == 3 and typeOfGeneratingProcess == 5:
            return 'W_FRSTR_06'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 232 and typeOfStatisticalProcessing == 3 and typeOfGeneratingProcess == 5:
            return 'W_FR_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 213 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_SVWSK_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 212 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_SVW_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 199 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_GEWSW_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 198 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_GEWSK_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 197 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_GEW_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 191 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_GLEIS_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 139 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'E_ORK_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 138 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_ORK_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 137 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_ORKAR_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 136 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_STMSW_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 134 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_STM_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 132 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_WND_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 77 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'E_SF_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 75 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_SFSK_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 74 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_SF_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 72 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_SFL_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 71 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_SFSK_06'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 70 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_SF_06'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 69 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_SFL_06'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 32 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'E_DR_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 29 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_DRRER_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 26 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_DRR_12'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 17 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_SKRRH_06'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 14 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_SKRR_06'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 3 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'U_SKRRH_01'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'W_SKRR_01'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'EIA-KE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'EFA-KE'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199:
            return 'CLCT_MOD'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198:
            return 'CLDEPTH'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 6:
            return 'VP'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 5:
            return 'UP'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 25 and typeOfFirstFixedSurface == 107:
            return 'IPV'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 4:
            return 'QVN'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 3:
            return 'WDIV'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 2:
            return 'ADRTG'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 1:
            return 'ADVOR'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 0:
            return 'ADVORG'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 24 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'CCL_NN'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 194:
            return 'CL_TYP'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 197:
            return 'VABS'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194:
            return 'VSTR_SSO'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfStatisticalProcessing == 0:
            return 'AVSTR_SSO'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193:
            return 'USTR_SSO'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 'AUSTR_SSO'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 194:
            return 'ZHD'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 193:
            return 'ZWD'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 192:
            return 'ZTD'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193:
            return 'FC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 'QVSFLX'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207:
            return 'DQVDT'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192:
            return 'NDVIRATIO'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 0:
            return 'NDVI_MRAT'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193:
            return 'VIO3'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192:
            return 'HMO3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196:
            return 'SOILTYP'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 199:
            return 'EMIS_RAD'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195:
            return 'DV_SSO'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194:
            return 'DU_SSO'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 3 and typeOfGeneratingProcess == 7:
            return 'ANA_ERR_V'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 2 and typeOfGeneratingProcess == 7:
            return 'ANA_ERR_U'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 5 and typeOfGeneratingProcess == 7:
            return 'ANA_ERR_FI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206:
            return 'QCVG_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205 and typeOfFirstFixedSurface == 2:
            return 'MFLX_CON'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'RESID_WSO'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'TOTFORCE_S'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'TRA_SUM'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'EVATRA_SUM'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193:
            return 'SOTR_RAD'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 192:
            return 'DTTDIV'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196:
            return 'KE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 'TKETENS'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 192:
            return 'CIN_ML'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 192:
            return 'CAPE_ML'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 193:
            return 'CIN_MU'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 193:
            return 'CAPE_MU'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 'SDI_2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 'SDI_1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'PP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202:
            return 'DQI_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 'FRESHSNW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201:
            return 'DQC_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200:
            return 'DQV_GSP'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'DT_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196:
            return 'Q_SEDIM'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199:
            return 'DQI_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198:
            return 'DQC_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 4:
            return 'SNOWLMT'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'HTOP_DC'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193:
            return 'DV_CON'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192:
            return 'DU_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197:
            return 'DQV_CON'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192:
            return 'DT_CON'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 'TOP_CON'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'BAS_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195:
            return 'CLW_CON'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'HTOP_SC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'HBAS_SC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194:
            return 'QI_RAD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193:
            return 'QC_RAD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'TDIV_HUM'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 'RSTOM'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 106:
            return 'ALHFL_PL'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 'ALHFL_BS'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192:
            return 'THHR_RAD'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192:
            return 'SOHR_RAD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26 and typeOfStatisticalProcessing == 2:
            return 'MCNV_CTMAX'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 25:
            return 'ECHOTOPinM'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 25:
            return 'ECHOTOP'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62200:
            return 'AMBRrprec'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'AMBRfr'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62200:
            return 'AMBR'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62300:
            return 'POACrprec'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'POACfr'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62300:
            return 'POAC'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62100:
            return 'ALNUrprec'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'ALNUfr'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62100:
            return 'ALNU'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62101:
            return 'BETUrprec'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'BETUfr'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62101:
            return 'BETU'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'VABSMX_10M'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'VGUST_DYN_10M'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'RELHUM_2M_L'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'TD_2M_L'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'T_2M_L'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 'RELV'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'DBZ_CTMAX'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5:
            return 'DBZCMP_SIM'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5 and typeOfGeneratingProcess == 8:
            return 'DBZCMP_OBS'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 81 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'TCOND_MAX'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 81 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 20 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 26315:
            return 'TCOND10_MX'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 15 and typeOfStatisticalProcessing == 2:
            return 'UH_MAX'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 23:
            return 'HBAS_RADIONUC_CLD'

        modeNumber = h.get_l('modeNumber')
        typeOfDistributionFunction = h.get_l('typeOfDistributionFunction')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 8:
            return 'ACCEMISS_DUSTC'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 8:
            return 'ACCEMISS_DUSTA'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 8:
            return 'ACCEMISS_DUSTB'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 8:
            return 'EMISS_DUSTA'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 8:
            return 'EMISS_DUSTC'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 8:
            return 'EMISS_DUSTB'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 24:
            return 'HTOP_RADIONUC_CLD'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 22 and constituentType == 62001:
            return 'HTOP_DUST_CLD'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 22 and constituentType == 62025:
            return 'HTOP_ASH_CLD'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 21 and constituentType == 62001:
            return 'HBAS_DUST_CLD'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 21 and constituentType == 62025:
            return 'HBAS_ASH_CLD'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 17 and typeOfFirstFixedSurface == 10:
            return 'RADIONUC_AC_VI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 99:
            return 'DENH'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 39:
            return 'DENI'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 38:
            return 'DENC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 98:
            return 'DENG'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 97:
            return 'DENS'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 96:
            return 'DENR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 107:
            return 'NDHAIL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 106:
            return 'NDGRAUPEL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 105:
            return 'NDSNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 103:
            return 'NCHAIL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 102:
            return 'NCGRAUPEL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 101:
            return 'NCSNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 104:
            return 'NDRAIN'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 100:
            return 'NCRAIN'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 116:
            return 'QS_LIQ'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 113:
            return 'QG_LIQ'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 110:
            return 'QH_LIQ'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ATHU_S'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'THUS_RAD'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 8:
            return 'SODT_RAD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 'MCONV'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'TOT_PR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 4:
            return 'SNOW_CON_D'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 4:
            return 'RAIN_CON_D'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 4:
            return 'SNOW_GSP_D'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 4:
            return 'RAIN_GSP_D'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102:
            return 'AEROSOL_OPTICAL_DEPTH'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and constituentType == 62025:
            return 'ASH_MAX_TOTAL_MC_LAYER'

        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 20000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10000 and constituentType == 62025:
            return 'ASH_MAX_TOTAL_MC_390_530'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 38500 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 20000 and constituentType == 62025:
            return 'ASH_MAX_TOTAL_MC_245_390'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 70000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 38500 and constituentType == 62025:
            return 'ASH_MAX_TOTAL_MC_100_245'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 24000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 9100 and constituentType == 62025:
            return 'ASH_MAX_TOTAL_MC_350_550'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 101325 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 70000 and constituentType == 62025:
            return 'ASH_MAX_TOTAL_MC_SFC_100'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 46500 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 24000 and constituentType == 62025:
            return 'ASH_MAX_TOTAL_MC_200_350'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 15:
            return 'RADIONUC_MAX_AC_LAYER'

        aerosolType = h.get_l('aerosolType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62008:
            return 'AOD_SEAS'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62001:
            return 'AOD_DUST'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62025:
            return 'AOD_ASH'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 62 and constituentType == 62025:
            return 'ASH_HML_MAX'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and typeOfFirstFixedSurface == 10 and constituentType == 62025:
            return 'ASH_TOTAL_MC_VI'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 101325 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 46500 and constituentType == 62025:
            return 'ASH_MAX_TOTAL_MC_SFC_200'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 0 and constituentType == 62025:
            return 'ASH_TOTAL_MC'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30102:
            return 'Ru_103'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30175:
            return 'Ba_140'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30139:
            return 'I_131o'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30138:
            return 'I_131g'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30161:
            return 'Xe_133'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30079:
            return 'Zr_95'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30129:
            return 'Te_132'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30141:
            return 'I_131a'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30172:
            return 'Cs_137'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'SEASC0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'SEASB0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'SEASA0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'SEASC'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'SEASB'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'SEASA'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'DUSTC0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'DUSTB0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'DUSTA0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'DUSTC'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'DUSTB'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'DUSTA'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'ASHC0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'ASHB0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'ASHA0'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'ASHC'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'ASHB'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'ASHA'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 6 and typeOfDistributionFunction == 1:
            return 'ASH6'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 5 and typeOfDistributionFunction == 1:
            return 'ASH5'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 4 and typeOfDistributionFunction == 1:
            return 'ASH4'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 1:
            return 'ASH3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 1:
            return 'ASH2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 1:
            return 'ASH1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 42:
            return 'V_G'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 41:
            return 'U_G'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 21:
            return 'UTCI_SUN'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 27 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'TW_2M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 27:
            return 'TW'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 3:
            return 'TTOP_CON'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'THETA_V_2M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'THETAE_2M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'TD'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'PT_2M'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10 and typeOfFirstFixedSurface == 10:
            return 'SLI'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 13:
            return 'SI'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 17:
            return 'RI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 94:
            return 'RH_ICE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'MIXRAT_2M'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2:
            return 'MIXRAT'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 5:
            return 'LCL_ML'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ASOD_S'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 44:
            return 'SP_G'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'D_TD_2M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7:
            return 'D_TD'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 43:
            return 'DD_G'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 3000:
            return 'CAPE_3KM'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 16:
            return 'BRN'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'ABSH_2M'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'ACCTHD_S'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ATHD_S'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'THDS_RAD'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 31:
            return 'NDICE'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 30:
            return 'NDCLOUD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 73 and typeOfStatisticalProcessing == 1:
            return 'HAIL_GSP'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 14:
            return 'DBZ_HAIL'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 13:
            return 'DBZ_GRAUPEL'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 12:
            return 'DBZ_RAIN'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 11:
            return 'DBZ_SNOW'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 10:
            return 'DBZ_ICE'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 9:
            return 'DBZ_CLOUD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 73:
            return 'PRH_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 72:
            return 'TQH'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 71:
            return 'QH'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 20:
            return 'SQSL'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 23:
            return 'MXWP'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 24:
            return 'MXWH'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 44:
            return 'BEFI'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 43:
            return 'SKUR'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 45:
            return 'GODA'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 33:
            return 'SPRS'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 30:
            return 'TM2S'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 27:
            return 'TM1S'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 32:
            return 'SPRW'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 29:
            return 'TM2W'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 26:
            return 'TM1W'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 19:
            return 'STRS'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 16:
            return 'DRAG'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 17:
            return 'USTR'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14:
            return 'DPTH'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 35:
            return 'LUC'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfStatisticalProcessing == 0:
            return 'AVDIS_SSO'

        numberOfGridInReference = h.get_l('numberOfGridInReference')

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and numberOfGridInReference == 2 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 1:
            return 'HSURF_V'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'VMFL_S'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'UMFL_S'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfFirstFixedSurface == 1:
            return 'SWDIFUS_RAD'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 'SATOSM'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 36:
            return 'FR_LUC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'VAPP'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'SNOHF'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 'WILT'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'ST'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'WMIXE'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'CIN'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'SWRAD'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'LWRAD'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'NSWRS'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'DIRSW'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 'ICED'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 'ICEG'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 'VICE'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 'UICE'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'SICED'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'DICED'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 'S'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 'SSW'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 'BLI'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'MTHA'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'MTHD'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'TTHDP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'ACPCP'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 'TSTM'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 'PRATE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 'SATD'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'PWAT'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'VCURR'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'UCURR'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 'ABSD'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 'SGCVV'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'MNTSF'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 'GPA'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 'PRESA'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 'TA'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 'PLI'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return 'RDSP3'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return 'RDSP2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'VIS'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'TMIN'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'TMAX'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'HSTDV'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 'TSEC'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'DSLM'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 'PERSW'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 'PERPW'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'DIRPW'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return 'ATMDIV'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return 'RFL39'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return 'RFL16'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return 'RFL08'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return 'RFL06'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 'SOLZA'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 'NPIXU'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 'ESTV'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 'ESTU'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 'CTOPHQI'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 'IRRATE'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 'ESTP'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 16:
            return 'VSOSM'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 15:
            return 'SOILP'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 14:
            return 'DIREC'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 13:
            return 'VOLDEC'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12:
            return 'TRANSO'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 11:
            return 'VOLTSO'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 10:
            return 'LIQVSM'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 9:
            return 'POROS'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 8:
            return 'SMDRY'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 7:
            return 'SMREF'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 'RLYRS'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 5:
            return 'SOIL1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 4:
            return 'BOTLST'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 3:
            return 'LOWLSM'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 2:
            return 'UPLSM'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 1:
            return 'UPLST'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 'VWILTM'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 'VSW'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 'HFLUX'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 'CISOILW'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 'RCQ'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 'RCSOL'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 'RCS'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 'CCOND'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 'BMIXL'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 'SFEXC'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return 'MSTAV'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 10:
            return 'GFLUX'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 'SOILW'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 'LANDU'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 'EVAPT'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return 'POP'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return 'PPOSP'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 'CPPOP'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 'SSRUN'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 'BGRUN'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return 'SWEPON'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return 'ESCT'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return 'RSSC'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 'FFLDRO'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 'FFLDG'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 'TSEC'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return 'SLDP'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return 'CAT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return 'ICT'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return 'CBHEXT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return 'ICI'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 17:
            return 'MXALB'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 'CONTB'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 'CONTT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 'CONTET'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 'CONTI'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 'PBLREG'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 'TURB'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 'TURBB'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 'TURBT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 6:
            return 'ICIB'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 5:
            return 'ICIT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 'VOLASH'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 8:
            return 'TIACRP'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 7:
            return 'TIACIP'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 6:
            return 'TIACCP'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 5:
            return 'GDRADP'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 4:
            return 'GDIOD'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 3:
            return 'GDCES'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 2:
            return 'ACRADP'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 1:
            return 'ACIOD'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 0:
            return 'ACCES'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5 and typeOfStatisticalProcessing == 1:
            return 'PREC'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 'LMAXBR'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 'VERIL'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 'BRVEL'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 'BSWID'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'AEROT'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return '4LFTX'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 'LFTX'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 'EHLX'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 'SX'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 'TOTALX'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 'KX'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 'CDCIMR'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 21:
            return 'FICE'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'TCOLC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 19:
            return 'TCOLI'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 18:
            return 'TCOLW'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 17:
            return 'TCOND1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 16:
            return 'CUEFI'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 15:
            return 'CWORK'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'CDCT'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'CDCB'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 10:
            return 'THUNC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 9:
            return 'TMAXT'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 8:
            return 'CDCT'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return 'CDCA'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'CWAT'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 'CICE'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'NLWRCS'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'ULWRF'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'DLWRF'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'NLWRT'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'NLWRS'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 'DWUVR'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 'NSWRFCS'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 'DSWRF'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'NSWRT'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return '5WAVA'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 'HPBL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 'V-GWD'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 'U-GWD'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return '5WAVH'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 'DENALT'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 'PRESALT'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 14:
            return 'MINDPD'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 'THICK'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 'VSTM'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 'USTM'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 'MFLX'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'VGUST'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 'UGUST'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'MAXGUST'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 'IPRATE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 'FPRATE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'SDWE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 'LSSRATE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 'CSRATE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'SF'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'TSNOWP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'TWATP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 48:
            return 'CWP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 47:
            return 'LSWP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'RIME'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'FRAIN'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 'PEVPR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 'PEVAP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return 'CPOFP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return 'CSNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return 'CICEP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return 'CFRZR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return 'CRAIN'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 'HAIL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 'PWCAT'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 29:
            return 'ASNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 28:
            return 'MAXAH'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 27:
            return 'MAXRH'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 'ICMR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 21:
            return 'TCOND'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 20:
            return 'ILIQW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 19:
            return 'PTYPE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18:
            return 'ABSH'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 17:
            return 'SNOAG'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 'SNOL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 'SNOC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 'SRWEQ'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 'NCPCP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'TCW'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'HEATX'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'BTMP'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'SUND'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'BLD'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'PT'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 'VVCSH'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 'VUCSH'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'VTMP'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 1:
            return 'RUNOFF_G'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 'RUNOFF_S'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 80000:
            return 'CLCL'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 80000 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 40000:
            return 'CLCM'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 40000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 'CLCH'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return 'SNOWC'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'SKT'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'VPOT'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'STRF'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 12:
            return 'SALT_LK'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 114:
            return 'W_SNOW_M'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 114:
            return 'RHO_SNOW_M'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 114:
            return 'H_SNOW_M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18 and typeOfFirstFixedSurface == 114:
            return 'T_SNOW_M'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'ACCSOB_T'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'ACCTHB_T'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'ACCTHB_S'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'ACCSOB_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'ACCSHFL_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'ACCLHFL_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 'SHFL_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'LHFL_S'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 29:
            return 'NCICE'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 28:
            return 'NCCLOUD'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 2:
            return 'VLON'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 2:
            return 'VLAT'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 3:
            return 'ELON'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 3:
            return 'ELAT'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 1:
            return 'CLON'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 1:
            return 'CLAT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return 'ALB_DIF'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18 and typeOfStatisticalProcessing == 0:
            return 'ALB_DIF12'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'QV_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 'LAPSE_RATE'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'CURS'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'CURD'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'THETA_V'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 35:
            return 'VT'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 34:
            return 'VN'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 26:
            return 'EXNER'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'GRAD'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'ICAHT'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16 and typeOfStatisticalProcessing == 1:
            return 'SNOW_MELT'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 33 and typeOfStatisticalProcessing == 1:
            return 'DURSUN'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 50 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 7:
            return 'W_G4'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 7 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'W_G3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'T_S_L'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25:
            return 'LNPS'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 'RDIV'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'GH'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'SM'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 19:
            return 'SM'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 4:
            return 'PREC_CON_D'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 'ALTS'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'DEN'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'POT_VORTIC'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 'VORTIC_W'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 'CL_TOP_HEIGHT'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 3 and typeOfSecondFixedSurface == 165 and typeOfFirstFixedSurface == 162:
            return 'H_B1_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 4 and typeOfFirstFixedSurface == 165:
            return 'T_B1_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 10 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 166:
            return 'C_T_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 0 and typeOfSecondFixedSurface == 166 and typeOfFirstFixedSurface == 1:
            return 'H_ML_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 162:
            return 'T_BOT_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfSecondFixedSurface == 166 and typeOfFirstFixedSurface == 1:
            return 'T_WML_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'T_MNW_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 4 and typeOfFirstFixedSurface == 164:
            return 'T_BS_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 3 and typeOfSecondFixedSurface == 164 and typeOfFirstFixedSurface == 162:
            return 'DP_BS_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 11 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'GAMSO_LK'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 33:
            return 'FETCH_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 0 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'DEPTH_LK'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 2:
            return 'FR_LAKE'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ASWDIFU_S'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'ABSV'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'T_SEA'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'WCF'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0 and typeOfStatisticalProcessing == 1:
            return 'TOT_O3'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50 and typeOfStatisticalProcessing == 2:
            return 'UVI_MAX_CS'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 'ATHB_S'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 'ASOB_S'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8 and typeOfGeneratingProcess == 1:
            return 'ATHB_T'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8 and typeOfGeneratingProcess == 1:
            return 'ASOB_T'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 4:
            return 'TOT_PREC_D'

        satelliteSeries = h.get_l('satelliteSeries')
        satelliteNumber = h.get_l('satelliteNumber')
        instrumentType = h.get_l('instrumentType')
        scaledValueOfCentralWaveNumber = h.get_l('scaledValueOfCentralWaveNumber')

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'OBSMSG_BT_WV7.3'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'OBSMSG_BT_WV6.2'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'OBSMSG_BT_IR9.7'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'OBSMSG_BT_IR8.7'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'OBSMSG_BT_IR3.9'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'OBSMSG_BT_IR13.4'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 83333:
            return 'OBSMSG_BT_IR12.0'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'OBSMSG_BT_IR10.8'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1250000:
            return 'OBSMSG_ALB_VIS0.8'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1666666:
            return 'OBSMSG_ALB_VIS0.6'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 625000:
            return 'OBSMSG_ALB_NIR1.6'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 2000000:
            return 'OBSMSG_ALB_HRV'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 198:
            return 'VMAX_10M_C'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 198:
            return 'SNOW_GSP_C'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 198:
            return 'TOT_PREC_C'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'VMAX_10M_S'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 197:
            return 'T_S_S'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 197:
            return 'SNOW_GSP_S'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 197:
            return 'CLCH_S'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400 and typeOfGeneratingProcess == 197:
            return 'CLCM_S'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800 and typeOfGeneratingProcess == 197:
            return 'CLCL_S'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfGeneratingProcess == 197:
            return 'CLCT_S'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 197:
            return 'TOT_PREC_S'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'V_10M_S'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'U_10M_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'TD_2M_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'TMIN_2M_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'TMAX_2M_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'T_2M_S'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'SYNMSG_RAD_CS_WV7.3'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'SYNMSG_RAD_CS_WV6.2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'SYNMSG_RAD_CS_IR9.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'SYNMSG_RAD_CS_IR8.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'SYNMSG_RAD_CS_IR3.9'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'SYNMSG_RAD_CS_IR13.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'SYNMSG_RAD_CS_IR12.1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'SYNMSG_RAD_CS_IR10.8'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'SYNMSG_RAD_CL_WV7.3'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'SYNMSG_RAD_CL_WV6.2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'SYNMSG_RAD_CL_IR9.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'SYNMSG_RAD_CL_IR8.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'SYNMSG_RAD_CL_IR3.9'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'SYNMSG_RAD_CL_IR13.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'SYNMSG_RAD_CL_IR12.1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'SYNMSG_RAD_CL_IR10.8'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'SYNMSG_BT_CS_WV7.3'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'SYNMSG_BT_CS_WV6.2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'SYNMSG_BT_CS_IR9.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'SYNMSG_BT_CS_IR3.9'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'SYNMSG_BT_CS_IR13.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'SYNMSG_BT_CS_IR12.1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'SYNMSG_BT_CS_IR10.8'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'SYNMSG_BT_CS_IR8.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'SYNMSG_BT_CL_WV7.3'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'SYNMSG_BT_CL_WV6.2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'SYNMSG_BT_CL_IR9.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'SYNMSG_BT_CL_IR8.7'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'SYNMSG_BT_CL_IR3.9'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'SYNMSG_BT_CL_IR13.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'SYNMSG_BT_CL_IR12.1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'SYNMSG_BT_CL_IR10.8'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'SYNME7_RAD_CS_WV6.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'SYNME7_RAD_CS_IR11.5'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'SYNME7_RAD_CL_WV6.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'SYNME7_RAD_CL_IR11.5'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'SYNME7_BT_CS_WV6.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'SYNME7_BT_CS_IR11.5'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'SYNME7_BT_CL_WV6.4'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'SYNME7_BT_CL_IR11.5'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'SYNME6_RAD_CS'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'SYNME6_RAD_CL'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'SYNME6_BT_CS'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'SYNME6_BT_CL'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'SYNME5_RAD_CS'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'SYNME5_RAD_CL'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'SYNME5_BT_CS'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'SYNME5_BT_CL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'EIA-OM'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'EFA-OM'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'EIA-T'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'EFA-T'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'EIA-RH'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'EFA-RH'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'EIA-FI'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'EFA-FI'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'EIA-V'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'EFA-V'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'EIA-U'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'EFA-U'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'EIA-PS'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'EFA-PS'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'ICE_GRD'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 'CEILING'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'THETAE'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 'KO'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 107:
            return 'PTHETA'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 25:
            return 'WW'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 2:
            return 'CCL_GND'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 'SRH'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 'W_SHAER'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51 and typeOfStatisticalProcessing == 2:
            return 'UVI_MAX_CL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23:
            return 'VDIS_SSO'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30175:
            return 'Ba-140w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30175:
            return 'Ba-140d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30175:
            return 'Ba-140'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30139:
            return 'I-131ow'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30139:
            return 'I-131od'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30139:
            return 'I-131o'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30138:
            return 'I-131gw'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30138:
            return 'I-131gd'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30138:
            return 'I-131g'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30161:
            return 'Xe-133w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30161:
            return 'Xe-133d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30161:
            return 'Xe-133'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30000:
            return 'Tr-2w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30000:
            return 'Tr-2d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30000:
            return 'Tr-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30059:
            return 'Kr-85w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30059:
            return 'Kr-85d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30059:
            return 'Kr-85'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30079:
            return 'Zr-95w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30079:
            return 'Zr-95d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30079:
            return 'Zr-95'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30129:
            return 'Te-132w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30129:
            return 'Te-132d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30129:
            return 'Te-132'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30172:
            return 'Cs-137w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30172:
            return 'Cs-137d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30172:
            return 'Cs-137'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30141:
            return 'I-131aw'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30141:
            return 'I-131ad'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30141:
            return 'I-131a'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30067:
            return 'Sr-90w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30067:
            return 'Sr-90d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30067:
            return 'Sr-90'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30102:
            return 'Ru-103w'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30102:
            return 'Ru-103d'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30102:
            return 'Ru-103'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'O3'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'USTAR'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2:
            return 'RLON'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1:
            return 'RLAT'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62008:
            return 'AER_SS12'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62008:
            return 'AER_SS'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62009:
            return 'AER_BC12'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62009:
            return 'AER_BC'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62010:
            return 'AER_ORG12'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62010:
            return 'AER_ORG'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62001:
            return 'AER_DUST12'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62001:
            return 'AER_DUST'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62006:
            return 'AER_SO412'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62006:
            return 'AER_SO4'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 2:
            return 'NDVI_MAX'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 0:
            return 'NDVI'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 30:
            return 'FOR_D'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 29:
            return 'FOR_E'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'ORO_MOD'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 3:
            return 'LAI_MN'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 2:
            return 'LAI_MX'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 3:
            return 'PLCOV_MN'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 2:
            return 'PLCOV_MX'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 32:
            return 'ROOTDP'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28:
            return 'LAI'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'SSO_SIGMA'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21:
            return 'SSO_THETA'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24:
            return 'SSO_GAMMA'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'SSO_STDH'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 31:
            return 'SPRD'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 'TM02'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 25:
            return 'TM01'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 'TM10'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 'PP1D'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 35:
            return 'PPWW'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 36:
            return 'PPTS'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'MWD'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'CAPE_CON'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'DBZ_CMAX'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 'DBZ'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'DBZ_850'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 'T_ICE'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 'RSMIN'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18:
            return 'T_SNOW'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 'W_I'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'W_SO_ICE'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'W_SO'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106:
            return 'T_SO'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'VMAX_10M'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'MH'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 19:
            return 'TCH'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 'TCM'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20:
            return 'TKVH'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 31:
            return 'TKVM'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'TKE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 24:
            return 'TKE_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 'RHO_SNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfStatisticalProcessing == 1:
            return 'GRAU_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75:
            return 'PRG_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfStatisticalProcessing == 1:
            return 'TOT_SNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfStatisticalProcessing == 1:
            return 'TOT_RAIN'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 1:
            return 'RAIN_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 'PRS_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76:
            return 'PRR_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 1:
            return 'RAIN_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 'PRS_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77:
            return 'PRR_GSP'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 4:
            return 'HZEROCL'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'HTOP_CON'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'HBAS_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 78:
            return 'TWATER'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 74:
            return 'TQG'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'QG'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'TQS'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'TQR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 'QS'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 'QR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82:
            return 'QI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 'QC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return 'CLC_SGS'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return 'CLC'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'PABS_RAD'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'APAB_S'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'AVMFL_S'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'AUMFL_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ASHFL_S'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ALHFL_S'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 8:
            return 'THBT_RAD'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8:
            return 'ATHB_T'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 8:
            return 'SOBT_RAD'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8:
            return 'ASOB_T'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'THBS_RAD'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ATHB_S'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'SOBS_RAD'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'ASOB_S'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 'MPTS'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'SHTS'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'MDTS'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'MPWW'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'SHWW'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'MDWW'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'SWH'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'H_ICE'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'FR_ICE'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'RUNOFF_S'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 10:
            return 'RUNOFF_G'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return 'PLCOV'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 100 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 10:
            return 'W_G2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 10 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'W_G1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 190 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 100:
            return 'W_CL'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'T_S'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 9:
            return 'T_M'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 41:
            return 'T_CL_LM'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 36:
            return 'T_CL'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfStatisticalProcessing == 0:
            return 'ALBEDO_B'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return 'ALB_RAD'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'Z0'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'FR_LAND'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1:
            return 'SNOW_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 1:
            return 'SNOW_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69:
            return 'TQC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0:
            return 'CLCH'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400:
            return 'CLCM'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800:
            return 'CLCL'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return 'CLC_CON'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'CLCT'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'H_SNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60:
            return 'W_SNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1:
            return 'PREC_CON'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1:
            return 'PREC_GSP'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1:
            return 'TOT_PREC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70:
            return 'TQI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'AEVAP_S'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 'TQV'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'RELHUM'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'RELHUM_2M'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'QV'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'QV_2M'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'W'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'OMEGA'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'V'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'V_10M'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'U'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'U_10M'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'SP'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'SP_10M'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'DD'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'DD_10M'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'WVSP3'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'WVSP2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'WVSP1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'DBZ_MAX'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'TD_2M_AV'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'TD_2M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'TMIN_2M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'TMAX_2M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'T'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 9:
            return 'T_2M_CL'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'T_2M_AV'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'T_2M'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'T_G'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 'TO3'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101:
            return 'HHL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 1:
            return 'HSURF'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'FI'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfSecondFixedSurface == 105 and typeOfFirstFixedSurface == 105:
            return 'FIF'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'FIS'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'DPSDT'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'PMSL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'P'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'PS'

    return wrapped
