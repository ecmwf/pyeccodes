import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 225:
            return 86020225

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 224:
            return 86020224

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 223:
            return 86020223

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 222:
            return 86020222

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 221:
            return 86020221

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 220:
            return 86020220

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 210:
            return 86020210

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 204:
            return 86020204

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 203:
            return 86020203

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202:
            return 86020202

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201:
            return 86020201

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199:
            return 86020199

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198:
            return 86020198

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197:
            return 86020197

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194:
            return 86020194

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193:
            return 86020193

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192:
            return 86020192

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 197:
            return 86007197

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 196:
            return 86007196

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 86007195

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194:
            return 86007194

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 86007193

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 86007192

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 86003192

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 86000194

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 86000193

    return wrapped
