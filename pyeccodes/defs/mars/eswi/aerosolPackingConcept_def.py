import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        matchAerosolBinNumber = h.get_l('matchAerosolBinNumber')

        if matchAerosolBinNumber == 5:
            return '1-5'

        if matchAerosolBinNumber == 4:
            return '1-5'

        if matchAerosolBinNumber == 3:
            return '1-5'

        if matchAerosolBinNumber == 2:
            return '1-5'

        if matchAerosolBinNumber == 1:
            return '1-5'

        if matchAerosolBinNumber == 0:
            return 0

    return wrapped
