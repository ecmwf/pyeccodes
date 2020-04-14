import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        generatingProcessIdentifier = h.get_l('generatingProcessIdentifier')

        if generatingProcessIdentifier == 220:
            return 'm'

        if generatingProcessIdentifier == 219:
            return 'm'

        if generatingProcessIdentifier == 218:
            return 'm'

        if generatingProcessIdentifier == 217:
            return 'm'

        if generatingProcessIdentifier == 216:
            return 'm'

        if generatingProcessIdentifier == 215:
            return 'm'

        if generatingProcessIdentifier == 214:
            return 'm'

        if generatingProcessIdentifier == 213:
            return 'm'

        if generatingProcessIdentifier == 212:
            return 'm'

        if generatingProcessIdentifier == 211:
            return 'm'

        if generatingProcessIdentifier == 210:
            return 'm'

        if generatingProcessIdentifier == 209:
            return 'm'

        if generatingProcessIdentifier == 208:
            return 'm'

        if generatingProcessIdentifier == 207:
            return 'm'

        if generatingProcessIdentifier == 206:
            return 'm'

        if generatingProcessIdentifier == 205:
            return 'm'

        if generatingProcessIdentifier == 204:
            return 'm'

        if generatingProcessIdentifier == 120:
            return 'g'

        if generatingProcessIdentifier == 119:
            return 'g'

        if generatingProcessIdentifier == 118:
            return 'g'

        if generatingProcessIdentifier == 117:
            return 'g'

        if generatingProcessIdentifier == 116:
            return 'g'

        if generatingProcessIdentifier == 115:
            return 'g'

        if generatingProcessIdentifier == 114:
            return 'g'

        if generatingProcessIdentifier == 113:
            return 'g'

        if generatingProcessIdentifier == 112:
            return 'g'

        if generatingProcessIdentifier == 111:
            return 'g'

        if generatingProcessIdentifier == 110:
            return 'g'

        if generatingProcessIdentifier == 109:
            return 'g'

        if generatingProcessIdentifier == 108:
            return 'g'

        if generatingProcessIdentifier == 107:
            return 'g'

        if generatingProcessIdentifier == 106:
            return 'g'

        if generatingProcessIdentifier == 105:
            return 'g'

        if generatingProcessIdentifier == 104:
            return 'g'

        latitudeOfFirstGridPoint = h.get_l('latitudeOfFirstGridPoint')
        longitudeOfFirstGridPoint = h.get_l('longitudeOfFirstGridPoint')
        latitudeOfLastGridPoint = h.get_l('latitudeOfLastGridPoint')
        longitudeOfLastGridPoint = h.get_l('longitudeOfLastGridPoint')

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -90000 and longitudeOfLastGridPoint == 359750:
            return 'g'

        if latitudeOfFirstGridPoint == -500 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -81000 and longitudeOfLastGridPoint == 359500:
            return 's'

        if latitudeOfFirstGridPoint == 81000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == 0 and longitudeOfLastGridPoint == 359500:
            return 'n'

        if latitudeOfFirstGridPoint == 81000 and longitudeOfFirstGridPoint == 262000 and latitudeOfLastGridPoint == 9000 and longitudeOfLastGridPoint == 42000:
            return 'm'

        if latitudeOfFirstGridPoint == 81000 and longitudeOfFirstGridPoint == -98000 and latitudeOfLastGridPoint == 9000 and longitudeOfLastGridPoint == 42000:
            return 'm'

        if latitudeOfFirstGridPoint == 81000 and longitudeOfFirstGridPoint == -98000 and latitudeOfLastGridPoint == 5000 and longitudeOfLastGridPoint == 54000:
            return 'm'

        if latitudeOfFirstGridPoint == 66000 and longitudeOfFirstGridPoint == 354000 and latitudeOfLastGridPoint == 30000 and longitudeOfLastGridPoint == 42000:
            return 'm'

        if latitudeOfFirstGridPoint == 66000 and longitudeOfFirstGridPoint == -6000 and latitudeOfLastGridPoint == 30000 and longitudeOfLastGridPoint == 42000:
            return 'm'

        if latitudeOfFirstGridPoint == 89731 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -89731 and longitudeOfLastGridPoint == 359648:
            return 'g'

        if latitudeOfFirstGridPoint == 81000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -78000 and longitudeOfLastGridPoint == 357000:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -78000 and longitudeOfLastGridPoint == 359000:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -78000 and longitudeOfLastGridPoint == 359500:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -78120 and longitudeOfLastGridPoint == 359640:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -78000 and longitudeOfLastGridPoint == 359750:
            return 'g'

        if latitudeOfFirstGridPoint == 81000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -78000 and longitudeOfLastGridPoint == 357000:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -90000 and longitudeOfLastGridPoint == 357000:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -90000 and longitudeOfLastGridPoint == 359640:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -90000 and longitudeOfLastGridPoint == 359500:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -90000 and longitudeOfLastGridPoint == 359000:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -90000 and longitudeOfLastGridPoint == 358500:
            return 'g'

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -81000 and longitudeOfLastGridPoint == 358500:
            return 'g'

        if latitudeOfFirstGridPoint == 81000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -81000 and longitudeOfLastGridPoint == 358500:
            return 'g'

    return wrapped
