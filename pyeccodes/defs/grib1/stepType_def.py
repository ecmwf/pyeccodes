import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if timeRangeIndicator == 124:
            return 'avgia'

        if timeRangeIndicator == 123:
            return 'avgua'

        if timeRangeIndicator == 5:
            return 'diff'

        if timeRangeIndicator == 118:
            return 'max'

        centre = h.get_l('centre')

        if timeRangeIndicator == 2 and centre == 98:
            return 'max'

        if timeRangeIndicator == 119:
            return 'min'

        if timeRangeIndicator == 2 and centre == 98:
            return 'min'

        if timeRangeIndicator == 2:
            return 'accum'

        if timeRangeIndicator == 4:
            return 'accum'

        if timeRangeIndicator == 113:
            return 'avgfc'

        if timeRangeIndicator == 113:
            return 'avgd'

        if timeRangeIndicator == 3:
            return 'avg'

        if timeRangeIndicator == 1:
            return 'instant'

        if timeRangeIndicator == 10:
            return 'instant'

        if timeRangeIndicator == 0:
            return 'instant'

    return wrapped
