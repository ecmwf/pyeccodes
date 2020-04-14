import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if timeRangeIndicator == 5:
            return 'diff'

        if timeRangeIndicator == 4:
            return 'accum'

        if timeRangeIndicator == 3:
            return 'avg'

        if timeRangeIndicator == 2:
            return 'min'

        if timeRangeIndicator == 2:
            return 'max'

        if timeRangeIndicator == 0:
            return 'instant'

        centre = h.get_l('centre')
        table2Version = h.get_l('table2Version')

        if centre == 78 and table2Version == 208:
            return 'max'

        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if centre == 78 and indicatorOfParameter == 16 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 15 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 14 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 13 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 12 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 11 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 10 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 9 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 8 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 7 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 6 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 5 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 4 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 3 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 2 and table2Version == 204:
            return 'rms'

        if centre == 78 and indicatorOfParameter == 1 and table2Version == 204:
            return 'rms'

        if timeRangeIndicator == 124:
            return 'avgia'

        if timeRangeIndicator == 123:
            return 'avgua'

        if timeRangeIndicator == 122:
            return 'cov'

        if timeRangeIndicator == 121:
            return 'sd'

        if timeRangeIndicator == 120:
            return 'rms'

        if timeRangeIndicator == 5:
            return 'diff'

        if timeRangeIndicator == 2 and centre == 98:
            return 'min'

        if timeRangeIndicator == 119:
            return 'min'

        if timeRangeIndicator == 2 and centre == 98:
            return 'max'

        if timeRangeIndicator == 118:
            return 'max'

        if timeRangeIndicator == 4:
            return 'accum'

        if timeRangeIndicator == 2:
            return 'accum'

        if timeRangeIndicator == 113:
            return 'avgd'

        if timeRangeIndicator == 113:
            return 'avgfc'

        if timeRangeIndicator == 14 and centre == 78:
            return 'instant'

        if timeRangeIndicator == 11 and centre == 78:
            return 'instant'

        if timeRangeIndicator == 13 and centre == 78:
            return 'instant'

        if timeRangeIndicator == 10:
            return 'instant'

        if timeRangeIndicator == 1:
            return 'instant'

        if timeRangeIndicator == 14:
            return 'instant'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 57 and table2Version == 2:
            return 'max'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 42 and table2Version == 201:
            return 'max'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 187 and table2Version == 201:
            return 'max'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 16 and table2Version == 2:
            return 'min'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 15 and table2Version == 2:
            return 'max'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 70 and table2Version == 202:
            return 'min'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 69 and table2Version == 202:
            return 'max'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 68 and table2Version == 202:
            return 'min'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 67 and table2Version == 202:
            return 'max'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 16 and table2Version == 206:
            return 'min'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 15 and table2Version == 206:
            return 'max'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 56 and table2Version == 203:
            return 'min'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 55 and table2Version == 203:
            return 'max'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 187 and table2Version == 201:
            return 'max'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 16 and table2Version == 2:
            return 'min'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 78 and table2Version == 202:
            return 'max'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 15 and table2Version == 2:
            return 'max'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 16 and table2Version == 2:
            return 'min'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 16 and table2Version == 2:
            return 'min'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 15 and table2Version == 2:
            return 'max'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 15 and table2Version == 2:
            return 'max'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 187 and table2Version == 201:
            return 'max'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 187 and table2Version == 201:
            return 'max'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 243 and table2Version == 202:
            return 'max'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 248 and table2Version == 202:
            return 'max'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 69 and table2Version == 202:
            return 'max'

        if timeRangeIndicator == 2 and centre == 78 and indicatorOfParameter == 67 and table2Version == 202:
            return 'max'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 78 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 113 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 79 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 57 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 42 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 90 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 79 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 113 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 90 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 78 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 61 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 61 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 102 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 102 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 113 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 132 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 132 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 102 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 233 and table2Version == 202:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 232 and table2Version == 202:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 231 and table2Version == 202:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 233 and table2Version == 202:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 232 and table2Version == 202:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 231 and table2Version == 202:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 24 and table2Version == 201:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 23 and table2Version == 201:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 22 and table2Version == 201:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 5 and table2Version == 201:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 24 and table2Version == 201:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 23 and table2Version == 201:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 22 and table2Version == 201:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 5 and table2Version == 201:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 122 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 121 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 125 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 124 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 125 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 124 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 122 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 121 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 114 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 113 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 112 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 13 and centre == 78 and indicatorOfParameter == 111 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 114 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 113 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 112 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 1 and centre == 78 and indicatorOfParameter == 111 and table2Version == 2:
            return 'avg'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 42 and table2Version == 201:
            return 'accum'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 90 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 79 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 78 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 61 and table2Version == 2:
            return 'accum'

        if timeRangeIndicator == 0 and centre == 78 and indicatorOfParameter == 57 and table2Version == 2:
            return 'accum'

    return wrapped
