import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        marsType = h.get('marsType')

        if marsType == "ia":
            return 'an'

        if marsType == "an":
            return 'an'

        if marsType == "fc":
            return 'fc'

        if marsType == "cf":
            return 'cf'

        if marsType == "pf":
            return 'pf'

        if marsType == "pf":
            return 'cp'

        if marsType == "pf":
            return 'ep'

    return wrapped
