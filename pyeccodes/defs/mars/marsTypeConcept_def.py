import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        marsType = h.get_s('marsType')

        if marsType == "pf":
            return 'ep'

        if marsType == "pf":
            return 'cp'

        if marsType == "pf":
            return 'pf'

        if marsType == "cf":
            return 'cf'

        if marsType == "fc":
            return 'fc'

        if marsType == "an":
            return 'an'

        if marsType == "ia":
            return 'an'

    return wrapped
