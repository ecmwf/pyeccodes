import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        generatingProcessIdentifier = h.get_l('generatingProcessIdentifier')

        if generatingProcessIdentifier == 255:
            return 'default'

        if generatingProcessIdentifier == 210:
            return 'arome-france-dble-1'

        if generatingProcessIdentifier == 209:
            return 'arome-france-dble-6'

        if generatingProcessIdentifier == 213:
            return 'arome-france-oper-1'

        if generatingProcessIdentifier == 204:
            return 'arome-france-oper-6'

        if generatingProcessIdentifier == 22:
            return 'arpege-france-dble-forecast-assim'

        if generatingProcessIdentifier == 212:
            return 'arpege-france-dble-forecast-production'

        if generatingProcessIdentifier == 12:
            return 'arpege-france-oper-forecast-assim'

        if generatingProcessIdentifier == 211:
            return 'arpege-france-oper-forecast-production'

    return wrapped
