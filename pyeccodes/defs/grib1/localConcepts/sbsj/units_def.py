import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 254 and indicatorOfParameter == 255:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 254:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 253:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 252:
            return 'm**2 s**-1'

        if table2Version == 254 and indicatorOfParameter == 251:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 250:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 249:
            return 'm**2 s**-1'

        if table2Version == 254 and indicatorOfParameter == 248:
            return 'kg kg**-1'

        if table2Version == 254 and indicatorOfParameter == 247:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 246:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 245:
            return '%'

        if table2Version == 254 and indicatorOfParameter == 244:
            return 'kg m**-2'

        if table2Version == 254 and indicatorOfParameter == 243:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 242:
            return 'cbar s**-1'

        if table2Version == 254 and indicatorOfParameter == 241:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 240:
            return '-/+'

        if table2Version == 254 and indicatorOfParameter == 239:
            return 'ln(cbar)'

        if table2Version == 254 and indicatorOfParameter == 238:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 237:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 236:
            return 'Pa s**-1'

        if table2Version == 254 and indicatorOfParameter == 235:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 234:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 233:
            return '~'

        if table2Version == 254 and indicatorOfParameter == 232:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 231:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 230:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 227:
            return '~'

        if table2Version == 254 and indicatorOfParameter == 226:
            return '~'

        if table2Version == 254 and indicatorOfParameter == 225:
            return 'K s**-2'

        if table2Version == 254 and indicatorOfParameter == 224:
            return 'm s**-12'

        if table2Version == 254 and indicatorOfParameter == 223:
            return 'm s**-12'

        if table2Version == 254 and indicatorOfParameter == 222:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 221:
            return 's**-12'

        if table2Version == 254 and indicatorOfParameter == 220:
            return 's**-12'

        if table2Version == 254 and indicatorOfParameter == 219:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 218:
            return 'K s**-2'

        if table2Version == 254 and indicatorOfParameter == 215:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 214:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 213:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 212:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 211:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 210:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 209:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 208:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 207:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 206:
            return 'K s**-2'

        if table2Version == 254 and indicatorOfParameter == 205:
            return 'K s**-2'

        if table2Version == 254 and indicatorOfParameter == 203:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 202:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 201:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 200:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 198:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 197:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 196:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 195:
            return 'Pa'

        if table2Version == 254 and indicatorOfParameter == 194:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 193:
            return 'Pa'

        if table2Version == 254 and indicatorOfParameter == 192:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 191:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 190:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 189:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 188:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 187:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 186:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 185:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 184:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 183:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 182:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 181:
            return 'kg kg**-1'

        if table2Version == 254 and indicatorOfParameter == 180:
            return 'mb'

        if table2Version == 254 and indicatorOfParameter == 179:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 178:
            return 'kg m**-2 s**-1'

        if table2Version == 254 and indicatorOfParameter == 177:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 176:
            return 'Ws m**-2'

        if table2Version == 254 and indicatorOfParameter == 175:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 174:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 173:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 172:
            return 'K s**-2'

        if table2Version == 254 and indicatorOfParameter == 171:
            return 'kg kg**-1 s**-1'

        if table2Version == 254 and indicatorOfParameter == 170:
            return 'kg kg**-1 s**-1'

        if table2Version == 254 and indicatorOfParameter == 169:
            return 'kg m**-2 s**-1'

        if table2Version == 254 and indicatorOfParameter == 168:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 167:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 165:
            return 'Pa'

        if table2Version == 254 and indicatorOfParameter == 164:
            return 'Pa'

        if table2Version == 254 and indicatorOfParameter == 163:
            return 'm s**-12'

        if table2Version == 254 and indicatorOfParameter == 162:
            return 'm s**-12'

        if table2Version == 254 and indicatorOfParameter == 160:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 159:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 158:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 157:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 156:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 155:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 154:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 153:
            return '%'

        if table2Version == 254 and indicatorOfParameter == 152:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 151:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 150:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 149:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 148:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 147:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 146:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 145:
            return 'K s**-2'

        if table2Version == 254 and indicatorOfParameter == 144:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 143:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 142:
            return 'K s**-2'

        if table2Version == 254 and indicatorOfParameter == 141:
            return 'm**2 s**-12'

        if table2Version == 254 and indicatorOfParameter == 140:
            return 'm**2 s**-12'

        if table2Version == 254 and indicatorOfParameter == 139:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 138:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 137:
            return '-/+'

        if table2Version == 254 and indicatorOfParameter == 136:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 135:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 134:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 133:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 132:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 130:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 129:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 128:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 127:
            return 'image^data'

        if table2Version == 254 and indicatorOfParameter == 123:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 122:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 121:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 117:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 116:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 115:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 114:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 113:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 112:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 111:
            return 'W m**-2'

        if table2Version == 254 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 254 and indicatorOfParameter == 109:
            return 'deg'

        if table2Version == 254 and indicatorOfParameter == 108:
            return 's'

        if table2Version == 254 and indicatorOfParameter == 107:
            return 'deg'

        if table2Version == 254 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 254 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 104:
            return 'deg'

        if table2Version == 254 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 254 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 101:
            return 'deg'

        if table2Version == 254 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 98:
            return 's s**-1'

        if table2Version == 254 and indicatorOfParameter == 97:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 96:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 95:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 94:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 93:
            return 'deg'

        if table2Version == 254 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 91:
            return 'Fraction'

        if table2Version == 254 and indicatorOfParameter == 89:
            return 'kg m**-3'

        if table2Version == 254 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 254 and indicatorOfParameter == 86:
            return 'kg m**-2'

        if table2Version == 254 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 254 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 81:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 76:
            return 'kg m**-2'

        if table2Version == 254 and indicatorOfParameter == 75:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 74:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 73:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 72:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 71:
            return '(0 - 1)'

        if table2Version == 254 and indicatorOfParameter == 70:
            return 'm cm'

        if table2Version == 254 and indicatorOfParameter == 69:
            return 'm cm'

        if table2Version == 254 and indicatorOfParameter == 68:
            return 'm cm'

        if table2Version == 254 and indicatorOfParameter == 67:
            return 'm cm'

        if table2Version == 254 and indicatorOfParameter == 66:
            return 'cm'

        if table2Version == 254 and indicatorOfParameter == 65:
            return 'kg m**-2'

        if table2Version == 254 and indicatorOfParameter == 64:
            return 'kg m**-2/day'

        if table2Version == 254 and indicatorOfParameter == 63:
            return 'kg m**-2/day'

        if table2Version == 254 and indicatorOfParameter == 62:
            return 'kg m**-2/day'

        if table2Version == 254 and indicatorOfParameter == 61:
            return 'kg m**-2/day'

        if table2Version == 254 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 254 and indicatorOfParameter == 59:
            return 'kg m**-2/day'

        if table2Version == 254 and indicatorOfParameter == 57:
            return 'kg m**-2/day'

        if table2Version == 254 and indicatorOfParameter == 56:
            return 'Pa hPa'

        if table2Version == 254 and indicatorOfParameter == 55:
            return 'Pa hPa'

        if table2Version == 254 and indicatorOfParameter == 54:
            return 'kg m**-2'

        if table2Version == 254 and indicatorOfParameter == 53:
            return 'kg kg**-1'

        if table2Version == 254 and indicatorOfParameter == 52:
            return '~'

        if table2Version == 254 and indicatorOfParameter == 51:
            return 'kg kg**-1'

        if table2Version == 254 and indicatorOfParameter == 50:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 48:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 47:
            return 'deg'

        if table2Version == 254 and indicatorOfParameter == 46:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 45:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 44:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 43:
            return 's**-1'

        if table2Version == 254 and indicatorOfParameter == 42:
            return '10**5 s**-1'

        if table2Version == 254 and indicatorOfParameter == 41:
            return '10**5 s**-1'

        if table2Version == 254 and indicatorOfParameter == 40:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 39:
            return 'Pa s**-1'

        if table2Version == 254 and indicatorOfParameter == 38:
            return 's s**-1'

        if table2Version == 254 and indicatorOfParameter == 36:
            return 'm**2 s**-1'

        if table2Version == 254 and indicatorOfParameter == 35:
            return 'm**2 s**-1'

        if table2Version == 254 and indicatorOfParameter == 34:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 33:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 32:
            return 'm s**-1'

        if table2Version == 254 and indicatorOfParameter == 31:
            return 'deg'

        if table2Version == 254 and indicatorOfParameter == 30:
            return 'dimensionless'

        if table2Version == 254 and indicatorOfParameter == 29:
            return 'dimensionless'

        if table2Version == 254 and indicatorOfParameter == 28:
            return 'dimensionless'

        if table2Version == 254 and indicatorOfParameter == 27:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 26:
            return 'Pa hPa'

        if table2Version == 254 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 23:
            return 'dimensionless'

        if table2Version == 254 and indicatorOfParameter == 22:
            return 'dimensionless'

        if table2Version == 254 and indicatorOfParameter == 21:
            return 'dimensionless'

        if table2Version == 254 and indicatorOfParameter == 19:
            return 'K m**-1'

        if table2Version == 254 and indicatorOfParameter == 18:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 16:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 15:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 14:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 254 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 254 and indicatorOfParameter == 6:
            return 'dam'

        if table2Version == 254 and indicatorOfParameter == 3:
            return 'Pa s**-1'

        if table2Version == 254 and indicatorOfParameter == 2:
            return 'hPa'

        if table2Version == 254 and indicatorOfParameter == 1:
            return 'hPa'

    return wrapped
