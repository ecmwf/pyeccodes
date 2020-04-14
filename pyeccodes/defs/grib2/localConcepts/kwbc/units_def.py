import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 8:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return '%'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 224:
            return 'm**2 s**-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 234:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 201:
            return 's'

        if discipline == 255 and parameterCategory == 255 and parameterNumber == 255:
            return '~'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 197:
            return 'Jm-2'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 196:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 195:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 194:
            return 'J kg**-1'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 193:
            return '~'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 192:
            return 'deg C'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 202:
            return 'kg (m**2 s**-1)**-1'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 201:
            return 'J kg**-1'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 200:
            return 'psuperday'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 199:
            return 'degreeperday'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 198:
            return 'W m**-2'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 197:
            return 'W m**-2'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 196:
            return 'kg m**-3'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 195:
            return 'm'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 194:
            return 'm'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 193:
            return 'm'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 192:
            return 'm'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 195:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 194:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 193:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 192:
            return 'm s**-1'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 192:
            return '~'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 193:
            return 'm s**-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 192:
            return 'm s**-1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 203:
            return 'Fraction'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 202:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 201:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 200:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 199:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 198:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'Index'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 230:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 229:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 228:
            return 'm s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 227:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 226:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 225:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 224:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 223:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 222:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 221:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 220:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 219:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 218:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 217:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 216:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 215:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 214:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 213:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 212:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 211:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 210:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 209:
            return 'm s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 208:
            return 'm s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 207:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 206:
            return '~'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 201:
            return 'Fraction'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'Integer(0-13)'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 195:
            return '%'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 194:
            return '%'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 192:
            return '%'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 197:
            return 'deg'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 196:
            return 'deg'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 195:
            return '~'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 193:
            return 'deg'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 192:
            return 'deg'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 232:
            return 'log10(kg m**-3)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 219:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 218:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 217:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 216:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 215:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 214:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 213:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 212:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 211:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 210:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 209:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205:
            return '~'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204:
            return 'Integer'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203:
            return 'categorical'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196:
            return 'categorical'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195:
            return 'categorical'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 194:
            return 'categorical'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192:
            return 'dimensionless'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 196:
            return 'dB'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 195:
            return 'dB'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 194:
            return 'mm**6 m**-3'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 193:
            return 'mm**6 m**-3'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 192:
            return 'mm**6 m**-3'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 199:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 198:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 197:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 196:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 195:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 194:
            return 'dimensionless'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193:
            return 'ppb'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195:
            return 'log10((10**-6g) m**-3)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194:
            return 'log10((10**-6g) m**-3)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193:
            return '(10**-6 g) m**-3'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192:
            return '(10**-6 g) m**-3'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 198:
            return '~'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 197:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return '~'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 200:
            return 'Pa s**-1'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 197:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 196:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 195:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 194:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 205:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 204:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 203:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 202:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 201:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 200:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 197:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 196:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 195:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 194:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 212:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 211:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 210:
            return '~'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 209:
            return 'kg (m**2 s-1)**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 208:
            return 'kg (m**2 s-1)**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 207:
            return 'kg (m**2 s-1)**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 206:
            return 'ln(kPa)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 205:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 204:
            return 'm**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 203:
            return 'm**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 202:
            return 'm**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 201:
            return 'm**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 200:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 199:
            return 'Pa s**-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 198:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'Pa'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 219:
            return '(s m**-1)**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 218:
            return '~'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 217:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 216:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 215:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 214:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 213:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 212:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 211:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 210:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 209:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 208:
            return 'm s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 207:
            return 'K m s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 206:
            return 'K m s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 205:
            return 'm**2 s**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 204:
            return 'm**2 s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 203:
            return 'deg'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 202:
            return 'deg'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 201:
            return 'deg'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 200:
            return 'deg'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 199:
            return 'deg'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 198:
            return 'deg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 225:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 224:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 223:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 222:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 221:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 220:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 219:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 218:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 217:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 216:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 215:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 214:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 213:
            return 'kg (kg s**-1)**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 212:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 211:
            return 'cm per day'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 210:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 209:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207:
            return 'dimensionless'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206:
            return 'dimensionless'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198:
            return '%'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 204:
            return 'J m**-2 K**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 203:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 202:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 201:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 200:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 199:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 198:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 197:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 196:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 195:
            return 'K s**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return '~'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'K s**-1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 204:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 205:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 203:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 202:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 200:
            return 's m**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'm s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'kg m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 'kg m**-2 s**-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193:
            return 'W m**-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192:
            return 'Proportion'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 193:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 192:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 194:
            return 's'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return '%'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 197:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193:
            return 'J kg**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192:
            return '%'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 193:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 196:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 197:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 196:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 195:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193:
            return 'gpm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 197:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194:
            return 'm s**-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193:
            return 'N m**-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192:
            return 's**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204:
            return 'kg m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199:
            return 'kg m**-2'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 193:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196:
            return 'kg m**-2 s**-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195:
            return '(Code table 4.222)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194:
            return '(Code table 4.222)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193:
            return '(Code table 4.222)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192:
            return '(Code table 4.222)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197:
            return 'kg kg**-1 s**-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195:
            return 'kg kg**-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192:
            return 'W m**-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'J kg**-1'

    return wrapped
