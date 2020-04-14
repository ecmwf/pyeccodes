import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        generatingProcessIdentifier = h.get('generatingProcessIdentifier')

        if generatingProcessIdentifier == 131:
            return 'cosmo_eu'

        if generatingProcessIdentifier == 132:
            return 'cosmo_eu'

        if generatingProcessIdentifier == 134:
            return 'cosmo_eu'

        if generatingProcessIdentifier == 135:
            return 'cosmo_eu'

        if generatingProcessIdentifier == 137:
            return 'cosmo_de'

        if generatingProcessIdentifier == 138:
            return 'cosmo_de'

        typeOfEnsembleForecast = h.get('typeOfEnsembleForecast')

        if generatingProcessIdentifier == 137 and typeOfEnsembleForecast == 192:
            return 'cosmo_de-eps'

        if generatingProcessIdentifier == 138 and typeOfEnsembleForecast == 192:
            return 'cosmo_de-eps'

        gridDefinitionTemplateNumber = h.get('gridDefinitionTemplateNumber')

        if gridDefinitionTemplateNumber == 101 and generatingProcessIdentifier == 1:
            return 'icogl'

        numberOfGridUsed = h.get('numberOfGridUsed')

        if numberOfGridUsed == 26 and generatingProcessIdentifier == 1:
            return 'icogl130'

        nlev = h.get('nlev')

        if numberOfGridUsed == 26 and nlev == 91 and generatingProcessIdentifier == 1:
            return 'icogl130l90'

        typeOfFirstFixedSurface = h.get('typeOfFirstFixedSurface')

        if numberOfGridUsed == 26 and typeOfFirstFixedSurface == 100 and generatingProcessIdentifier == 1:
            return 'icogl130p'

        if gridDefinitionTemplateNumber == 101 and generatingProcessIdentifier == 2:
            return 'icoeu'

        if numberOfGridUsed == 27 and generatingProcessIdentifier == 2:
            return 'icoeu065'

        if numberOfGridUsed == 27 and nlev == 61 and generatingProcessIdentifier == 2:
            return 'icoeu065l60'

        if gridDefinitionTemplateNumber == 0 and generatingProcessIdentifier == 2:
            return 'icreu'

        Dx = h.get('Dx')
        Dy = h.get('Dy')

        if gridDefinitionTemplateNumber == 0 and Dx == 62500 and Dy == 62500 and generatingProcessIdentifier == 2:
            return 'icreu_0.625'

        if gridDefinitionTemplateNumber == 0 and Dx == 62500 and Dy == 62500 and nlev == 61 and generatingProcessIdentifier == 2:
            return 'icreu_0.625l60'

        if gridDefinitionTemplateNumber == 0 and Dx == 62500 and Dy == 62500 and typeOfFirstFixedSurface == 100 and generatingProcessIdentifier == 2:
            return 'icreu_0.625p'

        if gridDefinitionTemplateNumber == 0 and Dx == 62500 and Dy == 62500 and typeOfFirstFixedSurface == 102 and generatingProcessIdentifier == 2:
            return 'icreu_0.625z'

        if gridDefinitionTemplateNumber == 0 and generatingProcessIdentifier == 3:
            return 'icrde'

        if gridDefinitionTemplateNumber == 0 and generatingProcessIdentifier == 1:
            return 'icrgl'

        if gridDefinitionTemplateNumber == 0 and Dx == 250000 and Dy == 250000 and generatingProcessIdentifier == 1:
            return 'icrgl_0.25'

    return wrapped
