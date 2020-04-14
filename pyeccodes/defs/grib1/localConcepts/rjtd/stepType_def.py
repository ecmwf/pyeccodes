import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if timeRangeIndicator == 132:
            return 'varins'

        if timeRangeIndicator == 131:
            return 'varad'

        if timeRangeIndicator == 129:
            return 'varas'

        if timeRangeIndicator == 130:
            return 'avgad'

        if timeRangeIndicator == 128:
            return 'avgas'

        if timeRangeIndicator == 124:
            return 'avgia'

        if timeRangeIndicator == 123:
            return 'avgua'

        if timeRangeIndicator == 5:
            return 'diff'

        if timeRangeIndicator == 4:
            return 'accum'

        if timeRangeIndicator == 2:
            return 'accum'

        if timeRangeIndicator == 113:
            return 'avgd'

        if timeRangeIndicator == 113:
            return 'avgfc'

        if timeRangeIndicator == 3:
            return 'avg'

        if timeRangeIndicator == 0:
            return 'instant'

        if timeRangeIndicator == 10:
            return 'instant'

        if timeRangeIndicator == 1:
            return 'instant'

    return wrapped
