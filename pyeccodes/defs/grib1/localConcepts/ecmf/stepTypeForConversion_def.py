import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        timeRangeIndicator = h.get('timeRangeIndicator')
        indicatorOfParameter = h.get('indicatorOfParameter')
        gribTablesVersionNo = h.get('gribTablesVersionNo')
        centre = h.get('centre')

        if timeRangeIndicator == 0 and indicatorOfParameter == 228 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if timeRangeIndicator == 1 and indicatorOfParameter == 228 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if timeRangeIndicator == 10 and indicatorOfParameter == 228 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if indicatorOfParameter == 146 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if indicatorOfParameter == 147 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if indicatorOfParameter == 169 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if indicatorOfParameter == 175 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if indicatorOfParameter == 176 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if indicatorOfParameter == 177 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if indicatorOfParameter == 179 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

        if indicatorOfParameter == 189 and gribTablesVersionNo == 128 and centre == 98:
            return 'accum'

    return wrapped
