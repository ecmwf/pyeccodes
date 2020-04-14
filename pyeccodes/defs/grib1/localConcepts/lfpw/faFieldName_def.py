import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        indicatorOfParameter = h.get_l('indicatorOfParameter')
        table2Version = h.get_l('table2Version')

        if indicatorOfParameter == 255 and table2Version == 255:
            return 'default'

        LSTCUM = h.get_l('LSTCUM')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')
        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if LSTCUM == 1 and indicatorOfParameter == 137 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SURFRAYT_DIR_SUR'

        if indicatorOfParameter == 40 and table2Version == 1 and timeRangeIndicator == 0:
            return 'VERT.VELOC'

        if indicatorOfParameter == 38 and table2Version == 159 and timeRangeIndicator == 0:
            return 'THETA_VIRT'

        if indicatorOfParameter == 31 and table2Version == 159 and timeRangeIndicator == 0:
            return 'SIM_REFLEC'

        if indicatorOfParameter == 34 and table2Version == 159 and timeRangeIndicator == 0:
            return 'SNOW'

        if indicatorOfParameter == 33 and table2Version == 159 and timeRangeIndicator == 0:
            return 'RAIN'

        if indicatorOfParameter == 247 and table2Version == 128 and timeRangeIndicator == 0:
            return 'ICE_CRYSTA'

        if indicatorOfParameter == 35 and table2Version == 159 and timeRangeIndicator == 0:
            return 'GRAUPEL'

        if indicatorOfParameter == 32 and table2Version == 159 and timeRangeIndicator == 0:
            return 'CLOUD_WATE'

        if indicatorOfParameter == 217 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 159 and timeRangeIndicator == 0:
            return 'SURFREFLECT.MAX'

        if indicatorOfParameter == 248 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 159 and timeRangeIndicator == 0:
            return 'SURFDIAGHAIL'

        if LSTCUM == 1 and indicatorOfParameter == 150 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 2 and timeRangeIndicator == 4:
            return 'SURFACCPLUIE'

        if LSTCUM == 1 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFACCNEIGE'

        if LSTCUM == 1 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 159 and timeRangeIndicator == 4:
            return 'SURFACCGRAUPEL'

        if indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 20 and level == 27315 and table2Version == 128 and timeRangeIndicator == 0:
            return 'SURFISOTPW1.MALT'

        if indicatorOfParameter == 135 and table2Version == 128 and timeRangeIndicator == 0:
            return 'EDR'

        if indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 100 and level == 108 and table2Version == 129 and timeRangeIndicator == 0:
            return 'C006_METEOSAT_09'

        if indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 100 and level == 62 and table2Version == 129 and timeRangeIndicator == 0:
            return 'C002_METEOSAT_09'

        if indicatorOfParameter == 34 and table2Version == 1 and timeRangeIndicator == 0:
            return 'VENT_MERIDIE'

        if indicatorOfParameter == 13 and table2Version == 1 and timeRangeIndicator == 0:
            return 'TEMPE_POTENT'

        if indicatorOfParameter == 6 and table2Version == 1 and timeRangeIndicator == 0:
            return 'GEOPOTENTIEL'

        if indicatorOfParameter == 41 and table2Version == 1 and timeRangeIndicator == 0:
            return 'ABS_VORTICIT'

        if indicatorOfParameter == 167 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFTOT.WAT.VAPO'

        if LSTCUM == 1 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFTENS.TOTA.ZO'

        if LSTCUM == 1 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFTENS.TOTA.ME'

        if indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFTEMPERATURE'

        if indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFRESERV.NEIGE'

        bottomLevel = h.get_l('bottomLevel')
        topLevel = h.get_l('topLevel')

        if bottomLevel == 1 and indicatorOfParameter == 152 and indicatorOfTypeOfLevel == 112 and table2Version == 1 and timeRangeIndicator == 0 and topLevel == 0:
            return 'SURFRESERV.GLACE'

        if bottomLevel == 1 and indicatorOfParameter == 153 and indicatorOfTypeOfLevel == 112 and table2Version == 1 and timeRangeIndicator == 0 and topLevel == 0:
            return 'SURFRESERV.EAU'

        if LSTCUM == 1 and indicatorOfParameter == 104 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 149 and timeRangeIndicator == 4:
            return 'SURFRAYT_THER_DE'

        if LSTCUM == 1 and indicatorOfParameter == 169 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SURFRAYT_THER_CL'

        if LSTCUM == 1 and indicatorOfParameter == 168 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SURFRAYT_SOL_CL'

        if LSTCUM == 1 and indicatorOfParameter == 105 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 149 and timeRangeIndicator == 4:
            return 'SURFRAYT_SOLA_DE'

        if LSTCUM == 1 and indicatorOfParameter == 158 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFRAYT.LUNE.DE'

        if indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFPRESSION'

        if LSTCUM == 1 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFPREC.NEI.GEC'

        if LSTCUM == 1 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFPREC.NEI.CON'

        if LSTCUM == 1 and indicatorOfParameter == 62 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFPREC.EAU.GEC'

        if LSTCUM == 1 and indicatorOfParameter == 63 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFPREC.EAU.CON'

        FMULTM = h.get_l('FMULTM')
        FMULTE = h.get_l('FMULTE')

        if FMULTM == 1 and FMULTE == 2 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFNEBUL.TOTALE'

        if FMULTM == 1 and FMULTE == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFNEBUL.MOYENN'

        if indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFNEBUL.HAUTE'

        if FMULTM == 1 and FMULTE == 2 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFNEBUL.CONVEC'

        if FMULTM == 1 and FMULTE == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFNEBUL.BASSE'

        if indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 20 and level == 27315 and table2Version == 128 and timeRangeIndicator == 0:
            return 'SURFISOTPW0.MALT'

        if LSTCUM == 1 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SURFFLU.RAY.THER'

        if LSTCUM == 1 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SURFFLU.RAY.SOLA'

        if LSTCUM == 1 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 4:
            return 'SURFFLU.MTOTA.NE'

        if LSTCUM == 1 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SURFFLU.LAT.MTOT'

        if LSTCUM == 1 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SURFFLU.CHA.SENS'

        if indicatorOfParameter == 160 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'SURFCAPE.POS.F00'

        if indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 159 and timeRangeIndicator == 0:
            return 'SURFCAPE.MOD.XFU'

        if LSTCUM == 1 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SOMMFLU.RAY.THER'

        if LSTCUM == 1 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and level == 0 and table2Version == 128 and timeRangeIndicator == 4:
            return 'SOMMFLU.RAY.SOLA'

        if indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 111 and level == 10 and table2Version == 1 and timeRangeIndicator == 0:
            return 'PROFTEMPERATURE'

        if bottomLevel == 250 and indicatorOfParameter == 152 and indicatorOfTypeOfLevel == 112 and table2Version == 1 and timeRangeIndicator == 0 and topLevel == 0:
            return 'PROFRESERV.GLACE'

        if bottomLevel == 250 and indicatorOfParameter == 153 and indicatorOfTypeOfLevel == 112 and table2Version == 1 and timeRangeIndicator == 0 and topLevel == 0:
            return 'PROFRESERV.EAU'

        if indicatorOfParameter == 44 and table2Version == 1 and timeRangeIndicator == 0:
            return 'DIVERGENCE'

        if indicatorOfParameter == 39 and table2Version == 1 and timeRangeIndicator == 0:
            return 'VITESSE_VE'

        if indicatorOfParameter == 14 and table2Version == 1 and timeRangeIndicator == 0:
            return 'THETA_PRIM'

        if indicatorOfParameter == 4 and table2Version == 1 and timeRangeIndicator == 0:
            return 'POT_VORTIC'

        if indicatorOfParameter == 6 and table2Version == 1 and timeRangeIndicator == 0:
            return 'GEOPOTENTI'

        if indicatorOfParameter == 41 and table2Version == 1 and timeRangeIndicator == 0:
            return 'ABS_VORTIC'

        if indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 102 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'MSLPRESSURE'

        if indicatorOfParameter == 8 and table2Version == 128 and timeRangeIndicator == 0:
            return 'ISOT_ALTIT'

        if indicatorOfParameter == 33 and table2Version == 1 and timeRangeIndicator == 0:
            return 'VENT_ZONAL'

        if indicatorOfParameter == 34 and table2Version == 1 and timeRangeIndicator == 0:
            return 'VENT_MERID'

        if indicatorOfParameter == 37 and table2Version == 159 and timeRangeIndicator == 0:
            return 'TKE'

        if indicatorOfParameter == 11 and table2Version == 1 and timeRangeIndicator == 0:
            return 'TEMPERATUR'

        if indicatorOfParameter == 247 and table2Version == 128 and timeRangeIndicator == 0:
            return 'RAD_SOLID_'

        if indicatorOfParameter == 32 and table2Version == 159 and timeRangeIndicator == 0:
            return 'RAD_LIQUID'

        if indicatorOfParameter == 1 and table2Version == 1 and timeRangeIndicator == 0:
            return 'PRESSURE'

        if FMULTM == 1 and FMULTE == 2 and indicatorOfParameter == 52 and table2Version == 1 and timeRangeIndicator == 0:
            return 'HUMI_RELAT'

        if indicatorOfParameter == 36 and table2Version == 159 and timeRangeIndicator == 0:
            return 'CLOUD_FRAC'

        if indicatorOfParameter == 164 and indicatorOfTypeOfLevel == 105 and level == 10 and table2Version == 1 and timeRangeIndicator == 0:
            return 'CLSV.RAF.MOD.XFU'

        if indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10 and table2Version == 1 and timeRangeIndicator == 0:
            return 'CLSVENT.ZONAL'

        if indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10 and table2Version == 1 and timeRangeIndicator == 0:
            return 'CLSVENT.MERIDIEN'

        if indicatorOfParameter == 163 and indicatorOfTypeOfLevel == 105 and level == 10 and table2Version == 1 and timeRangeIndicator == 0:
            return 'CLSU.RAF.MOD.XFU'

        if indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and table2Version == 1 and timeRangeIndicator == 0:
            return 'CLSTEMPERATURE'

        if indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and table2Version == 1 and timeRangeIndicator == 2:
            return 'CLSMINI.TEMPERAT'

        if indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and table2Version == 1 and timeRangeIndicator == 2:
            return 'CLSMAXI.TEMPERAT'

        if FMULTM == 1 and FMULTE == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2 and table2Version == 1 and timeRangeIndicator == 0:
            return 'CLSHUMI.RELATIVE'

        if indicatorOfParameter == 166 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'CLPMOCON.MOD.XFU'

        if indicatorOfParameter == 165 and indicatorOfTypeOfLevel == 1 and level == 0 and table2Version == 1 and timeRangeIndicator == 0:
            return 'CLPMHAUT.MOD.XFU'

    return wrapped
