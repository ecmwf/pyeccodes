import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        matchLandType = h.get('matchLandType')

        if matchLandType == 0:
            return 'all'

        if matchLandType == 1:
            return 'water'

        if matchLandType == 2:
            return 'rural'

        if matchLandType == 3:
            return 'urban'

        if matchLandType == 4:
            return 'lowveg'

        if matchLandType == 5:
            return 'forest'

        if matchLandType == 6:
            return 'noveg'

        if matchLandType == 21:
            return 'pasture'

        if matchLandType == 22:
            return 'arable'

        if matchLandType == 23:
            return 'beechoak'

        if matchLandType == 24:
            return 'deciduous'

        if matchLandType == 25:
            return 'spruce'

        if matchLandType == 26:
            return 'pine'

        if matchLandType == 27:
            return 'wetland'

        if matchLandType == 28:
            return 'mountain'

        if matchLandType == 29:
            return 'birch'

        if matchLandType == 51:
            return 'ice'

        if matchLandType == 52:
            return 'snow'

        if matchLandType == 71:
            return 'hslowv'

        if matchLandType == 72:
            return 'hsfor'

        if matchLandType == 73:
            return 'politi'

        if matchLandType == 74:
            return 'mask'

        if matchLandType == 81:
            return 'regional'

        if matchLandType == 82:
            return 'long-range'

        if matchLandType == 83:
            return 'local'

        if matchLandType == 90:
            return 'zone'

        if matchLandType == 100:
            return 'top'

        if matchLandType == 150:
            return 'effdose'

        if matchLandType == 151:
            return 'skin'

        if matchLandType == 152:
            return 'thyroid'

        if matchLandType == 153:
            return 'lung'

        if matchLandType == 255:
            return 'missing'

    return wrapped
