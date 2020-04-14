import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection3'))
    h.add(_.Transient('section3Length', 1))
    h.add(_.Section_pointer('section3Pointer', _.Get('offsetSection3'), _.Get('section3Length'), 3))
    h.add(_.Transient('numberOfUnusedBitsAtEndOfSection3', 0))
    h.add(_.Transient('tableReference', 0))
    h.add(_.Gds_not_present_bitmap('bitmap', _.Get('missingValue'), _.Get('numberOfValues'), _.Get('numberOfPoints'), _.Get('latitudeOfFirstGridPoint'), _.Get('Ni'), _.Get('numberOfUnusedBitsAtEndOfSection3')))
