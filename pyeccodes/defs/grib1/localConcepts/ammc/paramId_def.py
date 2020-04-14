import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        indicatorOfParameter = h.get('indicatorOfParameter')

        if indicatorOfParameter == 1:
            return 999999999

    return wrapped
