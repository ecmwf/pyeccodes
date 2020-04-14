import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('tiggeModel', 2, "grib2/local/[localSubSectionCentre:l]/models.table"))
    h.add(_.Codetable('tiggeCentre', 2, "grib2/local/[localSubSectionCentre:l]/centres.table"))

    def tiggeLAMName_inline_concept(h):
        def wrapped(h):

            tiggeCentre = h.get_l('tiggeCentre')
            tiggeModel = h.get_l('tiggeModel')

            if tiggeCentre == 0 and tiggeModel == 0:
                return 'MOGREPS-MO- EUA'

            if tiggeCentre == 1 and tiggeModel == 1:
                return 'AEMet-SREPS-MM-EUAT'

            if tiggeCentre == 1 and tiggeModel == 2:
                return 'SRNWP-PEPS'

            if tiggeCentre == 2 and tiggeModel == 3:
                return 'COSMOLEPS-ARPASIMC-EU'

            if tiggeCentre == 3 and tiggeModel == 4:
                return 'NORLAMEPS'

            if tiggeCentre == 4 and tiggeModel == 5:
                return 'ALADIN-LAEF'

            if tiggeCentre == 5 and tiggeModel == 6:
                return 'COSMO-DE EPS'

            if tiggeCentre == 2 and tiggeModel == 7:
                return 'COSMO-SREPS-BO-EU'

            if tiggeCentre == 6 and tiggeModel == 8:
                return 'GLAMEPS'

            if tiggeCentre == 7 and tiggeModel == 9:
                return 'PEARCE'

            if tiggeCentre == 8 and tiggeModel == 10:
                return 'DMI- HIRLAM'

            if tiggeCentre == 9 and tiggeModel == 11:
                return 'OMSZ- ALADIN-EPS'

            if tiggeCentre == 10 and tiggeModel == 11:
                return 'OMSZ- ALADIN-EPS'

            if tiggeCentre == 11 and tiggeModel == 11:
                return 'OMSZ- ALADIN-EPS'

        return wrapped

    h.add(_.Concept('tiggeLAMName', None, concepts=tiggeLAMName_inline_concept(h)))

