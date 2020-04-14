import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        timeRangeIndicator = h.get('timeRangeIndicator')

        if timeRangeIndicator == 1:
            return 'instant'

        if timeRangeIndicator == 10:
            return 'instant'

        if timeRangeIndicator == 0:
            return 'instant'

        if timeRangeIndicator == 3:
            return 'avg'

        if timeRangeIndicator == 113:
            return 'avgfc'

        if timeRangeIndicator == 113:
            return 'avgd'

        if timeRangeIndicator == 2:
            return 'accum'

        if timeRangeIndicator == 4:
            return 'accum'

        if timeRangeIndicator == 5:
            return 'diff'

        if timeRangeIndicator == 123:
            return 'avgua'

        if timeRangeIndicator == 124:
            return 'avgia'

        if timeRangeIndicator == 128:
            return 'avgas'

        if timeRangeIndicator == 130:
            return 'avgad'

        if timeRangeIndicator == 129:
            return 'varas'

        if timeRangeIndicator == 131:
            return 'varad'

        if timeRangeIndicator == 132:
            return 'varins'

    return wrapped
