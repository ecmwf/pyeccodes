import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'tp'

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2:
            return 'wilt'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaleFactorOfFirstFixedSurface == 0:
            return 'cap'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'tcc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'sf'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 'sd'

        is_tigge = h.get_l('is_tigge')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and is_tigge == 1:
            return 'st'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'st'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and is_tigge == 1:
            return 'sm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'sm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'orog'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'cin'

        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')
        probabilityType = h.get_l('probabilityType')
        scaleFactorOfLowerLimit = h.get_l('scaleFactorOfLowerLimit')
        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and productDefinitionTemplateNumber == 9 and scaledValueOfFirstFixedSurface == 10 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfLowerLimit == 20 and typeOfFirstFixedSurface == 103:
            return 'fg10g20'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and productDefinitionTemplateNumber == 9 and scaledValueOfFirstFixedSurface == 10 and probabilityType == 3 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 15 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 'fg10g15'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'wmixe'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'swrad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'lwrad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'grad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'nswrs'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'dirsw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 'swper'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'swell'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'swdir'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'mpww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'shww'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16:
            return 'snom'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 'iced'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 'iceg'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 'vice'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 'uice'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'siced'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'diced'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'icetk'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'den'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 's'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 'ssw'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 'bli'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'mtha'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'mthd'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'tthdp'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'mld'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'acpcp'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 'tstm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 'prate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 'satd'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'pwat'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'vcurr'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'ucurr'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 'vvcsh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 'vucsh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 'absd'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'absv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 'sgcvv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'mntsf'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'wvsp3'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'wvsp2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'wvsp1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 'gpa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 'presa'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 'ta'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 'pli'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return 'rdsp3'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return 'rdsp2'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6:
            return 'rdsp1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'vis'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 'lapr'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'dpt'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'tmin'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'tmax'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'hstdv'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'h'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'icaht'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2:
            return 'ptend'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return 'al'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 'tsec'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'dslm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 'ist'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'wz'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'spc'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'dirc'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 'persw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 'perpw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'dirpw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'wvdir'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return 'atmdiv'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return 'rfl39'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return 'rfl16'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return 'rfl08'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return 'rfl06'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 8:
            return 'raza'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 'solza'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 'npixu'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 'estv'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 'estu'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 'ctophqi'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 'ctoph'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 'irrate'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 'estp'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 'satosm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 16:
            return 'vsosm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 15:
            return 'soilp'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 14:
            return 'direc'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 13:
            return 'voldec'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12:
            return 'transo'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 11:
            return 'voltso'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 10:
            return 'liqvsm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 9:
            return 'poros'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 8:
            return 'smdry'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 7:
            return 'smref'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 'rlyrs'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 5:
            return 'soill'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 4:
            return 'botlst'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 3:
            return 'lowlsm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 2:
            return 'uplsm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 1:
            return 'uplst'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 'vwiltm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 'vsw'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 'hflux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 'cisoilw'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 'rcq'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 'rcsol'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 19:
            return 'rct'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 'rcs'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 'rsmin'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 'ccond'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 'bmixl'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 'cnwat'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 'sfexc'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return 'mstav'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 10:
            return 'gflux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 'soilw'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 'landu'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'mterh'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 'evapt'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5:
            return 'watr'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return 'veg'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'land'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return 'pop'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return 'pposp'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 'cppop'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 'ssrun'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 'bgrun'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return 'swepon'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return 'esct'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return 'rssc'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 'ffldro'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 'ffldg'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 'tsec'

        if discipline == 0 and parameterCategory == 190 and parameterNumber == 0:
            return 'var190m0'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return 'p260166'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return 'rcat'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return 'p260164'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return 'p260163'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return 'snfalb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 17:
            return 'mxsalb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 'contb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 'contt'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 'contet'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 'conti'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 'pblreg'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'tke'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 'turb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 'turbb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 'turbt'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'ici'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 6:
            return 'icib'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 5:
            return 'icit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 'volash'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 8:
            return 'tiacrp'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 7:
            return 'tiacip'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 6:
            return 'tiaccp'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 5:
            return 'gdradp'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 4:
            return 'gdiod'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 3:
            return 'gdces'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 2:
            return 'acradp'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 1:
            return 'aciod'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 0:
            return 'acces'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5:
            return 'prec'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 'lmaxbr'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 'veril'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 'brvel'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 'bref'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 'bswid'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 'tcioz'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0:
            return 'tozne'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'aerot'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return 'lftx4'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 'lftx'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 'ehlx'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 'hlcy'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 'sx'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 'totalx'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 'kox'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 'kx'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return 'p260120'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24:
            return 'suns'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 'cdcimr'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 21:
            return 'fice'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'tcolc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 19:
            return 'tcoli'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 18:
            return 'tcolw'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 17:
            return 'tcond'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 16:
            return 'cuefi'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 15:
            return 'cwork'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return 'cdlyr'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 'ceil'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'cdct'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'cdcb'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 10:
            return 'thunc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 9:
            return 'tmaxt'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 8:
            return 'cdct'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return 'cdca'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'cwat'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 'cice'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'nlwrcs'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5:
            return 'nlwrf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'ulwrf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'dlwrf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'nlwrt'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'nlwrs'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 'uvi'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50:
            return 'uviucs'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 'dwuvr'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 'nswrfcs'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10:
            return 'photar'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9:
            return 'nswrf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8:
            return 'uswrf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 'dswrf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'nswrt'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'sdsgso'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return 'p260084'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 'hpbl'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 'p260082'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 'p260081'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return 'wavh5'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 'denalt'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 'presalt'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 'thick'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 'alts'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'dist'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'prmsl'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'fricv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 'cd'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 'vstm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 'ustm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 'mflx'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 'vwsh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'vgust'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 'ugust'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'gust'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'maxgust'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18:
            return 'vflx'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17:
            return 'uflx'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 'iprate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 'fprate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66:
            return 'sprate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65:
            return 'rprate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 'tciwv'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'sdwe'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 'lssrate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 'csrate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 57:
            return 'tsrate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 'lssrwe'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 'csrwe'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54:
            return 'lsprate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'tsrwe'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'tprate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'tcwat'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'tsnowp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'twatp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 48:
            return 'cwp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 47:
            return 'lswp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'tcols'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'tcolr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'rime'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'frain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return 'snowc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 'pevpr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 'pevap'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return 'cpofp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 38:
            return 'mdiv'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37:
            return 'cprat'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return 'csnow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return 'cicep'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return 'cfrzr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return 'crain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'grle'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 'hail'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 'pwcat'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 29:
            return 'asnow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 28:
            return 'maxah'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 27:
            return 'maxrh'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 'mconv'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 'snmr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 'rwmr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 'icmr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 'clwmr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 21:
            return 'tcond'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 20:
            return 'iliqw'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 19:
            return 'ptype'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18:
            return 'absh'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 17:
            return 'snoag'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 'snol'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 'snoc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 'srweq'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 'ncpcp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'vapp'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'snohf'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 14:
            return 'mindpd'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'wcf'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'heatx'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11:
            return 'shtfl'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10:
            return 'lhtfl'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'skt'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'si10'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'btmp'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'sund'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'ttr'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'str'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'ssr'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'sr'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'lsm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'd2m'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 't2m'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'v10'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'u10'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'r'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'gh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 'd'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 101:
            return 'msl'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'slhf'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'sshf'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'bld'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 'vo'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'tcw'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'w'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'sp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'q'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'v'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'u'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 't'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'z'

        is_uerra = h.get_l('is_uerra')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')
        lengthOfTimeRange = h.get_l('lengthOfTimeRange')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'mn2t6'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'mx2t6'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'pv'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'cape'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'pres'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'pt'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'vp'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'strf'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 20 and typeOfStatisticalProcessing == 1 and probabilityType == 3:
            return 'tpg20'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and scaledValueOfLowerLimit == 10 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and productDefinitionTemplateNumber == 9:
            return 'tpg10'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 100:
            return 'v100'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 'u100'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'sithick'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 34:
            return 'sro'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 21 and typeOfSecondFixedSurface == 160 and typeOfFirstFixedSurface == 160 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'sav300'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and typeOfSecondFixedSurface == 255 and typeOfFirstFixedSurface == 20 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 29315:
            return 't20d'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'zos'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3 and typeOfFirstFixedSurface == 160:
            return 'von'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 160:
            return 'uoe'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 'mwp'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 'pp1d'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'mwd'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'swh'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 'mp2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'wdir'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'papt'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'vptmp'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'vtmp'

        if discipline == 20 and parameterCategory == 2 and parameterNumber == 0:
            return 'pop_dens'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 9:
            return 'mal_hab_frac'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 8:
            return 'mal_vect_dens'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 7:
            return 'mal_host_ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 6:
            return 'mal_infect_d10_ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 5:
            return 'mal_infect_ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 4:
            return 'mal_immun_ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 3:
            return 'mal_hbite_rate'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 2:
            return 'mal_innoc_rate'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 1:
            return 'mal_prot_ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 0:
            return 'mal_cases_frac'

        if discipline == 20 and parameterCategory == 0 and parameterNumber == 1:
            return 'mrt'

        if discipline == 20 and parameterCategory == 0 and parameterNumber == 0:
            return 'utci'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 23:
            return 'p260556'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 22:
            return 'p260555'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 21:
            return 'p260554'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 20:
            return 'p260553'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 19:
            return 'p260552'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17:
            return 'p260551'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16:
            return 'p260550'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 11:
            return 'fdsrte'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 10:
            return 'fbupinx'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 9:
            return 'infsinx'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 8:
            return 'drtcode'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 7:
            return 'dufmcode'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 6:
            return 'ffmcode'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 5:
            return 'fwinx'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 9:
            return 'p260539'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 8:
            return 'p260538'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 'p260537'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 6:
            return 'p260536'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 5:
            return 'p260535'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 4:
            return 'p260534'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 3:
            return 'p260533'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2:
            return 'p260532'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1:
            return 'p260531'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 0:
            return 'p260530'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15:
            return 'csbt'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14:
            return 'clbt'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 16 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 177:
            return 'perc'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'adlwrf_cs'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 53 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'auswrf_cs'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'adswrf_cs'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 27:
            return 'sod'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 16:
            return 'percr'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 26:
            return 'sohf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 8:
            return 'dlwrf_cs'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 53:
            return 'uswrf_cs'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 52:
            return 'dswrf_cs'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18:
            return 'sot'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 28:
            return 'mwt'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 29:
            return 'cat'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 121:
            return 'fscov'

        is_efas = h.get_l('is_efas')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and lengthOfTimeRange == 24 and indicatorOfUnitForTimeRange == 1 and is_efas == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'tp24'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and is_efas == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1:
            return 'tp06'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and lengthOfTimeRange == 24 and is_uerra == 0:
            return 'eva24'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and is_uerra == 0:
            return 'eva06'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 13 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'tidirswrf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 14:
            return 'difswrf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 13:
            return 'dirswrf'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'wdir10'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'eva'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79:
            return 'evarate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return 'ccl'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 2:
            return 'hindex'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 21:
            return 'aptmp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0:
            return 'r2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 9:
            return 'gwls'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 8:
            return 'gwus'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 25:
            return 'sd_elev'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 24:
            return 'dis24'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1:
            return 'dis06'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 15:
            return 'smups'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 14:
            return 'tpups'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 13:
            return 'woss'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 24:
            return 'frost'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 3:
            return 'dslr'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 2:
            return 'fldfrc'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 12:
            return 'fldsto'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 11:
            return 'rivsto'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7:
            return 'dis'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 10:
            return 'chside'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 13:
            return 'chcross'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20 and typeOfStatisticalProcessing == 0:
            return 'mtdch'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 0:
            return 'mtpf'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 30 and typeOfStatisticalProcessing == 0:
            return 'mddr'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 29 and typeOfStatisticalProcessing == 0:
            return 'mudr'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 28 and typeOfStatisticalProcessing == 0:
            return 'mdmf'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 27 and typeOfStatisticalProcessing == 0:
            return 'mumf'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 40 and typeOfStatisticalProcessing == 0:
            return 'mvtpm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 39 and typeOfStatisticalProcessing == 0:
            return 'mutpm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 108 and typeOfStatisticalProcessing == 0:
            return 'mqtpm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 26 and typeOfStatisticalProcessing == 0:
            return 'mttpm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 25 and typeOfStatisticalProcessing == 0:
            return 'mttlwrcs'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 24 and typeOfStatisticalProcessing == 0:
            return 'mttswrcs'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 23 and typeOfStatisticalProcessing == 0:
            return 'mttlwr'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 22 and typeOfStatisticalProcessing == 0:
            return 'mttswr'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 'si100'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 200:
            return 'si200'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 200:
            return 'v200'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 200 and typeOfFirstFixedSurface == 103:
            return 'u200'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 33:
            return 'ro'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'cp'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 10:
            return 'st100'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0:
            return 'st20'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and scaledValueOfSecondFixedSurface == 10 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106:
            return 'sm100'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106:
            return 'sm20'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1:
            return 'licga6'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 3 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1:
            return 'licga3'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'litota6'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 3 and indicatorOfUnitForTimeRange == 1:
            return 'litota3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 120:
            return 'ucciwc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 119:
            return 'ucclwc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 118:
            return 'ucq'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 1 and indicatorOfUnitForTimeRange == 1:
            return 'licga1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'licgi'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 1:
            return 'litota1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'litoti'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27:
            return 'hcct'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 93 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'rhw2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 19 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6:
            return 'mxcapes6'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1:
            return 'mxcape6'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 37:
            return 'fcpc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 36:
            return 'fspc'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 19:
            return 'asn'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 94:
            return 'rhi'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 93:
            return 'rhw'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and is_uerra == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfStatisticalProcessing == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 3:
            return 'fg310'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20 and scaledValueOfFirstFixedSurface == 27315 and scaleFactorOfFirstFixedSurface == 2:
            return 'deg0l'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20 and scaledValueOfFirstFixedSurface == 26315 and scaleFactorOfFirstFixedSurface == 2:
            return 'degm10l'

        is_aerosol = h.get_l('is_aerosol')
        aerosolType = h.get_l('aerosolType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and is_aerosol == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1 and aerosolType == 62003:
            return 'aermssam'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and is_aerosol == 1 and aerosolType == 62003:
            return 'aerwdcam'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and aerosolType == 62003 and is_aerosol == 1:
            return 'aerwdlam'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 62003 and is_aerosol == 1:
            return 'aersdmam'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 62003 and is_aerosol == 1:
            return 'aerddpam'

        typeOfWavelengthInterval = h.get_l('typeOfWavelengthInterval')
        scaleFactorOfFirstWavelength = h.get_l('scaleFactorOfFirstWavelength')
        scaledValueOfFirstWavelength = h.get_l('scaledValueOfFirstWavelength')
        typeOfSizeInterval = h.get_l('typeOfSizeInterval')
        is_aerosol_optical = h.get_l('is_aerosol_optical')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfWavelengthInterval == 11 and scaleFactorOfFirstWavelength == 8 and scaledValueOfFirstWavelength == 55 and typeOfSizeInterval == 255 and aerosolType == 62003 and is_aerosol_optical == 1:
            return 'amaod550'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and is_aerosol_optical == 1 and typeOfWavelengthInterval == 11 and scaleFactorOfFirstWavelength == 8 and scaledValueOfFirstWavelength == 55 and typeOfSizeInterval == 255 and aerosolType == 62004:
            return 'niaod550'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and aerosolType == 62003 and is_aerosol == 1:
            return 'aermr18'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and scaledValueOfFirstFixedSurface == 1 and scaleFactorOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 169 and typeOfSecondFixedSurface == 255:
            return 'mlotst010'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 3 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'sos'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 15 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 'mswt300m'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 18 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 'mswpt300m'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == -2 and probabilityType == 0 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9:
            return 'ptsa_lt_2stdev'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and probabilityType == 0 and scaleFactorOfLowerLimit == 1 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == -15:
            return 'ptsa_lt_1p5stdev'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == -1 and probabilityType == 0:
            return 'ptsa_lt_1stdev'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == 2 and probabilityType == 3 and scaleFactorOfLowerLimit == 0:
            return 'ptsa_gt_2stdev'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == 15 and probabilityType == 3 and scaleFactorOfLowerLimit == 1 and productDefinitionTemplateNumber == 9:
            return 'ptsa_gt_1p5stdev'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == 1 and probabilityType == 3:
            return 'ptsa_gt_1stdev'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaleFactorOfLowerLimit == 0 and scaledValueOfFirstFixedSurface == 10 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 2 and scaledValueOfLowerLimit == 10 and typeOfFirstFixedSurface == 103 and probabilityType == 3 and scaleFactorOfFirstFixedSurface == 0:
            return 'fgg1010'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 50:
            return 'tpg50'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 25 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1:
            return 'tpg25'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'hcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'mcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'lcc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'sde'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'lsp'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 32:
            return 'cc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 84:
            return 'ciwc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 83:
            return 'clwc'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'strc'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'ssrc'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'o3'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'mn2t'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 2 and is_uerra == 1:
            return 'mx2t'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 37:
            return 'nsss'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 38:
            return 'ewss'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'strd'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'ssrd'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 32:
            return 'etadot'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'cswc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'crwc'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfStatisticalProcessing == 2 and is_uerra == 1 and typeOfFirstFixedSurface == 103:
            return 'fg10'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0:
            return 'slt'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'sst'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 'rsn'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'siconc'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 45:
            return 'ucdv'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 31:
            return 'ucln'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 28:
            return 'uctp'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 200 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 'ws'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and is_uerra == 1 and scaledValueOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'ws'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'ws'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and scaledValueOfLowerLimit == 3 and scaleFactorOfLowerLimit == -2 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and productDefinitionTemplateNumber == 9:
            return 'tpg300'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 200 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1:
            return 'tpg200'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 150 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1:
            return 'tpg150'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 100 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9:
            return 'tpg100'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 80 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9:
            return 'tpg80'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 60 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9:
            return 'tpg60'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and scaledValueOfLowerLimit == 40 and probabilityType == 3 and scaleFactorOfLowerLimit == 0:
            return 'tpg40'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 5 and probabilityType == 3 and typeOfFirstFixedSurface == 1 and scaleFactorOfLowerLimit == 0:
            return 'tpg5'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 1 and probabilityType == 3 and scaleFactorOfLowerLimit == 0:
            return 'tpg1'

    return wrapped
