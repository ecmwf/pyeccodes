import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 207 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 207 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 207 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 206 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 206 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 'K'

        if table2Version == 206 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 206 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 206 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 206 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 206 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 206 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 206 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 206 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 206 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if table2Version == 206 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'K'

        if table2Version == 206 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'K'

        if table2Version == 206 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        localElementNumber = h.get_l('localElementNumber')

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 4:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 3:
            return 'W m sr m**-2'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 1:
            return 'K'

        if table2Version == 204 and indicatorOfParameter == 16:
            return 'J kg**-1'

        if table2Version == 204 and indicatorOfParameter == 15:
            return 'J kg**-1'

        if table2Version == 204 and indicatorOfParameter == 14:
            return 'Pa s**-1'

        if table2Version == 204 and indicatorOfParameter == 13:
            return 'Pa s**-1'

        if table2Version == 204 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 204 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 204 and indicatorOfParameter == 10:
            return '%'

        if table2Version == 204 and indicatorOfParameter == 9:
            return '%'

        if table2Version == 204 and indicatorOfParameter == 8:
            return 'm**2 s**-2'

        if table2Version == 204 and indicatorOfParameter == 7:
            return 'm**2 s**-2'

        if table2Version == 204 and indicatorOfParameter == 6:
            return 'm s**-1'

        if table2Version == 204 and indicatorOfParameter == 5:
            return 'm s**-1'

        if table2Version == 204 and indicatorOfParameter == 4:
            return 'm s**-1'

        if table2Version == 204 and indicatorOfParameter == 3:
            return 'm s**-1'

        if table2Version == 204 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 204 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 203 and indicatorOfParameter == 204 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 203 and indicatorOfParameter == 203 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 203 and indicatorOfParameter == 196 and indicatorOfTypeOfLevel == 100:
            return '~'

        if table2Version == 203 and indicatorOfParameter == 157 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 100:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 140 and indicatorOfTypeOfLevel == 1:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 100:
            return 'Pa'

        if table2Version == 203 and indicatorOfParameter == 132 and indicatorOfTypeOfLevel == 100:
            return 'm s**-1'

        if table2Version == 203 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 100:
            return 'm s**-1'

        if table2Version == 203 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 100:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 203 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 100:
            return 'm**2 kg**-1 s**-1'

        if table2Version == 203 and indicatorOfParameter == 109 and indicatorOfTypeOfLevel == 100:
            return 's**-1'

        if table2Version == 203 and indicatorOfParameter == 107 and indicatorOfTypeOfLevel == 101:
            return 'm**3 kg**-1 s**-1'

        if table2Version == 203 and indicatorOfParameter == 103 and indicatorOfTypeOfLevel == 101:
            return 'm**3 kg**-1 s**-1'

        if table2Version == 203 and indicatorOfParameter == 101 and indicatorOfTypeOfLevel == 100:
            return 's**-2'

        if table2Version == 203 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 203 and indicatorOfParameter == 94 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 203 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 100:
            return 's**-2'

        if table2Version == 203 and indicatorOfParameter == 30 and indicatorOfTypeOfLevel == 110:
            return 'J kg**-1'

        if table2Version == 203 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 110:
            return 'm s**-1'

        if table2Version == 202 and indicatorOfParameter == 248 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'W m**-2'

        if table2Version == 202 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 202 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'N m**-2'

        if table2Version == 202 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'N m**-2'

        if table2Version == 202 and indicatorOfParameter == 231 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'N m**-2'

        if table2Version == 202 and indicatorOfParameter == 231 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'N m**-2'

        if table2Version == 202 and indicatorOfParameter == 229 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 228 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 227:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 226 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 225 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 224:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 223 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 222 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 221:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 220 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 219 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 218:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 217 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 216 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 215:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 214 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 213 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 212:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 211 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 210 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 209:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 208 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 207 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 206:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 205 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 204 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 203:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 202 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 201 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 200:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 197:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 196 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 195 and indicatorOfTypeOfLevel == 1:
            return 'Bq m**-2'

        if table2Version == 202 and indicatorOfParameter == 194:
            return 'Bq m**-3'

        if table2Version == 202 and indicatorOfParameter == 180 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 202 and indicatorOfParameter == 123 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 120 and indicatorOfTypeOfLevel == 110:
            return 'm s**-1'

        if table2Version == 202 and indicatorOfParameter == 115 and indicatorOfTypeOfLevel == 1:
            return 'Degree E'

        if table2Version == 202 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 1:
            return 'Degree N'

        if table2Version == 202 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 1:
            return 's**-1'

        if table2Version == 202 and indicatorOfParameter == 105 and indicatorOfTypeOfLevel == 1:
            return 's**-1 m**-2'

        if table2Version == 202 and indicatorOfParameter == 104 and indicatorOfTypeOfLevel == 110:
            return 's**-1'

        if table2Version == 202 and indicatorOfParameter == 93 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 93:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 92 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 92:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 91 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 91:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 86 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 86:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 84:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 78 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 77 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 76 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return '~'

        topLevel = h.get_l('topLevel')
        bottomLevel = h.get_l('bottomLevel')

        if table2Version == 202 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and bottomLevel == 100:
            return 'kg**2 m**-4'

        if table2Version == 202 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 'kg**2 m**-4'

        if table2Version == 202 and indicatorOfParameter == 71:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 70 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 67 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

        if table2Version == 202 and indicatorOfParameter == 64 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

        if table2Version == 202 and indicatorOfParameter == 62 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 56 and indicatorOfTypeOfLevel == 1 and level == 0 and timeRangeIndicator == 0:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 49 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 48 and indicatorOfTypeOfLevel == 1:
            return 'radians'

        if table2Version == 202 and indicatorOfParameter == 47 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 202 and indicatorOfParameter == 46 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 45 and indicatorOfTypeOfLevel == 110:
            return 'm s**-1'

        if table2Version == 202 and indicatorOfParameter == 44 and indicatorOfTypeOfLevel == 110:
            return 'm s**-1'

        if table2Version == 202 and indicatorOfParameter == 42 and level == 100:
            return 'm**2 s**-2'

        if table2Version == 202 and indicatorOfParameter == 41 and indicatorOfTypeOfLevel == 100:
            return 'm**2 s**-2'

        if table2Version == 202 and indicatorOfParameter == 40 and indicatorOfTypeOfLevel == 100:
            return 'gpm'

        if table2Version == 202 and indicatorOfParameter == 19:
            return 'Degree true'

        if table2Version == 202 and indicatorOfParameter == 18:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 17:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 10:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 9:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 8:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 102:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 7:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 102:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 4:
            return 'Degree true'

        if table2Version == 201 and indicatorOfParameter == 243 and indicatorOfTypeOfLevel == 1:
            return 's**-1'

        if table2Version == 201 and indicatorOfParameter == 241 and indicatorOfTypeOfLevel == 1:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 240 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 239:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'W m**-2'

        if table2Version == 201 and indicatorOfParameter == 237:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 236:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 110:
            return 'K s**-1'

        if table2Version == 201 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 110:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200:
            return 'dB'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 110:
            return 'dB'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 1:
            return 'dB'

        if table2Version == 201 and indicatorOfParameter == 215 and indicatorOfTypeOfLevel == 1:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 212 and indicatorOfTypeOfLevel == 1:
            return 's m**-1'

        if table2Version == 201 and indicatorOfParameter == 203 and indicatorOfTypeOfLevel == 1:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 200 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 111:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 111:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 197 and indicatorOfTypeOfLevel == 111:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 194 and indicatorOfTypeOfLevel == 100:
            return 'Bq m**-3'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10 and timeRangeIndicator == 2:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 173 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 171 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 170 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 109:
            return 'm**2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 153 and indicatorOfTypeOfLevel == 109:
            return 'm**2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 152 and indicatorOfTypeOfLevel == 109:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 149 and indicatorOfTypeOfLevel == 110:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 148 and indicatorOfTypeOfLevel == 109:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 147:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 146 and indicatorOfTypeOfLevel == 1:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 145 and indicatorOfTypeOfLevel == 1:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 144 and indicatorOfTypeOfLevel == 1:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 143 and indicatorOfTypeOfLevel == 1:
            return 'J kg**-1'

        if table2Version == 201 and indicatorOfParameter == 142 and indicatorOfTypeOfLevel == 1:
            return 's**-1'

        if table2Version == 201 and indicatorOfParameter == 141 and indicatorOfTypeOfLevel == 1:
            return 's**-1'

        if table2Version == 201 and indicatorOfParameter == 139 and indicatorOfTypeOfLevel == 110:
            return 'Pa'

        if table2Version == 201 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-3'

        if table2Version == 201 and indicatorOfParameter == 132 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1 s**-1'

        if table2Version == 201 and indicatorOfParameter == 129 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 127 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1 s**-1'

        if table2Version == 201 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1 s**-1'

        if table2Version == 201 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 110:
            return 'K s**-1'

        if table2Version == 201 and indicatorOfParameter == 123 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 102 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 101 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 100 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2 s**-1'

        if table2Version == 201 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 89 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1 s**-1'

        if table2Version == 201 and indicatorOfParameter == 88 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1 s**-1'

        if table2Version == 201 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 4:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 4:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 82 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 110:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 110:
            return 'm s**-1'

        if table2Version == 201 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1 s**-1'

        if table2Version == 201 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 110:
            return 'K s**-1'

        if table2Version == 201 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 3:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 2:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 59 and indicatorOfTypeOfLevel == 3:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 2:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 53:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 52:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 51:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 44 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 43 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 42 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 41 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 40:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 39 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 38 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 37 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 201 and indicatorOfParameter == 36 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 35 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 110:
            return 'kg kg**-1'

        if table2Version == 201 and indicatorOfParameter == 30 and indicatorOfTypeOfLevel == 110:
            return '%'

        if table2Version == 201 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 110:
            return '%'

        if table2Version == 201 and indicatorOfParameter == 21 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 's m**-1'

        if table2Version == 201 and indicatorOfParameter == 20 and timeRangeIndicator == 4:
            return '~'

        if table2Version == 201 and indicatorOfParameter == 19 and indicatorOfTypeOfLevel == 111 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 201 and indicatorOfParameter == 18 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 201 and indicatorOfParameter == 14 and indicatorOfTypeOfLevel == 110:
            return 'K s**-1'

        if table2Version == 201 and indicatorOfParameter == 13 and indicatorOfTypeOfLevel == 110:
            return 'K s**-1'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'W m**-2'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'N m**-2'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'N m**-2'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 0:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 0:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 92 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and bottomLevel == 10 and timeRangeIndicator == 4 and topLevel == 0:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and timeRangeIndicator == 4 and topLevel == 10 and bottomLevel == 190:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and timeRangeIndicator == 4 and topLevel == 10 and bottomLevel == 100:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 87 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 100 and topLevel == 10:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 190 and topLevel == 100:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 9:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 41:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 36:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 83 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 81 and indicatorOfTypeOfLevel == 1:
            return '(0 - 1)'

        if table2Version == 2 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 76 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 110:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 66 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 63 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 62 and timeRangeIndicator == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'kg m**-2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 54 and indicatorOfTypeOfLevel == 1:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'kg kg**-1'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'kg kg**-1'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 1:
            return 'kg kg**-1'

        if table2Version == 2 and indicatorOfParameter == 40:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'Pa s**-1'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 110:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 110:
            return 'degrees'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'degrees'

        if table2Version == 2 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 28:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 21 and indicatorOfTypeOfLevel == 1:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 10 and indicatorOfTypeOfLevel == 1:
            return 'Dobson'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 109:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'm**2 s**-2'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 110:
            return 'm**2 s**-2'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 1:
            return 'm**2 s**-2'

        if table2Version == 2 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 1:
            return 'Pa s**-1'

        if table2Version == 2 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 102:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

    return wrapped
