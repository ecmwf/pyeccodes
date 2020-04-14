import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        generatingProcessIdentifier = h.get_l('generatingProcessIdentifier')

        if generatingProcessIdentifier == 130:
            return 'cosmo-e'

        if generatingProcessIdentifier == 103:
            return 'cosmo-e'

        if generatingProcessIdentifier == 107:
            return 'cosmo-7'

        if generatingProcessIdentifier == 102:
            return 'cosmo-2'

        if generatingProcessIdentifier == 101:
            return 'cosmo-1'

    return wrapped
