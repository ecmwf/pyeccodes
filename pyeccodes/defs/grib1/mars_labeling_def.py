import pyeccodes.accessors as _


def load(h):

    h.add(_.StringCodetable('marsClass', 1, "mars/class.table"))
    h.add(_.StringCodetable('marsType', 1, "mars/type.table"))
    h.add(_.StringCodetable('marsStream', 2, "mars/stream.table"))
    h.add(_.Ksec1expver('experimentVersionNumber', 4))
    h.alias('ls.dataType', 'marsType')
    h.alias('mars.class', 'marsClass')
    h.alias('mars.type', 'marsType')
    h.alias('mars.stream', 'marsStream')
    h.alias('mars.expver', 'experimentVersionNumber')
    h.alias('mars.domain', 'globalDomain')
