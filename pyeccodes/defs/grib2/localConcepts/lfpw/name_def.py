import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get('discipline')
        parameterCategory = h.get('parameterCategory')
        parameterNumber = h.get('parameterNumber')
        stepType = h.get('stepType')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10 and stepType == "accum":
            return 'Total convective Precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9 and stepType == "accum":
            return 'Total large scale precipitation'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'Convective Available Potential Energy instantaneous'

    return wrapped
