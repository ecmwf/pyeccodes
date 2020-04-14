import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 225:
            return 0

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 224:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 223:
            return 0

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 222:
            return 'degreeday'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 221:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 220:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 210:
            return 'bq m-3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 204:
            return 'bq m-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 203:
            return 'mol m-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202:
            return 'm-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201:
            return 'kg m-2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199:
            return 'bq m-2 s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198:
            return 'mol m-2 s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197:
            return 'm-2 s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194:
            return 'bq m-2 s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193:
            return 'mol m-2 s-1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192:
            return 'm-2 s-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 197:
            return 's-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 196:
            return 'kg m-3'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 'K'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 'm s-1'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 'm-1'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'm'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 'W m-2'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'W m-2'

    return wrapped
