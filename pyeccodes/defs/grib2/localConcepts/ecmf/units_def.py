import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 254:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 253:
            return 'm**3 m**-3'

        localTablesVersion = h.get_l('localTablesVersion')

        if localTablesVersion == 228 and discipline == 0 and parameterCategory == 254 and parameterNumber == 136:
            return 'm s**-2'

        if localTablesVersion == 228 and discipline == 0 and parameterCategory == 254 and parameterNumber == 134:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 101:
            return 'W'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 117:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 116:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 115:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 114:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 113:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 112:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 111:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 110:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 109:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 108:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 107:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 106:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 105:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 104:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 103:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 102:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 101:
            return 'W'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 216:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 215:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 228:
            return '%'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 167:
            return '%'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 151:
            return '%'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 139:
            return '%'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 132:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 131:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 19:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 18:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 17:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 16:
            return 'm**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 15:
            return 'm**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 14:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 13:
            return 'K'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 12:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 11:
            return 'K'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 10:
            return 'K'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 9:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 8:
            return 'K'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 7:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 6:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 5:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 4:
            return 'K'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 3:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 220 and parameterNumber == 228:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 216:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 215:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 214:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 213:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 212:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 207:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 206:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 203:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 185:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 184:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 183:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 182:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 181:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 166:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 165:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 164:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 163:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 162:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 161:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 160:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 159:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 158:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 157:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 156:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 155:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 154:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 153:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 152:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 151:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 150:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 149:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 148:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 147:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 146:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 145:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 144:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 143:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 142:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 141:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 140:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 139:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 138:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 137:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 136:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 135:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 134:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 133:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 132:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 131:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 130:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 129:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 128:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 127:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 126:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 125:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 124:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 123:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 122:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 121:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 100:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 99:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 98:
            return 'm**2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 97:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 96:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 95:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 94:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 93:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 92:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 71:
            return 's**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 70:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 69:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 68:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 67:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 66:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 65:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 64:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 63:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 62:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 61:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 54:
            return '%'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 53:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 52:
            return 'kg s**2 m**-5'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 51:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 50:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 49:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 48:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 47:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 46:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 42:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 41:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 40:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 39:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 38:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 37:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 36:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 35:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 34:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 33:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 32:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 31:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 27:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 26:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 25:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 24:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 23:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 22:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 21:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 20:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 19:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 18:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 17:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 16:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 12:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 11:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 10:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 9:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 8:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 7:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 6:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 5:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 4:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 3:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 2:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 1:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 216:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 215:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 214:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 213:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 212:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 207:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 206:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 203:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 185:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 184:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 183:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 182:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 181:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 166:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 165:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 164:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 163:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 162:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 161:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 160:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 159:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 158:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 157:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 156:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 155:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 154:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 153:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 152:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 151:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 150:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 149:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 148:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 147:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 146:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 145:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 144:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 143:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 142:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 141:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 140:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 139:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 138:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 137:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 136:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 135:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 134:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 133:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 132:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 131:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 130:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 129:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 128:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 127:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 126:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 125:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 124:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 123:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 122:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 121:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 100:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 99:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 97:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 96:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 95:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 94:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 93:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 92:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 91:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 90:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 89:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 88:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 87:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 86:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 85:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 84:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 83:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 82:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 81:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 80:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 71:
            return 's**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 70:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 69:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 68:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 67:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 66:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 65:
            return 'ppb'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 64:
            return 'ppm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 63:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 62:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 61:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 54:
            return '%'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 53:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 52:
            return 'kg s**2 m**-5'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 51:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 50:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 49:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 48:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 47:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 46:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 42:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 41:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 40:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 39:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 38:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 37:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 36:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 35:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 34:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 33:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 32:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 31:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 27:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 26:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 25:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 24:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 23:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 22:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 21:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 20:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 19:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 18:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 17:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 16:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 12:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 11:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 10:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 9:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 8:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 7:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 6:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 5:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 4:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 3:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 2:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 1:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 241:
            return 'J kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 215:
            return 'K'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 203:
            return 'K'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 200:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 187:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 150:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 139:
            return 'Pa'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 113:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 112:
            return 'kg s**-1 m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 111:
            return 'kg s**-1 m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 102:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 101:
            return 'kg s**-1 m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 100:
            return 'kg s**-1 m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 99:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 85:
            return 'm'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 84:
            return 'm'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 83:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 82:
            return 'm'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 81:
            return 's**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 80:
            return 's**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 79:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 78:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 77:
            return 's**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 76:
            return 'J kg**-1 s**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 75:
            return 's**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 74:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 73:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 72:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 71:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 70:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 69:
            return 'm'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 68:
            return 'm'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 67:
            return 'm**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 66:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 65:
            return 'kg s**-1 m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 64:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 63:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 62:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 61:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 60:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 56:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 55:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 54:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 53:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 52:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 51:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 50:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 42:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 41:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 38:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 37:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 36:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 35:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 34:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 33:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 32:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 31:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 30:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 29:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 17:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 16:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 15:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 14:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 13:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 12:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 11:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 10:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 9:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 8:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 7:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 6:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 5:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 4:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 3:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 2:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 1:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 168:
            return 'K'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 229:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 173:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 171:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 170:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 179:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 178:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 177:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 176:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 149:
            return 'm'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 236:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 202:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 201:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 183:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 175:
            return 'psu'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 170:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 168:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 167:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 164:
            return 'degrees C'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 139:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 111:
            return 'm'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 110:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 90:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 89:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 88:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 87:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 86:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 85:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 83:
            return 'kg C m**-2 s**-1'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 55:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 49:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 42:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 41:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 40:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 39:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 34:
            return 'K'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 31:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 6:
            return 'm'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 236:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 202:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 201:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 183:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 175:
            return 'psu'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 170:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 168:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 167:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 164:
            return 'degrees C'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 139:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 111:
            return 'm'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 110:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 99:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 95:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 94:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 90:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 89:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 88:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 87:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 86:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 85:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 83:
            return 'kg C m**-2 s**-1'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 55:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 49:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 42:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 41:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 40:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 39:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 34:
            return 'K'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 31:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 9:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 6:
            return 'm'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 240:
            return 'm of water equivalent s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 239:
            return 'm of water equivalent s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 228:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 212:
            return 'W m**-2 s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 211:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 210:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 209:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 208:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 205:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 197:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 196:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 195:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 189:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 182:
            return 'm of water s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 181:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 180:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 179:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 178:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 177:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 176:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 175:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 169:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 154:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 153:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 149:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 147:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 146:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 145:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 144:
            return 'm of water equivalent s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 143:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 142:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 50:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 48:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 45:
            return 'm of water s**-1'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 44:
            return 'm of water s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 240:
            return 'm of water equivalent s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 239:
            return 'm of water equivalent s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 228:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 212:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 211:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 210:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 209:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 208:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 205:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 197:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 196:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 195:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 189:
            return 's s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 182:
            return 'm of water s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 181:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 180:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 179:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 178:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 177:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 176:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 175:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 169:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 154:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 153:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 149:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 147:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 146:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 145:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 144:
            return 'm of water equivalent s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 143:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 142:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 50:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 48:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 45:
            return 'm of water s**-1'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 44:
            return 'm of water s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 254:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 253:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 252:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 251:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 250:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 249:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 248:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 247:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 246:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 245:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 244:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 243:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 242:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 241:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 240:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 239:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 238:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 237:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 236:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 235:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 234:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 233:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 232:
            return 'kg m**-2 s'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 231:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 230:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 229:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 228:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 227:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 226:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 225:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 224:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 223:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 222:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 221:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 220:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 219:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 218:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 217:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 216:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 215:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 214:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 212:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 211:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 210:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 209:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 208:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 207:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 206:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 205:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 204:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 203:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 202:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 201:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 200:
            return 'm**2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 199:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 198:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 197:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 196:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 195:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 194:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 193:
            return 'm**2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 192:
            return 'm**2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 191:
            return 'm**2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 190:
            return 'm**2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 189:
            return 's'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 188:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 187:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 186:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 185:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 184:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 183:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 182:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 181:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 180:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 179:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 178:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 177:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 176:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 175:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 174:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 173:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 171:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 170:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 169:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 168:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 167:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 166:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 165:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 164:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 162:
            return 'radians'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 159:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 158:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 157:
            return '%'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 156:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 155:
            return 's**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 154:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 153:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 152:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 151:
            return 'Pa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 149:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 147:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 146:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 145:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 144:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 143:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 142:
            return 'm'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 141:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 140:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 139:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 138:
            return 's**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 137:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 136:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 135:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 134:
            return 'Pa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 133:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 132:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 131:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 130:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 129:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 126:
            return 'Various'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 125:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 79:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 78:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 65:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 64:
            return 's'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 63:
            return 's'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 61:
            return 'Millimetres*100 + number of stations'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 60:
            return 'K m**2 kg**-1 s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 59:
            return 'J kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 58:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 57:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 56:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 55:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 54:
            return 'Pa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 53:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 52:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 51:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 50:
            return 's'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 49:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 48:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 47:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 46:
            return 's'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 45:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 44:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 43:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 42:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 41:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 40:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 39:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 38:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 37:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 36:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 35:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 34:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 33:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 32:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 31:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 29:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 28:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 27:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 26:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 23:
            return 's**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 21:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 14:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 13:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 12:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 11:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 5:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 4:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 3:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 2:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 1:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 179:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 171:
            return 'm'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 149:
            return 'm'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 233:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 232:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 231:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 230:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 229:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 227:
            return 'Pa**2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 226:
            return 'Pa**2 s**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 225:
            return 'm Pa s**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 224:
            return 'm Pa s**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 223:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 222:
            return 'Pa s**-1 K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 221:
            return 'm**2 Pa s**-3'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 220:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 219:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 218:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 217:
            return 'm s**-1 K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 216:
            return 'm**3 s**-3'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 215:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 214:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 213:
            return 'm s**-1 K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 212:
            return 'm**3 s**-3'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 210:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 209:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 208:
            return 'K**2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 207:
            return 'm**2 K s**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 206:
            return 'm**4 s**-4'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 113:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 112:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 111:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 110:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 109:
            return 'm**2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 108:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 107:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 106:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 105:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 104:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 103:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 102:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 101:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 100:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 87:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 86:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 85:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 84:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 83:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 82:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 81:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 78:
            return 'kg m**-1 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 77:
            return 'kg m**-1 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 76:
            return 'W m**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 75:
            return 'W m**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 74:
            return 'W m**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 73:
            return 'W m**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 72:
            return 'kg m**-1 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 71:
            return 'kg m**-1 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 70:
            return 'W m**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 69:
            return 'W m**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 68:
            return 'W m**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 67:
            return 'W m**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 66:
            return 'kg m**-1 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 65:
            return 'kg m**-1 s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 64:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 63:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 62:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 61:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 60:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 59:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 58:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 57:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 56:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 55:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 54:
            return 'K kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 53:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 51:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 254:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 249:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 247:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 246:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 243:
            return '~'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 242:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 241:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 240:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 239:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 231:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 226:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 225:
            return 'Pa m s**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 224:
            return 'Pa m s**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 223:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 222:
            return 'K Pa s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 221:
            return 'Pa m**2 s**-3'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 220:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 219:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 218:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 217:
            return 'K m s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 216:
            return 'm**3 s**-3'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 215:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 214:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 213:
            return 'K m s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 212:
            return 'm**3 s**-3'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 211:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 210:
            return 'K'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 209:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 208:
            return 'K'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 207:
            return 'K m**2 s**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 206:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 205:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 202:
            return 'K'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 201:
            return 'K'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 199:
            return '%'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 198:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 184:
            return 'm'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 182:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 181:
            return 'N m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 180:
            return 'N m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 171:
            return 'm'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 157:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 156:
            return 'm'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 144:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 143:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 142:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 140:
            return 'm'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 137:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 135:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 49:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 212:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 211:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 210:
            return 'Pa'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 209:
            return 'Pa'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 208:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 207:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 206:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 205:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 204:
            return 'Pa m**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 203:
            return 'Pa m**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 202:
            return '~'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 201:
            return 'deg C per time step'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 200:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 199:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 194:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 192:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 191:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 190:
            return 'psu per time step'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 188:
            return '~'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 187:
            return 'm s**-1 per time step'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 186:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 185:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 184:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 183:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 182:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 181:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 180:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 179:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 178:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 177:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 176:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 174:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 173:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 172:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 171:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 170:
            return 'J m**-1 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 169:
            return 'J m**-1 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 168:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 167:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 166:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 165:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 164:
            return 'degrees C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 162:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 161:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 160:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 159:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 158:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 157:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 156:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 155:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 154:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 153:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 152:
            return 'Nm**-3'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 151:
            return 'N m**-3'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 150:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 149:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 148:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 147:
            return 'm**3 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 146:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 144:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 143:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 142:
            return 'm s**-1 deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 141:
            return 'm s**-1 degC'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 140:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 139:
            return '~'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 138:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 137:
            return 'm'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 136:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 135:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 134:
            return 's**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 133:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 130:
            return 'psu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 129:
            return 'deg C'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 128:
            return 'deg C'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 183:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 182:
            return 'deg C'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 181:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 180:
            return 'deg C'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 173:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 172:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 171:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 170:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 169:
            return 'Pa'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 168:
            return 'Pa'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 155:
            return 'm'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 154:
            return 'm'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 153:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 152:
            return 'm'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 148:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 147:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 146:
            return 'm s**-1 deg C'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 145:
            return 'm s**-1 deg C'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 144:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 143:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 142:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 141:
            return 'm s**-1 deg C'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 140:
            return 'm s**-1 deg C'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 139:
            return 'm s**-2'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 137:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 135:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 134:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 133:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 131:
            return 'kg m**-3 -1000'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 130:
            return 'psu'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 129:
            return 'deg C'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 254:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 253:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 252:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 251:
            return 'm**2 s radian**-1'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 250:
            return 'm**2 s radian**-1'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 249:
            return 'degrees'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 248:
            return '~'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 247:
            return 'm'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 246:
            return 'm'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 245:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 244:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 243:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 242:
            return 'degrees'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 241:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 240:
            return 'm'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 239:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 238:
            return 'degrees'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 237:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 235:
            return 'degrees'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'm'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 233:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 231:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 228:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 227:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 226:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 225:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 224:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 223:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 222:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 221:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 220:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 219:
            return 'm'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 218:
            return 'm'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 217:
            return 's'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 200:
            return 'm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 92:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 91:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 90:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 89:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 88:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 87:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 86:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 85:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 84:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 83:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 82:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 81:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 80:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 79:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 78:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 77:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 76:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 75:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 74:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 73:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 72:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 71:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 70:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 69:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 68:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 67:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 66:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 65:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 64:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 63:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 62:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 61:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 60:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 59:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 58:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 57:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 56:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 55:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 54:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 53:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 52:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 51:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 50:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 49:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 48:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 47:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 46:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 45:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 44:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 43:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 42:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 41:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 40:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 39:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 38:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 37:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 36:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 35:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 34:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 33:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 32:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 31:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 30:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 29:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 28:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 27:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 26:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 25:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 24:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 23:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 22:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 21:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 20:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 19:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 18:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 17:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 16:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 15:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 14:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 13:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 12:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 11:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 10:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 9:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 8:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 7:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 6:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 5:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 4:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 3:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 2:
            return '%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 1:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 232:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 229:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 228:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 202:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 201:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 167:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 165:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 164:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 151:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 144:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 139:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 130:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 129:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 81:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 80:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 79:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 78:
            return '%'

        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')
        scaleFactorOfLowerLimit = h.get_l('scaleFactorOfLowerLimit')
        probabilityType = h.get_l('probabilityType')

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaledValueOfLowerLimit == 8 and typeOfFirstFixedSurface == 101 and productDefinitionTemplateNumber == 5 and scaleFactorOfLowerLimit == 0 and probabilityType == 3:
            return '%'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 6 and productDefinitionTemplateNumber == 5 and typeOfFirstFixedSurface == 101 and probabilityType == 3:
            return '%'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and probabilityType == 3 and typeOfFirstFixedSurface == 101 and productDefinitionTemplateNumber == 5 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 4:
            return '%'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 5 and scaledValueOfLowerLimit == 2 and typeOfFirstFixedSurface == 101 and probabilityType == 3:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 73:
            return '%'

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfLowerLimit == 25 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 103 and probabilityType == 3:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 69:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 68:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 67:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 66:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 65:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 64:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 59:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 49:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 25:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 24:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 23:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 22:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 21:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 20:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 18:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 17:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 16:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 15:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 10:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 9:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 8:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 7:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 6:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 5:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 4:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 3:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 2:
            return '%'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 1:
            return '%'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 232:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 231:
            return 'm**2 s**-3'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 230:
            return 'm**2 s**-3'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 229:
            return 'kg kg**-1 s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 228:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 226:
            return 'kg kg**-1 s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 225:
            return 'kg kg**-1 s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 224:
            return 'kg kg**-1 s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 221:
            return 'm**2 s**-3'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 220:
            return 'm**2 s**-3'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 219:
            return 'm**2 s**-3'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 218:
            return 'm**2 s**-3'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 217:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 216:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 215:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 214:
            return 'K s**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 213:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 212:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 211:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 210:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 209:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 208:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 254:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 253:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 252:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 251:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 250:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 249:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 248:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 247:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 246:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 245:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 244:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 243:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 242:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 241:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 240:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 239:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 238:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 237:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 236:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 235:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 234:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 233:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 232:
            return 'kg m**-2 s'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 231:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 230:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 229:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 228:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 227:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 226:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 225:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 224:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 223:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 222:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 221:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 220:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 219:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 218:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 217:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 216:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 215:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 214:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 212:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 211:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 210:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 209:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 208:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 207:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 206:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 205:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 204:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 203:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 202:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 201:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 200:
            return 'm**2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 199:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 198:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 197:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 196:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 195:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 194:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 193:
            return 'm**2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 192:
            return 'm**2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 191:
            return 'm**2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 190:
            return 'm**2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 189:
            return 's'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 188:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 187:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 186:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 185:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 184:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 183:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 182:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 181:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 180:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 179:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 178:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 177:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 176:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 175:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 174:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 173:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 172:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 171:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 170:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 169:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 168:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 167:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 166:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 165:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 164:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 162:
            return 'radians'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 159:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 158:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 157:
            return '%'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 156:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 155:
            return 's**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 154:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 153:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 152:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 151:
            return 'Pa'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 149:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 147:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 146:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 145:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 144:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 143:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 142:
            return 'm'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 141:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 140:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 139:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 138:
            return 's**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 137:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 136:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 135:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 134:
            return 'Pa'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 133:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 132:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 131:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 130:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 129:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 126:
            return 'Various'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 125:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 123:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 122:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 121:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 79:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 78:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 71:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 70:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 69:
            return 's m**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 68:
            return 's m**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 67:
            return 'm**2 m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 66:
            return 'm**2 m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 65:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 64:
            return 's'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 63:
            return 's'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 61:
            return 'Millimetres*100 + number of stations'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 60:
            return 'K m**2 kg**-1 s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 59:
            return 'J kg**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 58:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 57:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 56:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 55:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 54:
            return 'Pa'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 53:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 52:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 51:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 50:
            return 's'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 49:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 48:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 47:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 46:
            return 's'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 45:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 44:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 43:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 42:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 41:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 40:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 39:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 38:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 37:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 36:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 35:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 34:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 33:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 32:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 31:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 29:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 28:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 27:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 26:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 23:
            return 's**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 21:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 14:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 13:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 12:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 11:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 5:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 4:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 3:
            return 'K'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 2:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 1:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 255:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 252:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 251:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 250:
            return 'Proportion'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 248:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 130:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 129:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 103:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 102:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 101:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 100:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 94:
            return 'K'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 93:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 92:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 91:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 90:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 89:
            return 'kg m**-2'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'kg m**-2'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'dimensionless'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 60:
            return 'km**-2 day**-1'

        lengthOfTimeRange = h.get_l('lengthOfTimeRange')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and lengthOfTimeRange == 6 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'km**-2 day**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 59:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and lengthOfTimeRange == 3 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'km**-2 day**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 58:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6:
            return 'km**-2 day**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 57:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and lengthOfTimeRange == 3 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8:
            return 'km**-2 day**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 53:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 1 and typeOfSecondFixedSurface == 8:
            return 'km**-2 day**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 52:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'km**-2 day**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 51:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 1:
            return 'km**-2 day**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 50:
            return 'km**-2 day**-1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'km**-2 day**-1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 48:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 47:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 43:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 42:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 41:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 40:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 28:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and lengthOfTimeRange == 3 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and lengthOfTimeRange == 3 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1:
            return 'K'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 25:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 23:
            return 'm'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 22:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 21:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 206:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 205:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 204:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 203:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 202:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 201:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 200:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 199:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 198:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 197:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 196:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 195:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 194:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 193:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 192:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 191:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 190:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 189:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 188:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 187:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 186:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 185:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 184:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 183:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 182:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 181:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 180:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 179:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 178:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 177:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 176:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 175:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 174:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 173:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 172:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 171:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 170:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 169:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 168:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 167:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 166:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 165:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 164:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 163:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 162:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 161:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 160:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 159:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 158:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 157:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 156:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 155:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 154:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 153:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 152:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 151:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 150:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 149:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 148:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 147:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 146:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 145:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 144:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 143:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 142:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 141:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 140:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 139:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 138:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 137:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 136:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 135:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 134:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 133:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 132:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 131:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 130:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 129:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 128:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 127:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 126:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 125:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 124:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 123:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 122:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 121:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 120:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 119:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 118:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 117:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 116:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 115:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 114:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 113:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 112:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 111:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 110:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 109:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 108:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 107:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 106:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 105:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 104:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 103:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 102:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 101:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 100:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 99:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 98:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 97:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 96:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 95:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 94:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 93:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 92:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 91:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 90:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 89:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 88:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 87:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 86:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 85:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 84:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 83:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 82:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 81:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 80:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 79:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 78:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 77:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 76:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 75:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 74:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 73:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 72:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 71:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 70:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 69:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 68:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 67:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 66:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 65:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 64:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 63:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 62:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 61:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 60:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 59:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 58:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 57:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 56:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 55:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 54:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 53:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 52:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 51:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 50:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 49:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 48:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 47:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 46:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 45:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 44:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 43:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 42:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 41:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 40:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 39:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 38:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 37:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 36:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 35:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 34:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 33:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 32:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 31:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 30:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 29:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 28:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 27:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 26:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 25:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 24:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 23:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 22:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 21:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 20:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 19:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 18:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 17:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 16:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 15:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 14:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 13:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 12:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 11:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 10:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 9:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 8:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 7:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 6:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 5:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 4:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 3:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 2:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 1:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 220:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 219:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 218:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 217:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 216:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 215:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 214:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 213:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 212:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 211:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 210:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 209:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 208:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 207:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 206:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 205:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 204:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 203:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 202:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 201:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 200:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 199:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 198:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 197:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 196:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 195:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 194:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 193:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 192:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 191:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 190:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 189:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 188:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 187:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 186:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 185:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 184:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 183:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 182:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 181:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 180:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 179:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 178:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 177:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 176:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 175:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 174:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 173:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 172:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 171:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 170:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 169:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 168:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 167:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 166:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 165:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 164:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 163:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 162:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 161:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 160:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 159:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 158:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 157:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 156:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 155:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 154:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 153:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 152:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 151:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 150:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 149:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 148:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 147:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 146:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 145:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 144:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 143:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 142:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 141:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 140:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 139:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 138:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 137:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 136:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 135:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 134:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 133:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 132:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 131:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 130:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 129:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 128:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 127:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 126:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 125:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 124:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 123:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 122:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 121:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 120:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 119:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 118:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 117:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 116:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 115:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 114:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 113:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 112:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 111:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 110:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 109:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 108:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 107:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 106:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 105:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 104:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 103:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 102:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 101:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 100:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 99:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 98:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 97:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 96:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 95:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 94:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 93:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 92:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 91:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 90:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 89:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 88:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 87:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 86:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 85:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 84:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 83:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 82:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 81:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 80:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 79:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 78:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 77:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 76:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 75:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 74:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 73:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 72:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 71:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 70:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 69:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 68:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 67:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 66:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 65:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 64:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 63:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 62:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 61:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 60:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 59:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 58:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 57:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 56:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 55:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 54:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 53:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 52:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 51:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 50:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 49:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 48:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 47:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 46:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 45:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 44:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 43:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 42:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 41:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 40:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 39:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 38:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 37:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 36:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 35:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 34:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 33:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 32:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 31:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 30:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 29:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 28:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 27:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 26:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 25:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 24:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 23:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 22:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 21:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 20:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 19:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 18:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 17:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 16:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 15:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 14:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 13:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 12:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 11:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 10:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 9:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 8:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 7:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 6:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 5:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 4:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 3:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 2:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 1:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 206:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 205:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 204:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 203:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 202:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 201:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 200:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 199:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 198:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 197:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 196:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 195:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 194:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 193:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 192:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 191:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 190:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 189:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 188:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 187:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 186:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 185:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 184:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 183:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 182:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 181:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 180:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 179:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 178:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 177:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 176:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 175:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 174:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 173:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 172:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 171:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 170:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 169:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 168:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 167:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 166:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 165:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 164:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 163:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 162:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 161:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 160:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 159:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 158:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 157:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 156:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 155:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 154:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 153:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 152:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 151:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 150:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 149:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 148:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 147:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 146:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 145:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 144:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 143:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 142:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 141:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 140:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 139:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 138:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 137:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 136:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 135:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 134:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 133:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 132:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 131:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 130:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 129:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 128:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 127:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 126:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 125:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 124:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 123:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 122:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 121:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 120:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 119:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 118:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 117:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 116:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 115:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 114:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 113:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 112:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 111:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 110:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 109:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 108:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 107:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 106:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 105:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 104:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 103:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 102:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 101:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 100:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 99:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 98:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 97:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 96:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 95:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 94:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 93:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 92:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 91:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 90:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 89:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 88:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 87:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 86:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 85:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 84:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 83:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 82:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 81:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 80:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 79:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 78:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 77:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 76:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 75:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 74:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 73:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 72:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 71:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 70:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 69:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 68:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 67:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 66:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 65:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 64:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 63:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 62:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 61:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 60:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 59:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 58:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 57:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 56:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 55:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 54:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 53:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 52:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 51:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 50:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 49:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 48:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 47:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 46:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 45:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 44:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 43:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 42:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 41:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 40:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 39:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 38:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 37:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 36:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 35:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 34:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 33:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 32:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 30:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 29:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 28:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 27:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 26:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 24:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 23:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 22:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 21:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 20:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 19:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 18:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 16:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 15:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 14:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 13:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 12:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 11:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 10:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 9:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 7:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 6:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 4:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 3:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 206:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 205:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 204:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 203:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 202:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 201:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 200:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 199:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 198:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 197:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 196:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 195:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 194:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 193:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 192:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 191:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 190:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 189:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 188:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 187:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 186:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 185:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 184:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 183:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 182:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 181:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 180:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 179:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 178:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 177:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 176:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 175:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 174:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 173:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 172:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 171:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 170:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 169:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 168:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 167:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 166:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 165:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 164:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 163:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 162:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 161:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 160:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 159:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 158:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 157:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 156:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 155:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 154:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 153:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 152:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 151:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 150:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 149:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 148:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 147:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 146:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 145:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 144:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 143:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 142:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 141:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 140:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 139:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 138:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 137:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 136:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 135:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 134:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 133:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 132:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 131:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 130:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 129:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 128:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 127:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 126:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 125:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 124:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 123:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 122:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 121:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 120:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 119:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 118:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 117:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 116:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 115:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 114:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 113:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 112:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 111:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 110:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 109:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 108:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 107:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 106:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 105:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 104:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 103:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 102:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 101:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 100:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 99:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 98:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 97:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 96:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 95:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 94:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 93:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 92:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 91:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 90:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 89:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 88:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 87:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 86:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 85:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 84:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 83:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 82:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 81:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 80:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 79:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 78:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 77:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 76:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 75:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 74:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 73:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 72:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 71:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 70:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 69:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 68:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 67:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 66:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 65:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 64:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 63:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 62:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 61:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 60:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 59:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 58:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 57:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 56:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 55:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 54:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 53:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 52:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 51:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 50:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 49:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 48:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 47:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 46:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 45:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 44:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 43:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 42:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 41:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 40:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 39:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 38:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 37:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 36:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 35:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 34:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 33:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 32:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 30:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 29:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 28:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 27:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 26:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 24:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 23:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 22:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 21:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 20:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 19:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 18:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 16:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 15:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 14:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 13:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 12:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 11:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 10:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 9:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 7:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 6:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 4:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 3:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 254:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 253:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 252:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 251:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 250:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 249:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 248:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 247:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 246:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 245:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 244:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 243:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 242:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 241:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 240:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 239:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 238:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 237:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 236:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 235:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 234:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 233:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 232:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 231:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 230:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 229:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 228:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 227:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 226:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 225:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 224:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 223:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 222:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 221:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 220:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 219:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 218:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 217:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 216:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 215:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 214:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 213:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 212:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 207:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 206:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 205:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 204:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 203:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 202:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 201:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 200:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 199:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 198:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 197:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 196:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 195:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 194:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 193:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 192:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 191:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 190:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 189:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 188:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 187:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 186:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 185:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 184:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 183:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 182:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 181:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 180:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 179:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 178:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 177:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 176:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 175:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 174:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 173:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 172:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 171:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 170:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 169:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 168:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 167:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 166:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 165:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 164:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 162:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 159:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 158:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 157:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 156:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 155:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 154:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 153:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 152:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 151:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 149:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 147:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 146:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 145:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 144:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 143:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 142:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 141:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 140:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 139:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 138:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 137:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 136:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 135:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 134:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 133:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 132:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 131:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 130:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 129:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 125:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 124:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 123:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 122:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 121:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 79:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 78:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 77:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 76:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 75:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 74:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 73:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 72:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 71:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 70:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 69:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 68:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 67:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 66:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 65:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 64:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 63:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 61:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 60:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 59:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 58:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 57:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 54:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 53:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 52:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 51:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 50:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 49:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 48:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 47:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 46:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 45:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 44:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 43:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 42:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 41:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 40:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 39:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 38:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 37:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 36:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 35:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 34:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 33:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 32:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 31:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 29:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 28:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 27:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 26:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 23:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 21:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 20:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 19:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 18:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 17:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 16:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 15:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 14:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 13:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 12:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 11:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 10:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 9:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 8:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 7:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 6:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 5:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 4:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 3:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 2:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 1:
            return '~'

        is_aerosol = h.get_l('is_aerosol')
        aerosolType = h.get_l('aerosolType')

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and is_aerosol == 1 and aerosolType == 62003:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and is_aerosol == 1 and aerosolType == 62003:
            return 'kg m**-2 s**-1'

        typeOfWavelengthInterval = h.get_l('typeOfWavelengthInterval')
        scaleFactorOfFirstWavelength = h.get_l('scaleFactorOfFirstWavelength')
        is_aerosol_optical = h.get_l('is_aerosol_optical')
        typeOfSizeInterval = h.get_l('typeOfSizeInterval')
        scaledValueOfFirstWavelength = h.get_l('scaledValueOfFirstWavelength')

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfWavelengthInterval == 11 and aerosolType == 65533 and scaleFactorOfFirstWavelength == 8 and is_aerosol_optical == 1 and typeOfSizeInterval == 255 and scaledValueOfFirstWavelength == 55:
            return 'dimensionless'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and scaleFactorOfFirstWavelength == 8 and is_aerosol_optical == 1 and typeOfSizeInterval == 255 and scaledValueOfFirstWavelength == 55 and typeOfWavelengthInterval == 11 and aerosolType == 65534:
            return 'dimensionless'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and aerosolType == 65533 and is_aerosol == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'kg m**-2'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and is_aerosol == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1 and aerosolType == 65534:
            return 'kg m**-2'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and is_aerosol == 1 and aerosolType == 65533:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and aerosolType == 65534 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and is_aerosol == 1 and aerosolType == 65533:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and is_aerosol == 1 and aerosolType == 65534:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and is_aerosol == 1 and aerosolType == 65533:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and is_aerosol == 1 and aerosolType == 65534:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and is_aerosol == 1 and aerosolType == 65533:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 65534 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 65533 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 65534 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 65533 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 65534 and is_aerosol == 1:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 188:
            return 'm**-1 sr**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 187:
            return 'm**-1 sr**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 186:
            return 'm**-1 sr**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 185:
            return 'm**-1 sr**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 184:
            return 'm**-1 sr**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 183:
            return 'm**-1 sr**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 182:
            return 'm**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 181:
            return 'm**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 180:
            return 'm**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 179:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 178:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 177:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 176:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 175:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 174:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 173:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 172:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 171:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 170:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 169:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 168:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 167:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 166:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 165:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 164:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 162:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 159:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 158:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 157:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 156:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 155:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 154:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 153:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 152:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 151:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 149:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 148:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 147:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 146:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 145:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 144:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 143:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 142:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 141:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 140:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 139:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 138:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 137:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 136:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 135:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 134:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 133:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 132:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 131:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 130:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 129:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 125:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 124:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 123:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 122:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 121:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 95:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 94:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 93:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 92:
            return 'kg s**2 m**-5'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 91:
            return 'kg s**2 m**-5'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 90:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 89:
            return 's'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 87:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 86:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 85:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 84:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 83:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 82:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 81:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 79:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 78:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 77:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 76:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 75:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 74:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 73:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 72:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 71:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 70:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 69:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 68:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 67:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 66:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 65:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 64:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 63:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 62:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 61:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 60:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 59:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 58:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 57:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 56:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 55:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 54:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 53:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 52:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 51:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 50:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 49:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 48:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 47:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 46:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 45:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 44:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 43:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 42:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 41:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 40:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 39:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 38:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 37:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 36:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 35:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 34:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 33:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 32:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 31:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 30:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 29:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 28:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 27:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 26:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 25:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 23:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 21:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 20:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 19:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 18:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 17:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 16:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 15:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 14:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 13:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 12:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 11:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 10:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 9:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 8:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 7:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 6:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 5:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 4:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 3:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 2:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 1:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 52:
            return '~'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 51:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 50:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 49:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 48:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 47:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 46:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 45:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 44:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 43:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 42:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 41:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 40:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 39:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 38:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 37:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 36:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 35:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 34:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 33:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 32:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 31:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 30:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 29:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 28:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 27:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 26:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 25:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 24:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 23:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 22:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 21:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 20:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 19:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 18:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 17:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 16:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 15:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 14:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 13:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 12:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 11:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 10:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 9:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 8:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 7:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 6:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 5:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 4:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 3:
            return '~'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 2:
            return '~'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 1:
            return '~'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 150:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 149:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 148:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 147:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 146:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 145:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 144:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 143:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 142:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 141:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 140:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 139:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 138:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 137:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 136:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 135:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 134:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 133:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 132:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 131:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 130:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 129:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 128:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 127:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 126:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 125:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 124:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 123:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 122:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 121:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 120:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 119:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 118:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 117:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 116:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 115:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 114:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 113:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 112:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 111:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 110:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 109:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 108:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 107:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 106:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 105:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 104:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 103:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 102:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 101:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 5:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 4:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 3:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 2:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 1:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 254:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 253:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 252:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 251:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 250:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 249:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 248:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 247:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 246:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 245:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 244:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 243:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 242:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 241:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 240:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 239:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 238:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 237:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 236:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 235:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 234:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 233:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 232:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 231:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 230:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 229:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 228:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 227:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 226:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 225:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 224:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 223:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 222:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 221:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 220:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 219:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 218:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 217:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 216:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 215:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 214:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 213:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 212:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 207:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 206:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 205:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 204:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 203:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 202:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 201:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 200:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 199:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 198:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 197:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 196:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 195:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 194:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 193:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 192:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 191:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 190:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 189:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 188:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 187:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 186:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 185:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 184:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 183:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 182:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 181:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 180:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 179:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 178:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 177:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 176:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 175:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 174:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 173:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 172:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 171:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 170:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 169:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 168:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 167:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 166:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 165:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 164:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 162:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 159:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 158:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 157:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 156:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 155:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 154:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 153:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 152:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 151:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 149:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 147:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 146:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 145:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 144:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 143:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 142:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 141:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 140:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 139:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 138:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 137:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 136:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 135:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 134:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 133:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 132:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 131:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 130:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 129:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 125:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 124:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 123:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 122:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 121:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 79:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 78:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 77:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 76:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 75:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 74:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 73:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 72:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 71:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 70:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 69:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 68:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 67:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 66:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 65:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 64:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 63:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 61:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 60:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 59:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 58:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 57:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 54:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 53:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 52:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 51:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 50:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 49:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 48:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 47:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 46:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 45:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 44:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 43:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 42:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 41:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 40:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 39:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 38:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 37:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 36:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 35:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 34:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 33:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 32:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 31:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 29:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 28:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 27:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 26:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 23:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 21:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 20:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 19:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 18:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 17:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 16:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 15:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 14:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 13:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 12:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 11:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 10:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 9:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 8:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 7:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 6:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 5:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 4:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 3:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 2:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 1:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 120:
            return 'm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 119:
            return 'm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 45:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 44:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 43:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 30:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 29:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 28:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 15:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 14:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 13:
            return 'kg kg**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and aerosolType == 65533 and is_aerosol == 1:
            return 'kg kg**-1'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and is_aerosol == 1 and aerosolType == 65534:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 246:
            return 'm**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 245:
            return 'm**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 244:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 243:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 242:
            return 'm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 241:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 240:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 239:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 238:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 237:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 236:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 235:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 234:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 233:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 232:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 231:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 230:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 229:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 228:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 227:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 226:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 225:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 224:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 223:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 222:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 221:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 220:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 219:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 218:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 217:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 197:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 196:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 195:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 194:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 193:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 192:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 191:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 190:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 189:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 188:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 187:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 186:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 179:
            return 'W**-2 m**4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 177:
            return 'W**-2 m**4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 169:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 167:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 120:
            return 'm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 119:
            return 'm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 118:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 79:
            return 'deg'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 74:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 73:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 72:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 60:
            return 'm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 59:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 58:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 57:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 45:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 44:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 43:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 30:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 29:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 28:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 15:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 14:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 13:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 122:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 121:
            return 'K'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 7:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 6:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 141:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 140:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 139:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 138:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 137:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 136:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 135:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 134:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 133:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 132:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 131:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 130:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 129:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 128:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 127:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 126:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 125:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 124:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 123:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 122:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 121:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 120:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 119:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 118:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 117:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 116:
            return 'K'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 115:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 114:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 193:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 254:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 253:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 252:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 251:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 250:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 249:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 248:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 247:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 246:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 245:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 244:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 243:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 242:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 241:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 240:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 239:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 238:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 237:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 236:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 235:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 234:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 233:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 232:
            return 'kg m**-2 s'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 231:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 230:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 229:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 228:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 227:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 226:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 225:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 224:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 223:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 222:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 221:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 220:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 219:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 218:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 217:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 216:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 215:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 214:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 212:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 211:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 210:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 209:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 208:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 207:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 206:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 205:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 204:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 203:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 202:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 201:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 200:
            return 'm**2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 199:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 198:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 197:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 196:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 195:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 194:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 193:
            return 'm**2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 192:
            return 'm**2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 191:
            return 'm**2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 190:
            return 'm**2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 189:
            return 's'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 188:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 187:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 186:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 185:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 184:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 183:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 182:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 181:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 180:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 179:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 178:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 177:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 176:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 175:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 174:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 173:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 172:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 171:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 170:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 169:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 167:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 166:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 165:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 164:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 162:
            return 'radians'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 159:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 158:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 157:
            return '%'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 156:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 155:
            return 's**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 154:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 153:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 152:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 151:
            return 'Pa'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 149:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 147:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 146:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 145:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 144:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 143:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 142:
            return 'm'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 141:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 140:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 139:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 138:
            return 's**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 137:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 136:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 135:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 134:
            return 'Pa'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 133:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 132:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 131:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 130:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 129:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 126:
            return 'Various'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 125:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 123:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 122:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 121:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 79:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 78:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 71:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 70:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 69:
            return 's m**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 68:
            return 's m**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 67:
            return 'm**2 m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 66:
            return 'm**2 m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 65:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 64:
            return 's'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 63:
            return 's'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 61:
            return 'Millimetres*100 + number of stations'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 60:
            return 'K m**2 kg**-1 s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 59:
            return 'J kg**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 58:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 57:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 56:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 55:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 54:
            return 'Pa'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 53:
            return 'm**2 s**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 52:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 51:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 50:
            return 's'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 49:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 48:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 47:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 46:
            return 's'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 45:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 44:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 43:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 42:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 41:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 40:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 39:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 38:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 37:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 36:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 35:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 34:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 33:
            return 'kg m**-3'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 32:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 31:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 29:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 28:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 27:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 26:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 23:
            return 's**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 21:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 14:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 13:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 12:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 11:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 5:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 4:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 3:
            return 'K'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 2:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 1:
            return 'm**2 s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 254:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 253:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 252:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 251:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 250:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 249:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 245:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 244:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 243:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 242:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 241:
            return '(-1 to 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 240:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 239:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 238:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 237:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 236:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 234:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 233:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 232:
            return 'kg m**-2 s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 231:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 230:
            return 'N m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 229:
            return 'N m**-2'

        unitsFactor = h.get_l('unitsFactor')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and unitsFactor == 1000:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 227:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 226:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 225:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 224:
            return 'kg kg**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 223:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 222:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 221:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 220:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 219:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 218:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 217:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 216:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 215:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 214:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 213:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 212:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 209:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 208:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 206:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 205:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 204:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 200:
            return 'm**2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 199:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 198:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 197:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 196:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 195:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 193:
            return 'm**2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 192:
            return 'm**2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 191:
            return 'm**2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 190:
            return 'm**2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 188:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 187:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 186:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 185:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 184:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 183:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 182:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 178:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 174:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 171:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 170:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 164:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 162:
            return 'radians'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 159:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 158:
            return 'Pa s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 154:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 153:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25 and typeOfFirstFixedSurface == 105:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 150:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 149:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 144:
            return 'm of water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10 and unitsFactor == 1000:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 142:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and unitsFactor == 1000:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 140:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 139:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 137:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 126:
            return 'Various'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 125:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 124:
            return 'dimensionless'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 123:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 79:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 78:
            return 'kg m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 74:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 73:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 72:
            return 'W m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 71:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 70:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 69:
            return 's m**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 68:
            return 's m**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 67:
            return 'm**2 m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 66:
            return 'm**2 m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 65:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 64:
            return 's'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 63:
            return 's'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 58:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 57:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 56:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 55:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 53:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 24 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and lengthOfTimeRange == 24 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 50:
            return 's'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 48:
            return 'N m**-2 s'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 47:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 46:
            return 's'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 45:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 44:
            return 'm of water equivalent'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 42:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 41:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 40:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 39:
            return 'm**3 m**-3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 38:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 37:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 36:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 35:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 32:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 29:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 28:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 27:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 26:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 23:
            return 's**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 21:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 20:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 19:
            return 'J m**-2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 18:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 17:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 16:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 15:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 14:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 13:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 12:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 11:
            return 'm s**-1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 9:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 8:
            return 'm'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 7:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 6:
            return '(0 - 1)'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 5:
            return 'K'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 4:
            return 'K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 85:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 100 and productDefinitionTemplateNumber == 9:
            return '%'

    return wrapped
