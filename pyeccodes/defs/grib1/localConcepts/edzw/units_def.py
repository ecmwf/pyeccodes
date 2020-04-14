import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 202 and indicatorOfParameter == 39:
            return 'W m-2 K-1'

        if table2Version == 202 and indicatorOfParameter == 37:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 36:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 's-1'

        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200 and timeRangeIndicator == 2:
            return 'dBZ'

        if table2Version == 201 and indicatorOfParameter == 196 and timeRangeIndicator == 2:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 234:
            return 'dBZ'

        if table2Version == 201 and indicatorOfParameter == 235:
            return 'dBZ'

        if table2Version == 201 and indicatorOfParameter == 48 and indicatorOfTypeOfLevel == 200 and timeRangeIndicator == 2:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 49 and timeRangeIndicator == 2:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 37 and timeRangeIndicator == 2:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 36 and timeRangeIndicator == 2:
            return 's-1'

        if table2Version == 203 and indicatorOfParameter == 35 and timeRangeIndicator == 2:
            return 'm2s-2'

        if table2Version == 201 and indicatorOfParameter == 196:
            return 'J kg-1'

        if table2Version == 202 and indicatorOfParameter == 34:
            return 'W m-2'

        if table2Version == 202 and indicatorOfParameter == 33:
            return 'Proportion'

        if table2Version == 201 and indicatorOfParameter == 196:
            return 'J kg-1'

        if table2Version == 3 and indicatorOfParameter == 149:
            return 0

        if table2Version == 3 and indicatorOfParameter == 148:
            return 0

        if table2Version == 201 and indicatorOfParameter == 25 and timeRangeIndicator == 4:
            return 'W m-2 '

        if table2Version == 201 and indicatorOfParameter == 25 and timeRangeIndicator == 3:
            return 'W m-2 '

        if table2Version == 201 and indicatorOfParameter == 25:
            return 'W m-2 '

        if table2Version == 3 and indicatorOfParameter == 162:
            return 0

        if table2Version == 3 and indicatorOfParameter == 152:
            return 0

        if table2Version == 3 and indicatorOfParameter == 151:
            return 0

        if table2Version == 3 and indicatorOfParameter == 207:
            return 0

        if table2Version == 3 and indicatorOfParameter == 140:
            return 0

        if table2Version == 3 and indicatorOfParameter == 138:
            return 0

        if table2Version == 3 and indicatorOfParameter == 40:
            return 'm s-1'

        if table2Version == 202 and indicatorOfParameter == 120:
            return 0

        if table2Version == 250 and indicatorOfParameter == 20:
            return '%'

        if table2Version == 202 and indicatorOfParameter == 233 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 204 and indicatorOfParameter == 46:
            return '0.01 m'

        if table2Version == 203 and indicatorOfParameter == 77:
            return '0.01 m'

        if table2Version == 203 and indicatorOfParameter == 76:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 75:
            return 1

        if table2Version == 203 and indicatorOfParameter == 73:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 72:
            return 'kg m-2'

        if table2Version == 202 and indicatorOfParameter == 232 and timeRangeIndicator == 1:
            return 'N m-2'

        if table2Version == 202 and indicatorOfParameter == 231 and timeRangeIndicator == 1:
            return 'N m-2'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1:
            return 'N m-2'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1:
            return 'N m-2'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 151:
            return 'm2 s-3'

        if table2Version == 203 and indicatorOfParameter == 71:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'm2 2-1'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'm2 s-1'

        if table2Version == 3 and indicatorOfParameter == 98:
            return 's-1'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 's-1'

        if table2Version == 2 and indicatorOfParameter == 98:
            return 's-1'

        if table2Version == 2 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'gpm'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 0

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'J'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'N m-2'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'N m-2'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 0

        if table2Version == 1 and indicatorOfParameter == 119:
            return 0

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'W m-2'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'W m-2'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'W m-2'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'W m-2'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'W m-2'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'w m-2'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'w m-2'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'degree true'

        if table2Version == 1 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 104:
            return 'degree coming from'

        if table2Version == 1 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 101:
            return 'degree true'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 97:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 96:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 95:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 94:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 93:
            return 'degree true'

        if table2Version == 1 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 91:
            return 'Proportion'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'kg m-3'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 0

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'kg m-2 s-1'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'kg m-2 s-1'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'kg kg-1'

        if table2Version == 1 and indicatorOfParameter == 50:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 48:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 47:
            return 'degree true'

        if table2Version == 1 and indicatorOfParameter == 46:
            return 's-1'

        if table2Version == 1 and indicatorOfParameter == 45:
            return 's-1'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 's-1'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 's-1'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 's-1'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'm-2/s-2'

        if table2Version == 1 and indicatorOfParameter == 31:
            return 'degree true'

        if table2Version == 1 and indicatorOfParameter == 30:
            return 'Numeric'

        if table2Version == 1 and indicatorOfParameter == 29:
            return 'Numeric'

        if table2Version == 1 and indicatorOfParameter == 28:
            return 'Numeric'

        if table2Version == 1 and indicatorOfParameter == 27:
            return 'gpm'

        if table2Version == 1 and indicatorOfParameter == 26:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 24:
            return 'Numeric'

        if table2Version == 1 and indicatorOfParameter == 23:
            return 'Numeric'

        if table2Version == 1 and indicatorOfParameter == 22:
            return 'Numeric'

        if table2Version == 1 and indicatorOfParameter == 21:
            return 'Numeric'

        if table2Version == 1 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 19:
            return 'K m-1'

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

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'Pa s-1'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'DU'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 75:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 74:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 73:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'kg m-2'

        if table2Version == 1 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'Proportion'

        if table2Version == 1 and indicatorOfParameter == 44:
            return 's-1'

        level = h.get_l('level')

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'W m-2'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'W m-2'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'W m-2'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 's-1'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'Pa s-1'

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'kg kg-1'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'm s-1'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'm2 s-2'

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'gpm'

        if table2Version == 2 and indicatorOfParameter == 127:
            return 0

        if table2Version == 2 and indicatorOfParameter == 126:
            return 'J'

        if table2Version == 2 and indicatorOfParameter == 125:
            return 'N m-2'

        if table2Version == 2 and indicatorOfParameter == 124:
            return 'N m-2'

        if table2Version == 2 and indicatorOfParameter == 120:
            return 0

        if table2Version == 2 and indicatorOfParameter == 119:
            return 0

        if table2Version == 2 and indicatorOfParameter == 116:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 115:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 114:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 113:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 112:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 111:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 109:
            return 'degree true'

        if table2Version == 2 and indicatorOfParameter == 99:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 97:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 96:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 95:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 94:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 93:
            return 'degree true'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 64:
            return 'kg m-2 s-1'

        if table2Version == 2 and indicatorOfParameter == 63:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 59:
            return 'kg m-2 s-1'

        if table2Version == 2 and indicatorOfParameter == 56:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 55:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 53:
            return 'kg kg-1'

        if table2Version == 2 and indicatorOfParameter == 50:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 49:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 48:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 47:
            return 'degree true'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 's-1'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 's-1'

        if table2Version == 2 and indicatorOfParameter == 42:
            return 's-1'

        if table2Version == 2 and indicatorOfParameter == 38:
            return 's-1'

        if table2Version == 3 and indicatorOfParameter == 37:
            return 'm-2/s-2'

        if table2Version == 2 and indicatorOfParameter == 37:
            return 'm-2/s-2'

        if table2Version == 2 and indicatorOfParameter == 27:
            return 'gpm'

        if table2Version == 2 and indicatorOfParameter == 26:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 24:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 23:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 22:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 18:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 16:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 15:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 14:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 14:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 90:
            return 0

        if table2Version == 2 and indicatorOfParameter == 118:
            return 0

        if table2Version == 2 and indicatorOfParameter == 75:
            return 0

        if table2Version == 2 and indicatorOfParameter == 74:
            return 0

        if table2Version == 2 and indicatorOfParameter == 73:
            return 0

        if table2Version == 2 and indicatorOfParameter == 57:
            return 0

        if table2Version == 2 and indicatorOfParameter == 121:
            return 0

        if table2Version == 2 and indicatorOfParameter == 122:
            return 0

        if table2Version == 2 and indicatorOfParameter == 123:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 61:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 65:
            return 'kg -2'

        if table2Version == 3 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'gpm'

        if table2Version == 3 and indicatorOfParameter == 127:
            return 0

        if table2Version == 3 and indicatorOfParameter == 126:
            return 'J'

        if table2Version == 3 and indicatorOfParameter == 125:
            return 'N m-2'

        if table2Version == 3 and indicatorOfParameter == 124:
            return 'N m-2'

        if table2Version == 3 and indicatorOfParameter == 120:
            return 0

        if table2Version == 3 and indicatorOfParameter == 119:
            return 0

        if table2Version == 3 and indicatorOfParameter == 117:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 116:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 115:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 114:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 113:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 112:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 111:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 3 and indicatorOfParameter == 109:
            return 'degree true'

        if table2Version == 3 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 3 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 104:
            return 'degree coming from'

        if table2Version == 3 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 3 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 101:
            return 'degree true'

        if table2Version == 3 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 99:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 97:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 96:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 95:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 94:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 93:
            return 'degree true'

        if table2Version == 3 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 91:
            return 'Proportion'

        if table2Version == 3 and indicatorOfParameter == 89:
            return 'kg m-3'

        if table2Version == 3 and indicatorOfParameter == 88:
            return 0

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 80:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 64:
            return 'kg m-2 s-1'

        if table2Version == 3 and indicatorOfParameter == 63:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 59:
            return 'kg m-2 s-1'

        if table2Version == 3 and indicatorOfParameter == 56:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 55:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 54:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 53:
            return 'kg kg-1'

        if table2Version == 3 and indicatorOfParameter == 50:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 49:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 48:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 47:
            return 'degree true'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 's-1'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 's-1'

        if table2Version == 3 and indicatorOfParameter == 42:
            return 's-1'

        if table2Version == 3 and indicatorOfParameter == 41:
            return 's-1'

        if table2Version == 3 and indicatorOfParameter == 38:
            return 's-1'

        if table2Version == 3 and indicatorOfParameter == 31:
            return 'degree true'

        if table2Version == 3 and indicatorOfParameter == 30:
            return 'Numeric'

        if table2Version == 3 and indicatorOfParameter == 29:
            return 'Numeric'

        if table2Version == 3 and indicatorOfParameter == 28:
            return 'Numeric'

        if table2Version == 3 and indicatorOfParameter == 27:
            return 'gpm'

        if table2Version == 3 and indicatorOfParameter == 26:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 24:
            return 'Numeric'

        if table2Version == 3 and indicatorOfParameter == 23:
            return 'Numeric'

        if table2Version == 3 and indicatorOfParameter == 22:
            return 'Numeric'

        if table2Version == 3 and indicatorOfParameter == 21:
            return 'Numeric'

        if table2Version == 3 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 19:
            return 'K m-1'

        if table2Version == 3 and indicatorOfParameter == 18:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 16:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 15:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 5:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 3:
            return 'Pa s-1'

        if table2Version == 3 and indicatorOfParameter == 123:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 118:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 76:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 62:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 79:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 78:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 10:
            return 'DU'

        if table2Version == 3 and indicatorOfParameter == 90:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 75:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 74:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 73:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 57:
            return 'kg m-2'

        if table2Version == 3 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 81:
            return 'Proportion'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 3 and indicatorOfParameter == 44:
            return 's-1'

        if table2Version == 3 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 121:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 122:
            return 'W m-2'

        if table2Version == 3 and indicatorOfParameter == 43:
            return 's-1'

        if table2Version == 3 and indicatorOfParameter == 39:
            return 'Pa s-1'

        if table2Version == 3 and indicatorOfParameter == 51:
            return 'kg kg-1'

        if table2Version == 3 and indicatorOfParameter == 34:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 33:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 6:
            return 'm2 s-2'

        if table2Version == 3 and indicatorOfParameter == 4:
            return 'K m2 kg-1 s-1'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'K m2 kg-1 s-1'

        if table2Version == 3 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 32:
            return 'm s-1'

        if table2Version == 3 and indicatorOfParameter == 36:
            return 'm2 s-1'

        if table2Version == 3 and indicatorOfParameter == 35:
            return 'm2 s-1'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1:
            return 0

        if table2Version == 202 and indicatorOfParameter == 38:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 36:
            return 'm2 s-1'

        if table2Version == 2 and indicatorOfParameter == 35:
            return 'm2 s-1'

        if table2Version == 2 and indicatorOfParameter == 88:
            return 'kg kg-1'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 0

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1:
            return 'W m-2'

        if table2Version == 202 and indicatorOfParameter == 129:
            return '%'

        if table2Version == 202 and indicatorOfParameter == 129 and timeRangeIndicator == 3:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 1:
            return 'kg kg-1'

        if table2Version == 254 and indicatorOfParameter == 254:
            return 0

        if table2Version == 254 and indicatorOfParameter == 253:
            return 0

        if table2Version == 254 and indicatorOfParameter == 252:
            return 0

        if table2Version == 254 and indicatorOfParameter == 251:
            return 0

        if table2Version == 254 and indicatorOfParameter == 250:
            return 0

        if table2Version == 254 and indicatorOfParameter == 249:
            return 0

        if table2Version == 254 and indicatorOfParameter == 248:
            return 0

        if table2Version == 254 and indicatorOfParameter == 247:
            return 0

        if table2Version == 254 and indicatorOfParameter == 246:
            return 0

        if table2Version == 254 and indicatorOfParameter == 245:
            return 0

        if table2Version == 254 and indicatorOfParameter == 244:
            return 0

        if table2Version == 254 and indicatorOfParameter == 243:
            return 0

        if table2Version == 254 and indicatorOfParameter == 242:
            return 0

        if table2Version == 254 and indicatorOfParameter == 241:
            return 0

        if table2Version == 254 and indicatorOfParameter == 240:
            return 0

        if table2Version == 254 and indicatorOfParameter == 239:
            return 0

        if table2Version == 254 and indicatorOfParameter == 238:
            return 0

        if table2Version == 254 and indicatorOfParameter == 237:
            return 0

        if table2Version == 254 and indicatorOfParameter == 236:
            return 0

        if table2Version == 254 and indicatorOfParameter == 235:
            return 0

        if table2Version == 254 and indicatorOfParameter == 234:
            return 0

        if table2Version == 254 and indicatorOfParameter == 233:
            return 0

        if table2Version == 254 and indicatorOfParameter == 232:
            return 0

        if table2Version == 254 and indicatorOfParameter == 231:
            return 0

        if table2Version == 254 and indicatorOfParameter == 230:
            return 0

        if table2Version == 254 and indicatorOfParameter == 229:
            return 0

        if table2Version == 254 and indicatorOfParameter == 228:
            return 0

        if table2Version == 254 and indicatorOfParameter == 227:
            return 0

        if table2Version == 254 and indicatorOfParameter == 226:
            return 0

        if table2Version == 254 and indicatorOfParameter == 225:
            return 0

        if table2Version == 254 and indicatorOfParameter == 224:
            return 0

        if table2Version == 254 and indicatorOfParameter == 223:
            return 0

        if table2Version == 254 and indicatorOfParameter == 222:
            return 0

        if table2Version == 254 and indicatorOfParameter == 221:
            return 0

        if table2Version == 254 and indicatorOfParameter == 220:
            return 0

        if table2Version == 254 and indicatorOfParameter == 219:
            return 0

        if table2Version == 254 and indicatorOfParameter == 218:
            return 0

        if table2Version == 254 and indicatorOfParameter == 217:
            return 0

        if table2Version == 254 and indicatorOfParameter == 216:
            return 0

        if table2Version == 254 and indicatorOfParameter == 215:
            return 0

        if table2Version == 254 and indicatorOfParameter == 214:
            return 0

        if table2Version == 254 and indicatorOfParameter == 213:
            return 0

        if table2Version == 254 and indicatorOfParameter == 212:
            return 0

        if table2Version == 254 and indicatorOfParameter == 211:
            return 0

        if table2Version == 254 and indicatorOfParameter == 210:
            return 0

        if table2Version == 254 and indicatorOfParameter == 209:
            return 0

        if table2Version == 254 and indicatorOfParameter == 208:
            return 0

        if table2Version == 254 and indicatorOfParameter == 207:
            return 0

        if table2Version == 254 and indicatorOfParameter == 206:
            return 0

        if table2Version == 254 and indicatorOfParameter == 205:
            return 0

        if table2Version == 254 and indicatorOfParameter == 204:
            return 0

        if table2Version == 254 and indicatorOfParameter == 203:
            return 0

        if table2Version == 254 and indicatorOfParameter == 202:
            return 0

        if table2Version == 254 and indicatorOfParameter == 201:
            return 0

        if table2Version == 254 and indicatorOfParameter == 200:
            return 0

        if table2Version == 254 and indicatorOfParameter == 199:
            return 0

        if table2Version == 254 and indicatorOfParameter == 198:
            return 0

        if table2Version == 254 and indicatorOfParameter == 197:
            return 0

        if table2Version == 254 and indicatorOfParameter == 196:
            return 0

        if table2Version == 254 and indicatorOfParameter == 195:
            return 0

        if table2Version == 254 and indicatorOfParameter == 194:
            return 0

        if table2Version == 254 and indicatorOfParameter == 193:
            return 0

        if table2Version == 254 and indicatorOfParameter == 192:
            return 0

        if table2Version == 254 and indicatorOfParameter == 191:
            return 0

        if table2Version == 254 and indicatorOfParameter == 190:
            return 0

        if table2Version == 254 and indicatorOfParameter == 189:
            return 0

        if table2Version == 254 and indicatorOfParameter == 188:
            return 0

        if table2Version == 254 and indicatorOfParameter == 187:
            return 0

        if table2Version == 254 and indicatorOfParameter == 186:
            return 0

        if table2Version == 254 and indicatorOfParameter == 185:
            return 0

        if table2Version == 254 and indicatorOfParameter == 184:
            return 0

        if table2Version == 254 and indicatorOfParameter == 183:
            return 0

        if table2Version == 254 and indicatorOfParameter == 182:
            return 0

        if table2Version == 254 and indicatorOfParameter == 181:
            return 0

        if table2Version == 254 and indicatorOfParameter == 180:
            return 0

        if table2Version == 254 and indicatorOfParameter == 179:
            return 0

        if table2Version == 254 and indicatorOfParameter == 178:
            return 0

        if table2Version == 254 and indicatorOfParameter == 177:
            return 0

        if table2Version == 254 and indicatorOfParameter == 176:
            return 0

        if table2Version == 254 and indicatorOfParameter == 175:
            return 0

        if table2Version == 254 and indicatorOfParameter == 174:
            return 0

        if table2Version == 254 and indicatorOfParameter == 173:
            return 0

        if table2Version == 254 and indicatorOfParameter == 172:
            return 0

        if table2Version == 254 and indicatorOfParameter == 171:
            return 0

        if table2Version == 254 and indicatorOfParameter == 170:
            return 0

        if table2Version == 254 and indicatorOfParameter == 169:
            return 0

        if table2Version == 254 and indicatorOfParameter == 168:
            return 0

        if table2Version == 254 and indicatorOfParameter == 167:
            return 0

        if table2Version == 254 and indicatorOfParameter == 166:
            return 0

        if table2Version == 254 and indicatorOfParameter == 165:
            return 0

        if table2Version == 254 and indicatorOfParameter == 164:
            return 0

        if table2Version == 254 and indicatorOfParameter == 163:
            return 0

        if table2Version == 254 and indicatorOfParameter == 162:
            return 0

        if table2Version == 254 and indicatorOfParameter == 161:
            return 0

        if table2Version == 254 and indicatorOfParameter == 160:
            return 0

        if table2Version == 254 and indicatorOfParameter == 159:
            return 0

        if table2Version == 254 and indicatorOfParameter == 158:
            return 0

        if table2Version == 254 and indicatorOfParameter == 157:
            return 0

        if table2Version == 254 and indicatorOfParameter == 156:
            return 0

        if table2Version == 254 and indicatorOfParameter == 155:
            return 0

        if table2Version == 254 and indicatorOfParameter == 154:
            return 0

        if table2Version == 254 and indicatorOfParameter == 153:
            return 0

        if table2Version == 254 and indicatorOfParameter == 152:
            return 0

        if table2Version == 254 and indicatorOfParameter == 151:
            return 0

        if table2Version == 254 and indicatorOfParameter == 150:
            return 0

        if table2Version == 254 and indicatorOfParameter == 149:
            return 0

        if table2Version == 254 and indicatorOfParameter == 148:
            return 0

        if table2Version == 254 and indicatorOfParameter == 147:
            return 0

        if table2Version == 254 and indicatorOfParameter == 146:
            return 0

        if table2Version == 254 and indicatorOfParameter == 145:
            return 0

        if table2Version == 254 and indicatorOfParameter == 144:
            return 0

        if table2Version == 254 and indicatorOfParameter == 143:
            return 0

        if table2Version == 254 and indicatorOfParameter == 142:
            return 0

        if table2Version == 254 and indicatorOfParameter == 141:
            return 0

        if table2Version == 254 and indicatorOfParameter == 140:
            return 0

        if table2Version == 254 and indicatorOfParameter == 139:
            return 0

        if table2Version == 254 and indicatorOfParameter == 138:
            return 0

        if table2Version == 254 and indicatorOfParameter == 137:
            return 0

        if table2Version == 254 and indicatorOfParameter == 136:
            return 0

        if table2Version == 254 and indicatorOfParameter == 135:
            return 0

        if table2Version == 254 and indicatorOfParameter == 134:
            return 0

        if table2Version == 254 and indicatorOfParameter == 133:
            return 0

        if table2Version == 254 and indicatorOfParameter == 132:
            return 0

        if table2Version == 254 and indicatorOfParameter == 131:
            return 0

        if table2Version == 254 and indicatorOfParameter == 130:
            return 0

        if table2Version == 254 and indicatorOfParameter == 129:
            return 0

        if table2Version == 254 and indicatorOfParameter == 128:
            return 0

        if table2Version == 254 and indicatorOfParameter == 127:
            return 0

        if table2Version == 254 and indicatorOfParameter == 126:
            return 0

        if table2Version == 254 and indicatorOfParameter == 125:
            return 0

        if table2Version == 254 and indicatorOfParameter == 124:
            return 0

        if table2Version == 254 and indicatorOfParameter == 123:
            return 0

        if table2Version == 254 and indicatorOfParameter == 122:
            return 0

        if table2Version == 254 and indicatorOfParameter == 121:
            return 0

        if table2Version == 254 and indicatorOfParameter == 120:
            return 0

        if table2Version == 254 and indicatorOfParameter == 119:
            return 0

        if table2Version == 254 and indicatorOfParameter == 118:
            return 0

        if table2Version == 254 and indicatorOfParameter == 117:
            return 0

        if table2Version == 254 and indicatorOfParameter == 116:
            return 0

        if table2Version == 254 and indicatorOfParameter == 115:
            return 0

        if table2Version == 254 and indicatorOfParameter == 114:
            return 0

        if table2Version == 254 and indicatorOfParameter == 113:
            return 0

        if table2Version == 254 and indicatorOfParameter == 112:
            return 0

        if table2Version == 254 and indicatorOfParameter == 111:
            return 0

        if table2Version == 254 and indicatorOfParameter == 110:
            return 0

        if table2Version == 254 and indicatorOfParameter == 109:
            return 0

        if table2Version == 254 and indicatorOfParameter == 108:
            return 0

        if table2Version == 254 and indicatorOfParameter == 107:
            return 0

        if table2Version == 254 and indicatorOfParameter == 106:
            return 0

        if table2Version == 254 and indicatorOfParameter == 105:
            return 0

        if table2Version == 254 and indicatorOfParameter == 104:
            return 0

        if table2Version == 254 and indicatorOfParameter == 103:
            return 0

        if table2Version == 254 and indicatorOfParameter == 102:
            return 0

        if table2Version == 254 and indicatorOfParameter == 101:
            return 0

        if table2Version == 254 and indicatorOfParameter == 100:
            return 0

        if table2Version == 254 and indicatorOfParameter == 99:
            return 0

        if table2Version == 254 and indicatorOfParameter == 98:
            return 0

        if table2Version == 254 and indicatorOfParameter == 97:
            return 0

        if table2Version == 254 and indicatorOfParameter == 96:
            return 0

        if table2Version == 254 and indicatorOfParameter == 95:
            return 0

        if table2Version == 254 and indicatorOfParameter == 94:
            return 0

        if table2Version == 254 and indicatorOfParameter == 93:
            return 0

        if table2Version == 254 and indicatorOfParameter == 92:
            return 0

        if table2Version == 254 and indicatorOfParameter == 91:
            return 0

        if table2Version == 254 and indicatorOfParameter == 90:
            return 0

        if table2Version == 254 and indicatorOfParameter == 89:
            return 0

        if table2Version == 254 and indicatorOfParameter == 88:
            return 0

        if table2Version == 254 and indicatorOfParameter == 87:
            return 0

        if table2Version == 254 and indicatorOfParameter == 86:
            return 0

        if table2Version == 254 and indicatorOfParameter == 85:
            return 0

        if table2Version == 254 and indicatorOfParameter == 84:
            return 0

        if table2Version == 254 and indicatorOfParameter == 83:
            return 0

        if table2Version == 254 and indicatorOfParameter == 82:
            return 0

        if table2Version == 254 and indicatorOfParameter == 81:
            return 0

        if table2Version == 254 and indicatorOfParameter == 80:
            return 0

        if table2Version == 254 and indicatorOfParameter == 79:
            return 0

        if table2Version == 254 and indicatorOfParameter == 78:
            return 0

        if table2Version == 254 and indicatorOfParameter == 77:
            return 0

        if table2Version == 254 and indicatorOfParameter == 76:
            return 0

        if table2Version == 254 and indicatorOfParameter == 75:
            return 0

        if table2Version == 254 and indicatorOfParameter == 74:
            return 0

        if table2Version == 254 and indicatorOfParameter == 73:
            return 0

        if table2Version == 254 and indicatorOfParameter == 72:
            return 0

        if table2Version == 254 and indicatorOfParameter == 71:
            return 0

        if table2Version == 254 and indicatorOfParameter == 70:
            return 0

        if table2Version == 254 and indicatorOfParameter == 69:
            return 0

        if table2Version == 254 and indicatorOfParameter == 68:
            return 0

        if table2Version == 254 and indicatorOfParameter == 67:
            return 0

        if table2Version == 254 and indicatorOfParameter == 66:
            return 0

        if table2Version == 254 and indicatorOfParameter == 65:
            return 0

        if table2Version == 254 and indicatorOfParameter == 64:
            return 0

        if table2Version == 254 and indicatorOfParameter == 63:
            return 0

        if table2Version == 254 and indicatorOfParameter == 62:
            return 0

        if table2Version == 254 and indicatorOfParameter == 61:
            return 0

        if table2Version == 254 and indicatorOfParameter == 60:
            return 0

        if table2Version == 254 and indicatorOfParameter == 59:
            return 0

        if table2Version == 254 and indicatorOfParameter == 58:
            return 0

        if table2Version == 254 and indicatorOfParameter == 57:
            return 0

        if table2Version == 254 and indicatorOfParameter == 56:
            return 0

        if table2Version == 254 and indicatorOfParameter == 55:
            return 0

        if table2Version == 254 and indicatorOfParameter == 54:
            return 0

        if table2Version == 254 and indicatorOfParameter == 53:
            return 0

        if table2Version == 254 and indicatorOfParameter == 52:
            return 0

        if table2Version == 254 and indicatorOfParameter == 51:
            return 0

        if table2Version == 254 and indicatorOfParameter == 50:
            return 0

        if table2Version == 254 and indicatorOfParameter == 49:
            return 0

        if table2Version == 254 and indicatorOfParameter == 48:
            return 0

        if table2Version == 254 and indicatorOfParameter == 47:
            return 0

        if table2Version == 254 and indicatorOfParameter == 46:
            return 0

        if table2Version == 254 and indicatorOfParameter == 45:
            return 0

        if table2Version == 254 and indicatorOfParameter == 44:
            return 0

        if table2Version == 254 and indicatorOfParameter == 43:
            return 0

        if table2Version == 254 and indicatorOfParameter == 42:
            return 0

        if table2Version == 254 and indicatorOfParameter == 41:
            return 0

        if table2Version == 254 and indicatorOfParameter == 40:
            return 0

        if table2Version == 254 and indicatorOfParameter == 39:
            return 0

        if table2Version == 254 and indicatorOfParameter == 38:
            return 0

        if table2Version == 254 and indicatorOfParameter == 37:
            return 0

        if table2Version == 254 and indicatorOfParameter == 36:
            return 0

        if table2Version == 254 and indicatorOfParameter == 35:
            return 0

        if table2Version == 254 and indicatorOfParameter == 34:
            return 0

        if table2Version == 254 and indicatorOfParameter == 33:
            return 0

        if table2Version == 254 and indicatorOfParameter == 32:
            return 0

        if table2Version == 254 and indicatorOfParameter == 31:
            return 0

        if table2Version == 254 and indicatorOfParameter == 30:
            return 0

        if table2Version == 254 and indicatorOfParameter == 29:
            return 0

        if table2Version == 254 and indicatorOfParameter == 28:
            return 0

        if table2Version == 254 and indicatorOfParameter == 27:
            return 0

        if table2Version == 254 and indicatorOfParameter == 26:
            return 0

        if table2Version == 254 and indicatorOfParameter == 25:
            return 0

        if table2Version == 254 and indicatorOfParameter == 24:
            return 0

        if table2Version == 254 and indicatorOfParameter == 23:
            return 0

        if table2Version == 254 and indicatorOfParameter == 22:
            return 0

        if table2Version == 254 and indicatorOfParameter == 21:
            return 0

        if table2Version == 254 and indicatorOfParameter == 20:
            return 0

        if table2Version == 254 and indicatorOfParameter == 19:
            return 0

        if table2Version == 254 and indicatorOfParameter == 18:
            return 0

        if table2Version == 254 and indicatorOfParameter == 17:
            return 0

        if table2Version == 254 and indicatorOfParameter == 16:
            return 0

        if table2Version == 254 and indicatorOfParameter == 15:
            return 0

        if table2Version == 254 and indicatorOfParameter == 14:
            return 0

        if table2Version == 254 and indicatorOfParameter == 13:
            return 0

        if table2Version == 254 and indicatorOfParameter == 12:
            return 0

        if table2Version == 254 and indicatorOfParameter == 11:
            return 0

        if table2Version == 254 and indicatorOfParameter == 10:
            return 0

        if table2Version == 254 and indicatorOfParameter == 9:
            return 0

        if table2Version == 254 and indicatorOfParameter == 8:
            return 0

        if table2Version == 254 and indicatorOfParameter == 7:
            return 0

        if table2Version == 254 and indicatorOfParameter == 6:
            return 0

        if table2Version == 254 and indicatorOfParameter == 5:
            return 0

        if table2Version == 254 and indicatorOfParameter == 4:
            return 0

        if table2Version == 254 and indicatorOfParameter == 3:
            return 0

        if table2Version == 254 and indicatorOfParameter == 2:
            return 0

        if table2Version == 254 and indicatorOfParameter == 1:
            return 0

        if table2Version == 242 and indicatorOfParameter == 252:
            return 'm-3'

        if table2Version == 242 and indicatorOfParameter == 251:
            return 'kg m-3'

        if table2Version == 242 and indicatorOfParameter == 74:
            return 'm-3'

        if table2Version == 242 and indicatorOfParameter == 73:
            return 'm-3'

        if table2Version == 242 and indicatorOfParameter == 72:
            return 'm-3'

        if table2Version == 242 and indicatorOfParameter == 35:
            return 'kg m-3'

        if table2Version == 242 and indicatorOfParameter == 34:
            return 'kg m-3'

        if table2Version == 2 and indicatorOfParameter == 19:
            return 'K m-1'

        if table2Version == 242 and indicatorOfParameter == 33:
            return 'kg m-3'

        if table2Version == 201 and indicatorOfParameter == 90:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 211:
            return 's m-1'

        if table2Version == 201 and indicatorOfParameter == 157:
            return 'm2 s-3'

        if table2Version == 201 and indicatorOfParameter == 156:
            return 'm2 s-3'

        if table2Version == 201 and indicatorOfParameter == 155:
            return 'm2 s-3'

        if table2Version == 210 and indicatorOfParameter == 34:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 33:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 32:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 31:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 30:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 29:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 28:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 27:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 26:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 25:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 24:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 23:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 22:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 21:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 20:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 19:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 18:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 17:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 16:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 15:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 14:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 13:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 12:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 11:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 10:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 9:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 8:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 7:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 6:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 5:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 4:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 3:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 2:
            return 'Numeric'

        if table2Version == 210 and indicatorOfParameter == 1:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 117:
            return 'W m-2'

        if table2Version == 203 and indicatorOfParameter == 2:
            return '10 gpm'

        if table2Version == 2 and indicatorOfParameter == 5:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'kg m-2'

        if table2Version == 204 and indicatorOfParameter == 71:
            return '10-7 s-2'

        if table2Version == 204 and indicatorOfParameter == 70:
            return 'm2/3 s-1'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 1 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 1 and level == 2:
            return 'K'

        topLevel = h.get_l('topLevel')
        bottomLevel = h.get_l('bottomLevel')

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 7 and bottomLevel == 50:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 7:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 112:
            return 'K'

        localElementNumber = h.get_l('localElementNumber')

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 2 and indicatorOfTypeOfLevel == 112 and topLevel == 0:
            return 'kg2 m-4'

        if table2Version == 203 and indicatorOfParameter == 10:
            return 'Pa-3h'

        if table2Version == 202 and indicatorOfParameter == 119:
            return 'Pa'

        if table2Version == 202 and indicatorOfParameter == 117:
            return 'C'

        if table2Version == 202 and indicatorOfParameter == 101:
            return 's2 m-2'

        if table2Version == 201 and indicatorOfParameter == 231:
            return 0

        if table2Version == 201 and indicatorOfParameter == 83:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 44:
            return 's-1'

        if table2Version == 2 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 203 and indicatorOfParameter == 146:
            return 's-1'

        if table2Version == 203 and indicatorOfParameter == 128:
            return 'Km kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 127:
            return 'm kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 126:
            return 'm kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 125:
            return 'm2 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 123:
            return 'm kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 118:
            return 'K2 m-2 s-1'

        if table2Version == 203 and indicatorOfParameter == 117:
            return 'm kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 116:
            return 'm kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 115:
            return 'm2 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 114:
            return 'm2 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 113:
            return 'm kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 112:
            return 'm2 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 111:
            return 'm2 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 105:
            return 'm kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 100:
            return 's-1'

        if table2Version == 203 and indicatorOfParameter == 119:
            return 'K m2 kg-1 s-1'

        if table2Version == 2 and indicatorOfParameter == 63 and timeRangeIndicator == 5:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 89:
            return 'kg m-3'

        if table2Version == 2 and indicatorOfParameter == 4:
            return 'K m2 kg-1 s-1'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 's-1'

        if table2Version == 202 and indicatorOfParameter == 134:
            return 's-1'

        if table2Version == 202 and indicatorOfParameter == 133:
            return 's-1'

        if table2Version == 203 and indicatorOfParameter == 205:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 194:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 193:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 192:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 191:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'hft'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'hft'

        if table2Version == 201 and indicatorOfParameter == 94:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 192:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 91:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 95:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 191:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 193:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 194:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 190:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 93:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 92:
            return 'm-1'

        if table2Version == 201 and indicatorOfParameter == 97:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 96:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 55:
            return 'Proportion'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 42 and timeRangeIndicator == 0:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 203 and indicatorOfParameter == 58:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 57:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 41:
            return 's-1'

        if table2Version == 203 and indicatorOfParameter == 61:
            return 'C'

        if table2Version == 2 and indicatorOfParameter == 80:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 60:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 93:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 249:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 247:
            return 'DU'

        if table2Version == 202 and indicatorOfParameter == 243:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 242:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 241:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 240:
            return 'Numeric'

        if table2Version == 208 and indicatorOfParameter == 236:
            return 'K'

        if table2Version == 208 and indicatorOfParameter == 232:
            return 'K'

        if table2Version == 208 and indicatorOfParameter == 213:
            return 'Numeric'

        if table2Version == 208 and indicatorOfParameter == 212:
            return 'Numeric'

        if table2Version == 208 and indicatorOfParameter == 199:
            return 'Numeric'

        if table2Version == 208 and indicatorOfParameter == 198:
            return 'Numeric'

        if table2Version == 208 and indicatorOfParameter == 197:
            return 'Numeric'

        if table2Version == 208 and indicatorOfParameter == 191:
            return 'Numeric'

        if table2Version == 208 and indicatorOfParameter == 139:
            return 'm s-1'

        if table2Version == 208 and indicatorOfParameter == 138:
            return 'm s-1'

        if table2Version == 208 and indicatorOfParameter == 137:
            return 'm s-1'

        if table2Version == 208 and indicatorOfParameter == 136:
            return 'm s-1'

        if table2Version == 208 and indicatorOfParameter == 134:
            return 'm s-1'

        if table2Version == 208 and indicatorOfParameter == 132:
            return 'm s-1'

        if table2Version == 208 and indicatorOfParameter == 77:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 75:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 74:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 72:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 71:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 70:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 69:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 32:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 29:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 26:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 17:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 14:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 3:
            return 'kg m2'

        if table2Version == 208 and indicatorOfParameter == 1:
            return 'kg m2'

        if table2Version == 201 and indicatorOfParameter == 132 and timeRangeIndicator == 0:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 113 and timeRangeIndicator == 1:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 102 and timeRangeIndicator == 1:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'N m-2'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'N m-2'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 1:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 78 and timeRangeIndicator == 1:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 79 and timeRangeIndicator == 1:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 10:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 78 and timeRangeIndicator == 0:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 113 and timeRangeIndicator == 0:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 79 and timeRangeIndicator == 0:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 102 and timeRangeIndicator == 0:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 0:
            return 'kg m-2'

        if table2Version == 203 and indicatorOfParameter == 56 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'C'

        if table2Version == 203 and indicatorOfParameter == 55 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'C'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 5:
            return 'kg m-2'

        if table2Version == 207 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 207 and indicatorOfParameter == 79:
            return 'kg m-2'

        if table2Version == 207 and indicatorOfParameter == 61:
            return 'kg m-2'

        if table2Version == 206 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 206 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 'K'

        if table2Version == 206 and indicatorOfParameter == 79:
            return 'kg m-2'

        if table2Version == 206 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 206 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 206 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 206 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 206 and indicatorOfParameter == 61:
            return 'kg m-2'

        if table2Version == 206 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 206 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 206 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 206 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'K'

        if table2Version == 206 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'K'

        if table2Version == 206 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222:
            return 'W m sr m-2'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222:
            return 'K'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222:
            return 'K'

        if table2Version == 204 and indicatorOfParameter == 16:
            return 'J kg-1'

        if table2Version == 204 and indicatorOfParameter == 15:
            return 'J kg-1'

        if table2Version == 204 and indicatorOfParameter == 14:
            return 'Pa s-1'

        if table2Version == 204 and indicatorOfParameter == 13:
            return 'Pa s-1'

        if table2Version == 204 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 204 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 204 and indicatorOfParameter == 10:
            return '%'

        if table2Version == 204 and indicatorOfParameter == 9:
            return '%'

        if table2Version == 204 and indicatorOfParameter == 8:
            return 'm2 s-2'

        if table2Version == 204 and indicatorOfParameter == 7:
            return 'm2 s-2'

        if table2Version == 204 and indicatorOfParameter == 6:
            return 'm s-1'

        if table2Version == 204 and indicatorOfParameter == 5:
            return 'm s-1'

        if table2Version == 204 and indicatorOfParameter == 4:
            return 'm s-1'

        if table2Version == 204 and indicatorOfParameter == 3:
            return 'm s-1'

        if table2Version == 204 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 204 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 203 and indicatorOfParameter == 204:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 203:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 196:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 157:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 154:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 140:
            return 'K'

        if table2Version == 203 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 100:
            return 'hPa'

        if table2Version == 203 and indicatorOfParameter == 132:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 131:
            return 'm s-1'

        if table2Version == 203 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 100:
            return 'K m2 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 124:
            return 'm2 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 109:
            return 's-1'

        if table2Version == 203 and indicatorOfParameter == 107:
            return 'm3 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 103:
            return 'm3 kg-1 s-1'

        if table2Version == 203 and indicatorOfParameter == 101:
            return 's-2'

        if table2Version == 203 and indicatorOfParameter == 99:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 94 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 203 and indicatorOfParameter == 90:
            return 'Numeric'

        if table2Version == 203 and indicatorOfParameter == 33:
            return 's-2'

        if table2Version == 203 and indicatorOfParameter == 30:
            return 'J kg-1'

        if table2Version == 203 and indicatorOfParameter == 29:
            return 's-1'

        if table2Version == 202 and indicatorOfParameter == 248:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 233:
            return 'W m-2'

        if table2Version == 202 and indicatorOfParameter == 233 and timeRangeIndicator == 1:
            return 'W m-2'

        if table2Version == 202 and indicatorOfParameter == 232:
            return 'N m-2'

        if table2Version == 202 and indicatorOfParameter == 232 and timeRangeIndicator == 3:
            return 'N m-2'

        if table2Version == 202 and indicatorOfParameter == 231:
            return 'N m-2'

        if table2Version == 202 and indicatorOfParameter == 231 and timeRangeIndicator == 3:
            return 'N m-2'

        if table2Version == 202 and indicatorOfParameter == 229:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 228:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 227:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 226:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 225:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 224:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 223:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 222:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 221:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 220:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 219:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 218:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 217:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 216:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 215:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 214:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 213:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 212:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 211:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 210:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 209:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 208:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 207:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 206:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 205:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 204:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 203:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 202:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 201:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 200:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 199:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 198:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 197:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 196:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 195:
            return 'Bq m-2'

        if table2Version == 202 and indicatorOfParameter == 194:
            return 'Bq m-3'

        if table2Version == 202 and indicatorOfParameter == 180:
            return 'kg kg-1'

        if table2Version == 202 and indicatorOfParameter == 123:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 122:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 121:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 115:
            return 'deg E'

        if table2Version == 202 and indicatorOfParameter == 114:
            return 'deg N'

        if table2Version == 202 and indicatorOfParameter == 113:
            return 's-1'

        if table2Version == 202 and indicatorOfParameter == 105:
            return 's-1 m-2'

        if table2Version == 202 and indicatorOfParameter == 104:
            return 's-1'

        if table2Version == 202 and indicatorOfParameter == 93 and timeRangeIndicator == 3:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 93:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 92 and timeRangeIndicator == 3:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 92:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 91 and timeRangeIndicator == 3:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 91:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 86 and timeRangeIndicator == 3:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 86:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 84:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 79 and timeRangeIndicator == 0:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 79 and timeRangeIndicator == 3:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 78 and timeRangeIndicator == 0:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 77 and timeRangeIndicator == 3:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 76:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 75:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 2 and indicatorOfTypeOfLevel == 112:
            return 'kg2 m-4'

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 1 and indicatorOfTypeOfLevel == 112 and topLevel == 0:
            return 'kg2 m-4'

        if table2Version == 202 and indicatorOfParameter == 71:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 70:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 69:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 68:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 67:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 65:
            return 'Pa'

        if table2Version == 202 and indicatorOfParameter == 64:
            return 'Pa'

        if table2Version == 202 and indicatorOfParameter == 62:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 61:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 57:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 56:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 49:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 48:
            return 'rad'

        if table2Version == 202 and indicatorOfParameter == 47:
            return 'Numeric'

        if table2Version == 202 and indicatorOfParameter == 46:
            return 'm'

        if table2Version == 202 and indicatorOfParameter == 45:
            return 'm s-2'

        if table2Version == 202 and indicatorOfParameter == 44:
            return 'm s-2'

        if table2Version == 202 and indicatorOfParameter == 42:
            return 'm2 s-2'

        if table2Version == 202 and indicatorOfParameter == 41:
            return 'm2 s-2'

        if table2Version == 202 and indicatorOfParameter == 40:
            return 'gpm'

        if table2Version == 202 and indicatorOfParameter == 19:
            return 'degree true'

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

        if table2Version == 202 and indicatorOfParameter == 7:
            return 's'

        if table2Version == 202 and indicatorOfParameter == 4:
            return 'degree true'

        if table2Version == 201 and indicatorOfParameter == 243:
            return 's-1'

        if table2Version == 201 and indicatorOfParameter == 241:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 240 and indicatorOfTypeOfLevel == 1:
            return 'kg m-2 s-1'

        if table2Version == 201 and indicatorOfParameter == 239:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 237:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 236:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 233:
            return 'K s-1'

        if table2Version == 201 and indicatorOfParameter == 232:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200:
            return 'dBZ'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 110:
            return 'dBZ'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 1:
            return 'dBZ'

        if table2Version == 201 and indicatorOfParameter == 215:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 212:
            return 's m-1'

        if table2Version == 201 and indicatorOfParameter == 203:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 200:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 111:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 111:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 197 and indicatorOfTypeOfLevel == 111:
            return 'K'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 201 and indicatorOfParameter == 173:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 171:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 170:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 154:
            return 'm2 s-1'

        if table2Version == 201 and indicatorOfParameter == 153:
            return 'm2 s-1'

        if table2Version == 201 and indicatorOfParameter == 152:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 149:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 148:
            return 'm2 s-3'

        if table2Version == 201 and indicatorOfParameter == 147:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 146 and indicatorOfTypeOfLevel == 1:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 145 and indicatorOfTypeOfLevel == 1:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 144 and indicatorOfTypeOfLevel == 1:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 143 and indicatorOfTypeOfLevel == 1:
            return 'J kg-1'

        if table2Version == 201 and indicatorOfParameter == 142:
            return 's-1'

        if table2Version == 201 and indicatorOfParameter == 141:
            return 's-1'

        if table2Version == 201 and indicatorOfParameter == 139:
            return 'Pa'

        if table2Version == 201 and indicatorOfParameter == 133:
            return 'kg m-3'

        if table2Version == 201 and indicatorOfParameter == 132:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 131:
            return 'kg m-2 s-1'

        if table2Version == 201 and indicatorOfParameter == 130:
            return 'kg kg-1 s-1'

        if table2Version == 201 and indicatorOfParameter == 129:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 127:
            return 'kg kg-1 s-1'

        if table2Version == 201 and indicatorOfParameter == 125:
            return 'kg kg-1 s-1'

        if table2Version == 201 and indicatorOfParameter == 124:
            return 'K s-1'

        if table2Version == 201 and indicatorOfParameter == 123:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 122:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 113:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 112:
            return 'kg m-2 s-1'

        if table2Version == 201 and indicatorOfParameter == 111:
            return 'kg m-2 s-1'

        if table2Version == 201 and indicatorOfParameter == 102:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 101:
            return 'kg m-2 s-1'

        if table2Version == 201 and indicatorOfParameter == 100:
            return 'kg m-2 s-1'

        if table2Version == 201 and indicatorOfParameter == 99:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 89:
            return 'kg kg-1 s-1'

        if table2Version == 201 and indicatorOfParameter == 88:
            return 'kg kg-1 s-1'

        if table2Version == 201 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 4:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 4:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 82 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 79:
            return 'm s-2'

        if table2Version == 201 and indicatorOfParameter == 78:
            return 'm s-2'

        if table2Version == 201 and indicatorOfParameter == 75:
            return 'kg kg-1 s-1'

        if table2Version == 201 and indicatorOfParameter == 74:
            return 'K s-1'

        if table2Version == 201 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 3:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 2:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 61:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 59 and indicatorOfTypeOfLevel == 3:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 2:
            return 'm'

        if table2Version == 201 and indicatorOfParameter == 53:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 52:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 51:
            return 'Numeric'

        if table2Version == 201 and indicatorOfParameter == 44:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 43:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 42:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 41:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 40:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 39:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 38:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 37:
            return 'kg m-2'

        if table2Version == 201 and indicatorOfParameter == 36:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 35:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 33:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 31:
            return 'kg kg-1'

        if table2Version == 201 and indicatorOfParameter == 30:
            return '%'

        if table2Version == 201 and indicatorOfParameter == 29:
            return '%'

        if table2Version == 201 and indicatorOfParameter == 21 and timeRangeIndicator == 0:
            return 's m-1'

        if table2Version == 201 and indicatorOfParameter == 20 and timeRangeIndicator == 4:
            return 'h'

        if table2Version == 201 and indicatorOfParameter == 19 and indicatorOfTypeOfLevel == 111 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 18 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 14:
            return 'K s-1'

        if table2Version == 201 and indicatorOfParameter == 13:
            return 'K s-1'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1:
            return 'W m-2'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'N m-2'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'N m-2'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'W m-2'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'degree coming from'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'degree true'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 91:
            return 'Proportion'

        if table2Version == 2 and indicatorOfParameter == 90 and topLevel == 0:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 90 and topLevel == 10:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and bottomLevel == 100:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 100 and bottomLevel == 190:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 9:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 41:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 36:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 81:
            return 'Proportion'

        if table2Version == 2 and indicatorOfParameter == 79:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 78:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 76:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 65:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 63 and timeRangeIndicator == 4:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 62 and timeRangeIndicator == 4:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 61:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 58:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 54:
            return 'kg m-2'

        if table2Version == 2 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'kg kg-1'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'kg kg-1'

        if table2Version == 2 and indicatorOfParameter == 40:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'Pa s-1'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 32:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s-1'

        if table2Version == 2 and indicatorOfParameter == 31:
            return 'degree true'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'degree true'

        if table2Version == 2 and indicatorOfParameter == 30:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 29:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 28:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 21:
            return 'Numeric'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 10:
            return 'DU'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 109:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'm2 s-2'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 110:
            return 'm2 s-2'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 1:
            return 'm2 s-2'

        if table2Version == 2 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 1:
            return 'Pa s-1'

        if table2Version == 2 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

    return wrapped
