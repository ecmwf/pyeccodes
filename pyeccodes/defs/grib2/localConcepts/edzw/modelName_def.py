import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        gridDefinitionTemplateNumber = h.get_l('gridDefinitionTemplateNumber')
        Dx = h.get_l('Dx')
        Dy = h.get_l('Dy')
        generatingProcessIdentifier = h.get_l('generatingProcessIdentifier')

        if gridDefinitionTemplateNumber == 0 and Dx == 250000 and Dy == 250000 and generatingProcessIdentifier == 1:
            return 'icrgl_0.25'

        if gridDefinitionTemplateNumber == 0 and generatingProcessIdentifier == 1:
            return 'icrgl'

        if gridDefinitionTemplateNumber == 0 and generatingProcessIdentifier == 3:
            return 'icrde'

        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')

        if gridDefinitionTemplateNumber == 0 and Dx == 62500 and Dy == 62500 and typeOfFirstFixedSurface == 102 and generatingProcessIdentifier == 2:
            return 'icreu_0.625z'

        if gridDefinitionTemplateNumber == 0 and Dx == 62500 and Dy == 62500 and typeOfFirstFixedSurface == 100 and generatingProcessIdentifier == 2:
            return 'icreu_0.625p'

        nlev = h.get_l('nlev')

        if gridDefinitionTemplateNumber == 0 and Dx == 62500 and Dy == 62500 and nlev == 61 and generatingProcessIdentifier == 2:
            return 'icreu_0.625l60'

        if gridDefinitionTemplateNumber == 0 and Dx == 62500 and Dy == 62500 and generatingProcessIdentifier == 2:
            return 'icreu_0.625'

        if gridDefinitionTemplateNumber == 0 and generatingProcessIdentifier == 2:
            return 'icreu'

        numberOfGridUsed = h.get_l('numberOfGridUsed')

        if numberOfGridUsed == 27 and nlev == 61 and generatingProcessIdentifier == 2:
            return 'icoeu065l60'

        if numberOfGridUsed == 27 and generatingProcessIdentifier == 2:
            return 'icoeu065'

        if gridDefinitionTemplateNumber == 101 and generatingProcessIdentifier == 2:
            return 'icoeu'

        if numberOfGridUsed == 26 and typeOfFirstFixedSurface == 100 and generatingProcessIdentifier == 1:
            return 'icogl130p'

        if numberOfGridUsed == 26 and nlev == 91 and generatingProcessIdentifier == 1:
            return 'icogl130l90'

        if numberOfGridUsed == 26 and generatingProcessIdentifier == 1:
            return 'icogl130'

        if gridDefinitionTemplateNumber == 101 and generatingProcessIdentifier == 1:
            return 'icogl'

        typeOfEnsembleForecast = h.get_l('typeOfEnsembleForecast')

        if generatingProcessIdentifier == 138 and typeOfEnsembleForecast == 192:
            return 'cosmo_de-eps'

        if generatingProcessIdentifier == 137 and typeOfEnsembleForecast == 192:
            return 'cosmo_de-eps'

        if generatingProcessIdentifier == 138:
            return 'cosmo_de'

        if generatingProcessIdentifier == 137:
            return 'cosmo_de'

        if generatingProcessIdentifier == 135:
            return 'cosmo_eu'

        if generatingProcessIdentifier == 134:
            return 'cosmo_eu'

        if generatingProcessIdentifier == 132:
            return 'cosmo_eu'

        if generatingProcessIdentifier == 131:
            return 'cosmo_eu'

    return wrapped
