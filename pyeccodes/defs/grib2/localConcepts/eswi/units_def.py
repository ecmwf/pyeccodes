import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 19:
            return 'm/s'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return '1/s'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return '%'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 8:
            return 'Degree'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 'Degree'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 'm/s'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 'm/s'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 'Code'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 'm'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 'kg/m2/s'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg/m2'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 9:
            return 'Code'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 8:
            return 'Code'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 'Code'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 5:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 4:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 3:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1:
            return 'Numeric'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 0:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 'kg/m3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 16:
            return 'kg/m3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 15:
            return 'm3/m3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 14:
            return 'kg/m3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 13:
            return 'm3/m3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12:
            return 'kg/m3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 11:
            return 'm3/m3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 10:
            return 'm3/m3'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 'Numeric'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 'm3/m3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26:
            return 'kg/m3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 'm3/m3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 'W/m2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 'kg/m2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'kg/m3'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 19:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 's/m'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 'm/s'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 'kg/m2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 'kg/m2/s'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 'Proportion'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 'Code'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return '1/kg2/s'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'fraction'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21:
            return 'rad'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 'N/m2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 'N/m2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return 'gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 'Pa'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 32:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 'N/m2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 'm/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 84:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 83:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 62:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 'm/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 'm/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 57:
            return 'm/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'Proportion'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 23:
            return 1

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 22:
            return 1

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 21:
            return 1

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 20:
            return 1

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 'Code'

        atmosphericChemicalConsituentType = h.get_l('atmosphericChemicalConsituentType')

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10006:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10022:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10021:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10012:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10002:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10001:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 12:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 20:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 14:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 16:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 18:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 15:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 13:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63011:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60013:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10004:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10011:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10017:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 7:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10023:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10015:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10009:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10016:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10008:
            return '-'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'J/kg'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 1:
            return 'm3/s'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 's'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return '%'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg/m2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 'kg/m2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 'kg/m2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return '%'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return 'Code'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return 'Code'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 'kg/m2'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 'kg/m2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'Deg. true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'Deg true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'Deg true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'Deg. true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'Deg. true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return '1/s'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 'm/s'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'm/s'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'Deg true'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'Fraction'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'kg/m3'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'Fraction'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'g/kg'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'cm/s'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'cm/s'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'm/s'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'Deg true'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'm2/s2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'm2/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'm2/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'Deg true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return '-'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return '-'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return '-'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pa'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'J/kg'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'm/s'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'm/s'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 's'

        if discipline == 0 and parameterCategory == 190 and parameterNumber == 0:
            return 'CCITTIA5'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 'Code'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 'Code'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 'Code'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 'Code'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'Code'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 6:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 5:
            return 'm'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5:
            return 'dB'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 4:
            return 'dB'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 2:
            return 'mm6/m3'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 1:
            return 'mm6/m3'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 0:
            return 'mm6/m3'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5:
            return 'kg/m'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 'dB'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 'kg/m'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 'm/s'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 'dB'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 'm/s'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 'Dobson'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'Code'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 12:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 'J/kg'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 33:
            return 's'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 32:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 21:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 19:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 18:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 17:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 16:
            return 'Proportion'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 15:
            return 'J/kg'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 10:
            return 'Code'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 9:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 8:
            return 'Code'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return '%'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50:
            return 'Numeric'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'M/S'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'fraction'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 38:
            return 'kg/kg/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return 'code'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return 'code'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return 'code'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return 'code'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 'code'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 'kg/kg/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 21:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 20:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 19:
            return 'code'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18:
            return 'kg/m3'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 17:
            return 'day'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'fraction'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'fraction'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'm/s'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pa'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return ' m'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62000:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40009:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62012:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63016:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63015:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63014:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40008:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63018:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63017:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62001:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40008:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40009:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62008:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 23:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63012:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63013:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 2:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 3:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 4:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10000:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 19:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 0:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63004:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 9:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60004:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60003:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63001:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63009:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63007:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 17:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 5:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 11:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63005:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63008:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63006:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10500:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 22:
            return '-'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 8:
            return '-'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'm/s'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'J/kg'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'J/kg'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'J/kg'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0:
            return 'code'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return '?'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 19:
            return 'Fraction'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'Fraction'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'J'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18:
            return 'N/m2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17:
            return 'N/m2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'W/m3/sr'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'W/m/sr'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 2:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 2:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'W/m2'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'W/m2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'deg. true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'deg. true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'deg. true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 's'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'm'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'deg. true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16:
            return 'kg/m2'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return '1/s'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 'm/s'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 'm/s'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 'm/s'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'm/s'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'deg. true'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'Fraction'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'kg/m3'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 'kg/kg'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 'kg/m2'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return '%'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'Fraction'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return '%'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return '%'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'm'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'm'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 8:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 'kg/m2/s'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 6:
            return 'm of water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'Pa'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'kg/m2'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2:
            return 'kg/kg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return '%'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'kg/kg'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'm/s'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'm/s'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'm/s'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'Deg. true'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'Pa/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return '1/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'm2/s2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'm2/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'm2/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'm/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'Deg. true'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return '-'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return '-'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return '-'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 'Gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 'Pa'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return '-'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return '-'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6:
            return '-'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 'K/m'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'K'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'K'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0:
            return 'Dobson'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'Gpm'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'm2/s2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'K*m2 / kg / s'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2:
            return 'Pa/s'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pa'

    return wrapped
