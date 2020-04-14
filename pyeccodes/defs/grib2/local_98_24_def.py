import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('channelNumber', 2))
    h.alias('mars.channel', 'channelNumber')
