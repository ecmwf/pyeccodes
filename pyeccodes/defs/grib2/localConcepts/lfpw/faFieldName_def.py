import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get('discipline')
        parameterCategory = h.get('parameterCategory')
        parameterNumber = h.get('parameterNumber')

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return 'CLOUD_FRACTI'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'CLOUD_WATER'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'FONC.COURANT'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'GRAUPEL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'HUMI.SPECIFI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82:
            return 'ICE_CRYSTAL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 83:
            return 'LIQUID_WATER'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'POT.VITESSE'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 'PRESS.DEPART'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69:
            return 'RAD_LIQUID_W'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70:
            return 'RAD_SOLID_WA'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'RAIN'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5:
            return 'RAYT'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 'RAYT_SOL_CL'

        LSTCUM = h.get('LSTCUM')

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'RAYT_THER_CL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'SNOW'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 84:
            return 'SOLID_WATER'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'TEMPERATURE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'TKE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'VENT_MERIDIE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'VENT_ZONAL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 'VERTIC.DIVER'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'VITESSE_VERT'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'WIND.U.PHYS'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'WIND.V.PHYS'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'ABS_VORTIC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return 'CLOUD_FRAC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'CLOUD_WATE'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'GEOPOTENTI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'GRAUPEL'

        FMULTM = h.get('FMULTM')
        FMULTE = h.get('FMULTE')

        if FMULTM == 1 and FMULTE == 2 and discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'HUMI_RELAT'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82:
            return 'ICE_CRYSTA'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'PRESSURE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'POT_VORTIC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69:
            return 'RAD_LIQUID'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70:
            return 'RAD_SOLID_'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'RAIN'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 4:
            return 'SIM_REFLEC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'SNOW'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'TEMPERATUR'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'TEMPE_POTE'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'THETA_PRIM'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'TKE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'VENT_MERID'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'VENT_ZONAL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'ABS_VORTIC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return 'CLOUD_FRAC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'CLOUD_WATE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 'DIVERGENCE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 28:
            return 'EDR'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'GEOPOTENTI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'GRAUPEL'

        if FMULTM == 1 and FMULTE == 2 and discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'HUMI_RELAT'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82:
            return 'ICE_CRYSTA'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'POT_VORTIC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69:
            return 'RAD_LIQUID'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70:
            return 'RAD_SOLID_'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'RAIN'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 4:
            return 'SIM_REFLEC'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'SNOW'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'TEMPERATUR'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'THETA_PRIM'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'THETA_VIRT'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'TKE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'VENT_MERID'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'VENT_ZONAL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'VERT.VELOC'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'VITESSE_VE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'ABS_VORTICIT'

        if FMULTM == 101971621297793 and FMULTE == -15 and discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'GEOPOTENTIEL'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'TEMPE_POTENT'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'VENT_MERIDIE'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'VENT_ZONAL'

        typeOfFirstFixedSurface = h.get('typeOfFirstFixedSurface')

        if FMULTM == 101971621297793 and FMULTE == -15 and discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'SPECSURFGEOPOTEN'

        productDefinitionTemplateNumber = h.get('productDefinitionTemplateNumber')
        typeOfStatisticalProcessing = h.get('typeOfStatisticalProcessing')

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 32 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFACCGRAUPEL'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 50 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFACCNEIGE'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 49 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFACCPLUIE'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFAEROS.LAND'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFAEROS.DESERT'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFAEROS.SEA'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFAEROS.SOOT'

        if FMULTM == 1 and FMULTE == 2 and discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'SURFALBEDO'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 19 and typeOfFirstFixedSurface == 1:
            return 'SURFALBEDO_NEIGE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFALBEDO_HISTO'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'SURFALBEDO.SOLNU'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFALBEDO.VEG'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFA.OF.OZONE'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFB.OF.OZONE'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFC.OF.OZONE'

        level = h.get('level')

        if discipline == 0 and level == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'SURFCAPE.MOD.XFU'

        if discipline == 0 and level == 1 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'SURFCAPE.POS.F00'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31 and typeOfFirstFixedSurface == 1:
            return 'SURFDIAGHAIL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 1:
            return 'SURFDENSIT.NEIGE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 218 and typeOfFirstFixedSurface == 1:
            return 'SURFEMISSIVITE'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFEPAIS.SOL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFET.GEOPOTENT'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFFL.CT_TURBUL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFFL.Q_TURBUL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFFL.U_TURBUL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFFL.V_TURBUL'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFFLU.CHA.SENS'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 41 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFFLU.LAT.MEVA'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 62 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFFLU.LAT.MSUB'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 41 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFFLU.MEVAP.EA'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 62 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFFLU.MSUBL.NE'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFFLU.RAY.SOLA'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFFLU.RAY.THER'

        if FMULTM == 101971621297793 and FMULTE == -15 and discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'SURFGEOPOTENTIEL'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 216 and typeOfFirstFixedSurface == 1:
            return 'SURFGZ0.THERM'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfFirstFixedSurface == 1:
            return 'SURFIND.FOLIAIRE'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'SURFIND.TERREMER'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFIND.VEG.DOMI'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1:
            return 'SURFINSGRAUPEL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfFirstFixedSurface == 1:
            return 'SURFINSNEIGE'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfFirstFixedSurface == 1:
            return 'SURFINSPLUIE'

        if discipline == 0 and level == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20:
            return 'SURFISOT0.MALTIT'

        if discipline == 0 and level == -10 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20:
            return 'SURFISOTM10.MALT'

        if discipline == 0 and level == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 107:
            return 'SURFISOTPW0.MALT'

        if discipline == 0 and level == 1 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 107:
            return 'SURFISOTPW1.MALT'

        if FMULTM == 1 and FMULTE == 2 and discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'SURFNEBUL.TOTALE'

        if FMULTM == 1 and FMULTE == 2 and discipline == 0 and parameterCategory == 6 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'SURFNEBUL.CONVEC'

        if FMULTM == 1 and FMULTE == 2 and discipline == 0 and parameterCategory == 6 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'SURFNEBUL.BASSE'

        if FMULTM == 1 and FMULTE == 2 and discipline == 0 and parameterCategory == 6 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'SURFNEBUL.MOYENN'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'SURFNEBUL.HAUTE'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 48 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFPREC.EAU.CON'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 47 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFPREC.EAU.GEC'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 14 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFPREC.NEI.CON'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 1 and parameterNumber == 15 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFPREC.NEI.GEC'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25 and typeOfFirstFixedSurface == 1:
            return 'SURFPRESSION'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFPROP.ARGILE'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFPROP.SABLE'

        if FMULTM == 1 and FMULTE == 2 and discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'SURFPROP.VEGETAT'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 1:
            return 'SURFRAYT_DIR_SUR'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 4 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 'SURFRAYT_SOL_CL'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFRAYT_SOLA_DE'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 5 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'SURFRAYT_THER_CL'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'SURFRAYT_THER_DE'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 4 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFRAYT.LUNE.DE'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'SURFRAYT.SOLAIRE'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'SURFRAYT.TERREST'

        if discipline == 0 and parameterCategory == 255 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFREFLECT.MAX'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 'SURFRES.EVAPOTRA'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 1:
            return 'SURFRESERV.EAU'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 1:
            return 'SURFRESERV.GLACE'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 1:
            return 'SURFRESERV.INTER'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 'SURFRESERV.NEIGE'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16 and typeOfFirstFixedSurface == 1:
            return 'SURFRESI.STO.MIN'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'SURFTEMPERATURE'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 3 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'SURFTENS.DMOG.ME'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 3 and parameterNumber == 16 and typeOfFirstFixedSurface == 1:
            return 'SURFTENS.DMOG.ZO'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 2 and parameterNumber == 37 and typeOfFirstFixedSurface == 1:
            return 'SURFTENS.TURB.ME'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 2 and parameterNumber == 38 and typeOfFirstFixedSurface == 1:
            return 'SURFTENS.TURB.ZO'

        typeOfSecondFixedSurface = h.get('typeOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'SURFTOT.WAT.VAPO'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24 and typeOfFirstFixedSurface == 1:
            return 'SURFVAR.GEOP.ANI'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21 and typeOfFirstFixedSurface == 1:
            return 'SURFVAR.GEOP.DIR'

        if FMULTM == 101971621297793 and FMULTE == -15 and discipline == 2 and parameterCategory == 0 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'SURFZ0.FOIS.G'

        if discipline == 2 and level == 255 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106:
            return 'PROFRESERV.EAU'

        if discipline == 2 and level == 255 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 106:
            return 'PROFRESERV.GLACE'

        if discipline == 2 and level == 255 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106:
            return 'PROFTEMPERATURE'

        if discipline == 2 and level == 255 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106:
            return 'PROFXRUISSELLEME'

        if FMULTM == 1 and FMULTE == 2 and discipline == 0 and level == 2 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103:
            return 'CLSHUMI.RELATIVE'

        if discipline == 0 and level == 2 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 103:
            return 'CLSHUMI.SPECIFIQ'

        if discipline == 0 and level == 2 and parameterCategory == 1 and parameterNumber == 1 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 'CLSMAXI.HUMI.REL'

        if discipline == 0 and level == 2 and parameterCategory == 0 and parameterNumber == 0 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 'CLSMAXI.TEMPERAT'

        if discipline == 0 and level == 2 and parameterCategory == 1 and parameterNumber == 1 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3:
            return 'CLSMINI.HUMI.REL'

        if discipline == 0 and level == 2 and parameterCategory == 0 and parameterNumber == 0 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3:
            return 'CLSMINI.TEMPERAT'

        if discipline == 0 and level == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103:
            return 'CLSTEMPERATURE'

        if discipline == 0 and level == 10 and parameterCategory == 2 and parameterNumber == 23 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 0:
            return 'CLSU.RAF.MOD.XFU'

        if discipline == 0 and level == 10 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103:
            return 'CLSVENT.ZONAL'

        if discipline == 0 and level == 10 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103:
            return 'CLSVENT.MERIDIEN'

        if discipline == 0 and level == 10 and parameterCategory == 2 and parameterNumber == 24 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 0:
            return 'CLSV.RAF.MOD.XFU'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 8 and typeOfStatisticalProcessing == 1:
            return 'SOMMFLU.RAY.SOLA'

        if LSTCUM == 1 and discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 8 and typeOfStatisticalProcessing == 1:
            return 'SOMMFLU.RAY.THER'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 8:
            return 'SOMMRAYT.SOLAIRE'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 8:
            return 'SOMMRAYT.TERREST'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 8:
            return 'TOPRAYT_DIR_SOM'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'ATMONEBUL.TOTALE'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'ATMONEBUL.CONVEC'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'ATMONEBUL.BASSE'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'ATMONEBUL.MOYENN'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5 and productDefinitionTemplateNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'ATMONEBUL.HAUTE'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 255:
            return 'CLPMHAUT.MOD.XFU'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 255:
            return 'CLPMOCON.MOD.XFU'

        if discipline == 0 and level == 1 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'CUF1PRESSURE'

        if discipline == 0 and level == 2 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'CUF2PRESSURE'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'GEOMASK.FPOS'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'LAT_G_XY'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'LATGAUSS'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'LON_G_XY'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'LONGAUSS'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'MAP_FACTOR'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'MESHGAUSS'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 101:
            return 'MSLPRESSURE'

        if discipline == 2 and level == 255 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106:
            return 'RELATEMPERATURE'

        if discipline == 2 and level == 255 and parameterCategory == 3 and parameterNumber == 255 and typeOfFirstFixedSurface == 106:
            return 'RELAPROP.RMAX.EA'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 4 and typeOfFirstFixedSurface == 10:
            return 'SIM_REFLECT.MAX'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 33 and typeOfFirstFixedSurface == 1:
            return 'SUNSHI._DURATION'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 255 and typeOfFirstFixedSurface == 1:
            return 'THETAPWP_FLUX'

        if discipline == 255 and parameterCategory == 255 and parameterNumber == 255:
            return 'default'

    return wrapped
