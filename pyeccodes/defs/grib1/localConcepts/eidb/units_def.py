import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 253 and indicatorOfParameter == 255:
            return 0

        if table2Version == 253 and indicatorOfParameter == 254:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 253:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 252:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 251:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 250:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 249:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 248:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 247:
            return '???'

        if table2Version == 253 and indicatorOfParameter == 246:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 245:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 244:
            return 'J kg**-1'

        if table2Version == 253 and indicatorOfParameter == 243:
            return 's'

        if table2Version == 253 and indicatorOfParameter == 242:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 241:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 240:
            return 's m**-1'

        if table2Version == 253 and indicatorOfParameter == 239:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 238:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 237:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 236:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 235:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 234:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 232:
            return 'm**2 m**-2'

        if table2Version == 253 and indicatorOfParameter == 231:
            return 's m**-1'

        if table2Version == 253 and indicatorOfParameter == 230:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 229:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 228:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 227:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 226:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 225:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 224:
            return 'm2 2**-2'

        if table2Version == 253 and indicatorOfParameter == 223:
            return 'm2 2**-2'

        if table2Version == 253 and indicatorOfParameter == 222:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 221:
            return 'rad'

        if table2Version == 253 and indicatorOfParameter == 220:
            return 'm**2s**-2'

        if table2Version == 253 and indicatorOfParameter == 219:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 217:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 216:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 215:
            return 'ms*-1'

        if table2Version == 253 and indicatorOfParameter == 214:
            return 'ms*-1'

        if table2Version == 253 and indicatorOfParameter == 213:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 212:
            return 'Pa'

        if table2Version == 253 and indicatorOfParameter == 211:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 210:
            return 'dBz'

        if table2Version == 253 and indicatorOfParameter == 204:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 200:
            return 'm**2 s**-2'

        if table2Version == 253 and indicatorOfParameter == 196:
            return 'kg m**-1 s**-1'

        if table2Version == 253 and indicatorOfParameter == 195:
            return 'kg m**-1 s**-1'

        if table2Version == 253 and indicatorOfParameter == 193:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 192:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 191:
            return 'kg m**-3'

        if table2Version == 253 and indicatorOfParameter == 190:
            return '(0-1)'

        if table2Version == 253 and indicatorOfParameter == 188:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 187:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 186:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 185:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 183:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 182:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 181:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 175:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 174:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 173:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 172:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 171:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 170:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 167:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 166:
            return ' kg kg**-1 s**-1'

        if table2Version == 253 and indicatorOfParameter == 163:
            return 'm s*-1'

        if table2Version == 253 and indicatorOfParameter == 162:
            return 'm s*-1'

        if table2Version == 253 and indicatorOfParameter == 161:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 160:
            return 'J kg-1'

        if table2Version == 253 and indicatorOfParameter == 158:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 144:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 140:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 139:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 138:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 137:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 136:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 135:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 133:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 132:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 131:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 130:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 253 and indicatorOfParameter == 128:
            return 'm**2 s**-2'

        if table2Version == 253 and indicatorOfParameter == 127:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 126:
            return 'J'

        if table2Version == 253 and indicatorOfParameter == 125:
            return 'N m**-2'

        if table2Version == 253 and indicatorOfParameter == 124:
            return 'N m**-2'

        if table2Version == 253 and indicatorOfParameter == 123:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 122:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 121:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 120:
            return 'W m-**3 sr**-1'

        if table2Version == 253 and indicatorOfParameter == 119:
            return 'W m**-1 sr**-1'

        if table2Version == 253 and indicatorOfParameter == 118:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 117:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 116:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 115:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 112:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 111:
            return 'W m**-2'

        if table2Version == 253 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 253 and indicatorOfParameter == 109:
            return 'Degree true'

        if table2Version == 253 and indicatorOfParameter == 108:
            return 's'

        if table2Version == 253 and indicatorOfParameter == 107:
            return 'Degree true'

        if table2Version == 253 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 253 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 104:
            return 'Degree true'

        if table2Version == 253 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 253 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 101:
            return 'Degree true'

        if table2Version == 253 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 99:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 98:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 97:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 96:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 95:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 94:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 93:
            return 'Degree true'

        if table2Version == 253 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 91:
            return '(0 - 1)'

        if table2Version == 253 and indicatorOfParameter == 90:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 89:
            return 'kg m**-3'

        if table2Version == 253 and indicatorOfParameter == 88:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 86:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 84:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 81:
            return '(0 - 1)'

        if table2Version == 253 and indicatorOfParameter == 80:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 76:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 75:
            return '(0 - 1)'

        if table2Version == 253 and indicatorOfParameter == 74:
            return '(0 - 1)'

        if table2Version == 253 and indicatorOfParameter == 73:
            return '(0 - 1)'

        if table2Version == 253 and indicatorOfParameter == 72:
            return '(0 - 1)'

        if table2Version == 253 and indicatorOfParameter == 71:
            return '(0 - 1)'

        if table2Version == 253 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 65:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 64:
            return 'kg m**-2 s**-1'

        if table2Version == 253 and indicatorOfParameter == 63:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 62:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 61:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 59:
            return 'kg m**-2 s**-1'

        if table2Version == 253 and indicatorOfParameter == 58:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 57:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 56:
            return 'Pa'

        if table2Version == 253 and indicatorOfParameter == 55:
            return 'Pa'

        if table2Version == 253 and indicatorOfParameter == 54:
            return 'kg m**-2'

        if table2Version == 253 and indicatorOfParameter == 53:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 51:
            return 'kg kg**-1'

        if table2Version == 253 and indicatorOfParameter == 50:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 48:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 47:
            return 'Degree true'

        if table2Version == 253 and indicatorOfParameter == 46:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 45:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 44:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 43:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 42:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 41:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 40:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 39:
            return 'Pa s**-1'

        if table2Version == 253 and indicatorOfParameter == 38:
            return 's**-1'

        if table2Version == 253 and indicatorOfParameter == 37:
            return 'm**2 s**-1'

        if table2Version == 253 and indicatorOfParameter == 36:
            return 'm2 s**-1'

        if table2Version == 253 and indicatorOfParameter == 35:
            return 'm2 s**-1'

        if table2Version == 253 and indicatorOfParameter == 34:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 33:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 32:
            return 'm s**-1'

        if table2Version == 253 and indicatorOfParameter == 31:
            return 'Degree true'

        if table2Version == 253 and indicatorOfParameter == 30:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 29:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 28:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 27:
            return 'gpm'

        if table2Version == 253 and indicatorOfParameter == 26:
            return 'Pa'

        if table2Version == 253 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 24:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 23:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 22:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 21:
            return '-'

        if table2Version == 253 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 19:
            return 'K m**-1'

        if table2Version == 253 and indicatorOfParameter == 18:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 16:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 15:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 14:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 10:
            return 'Dobson'

        if table2Version == 253 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 253 and indicatorOfParameter == 6:
            return 'm**2 s**-2'

        if table2Version == 253 and indicatorOfParameter == 5:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 4:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 253 and indicatorOfParameter == 3:
            return 'Pa s**-1'

        if table2Version == 253 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 253 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 228:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 209:
            return 'gpm'

        if table2Version == 1 and indicatorOfParameter == 208:
            return 'rad'

        if table2Version == 1 and indicatorOfParameter == 200:
            return 'J kg**-1'

        if table2Version == 1 and indicatorOfParameter == 199:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 198:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 197:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 196:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 195:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 193:
            return 'm**3 m**-3'

        if table2Version == 1 and indicatorOfParameter == 192:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 191:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 190:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 167:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 166:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 165:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 163:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 162:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 161:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 160:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 143:
            return 0

        if table2Version == 1 and indicatorOfParameter == 142:
            return 0

        if table2Version == 1 and indicatorOfParameter == 141:
            return 'kg kg**-1'

        if table2Version == 1 and indicatorOfParameter == 140:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 135:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 128:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 0

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'J'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'N m**-2'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'N m**-2'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'W m-**3 sr**-1'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'W m**-1 sr**-1'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 108:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 107:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 104:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 101:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 97:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 96:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 95:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 94:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 93:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 91:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'kg m**-3'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 'kg kg**-1'

        if table2Version == 1 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 81:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 75:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 74:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 73:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 72:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 71:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'kg m**-2 s**-1'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'kg m**-2 s**-1'

        if table2Version == 1 and indicatorOfParameter == 58:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'kg kg**-1'

        if table2Version == 1 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'kg kg**-1'

        if table2Version == 1 and indicatorOfParameter == 50:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 48:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 47:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 46:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 45:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 44:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 40:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'Pa s**-1'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'm**2 s**-1'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'm2 s**-1'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'm2 s**-1'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 31:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 30:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 29:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 28:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 27:
            return 'gpm'

        if table2Version == 1 and indicatorOfParameter == 26:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 24:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 23:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 22:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 21:
            return '-'

        if table2Version == 1 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 19:
            return 'K m**-1'

        if table2Version == 1 and indicatorOfParameter == 18:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 16:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 15:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 14:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'Dobson'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'm**2 s**-2'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'Pa s**-1'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 0:
            return 'Reserved'

    return wrapped
