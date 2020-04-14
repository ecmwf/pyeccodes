import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 228 and indicatorOfParameter == 254:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 253:
            return 'm**3 m**-3'

        if table2Version == 228 and indicatorOfParameter == 247:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 246:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 136:
            return 'm s**-2'

        if table2Version == 228 and indicatorOfParameter == 134:
            return 'm s**-2'

        if table2Version == 211 and indicatorOfParameter == 117:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 116:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 115:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 114:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 113:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 112:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 111:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 110:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 109:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 108:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 107:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 106:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 105:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 104:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 103:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 102:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 101:
            return 'W'

        if table2Version == 210 and indicatorOfParameter == 117:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 116:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 115:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 114:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 113:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 112:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 111:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 110:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 109:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 108:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 107:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 106:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 105:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 104:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 103:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 102:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 101:
            return 'W'

        if table2Version == 140 and indicatorOfParameter == 216:
            return 'm s**-1'

        if table2Version == 140 and indicatorOfParameter == 215:
            return 'm s**-1'

        if table2Version == 234 and indicatorOfParameter == 228:
            return '%'

        if table2Version == 234 and indicatorOfParameter == 167:
            return '%'

        if table2Version == 234 and indicatorOfParameter == 151:
            return '%'

        if table2Version == 234 and indicatorOfParameter == 139:
            return '%'

        if table2Version == 230 and indicatorOfParameter == 212:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 211:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 210:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 209:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 208:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 205:
            return 'm'

        if table2Version == 230 and indicatorOfParameter == 198:
            return 'kg m**-2'

        if table2Version == 230 and indicatorOfParameter == 197:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 196:
            return 'N m**-2 s'

        if table2Version == 230 and indicatorOfParameter == 195:
            return 'N m**-2 s'

        if table2Version == 230 and indicatorOfParameter == 189:
            return 's'

        if table2Version == 230 and indicatorOfParameter == 182:
            return 'kg m**-2'

        if table2Version == 230 and indicatorOfParameter == 181:
            return 'N m**-2 s'

        if table2Version == 230 and indicatorOfParameter == 180:
            return 'N m**-2 s'

        if table2Version == 230 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 175:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 169:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 145:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 144:
            return 'm of water equivalent'

        if table2Version == 230 and indicatorOfParameter == 143:
            return 'm'

        if table2Version == 230 and indicatorOfParameter == 142:
            return 'm'

        if table2Version == 230 and indicatorOfParameter == 58:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 57:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 46:
            return 's'

        if table2Version == 230 and indicatorOfParameter == 45:
            return 'kg m**-2'

        if table2Version == 230 and indicatorOfParameter == 44:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 228:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 171:
            return 'kg m**-3'

        if table2Version == 228 and indicatorOfParameter == 170:
            return 'kg m**-3'

        if table2Version == 228 and indicatorOfParameter == 164:
            return '%'

        if table2Version == 228 and indicatorOfParameter == 144:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 141:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 39:
            return 'kg m**-3'

        if table2Version == 228 and indicatorOfParameter == 19:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 18:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 17:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 16:
            return 'm**-1'

        if table2Version == 228 and indicatorOfParameter == 15:
            return 'm**-1'

        if table2Version == 228 and indicatorOfParameter == 14:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 12:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 10:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 8:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 7:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 6:
            return '(0 - 1)'

        if table2Version == 228 and indicatorOfParameter == 5:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 4:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 3:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 2:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 1:
            return 'J kg**-1'

        if table2Version == 220 and indicatorOfParameter == 228:
            return 'dimensionless'

        if table2Version == 211 and indicatorOfParameter == 216:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 215:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 214:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 213:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 212:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 211:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 210:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 209:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 208:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 207:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 206:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 203:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 185:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 184:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 183:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 182:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 181:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 166:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 165:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 164:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 163:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 162:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 161:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 160:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 159:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 158:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 157:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 156:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 155:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 154:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 153:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 152:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 151:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 150:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 149:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 148:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 147:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 146:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 145:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 144:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 143:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 142:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 141:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 140:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 139:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 138:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 137:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 136:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 135:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 134:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 132:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 131:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 130:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 129:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 128:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 127:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 126:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 125:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 124:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 123:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 122:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 121:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 100:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 99:
            return 'W m**-2'

        if table2Version == 211 and indicatorOfParameter == 98:
            return 'm**2'

        if table2Version == 211 and indicatorOfParameter == 97:
            return 'dimensionless'

        if table2Version == 211 and indicatorOfParameter == 96:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 95:
            return 'dimensionless'

        if table2Version == 211 and indicatorOfParameter == 94:
            return 'dimensionless'

        if table2Version == 211 and indicatorOfParameter == 93:
            return 'dimensionless'

        if table2Version == 211 and indicatorOfParameter == 92:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 91:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 90:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 89:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 88:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 87:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 86:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 85:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 84:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 83:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 82:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 81:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 80:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 71:
            return 's**-1'

        if table2Version == 211 and indicatorOfParameter == 70:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 69:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 68:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 67:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 66:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 65:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 64:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 63:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 62:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 61:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 54:
            return '%'

        if table2Version == 211 and indicatorOfParameter == 53:
            return 'm s**-1'

        if table2Version == 211 and indicatorOfParameter == 52:
            return 'kg s**2 m**-5'

        if table2Version == 211 and indicatorOfParameter == 51:
            return 'dimensionless'

        if table2Version == 211 and indicatorOfParameter == 50:
            return 'dimensionless'

        if table2Version == 211 and indicatorOfParameter == 49:
            return 'dimensionless'

        if table2Version == 211 and indicatorOfParameter == 48:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 47:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 46:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 42:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 41:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 40:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 39:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 38:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 37:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 36:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 35:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 34:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 33:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 32:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 31:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 27:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 26:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 25:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 24:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 23:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 22:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 21:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 20:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 19:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 18:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 17:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 16:
            return 'kg m**-2'

        if table2Version == 211 and indicatorOfParameter == 12:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 11:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 10:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 9:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 8:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 7:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 6:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 5:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 4:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 3:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 2:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 1:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 216:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 215:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 214:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 213:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 212:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 211:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 210:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 209:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 208:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 207:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 206:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 203:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 185:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 184:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 183:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 182:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 181:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 166:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 165:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 164:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 163:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 162:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 161:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 160:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 159:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 158:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 157:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 156:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 155:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 154:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 153:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 152:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 151:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 150:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 149:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 148:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 147:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 146:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 145:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 144:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 143:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 142:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 141:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 140:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 139:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 138:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 137:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 136:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 135:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 134:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 132:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 131:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 130:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 129:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 128:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 127:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 126:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 125:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 124:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 123:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 122:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 121:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 100:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 99:
            return 'W m**-2'

        if table2Version == 210 and indicatorOfParameter == 98:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 97:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 96:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 95:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 94:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 93:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 92:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 91:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 90:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 89:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 88:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 87:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 86:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 85:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 84:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 83:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 82:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 81:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 80:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 71:
            return 's**-1'

        if table2Version == 210 and indicatorOfParameter == 70:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 69:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 68:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 67:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 66:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 65:
            return 'ppb'

        if table2Version == 210 and indicatorOfParameter == 64:
            return 'ppm'

        if table2Version == 210 and indicatorOfParameter == 63:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 62:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 61:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 54:
            return '%'

        if table2Version == 210 and indicatorOfParameter == 53:
            return 'm s**-1'

        if table2Version == 210 and indicatorOfParameter == 52:
            return 'kg s**2 m**-5'

        if table2Version == 210 and indicatorOfParameter == 51:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 50:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 49:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 48:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 47:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 46:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 42:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 41:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 40:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 39:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 38:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 37:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 36:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 35:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 34:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 33:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 32:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 31:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 27:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 26:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 25:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 24:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 23:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 22:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 21:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 20:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 19:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 18:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 17:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 16:
            return 'kg m**-2'

        if table2Version == 210 and indicatorOfParameter == 12:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 11:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 10:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 9:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 8:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 7:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 6:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 5:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 4:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 3:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 2:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 1:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 241:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 215:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 203:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 200:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 187:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 150:
            return 'm**2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 139:
            return 'Pa'

        if table2Version == 201 and indicatorOfParameter == 113:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 112:
            return 'kg s**-1 m**-2'

        if table2Version == 201 and indicatorOfParameter == 111:
            return 'kg s**-1 m**-2'

        if table2Version == 201 and indicatorOfParameter == 102:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 101:
            return 'kg s**-1 m**-2'

        if table2Version == 201 and indicatorOfParameter == 100:
            return 'kg s**-1 m**-2'

        if table2Version == 201 and indicatorOfParameter == 99:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 85:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 84:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 83:
            return 'dimensionless'

        if table2Version == 201 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 81:
            return 's**-2'

        if table2Version == 201 and indicatorOfParameter == 80:
            return 's**-2'

        if table2Version == 201 and indicatorOfParameter == 79:
            return 'm s**-2'

        if table2Version == 201 and indicatorOfParameter == 78:
            return 'm s**-2'

        if table2Version == 201 and indicatorOfParameter == 77:
            return 's**-1'

        if table2Version == 201 and indicatorOfParameter == 76:
            return 'J kg**-1 s**-1'

        if table2Version == 201 and indicatorOfParameter == 75:
            return 's**-1'

        if table2Version == 201 and indicatorOfParameter == 74:
            return 'K s**-1'

        if table2Version == 201 and indicatorOfParameter == 73:
            return 'dimensionless'

        if table2Version == 201 and indicatorOfParameter == 72:
            return 'dimensionless'

        if table2Version == 201 and indicatorOfParameter == 71:
            return 'dimensionless'

        if table2Version == 201 and indicatorOfParameter == 70:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 67:
            return 'm**-1'

        if table2Version == 201 and indicatorOfParameter == 66:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 65:
            return 'kg s**-1 m**-2'

        if table2Version == 201 and indicatorOfParameter == 64:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 63:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 62:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 61:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 60:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 56:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 55:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 54:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 53:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 52:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 51:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 50:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 42:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 41:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 38:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 37:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 36:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 35:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 34:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 33:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 32:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 31:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 30:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 29:
            return '(0 - 1)'

        if table2Version == 201 and indicatorOfParameter == 17:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 16:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 15:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 14:
            return 'K s**-1'

        if table2Version == 201 and indicatorOfParameter == 13:
            return 'K s**-1'

        if table2Version == 201 and indicatorOfParameter == 12:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 11:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 10:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 9:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 8:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 7:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 6:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 5:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 4:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 3:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 2:
            return 'J m**-2'

        if table2Version == 201 and indicatorOfParameter == 1:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 190 and indicatorOfParameter == 229:
            return 'm**3 m**-3'

        if table2Version == 190 and indicatorOfParameter == 173:
            return '(0 - 1)'

        if table2Version == 190 and indicatorOfParameter == 171:
            return '(0 - 1)'

        if table2Version == 190 and indicatorOfParameter == 170:
            return '(0 - 1)'

        if table2Version == 190 and indicatorOfParameter == 141:
            return 'kg m**-2'

        if table2Version == 180 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 180 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 180 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 180 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 180 and indicatorOfParameter == 149:
            return 'm'

        if table2Version == 175 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 175 and indicatorOfParameter == 236:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 183:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 175:
            return 'psu'

        if table2Version == 175 and indicatorOfParameter == 170:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 164:
            return 'degrees C'

        if table2Version == 175 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 111:
            return 'm'

        if table2Version == 175 and indicatorOfParameter == 110:
            return '(0 - 1)'

        if table2Version == 175 and indicatorOfParameter == 90:
            return 'J m**-2'

        if table2Version == 175 and indicatorOfParameter == 89:
            return 'J m**-2'

        if table2Version == 175 and indicatorOfParameter == 88:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 87:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 86:
            return 'm s**-1'

        if table2Version == 175 and indicatorOfParameter == 85:
            return 'm s**-1'

        if table2Version == 175 and indicatorOfParameter == 83:
            return 'kg C m**-2 s**-1'

        if table2Version == 175 and indicatorOfParameter == 55:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 175 and indicatorOfParameter == 42:
            return 'm**3 m**-3'

        if table2Version == 175 and indicatorOfParameter == 41:
            return 'm**3 m**-3'

        if table2Version == 175 and indicatorOfParameter == 40:
            return 'm**3 m**-3'

        if table2Version == 175 and indicatorOfParameter == 39:
            return 'm**3 m**-3'

        if table2Version == 175 and indicatorOfParameter == 34:
            return 'K'

        if table2Version == 175 and indicatorOfParameter == 31:
            return '(0 - 1)'

        if table2Version == 175 and indicatorOfParameter == 6:
            return 'm'

        if table2Version == 174 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 174 and indicatorOfParameter == 236:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 183:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 175:
            return 'psu'

        if table2Version == 174 and indicatorOfParameter == 170:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 164:
            return 'degrees C'

        if table2Version == 174 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 111:
            return 'm'

        if table2Version == 174 and indicatorOfParameter == 110:
            return '(0 - 1)'

        if table2Version == 174 and indicatorOfParameter == 99:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 98:
            return 'm'

        if table2Version == 174 and indicatorOfParameter == 95:
            return 'kg kg**-1'

        if table2Version == 174 and indicatorOfParameter == 94:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 90:
            return 'J m**-2'

        if table2Version == 174 and indicatorOfParameter == 89:
            return 'J m**-2'

        if table2Version == 174 and indicatorOfParameter == 88:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 87:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 86:
            return 'm s**-1'

        if table2Version == 174 and indicatorOfParameter == 85:
            return 'm s**-1'

        if table2Version == 174 and indicatorOfParameter == 83:
            return 'kg C m**-2 s**-1'

        if table2Version == 174 and indicatorOfParameter == 55:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 174 and indicatorOfParameter == 42:
            return 'm**3 m**-3'

        if table2Version == 174 and indicatorOfParameter == 41:
            return 'm**3 m**-3'

        if table2Version == 174 and indicatorOfParameter == 40:
            return 'm**3 m**-3'

        if table2Version == 174 and indicatorOfParameter == 39:
            return 'm**3 m**-3'

        if table2Version == 174 and indicatorOfParameter == 34:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 31:
            return '(0 - 1)'

        if table2Version == 174 and indicatorOfParameter == 9:
            return 'kg m**-2'

        if table2Version == 174 and indicatorOfParameter == 8:
            return 'kg m**-2'

        if table2Version == 174 and indicatorOfParameter == 6:
            return 'm'

        if table2Version == 173 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 173 and indicatorOfParameter == 240:
            return 'm of water equivalent s**-1'

        if table2Version == 173 and indicatorOfParameter == 239:
            return 'm of water equivalent s**-1'

        if table2Version == 173 and indicatorOfParameter == 228:
            return 'm s**-1'

        if table2Version == 173 and indicatorOfParameter == 212:
            return 'W m**-2 s**-1'

        if table2Version == 173 and indicatorOfParameter == 211:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 210:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 209:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 208:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 205:
            return 'm s**-1'

        if table2Version == 173 and indicatorOfParameter == 197:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 196:
            return 'N m**-2'

        if table2Version == 173 and indicatorOfParameter == 195:
            return 'N m**-2'

        if table2Version == 173 and indicatorOfParameter == 189:
            return 'dimensionless'

        if table2Version == 173 and indicatorOfParameter == 182:
            return 'm of water s**-1'

        if table2Version == 173 and indicatorOfParameter == 181:
            return 'N m**-2'

        if table2Version == 173 and indicatorOfParameter == 180:
            return 'N m**-2'

        if table2Version == 173 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 175:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 169:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 154:
            return 'K s**-1'

        if table2Version == 173 and indicatorOfParameter == 153:
            return 'K s**-1'

        if table2Version == 173 and indicatorOfParameter == 149:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 145:
            return 'J m**-2'

        if table2Version == 173 and indicatorOfParameter == 144:
            return 'm of water equivalent s**-1'

        if table2Version == 173 and indicatorOfParameter == 143:
            return 'm s**-1'

        if table2Version == 173 and indicatorOfParameter == 142:
            return 'm s**-1'

        if table2Version == 173 and indicatorOfParameter == 50:
            return '~'

        if table2Version == 173 and indicatorOfParameter == 48:
            return 'N m**-2'

        if table2Version == 173 and indicatorOfParameter == 45:
            return 'm of water s**-1'

        if table2Version == 173 and indicatorOfParameter == 44:
            return 'm of water s**-1'

        if table2Version == 172 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 172 and indicatorOfParameter == 240:
            return 'm of water equivalent s**-1'

        if table2Version == 172 and indicatorOfParameter == 239:
            return 'm of water equivalent s**-1'

        if table2Version == 172 and indicatorOfParameter == 228:
            return 'm s**-1'

        if table2Version == 172 and indicatorOfParameter == 212:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 211:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 210:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 209:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 208:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 205:
            return 'm s**-1'

        if table2Version == 172 and indicatorOfParameter == 197:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 196:
            return 'N m**-2'

        if table2Version == 172 and indicatorOfParameter == 195:
            return 'N m**-2'

        if table2Version == 172 and indicatorOfParameter == 189:
            return 's s**-1'

        if table2Version == 172 and indicatorOfParameter == 182:
            return 'm of water s**-1'

        if table2Version == 172 and indicatorOfParameter == 181:
            return 'N m**-2'

        if table2Version == 172 and indicatorOfParameter == 180:
            return 'N m**-2'

        if table2Version == 172 and indicatorOfParameter == 179:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 178:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 177:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 176:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 175:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 169:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 154:
            return 'K s**-1'

        if table2Version == 172 and indicatorOfParameter == 153:
            return 'K s**-1'

        if table2Version == 172 and indicatorOfParameter == 149:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 147:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 146:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 145:
            return 'W m**-2'

        if table2Version == 172 and indicatorOfParameter == 144:
            return 'm of water equivalent s**-1'

        if table2Version == 172 and indicatorOfParameter == 143:
            return 'm s**-1'

        if table2Version == 172 and indicatorOfParameter == 142:
            return 'm s**-1'

        if table2Version == 172 and indicatorOfParameter == 50:
            return '~'

        if table2Version == 172 and indicatorOfParameter == 48:
            return 'N m**-2'

        if table2Version == 172 and indicatorOfParameter == 45:
            return 'm of water s**-1'

        if table2Version == 172 and indicatorOfParameter == 44:
            return 'm of water s**-1'

        if table2Version == 171 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 254:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 253:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 252:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 251:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 250:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 249:
            return '(-1 to 1)'

        if table2Version == 171 and indicatorOfParameter == 248:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 247:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 246:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 245:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 244:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 243:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 242:
            return '(-1 to 1)'

        if table2Version == 171 and indicatorOfParameter == 241:
            return '(-1 to 1)'

        if table2Version == 171 and indicatorOfParameter == 240:
            return 'm of water equivalent'

        if table2Version == 171 and indicatorOfParameter == 239:
            return 'm of water equivalent'

        if table2Version == 171 and indicatorOfParameter == 238:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 237:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 236:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 235:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 234:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 233:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 232:
            return 'kg m**-2 s'

        if table2Version == 171 and indicatorOfParameter == 231:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 230:
            return 'N m**-2'

        if table2Version == 171 and indicatorOfParameter == 229:
            return 'N m**-2'

        if table2Version == 171 and indicatorOfParameter == 228:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 227:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 226:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 225:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 224:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 223:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 222:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 221:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 220:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 219:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 218:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 217:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 216:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 215:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 214:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 212:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 211:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 210:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 209:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 208:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 207:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 206:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 205:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 204:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 203:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 200:
            return 'm**2'

        if table2Version == 171 and indicatorOfParameter == 199:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 198:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 197:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 196:
            return 'N m**-2 s'

        if table2Version == 171 and indicatorOfParameter == 195:
            return 'N m**-2 s'

        if table2Version == 171 and indicatorOfParameter == 194:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 193:
            return 'm**2'

        if table2Version == 171 and indicatorOfParameter == 192:
            return 'm**2'

        if table2Version == 171 and indicatorOfParameter == 191:
            return 'm**2'

        if table2Version == 171 and indicatorOfParameter == 190:
            return 'm**2'

        if table2Version == 171 and indicatorOfParameter == 189:
            return 's'

        if table2Version == 171 and indicatorOfParameter == 188:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 187:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 186:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 185:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 184:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 183:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 182:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 181:
            return 'N m**-2 s'

        if table2Version == 171 and indicatorOfParameter == 180:
            return 'N m**-2 s'

        if table2Version == 171 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 175:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 174:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 173:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 171:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 170:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 169:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 166:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 165:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 164:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 163:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 162:
            return 'radians'

        if table2Version == 171 and indicatorOfParameter == 161:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 160:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 159:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 158:
            return 'Pa s**-1'

        if table2Version == 171 and indicatorOfParameter == 157:
            return '%'

        if table2Version == 171 and indicatorOfParameter == 156:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 155:
            return 's**-1'

        if table2Version == 171 and indicatorOfParameter == 154:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 153:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 152:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 151:
            return 'Pa'

        if table2Version == 171 and indicatorOfParameter == 150:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 149:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 148:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 145:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 144:
            return 'm of water equivalent'

        if table2Version == 171 and indicatorOfParameter == 143:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 142:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 141:
            return 'm of water equivalent'

        if table2Version == 171 and indicatorOfParameter == 140:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 138:
            return 's**-1'

        if table2Version == 171 and indicatorOfParameter == 137:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 136:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 135:
            return 'Pa s**-1'

        if table2Version == 171 and indicatorOfParameter == 134:
            return 'Pa'

        if table2Version == 171 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 171 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 130:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 171 and indicatorOfParameter == 128:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 126:
            return 'Various'

        if table2Version == 171 and indicatorOfParameter == 125:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 65:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 64:
            return 's'

        if table2Version == 171 and indicatorOfParameter == 63:
            return 's'

        if table2Version == 171 and indicatorOfParameter == 62:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 61:
            return 'Millimetres*100 + number of stations'

        if table2Version == 171 and indicatorOfParameter == 60:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 171 and indicatorOfParameter == 59:
            return 'J kg**-1'

        if table2Version == 171 and indicatorOfParameter == 58:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 57:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 56:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 55:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 54:
            return 'Pa'

        if table2Version == 171 and indicatorOfParameter == 53:
            return 'm**2 s**-2'

        if table2Version == 171 and indicatorOfParameter == 52:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 51:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 50:
            return 's'

        if table2Version == 171 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 48:
            return 'N m**-2 s'

        if table2Version == 171 and indicatorOfParameter == 47:
            return 'J m**-2'

        if table2Version == 171 and indicatorOfParameter == 46:
            return 's'

        if table2Version == 171 and indicatorOfParameter == 45:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 44:
            return 'kg m**-2'

        if table2Version == 171 and indicatorOfParameter == 43:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 42:
            return 'm**3 m**-3'

        if table2Version == 171 and indicatorOfParameter == 41:
            return 'm**3 m**-3'

        if table2Version == 171 and indicatorOfParameter == 40:
            return 'm**3 m**-3'

        if table2Version == 171 and indicatorOfParameter == 39:
            return 'm**3 m**-3'

        if table2Version == 171 and indicatorOfParameter == 38:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 37:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 36:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 35:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 34:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 33:
            return 'kg m**-3'

        if table2Version == 171 and indicatorOfParameter == 32:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 31:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 28:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 27:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 26:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 23:
            return 's**-1'

        if table2Version == 171 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 171 and indicatorOfParameter == 21:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 14:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 13:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 12:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 11:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 5:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 4:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 3:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 2:
            return 'm**2 s**-1'

        if table2Version == 171 and indicatorOfParameter == 1:
            return 'm**2 s**-1'

        if table2Version == 170 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 170 and indicatorOfParameter == 171:
            return 'm'

        if table2Version == 170 and indicatorOfParameter == 149:
            return 'm'

        if table2Version == 162 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 162 and indicatorOfParameter == 233:
            return 'dimensionless'

        if table2Version == 162 and indicatorOfParameter == 232:
            return 'Pa s**-1'

        if table2Version == 162 and indicatorOfParameter == 231:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 230:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 229:
            return 'dimensionless'

        if table2Version == 162 and indicatorOfParameter == 227:
            return 'Pa**2'

        if table2Version == 162 and indicatorOfParameter == 226:
            return 'Pa**2 s**-2'

        if table2Version == 162 and indicatorOfParameter == 225:
            return 'm Pa s**-2'

        if table2Version == 162 and indicatorOfParameter == 224:
            return 'm Pa s**-2'

        if table2Version == 162 and indicatorOfParameter == 223:
            return 'Pa s**-1'

        if table2Version == 162 and indicatorOfParameter == 222:
            return 'Pa s**-1 K'

        if table2Version == 162 and indicatorOfParameter == 221:
            return 'm**2 Pa s**-3'

        if table2Version == 162 and indicatorOfParameter == 220:
            return 'm**2 s**-2'

        if table2Version == 162 and indicatorOfParameter == 219:
            return 'm**2 s**-2'

        if table2Version == 162 and indicatorOfParameter == 218:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 217:
            return 'm s**-1 K'

        if table2Version == 162 and indicatorOfParameter == 216:
            return 'm**3 s**-3'

        if table2Version == 162 and indicatorOfParameter == 215:
            return 'm**2 s**-2'

        if table2Version == 162 and indicatorOfParameter == 214:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 213:
            return 'm s**-1 K'

        if table2Version == 162 and indicatorOfParameter == 212:
            return 'm**3 s**-3'

        if table2Version == 162 and indicatorOfParameter == 211:
            return '~'

        if table2Version == 162 and indicatorOfParameter == 210:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 209:
            return 'm**2 s**-2'

        if table2Version == 162 and indicatorOfParameter == 208:
            return 'K**2'

        if table2Version == 162 and indicatorOfParameter == 207:
            return 'm**2 K s**-2'

        if table2Version == 162 and indicatorOfParameter == 206:
            return 'm**4 s**-4'

        if table2Version == 162 and indicatorOfParameter == 113:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 112:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 111:
            return 'kg kg**-1'

        if table2Version == 162 and indicatorOfParameter == 110:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 109:
            return 'm**2'

        if table2Version == 162 and indicatorOfParameter == 108:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 107:
            return 'kg m**-3'

        if table2Version == 162 and indicatorOfParameter == 106:
            return 'kg m**-3'

        if table2Version == 162 and indicatorOfParameter == 105:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 104:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 103:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 102:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 101:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 100:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 87:
            return 'kg m**-2 s**-1'

        if table2Version == 162 and indicatorOfParameter == 86:
            return 'W m**-2'

        if table2Version == 162 and indicatorOfParameter == 85:
            return 'W m**-2'

        if table2Version == 162 and indicatorOfParameter == 84:
            return 'kg m**-2 s**-1'

        if table2Version == 162 and indicatorOfParameter == 83:
            return 'W m**-2'

        if table2Version == 162 and indicatorOfParameter == 82:
            return 'W m**-2'

        if table2Version == 162 and indicatorOfParameter == 81:
            return 'kg m**-2 s**-1'

        if table2Version == 162 and indicatorOfParameter == 78:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 77:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 76:
            return 'W m**-1'

        if table2Version == 162 and indicatorOfParameter == 75:
            return 'W m**-1'

        if table2Version == 162 and indicatorOfParameter == 74:
            return 'W m**-1'

        if table2Version == 162 and indicatorOfParameter == 73:
            return 'W m**-1'

        if table2Version == 162 and indicatorOfParameter == 72:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 71:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 70:
            return 'W m**-1'

        if table2Version == 162 and indicatorOfParameter == 69:
            return 'W m**-1'

        if table2Version == 162 and indicatorOfParameter == 68:
            return 'W m**-1'

        if table2Version == 162 and indicatorOfParameter == 67:
            return 'W m**-1'

        if table2Version == 162 and indicatorOfParameter == 66:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 65:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 64:
            return 'W m**-2'

        if table2Version == 162 and indicatorOfParameter == 63:
            return 'J m**-2'

        if table2Version == 162 and indicatorOfParameter == 62:
            return 'J m**-2'

        if table2Version == 162 and indicatorOfParameter == 61:
            return 'J m**-2'

        if table2Version == 162 and indicatorOfParameter == 60:
            return 'J m**-2'

        if table2Version == 162 and indicatorOfParameter == 59:
            return 'J m**-2'

        if table2Version == 162 and indicatorOfParameter == 58:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 57:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 56:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 55:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 54:
            return 'K kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 53:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 51:
            return 'm**2 s**-2'

        if table2Version == 160 and indicatorOfParameter == 254:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 249:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 247:
            return 'N m**-2'

        if table2Version == 160 and indicatorOfParameter == 246:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 243:
            return '~'

        if table2Version == 160 and indicatorOfParameter == 242:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 241:
            return 'kg kg**-1'

        if table2Version == 160 and indicatorOfParameter == 240:
            return 'kg m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 239:
            return 'kg m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 231:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 226:
            return 'Pa s**-1'

        if table2Version == 160 and indicatorOfParameter == 225:
            return 'Pa m s**-2'

        if table2Version == 160 and indicatorOfParameter == 224:
            return 'Pa m s**-2'

        if table2Version == 160 and indicatorOfParameter == 223:
            return 'Pa s**-1'

        if table2Version == 160 and indicatorOfParameter == 222:
            return 'K Pa s**-1'

        if table2Version == 160 and indicatorOfParameter == 221:
            return 'Pa m**2 s**-3'

        if table2Version == 160 and indicatorOfParameter == 220:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 219:
            return 'm**2 s**-2'

        if table2Version == 160 and indicatorOfParameter == 218:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 217:
            return 'K m s**-1'

        if table2Version == 160 and indicatorOfParameter == 216:
            return 'm**3 s**-3'

        if table2Version == 160 and indicatorOfParameter == 215:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 214:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 213:
            return 'K m s**-1'

        if table2Version == 160 and indicatorOfParameter == 212:
            return 'm**3 s**-3'

        if table2Version == 160 and indicatorOfParameter == 211:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 210:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 209:
            return 'm**2 s**-2'

        if table2Version == 160 and indicatorOfParameter == 208:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 207:
            return 'K m**2 s**-2'

        if table2Version == 160 and indicatorOfParameter == 206:
            return 'm**2 s**-2'

        if table2Version == 160 and indicatorOfParameter == 205:
            return 'kg m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 199:
            return '%'

        if table2Version == 160 and indicatorOfParameter == 198:
            return 'kg m**-2'

        if table2Version == 160 and indicatorOfParameter == 184:
            return 'm'

        if table2Version == 160 and indicatorOfParameter == 182:
            return 'kg m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 181:
            return 'N m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 180:
            return 'N m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 171:
            return 'm'

        if table2Version == 160 and indicatorOfParameter == 157:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 156:
            return 'm'

        if table2Version == 160 and indicatorOfParameter == 144:
            return 'kg m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 143:
            return 'kg m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 142:
            return 'kg m**-2 s**-1'

        if table2Version == 160 and indicatorOfParameter == 141:
            return 'kg m**-2'

        if table2Version == 160 and indicatorOfParameter == 140:
            return 'm'

        if table2Version == 160 and indicatorOfParameter == 137:
            return 'kg m**-2'

        if table2Version == 160 and indicatorOfParameter == 135:
            return 'Pa s**-1'

        if table2Version == 160 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 151 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 151 and indicatorOfParameter == 212:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 211:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 210:
            return 'Pa'

        if table2Version == 151 and indicatorOfParameter == 209:
            return 'Pa'

        if table2Version == 151 and indicatorOfParameter == 208:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 207:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 206:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 205:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 204:
            return 'Pa m**-1'

        if table2Version == 151 and indicatorOfParameter == 203:
            return 'Pa m**-1'

        if table2Version == 151 and indicatorOfParameter == 202:
            return '~'

        if table2Version == 151 and indicatorOfParameter == 201:
            return 'deg C per time step'

        if table2Version == 151 and indicatorOfParameter == 200:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 199:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 194:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 192:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 191:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 190:
            return 'psu per time step'

        if table2Version == 151 and indicatorOfParameter == 188:
            return '~'

        if table2Version == 151 and indicatorOfParameter == 187:
            return 'm s**-1 per time step'

        if table2Version == 151 and indicatorOfParameter == 186:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 185:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 184:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 183:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 182:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 181:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 180:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 179:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 178:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 177:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 176:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 175:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 174:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 173:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 172:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 171:
            return 'm s**-1'

        if table2Version == 151 and indicatorOfParameter == 170:
            return 'J m**-1 s**-1'

        if table2Version == 151 and indicatorOfParameter == 169:
            return 'J m**-1 s**-1'

        if table2Version == 151 and indicatorOfParameter == 168:
            return 'm**2 s**-1'

        if table2Version == 151 and indicatorOfParameter == 167:
            return 'm**2 s**-1'

        if table2Version == 151 and indicatorOfParameter == 166:
            return 'm**2 s**-1'

        if table2Version == 151 and indicatorOfParameter == 165:
            return 'm**2 s**-1'

        if table2Version == 151 and indicatorOfParameter == 164:
            return 'degrees C'

        if table2Version == 151 and indicatorOfParameter == 163:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 162:
            return 'J m**-2'

        if table2Version == 151 and indicatorOfParameter == 161:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 160:
            return 'J m**-2'

        if table2Version == 151 and indicatorOfParameter == 159:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 158:
            return 'm s**-1'

        if table2Version == 151 and indicatorOfParameter == 157:
            return 'J m**-2'

        if table2Version == 151 and indicatorOfParameter == 156:
            return 'J m**-2'

        if table2Version == 151 and indicatorOfParameter == 155:
            return 'J m**-2'

        if table2Version == 151 and indicatorOfParameter == 154:
            return 'N m**-2'

        if table2Version == 151 and indicatorOfParameter == 153:
            return 'N m**-2'

        if table2Version == 151 and indicatorOfParameter == 152:
            return 'Nm**-3'

        if table2Version == 151 and indicatorOfParameter == 151:
            return 'N m**-3'

        if table2Version == 151 and indicatorOfParameter == 150:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 149:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 148:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 147:
            return 'm**3 s**-1'

        if table2Version == 151 and indicatorOfParameter == 146:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 145:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 144:
            return 'm**2 s**-2'

        if table2Version == 151 and indicatorOfParameter == 143:
            return 'm**2 s**-2'

        if table2Version == 151 and indicatorOfParameter == 142:
            return 'm s**-1 deg C'

        if table2Version == 151 and indicatorOfParameter == 141:
            return 'm s**-1 degC'

        if table2Version == 151 and indicatorOfParameter == 140:
            return 'm**2 s**-2'

        if table2Version == 151 and indicatorOfParameter == 139:
            return '~'

        if table2Version == 151 and indicatorOfParameter == 138:
            return 'kg m**-3'

        if table2Version == 151 and indicatorOfParameter == 137:
            return 'm'

        if table2Version == 151 and indicatorOfParameter == 136:
            return 'm**2 s**-1'

        if table2Version == 151 and indicatorOfParameter == 135:
            return 'm**2 s**-1'

        if table2Version == 151 and indicatorOfParameter == 134:
            return 's**-1'

        if table2Version == 151 and indicatorOfParameter == 133:
            return 'm s**-1'

        if table2Version == 151 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 151 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 151 and indicatorOfParameter == 130:
            return 'psu'

        if table2Version == 151 and indicatorOfParameter == 129:
            return 'deg C'

        if table2Version == 151 and indicatorOfParameter == 128:
            return 'deg C'

        if table2Version == 150 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 150 and indicatorOfParameter == 183:
            return 'J m**-2'

        if table2Version == 150 and indicatorOfParameter == 182:
            return 'deg C'

        if table2Version == 150 and indicatorOfParameter == 181:
            return 'J m**-2'

        if table2Version == 150 and indicatorOfParameter == 180:
            return 'deg C'

        if table2Version == 150 and indicatorOfParameter == 173:
            return '~'

        if table2Version == 150 and indicatorOfParameter == 172:
            return '~'

        if table2Version == 150 and indicatorOfParameter == 171:
            return '~'

        if table2Version == 150 and indicatorOfParameter == 170:
            return '~'

        if table2Version == 150 and indicatorOfParameter == 169:
            return 'Pa'

        if table2Version == 150 and indicatorOfParameter == 168:
            return 'Pa'

        if table2Version == 150 and indicatorOfParameter == 155:
            return 'm'

        if table2Version == 150 and indicatorOfParameter == 154:
            return 'm'

        if table2Version == 150 and indicatorOfParameter == 153:
            return '~'

        if table2Version == 150 and indicatorOfParameter == 152:
            return 'm'

        if table2Version == 150 and indicatorOfParameter == 148:
            return 'm s**-2'

        if table2Version == 150 and indicatorOfParameter == 147:
            return 'm s**-2'

        if table2Version == 150 and indicatorOfParameter == 146:
            return 'm s**-1 deg C'

        if table2Version == 150 and indicatorOfParameter == 145:
            return 'm s**-1 deg C'

        if table2Version == 150 and indicatorOfParameter == 144:
            return 'm s**-2'

        if table2Version == 150 and indicatorOfParameter == 143:
            return 'm s**-2'

        if table2Version == 150 and indicatorOfParameter == 142:
            return 'm s**-2'

        if table2Version == 150 and indicatorOfParameter == 141:
            return 'm s**-1 deg C'

        if table2Version == 150 and indicatorOfParameter == 140:
            return 'm s**-1 deg C'

        if table2Version == 150 and indicatorOfParameter == 139:
            return 'm s**-2'

        if table2Version == 150 and indicatorOfParameter == 137:
            return '~'

        if table2Version == 150 and indicatorOfParameter == 135:
            return 'm s**-1'

        if table2Version == 150 and indicatorOfParameter == 134:
            return 'm s**-1'

        if table2Version == 150 and indicatorOfParameter == 133:
            return 'm s**-1'

        if table2Version == 150 and indicatorOfParameter == 131:
            return 'kg m**-3 -1000'

        if table2Version == 150 and indicatorOfParameter == 130:
            return 'psu'

        if table2Version == 150 and indicatorOfParameter == 129:
            return 'deg C'

        if table2Version == 140 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 254:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 253:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 252:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 251:
            return 'm**2 s radian**-1'

        if table2Version == 140 and indicatorOfParameter == 250:
            return 'm**2 s radian**-1'

        if table2Version == 140 and indicatorOfParameter == 249:
            return 'degrees'

        if table2Version == 140 and indicatorOfParameter == 248:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 247:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 246:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 245:
            return 'm s**-1'

        if table2Version == 140 and indicatorOfParameter == 244:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 243:
            return 'm s**-1'

        if table2Version == 140 and indicatorOfParameter == 242:
            return 'degrees'

        if table2Version == 140 and indicatorOfParameter == 241:
            return 'm s**-1'

        if table2Version == 140 and indicatorOfParameter == 240:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 239:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 238:
            return 'degrees'

        if table2Version == 140 and indicatorOfParameter == 237:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 236:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 235:
            return 'degrees'

        if table2Version == 140 and indicatorOfParameter == 234:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 233:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 232:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 231:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 230:
            return 'Degree true'

        if table2Version == 140 and indicatorOfParameter == 229:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 228:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 227:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 226:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 225:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 224:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 223:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 222:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 221:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 220:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 219:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 218:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 217:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 200:
            return 'm'

        if table2Version == 133 and indicatorOfParameter == 92:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 91:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 90:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 89:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 88:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 86:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 85:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 83:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 82:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 81:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 80:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 79:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 78:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 77:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 76:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 75:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 74:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 73:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 70:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 69:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 68:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 67:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 66:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 65:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 64:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 63:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 62:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 61:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 59:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 58:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 57:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 56:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 55:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 54:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 53:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 51:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 50:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 49:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 48:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 47:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 46:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 45:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 44:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 43:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 42:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 41:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 40:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 39:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 38:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 37:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 36:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 35:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 34:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 33:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 32:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 31:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 30:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 29:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 28:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 27:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 26:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 25:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 24:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 23:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 22:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 21:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 20:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 19:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 18:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 17:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 16:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 15:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 14:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 13:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 12:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 11:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 10:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 9:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 8:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 7:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 6:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 5:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 4:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 3:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 2:
            return '%'

        if table2Version == 133 and indicatorOfParameter == 1:
            return '%'

        if table2Version == 132 and indicatorOfParameter == 228:
            return '(-1 to 1)'

        if table2Version == 132 and indicatorOfParameter == 202:
            return '(-1 to 1)'

        if table2Version == 132 and indicatorOfParameter == 201:
            return '(-1 to 1)'

        if table2Version == 132 and indicatorOfParameter == 167:
            return '(-1 to 1)'

        if table2Version == 132 and indicatorOfParameter == 165:
            return '(-1 to 1)'

        if table2Version == 132 and indicatorOfParameter == 144:
            return '(-1 to 1)'

        if table2Version == 132 and indicatorOfParameter == 49:
            return '(-1 to 1)'

        if table2Version == 131 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 131 and indicatorOfParameter == 232:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 229:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 228:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 202:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 201:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 167:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 165:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 164:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 151:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 144:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 139:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 130:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 129:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 81:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 80:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 79:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 78:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 77:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 76:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 75:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 74:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 73:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 70:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 69:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 68:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 67:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 66:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 65:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 64:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 59:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 49:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 25:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 24:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 23:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 22:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 21:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 20:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 18:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 17:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 16:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 15:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 10:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 9:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 8:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 7:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 6:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 5:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 4:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 3:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 2:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 1:
            return '%'

        if table2Version == 130 and indicatorOfParameter == 232:
            return 'Pa s**-1'

        if table2Version == 130 and indicatorOfParameter == 231:
            return 'm**2 s**-3'

        if table2Version == 130 and indicatorOfParameter == 230:
            return 'm**2 s**-3'

        if table2Version == 130 and indicatorOfParameter == 229:
            return 'kg kg**-1 s**-1'

        if table2Version == 130 and indicatorOfParameter == 228:
            return 'K s**-1'

        if table2Version == 130 and indicatorOfParameter == 226:
            return 'kg kg**-1 s**-1'

        if table2Version == 130 and indicatorOfParameter == 225:
            return 'kg kg**-1 s**-1'

        if table2Version == 130 and indicatorOfParameter == 224:
            return 'kg kg**-1 s**-1'

        if table2Version == 130 and indicatorOfParameter == 221:
            return 'm**2 s**-3'

        if table2Version == 130 and indicatorOfParameter == 220:
            return 'm**2 s**-3'

        if table2Version == 130 and indicatorOfParameter == 219:
            return 'm**2 s**-3'

        if table2Version == 130 and indicatorOfParameter == 218:
            return 'm**2 s**-3'

        if table2Version == 130 and indicatorOfParameter == 217:
            return 'K s**-1'

        if table2Version == 130 and indicatorOfParameter == 216:
            return 'K s**-1'

        if table2Version == 130 and indicatorOfParameter == 215:
            return 'K s**-1'

        if table2Version == 130 and indicatorOfParameter == 214:
            return 'K s**-1'

        if table2Version == 130 and indicatorOfParameter == 213:
            return '(0 - 1)'

        if table2Version == 130 and indicatorOfParameter == 212:
            return 'kg kg**-1'

        if table2Version == 130 and indicatorOfParameter == 211:
            return 'J m**-2'

        if table2Version == 130 and indicatorOfParameter == 210:
            return 'J m**-2'

        if table2Version == 130 and indicatorOfParameter == 209:
            return 'J m**-2'

        if table2Version == 130 and indicatorOfParameter == 208:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 254:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 253:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 252:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 251:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 250:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 249:
            return '(-1 to 1)'

        if table2Version == 129 and indicatorOfParameter == 248:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 247:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 246:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 245:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 244:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 243:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 242:
            return '(-1 to 1)'

        if table2Version == 129 and indicatorOfParameter == 241:
            return '(-1 to 1)'

        if table2Version == 129 and indicatorOfParameter == 240:
            return 'm of water equivalent'

        if table2Version == 129 and indicatorOfParameter == 239:
            return 'm of water equivalent'

        if table2Version == 129 and indicatorOfParameter == 238:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 237:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 236:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 235:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 234:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 233:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 232:
            return 'kg m**-2 s'

        if table2Version == 129 and indicatorOfParameter == 231:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 230:
            return 'N m**-2'

        if table2Version == 129 and indicatorOfParameter == 229:
            return 'N m**-2'

        if table2Version == 129 and indicatorOfParameter == 228:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 227:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 226:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 225:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 224:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 223:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 222:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 221:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 220:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 219:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 218:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 217:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 216:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 215:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 214:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 212:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 211:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 210:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 209:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 208:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 207:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 206:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 205:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 204:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 203:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 200:
            return 'm**2'

        if table2Version == 129 and indicatorOfParameter == 199:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 198:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 197:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 196:
            return 'N m**-2 s'

        if table2Version == 129 and indicatorOfParameter == 195:
            return 'N m**-2 s'

        if table2Version == 129 and indicatorOfParameter == 194:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 193:
            return 'm**2'

        if table2Version == 129 and indicatorOfParameter == 192:
            return 'm**2'

        if table2Version == 129 and indicatorOfParameter == 191:
            return 'm**2'

        if table2Version == 129 and indicatorOfParameter == 190:
            return 'm**2'

        if table2Version == 129 and indicatorOfParameter == 189:
            return 's'

        if table2Version == 129 and indicatorOfParameter == 188:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 187:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 186:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 185:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 184:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 183:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 182:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 181:
            return 'N m**-2 s'

        if table2Version == 129 and indicatorOfParameter == 180:
            return 'N m**-2 s'

        if table2Version == 129 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 175:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 174:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 173:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 171:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 170:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 169:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 166:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 165:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 164:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 163:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 162:
            return 'radians'

        if table2Version == 129 and indicatorOfParameter == 161:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 160:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 159:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 158:
            return 'Pa s**-1'

        if table2Version == 129 and indicatorOfParameter == 157:
            return '%'

        if table2Version == 129 and indicatorOfParameter == 156:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 155:
            return 's**-1'

        if table2Version == 129 and indicatorOfParameter == 154:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 153:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 152:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 151:
            return 'Pa'

        if table2Version == 129 and indicatorOfParameter == 150:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 149:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 148:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 145:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 144:
            return 'm of water equivalent'

        if table2Version == 129 and indicatorOfParameter == 143:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 142:
            return 'm'

        if table2Version == 129 and indicatorOfParameter == 141:
            return 'm of water equivalent'

        if table2Version == 129 and indicatorOfParameter == 140:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 138:
            return 's**-1'

        if table2Version == 129 and indicatorOfParameter == 137:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 136:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 135:
            return 'Pa s**-1'

        if table2Version == 129 and indicatorOfParameter == 134:
            return 'Pa'

        if table2Version == 129 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 129 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 130:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 129 and indicatorOfParameter == 128:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 126:
            return 'Various'

        if table2Version == 129 and indicatorOfParameter == 125:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 123:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 122:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 121:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 120:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 119:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 118:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 117:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 116:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 115:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 114:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 113:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 112:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 111:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 110:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 109:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 108:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 107:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 106:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 105:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 104:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 103:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 102:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 101:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 100:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 99:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 98:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 97:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 96:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 95:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 94:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 93:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 92:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 91:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 90:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 89:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 88:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 87:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 86:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 85:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 84:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 83:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 82:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 81:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 80:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 71:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 70:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 69:
            return 's m**-1'

        if table2Version == 129 and indicatorOfParameter == 68:
            return 's m**-1'

        if table2Version == 129 and indicatorOfParameter == 67:
            return 'm**2 m**-2'

        if table2Version == 129 and indicatorOfParameter == 66:
            return 'm**2 m**-2'

        if table2Version == 129 and indicatorOfParameter == 65:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 64:
            return 's'

        if table2Version == 129 and indicatorOfParameter == 63:
            return 's'

        if table2Version == 129 and indicatorOfParameter == 62:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 61:
            return 'Millimetres*100 + number of stations'

        if table2Version == 129 and indicatorOfParameter == 60:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 129 and indicatorOfParameter == 59:
            return 'J kg**-1'

        if table2Version == 129 and indicatorOfParameter == 58:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 57:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 56:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 55:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 54:
            return 'Pa'

        if table2Version == 129 and indicatorOfParameter == 53:
            return 'm**2 s**-2'

        if table2Version == 129 and indicatorOfParameter == 52:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 51:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 50:
            return 's'

        if table2Version == 129 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 48:
            return 'N m**-2 s'

        if table2Version == 129 and indicatorOfParameter == 47:
            return 'J m**-2'

        if table2Version == 129 and indicatorOfParameter == 46:
            return 's'

        if table2Version == 129 and indicatorOfParameter == 45:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 44:
            return 'kg m**-2'

        if table2Version == 129 and indicatorOfParameter == 43:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 42:
            return 'm**3 m**-3'

        if table2Version == 129 and indicatorOfParameter == 41:
            return 'm**3 m**-3'

        if table2Version == 129 and indicatorOfParameter == 40:
            return 'm**3 m**-3'

        if table2Version == 129 and indicatorOfParameter == 39:
            return 'm**3 m**-3'

        if table2Version == 129 and indicatorOfParameter == 38:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 37:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 36:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 35:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 34:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 33:
            return 'kg m**-3'

        if table2Version == 129 and indicatorOfParameter == 32:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 31:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 28:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 27:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 26:
            return '(0 - 1)'

        if table2Version == 129 and indicatorOfParameter == 25:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 24:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 23:
            return 's**-1'

        if table2Version == 129 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 129 and indicatorOfParameter == 21:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 14:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 13:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 12:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 11:
            return 'm s**-1'

        if table2Version == 129 and indicatorOfParameter == 5:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 4:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 3:
            return 'K'

        if table2Version == 129 and indicatorOfParameter == 2:
            return 'm**2 s**-1'

        if table2Version == 129 and indicatorOfParameter == 1:
            return 'm**2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 123:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 121:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 109:
            return 'm'

        if table2Version == 254 and indicatorOfParameter == 48:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 70:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 69:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 68:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 67:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 66:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 65:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 64:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 63:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 62:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 61:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 60:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 59:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 58:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 57:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 56:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 55:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 54:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 53:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 52:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 51:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 50:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 49:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 48:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 47:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 46:
            return 'N m**-2'

        if table2Version == 235 and indicatorOfParameter == 45:
            return 'N m**-2'

        if table2Version == 235 and indicatorOfParameter == 44:
            return 'Proportion'

        if table2Version == 235 and indicatorOfParameter == 43:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 42:
            return 'N m**-2'

        if table2Version == 235 and indicatorOfParameter == 41:
            return 'N m**-2'

        if table2Version == 235 and indicatorOfParameter == 40:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 39:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 38:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 37:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 36:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 35:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 34:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 33:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 32:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 31:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 30:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 29:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 28:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 27:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 26:
            return 'Proportion'

        if table2Version == 235 and indicatorOfParameter == 25:
            return 'N m**-2'

        if table2Version == 235 and indicatorOfParameter == 24:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 23:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 22:
            return 'W m**-2'

        if table2Version == 235 and indicatorOfParameter == 21:
            return 'kg m**-2 s**-1'

        if table2Version == 235 and indicatorOfParameter == 20:
            return 'kg m**-2 s**-1'

        if table2Version == 230 and indicatorOfParameter == 251:
            return 'm'

        if table2Version == 230 and indicatorOfParameter == 240:
            return 'm of water equivalent'

        if table2Version == 230 and indicatorOfParameter == 239:
            return 'm of water equivalent'

        if table2Version == 230 and indicatorOfParameter == 228:
            return 'm'

        if table2Version == 230 and indicatorOfParameter == 216:
            return 'm'

        if table2Version == 230 and indicatorOfParameter == 213:
            return 'kg m**-2'

        if table2Version == 230 and indicatorOfParameter == 174:
            return '(0 - 1)'

        if table2Version == 230 and indicatorOfParameter == 130:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 129:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 82:
            return 'kg m**-2'

        if table2Version == 230 and indicatorOfParameter == 81:
            return 'kg m**-2'

        if table2Version == 230 and indicatorOfParameter == 80:
            return 'kg m**-2'

        if table2Version == 230 and indicatorOfParameter == 50:
            return 's'

        if table2Version == 230 and indicatorOfParameter == 47:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 22:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 21:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 20:
            return 'J m**-2'

        if table2Version == 230 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 230 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 252:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 251:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 250:
            return 'Proportion'

        if table2Version == 228 and indicatorOfParameter == 249:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 245:
            return '(0 - 1)'

        if table2Version == 228 and indicatorOfParameter == 244:
            return '(0 - 1)'

        if table2Version == 228 and indicatorOfParameter == 243:
            return 'J m**-2'

        if table2Version == 228 and indicatorOfParameter == 242:
            return 'J m**-2'

        if table2Version == 228 and indicatorOfParameter == 241:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 240:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 239:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 230:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 229:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 227:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 226:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 225:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 224:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 223:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 222:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 221:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 220:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 219:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 218:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 217:
            return '(0 - 1)'

        if table2Version == 228 and indicatorOfParameter == 216:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 130:
            return 'J m**-2'

        if table2Version == 228 and indicatorOfParameter == 129:
            return 'J m**-2'

        if table2Version == 228 and indicatorOfParameter == 94:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 93:
            return 'm**3 m**-3'

        if table2Version == 228 and indicatorOfParameter == 92:
            return '(0 - 1)'

        if table2Version == 228 and indicatorOfParameter == 91:
            return '(0 - 1)'

        if table2Version == 228 and indicatorOfParameter == 90:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 89:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 88:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 85:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 84:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 83:
            return 'kg m**-2 s**-1'

        if table2Version == 228 and indicatorOfParameter == 82:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 81:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 80:
            return 'kg m**-2'

        if table2Version == 228 and indicatorOfParameter == 79:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 78:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 74:
            return 'hour'

        if table2Version == 228 and indicatorOfParameter == 73:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 228 and indicatorOfParameter == 71:
            return 'm**3 m**-3'

        if table2Version == 228 and indicatorOfParameter == 70:
            return 'm**3 m**-3'

        if table2Version == 228 and indicatorOfParameter == 53:
            return 'km**-2 day**-1'

        if table2Version == 228 and indicatorOfParameter == 52:
            return 'km**-2 day**-1'

        if table2Version == 228 and indicatorOfParameter == 51:
            return 'km**-2 day**-1'

        if table2Version == 228 and indicatorOfParameter == 50:
            return 'km**-2 day**-1'

        if table2Version == 228 and indicatorOfParameter == 48:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 47:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 46:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 44:
            return 'm**2 s**-2'

        if table2Version == 228 and indicatorOfParameter == 43:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 42:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 41:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 40:
            return 'dimensionless'

        if table2Version == 228 and indicatorOfParameter == 37:
            return '%'

        if table2Version == 228 and indicatorOfParameter == 29:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 28:
            return 'm s**-1'

        if table2Version == 228 and indicatorOfParameter == 27:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 26:
            return 'K'

        if table2Version == 228 and indicatorOfParameter == 25:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 24:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 23:
            return 'm'

        if table2Version == 228 and indicatorOfParameter == 22:
            return 'J m**-2'

        if table2Version == 228 and indicatorOfParameter == 21:
            return 'J m**-2'

        if table2Version == 228 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 221 and indicatorOfParameter == 56:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 55:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 54:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 53:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 52:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 51:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 50:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 48:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 47:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 46:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 45:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 44:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 43:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 42:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 41:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 40:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 39:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 38:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 37:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 36:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 35:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 34:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 33:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 32:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 31:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 30:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 29:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 28:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 27:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 26:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 25:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 24:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 23:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 22:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 21:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 20:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 19:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 18:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 17:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 16:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 15:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 14:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 13:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 12:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 11:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 10:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 9:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 8:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 7:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 6:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 5:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 4:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 3:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 2:
            return 'm s**-1'

        if table2Version == 221 and indicatorOfParameter == 1:
            return 'm s**-1'

        if table2Version == 219 and indicatorOfParameter == 56:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 55:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 54:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 53:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 52:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 51:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 50:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 49:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 48:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 47:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 46:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 45:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 44:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 43:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 42:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 41:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 40:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 39:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 38:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 37:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 36:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 35:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 34:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 33:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 32:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 31:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 30:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 29:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 28:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 27:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 26:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 25:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 24:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 23:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 22:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 21:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 20:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 19:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 18:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 17:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 16:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 15:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 14:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 13:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 12:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 11:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 10:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 9:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 8:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 7:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 6:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 5:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 3:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 2:
            return 'kg m**-2 s**-1'

        if table2Version == 219 and indicatorOfParameter == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 218 and indicatorOfParameter == 56:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 55:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 54:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 53:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 52:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 51:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 50:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 49:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 48:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 47:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 46:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 45:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 44:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 43:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 42:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 41:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 40:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 39:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 38:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 37:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 36:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 35:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 34:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 33:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 32:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 30:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 29:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 28:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 27:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 26:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 24:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 23:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 22:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 21:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 20:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 19:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 18:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 16:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 15:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 14:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 13:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 12:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 11:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 10:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 9:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 7:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 6:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 4:
            return 'kg m**-2'

        if table2Version == 218 and indicatorOfParameter == 3:
            return 'kg m**-2'

        if table2Version == 217 and indicatorOfParameter == 56:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 55:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 54:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 53:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 52:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 51:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 50:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 49:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 48:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 47:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 46:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 45:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 44:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 43:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 42:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 41:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 40:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 39:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 38:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 37:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 36:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 35:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 34:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 33:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 32:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 30:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 29:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 28:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 27:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 26:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 24:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 23:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 22:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 21:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 20:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 19:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 18:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 16:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 15:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 14:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 13:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 12:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 11:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 10:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 9:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 7:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 6:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 4:
            return 'kg kg**-1'

        if table2Version == 217 and indicatorOfParameter == 3:
            return 'kg kg**-1'

        if table2Version == 216 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 254:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 253:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 252:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 251:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 250:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 249:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 248:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 247:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 246:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 245:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 244:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 243:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 242:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 241:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 240:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 239:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 238:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 237:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 236:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 235:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 234:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 233:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 232:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 231:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 230:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 229:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 228:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 227:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 226:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 225:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 224:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 223:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 222:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 221:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 220:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 219:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 218:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 217:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 216:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 215:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 214:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 213:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 212:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 211:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 210:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 209:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 208:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 207:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 206:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 205:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 204:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 203:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 202:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 201:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 200:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 199:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 198:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 197:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 196:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 195:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 194:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 193:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 192:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 191:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 190:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 189:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 188:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 187:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 186:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 185:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 184:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 183:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 182:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 181:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 180:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 179:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 178:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 177:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 176:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 175:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 174:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 173:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 172:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 171:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 170:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 169:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 168:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 167:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 166:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 165:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 164:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 163:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 162:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 161:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 160:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 159:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 158:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 157:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 156:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 155:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 154:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 153:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 152:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 151:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 150:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 149:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 148:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 147:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 146:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 145:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 144:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 143:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 142:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 141:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 140:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 139:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 138:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 137:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 136:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 135:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 134:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 133:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 132:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 131:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 130:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 129:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 128:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 126:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 125:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 124:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 123:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 122:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 121:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 120:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 119:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 118:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 117:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 116:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 115:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 114:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 113:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 112:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 111:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 110:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 109:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 108:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 107:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 106:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 105:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 104:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 103:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 102:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 101:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 100:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 99:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 98:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 97:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 96:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 95:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 94:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 93:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 92:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 91:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 90:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 89:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 88:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 87:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 86:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 85:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 84:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 83:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 82:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 81:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 80:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 79:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 78:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 77:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 76:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 75:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 74:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 73:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 72:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 71:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 70:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 69:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 68:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 67:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 66:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 65:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 64:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 63:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 62:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 61:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 60:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 59:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 58:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 57:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 56:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 55:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 54:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 53:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 52:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 51:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 50:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 49:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 48:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 47:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 46:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 45:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 44:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 43:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 42:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 41:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 40:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 39:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 38:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 37:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 36:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 35:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 34:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 33:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 32:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 31:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 28:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 27:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 26:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 25:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 24:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 23:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 21:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 20:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 19:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 18:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 17:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 16:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 15:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 14:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 13:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 12:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 11:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 10:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 9:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 8:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 7:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 6:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 5:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 4:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 3:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 2:
            return '~'

        if table2Version == 216 and indicatorOfParameter == 1:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 211:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 210:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 209:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 208:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 207:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 206:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 205:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 204:
            return 'dimensionless'

        if table2Version == 215 and indicatorOfParameter == 203:
            return 'dimensionless'

        if table2Version == 215 and indicatorOfParameter == 202:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 201:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 200:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 199:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 198:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 197:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 196:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 195:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 194:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 193:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 192:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 191:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 190:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 189:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 188:
            return 'm**-1 sr**-1'

        if table2Version == 215 and indicatorOfParameter == 187:
            return 'm**-1 sr**-1'

        if table2Version == 215 and indicatorOfParameter == 186:
            return 'm**-1 sr**-1'

        if table2Version == 215 and indicatorOfParameter == 185:
            return 'm**-1 sr**-1'

        if table2Version == 215 and indicatorOfParameter == 184:
            return 'm**-1 sr**-1'

        if table2Version == 215 and indicatorOfParameter == 183:
            return 'm**-1 sr**-1'

        if table2Version == 215 and indicatorOfParameter == 182:
            return 'm**-1'

        if table2Version == 215 and indicatorOfParameter == 181:
            return 'm**-1'

        if table2Version == 215 and indicatorOfParameter == 180:
            return 'm**-1'

        if table2Version == 215 and indicatorOfParameter == 179:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 178:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 177:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 176:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 175:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 174:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 173:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 172:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 171:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 170:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 169:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 168:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 167:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 166:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 165:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 164:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 163:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 162:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 161:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 160:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 159:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 158:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 157:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 156:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 155:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 154:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 153:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 152:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 151:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 150:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 149:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 148:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 147:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 146:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 145:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 144:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 143:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 142:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 141:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 140:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 139:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 138:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 137:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 136:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 135:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 134:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 133:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 132:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 131:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 130:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 129:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 128:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 126:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 125:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 124:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 123:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 122:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 121:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 120:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 119:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 118:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 117:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 116:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 115:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 114:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 113:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 112:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 111:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 110:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 109:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 108:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 107:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 106:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 105:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 104:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 103:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 102:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 101:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 100:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 99:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 98:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 97:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 96:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 95:
            return 'dimensionless'

        if table2Version == 215 and indicatorOfParameter == 94:
            return 'dimensionless'

        if table2Version == 215 and indicatorOfParameter == 93:
            return 'dimensionless'

        if table2Version == 215 and indicatorOfParameter == 92:
            return 'kg s**2 m**-5'

        if table2Version == 215 and indicatorOfParameter == 91:
            return 'kg s**2 m**-5'

        if table2Version == 215 and indicatorOfParameter == 90:
            return '(0 - 1)'

        if table2Version == 215 and indicatorOfParameter == 89:
            return 's'

        if table2Version == 215 and indicatorOfParameter == 88:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 87:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 86:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 85:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 84:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 83:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 82:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 81:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 80:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 79:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 77:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 76:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 75:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 74:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 73:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 72:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 71:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 70:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 69:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 68:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 67:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 66:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 65:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 64:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 63:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 62:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 61:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 60:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 59:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 58:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 57:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 56:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 55:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 54:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 53:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 52:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 51:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 50:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 49:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 48:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 47:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 46:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 45:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 44:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 43:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 42:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 41:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 40:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 39:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 38:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 37:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 36:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 35:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 34:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 33:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 32:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 31:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 30:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 29:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 28:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 27:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 26:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 25:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 24:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 23:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 215 and indicatorOfParameter == 21:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 20:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 19:
            return 'kg m**-2'

        if table2Version == 215 and indicatorOfParameter == 18:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 17:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 16:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 15:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 14:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 13:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 12:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 11:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 10:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 9:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 8:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 7:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 6:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 5:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 3:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 2:
            return 'kg m**-2 s**-1'

        if table2Version == 215 and indicatorOfParameter == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 214 and indicatorOfParameter == 52:
            return '~'

        if table2Version == 214 and indicatorOfParameter == 51:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 50:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 49:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 48:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 47:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 46:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 45:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 44:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 43:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 42:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 41:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 40:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 39:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 38:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 37:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 36:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 35:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 34:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 33:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 32:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 31:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 30:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 29:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 28:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 27:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 26:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 25:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 24:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 23:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 22:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 21:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 20:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 19:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 18:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 17:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 16:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 15:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 14:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 13:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 12:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 11:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 10:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 9:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 8:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 7:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 6:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 5:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 4:
            return 'W m**-2'

        if table2Version == 214 and indicatorOfParameter == 3:
            return '~'

        if table2Version == 214 and indicatorOfParameter == 2:
            return '~'

        if table2Version == 214 and indicatorOfParameter == 1:
            return '~'

        if table2Version == 213 and indicatorOfParameter == 150:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 149:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 148:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 147:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 146:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 145:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 144:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 143:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 142:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 141:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 140:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 139:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 138:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 137:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 136:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 135:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 134:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 133:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 132:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 131:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 130:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 129:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 128:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 127:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 126:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 125:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 124:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 123:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 122:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 121:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 120:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 119:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 118:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 117:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 116:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 115:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 114:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 113:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 112:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 111:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 110:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 109:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 108:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 107:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 106:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 105:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 104:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 103:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 102:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 101:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 5:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 4:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 3:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 2:
            return 'dimensionless'

        if table2Version == 213 and indicatorOfParameter == 1:
            return 'dimensionless'

        if table2Version == 212 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 254:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 253:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 252:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 251:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 250:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 249:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 248:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 247:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 246:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 245:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 244:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 243:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 242:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 241:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 240:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 239:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 238:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 237:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 236:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 235:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 234:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 233:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 232:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 231:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 230:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 229:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 228:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 227:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 226:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 225:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 224:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 223:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 222:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 221:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 220:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 219:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 218:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 217:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 216:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 215:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 214:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 213:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 212:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 211:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 210:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 209:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 208:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 207:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 206:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 205:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 204:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 203:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 202:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 201:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 200:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 199:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 198:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 197:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 196:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 195:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 194:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 193:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 192:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 191:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 190:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 189:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 188:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 187:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 186:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 185:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 184:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 183:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 182:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 181:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 180:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 179:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 178:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 177:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 176:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 175:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 174:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 173:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 172:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 171:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 170:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 169:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 168:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 167:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 166:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 165:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 164:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 163:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 162:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 161:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 160:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 159:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 158:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 157:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 156:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 155:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 154:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 153:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 152:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 151:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 150:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 149:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 148:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 147:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 146:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 145:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 144:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 143:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 142:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 141:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 140:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 139:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 138:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 137:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 136:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 135:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 134:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 133:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 132:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 131:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 130:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 129:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 128:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 126:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 125:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 124:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 123:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 122:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 121:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 120:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 119:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 118:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 117:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 116:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 115:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 114:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 113:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 112:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 111:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 110:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 109:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 108:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 107:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 106:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 105:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 104:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 103:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 102:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 101:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 100:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 99:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 98:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 97:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 96:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 95:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 94:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 93:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 92:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 91:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 90:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 89:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 88:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 87:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 86:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 85:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 84:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 83:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 82:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 81:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 80:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 79:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 78:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 77:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 76:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 75:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 74:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 73:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 72:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 71:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 70:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 69:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 68:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 67:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 66:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 65:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 64:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 63:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 62:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 61:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 60:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 59:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 58:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 57:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 56:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 55:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 54:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 53:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 52:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 51:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 50:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 49:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 48:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 47:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 46:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 45:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 44:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 43:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 42:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 41:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 40:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 39:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 38:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 37:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 36:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 35:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 34:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 33:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 32:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 31:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 28:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 27:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 26:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 25:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 24:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 23:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 21:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 20:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 19:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 18:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 17:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 16:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 15:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 14:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 13:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 12:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 11:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 10:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 9:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 8:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 7:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 6:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 5:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 4:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 3:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 2:
            return '~'

        if table2Version == 212 and indicatorOfParameter == 1:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 120:
            return 'm'

        if table2Version == 211 and indicatorOfParameter == 119:
            return 'm'

        if table2Version == 211 and indicatorOfParameter == 118:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 56:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 55:
            return '~'

        if table2Version == 211 and indicatorOfParameter == 45:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 44:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 43:
            return 'kg m**-2 s**-1'

        if table2Version == 211 and indicatorOfParameter == 30:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 29:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 28:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 15:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 14:
            return 'kg kg**-1'

        if table2Version == 211 and indicatorOfParameter == 13:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 251:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 250:
            return 'dimensionless'

        if table2Version == 210 and indicatorOfParameter == 249:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 248:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 247:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 246:
            return 'm**-1'

        if table2Version == 210 and indicatorOfParameter == 245:
            return 'm**-1'

        if table2Version == 210 and indicatorOfParameter == 244:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 243:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 242:
            return 'm'

        if table2Version == 210 and indicatorOfParameter == 241:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 240:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 239:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 238:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 237:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 236:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 235:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 234:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 233:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 232:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 231:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 230:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 229:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 228:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 227:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 226:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 225:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 224:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 223:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 222:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 221:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 220:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 219:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 218:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 217:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 197:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 196:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 195:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 194:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 193:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 192:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 191:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 190:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 189:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 188:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 187:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 186:
            return '(0 - 1)'

        if table2Version == 210 and indicatorOfParameter == 120:
            return 'm'

        if table2Version == 210 and indicatorOfParameter == 119:
            return 'm'

        if table2Version == 210 and indicatorOfParameter == 118:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 79:
            return 'deg'

        if table2Version == 210 and indicatorOfParameter == 74:
            return 'kg m**-3'

        if table2Version == 210 and indicatorOfParameter == 73:
            return 'kg m**-3'

        if table2Version == 210 and indicatorOfParameter == 72:
            return 'kg m**-3'

        if table2Version == 210 and indicatorOfParameter == 60:
            return 'm'

        if table2Version == 210 and indicatorOfParameter == 59:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 58:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 57:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 56:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 55:
            return '~'

        if table2Version == 210 and indicatorOfParameter == 45:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 44:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 43:
            return 'kg m**-2 s**-1'

        if table2Version == 210 and indicatorOfParameter == 30:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 29:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 28:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 15:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 14:
            return 'kg kg**-1'

        if table2Version == 210 and indicatorOfParameter == 13:
            return 'kg kg**-1'

        if table2Version == 174 and indicatorOfParameter == 249:
            return '(0 - 1)'

        if table2Version == 174 and indicatorOfParameter == 248:
            return '(0 - 1)'

        if table2Version == 174 and indicatorOfParameter == 240:
            return 'kg m**-2 s**-1'

        if table2Version == 174 and indicatorOfParameter == 239:
            return 'kg m**-2 s**-1'

        if table2Version == 174 and indicatorOfParameter == 186:
            return '(0 - 1)'

        if table2Version == 174 and indicatorOfParameter == 143:
            return 'kg m**-2 s**-1'

        if table2Version == 174 and indicatorOfParameter == 142:
            return 'kg m**-2 s**-1'

        if table2Version == 174 and indicatorOfParameter == 137:
            return 'kg m**-2'

        if table2Version == 174 and indicatorOfParameter == 117:
            return 'J m**-2'

        if table2Version == 174 and indicatorOfParameter == 116:
            return 'J m**-2'

        if table2Version == 174 and indicatorOfParameter == 97:
            return 'm'

        if table2Version == 174 and indicatorOfParameter == 96:
            return 'kg kg**-1'

        if table2Version == 174 and indicatorOfParameter == 52:
            return 'kg kg**-1'

        if table2Version == 174 and indicatorOfParameter == 51:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 50:
            return 'K'

        if table2Version == 174 and indicatorOfParameter == 25:
            return 'm'

        if table2Version == 174 and indicatorOfParameter == 13:
            return 'W m**-2'

        if table2Version == 174 and indicatorOfParameter == 10:
            return 'W m**-2'

        if table2Version == 173 and indicatorOfParameter == 9:
            return 'm of water equivalent s**-1'

        if table2Version == 173 and indicatorOfParameter == 8:
            return 'm of water equivalent s**-1'

        if table2Version == 172 and indicatorOfParameter == 9:
            return 'm of water equivalent s**-1'

        if table2Version == 172 and indicatorOfParameter == 8:
            return 'm of water equivalent s**-1'

        if table2Version == 171 and indicatorOfParameter == 122:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 121:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 25:
            return 'm'

        if table2Version == 171 and indicatorOfParameter == 24:
            return 'K'

        if table2Version == 171 and indicatorOfParameter == 7:
            return 'm s**-1'

        if table2Version == 171 and indicatorOfParameter == 6:
            return 'm s**-1'

        if table2Version == 170 and indicatorOfParameter == 3:
            return 'dimensionless'

        if table2Version == 170 and indicatorOfParameter == 2:
            return 'dimensionless'

        if table2Version == 170 and indicatorOfParameter == 1:
            return 'dimensionless'

        if table2Version == 162 and indicatorOfParameter == 141:
            return 'kg kg**-1'

        if table2Version == 162 and indicatorOfParameter == 140:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 139:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 138:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 137:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 136:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 135:
            return 'kg kg**-1'

        if table2Version == 162 and indicatorOfParameter == 134:
            return 'kg kg**-1'

        if table2Version == 162 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 162 and indicatorOfParameter == 132:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 131:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 130:
            return 'kg m**-2'

        if table2Version == 162 and indicatorOfParameter == 129:
            return 'kg kg**-1'

        if table2Version == 162 and indicatorOfParameter == 128:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 127:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 126:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 125:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 124:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 123:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 122:
            return 'kg kg**-1'

        if table2Version == 162 and indicatorOfParameter == 121:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 120:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 119:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 118:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 117:
            return 'kg kg**-1'

        if table2Version == 162 and indicatorOfParameter == 116:
            return 'K'

        if table2Version == 162 and indicatorOfParameter == 115:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 114:
            return 'm s**-1'

        if table2Version == 162 and indicatorOfParameter == 92:
            return 'kg m**-2 s**-1'

        if table2Version == 162 and indicatorOfParameter == 91:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 90:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 89:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 88:
            return 'kg m**-1 s**-1'

        if table2Version == 162 and indicatorOfParameter == 80:
            return 'kg m**-2 s**-1'

        if table2Version == 162 and indicatorOfParameter == 79:
            return 'kg m**-2 s**-1'

        if table2Version == 162 and indicatorOfParameter == 45:
            return 'kg m**-1 s**-1'

        if table2Version == 151 and indicatorOfParameter == 193:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 214:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 213:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 212:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 211:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 210:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 209:
            return 'kg m**-3'

        if table2Version == 140 and indicatorOfParameter == 208:
            return 'm s**-1'

        if table2Version == 140 and indicatorOfParameter == 207:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 129:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 128:
            return 'degrees'

        if table2Version == 140 and indicatorOfParameter == 127:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 126:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 125:
            return 'degrees'

        if table2Version == 140 and indicatorOfParameter == 124:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 123:
            return 's'

        if table2Version == 140 and indicatorOfParameter == 122:
            return 'degrees'

        if table2Version == 140 and indicatorOfParameter == 121:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 120:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 119:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 118:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 117:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 116:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 115:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 114:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 113:
            return 'Degree true'

        if table2Version == 140 and indicatorOfParameter == 112:
            return 'W m**-1'

        if table2Version == 140 and indicatorOfParameter == 111:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 110:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 109:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 108:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 107:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 106:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 105:
            return 'W m**-2'

        if table2Version == 140 and indicatorOfParameter == 104:
            return 'N m**-2'

        if table2Version == 140 and indicatorOfParameter == 103:
            return 'N m**-2'

        if table2Version == 140 and indicatorOfParameter == 102:
            return 'N m**-2'

        if table2Version == 140 and indicatorOfParameter == 101:
            return 'N m**-2'

        if table2Version == 140 and indicatorOfParameter == 100:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 99:
            return 'dimensionless'

        if table2Version == 140 and indicatorOfParameter == 98:
            return 'm'

        if table2Version == 140 and indicatorOfParameter == 84:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 83:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 82:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 81:
            return '~'

        if table2Version == 140 and indicatorOfParameter == 80:
            return '~'

        if table2Version == 132 and indicatorOfParameter == 216:
            return '(-1 to 1)'

        if table2Version == 132 and indicatorOfParameter == 59:
            return '(-1 to 1)'

        if table2Version == 132 and indicatorOfParameter == 45:
            return 'dimensionless'

        if table2Version == 132 and indicatorOfParameter == 44:
            return '(-1 to 1)'

        if table2Version == 131 and indicatorOfParameter == 100:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 99:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 98:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 97:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 96:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 95:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 94:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 93:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 92:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 91:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 90:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 89:
            return '%'

        if table2Version == 200 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 254:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 253:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 252:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 251:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 250:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 249:
            return '(-1 to 1)'

        if table2Version == 200 and indicatorOfParameter == 248:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 247:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 246:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 245:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 244:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 243:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 242:
            return '(-1 to 1)'

        if table2Version == 200 and indicatorOfParameter == 241:
            return '(-1 to 1)'

        if table2Version == 200 and indicatorOfParameter == 240:
            return 'm of water equivalent'

        if table2Version == 200 and indicatorOfParameter == 239:
            return 'm of water equivalent'

        if table2Version == 200 and indicatorOfParameter == 238:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 237:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 236:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 235:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 234:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 233:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 232:
            return 'kg m**-2 s'

        if table2Version == 200 and indicatorOfParameter == 231:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 230:
            return 'N m**-2'

        if table2Version == 200 and indicatorOfParameter == 229:
            return 'N m**-2'

        if table2Version == 200 and indicatorOfParameter == 228:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 227:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 226:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 225:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 224:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 223:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 222:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 221:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 220:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 219:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 218:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 217:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 216:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 215:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 214:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 212:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 211:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 210:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 209:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 208:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 207:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 206:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 205:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 204:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 203:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 200:
            return 'm**2'

        if table2Version == 200 and indicatorOfParameter == 199:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 198:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 197:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 196:
            return 'N m**-2 s'

        if table2Version == 200 and indicatorOfParameter == 195:
            return 'N m**-2 s'

        if table2Version == 200 and indicatorOfParameter == 194:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 193:
            return 'm**2'

        if table2Version == 200 and indicatorOfParameter == 192:
            return 'm**2'

        if table2Version == 200 and indicatorOfParameter == 191:
            return 'm**2'

        if table2Version == 200 and indicatorOfParameter == 190:
            return 'm**2'

        if table2Version == 200 and indicatorOfParameter == 189:
            return 's'

        if table2Version == 200 and indicatorOfParameter == 188:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 187:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 186:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 185:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 184:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 183:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 182:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 181:
            return 'N m**-2 s'

        if table2Version == 200 and indicatorOfParameter == 180:
            return 'N m**-2 s'

        if table2Version == 200 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 175:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 174:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 173:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 171:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 170:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 169:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 166:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 165:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 164:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 163:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 162:
            return 'radians'

        if table2Version == 200 and indicatorOfParameter == 161:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 160:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 159:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 158:
            return 'Pa s**-1'

        if table2Version == 200 and indicatorOfParameter == 157:
            return '%'

        if table2Version == 200 and indicatorOfParameter == 156:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 155:
            return 's**-1'

        if table2Version == 200 and indicatorOfParameter == 154:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 153:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 152:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 151:
            return 'Pa'

        if table2Version == 200 and indicatorOfParameter == 150:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 149:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 148:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 145:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 144:
            return 'm of water equivalent'

        if table2Version == 200 and indicatorOfParameter == 143:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 142:
            return 'm'

        if table2Version == 200 and indicatorOfParameter == 141:
            return 'm of water equivalent'

        if table2Version == 200 and indicatorOfParameter == 140:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 138:
            return 's**-1'

        if table2Version == 200 and indicatorOfParameter == 137:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 136:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 135:
            return 'Pa s**-1'

        if table2Version == 200 and indicatorOfParameter == 134:
            return 'Pa'

        if table2Version == 200 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 200 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 130:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 200 and indicatorOfParameter == 128:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 126:
            return 'Various'

        if table2Version == 200 and indicatorOfParameter == 125:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 123:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 122:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 121:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 120:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 119:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 118:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 117:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 116:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 115:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 114:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 113:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 112:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 111:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 110:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 109:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 108:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 107:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 106:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 105:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 104:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 103:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 102:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 101:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 100:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 99:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 98:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 97:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 96:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 95:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 94:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 93:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 92:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 91:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 90:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 89:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 88:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 87:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 86:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 85:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 84:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 83:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 82:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 81:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 80:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 71:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 70:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 69:
            return 's m**-1'

        if table2Version == 200 and indicatorOfParameter == 68:
            return 's m**-1'

        if table2Version == 200 and indicatorOfParameter == 67:
            return 'm**2 m**-2'

        if table2Version == 200 and indicatorOfParameter == 66:
            return 'm**2 m**-2'

        if table2Version == 200 and indicatorOfParameter == 65:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 64:
            return 's'

        if table2Version == 200 and indicatorOfParameter == 63:
            return 's'

        if table2Version == 200 and indicatorOfParameter == 62:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 61:
            return 'Millimetres*100 + number of stations'

        if table2Version == 200 and indicatorOfParameter == 60:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 200 and indicatorOfParameter == 59:
            return 'J kg**-1'

        if table2Version == 200 and indicatorOfParameter == 58:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 57:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 56:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 55:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 54:
            return 'Pa'

        if table2Version == 200 and indicatorOfParameter == 53:
            return 'm**2 s**-2'

        if table2Version == 200 and indicatorOfParameter == 52:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 51:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 50:
            return 's'

        if table2Version == 200 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 48:
            return 'N m**-2 s'

        if table2Version == 200 and indicatorOfParameter == 47:
            return 'J m**-2'

        if table2Version == 200 and indicatorOfParameter == 46:
            return 's'

        if table2Version == 200 and indicatorOfParameter == 45:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 44:
            return 'kg m**-2'

        if table2Version == 200 and indicatorOfParameter == 43:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 42:
            return 'm**3 m**-3'

        if table2Version == 200 and indicatorOfParameter == 41:
            return 'm**3 m**-3'

        if table2Version == 200 and indicatorOfParameter == 40:
            return 'm**3 m**-3'

        if table2Version == 200 and indicatorOfParameter == 39:
            return 'm**3 m**-3'

        if table2Version == 200 and indicatorOfParameter == 38:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 37:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 36:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 35:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 34:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 33:
            return 'kg m**-3'

        if table2Version == 200 and indicatorOfParameter == 32:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 31:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 28:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 27:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 26:
            return '(0 - 1)'

        if table2Version == 200 and indicatorOfParameter == 25:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 24:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 23:
            return 's**-1'

        if table2Version == 200 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 200 and indicatorOfParameter == 21:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 14:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 13:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 12:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 11:
            return 'm s**-1'

        if table2Version == 200 and indicatorOfParameter == 5:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 4:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 3:
            return 'K'

        if table2Version == 200 and indicatorOfParameter == 2:
            return 'm**2 s**-1'

        if table2Version == 200 and indicatorOfParameter == 1:
            return 'm**2 s**-1'

        if table2Version == 190 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 180 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 170 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 160 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 132 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 130 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 255:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 254:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 253:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 252:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 251:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 250:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 249:
            return '(-1 to 1)'

        if table2Version == 128 and indicatorOfParameter == 248:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 247:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 246:
            return 'kg kg**-1'

        if table2Version == 160 and indicatorOfParameter == 245:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 245:
            return '~'

        if table2Version == 160 and indicatorOfParameter == 244:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 244:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 243:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 242:
            return '(-1 to 1)'

        if table2Version == 128 and indicatorOfParameter == 241:
            return '(-1 to 1)'

        if table2Version == 128 and indicatorOfParameter == 240:
            return 'm of water equivalent'

        if table2Version == 128 and indicatorOfParameter == 239:
            return 'm of water equivalent'

        if table2Version == 160 and indicatorOfParameter == 238:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 238:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 237:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 237:
            return 'm'

        if table2Version == 160 and indicatorOfParameter == 236:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 236:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 235:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 235:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 234:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 234:
            return '~'

        if table2Version == 160 and indicatorOfParameter == 233:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 233:
            return 'kg kg**-1'

        if table2Version == 160 and indicatorOfParameter == 232:
            return 'kg m**-2 s**-1'

        if table2Version == 128 and indicatorOfParameter == 232:
            return 'kg m**-2 s**-1'

        if table2Version == 128 and indicatorOfParameter == 231:
            return 'W m**-2'

        if table2Version == 160 and indicatorOfParameter == 230:
            return 'N m**-2'

        if table2Version == 128 and indicatorOfParameter == 230:
            return 'N m**-2'

        if table2Version == 160 and indicatorOfParameter == 229:
            return 'N m**-2'

        if table2Version == 128 and indicatorOfParameter == 229:
            return 'N m**-2'

        if table2Version == 190 and indicatorOfParameter == 228:
            return 'm'

        if table2Version == 170 and indicatorOfParameter == 228:
            return 'm'

        if table2Version == 160 and indicatorOfParameter == 228:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 228:
            return 'm'

        if table2Version == 130 and indicatorOfParameter == 227:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 227:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 226:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 225:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 224:
            return 'kg kg**-1'

        if table2Version == 130 and indicatorOfParameter == 223:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 223:
            return 'm s**-1'

        if table2Version == 130 and indicatorOfParameter == 222:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 222:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 221:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 220:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 219:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 218:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 217:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 216:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 215:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 214:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 213:
            return 'kg m**-2'

        if table2Version == 128 and indicatorOfParameter == 212:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 211:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 210:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 209:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 208:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 207:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 206:
            return 'kg m**-2'

        if table2Version == 180 and indicatorOfParameter == 205:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 205:
            return 'm'

        if table2Version == 160 and indicatorOfParameter == 204:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 204:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 203:
            return 'kg kg**-1'

        if table2Version == 190 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 170 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 202:
            return 'K'

        if table2Version == 190 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 170 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 201:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 200:
            return 'm**2'

        if table2Version == 128 and indicatorOfParameter == 200:
            return 'm**2'

        if table2Version == 128 and indicatorOfParameter == 199:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 198:
            return 'm of water equivalent'

        if table2Version == 160 and indicatorOfParameter == 197:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 197:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 196:
            return 'N m**-2 s'

        if table2Version == 128 and indicatorOfParameter == 196:
            return 'N m**-2 s'

        if table2Version == 160 and indicatorOfParameter == 195:
            return 'N m**-2 s'

        if table2Version == 128 and indicatorOfParameter == 195:
            return 'N m**-2 s'

        if table2Version == 128 and indicatorOfParameter == 194:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 193:
            return 'm**2'

        if table2Version == 128 and indicatorOfParameter == 193:
            return 'm**2'

        if table2Version == 160 and indicatorOfParameter == 192:
            return 'm**2'

        if table2Version == 128 and indicatorOfParameter == 192:
            return 'm**2'

        if table2Version == 160 and indicatorOfParameter == 191:
            return 'm**2'

        if table2Version == 128 and indicatorOfParameter == 191:
            return 'm**2'

        if table2Version == 160 and indicatorOfParameter == 190:
            return 'm**2'

        if table2Version == 128 and indicatorOfParameter == 190:
            return 'm**2'

        if table2Version == 128 and indicatorOfParameter == 189:
            return 's'

        if table2Version == 160 and indicatorOfParameter == 188:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 188:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 187:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 187:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 186:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 186:
            return '(0 - 1)'

        if table2Version == 170 and indicatorOfParameter == 185:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 185:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 185:
            return '(0 - 1)'

        if table2Version == 170 and indicatorOfParameter == 184:
            return 'm of water equivalent'

        if table2Version == 128 and indicatorOfParameter == 184:
            return 'm of water equivalent'

        if table2Version == 160 and indicatorOfParameter == 183:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 183:
            return 'K'

        if table2Version == 190 and indicatorOfParameter == 182:
            return 'm of water equivalent'

        if table2Version == 180 and indicatorOfParameter == 182:
            return 'm of water equivalent'

        if table2Version == 170 and indicatorOfParameter == 182:
            return 'm of water equivalent'

        if table2Version == 128 and indicatorOfParameter == 182:
            return 'm of water equivalent'

        if table2Version == 180 and indicatorOfParameter == 181:
            return 'N m**-2 s'

        if table2Version == 170 and indicatorOfParameter == 181:
            return 'N m**-2 s'

        if table2Version == 128 and indicatorOfParameter == 181:
            return 'N m**-2 s'

        if table2Version == 180 and indicatorOfParameter == 180:
            return 'N m**-2 s'

        if table2Version == 170 and indicatorOfParameter == 180:
            return 'N m**-2 s'

        if table2Version == 128 and indicatorOfParameter == 180:
            return 'N m**-2 s'

        if table2Version == 190 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 179:
            return 'J m**-2'

        if table2Version == 190 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 178:
            return 'J m**-2'

        if table2Version == 190 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 170 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 177:
            return 'J m**-2'

        if table2Version == 190 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 170 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 176:
            return 'J m**-2'

        if table2Version == 190 and indicatorOfParameter == 175:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 175:
            return 'J m**-2'

        if table2Version == 190 and indicatorOfParameter == 174:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 174:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 174:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 173:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 173:
            return 'm'

        if table2Version == 190 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 180 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 175 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 174 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 171 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 172:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 171:
            return 'm of water equivalent'

        if table2Version == 160 and indicatorOfParameter == 170:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 170:
            return 'K'

        if table2Version == 190 and indicatorOfParameter == 169:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 169:
            return 'J m**-2'

        if table2Version == 190 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 180 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 168:
            return 'K'

        if table2Version == 190 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 180 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 167:
            return 'K'

        if table2Version == 190 and indicatorOfParameter == 166:
            return 'm s**-1'

        if table2Version == 180 and indicatorOfParameter == 166:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 166:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 166:
            return 'm s**-1'

        if table2Version == 190 and indicatorOfParameter == 165:
            return 'm s**-1'

        if table2Version == 180 and indicatorOfParameter == 165:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 165:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 165:
            return 'm s**-1'

        if table2Version == 190 and indicatorOfParameter == 164:
            return '(0 - 1)'

        if table2Version == 180 and indicatorOfParameter == 164:
            return '(0 - 1)'

        if table2Version == 170 and indicatorOfParameter == 164:
            return '(0 - 1)'

        if table2Version == 160 and indicatorOfParameter == 164:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 164:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 163:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 162:
            return 'radians'

        if table2Version == 128 and indicatorOfParameter == 161:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 160:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 159:
            return 'm'

        if table2Version == 160 and indicatorOfParameter == 158:
            return 'Pa s**-1'

        if table2Version == 128 and indicatorOfParameter == 158:
            return 'Pa s**-1'

        if table2Version == 190 and indicatorOfParameter == 157:
            return '%'

        if table2Version == 170 and indicatorOfParameter == 157:
            return '%'

        if table2Version == 128 and indicatorOfParameter == 157:
            return '%'

        if table2Version == 128 and indicatorOfParameter == 156:
            return 'gpm'

        if table2Version == 190 and indicatorOfParameter == 155:
            return 's**-1'

        if table2Version == 180 and indicatorOfParameter == 155:
            return 's**-1'

        if table2Version == 170 and indicatorOfParameter == 155:
            return 's**-1'

        if table2Version == 160 and indicatorOfParameter == 155:
            return 's**-1'

        if table2Version == 128 and indicatorOfParameter == 155:
            return 's**-1'

        if table2Version == 128 and indicatorOfParameter == 154:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 153:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 152:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 152:
            return '~'

        if table2Version == 190 and indicatorOfParameter == 151:
            return 'Pa'

        if table2Version == 180 and indicatorOfParameter == 151:
            return 'Pa'

        if table2Version == 170 and indicatorOfParameter == 151:
            return 'Pa'

        if table2Version == 160 and indicatorOfParameter == 151:
            return 'Pa'

        if table2Version == 128 and indicatorOfParameter == 151:
            return 'Pa'

        if table2Version == 128 and indicatorOfParameter == 150:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 149:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 148:
            return '~'

        if table2Version == 190 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 180 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 170 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 147:
            return 'J m**-2'

        if table2Version == 190 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 180 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 170 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 146:
            return 'J m**-2'

        if table2Version == 160 and indicatorOfParameter == 145:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 145:
            return 'J m**-2'

        if table2Version == 180 and indicatorOfParameter == 144:
            return 'm of water equivalent'

        if table2Version == 128 and indicatorOfParameter == 144:
            return 'm of water equivalent'

        if table2Version == 180 and indicatorOfParameter == 143:
            return 'm'

        if table2Version == 170 and indicatorOfParameter == 143:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 143:
            return 'm'

        if table2Version == 180 and indicatorOfParameter == 142:
            return 'm'

        if table2Version == 170 and indicatorOfParameter == 142:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 142:
            return 'm'

        if table2Version == 180 and indicatorOfParameter == 141:
            return 'm of water equivalent'

        if table2Version == 170 and indicatorOfParameter == 141:
            return 'm of water equivalent'

        if table2Version == 128 and indicatorOfParameter == 141:
            return 'm of water equivalent'

        if table2Version == 170 and indicatorOfParameter == 140:
            return 'm of water equivalent'

        if table2Version == 128 and indicatorOfParameter == 140:
            return 'm of water equivalent'

        if table2Version == 190 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 170 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 139:
            return 'K'

        if table2Version == 190 and indicatorOfParameter == 138:
            return 's**-1'

        if table2Version == 180 and indicatorOfParameter == 138:
            return 's**-1'

        if table2Version == 170 and indicatorOfParameter == 138:
            return 's**-1'

        if table2Version == 160 and indicatorOfParameter == 138:
            return 's**-1'

        if table2Version == 128 and indicatorOfParameter == 138:
            return 's**-1'

        if table2Version == 180 and indicatorOfParameter == 137:
            return 'kg m**-2'

        if table2Version == 128 and indicatorOfParameter == 137:
            return 'kg m**-2'

        if table2Version == 160 and indicatorOfParameter == 136:
            return 'kg m**-2'

        if table2Version == 128 and indicatorOfParameter == 136:
            return 'kg m**-2'

        if table2Version == 170 and indicatorOfParameter == 135:
            return 'Pa s**-1'

        if table2Version == 128 and indicatorOfParameter == 135:
            return 'Pa s**-1'

        if table2Version == 190 and indicatorOfParameter == 134:
            return 'Pa'

        if table2Version == 180 and indicatorOfParameter == 134:
            return 'Pa'

        if table2Version == 162 and indicatorOfParameter == 52:
            return 'Pa'

        if table2Version == 160 and indicatorOfParameter == 134:
            return 'Pa'

        if table2Version == 128 and indicatorOfParameter == 134:
            return 'Pa'

        if table2Version == 190 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 180 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 170 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 160 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 133:
            return 'kg kg**-1'

        if table2Version == 190 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 180 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 170 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 132:
            return 'm s**-1'

        if table2Version == 190 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 180 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 170 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 160 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 131:
            return 'm s**-1'

        if table2Version == 190 and indicatorOfParameter == 130:
            return 'K'

        if table2Version == 180 and indicatorOfParameter == 130:
            return 'K'

        if table2Version == 170 and indicatorOfParameter == 130:
            return 'K'

        if table2Version == 160 and indicatorOfParameter == 130:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 130:
            return 'K'

        if table2Version == 190 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 180 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 170 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 160 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 128 and indicatorOfParameter == 129:
            return 'm**2 s**-2'

        if table2Version == 160 and indicatorOfParameter == 128:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 128:
            return '~'

        if table2Version == 160 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 126:
            return 'Various'

        if table2Version == 128 and indicatorOfParameter == 125:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 124:
            return 'dimensionless'

        if table2Version == 128 and indicatorOfParameter == 123:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 122:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 121:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 120:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 119:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 118:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 117:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 116:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 115:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 114:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 113:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 112:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 111:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 110:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 109:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 108:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 107:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 106:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 105:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 104:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 103:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 102:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 101:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 100:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 99:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 98:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 97:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 96:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 95:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 94:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 93:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 92:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 91:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 90:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 89:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 88:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 87:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 86:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 85:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 84:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 83:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 82:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 81:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 80:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 128 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 128 and indicatorOfParameter == 77:
            return 's**-1'

        if table2Version == 128 and indicatorOfParameter == 76:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 75:
            return 'kg kg**-1'

        if table2Version == 128 and indicatorOfParameter == 74:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 73:
            return 'W m**-2'

        if table2Version == 128 and indicatorOfParameter == 72:
            return 'W m**-2'

        if table2Version == 128 and indicatorOfParameter == 71:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 70:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 69:
            return 's m**-1'

        if table2Version == 128 and indicatorOfParameter == 68:
            return 's m**-1'

        if table2Version == 128 and indicatorOfParameter == 67:
            return 'm**2 m**-2'

        if table2Version == 128 and indicatorOfParameter == 66:
            return 'm**2 m**-2'

        if table2Version == 128 and indicatorOfParameter == 65:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 64:
            return 's'

        if table2Version == 128 and indicatorOfParameter == 63:
            return 's'

        if table2Version == 128 and indicatorOfParameter == 62:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 60:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 128 and indicatorOfParameter == 59:
            return 'J kg**-1'

        if table2Version == 128 and indicatorOfParameter == 58:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 57:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 56:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 55:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 54:
            return 'Pa'

        if table2Version == 128 and indicatorOfParameter == 53:
            return 'm**2 s**-2'

        if table2Version == 128 and indicatorOfParameter == 52:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 51:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 50:
            return 's'

        if table2Version == 128 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 48:
            return 'N m**-2 s'

        if table2Version == 128 and indicatorOfParameter == 47:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 46:
            return 's'

        if table2Version == 128 and indicatorOfParameter == 45:
            return 'm of water equivalent'

        if table2Version == 128 and indicatorOfParameter == 44:
            return 'm of water equivalent'

        if table2Version == 128 and indicatorOfParameter == 43:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 42:
            return 'm**3 m**-3'

        if table2Version == 128 and indicatorOfParameter == 41:
            return 'm**3 m**-3'

        if table2Version == 128 and indicatorOfParameter == 40:
            return 'm**3 m**-3'

        if table2Version == 128 and indicatorOfParameter == 39:
            return 'm**3 m**-3'

        if table2Version == 128 and indicatorOfParameter == 38:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 37:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 36:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 35:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 34:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 33:
            return 'kg m**-3'

        if table2Version == 128 and indicatorOfParameter == 32:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 31:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 28:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 27:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 26:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 25:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 24:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 23:
            return 's**-1'

        if table2Version == 128 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 128 and indicatorOfParameter == 21:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 20:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 19:
            return 'J m**-2'

        if table2Version == 128 and indicatorOfParameter == 18:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 17:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 16:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 15:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 14:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 13:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 12:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 11:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 10:
            return 'm s**-1'

        if table2Version == 128 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 128 and indicatorOfParameter == 7:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 6:
            return '(0 - 1)'

        if table2Version == 128 and indicatorOfParameter == 5:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 4:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 3:
            return 'K'

        if table2Version == 128 and indicatorOfParameter == 2:
            return 'm**2 s**-1'

        if table2Version == 128 and indicatorOfParameter == 1:
            return 'm**2 s**-1'

        if table2Version == 131 and indicatorOfParameter == 88:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 86:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 85:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 83:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 82:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 63:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 62:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 61:
            return '%'

        if table2Version == 131 and indicatorOfParameter == 60:
            return '%'

    return wrapped
