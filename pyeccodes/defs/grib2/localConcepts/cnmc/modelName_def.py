import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        subCentre = h.get_l('subCentre')
        grib2LocalSectionNumber = h.get_l('grib2LocalSectionNumber')

        if subCentre == 98 and grib2LocalSectionNumber == 28:
            return 'cosmo-leps'

    return wrapped
