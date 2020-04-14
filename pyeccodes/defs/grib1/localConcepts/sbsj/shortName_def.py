import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 254 and indicatorOfParameter == 255:
            return 'uvmt'

        if table2Version == 254 and indicatorOfParameter == 254:
            return 'vtmt'

        if table2Version == 254 and indicatorOfParameter == 253:
            return 'tvmt'

        if table2Version == 254 and indicatorOfParameter == 252:
            return 'pvmt'

        if table2Version == 254 and indicatorOfParameter == 251:
            return 'tmmt'

        if table2Version == 254 and indicatorOfParameter == 250:
            return 'psmt'

        if table2Version == 254 and indicatorOfParameter == 249:
            return 'fcmt'

        if table2Version == 254 and indicatorOfParameter == 248:
            return 'uemt'

        if table2Version == 254 and indicatorOfParameter == 247:
            return 'simt'

        if table2Version == 254 and indicatorOfParameter == 246:
            return 'mpmt'

        if table2Version == 254 and indicatorOfParameter == 245:
            return 'rhmt'

        if table2Version == 254 and indicatorOfParameter == 244:
            return 'pcmt'

        if table2Version == 254 and indicatorOfParameter == 243:
            return 'ptmt'

        if table2Version == 254 and indicatorOfParameter == 242:
            return 'omtm'

        if table2Version == 254 and indicatorOfParameter == 241:
            return 'vvmt'

        if table2Version == 254 and indicatorOfParameter == 240:
            return 'mkmt'

        if table2Version == 254 and indicatorOfParameter == 239:
            return 'lnmt'

        if table2Version == 254 and indicatorOfParameter == 238:
            return 'zhmt'

        if table2Version == 254 and indicatorOfParameter == 237:
            return 'dvmt'

        if table2Version == 254 and indicatorOfParameter == 236:
            return 'ommt'

        if table2Version == 254 and indicatorOfParameter == 235:
            return 'stmt'

        if table2Version == 254 and indicatorOfParameter == 234:
            return 'atmt'

        if table2Version == 254 and indicatorOfParameter == 233:
            return 'rsmt'

        if table2Version == 254 and indicatorOfParameter == 232:
            return 'tsmt'

        if table2Version == 254 and indicatorOfParameter == 231:
            return 'vsmt'

        if table2Version == 254 and indicatorOfParameter == 230:
            return 'usmt'

        if table2Version == 254 and indicatorOfParameter == 227:
            return 'vdcc'

        if table2Version == 254 and indicatorOfParameter == 226:
            return 'umrs'

        if table2Version == 254 and indicatorOfParameter == 225:
            return 'vdfh'

        if table2Version == 254 and indicatorOfParameter == 224:
            return 'vdfv'

        if table2Version == 254 and indicatorOfParameter == 223:
            return 'vdfu'

        if table2Version == 254 and indicatorOfParameter == 222:
            return 'vdms'

        if table2Version == 254 and indicatorOfParameter == 221:
            return 'hvdf'

        if table2Version == 254 and indicatorOfParameter == 220:
            return 'hddf'

        if table2Version == 254 and indicatorOfParameter == 219:
            return 'hmdf'

        if table2Version == 254 and indicatorOfParameter == 218:
            return 'hhdf'

        if table2Version == 254 and indicatorOfParameter == 215:
            return 'swtc'

        if table2Version == 254 and indicatorOfParameter == 214:
            return 'roce'

        if table2Version == 254 and indicatorOfParameter == 213:
            return 'swgc'

        if table2Version == 254 and indicatorOfParameter == 212:
            return 'oces'

        if table2Version == 254 and indicatorOfParameter == 211:
            return 'oles'

        if table2Version == 254 and indicatorOfParameter == 210:
            return 'ocic'

        if table2Version == 254 and indicatorOfParameter == 209:
            return 'ocis'

        if table2Version == 254 and indicatorOfParameter == 208:
            return 'olic'

        if table2Version == 254 and indicatorOfParameter == 207:
            return 'olis'

        if table2Version == 254 and indicatorOfParameter == 206:
            return 'swrh'

        if table2Version == 254 and indicatorOfParameter == 205:
            return 'lwrh'

        if table2Version == 254 and indicatorOfParameter == 203:
            return 'ocac'

        if table2Version == 254 and indicatorOfParameter == 202:
            return 'swec'

        if table2Version == 254 and indicatorOfParameter == 201:
            return 'lwtc'

        if table2Version == 254 and indicatorOfParameter == 200:
            return 'lwbc'

        if table2Version == 254 and indicatorOfParameter == 198:
            return 'ghfl'

        if table2Version == 254 and indicatorOfParameter == 197:
            return 'iswf'

        if table2Version == 254 and indicatorOfParameter == 196:
            return 'suvf'

        if table2Version == 254 and indicatorOfParameter == 195:
            return 'vsst'

        if table2Version == 254 and indicatorOfParameter == 194:
            return 'vves'

        if table2Version == 254 and indicatorOfParameter == 193:
            return 'usst'

        if table2Version == 254 and indicatorOfParameter == 192:
            return 'uves'

        if table2Version == 254 and indicatorOfParameter == 191:
            return 'tgsc'

        if table2Version == 254 and indicatorOfParameter == 190:
            return 'ctmp'

        if table2Version == 254 and indicatorOfParameter == 189:
            return 'tcas'

        if table2Version == 254 and indicatorOfParameter == 188:
            return 'tems'

        if table2Version == 254 and indicatorOfParameter == 187:
            return 'tsfc'

        if table2Version == 254 and indicatorOfParameter == 186:
            return 'amsl'

        if table2Version == 254 and indicatorOfParameter == 185:
            return 'amdl'

        if table2Version == 254 and indicatorOfParameter == 184:
            return 'uzds'

        if table2Version == 254 and indicatorOfParameter == 183:
            return 'uzrs'

        if table2Version == 254 and indicatorOfParameter == 182:
            return 'ussl'

        if table2Version == 254 and indicatorOfParameter == 181:
            return 'qsfc'

        if table2Version == 254 and indicatorOfParameter == 180:
            return 'vpca'

        if table2Version == 254 and indicatorOfParameter == 179:
            return 'pitp'

        if table2Version == 254 and indicatorOfParameter == 178:
            return 'rnof'

        if table2Version == 254 and indicatorOfParameter == 177:
            return 'evpp'

        if table2Version == 254 and indicatorOfParameter == 176:
            return 'bslh'

        if table2Version == 254 and indicatorOfParameter == 175:
            return 'tgrz'

        if table2Version == 254 and indicatorOfParameter == 174:
            return 'smav'

        if table2Version == 254 and indicatorOfParameter == 173:
            return 'lgms'

        if table2Version == 254 and indicatorOfParameter == 172:
            return 'lglh'

        if table2Version == 254 and indicatorOfParameter == 171:
            return 'nhcm'

        if table2Version == 254 and indicatorOfParameter == 170:
            return 'vadv'

        if table2Version == 254 and indicatorOfParameter == 169:
            return 'vmfl'

        if table2Version == 254 and indicatorOfParameter == 168:
            return 'hmfc'

        if table2Version == 254 and indicatorOfParameter == 167:
            return 'dvsh'

        if table2Version == 254 and indicatorOfParameter == 165:
            return 'gvvs'

        if table2Version == 254 and indicatorOfParameter == 164:
            return 'gvus'

        if table2Version == 254 and indicatorOfParameter == 163:
            return 'gvdv'

        if table2Version == 254 and indicatorOfParameter == 162:
            return 'gvdu'

        if table2Version == 254 and indicatorOfParameter == 160:
            return 'tppv'

        if table2Version == 254 and indicatorOfParameter == 159:
            return 'tppu'

        if table2Version == 254 and indicatorOfParameter == 158:
            return 'tppt'

        if table2Version == 254 and indicatorOfParameter == 157:
            return 'tppp'

        if table2Version == 254 and indicatorOfParameter == 156:
            return 'fdlv'

        if table2Version == 254 and indicatorOfParameter == 155:
            return 'fdlu'

        if table2Version == 254 and indicatorOfParameter == 154:
            return 'fdlt'

        if table2Version == 254 and indicatorOfParameter == 153:
            return 'fzrh'

        if table2Version == 254 and indicatorOfParameter == 152:
            return 'fzht'

        if table2Version == 254 and indicatorOfParameter == 151:
            return 'pctp'

        if table2Version == 254 and indicatorOfParameter == 150:
            return 'pcbs'

        if table2Version == 254 and indicatorOfParameter == 149:
            return 'cbnt'

        if table2Version == 254 and indicatorOfParameter == 148:
            return 'vstr'

        if table2Version == 254 and indicatorOfParameter == 147:
            return 'ustr'

        if table2Version == 254 and indicatorOfParameter == 146:
            return 'mxwp'

        if table2Version == 254 and indicatorOfParameter == 145:
            return 'scvh'

        if table2Version == 254 and indicatorOfParameter == 144:
            return 'scvm'

        if table2Version == 254 and indicatorOfParameter == 143:
            return 'mscv'

        if table2Version == 254 and indicatorOfParameter == 142:
            return 'lhcv'

        if table2Version == 254 and indicatorOfParameter == 141:
            return 'cine'

        if table2Version == 254 and indicatorOfParameter == 140:
            return 'cape'

        if table2Version == 254 and indicatorOfParameter == 139:
            return 'mxwv'

        if table2Version == 254 and indicatorOfParameter == 138:
            return 'mxwu'

        if table2Version == 254 and indicatorOfParameter == 137:
            return 'mask'

        if table2Version == 254 and indicatorOfParameter == 136:
            return 'pslm'

        if table2Version == 254 and indicatorOfParameter == 135:
            return 'pslc'

        if table2Version == 254 and indicatorOfParameter == 134:
            return 'lnsp'

        if table2Version == 254 and indicatorOfParameter == 133:
            return 'gsfp'

        if table2Version == 254 and indicatorOfParameter == 132:
            return 'topo'

        if table2Version == 254 and indicatorOfParameter == 131:
            return 'v10m'

        if table2Version == 254 and indicatorOfParameter == 130:
            return 'u10m'

        if table2Version == 254 and indicatorOfParameter == 129:
            return 'dp2m'

        if table2Version == 254 and indicatorOfParameter == 128:
            return 'tp2m'

        if table2Version == 254 and indicatorOfParameter == 127:
            return 'imag'

        if table2Version == 254 and indicatorOfParameter == 123:
            return 'blds'

        if table2Version == 254 and indicatorOfParameter == 122:
            return 'cssf'

        if table2Version == 254 and indicatorOfParameter == 121:
            return 'clsf'

        if table2Version == 254 and indicatorOfParameter == 117:
            return 'glbr'

        if table2Version == 254 and indicatorOfParameter == 116:
            return 'swea'

        if table2Version == 254 and indicatorOfParameter == 115:
            return 'lwrd'

        if table2Version == 254 and indicatorOfParameter == 114:
            return 'role'

        if table2Version == 254 and indicatorOfParameter == 113:
            return 'nswr'

        if table2Version == 254 and indicatorOfParameter == 112:
            return 'slds'

        if table2Version == 254 and indicatorOfParameter == 111:
            return 'ocas'

        if table2Version == 254 and indicatorOfParameter == 110:
            return 'swmp'

        if table2Version == 254 and indicatorOfParameter == 109:
            return 'swdi'

        if table2Version == 254 and indicatorOfParameter == 108:
            return 'prmp'

        if table2Version == 254 and indicatorOfParameter == 107:
            return 'prwd'

        if table2Version == 254 and indicatorOfParameter == 106:
            return 'swmp'

        if table2Version == 254 and indicatorOfParameter == 105:
            return 'swsh'

        if table2Version == 254 and indicatorOfParameter == 104:
            return 'swdi'

        if table2Version == 254 and indicatorOfParameter == 103:
            return 'wwmp'

        if table2Version == 254 and indicatorOfParameter == 102:
            return 'wwsh'

        if table2Version == 254 and indicatorOfParameter == 101:
            return 'wwdi'

        if table2Version == 254 and indicatorOfParameter == 100:
            return 'shcw'

        if table2Version == 254 and indicatorOfParameter == 98:
            return 'icdv'

        if table2Version == 254 and indicatorOfParameter == 97:
            return 'iceg'

        if table2Version == 254 and indicatorOfParameter == 96:
            return 'icev'

        if table2Version == 254 and indicatorOfParameter == 95:
            return 'iceu'

        if table2Version == 254 and indicatorOfParameter == 94:
            return 'ices'

        if table2Version == 254 and indicatorOfParameter == 93:
            return 'iced'

        if table2Version == 254 and indicatorOfParameter == 92:
            return 'icet'

        if table2Version == 254 and indicatorOfParameter == 91:
            return 'icec'

        if table2Version == 254 and indicatorOfParameter == 89:
            return 'dens'

        if table2Version == 254 and indicatorOfParameter == 87:
            return 'vege'

        if table2Version == 254 and indicatorOfParameter == 86:
            return 'soic'

        if table2Version == 254 and indicatorOfParameter == 85:
            return 'dstp'

        if table2Version == 254 and indicatorOfParameter == 84:
            return 'albe'

        if table2Version == 254 and indicatorOfParameter == 83:
            return 'zorl'

        if table2Version == 254 and indicatorOfParameter == 82:
            return 'dslm'

        if table2Version == 254 and indicatorOfParameter == 81:
            return 'lsmk'

        if table2Version == 254 and indicatorOfParameter == 77:
            return 'bli'

        if table2Version == 254 and indicatorOfParameter == 76:
            return 'wtnv'

        if table2Version == 254 and indicatorOfParameter == 75:
            return 'hinv'

        if table2Version == 254 and indicatorOfParameter == 74:
            return 'mdnv'

        if table2Version == 254 and indicatorOfParameter == 73:
            return 'lwnv'

        if table2Version == 254 and indicatorOfParameter == 72:
            return 'cvnv'

        if table2Version == 254 and indicatorOfParameter == 71:
            return 'cbnv'

        if table2Version == 254 and indicatorOfParameter == 70:
            return 'mtha'

        if table2Version == 254 and indicatorOfParameter == 69:
            return 'mthd'

        if table2Version == 254 and indicatorOfParameter == 68:
            return 'tthd'

        if table2Version == 254 and indicatorOfParameter == 67:
            return 'mxld'

        if table2Version == 254 and indicatorOfParameter == 66:
            return 'nvde'

        if table2Version == 254 and indicatorOfParameter == 65:
            return 'wenv'

        if table2Version == 254 and indicatorOfParameter == 64:
            return 'neve'

        if table2Version == 254 and indicatorOfParameter == 63:
            return 'prcv'

        if table2Version == 254 and indicatorOfParameter == 62:
            return 'prge'

        if table2Version == 254 and indicatorOfParameter == 61:
            return 'prec'

        if table2Version == 254 and indicatorOfParameter == 60:
            return 'thpb'

        if table2Version == 254 and indicatorOfParameter == 59:
            return 'prcr'

        if table2Version == 254 and indicatorOfParameter == 57:
            return 'evap'

        if table2Version == 254 and indicatorOfParameter == 56:
            return 'sadf'

        if table2Version == 254 and indicatorOfParameter == 55:
            return 'vapp'

        if table2Version == 254 and indicatorOfParameter == 54:
            return 'agpl'

        if table2Version == 254 and indicatorOfParameter == 53:
            return 'hmxr'

        if table2Version == 254 and indicatorOfParameter == 52:
            return 'umrl'

        if table2Version == 254 and indicatorOfParameter == 51:
            return 'umes'

        if table2Version == 254 and indicatorOfParameter == 50:
            return 'vcpc'

        if table2Version == 254 and indicatorOfParameter == 49:
            return 'ucpc'

        if table2Version == 254 and indicatorOfParameter == 48:
            return 'spdc'

        if table2Version == 254 and indicatorOfParameter == 47:
            return 'dirc'

        if table2Version == 254 and indicatorOfParameter == 46:
            return 'vvcs'

        if table2Version == 254 and indicatorOfParameter == 45:
            return 'vucs'

        if table2Version == 254 and indicatorOfParameter == 44:
            return 'divg'

        if table2Version == 254 and indicatorOfParameter == 43:
            return 'vort'

        if table2Version == 254 and indicatorOfParameter == 42:
            return 'abdv'

        if table2Version == 254 and indicatorOfParameter == 41:
            return 'abvo'

        if table2Version == 254 and indicatorOfParameter == 40:
            return 'omg2'

        if table2Version == 254 and indicatorOfParameter == 39:
            return 'omeg'

        if table2Version == 254 and indicatorOfParameter == 38:
            return 'sgvv'

        if table2Version == 254 and indicatorOfParameter == 36:
            return 'potv'

        if table2Version == 254 and indicatorOfParameter == 35:
            return 'fcor'

        if table2Version == 254 and indicatorOfParameter == 34:
            return 'vvel'

        if table2Version == 254 and indicatorOfParameter == 33:
            return 'uvel'

        if table2Version == 254 and indicatorOfParameter == 32:
            return 'wins'

        if table2Version == 254 and indicatorOfParameter == 31:
            return 'wind'

        if table2Version == 254 and indicatorOfParameter == 30:
            return 'wvs3'

        if table2Version == 254 and indicatorOfParameter == 29:
            return 'wvs2'

        if table2Version == 254 and indicatorOfParameter == 28:
            return 'wvs1'

        if table2Version == 254 and indicatorOfParameter == 27:
            return 'zgan'

        if table2Version == 254 and indicatorOfParameter == 26:
            return 'psan'

        if table2Version == 254 and indicatorOfParameter == 25:
            return 'tpan'

        if table2Version == 254 and indicatorOfParameter == 23:
            return 'rds3'

        if table2Version == 254 and indicatorOfParameter == 22:
            return 'rds2'

        if table2Version == 254 and indicatorOfParameter == 21:
            return 'rds1'

        if table2Version == 254 and indicatorOfParameter == 19:
            return 'lpsr'

        if table2Version == 254 and indicatorOfParameter == 18:
            return 'dptd'

        if table2Version == 254 and indicatorOfParameter == 17:
            return 'tpor'

        if table2Version == 254 and indicatorOfParameter == 16:
            return 'mntp'

        if table2Version == 254 and indicatorOfParameter == 15:
            return 'mxtp'

        if table2Version == 254 and indicatorOfParameter == 14:
            return 'psat'

        if table2Version == 254 and indicatorOfParameter == 13:
            return 'ptmp'

        if table2Version == 254 and indicatorOfParameter == 12:
            return 'vtmp'

        if table2Version == 254 and indicatorOfParameter == 11:
            return 'temp'

        if table2Version == 254 and indicatorOfParameter == 8:
            return 'gzge'

        if table2Version == 254 and indicatorOfParameter == 7:
            return 'zgeo'

        if table2Version == 254 and indicatorOfParameter == 6:
            return 'geop'

        if table2Version == 254 and indicatorOfParameter == 3:
            return 'tsps'

        if table2Version == 254 and indicatorOfParameter == 2:
            return 'psnm'

        if table2Version == 254 and indicatorOfParameter == 1:
            return 'pres'

    return wrapped
