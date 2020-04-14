import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        timeRangeIndicator = h.get('timeRangeIndicator')

        if timeRangeIndicator == 0:
            return 'instant'

        if timeRangeIndicator == 10:
            return 'instant'

        if timeRangeIndicator == 1:
            return 'instant'

        if timeRangeIndicator == 14:
            return 'instant'

        if timeRangeIndicator == 3:
            return 'avg'

        if timeRangeIndicator == 113:
            return 'avgd'

        if timeRangeIndicator == 113:
            return 'avgfc'

        if timeRangeIndicator == 4:
            return 'accum'

        if timeRangeIndicator == 2:
            return 'accum'

        centre = h.get('centre')

        if timeRangeIndicator == 2 and centre == 98:
            return 'min'

        if timeRangeIndicator == 119:
            return 'min'

        if timeRangeIndicator == 2 and centre == 98:
            return 'max'

        if timeRangeIndicator == 118:
            return 'max'

        if timeRangeIndicator == 5:
            return 'diff'

        if timeRangeIndicator == 120:
            return 'rms'

        if timeRangeIndicator == 121:
            return 'sd'

        if timeRangeIndicator == 122:
            return 'cov'

        if timeRangeIndicator == 123:
            return 'avgua'

        if timeRangeIndicator == 124:
            return 'avgia'

        if timeRangeIndicator == 128:
            return 'avgas'

        if timeRangeIndicator == 130:
            return 'avgad'

        if timeRangeIndicator == 133:
            return 'avgid'

    return wrapped
