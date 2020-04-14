import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('domain', "g"))
    h.add(_.Constant('levtype', "sfc"))
    h.add(_.Constant('param', "128.128"))
    h.alias('mars.param', 'param')
    h.alias('mars.levtype', 'levtype')
