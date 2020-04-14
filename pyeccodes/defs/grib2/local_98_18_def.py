import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('dataOrigin', 1, "common/c-1.table"))
    h.alias('mars.origin', 'dataOrigin')
    h.add(_.Ascii('modelIdentifier', 4))
    h.add(_.Unsigned('consensusCount', 1))

    with h.list('consensus'):
        for i in range(0, h.get_l('consensusCount')):
            h.add(_.Ascii('ccccIdentifiers', 4))
    h.alias('local.dataOrigin', 'dataOrigin')
    h.alias('local.modelIdentifier', 'modelIdentifier')
    h.alias('local.consensusCount', 'consensusCount')
