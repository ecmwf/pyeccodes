import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

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

        if latitudeOfFirstGridPoint == 81000 and longitudeOfFirstGridPoint == -98000 and latitudeOfLastGridPoint == 5100 and longitudeOfLastGridPoint == 53950:
            return 'm'

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

        if latitudeOfFirstGridPoint == 90000 and longitudeOfFirstGridPoint == 0 and latitudeOfLastGridPoint == -90000 and longitudeOfLastGridPoint == 359750:
            return 'g'

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
