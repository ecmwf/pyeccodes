import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        originatingCentre = h.get_l('originatingCentre')

        if originatingCentre == 242:
            return 'cosmo-romania'

        if originatingCentre == 220:
            return 'cosmo-poland'

        if originatingCentre == 96:
            return 'cosmo-greece'

        generatingProcessIdentifier = h.get_l('generatingProcessIdentifier')

        if originatingCentre == 76 and generatingProcessIdentifier == 235:
            return 'cosmo_ru-eps'

        if originatingCentre == 76 and generatingProcessIdentifier == 135:
            return 'cosmo_ru'

        if originatingCentre == 200 and generatingProcessIdentifier == 131:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 46:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 42:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 38:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 34:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 32:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 31:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 148:
            return 'cosmo-i2'

        if originatingCentre == 200 and generatingProcessIdentifier == 144:
            return 'cosmo-i2'

        if originatingCentre == 200 and generatingProcessIdentifier == 139:
            return 'cosmo-i2'

        if originatingCentre == 200 and generatingProcessIdentifier == 36:
            return 'cosmo-i2'

        subCentre = h.get_l('subCentre')

        if subCentre == 250:
            return 'cosmo'

        if originatingCentre == 250:
            return 'cosmo'

    return wrapped
