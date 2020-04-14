import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 1 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'tp'

        if table2Version == 1 and indicatorOfParameter == 71:
            return 'tcc'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'sf'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'st'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'sm'

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'orog'

        if table2Version == 1 and indicatorOfParameter == 87:
            return 'vegrea'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 'imgd'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'wmixe'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'vflx'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'uflx'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'swrad'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'lwrad'

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'grad'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'swavr'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'lwavr'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'nlwrt'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'nswrt'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'nlwrs'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'nswrs'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 'swp'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'dirsw'

        if table2Version == 1 and indicatorOfParameter == 108:
            return 'mpps'

        if table2Version == 1 and indicatorOfParameter == 107:
            return 'mdps'

        if table2Version == 1 and indicatorOfParameter == 106:
            return 'swper'

        if table2Version == 1 and indicatorOfParameter == 105:
            return 'swell'

        if table2Version == 1 and indicatorOfParameter == 104:
            return 'swdir'

        if table2Version == 1 and indicatorOfParameter == 103:
            return 'mpww'

        if table2Version == 1 and indicatorOfParameter == 102:
            return 'shww'

        if table2Version == 1 and indicatorOfParameter == 101:
            return 'mdww'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'swh'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'snom'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 'iced'

        if table2Version == 1 and indicatorOfParameter == 97:
            return 'iceg'

        if table2Version == 1 and indicatorOfParameter == 96:
            return 'vice'

        if table2Version == 1 and indicatorOfParameter == 95:
            return 'uice'

        if table2Version == 1 and indicatorOfParameter == 94:
            return 'siced'

        if table2Version == 1 and indicatorOfParameter == 93:
            return 'diced'

        if table2Version == 1 and indicatorOfParameter == 92:
            return 'icetk'

        if table2Version == 1 and indicatorOfParameter == 91:
            return 'icec'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'den'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'ssw'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'dslm'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'wtmp'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'bli'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'mtha'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'mthd'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'tthdp'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'mld'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'srweq'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'acpcp'

        if table2Version == 1 and indicatorOfParameter == 60:
            return 'tstm'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'prate'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'satd'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'vp'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'pwat'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'mixr'

        if table2Version == 1 and indicatorOfParameter == 50:
            return 'vcurr'

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'ucurr'

        if table2Version == 1 and indicatorOfParameter == 48:
            return 'spc'

        if table2Version == 1 and indicatorOfParameter == 47:
            return 'dirc'

        if table2Version == 1 and indicatorOfParameter == 46:
            return 'vvcsh'

        if table2Version == 1 and indicatorOfParameter == 45:
            return 'vucsh'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 'absd'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 'absv'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 'sgcvv'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'mntsf'

        if table2Version == 1 and indicatorOfParameter == 31:
            return 'wdir'

        if table2Version == 1 and indicatorOfParameter == 30:
            return 'wvsp3'

        if table2Version == 1 and indicatorOfParameter == 29:
            return 'wvsp2'

        if table2Version == 1 and indicatorOfParameter == 28:
            return 'wvsp1'

        if table2Version == 1 and indicatorOfParameter == 27:
            return 'gpa'

        if table2Version == 1 and indicatorOfParameter == 26:
            return 'presa'

        if table2Version == 1 and indicatorOfParameter == 25:
            return 'ta'

        if table2Version == 1 and indicatorOfParameter == 24:
            return 'pli'

        if table2Version == 1 and indicatorOfParameter == 23:
            return 'rdsp3'

        if table2Version == 1 and indicatorOfParameter == 22:
            return 'rdsp2'

        if table2Version == 1 and indicatorOfParameter == 21:
            return 'rdsp1'

        if table2Version == 1 and indicatorOfParameter == 20:
            return 'vis'

        if table2Version == 1 and indicatorOfParameter == 19:
            return 'lapr'

        if table2Version == 1 and indicatorOfParameter == 18:
            return 'depr'

        if table2Version == 1 and indicatorOfParameter == 17:
            return 'dpt'

        if table2Version == 1 and indicatorOfParameter == 16:
            return 'tmin'

        if table2Version == 1 and indicatorOfParameter == 15:
            return 'tmax'

        if table2Version == 1 and indicatorOfParameter == 14:
            return 'papt'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'hstdv'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'h'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'icaht'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'ptend'

        if table2Version == 1 and indicatorOfParameter == 84:
            return 'al'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'cwat'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'snoc'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'bld'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'shf'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'lhf'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'lssf'

        if table2Version == 1 and indicatorOfParameter == 75:
            return 'hcc'

        if table2Version == 1 and indicatorOfParameter == 74:
            return 'mcc'

        if table2Version == 1 and indicatorOfParameter == 73:
            return 'lcc'

        if table2Version == 1 and indicatorOfParameter == 72:
            return 'ccc'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'sde'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'lsp'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'tco3'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'ro'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'btmp'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'e'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'sr'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 1 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2d'

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2t'

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10v'

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10u'

        if table2Version == 1 and indicatorOfParameter == 52:
            return 'r'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'gh'

        if table2Version == 1 and indicatorOfParameter == 44:
            return 'd'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'msl'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 'vo'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'w'

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'sp'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'q'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'z'

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mn2t6'

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mx2t6'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'pv'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'pres'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'ws'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'pt'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'vp'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'strf'

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'tp'

        if table2Version == 2 and indicatorOfParameter == 71:
            return 'tcc'

        if table2Version == 2 and indicatorOfParameter == 65:
            return 'sf'

        if table2Version == 2 and indicatorOfParameter == 85:
            return 'st'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'sm'

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'orog'

        if table2Version == 2 and indicatorOfParameter == 87:
            return 'vegrea'

        if table2Version == 2 and indicatorOfParameter == 127:
            return 'imgd'

        if table2Version == 2 and indicatorOfParameter == 126:
            return 'wmixe'

        if table2Version == 2 and indicatorOfParameter == 125:
            return 'vflx'

        if table2Version == 2 and indicatorOfParameter == 124:
            return 'uflx'

        if table2Version == 2 and indicatorOfParameter == 120:
            return 'swrad'

        if table2Version == 2 and indicatorOfParameter == 119:
            return 'lwrad'

        if table2Version == 2 and indicatorOfParameter == 117:
            return 'grad'

        if table2Version == 2 and indicatorOfParameter == 116:
            return 'swavr'

        if table2Version == 2 and indicatorOfParameter == 115:
            return 'lwavr'

        if table2Version == 2 and indicatorOfParameter == 114:
            return 'nlwrt'

        if table2Version == 2 and indicatorOfParameter == 113:
            return 'nswrt'

        if table2Version == 2 and indicatorOfParameter == 112:
            return 'nlwrs'

        if table2Version == 2 and indicatorOfParameter == 111:
            return 'nswrs'

        if table2Version == 2 and indicatorOfParameter == 110:
            return 'swp'

        if table2Version == 2 and indicatorOfParameter == 109:
            return 'dirsw'

        if table2Version == 2 and indicatorOfParameter == 108:
            return 'mpps'

        if table2Version == 2 and indicatorOfParameter == 107:
            return 'mdps'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 'swper'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'swell'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'swdir'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 'mpww'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'shww'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'mdww'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'swh'

        if table2Version == 2 and indicatorOfParameter == 99:
            return 'snom'

        if table2Version == 2 and indicatorOfParameter == 98:
            return 'iced'

        if table2Version == 2 and indicatorOfParameter == 97:
            return 'iceg'

        if table2Version == 2 and indicatorOfParameter == 96:
            return 'vice'

        if table2Version == 2 and indicatorOfParameter == 95:
            return 'uice'

        if table2Version == 2 and indicatorOfParameter == 94:
            return 'siced'

        if table2Version == 2 and indicatorOfParameter == 93:
            return 'diced'

        if table2Version == 2 and indicatorOfParameter == 92:
            return 'icetk'

        if table2Version == 2 and indicatorOfParameter == 91:
            return 'icec'

        if table2Version == 2 and indicatorOfParameter == 89:
            return 'den'

        if table2Version == 2 and indicatorOfParameter == 88:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'ssw'

        if table2Version == 2 and indicatorOfParameter == 82:
            return 'dslm'

        if table2Version == 2 and indicatorOfParameter == 80:
            return 'wtmp'

        if table2Version == 2 and indicatorOfParameter == 77:
            return 'bli'

        if table2Version == 2 and indicatorOfParameter == 70:
            return 'mtha'

        if table2Version == 2 and indicatorOfParameter == 69:
            return 'mthd'

        if table2Version == 2 and indicatorOfParameter == 68:
            return 'tthdp'

        if table2Version == 2 and indicatorOfParameter == 67:
            return 'mld'

        if table2Version == 2 and indicatorOfParameter == 64:
            return 'srweq'

        if table2Version == 2 and indicatorOfParameter == 63:
            return 'acpcp'

        if table2Version == 2 and indicatorOfParameter == 60:
            return 'tstm'

        if table2Version == 2 and indicatorOfParameter == 59:
            return 'prate'

        if table2Version == 2 and indicatorOfParameter == 56:
            return 'satd'

        if table2Version == 2 and indicatorOfParameter == 55:
            return 'vp'

        if table2Version == 2 and indicatorOfParameter == 54:
            return 'pwat'

        if table2Version == 2 and indicatorOfParameter == 53:
            return 'mixr'

        if table2Version == 2 and indicatorOfParameter == 50:
            return 'vcurr'

        if table2Version == 2 and indicatorOfParameter == 49:
            return 'ucurr'

        if table2Version == 2 and indicatorOfParameter == 48:
            return 'spc'

        if table2Version == 2 and indicatorOfParameter == 47:
            return 'dirc'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 'vvcsh'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 'vucsh'

        if table2Version == 2 and indicatorOfParameter == 42:
            return 'absd'

        if table2Version == 2 and indicatorOfParameter == 41:
            return 'absv'

        if table2Version == 2 and indicatorOfParameter == 38:
            return 'sgcvv'

        if table2Version == 2 and indicatorOfParameter == 37:
            return 'mntsf'

        if table2Version == 2 and indicatorOfParameter == 31:
            return 'wdir'

        if table2Version == 2 and indicatorOfParameter == 30:
            return 'wvsp3'

        if table2Version == 2 and indicatorOfParameter == 29:
            return 'wvsp2'

        if table2Version == 2 and indicatorOfParameter == 28:
            return 'wvsp1'

        if table2Version == 2 and indicatorOfParameter == 27:
            return 'gpa'

        if table2Version == 2 and indicatorOfParameter == 26:
            return 'presa'

        if table2Version == 2 and indicatorOfParameter == 25:
            return 'ta'

        if table2Version == 2 and indicatorOfParameter == 24:
            return 'pli'

        if table2Version == 2 and indicatorOfParameter == 23:
            return 'rdsp3'

        if table2Version == 2 and indicatorOfParameter == 22:
            return 'rdsp2'

        if table2Version == 2 and indicatorOfParameter == 21:
            return 'rdsp1'

        if table2Version == 2 and indicatorOfParameter == 20:
            return 'vis'

        if table2Version == 2 and indicatorOfParameter == 19:
            return 'lapr'

        if table2Version == 2 and indicatorOfParameter == 18:
            return 'depr'

        if table2Version == 2 and indicatorOfParameter == 17:
            return 'dpt'

        if table2Version == 2 and indicatorOfParameter == 16:
            return 'tmin'

        if table2Version == 2 and indicatorOfParameter == 15:
            return 'tmax'

        if table2Version == 2 and indicatorOfParameter == 14:
            return 'papt'

        if table2Version == 2 and indicatorOfParameter == 9:
            return 'hstdv'

        if table2Version == 2 and indicatorOfParameter == 8:
            return 'h'

        if table2Version == 2 and indicatorOfParameter == 5:
            return 'icaht'

        if table2Version == 2 and indicatorOfParameter == 3:
            return 'ptend'

        if table2Version == 2 and indicatorOfParameter == 84:
            return 'al'

        if table2Version == 2 and indicatorOfParameter == 76:
            return 'cwat'

        if table2Version == 2 and indicatorOfParameter == 78:
            return 'snoc'

        if table2Version == 2 and indicatorOfParameter == 123:
            return 'bld'

        if table2Version == 2 and indicatorOfParameter == 122:
            return 'shf'

        if table2Version == 2 and indicatorOfParameter == 121:
            return 'lhf'

        if table2Version == 2 and indicatorOfParameter == 79:
            return 'lssf'

        if table2Version == 2 and indicatorOfParameter == 75:
            return 'hcc'

        if table2Version == 2 and indicatorOfParameter == 74:
            return 'mcc'

        if table2Version == 2 and indicatorOfParameter == 73:
            return 'lcc'

        if table2Version == 2 and indicatorOfParameter == 72:
            return 'ccc'

        if table2Version == 2 and indicatorOfParameter == 66:
            return 'sde'

        if table2Version == 2 and indicatorOfParameter == 62:
            return 'lsp'

        if table2Version == 2 and indicatorOfParameter == 10:
            return 'tco3'

        if table2Version == 2 and indicatorOfParameter == 90:
            return 'ro'

        if table2Version == 2 and indicatorOfParameter == 118:
            return 'btmp'

        if table2Version == 2 and indicatorOfParameter == 57:
            return 'e'

        if table2Version == 2 and indicatorOfParameter == 83:
            return 'sr'

        if table2Version == 2 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2d'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2t'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10v'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10u'

        if table2Version == 2 and indicatorOfParameter == 52:
            return 'r'

        if table2Version == 2 and indicatorOfParameter == 7:
            return 'gh'

        if table2Version == 2 and indicatorOfParameter == 44:
            return 'd'

        if table2Version == 2 and indicatorOfParameter == 2:
            return 'msl'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 'vo'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'w'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'sp'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'q'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'z'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mn2t6'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mx2t6'

        if table2Version == 2 and indicatorOfParameter == 4:
            return 'pv'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'pres'

        if table2Version == 2 and indicatorOfParameter == 32:
            return 'ws'

        if table2Version == 2 and indicatorOfParameter == 13:
            return 'pt'

        if table2Version == 2 and indicatorOfParameter == 36:
            return 'vp'

        if table2Version == 2 and indicatorOfParameter == 35:
            return 'strf'

        if table2Version == 3 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'tp'

        if table2Version == 3 and indicatorOfParameter == 71:
            return 'tcc'

        if table2Version == 3 and indicatorOfParameter == 65:
            return 'sf'

        if table2Version == 3 and indicatorOfParameter == 85:
            return 'st'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'sm'

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'orog'

        if table2Version == 3 and indicatorOfParameter == 87:
            return 'vegrea'

        if table2Version == 3 and indicatorOfParameter == 127:
            return 'imgd'

        if table2Version == 3 and indicatorOfParameter == 126:
            return 'wmixe'

        if table2Version == 3 and indicatorOfParameter == 125:
            return 'vflx'

        if table2Version == 3 and indicatorOfParameter == 124:
            return 'uflx'

        if table2Version == 3 and indicatorOfParameter == 120:
            return 'swrad'

        if table2Version == 3 and indicatorOfParameter == 119:
            return 'lwrad'

        if table2Version == 3 and indicatorOfParameter == 117:
            return 'grad'

        if table2Version == 3 and indicatorOfParameter == 116:
            return 'swavr'

        if table2Version == 3 and indicatorOfParameter == 115:
            return 'lwavr'

        if table2Version == 3 and indicatorOfParameter == 114:
            return 'nlwrt'

        if table2Version == 3 and indicatorOfParameter == 113:
            return 'nswrt'

        if table2Version == 3 and indicatorOfParameter == 112:
            return 'nlwrs'

        if table2Version == 3 and indicatorOfParameter == 111:
            return 'nswrs'

        if table2Version == 3 and indicatorOfParameter == 110:
            return 'swp'

        if table2Version == 3 and indicatorOfParameter == 109:
            return 'dirsw'

        if table2Version == 3 and indicatorOfParameter == 108:
            return 'mpps'

        if table2Version == 3 and indicatorOfParameter == 107:
            return 'mdps'

        if table2Version == 3 and indicatorOfParameter == 106:
            return 'swper'

        if table2Version == 3 and indicatorOfParameter == 105:
            return 'swell'

        if table2Version == 3 and indicatorOfParameter == 104:
            return 'swdir'

        if table2Version == 3 and indicatorOfParameter == 103:
            return 'mpww'

        if table2Version == 3 and indicatorOfParameter == 102:
            return 'shww'

        if table2Version == 3 and indicatorOfParameter == 101:
            return 'mdww'

        if table2Version == 3 and indicatorOfParameter == 100:
            return 'swh'

        if table2Version == 3 and indicatorOfParameter == 99:
            return 'snom'

        if table2Version == 3 and indicatorOfParameter == 98:
            return 'iced'

        if table2Version == 3 and indicatorOfParameter == 97:
            return 'iceg'

        if table2Version == 3 and indicatorOfParameter == 96:
            return 'vice'

        if table2Version == 3 and indicatorOfParameter == 95:
            return 'uice'

        if table2Version == 3 and indicatorOfParameter == 94:
            return 'siced'

        if table2Version == 3 and indicatorOfParameter == 93:
            return 'diced'

        if table2Version == 3 and indicatorOfParameter == 92:
            return 'icetk'

        if table2Version == 3 and indicatorOfParameter == 91:
            return 'icec'

        if table2Version == 3 and indicatorOfParameter == 89:
            return 'den'

        if table2Version == 3 and indicatorOfParameter == 88:
            return 's'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'ssw'

        if table2Version == 3 and indicatorOfParameter == 82:
            return 'dslm'

        if table2Version == 3 and indicatorOfParameter == 80:
            return 'wtmp'

        if table2Version == 3 and indicatorOfParameter == 77:
            return 'bli'

        if table2Version == 3 and indicatorOfParameter == 70:
            return 'mtha'

        if table2Version == 3 and indicatorOfParameter == 69:
            return 'mthd'

        if table2Version == 3 and indicatorOfParameter == 68:
            return 'tthdp'

        if table2Version == 3 and indicatorOfParameter == 67:
            return 'mld'

        if table2Version == 3 and indicatorOfParameter == 64:
            return 'srweq'

        if table2Version == 3 and indicatorOfParameter == 63:
            return 'acpcp'

        if table2Version == 3 and indicatorOfParameter == 60:
            return 'tstm'

        if table2Version == 3 and indicatorOfParameter == 59:
            return 'prate'

        if table2Version == 3 and indicatorOfParameter == 56:
            return 'satd'

        if table2Version == 3 and indicatorOfParameter == 55:
            return 'vp'

        if table2Version == 3 and indicatorOfParameter == 54:
            return 'pwat'

        if table2Version == 3 and indicatorOfParameter == 53:
            return 'mixr'

        if table2Version == 3 and indicatorOfParameter == 50:
            return 'vcurr'

        if table2Version == 3 and indicatorOfParameter == 49:
            return 'ucurr'

        if table2Version == 3 and indicatorOfParameter == 48:
            return 'spc'

        if table2Version == 3 and indicatorOfParameter == 47:
            return 'dirc'

        if table2Version == 3 and indicatorOfParameter == 46:
            return 'vvcsh'

        if table2Version == 3 and indicatorOfParameter == 45:
            return 'vucsh'

        if table2Version == 3 and indicatorOfParameter == 42:
            return 'absd'

        if table2Version == 3 and indicatorOfParameter == 41:
            return 'absv'

        if table2Version == 3 and indicatorOfParameter == 38:
            return 'sgcvv'

        if table2Version == 3 and indicatorOfParameter == 37:
            return 'mntsf'

        if table2Version == 3 and indicatorOfParameter == 31:
            return 'wdir'

        if table2Version == 3 and indicatorOfParameter == 30:
            return 'wvsp3'

        if table2Version == 3 and indicatorOfParameter == 29:
            return 'wvsp2'

        if table2Version == 3 and indicatorOfParameter == 28:
            return 'wvsp1'

        if table2Version == 3 and indicatorOfParameter == 27:
            return 'gpa'

        if table2Version == 3 and indicatorOfParameter == 26:
            return 'presa'

        if table2Version == 3 and indicatorOfParameter == 25:
            return 'ta'

        if table2Version == 3 and indicatorOfParameter == 24:
            return 'pli'

        if table2Version == 3 and indicatorOfParameter == 23:
            return 'rdsp3'

        if table2Version == 3 and indicatorOfParameter == 22:
            return 'rdsp2'

        if table2Version == 3 and indicatorOfParameter == 21:
            return 'rdsp1'

        if table2Version == 3 and indicatorOfParameter == 20:
            return 'vis'

        if table2Version == 3 and indicatorOfParameter == 19:
            return 'lapr'

        if table2Version == 3 and indicatorOfParameter == 18:
            return 'depr'

        if table2Version == 3 and indicatorOfParameter == 17:
            return 'dpt'

        if table2Version == 3 and indicatorOfParameter == 16:
            return 'tmin'

        if table2Version == 3 and indicatorOfParameter == 15:
            return 'tmax'

        if table2Version == 3 and indicatorOfParameter == 14:
            return 'papt'

        if table2Version == 3 and indicatorOfParameter == 9:
            return 'hstdv'

        if table2Version == 3 and indicatorOfParameter == 8:
            return 'h'

        if table2Version == 3 and indicatorOfParameter == 5:
            return 'icaht'

        if table2Version == 3 and indicatorOfParameter == 3:
            return 'ptend'

        if table2Version == 3 and indicatorOfParameter == 12:
            return 'vtmp'

        if table2Version == 2 and indicatorOfParameter == 12:
            return 'vtmp'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'vtmp'

        if table2Version == 3 and indicatorOfParameter == 84:
            return 'al'

        if table2Version == 3 and indicatorOfParameter == 76:
            return 'cwat'

        if table2Version == 3 and indicatorOfParameter == 78:
            return 'snoc'

        if table2Version == 3 and indicatorOfParameter == 123:
            return 'bld'

        if table2Version == 3 and indicatorOfParameter == 122:
            return 'shf'

        if table2Version == 3 and indicatorOfParameter == 121:
            return 'lhf'

        if table2Version == 3 and indicatorOfParameter == 79:
            return 'lssf'

        if table2Version == 3 and indicatorOfParameter == 75:
            return 'hcc'

        if table2Version == 3 and indicatorOfParameter == 74:
            return 'mcc'

        if table2Version == 3 and indicatorOfParameter == 73:
            return 'lcc'

        if table2Version == 3 and indicatorOfParameter == 72:
            return 'ccc'

        if table2Version == 3 and indicatorOfParameter == 66:
            return 'sde'

        if table2Version == 3 and indicatorOfParameter == 62:
            return 'lsp'

        if table2Version == 3 and indicatorOfParameter == 10:
            return 'tco3'

        if table2Version == 3 and indicatorOfParameter == 90:
            return 'ro'

        if table2Version == 3 and indicatorOfParameter == 118:
            return 'btmp'

        if table2Version == 3 and indicatorOfParameter == 57:
            return 'e'

        if table2Version == 3 and indicatorOfParameter == 83:
            return 'sr'

        if table2Version == 3 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 3 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2d'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2t'

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10v'

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10u'

        if table2Version == 3 and indicatorOfParameter == 52:
            return 'r'

        if table2Version == 3 and indicatorOfParameter == 7:
            return 'gh'

        if table2Version == 3 and indicatorOfParameter == 44:
            return 'd'

        if table2Version == 3 and indicatorOfParameter == 2:
            return 'msl'

        if table2Version == 3 and indicatorOfParameter == 43:
            return 'vo'

        if table2Version == 3 and indicatorOfParameter == 39:
            return 'w'

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'sp'

        if table2Version == 3 and indicatorOfParameter == 51:
            return 'q'

        if table2Version == 3 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 3 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 3 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 3 and indicatorOfParameter == 6:
            return 'z'

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mn2t6'

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mx2t6'

        if table2Version == 3 and indicatorOfParameter == 4:
            return 'pv'

        if table2Version == 3 and indicatorOfParameter == 1:
            return 'pres'

        if table2Version == 3 and indicatorOfParameter == 32:
            return 'ws'

        if table2Version == 3 and indicatorOfParameter == 13:
            return 'pt'

        if table2Version == 3 and indicatorOfParameter == 36:
            return 'vp'

        if table2Version == 3 and indicatorOfParameter == 35:
            return 'strf'

    return wrapped
