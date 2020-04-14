import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 253 and indicatorOfParameter == 228:
            return 'm s-1'

        if table2Version == 253 and indicatorOfParameter == 210:
            return 'dBZ'

        if table2Version == 253 and indicatorOfParameter == 209:
            return 'JustAnumber'

        if table2Version == 253 and indicatorOfParameter == 204:
            return 'kg m-2'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'kg/m2/h'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'kg m-2'

        if table2Version == 253 and indicatorOfParameter == 200:
            return 'J kg-1'

        if table2Version == 253 and indicatorOfParameter == 187:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 186:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 185:
            return 'kg m-2'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'kg/m2/h'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'kg m-2'

        if table2Version == 253 and indicatorOfParameter == 181:
            return 'kg/m2/h'

        if table2Version == 253 and indicatorOfParameter == 163:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 162:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 160:
            return 'J kg-1'

        if table2Version == 253 and indicatorOfParameter == 144:
            return 'JustAnumber'

        if table2Version == 253 and indicatorOfParameter == 135:
            return 'Code'

        if table2Version == 253 and indicatorOfParameter == 125:
            return 'N m-2 s'

        if table2Version == 253 and indicatorOfParameter == 124:
            return 'N m-2 s'

        if table2Version == 253 and indicatorOfParameter == 122:
            return 'kg s-2'

        if table2Version == 253 and indicatorOfParameter == 121:
            return 'kg s-2'

        if table2Version == 253 and indicatorOfParameter == 117:
            return 'J m-2'

        if table2Version == 253 and indicatorOfParameter == 115:
            return 'J m-2'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'J m-2'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'W m-2'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'J m-2'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'W m-2'

        if table2Version == 253 and indicatorOfParameter == 112:
            return 'J m-2'

        if table2Version == 253 and indicatorOfParameter == 111:
            return 'J m-2'

        if table2Version == 253 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 253 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 101:
            return 'Deg'

        if table2Version == 253 and indicatorOfParameter == 91:
            return '0to1'

        if table2Version == 253 and indicatorOfParameter == 86:
            return 'kg m-2'

        if table2Version == 253 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 81:
            return '0to1'

        if table2Version == 253 and indicatorOfParameter == 76:
            return 'kg kg-1'

        if table2Version == 253 and indicatorOfParameter == 75:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 74:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 73:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 71:
            return '0to1'

        if table2Version == 253 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 61:
            return 'kg m-2'

        if table2Version == 253 and indicatorOfParameter == 58:
            return 'kg kg-1'

        if table2Version == 253 and indicatorOfParameter == 57:
            return 'hPa s-1'

        if table2Version == 253 and indicatorOfParameter == 54:
            return 'kg m-2'

        if table2Version == 253 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 253 and indicatorOfParameter == 51:
            return 'kg kg-1'

        if table2Version == 253 and indicatorOfParameter == 41:
            return 's-1'

        if table2Version == 253 and indicatorOfParameter == 40:
            return 'm s-1'

        if table2Version == 253 and indicatorOfParameter == 39:
            return 'Pa/s'

        if table2Version == 253 and indicatorOfParameter == 34:
            return 'm s-1'

        if table2Version == 253 and indicatorOfParameter == 33:
            return 'm s-1'

        if table2Version == 253 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 16:
            return 'C'

        if table2Version == 253 and indicatorOfParameter == 15:
            return 'C'

        if table2Version == 253 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 253 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 253 and indicatorOfParameter == 6:
            return 'm2 s-2'

        if table2Version == 253 and indicatorOfParameter == 2:
            return 'kg m-1 s-2'

        if table2Version == 253 and indicatorOfParameter == 1:
            return 'kg m-1 s-2'

        if table2Version == 205 and indicatorOfParameter == 14:
            return 'm s-1'

        if table2Version == 205 and indicatorOfParameter == 13:
            return 'm s-1'

        if table2Version == 205 and indicatorOfParameter == 12:
            return '%'

        if table2Version == 205 and indicatorOfParameter == 11:
            return 'cm'

        if table2Version == 205 and indicatorOfParameter == 10:
            return '%'

        if table2Version == 205 and indicatorOfParameter == 9:
            return 'cm'

        if table2Version == 205 and indicatorOfParameter == 8:
            return 'm s-1'

        if table2Version == 205 and indicatorOfParameter == 7:
            return 'm s-1'

        if table2Version == 205 and indicatorOfParameter == 6:
            return 'cm'

        if table2Version == 205 and indicatorOfParameter == 5:
            return 'cm'

        if table2Version == 205 and indicatorOfParameter == 4:
            return 'cm'

        if table2Version == 205 and indicatorOfParameter == 3:
            return 'cm'

        if table2Version == 205 and indicatorOfParameter == 2:
            return '%'

        if table2Version == 205 and indicatorOfParameter == 1:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 255:
            return 'JustAnumber'

        if table2Version == 203 and indicatorOfParameter == 254:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 253:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 252:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 251:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 250:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 249:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 248:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 247:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 246:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 245:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 244:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 243:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 242:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 241:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 240:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 239:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 238:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 237:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 236:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 235:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 234:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 233:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 232:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 231:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 230:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 229:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 228:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 227:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 226:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 225:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 224:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 223:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 222:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 221:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 220:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 219:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 218:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 217:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 216:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 215:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 214:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 213:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 212:
            return 'kg/m2/h'

        if table2Version == 203 and indicatorOfParameter == 211:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 210:
            return 'N m-2 s'

        if table2Version == 203 and indicatorOfParameter == 209:
            return 'N m-2 s'

        if table2Version == 203 and indicatorOfParameter == 208:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 207:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 206:
            return 'JustAnumber'

        if table2Version == 203 and indicatorOfParameter == 205:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 204:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 203:
            return 'kg m-1 s-2'

        if table2Version == 203 and indicatorOfParameter == 202:
            return 'kg s-2'

        if table2Version == 203 and indicatorOfParameter == 201:
            return 'kg s-2'

        if table2Version == 203 and indicatorOfParameter == 200:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 199:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 198:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 197:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 196:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 195:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 194:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 193:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 192:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 191:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 190:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 189:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 188:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 187:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 186:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 185:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 184:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 183:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 182:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 181:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 180:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 179:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 178:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 177:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 176:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 175:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 174:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 173:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 172:
            return 'kg s-2'

        if table2Version == 203 and indicatorOfParameter == 171:
            return 'kg s-2'

        if table2Version == 203 and indicatorOfParameter == 170:
            return 'kg s-2'

        if table2Version == 203 and indicatorOfParameter == 169:
            return 'kg s-2'

        if table2Version == 203 and indicatorOfParameter == 168:
            return 'kg s-2'

        if table2Version == 203 and indicatorOfParameter == 167:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 166:
            return 'kg/m2/h'

        if table2Version == 203 and indicatorOfParameter == 165:
            return 'kg/m2/h'

        if table2Version == 203 and indicatorOfParameter == 164:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 163:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 161:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 159:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 158:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 157:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 156:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 155:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 154:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 153:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 152:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 151:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 150:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 149:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 148:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 147:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 146:
            return 'kt'

        if table2Version == 203 and indicatorOfParameter == 145:
            return 'kt'

        if table2Version == 203 and indicatorOfParameter == 144:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 143:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 142:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 141:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 134:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 133:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 132:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 131:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 130:
            return 'kg m-3'

        if table2Version == 203 and indicatorOfParameter == 129:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 128:
            return 'W m-2'

        if table2Version == 203 and indicatorOfParameter == 126:
            return 'W m-2'

        if table2Version == 203 and indicatorOfParameter == 122:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 121:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 120:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 119:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 118:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 117:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 116:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 115:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 114:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 113:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 112:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 111:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 110:
            return 'kg/m2/h'

        if table2Version == 203 and indicatorOfParameter == 109:
            return 'kg m-2 s-1'

        if table2Version == 203 and indicatorOfParameter == 108:
            return 'kg m-2 s-1'

        if table2Version == 203 and indicatorOfParameter == 107:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 106:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 105:
            return 'kg kg-1'

        if table2Version == 203 and indicatorOfParameter == 104:
            return 'kg kg-1'

        if table2Version == 203 and indicatorOfParameter == 103:
            return 'Code'

        if table2Version == 203 and indicatorOfParameter == 102:
            return 'Code'

        if table2Version == 203 and indicatorOfParameter == 101:
            return 'kg m-3'

        if table2Version == 203 and indicatorOfParameter == 100:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 99:
            return '0to1'

        if table2Version == 203 and indicatorOfParameter == 96:
            return 'W m-2'

        if table2Version == 203 and indicatorOfParameter == 95:
            return 'W m-2'

        if table2Version == 203 and indicatorOfParameter == 91:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 89:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 80:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 79:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 78:
            return 'kg kg-1'

        if table2Version == 203 and indicatorOfParameter == 77:
            return 'cm'

        if table2Version == 203 and indicatorOfParameter == 75:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 74:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 73:
            return 'kg/m2/h'

        if table2Version == 203 and indicatorOfParameter == 72:
            return 'kg/m2/h'

        if table2Version == 203 and indicatorOfParameter == 71:
            return 'kg/m2/h'

        if table2Version == 203 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 69:
            return 'W m-2'

        if table2Version == 203 and indicatorOfParameter == 68:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 63:
            return 'm 10-4'

        if table2Version == 203 and indicatorOfParameter == 62:
            return 'm 10-4'

        if table2Version == 203 and indicatorOfParameter == 60:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 59:
            return 'JustAnumber'

        if table2Version == 203 and indicatorOfParameter == 58:
            return 'mm'

        if table2Version == 203 and indicatorOfParameter == 57:
            return 'mm'

        if table2Version == 203 and indicatorOfParameter == 56:
            return 'mm'

        if table2Version == 203 and indicatorOfParameter == 55:
            return 'mm'

        if table2Version == 203 and indicatorOfParameter == 54:
            return 'mm'

        if table2Version == 203 and indicatorOfParameter == 53:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 52:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 51:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 50:
            return 'mm'

        if table2Version == 203 and indicatorOfParameter == 47:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 44:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 43:
            return 'mm s-1'

        if table2Version == 203 and indicatorOfParameter == 40:
            return 'Pa/s'

        if table2Version == 203 and indicatorOfParameter == 39:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 38:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 31:
            return 's-1 10-5'

        if table2Version == 203 and indicatorOfParameter == 28:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 27:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 24:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 23:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 22:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 21:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 20:
            return 'Deg'

        if table2Version == 203 and indicatorOfParameter == 19:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 18:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 15:
            return 'No Unit'

        if table2Version == 203 and indicatorOfParameter == 13:
            return '%'

        if table2Version == 203 and indicatorOfParameter == 12:
            return 'kg kg-1'

        if table2Version == 203 and indicatorOfParameter == 10:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 9:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 8:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 4:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 3:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 2:
            return 'm2 s-2'

        if table2Version == 203 and indicatorOfParameter == 1:
            return 'hPa'

    return wrapped
