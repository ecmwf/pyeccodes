import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('marsStream', "oper"))
    h.alias('mars.stream', 'marsStream')
    h.add(_.Constant('marsDomain', "g"))
    h.alias('mars.domain', 'marsDomain')
