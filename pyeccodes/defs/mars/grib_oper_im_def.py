import pyeccodes.accessors as _


def load(h):

    h.unalias('mars.levtype')

    if (h.get_l('localDefinitionNumber') == 3):
        h.add(_.Constant('marsType', "oldim"))
        h.alias('mars.type', 'marsType')
        h.alias('mars.ident', 'indicatorOfTypeOfLevel')

        if (h.get_l('marsStream') < 1024):
            h.alias('mars.ident', 'marsStream')

        h.unalias('mars.step')

    if (h.get_l('localDefinitionNumber') == 24):
        h.unalias('mars.param')
        h.unalias('mars.step')

