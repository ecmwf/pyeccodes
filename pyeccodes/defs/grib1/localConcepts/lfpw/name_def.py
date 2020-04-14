import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get('table2Version')
        indicatorOfParameter = h.get('indicatorOfParameter')
        stepType = h.get('stepType')

        if table2Version == 1 and indicatorOfParameter == 156 and stepType == "accum":
            return 'Total convective Precipitation'

        if table2Version == 1 and indicatorOfParameter == 157 and stepType == "accum":
            return 'Total large scale precipitation'

        if table2Version == 1 and indicatorOfParameter == 160:
            return 'Convective Available Potential Energy instantaneous'

    return wrapped
