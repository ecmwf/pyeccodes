import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 235:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'W m-2 K-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 235:
            return 'Numeric'

        constituentType = h.get_l('constituentType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62101:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62200:
            return 'm-2s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62200:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62200:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62200:
            return 'd'

        typeOfGeneratingProcess = h.get_l('typeOfGeneratingProcess')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62200:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return '0-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62200:
            return '0-1'

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62200:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62200:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62200:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62300:
            return 'm-2s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62300:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62300:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62300:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62300:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return '0-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62300:
            return '0-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62300:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62300:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62300:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62100:
            return 'm-2s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62100:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62100:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62100:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62100:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return '0-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62100:
            return '0-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62100:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62100:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62100:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62101:
            return 'm-2s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62101:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62101:
            return 'd'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62101:
            return 'deg C'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return '0-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62101:
            return '0-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62101:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62101:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62101:
            return 'm-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'kgm-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 234:
            return 'Numeric'

        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 205 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'ms-1'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192 and typeOfStatisticalProcessing == 2:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 207 and typeOfStatisticalProcessing == 2:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 206 and typeOfStatisticalProcessing == 2:
            return 's-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 203:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 3:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 1:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 234:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'W m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 2:
            return 'K kg kg-1'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 1:
            return 'kg2 kg-2'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 0:
            return 'K2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 192 and typeOfFirstFixedSurface == 10:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 202:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 201:
            return 's-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 28:
            return 's-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 27:
            return 's-2'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 26:
            return 's-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 195 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 199:
            return 'm'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 198:
            return 'm'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 2:
            return 'K'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 233:
            return '%'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 12:
            return 'm s-1'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 11:
            return 'm s-1'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 10:
            return 'm s-1'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 9:
            return 'm s-1'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 8:
            return 'm s-1'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 7:
            return 'm s-1'

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 197 and typeOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 3:
            return 'Pa'

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2 '

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 2 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2 '

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2 '

        if discipline == 215 and parameterCategory == 19 and parameterNumber == 0:
            return 'klux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 194:
            return 'm'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 6:
            return 's'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 5:
            return 's'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 4:
            return 's'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 3:
            return 's'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 2:
            return 's'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 1:
            return 's'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 205:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 204:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 203:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 202:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 201:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 206 and typeOfFirstFixedSurface == 1:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 205 and typeOfStatisticalProcessing == 11 and typeOfFirstFixedSurface == 1:
            return 's'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'Numeric'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194 and typeOfFirstFixedSurface == 10:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 232:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 231:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 233:
            return 's-2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 232:
            return 's-2'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 29:
            return 's-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 231:
            return 's-2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 230:
            return 's-2'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 197:
            return 'm'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 196:
            return 'm'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 195:
            return 'm'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 194:
            return 'm'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 201:
            return 'W m-2'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 229:
            return '%'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 196:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 230 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 228:
            return 'm2/3 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 227:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 204:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 203:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 226:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 225:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 224:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 223:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 222:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 221:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 219:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 218:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 217:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 229:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 228:
            return 'kg-1'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 201:
            return 'Hz'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 200 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 220:
            return '%'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 193:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 197 and typeOfStatisticalProcessing == 1:
            return '0.01 m'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 196 and typeOfStatisticalProcessing == 1:
            return '0.01 m'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 195 and typeOfStatisticalProcessing == 1:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 194 and typeOfStatisticalProcessing == 1:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 193 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 216:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 215:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 214:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 213:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 212:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 211:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 198:
            return 'm'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 197:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 196:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 195:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 227:
            return 'm2 s-3'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 226:
            return 'm2/3 s-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 225:
            return 'm2/3 s-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 224:
            return 'm2/3 s-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 223:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 223 and typeOfStatisticalProcessing == 0:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 222:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 222 and typeOfStatisticalProcessing == 0:
            return '%'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 210 and typeOfFirstFixedSurface == 114:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 254:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 253:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 252:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 251:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 250:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 249:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 248:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 247:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 246:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 245:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 244:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 243:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 242:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 241:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 240:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 239:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 238:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 237:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 236:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 235:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 234:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 233:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 232:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 231:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 230:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 229:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 228:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 227:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 226:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 225:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 224:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 223:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 222:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 221:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 220:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 219:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 218:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 217:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 216:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 215:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 214:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 213:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 212:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 211:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 210:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 209:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 208:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 207:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 206:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 205:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 204:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 203:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 202:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 201:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 200:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 199:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 198:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 197:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 196:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 195:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 194:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 193:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 192:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 191:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 190:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 189:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 188:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 187:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 186:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 185:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 184:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 183:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 182:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 181:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 180:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 179:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 178:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 177:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 176:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 175:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 174:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 173:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 172:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 171:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 170:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 169:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 168:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 167:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 166:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 165:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 164:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 163:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 162:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 161:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 160:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 159:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 158:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 157:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 156:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 155:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 154:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 153:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 152:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 151:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 150:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 149:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 148:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 147:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 146:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 145:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 144:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 143:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 142:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 141:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 140:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 139:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 138:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 137:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 136:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 135:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 134:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 133:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 132:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 131:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 130:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 129:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 128:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 127:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 126:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 125:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 124:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 123:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 122:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 121:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 120:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 119:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 118:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 117:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 116:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 115:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 114:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 113:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 112:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 111:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 110:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 109:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 108:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 107:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 106:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 105:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 104:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 103:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 102:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 101:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 100:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 99:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 98:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 97:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 96:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 95:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 94:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 93:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 92:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 91:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 90:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 89:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 88:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 87:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 86:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 85:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 84:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 83:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 82:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 81:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 80:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 79:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 78:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 77:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 76:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 75:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 74:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 73:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 72:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 71:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 70:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 69:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 68:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 67:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 66:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 65:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 64:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 63:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 62:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 61:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 60:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 59:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 58:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 57:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 56:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 55:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 54:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 53:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 52:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 51:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 50:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 49:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 48:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 47:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 46:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 45:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 44:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 43:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 42:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 41:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 40:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 39:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 38:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 37:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 36:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 35:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 34:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 33:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 32:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 31:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 30:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 29:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 28:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 27:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 26:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 25:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 24:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 23:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 22:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 21:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 20:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 19:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 18:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 17:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 16:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 15:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 14:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 13:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 12:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 11:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 10:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 9:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 8:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 7:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 6:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 5:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 4:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 3:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 2:
            return 0

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 1:
            return 0

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 252:
            return 'm-3'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 251:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 74:
            return 'm-3'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 73:
            return 'm-3'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 72:
            return 'm-3'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 35:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 34:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 33:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 197:
            return 'm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 200:
            return 's m-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 218:
            return 'm2 s-3'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 219:
            return 'm2 s-3'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 221:
            return 'm2 s-3'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 220:
            return 'm2 s-3'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 14 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 13 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 12 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 10 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 9 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 8 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 7 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 6 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 5 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 4 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 3 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 2 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 1 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 209 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 217:
            return '10-7 s-2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 216:
            return 'm2/3 s-1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 198 and typeOfGeneratingProcess == 6:
            return 'kg2 m-4'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197 and typeOfGeneratingProcess == 6:
            return 'kg2 m-4'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 195:
            return 'Pa-3h'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 192:
            return 'C'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 192:
            return 's2 m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 202:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 22:
            return 's-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 21:
            return 'Km kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 20:
            return 'm kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 19:
            return 'm kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 18:
            return 'm2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 17:
            return 'm kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 16:
            return 'K2 m-2 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 15:
            return 'm kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 14:
            return 'm kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 13:
            return 'm2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 12:
            return 'm2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 11:
            return 'm kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 10:
            return 'm2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 9:
            return 'm2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 8:
            return 'm kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 7:
            return 's-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 23:
            return 'K m2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 199:
            return 's-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 198:
            return 's-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 192:
            return 'K'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 192:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 209:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208 and typeOfGeneratingProcess == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207 and typeOfGeneratingProcess == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208 and typeOfGeneratingProcess == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207 and typeOfGeneratingProcess == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206 and typeOfGeneratingProcess == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205 and typeOfGeneratingProcess == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204 and typeOfGeneratingProcess == 0:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203 and typeOfGeneratingProcess == 0:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202 and typeOfGeneratingProcess == 0:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201 and typeOfGeneratingProcess == 0:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200 and typeOfGeneratingProcess == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199 and typeOfGeneratingProcess == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198 and typeOfGeneratingProcess == 0:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197 and typeOfGeneratingProcess == 0:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196 and typeOfGeneratingProcess == 0:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195 and typeOfGeneratingProcess == 0:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206 and typeOfGeneratingProcess == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205 and typeOfGeneratingProcess == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204 and typeOfGeneratingProcess == 2:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203 and typeOfGeneratingProcess == 2:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202 and typeOfGeneratingProcess == 2:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201 and typeOfGeneratingProcess == 2:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200 and typeOfGeneratingProcess == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199 and typeOfGeneratingProcess == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198 and typeOfGeneratingProcess == 2:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197 and typeOfGeneratingProcess == 2:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196 and typeOfGeneratingProcess == 2:
            return 'hft'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195 and typeOfGeneratingProcess == 2:
            return 'hft'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 3:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 201:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 194 and typeOfStatisticalProcessing == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 197:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 196:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 195:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 236 and typeOfStatisticalProcessing == 3 and typeOfGeneratingProcess == 5:
            return 'K'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 232 and typeOfStatisticalProcessing == 3 and typeOfGeneratingProcess == 5:
            return 'K'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 213 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 212 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 199 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 198 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 197 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 191 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 139 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 138 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 137 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 136 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 134 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 132 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 77 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 75 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 74 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 72 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 71 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 70 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 69 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 32 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 29 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 26 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 17 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 14 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 3 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'kg m2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 6:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 5:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 25 and typeOfFirstFixedSurface == 107:
            return 'K m2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 4:
            return 'm2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 3:
            return 's-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 2:
            return 'm3 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 1:
            return 'm3 kg-1 s-1'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 0:
            return 's-2'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 24 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 194:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 197:
            return 's-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfStatisticalProcessing == 0:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 194:
            return 'm'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 193:
            return 'm'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 192:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193:
            return 's-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 's-1 m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207:
            return 's-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193:
            return 'Pa'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192:
            return 'Pa'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 199:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195:
            return 'm s-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194:
            return 'm s-2'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 3 and typeOfGeneratingProcess == 7:
            return 'm2 s-2'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 2 and typeOfGeneratingProcess == 7:
            return 'm2 s-2'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 5 and typeOfGeneratingProcess == 7:
            return 'gpm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206:
            return 's-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205 and typeOfFirstFixedSurface == 2:
            return 'kg m-2 s-1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'W m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193:
            return 'K s-1'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 192:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 'm2 s-3'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 192:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 192:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 193:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 193:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 's-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 's-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202:
            return 'kg kg-1 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201:
            return 'kg kg-1 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200:
            return 'kg kg-1 s-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'K s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199:
            return 'kg kg-1 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198:
            return 'kg kg-1 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 4:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193:
            return 'm s-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192:
            return 'm s-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197:
            return 'kg kg-1 s-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192:
            return 'K s-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 's m-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 106:
            return 'W m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192:
            return 'K s-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192:
            return 'K s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26 and typeOfStatisticalProcessing == 2:
            return 'kg kg-1 s-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 25:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 25:
            return 'Pa'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62200:
            return 'kgm-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return '%'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62200:
            return 'm-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62300:
            return 'kgm-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return '%'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62300:
            return 'm-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62100:
            return 'kgm-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return '%'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62100:
            return 'm-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62101:
            return 'kgm-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return '%'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62101:
            return 'm-3'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'ms-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'ms-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '%'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 's-1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5 and typeOfGeneratingProcess == 8:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 81 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 81 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 20 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 26315:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 15 and typeOfStatisticalProcessing == 2:
            return 'm2 s-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 23:
            return 'm'

        modeNumber = h.get_l('modeNumber')
        typeOfDistributionFunction = h.get_l('typeOfDistributionFunction')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 8:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 8:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 8:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 8:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 8:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 8:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 24:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 22 and constituentType == 62001:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 22 and constituentType == 62025:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 21 and constituentType == 62001:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 21 and constituentType == 62025:
            return 'm'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 17 and typeOfFirstFixedSurface == 10:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 99:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 39:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 38:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 98:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 97:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 96:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 107:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 106:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 105:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 103:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 102:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 101:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 104:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 100:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 116:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 113:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 110:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 8:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 'kg kg-1 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 4:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 4:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 4:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 4:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and constituentType == 62025:
            return 'kg m-3'

        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 20000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10000 and constituentType == 62025:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 38500 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 20000 and constituentType == 62025:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 70000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 38500 and constituentType == 62025:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 24000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 9100 and constituentType == 62025:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 101325 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 70000 and constituentType == 62025:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 46500 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 24000 and constituentType == 62025:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 15:
            return 'Bq m-3'

        aerosolType = h.get_l('aerosolType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62008:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62001:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62025:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 62 and constituentType == 62025:
            return 'm'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and typeOfFirstFixedSurface == 10 and constituentType == 62025:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 101325 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 46500 and constituentType == 62025:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 0 and constituentType == 62025:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30102:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30175:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30139:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30138:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30161:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30079:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30129:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30141:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30172:
            return 'Bq kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 6 and typeOfDistributionFunction == 1:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 5 and typeOfDistributionFunction == 1:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 4 and typeOfDistributionFunction == 1:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 1:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 1:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 1:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 42:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 41:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 21:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 27 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 27:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 3:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10 and typeOfFirstFixedSurface == 10:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 13:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 17:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 94:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 5:
            return 'm'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 44:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 43:
            return 0

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 3000:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 16:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'M'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 31:
            return 'm-3'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 30:
            return 'm-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 73 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 14:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 13:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 12:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 11:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 10:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 9:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 73:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 72:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 71:
            return 'kg kg-1'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 20:
            return 0

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 23:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 24:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 44:
            return 0

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 43:
            return 0

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 45:
            return 's-1'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 33:
            return 'degree'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 30:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 27:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 32:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 29:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 26:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 19:
            return '%'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 16:
            return 'Numeric'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 17:
            return 'm s-1'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 35:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfStatisticalProcessing == 0:
            return 'W m-2'

        numberOfGridInReference = h.get_l('numberOfGridInReference')

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and numberOfGridInReference == 2 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 'kg m-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 36:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'Pa'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'W m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 'kg m-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'J'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'W m-1 s-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'W m-1 s-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'J m-2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 's-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 'm s-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 'm s-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 'm s-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'm s-1'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'Degree true'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 'kg kg-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 'K'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'kg m-2'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'm s-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 's-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 's-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'm2 s-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 'Pa'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return 'DBZ_MAX'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return 'DBZ_MAX'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'm'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 's'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'Degree true'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return 's-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 'Degree'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 'm s-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 'm s-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 'table 4.21C.t.h.q.i.'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 'kg m-2 s-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 16:
            return 'm3 m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 15:
            return 'm3 m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 14:
            return 'kg m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 13:
            return 'm3 m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12:
            return 'kg m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 11:
            return 'm3 m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 10:
            return 'm3 m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 9:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 8:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 7:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 5:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 4:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 3:
            return 'kg m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 2:
            return 'kg m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 1:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 'm3 m-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 'm3 m-3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 'W m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 'm s-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 'kg m-2 s-1'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 10:
            return 'W m-2 '

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 'table (4.2 Land use)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 'kg-2 s-1'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return '%'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg m-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 'kg m-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 'kg m-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return '%'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return 'table 4.2 E.e.s.c.t.'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return 'table 4.2 R.s.s.c.'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 'kg m-2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 's'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 17:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 'table (4.2 C.e.t.)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 'table (4.2 C. i.)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 'table (4.2 P.b.l.r.)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 'table (4.2 Turb.)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 6:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 5:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 'table (4.2 Volc.ash)'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 8:
            return 'Bq s m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 7:
            return 'Bq s m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 6:
            return 'Bq s m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 5:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 4:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 3:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 2:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 1:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 0:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 'dB'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 'kg m-1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'code table (4.2)'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 21:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 19:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 18:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 17:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 16:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 15:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 10:
            return 'code table (4.2 )'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 9:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 8:
            return 'code table (4.2)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 'W m-2 '

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 'N m-2 '

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 'N m-2 '

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 14:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 'm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'ms-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 'ms-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'ms-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return ' m s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 48:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 47:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'proportion'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return 'Code table 4.2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 'code table (4.2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 29:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 28:
            return 'kg kg-1m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 27:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 21:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 20:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 19:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 17:
            return 'd'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'K'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 's'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 's-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 's-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 1:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 80000:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 80000 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 40000:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 40000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return '%'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'm2 s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'm2 s-1'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 12:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 114:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 114:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 114:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18 and typeOfFirstFixedSurface == 114:
            return 'K'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 29:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 28:
            return 'kg-1'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 2:
            return 'deg E'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 2:
            return 'deg N'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 3:
            return 'deg E'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 3:
            return 'deg N'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 1:
            return 'deg E'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 1:
            return 'deg N'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18 and typeOfStatisticalProcessing == 0:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 'K m-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'm s-1'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'degree true'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 35:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 34:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 26:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 33 and typeOfStatisticalProcessing == 1:
            return 's'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 50 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 7:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 7 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25:
            return 'Pa'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 's-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'gpm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'kg m-3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 19:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 4:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'K m2 kg-1 s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 's-1'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 'm'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 3 and typeOfSecondFixedSurface == 165 and typeOfFirstFixedSurface == 162:
            return 'm'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 4 and typeOfFirstFixedSurface == 165:
            return 'K'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 10 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 166:
            return 'Numeric'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 0 and typeOfSecondFixedSurface == 166 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 162:
            return 'K'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfSecondFixedSurface == 166 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 4 and typeOfFirstFixedSurface == 164:
            return 'K'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 3 and typeOfSecondFixedSurface == 164 and typeOfFirstFixedSurface == 162:
            return 'm'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 11 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'm-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 33:
            return 'm'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 0 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 2:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 's-1'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'K'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0 and typeOfStatisticalProcessing == 1:
            return 'DU'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50 and typeOfStatisticalProcessing == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8 and typeOfGeneratingProcess == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8 and typeOfGeneratingProcess == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 4:
            return 'kg m-2'

        satelliteSeries = h.get_l('satelliteSeries')
        satelliteNumber = h.get_l('satelliteNumber')
        instrumentType = h.get_l('instrumentType')
        scaledValueOfCentralWaveNumber = h.get_l('scaledValueOfCentralWaveNumber')

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 83333:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1250000:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1666666:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 625000:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 2000000:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 198:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 198:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 198:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'm s-1'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 197:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 197:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 197:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400 and typeOfGeneratingProcess == 197:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800 and typeOfGeneratingProcess == 197:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfGeneratingProcess == 197:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 197:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'W m sr m-2'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'K'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Pa s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Pa s-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return '%'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'm2 s-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'm2 s-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Pa'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 107:
            return 'Pa'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 25:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 's-1'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51 and typeOfStatisticalProcessing == 2:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30175:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30175:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30175:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30139:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30139:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30139:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30138:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30138:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30138:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30161:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30161:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30161:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30000:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30000:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30000:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30059:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30059:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30059:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30079:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30079:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30079:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30129:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30129:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30129:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30172:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30172:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30172:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30141:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30141:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30141:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30067:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30067:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30067:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30102:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30102:
            return 'Bq m-2'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30102:
            return 'Bq m-3'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2:
            return 'deg E'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1:
            return 'deg N'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62008:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62008:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62009:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62009:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62010:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62010:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62001:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62001:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62006:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62006:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 2:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 0:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 30:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 29:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 3:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 2:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 3:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 2:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 32:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21:
            return 'rad'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 31:
            return 'degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 25:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 35:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 36:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'degree true'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 'dBZ'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'dBZ'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 's m-1'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18:
            return 'K'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106:
            return 'K'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 19:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20:
            return 'm2 s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 31:
            return 'm2 s-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 24:
            return 'J kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77:
            return 'kg m-2 s-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 4:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 78:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 74:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return '%'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'N m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 8:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 8:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'W m-2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'degree coming from'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 10:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return '%'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 100 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 10:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 10 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 190 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 100:
            return 'kg m-2'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 9:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 41:
            return 'K'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 36:
            return 'K'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfStatisticalProcessing == 0:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'kg kg-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'Pa s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'degree true'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'degree true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'Numeric'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'Numeric'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 9:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 'DU'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 1:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'm2 s-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfSecondFixedSurface == 105 and typeOfFirstFixedSurface == 105:
            return 'm2 s-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'm2 s-2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'Pa s-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Pa'

    return wrapped
