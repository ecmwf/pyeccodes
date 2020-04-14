import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('channelNumber', 4))
    h.alias('mars.channel', 'channelNumber')
