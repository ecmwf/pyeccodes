import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        originatingCentre = h.get('originatingCentre')

        if originatingCentre == 250:
            return 'cosmo'

        subCentre = h.get('subCentre')

        if subCentre == 250:
            return 'cosmo'

        generatingProcessIdentifier = h.get('generatingProcessIdentifier')

        if originatingCentre == 200 and generatingProcessIdentifier == 36:
            return 'cosmo-i2'

        if originatingCentre == 200 and generatingProcessIdentifier == 139:
            return 'cosmo-i2'

        if originatingCentre == 200 and generatingProcessIdentifier == 144:
            return 'cosmo-i2'

        if originatingCentre == 200 and generatingProcessIdentifier == 148:
            return 'cosmo-i2'

        if originatingCentre == 200 and generatingProcessIdentifier == 31:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 32:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 34:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 38:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 42:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 46:
            return 'cosmo-i7'

        if originatingCentre == 200 and generatingProcessIdentifier == 131:
            return 'cosmo-i7'

        if originatingCentre == 76 and generatingProcessIdentifier == 135:
            return 'cosmo_ru'

        if originatingCentre == 76 and generatingProcessIdentifier == 235:
            return 'cosmo_ru-eps'

        if originatingCentre == 96:
            return 'cosmo-greece'

        if originatingCentre == 220:
            return 'cosmo-poland'

        if originatingCentre == 242:
            return 'cosmo-romania'

    return wrapped
