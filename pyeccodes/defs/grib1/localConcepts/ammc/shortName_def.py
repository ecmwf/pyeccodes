import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if indicatorOfParameter == 1:
            return 0

    return wrapped
