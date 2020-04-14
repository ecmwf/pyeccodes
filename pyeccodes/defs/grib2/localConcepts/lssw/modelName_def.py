import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        generatingProcessIdentifier = h.get('generatingProcessIdentifier')

        if generatingProcessIdentifier == 101:
            return 'cosmo-1'

        if generatingProcessIdentifier == 102:
            return 'cosmo-2'

        if generatingProcessIdentifier == 107:
            return 'cosmo-7'

        if generatingProcessIdentifier == 103:
            return 'cosmo-e'

        if generatingProcessIdentifier == 130:
            return 'cosmo-e'

    return wrapped
