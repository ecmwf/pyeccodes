import pyeccodes.accessors as _


def load(h):

    if (h.get_l('class') != 8):
        h.add(_.Sprintf('marsGrid', "%d", _.Get('N')))
        h.alias('mars.grid', 'marsGrid')
    else:
        h.alias('mars.origin', 'centre')

