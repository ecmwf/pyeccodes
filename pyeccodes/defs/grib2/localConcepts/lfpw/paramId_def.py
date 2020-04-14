import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 85001160

        stepType = h.get_s('stepType')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9 and stepType == "accum":
            return 85001157

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10 and stepType == "accum":
            return 85001156

    return wrapped
