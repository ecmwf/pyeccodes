import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 253 and indicatorOfParameter == 255:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 254:
            return 'aerd'

        if table2Version == 253 and indicatorOfParameter == 253:
            return 'aerc'

        if table2Version == 253 and indicatorOfParameter == 252:
            return 'aerl'

        if table2Version == 253 and indicatorOfParameter == 251:
            return 'aers'

        if table2Version == 253 and indicatorOfParameter == 250:
            return 'co'

        if table2Version == 253 and indicatorOfParameter == 249:
            return 'bo'

        if table2Version == 253 and indicatorOfParameter == 248:
            return 'ao'

        if table2Version == 253 and indicatorOfParameter == 247:
            return 'shis'

        if table2Version == 253 and indicatorOfParameter == 246:
            return 'snsub'

        if table2Version == 253 and indicatorOfParameter == 245:
            return 'wevap'

        if table2Version == 253 and indicatorOfParameter == 244:
            return 'lhsub'

        if table2Version == 253 and indicatorOfParameter == 243:
            return 'dutp'

        if table2Version == 253 and indicatorOfParameter == 242:
            return 'rmx'

        if table2Version == 253 and indicatorOfParameter == 241:
            return 'rmn'

        if table2Version == 253 and indicatorOfParameter == 240:
            return 'rev'

        if table2Version == 253 and indicatorOfParameter == 239:
            return 'zt'

        if table2Version == 253 and indicatorOfParameter == 238:
            return 'swv'

        if table2Version == 253 and indicatorOfParameter == 237:
            return 'sld'

        if table2Version == 253 and indicatorOfParameter == 236:
            return 'sdmax'

        if table2Version == 253 and indicatorOfParameter == 235:
            return 'se'

        if table2Version == 253 and indicatorOfParameter == 234:
            return 'dvi'

        if table2Version == 253 and indicatorOfParameter == 232:
            return 'lai'

        if table2Version == 253 and indicatorOfParameter == 231:
            return 'smnr'

        if table2Version == 253 and indicatorOfParameter == 230:
            return 'alv'

        if table2Version == 253 and indicatorOfParameter == 229:
            return 'alb'

        if table2Version == 253 and indicatorOfParameter == 228:
            return 'fg'

        if table2Version == 253 and indicatorOfParameter == 227:
            return 'vegmax'

        if table2Version == 253 and indicatorOfParameter == 226:
            return 'slfr'

        if table2Version == 253 and indicatorOfParameter == 225:
            return 'clfr'

        if table2Version == 253 and indicatorOfParameter == 224:
            return 'srveg'

        if table2Version == 253 and indicatorOfParameter == 223:
            return 'srbs'

        if table2Version == 253 and indicatorOfParameter == 222:
            return 'dtop'

        if table2Version == 253 and indicatorOfParameter == 221:
            return 'atop'

        if table2Version == 253 and indicatorOfParameter == 220:
            return 'stdo'

        if table2Version == 253 and indicatorOfParameter == 219:
            return 'alns'

        if table2Version == 253 and indicatorOfParameter == 217:
            return 'dnmf'

        if table2Version == 253 and indicatorOfParameter == 216:
            return 'upmf'

        if table2Version == 253 and indicatorOfParameter == 215:
            return 'dnom'

        if table2Version == 253 and indicatorOfParameter == 214:
            return 'upom'

        if table2Version == 253 and indicatorOfParameter == 213:
            return 'vdiv'

        if table2Version == 253 and indicatorOfParameter == 212:
            return 'pdep'

        if table2Version == 253 and indicatorOfParameter == 211:
            return 'lgt'

        if table2Version == 253 and indicatorOfParameter == 210:
            return 'refl'

        if table2Version == 253 and indicatorOfParameter == 204:
            return 'hail'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'grpl'

        if table2Version == 253 and indicatorOfParameter == 200:
            return 'tke'

        if table2Version == 253 and indicatorOfParameter == 196:
            return 'gwdv'

        if table2Version == 253 and indicatorOfParameter == 195:
            return 'gwdu'

        if table2Version == 253 and indicatorOfParameter == 193:
            return 'w_so_ice'

        if table2Version == 253 and indicatorOfParameter == 192:
            return 'w_i'

        if table2Version == 253 and indicatorOfParameter == 191:
            return 'rsn'

        if table2Version == 253 and indicatorOfParameter == 190:
            return 'asn'

        if table2Version == 253 and indicatorOfParameter == 188:
            return 'ful'

        if table2Version == 253 and indicatorOfParameter == 187:
            return 'ct'

        if table2Version == 253 and indicatorOfParameter == 186:
            return 'cb'

        if table2Version == 253 and indicatorOfParameter == 185:
            return 'tpsolid'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'snow'

        if table2Version == 253 and indicatorOfParameter == 183:
            return 'cr'

        if table2Version == 253 and indicatorOfParameter == 182:
            return 'srain'

        if table2Version == 253 and indicatorOfParameter == 181:
            return 'rain'

        if table2Version == 253 and indicatorOfParameter == 175:
            return 'bt_wv_cl'

        if table2Version == 253 and indicatorOfParameter == 174:
            return 'bt_wv_cs'

        if table2Version == 253 and indicatorOfParameter == 173:
            return 'bt_ir_cl'

        if table2Version == 253 and indicatorOfParameter == 172:
            return 'bt_ir_cs'

        if table2Version == 253 and indicatorOfParameter == 171:
            return 'bt_oz_cl'

        if table2Version == 253 and indicatorOfParameter == 170:
            return 'bt_oz_cs'

        if table2Version == 253 and indicatorOfParameter == 167:
            return 'totqv'

        if table2Version == 253 and indicatorOfParameter == 166:
            return 'mcn'

        if table2Version == 253 and indicatorOfParameter == 163:
            return 'vgst'

        if table2Version == 253 and indicatorOfParameter == 162:
            return 'ugst'

        if table2Version == 253 and indicatorOfParameter == 161:
            return 'xhail'

        if table2Version == 253 and indicatorOfParameter == 160:
            return 'cape'

        if table2Version == 253 and indicatorOfParameter == 158:
            return 'mrad'

        if table2Version == 253 and indicatorOfParameter == 144:
            return 'prtp'

        if table2Version == 253 and indicatorOfParameter == 140:
            return 'dni'

        if table2Version == 253 and indicatorOfParameter == 139:
            return 'pscw'

        if table2Version == 253 and indicatorOfParameter == 138:
            return 'pstbc'

        if table2Version == 253 and indicatorOfParameter == 137:
            return 'pstb'

        if table2Version == 253 and indicatorOfParameter == 136:
            return 'psct'

        if table2Version == 253 and indicatorOfParameter == 135:
            return 'icei'

        if table2Version == 253 and indicatorOfParameter == 133:
            return 'msca'

        if table2Version == 253 and indicatorOfParameter == 132:
            return 'lhe'

        if table2Version == 253 and indicatorOfParameter == 131:
            return 'cslw'

        if table2Version == 253 and indicatorOfParameter == 130:
            return 'cssw'

        if table2Version == 253 and indicatorOfParameter == 129:
            return 'frmsp'

        if table2Version == 253 and indicatorOfParameter == 128:
            return 'armsp'

        if table2Version == 253 and indicatorOfParameter == 127:
            return 'imgd'

        if table2Version == 253 and indicatorOfParameter == 126:
            return 'wmixe'

        if table2Version == 253 and indicatorOfParameter == 125:
            return 'vflx'

        if table2Version == 253 and indicatorOfParameter == 124:
            return 'uflx'

        if table2Version == 253 and indicatorOfParameter == 123:
            return 'bld'

        if table2Version == 253 and indicatorOfParameter == 122:
            return 'sshf'

        if table2Version == 253 and indicatorOfParameter == 121:
            return 'slhf'

        if table2Version == 253 and indicatorOfParameter == 120:
            return 'swrad'

        if table2Version == 253 and indicatorOfParameter == 119:
            return 'lwrad'

        if table2Version == 253 and indicatorOfParameter == 118:
            return 'btmp'

        if table2Version == 253 and indicatorOfParameter == 117:
            return 'grad'

        if table2Version == 253 and indicatorOfParameter == 116:
            return 'swavr'

        if table2Version == 253 and indicatorOfParameter == 115:
            return 'lwavr'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'nlwrt'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'nswrt'

        if table2Version == 253 and indicatorOfParameter == 112:
            return 'nlwrs'

        if table2Version == 253 and indicatorOfParameter == 111:
            return 'nswrs'

        if table2Version == 253 and indicatorOfParameter == 110:
            return 'swp'

        if table2Version == 253 and indicatorOfParameter == 109:
            return 'dirsw'

        if table2Version == 253 and indicatorOfParameter == 108:
            return 'mpps'

        if table2Version == 253 and indicatorOfParameter == 107:
            return 'mdps'

        if table2Version == 253 and indicatorOfParameter == 106:
            return 'swper'

        if table2Version == 253 and indicatorOfParameter == 105:
            return 'swell'

        if table2Version == 253 and indicatorOfParameter == 104:
            return 'swdir'

        if table2Version == 253 and indicatorOfParameter == 103:
            return 'mpww'

        if table2Version == 253 and indicatorOfParameter == 102:
            return 'shww'

        if table2Version == 253 and indicatorOfParameter == 101:
            return 'mdww'

        if table2Version == 253 and indicatorOfParameter == 100:
            return 'swh'

        if table2Version == 253 and indicatorOfParameter == 99:
            return 'snom'

        if table2Version == 253 and indicatorOfParameter == 98:
            return 'iced'

        if table2Version == 253 and indicatorOfParameter == 97:
            return 'iceg'

        if table2Version == 253 and indicatorOfParameter == 96:
            return 'vice'

        if table2Version == 253 and indicatorOfParameter == 95:
            return 'uice'

        if table2Version == 253 and indicatorOfParameter == 94:
            return 'siced'

        if table2Version == 253 and indicatorOfParameter == 93:
            return 'diced'

        if table2Version == 253 and indicatorOfParameter == 92:
            return 'icetk'

        if table2Version == 253 and indicatorOfParameter == 91:
            return 'icec'

        if table2Version == 253 and indicatorOfParameter == 90:
            return 'ro'

        if table2Version == 253 and indicatorOfParameter == 89:
            return 'den'

        if table2Version == 253 and indicatorOfParameter == 88:
            return 's'

        if table2Version == 253 and indicatorOfParameter == 87:
            return 'veg'

        if table2Version == 253 and indicatorOfParameter == 86:
            return 'sm'

        if table2Version == 253 and indicatorOfParameter == 85:
            return 'st'

        if table2Version == 253 and indicatorOfParameter == 84:
            return 'al'

        if table2Version == 253 and indicatorOfParameter == 83:
            return 'sr'

        if table2Version == 253 and indicatorOfParameter == 82:
            return 'dslm'

        if table2Version == 253 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 253 and indicatorOfParameter == 80:
            return 'wtmp'

        if table2Version == 253 and indicatorOfParameter == 79:
            return 'lsf'

        if table2Version == 253 and indicatorOfParameter == 78:
            return 'csf'

        if table2Version == 253 and indicatorOfParameter == 77:
            return 'bli'

        if table2Version == 253 and indicatorOfParameter == 76:
            return 'cwat'

        if table2Version == 253 and indicatorOfParameter == 75:
            return 'hcc'

        if table2Version == 253 and indicatorOfParameter == 74:
            return 'mcc'

        if table2Version == 253 and indicatorOfParameter == 73:
            return 'lcc'

        if table2Version == 253 and indicatorOfParameter == 72:
            return 'ccc'

        if table2Version == 253 and indicatorOfParameter == 71:
            return 'tcc'

        if table2Version == 253 and indicatorOfParameter == 70:
            return 'mtha'

        if table2Version == 253 and indicatorOfParameter == 69:
            return 'mthd'

        if table2Version == 253 and indicatorOfParameter == 68:
            return 'tthdp'

        if table2Version == 253 and indicatorOfParameter == 67:
            return 'mld'

        if table2Version == 253 and indicatorOfParameter == 66:
            return 'sd'

        if table2Version == 253 and indicatorOfParameter == 65:
            return 'sf'

        if table2Version == 253 and indicatorOfParameter == 64:
            return 'srweq'

        if table2Version == 253 and indicatorOfParameter == 63:
            return 'acpcp'

        if table2Version == 253 and indicatorOfParameter == 62:
            return 'lsp'

        if table2Version == 253 and indicatorOfParameter == 61:
            return 'tp'

        if table2Version == 253 and indicatorOfParameter == 60:
            return 'tstm'

        if table2Version == 253 and indicatorOfParameter == 59:
            return 'prate'

        if table2Version == 253 and indicatorOfParameter == 58:
            return 'ciwc'

        if table2Version == 253 and indicatorOfParameter == 57:
            return 'e'

        if table2Version == 253 and indicatorOfParameter == 56:
            return 'satd'

        if table2Version == 253 and indicatorOfParameter == 55:
            return 'vp'

        if table2Version == 253 and indicatorOfParameter == 54:
            return 'pwat'

        if table2Version == 253 and indicatorOfParameter == 53:
            return 'mixr'

        if table2Version == 253 and indicatorOfParameter == 52:
            return 'r'

        if table2Version == 253 and indicatorOfParameter == 51:
            return 'q'

        if table2Version == 253 and indicatorOfParameter == 50:
            return 'vcurr'

        if table2Version == 253 and indicatorOfParameter == 49:
            return 'ucurr'

        if table2Version == 253 and indicatorOfParameter == 48:
            return 'spc'

        if table2Version == 253 and indicatorOfParameter == 47:
            return 'dirc'

        if table2Version == 253 and indicatorOfParameter == 46:
            return 'vvcsh'

        if table2Version == 253 and indicatorOfParameter == 45:
            return 'vucsh'

        if table2Version == 253 and indicatorOfParameter == 44:
            return 'd'

        if table2Version == 253 and indicatorOfParameter == 43:
            return 'vo'

        if table2Version == 253 and indicatorOfParameter == 42:
            return 'absd'

        if table2Version == 253 and indicatorOfParameter == 41:
            return 'absv'

        if table2Version == 253 and indicatorOfParameter == 40:
            return 'tw'

        if table2Version == 253 and indicatorOfParameter == 39:
            return 'w'

        if table2Version == 253 and indicatorOfParameter == 38:
            return 'sgcvv'

        if table2Version == 253 and indicatorOfParameter == 37:
            return 'mntsf'

        if table2Version == 253 and indicatorOfParameter == 36:
            return 'vp'

        if table2Version == 253 and indicatorOfParameter == 35:
            return 'strf'

        if table2Version == 253 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 253 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 253 and indicatorOfParameter == 32:
            return 'ws'

        if table2Version == 253 and indicatorOfParameter == 31:
            return 'wdir'

        if table2Version == 253 and indicatorOfParameter == 30:
            return 'wvsp3'

        if table2Version == 253 and indicatorOfParameter == 29:
            return 'wvsp2'

        if table2Version == 253 and indicatorOfParameter == 28:
            return 'wvsp1'

        if table2Version == 253 and indicatorOfParameter == 27:
            return 'gpa'

        if table2Version == 253 and indicatorOfParameter == 26:
            return 'presa'

        if table2Version == 253 and indicatorOfParameter == 25:
            return 'ta'

        if table2Version == 253 and indicatorOfParameter == 24:
            return 'pli'

        if table2Version == 253 and indicatorOfParameter == 23:
            return 'rdsp3'

        if table2Version == 253 and indicatorOfParameter == 22:
            return 'rdsp2'

        if table2Version == 253 and indicatorOfParameter == 21:
            return 'rdsp1'

        if table2Version == 253 and indicatorOfParameter == 20:
            return 'vis'

        if table2Version == 253 and indicatorOfParameter == 19:
            return 'lapr'

        if table2Version == 253 and indicatorOfParameter == 18:
            return 'depr'

        if table2Version == 253 and indicatorOfParameter == 17:
            return 'td'

        if table2Version == 253 and indicatorOfParameter == 16:
            return 'tmin'

        if table2Version == 253 and indicatorOfParameter == 15:
            return 'tmax'

        if table2Version == 253 and indicatorOfParameter == 14:
            return 'papt'

        if table2Version == 253 and indicatorOfParameter == 13:
            return 'pt'

        if table2Version == 253 and indicatorOfParameter == 12:
            return 'vptmp'

        if table2Version == 253 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 253 and indicatorOfParameter == 10:
            return 'tco3'

        if table2Version == 253 and indicatorOfParameter == 9:
            return 'hstdv'

        if table2Version == 253 and indicatorOfParameter == 8:
            return 'h'

        if table2Version == 253 and indicatorOfParameter == 7:
            return 'gh'

        if table2Version == 253 and indicatorOfParameter == 6:
            return 'z'

        if table2Version == 253 and indicatorOfParameter == 5:
            return 'icaht'

        if table2Version == 253 and indicatorOfParameter == 4:
            return 'pv'

        if table2Version == 253 and indicatorOfParameter == 3:
            return 'ptend'

        if table2Version == 253 and indicatorOfParameter == 2:
            return 'msl'

        if table2Version == 253 and indicatorOfParameter == 1:
            return 'pres'

        if table2Version == 1 and indicatorOfParameter == 228:
            return 'gust'

        if table2Version == 1 and indicatorOfParameter == 209:
            return 'sdsso'

        if table2Version == 1 and indicatorOfParameter == 208:
            return 'mssso'

        if table2Version == 1 and indicatorOfParameter == 200:
            return 'tke'

        if table2Version == 1 and indicatorOfParameter == 199:
            return 'vgtyp'

        if table2Version == 1 and indicatorOfParameter == 198:
            return 'fool'

        if table2Version == 1 and indicatorOfParameter == 197:
            return 'fof'

        if table2Version == 1 and indicatorOfParameter == 196:
            return 'fol'

        if table2Version == 1 and indicatorOfParameter == 195:
            return 'sltyp'

        if table2Version == 1 and indicatorOfParameter == 193:
            return 'ssi'

        if table2Version == 1 and indicatorOfParameter == 192:
            return 'watcn'

        if table2Version == 1 and indicatorOfParameter == 191:
            return 'dsn'

        if table2Version == 1 and indicatorOfParameter == 190:
            return 'asn'

        if table2Version == 1 and indicatorOfParameter == 167:
            return 'frasp'

        if table2Version == 1 and indicatorOfParameter == 166:
            return 'skwf'

        if table2Version == 1 and indicatorOfParameter == 165:
            return 'susl'

        if table2Version == 1 and indicatorOfParameter == 163:
            return 'rshb'

        if table2Version == 1 and indicatorOfParameter == 162:
            return 'rsha'

        if table2Version == 1 and indicatorOfParameter == 161:
            return 'shfr'

        if table2Version == 1 and indicatorOfParameter == 160:
            return 'slfr'

        if table2Version == 1 and indicatorOfParameter == 143:
            return 'dptland'

        if table2Version == 1 and indicatorOfParameter == 142:
            return 'rhland'

        if table2Version == 1 and indicatorOfParameter == 141:
            return 'qland'

        if table2Version == 1 and indicatorOfParameter == 140:
            return 'tland'

        if table2Version == 1 and indicatorOfParameter == 135:
            return 'maxv'

        if table2Version == 1 and indicatorOfParameter == 128:
            return 'mofl'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 'imgd'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'wmixe'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'vflx'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'uflx'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'bld'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'sshf'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'slhf'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'swrad'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'lwrad'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'btmp'

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

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'ro'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'den'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 87:
            return 'veg'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'sm'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'st'

        if table2Version == 1 and indicatorOfParameter == 84:
            return 'al'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'sr'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'dslm'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'wtmp'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'lsf'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'csf'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'bli'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'cwat'

        if table2Version == 1 and indicatorOfParameter == 75:
            return 'hcc'

        if table2Version == 1 and indicatorOfParameter == 74:
            return 'mcc'

        if table2Version == 1 and indicatorOfParameter == 73:
            return 'lcc'

        if table2Version == 1 and indicatorOfParameter == 72:
            return 'ccc'

        if table2Version == 1 and indicatorOfParameter == 71:
            return 'tcc'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'mtha'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'mthd'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'tthdp'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'mld'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'sd'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'sf'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'srweq'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'acpcp'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'lsp'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'tp'

        if table2Version == 1 and indicatorOfParameter == 60:
            return 'tstm'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'prate'

        if table2Version == 1 and indicatorOfParameter == 58:
            return 'ciwc'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'e'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'satd'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'vp'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'pwat'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'mixr'

        if table2Version == 1 and indicatorOfParameter == 52:
            return 'r'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'q'

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

        if table2Version == 1 and indicatorOfParameter == 44:
            return 'd'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 'vo'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 'absd'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 'absv'

        if table2Version == 1 and indicatorOfParameter == 40:
            return 'tw'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'w'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 'sgcvv'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'mntsf'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'vp'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'strf'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'ws'

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
            return 'td'

        if table2Version == 1 and indicatorOfParameter == 16:
            return 'tmin'

        if table2Version == 1 and indicatorOfParameter == 15:
            return 'tmax'

        if table2Version == 1 and indicatorOfParameter == 14:
            return 'papt'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'pt'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'vptmp'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'tco3'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'hstdv'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'h'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'gh'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'z'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'icaht'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'pv'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'ptend'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'msl'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'pres'

        if table2Version == 1 and indicatorOfParameter == 0:
            return 'Reserved'

    return wrapped
