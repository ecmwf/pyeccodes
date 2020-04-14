import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        matchAerosolBinNumber = h.get_l('matchAerosolBinNumber')

        if matchAerosolBinNumber == 255:
            return 'missing'

        if matchAerosolBinNumber == 100:
            return 'all'

        if matchAerosolBinNumber == 10:
            return 'bin10'

        if matchAerosolBinNumber == 9:
            return 'bin9'

        if matchAerosolBinNumber == 8:
            return 'bin8'

        if matchAerosolBinNumber == 7:
            return 'bin7'

        if matchAerosolBinNumber == 6:
            return 'bin6'

        if matchAerosolBinNumber == 5:
            return 'bin5'

        if matchAerosolBinNumber == 4:
            return 'bin4'

        if matchAerosolBinNumber == 3:
            return 'bin3'

        if matchAerosolBinNumber == 2:
            return 'bin2'

        if matchAerosolBinNumber == 1:
            return 'bin1'

        if matchAerosolBinNumber == 0:
            return 'none'

    return wrapped
