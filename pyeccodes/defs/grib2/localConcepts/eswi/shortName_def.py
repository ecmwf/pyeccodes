import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 19:
            return 'ws_sp'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return 'atmdiv'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return 'rf39'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return 'rf16'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return 'rf08'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return 'rf06'

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

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 9:
            return 'fde'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 8:
            return 'pst'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 'cmsk'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 6:
            return 'skt_sc'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 5:
            return 'pctp_sc'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 4:
            return 'li_sc'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 3:
            return 'pwat_sc'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2:
            return 'btmp_sc'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1:
            return 'al_sc'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 0:
            return 'rad_sc'

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

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 'rlyrs'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 'vwiltm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26:
            return 'wilt'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 'vsw'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 'hflux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 'w_cl'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'sm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 'rcsol'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 'rcq'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 19:
            return 'rct'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 'rcs'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 'prs_min'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 'ccond'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 'bmixl'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 'w_i'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 'sfexc'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return 'mstav'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 'soilw'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 'lu'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'z'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 'evapt'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'lcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'tcc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'sd'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'pwat'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'q'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'pres'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25:
            return 'nlpres'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24:
            return 'isor'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23:
            return 'gwd'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'slsgor'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21:
            return 'angsgor'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'stdsgor'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return '5wava'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 'hbpl'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 'v-gwd'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 'u-gwd'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return '5wavh'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 'denalt'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 'presalt'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 'thick'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 'alts'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 32:
            return 'eta'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'cswc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'crwc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 84:
            return 'ciwc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 83:
            return 'clwc'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 62:
            return 'se'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60:
            return 'sdwe'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 'lssrate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 'csrate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 57:
            return 'tsrate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 'prs_gsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 'csrwe'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54:
            return 'lsprate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'tcw'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'tsnowp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'twatp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'tqs'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'tqr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'facra'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'fra'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 23:
            return 'Ang'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 22:
            return 'AOD-1640'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 21:
            return 'AOD-810'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 20:
            return 'AOD-635'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 'va'

        atmosphericChemicalConsituentType = h.get_l('atmosphericChemicalConsituentType')

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10006:
            return 'HCN'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10022:
            return 'TOLUENE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10021:
            return 'BENZENE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10012:
            return 'C2H5OOH'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10002:
            return 'CH3O2H'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10001:
            return 'CH3O2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 12:
            return 'O'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 20:
            return 'H2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 14:
            return 'HO2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 16:
            return 'HONO'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 18:
            return 'HO2NO2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 15:
            return 'N2O5'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 13:
            return 'NO3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63011:
            return 'PAN'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60013:
            return 'NMVOC_C'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10004:
            return 'CH3OH'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10011:
            return 'C2H5OH'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10017:
            return 'C5H8'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 7:
            return 'HCHO'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10023:
            return 'OXYLENE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10015:
            return 'C3H6'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10009:
            return 'C2H4'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10016:
            return 'NC4H10'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10008:
            return 'C2H6'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'TKE'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 1:
            return 'mosf'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 'tsec'

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

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'wadir'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 'mpw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 'persw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'dirsw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 'perpw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'dirpw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 'swper'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'shps'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'swdir'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'mpww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'shww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'wvdir'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'swh'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 'iced'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 'iceg'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'siced'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'diced'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'icetk'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'icec'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'den'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'wtmp'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'tcc'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'mtha'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'mthd'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'tthdp'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'mld'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'sd'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'q'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'vcur'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'ucur'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'spdhcur'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'dirhcur'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'mntsf'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'vp'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'strf'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'ws'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'wdir'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'wvsp3'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'wvsp2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'wvsp1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'pt'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'msl'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'TKE'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'ncurr'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'ecurr'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 'secpref'

        if discipline == 0 and parameterCategory == 190 and parameterNumber == 0:
            return 'text'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return 'scld_prob'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return 'cat'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return 'icturb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return 'ici_prop'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return 'snfalb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 'contb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 'contt'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 'contet'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 'conti'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 'pblr'

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

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5:
            return 'corefl_rad'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 4:
            return 'refl_rad'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 3:
            return 'ectop_rad'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 2:
            return 'eqrfpc'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 1:
            return 'eqrrsn'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 0:
            return 'eqrrra'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5:
            return 'prrad'

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

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'o3mx'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'aerot'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 12:
            return 'ri'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return '4lftx'

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

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 33:
            return 'sund'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 32:
            return 'fracc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return 'cbext'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24:
            return 'suns'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 'cdcimr'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return 'cc'

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

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'nlwrfcs'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5:
            return 'nlwrf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'ulwrf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'dlwrf'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'pis'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'pit'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'gust'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 'cm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'hcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'mcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'lcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return 'ccc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'tcc'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 'tstm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'r'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'vis'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'msl'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return 'snowc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 'pevpr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 'pev'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return 'cpofp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 38:
            return 'mconv'

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
            return 'snag'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17:
            return 'skt'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'snohf'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'wcf'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'hindx'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'vpt'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'ctsig'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'cbsig'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'hcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'mcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'lcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'tcc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'r'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'gust'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'vis'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'tmin'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'tmax'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'msl'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return ' VIS'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62000:
            return ' PM'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40009:
            return ' PM2.5'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62012:
            return ' SOA'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63016:
            return ' PNHX'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63015:
            return ' PNOX'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63014:
            return ' PSOX'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40008:
            return ' PM10'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63018:
            return ' PMASS'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63017:
            return ' PNUMBER'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62001:
            return ' DUST'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40008:
            return ' PMCOARSE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40009:
            return ' PMFINE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62008:
            return ' NACL'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 23:
            return ' Rn222'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63012:
            return ' EC'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63013:
            return ' OC'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 2:
            return ' CH4'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 3:
            return ' CO2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 4:
            return ' CO'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10000:
            return ' OH'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 19:
            return ' H2O2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 0:
            return ' O3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63004:
            return ' NHX_N'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10:
            return ' NH4(+1)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 9:
            return ' NH3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60004:
            return ' NOY_N'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60003:
            return ' NOX_N'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63001:
            return ' NOX'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63009:
            return ' NITRATE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63007:
            return ' NH4NO3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 17:
            return ' HNO3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 5:
            return ' NO2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 11:
            return ' NO'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63005:
            return ' SOX_S'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63008:
            return ' SFT'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63006:
            return ' NH42SO4'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10500:
            return ' DMS'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 22:
            return ' SO4(2-)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 8:
            return ' SO2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'gust'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'vfr'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'CAPE'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'ci'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'TKE'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0:
            return 'slt'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 'dsn'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 19:
            return 'asn'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'slfr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'sd_cold'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'icc'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'maxgust'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'wmixe'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18:
            return 'vflx'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17:
            return 'uflx'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'bld'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11:
            return 'shtfl'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10:
            return 'lhtfl'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'swrad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'lwrad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'btmp'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'grad'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 2:
            return 'swavr'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 2:
            return 'lwavr'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'nlwrt'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'nswrt'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'nlwrs'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'nswrs'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 'persw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'dirsw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 'perpw'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'prwd'

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

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'mdww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'swh'

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

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'icec'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5:
            return 'watr'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'den'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 's'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return 'veg'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 'ssw'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'st'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return 'al'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'sr'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'dslm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'lsm'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'wtmp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 'lsf'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 'csf'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 'bli'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'cwat'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'hcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'mcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'lcc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return 'ccc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'tcc'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'mtha'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'mthd'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'tthdp'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'mld'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'sd'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'sdwe'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 'srweq'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'acpcp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 'lsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 8:
            return 'tp'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 'tstm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 'prate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 'cice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 6:
            return 'e'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 'satd'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'vp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'pwat'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2:
            return 'mixr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'r'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'q'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'vcurr'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'ucurr'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'spc'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'dirc'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 'vvsch'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 'vusch'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 'd'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 'vo'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 'absd'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'absv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'w'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'omega'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 'sgcvv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'mntsf'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'vp'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'strf'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'v'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'u'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'ws'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'wdir'

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

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7:
            return 'dptd'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'dpt'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'tmin'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'tmax'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'papt'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'pt'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'vtmp'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 't'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0:
            return 'tozne'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'hstdv'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'h'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'gh'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'z'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'icaht'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'pv'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2:
            return 'ptend'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'msl'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'pres'

    return wrapped
