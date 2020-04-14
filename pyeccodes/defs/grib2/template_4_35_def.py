import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('dataRepresentationType', 90))
    h.add(_.Codetable('parameterCategory', 1, "4.1.[discipline:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('parameterNumber', 1, "4.2.[discipline:l].[parameterCategory:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_units('parameterUnits', _.Get('parameterNumber')))
    h.add(_.Codetable_title('parameterName', _.Get('parameterNumber')))
    h.add(_.Codetable('typeOfGeneratingProcess', 1, "4.3.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('observationGeneratingProcessIdentifier', 1))
    h.alias('generatingProcessIdentifier', 'observationGeneratingProcessIdentifier')
    h.add(_.Codetable('qualityValueAssociatedWithParameter', 1, "4.16.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('NB', 1))
    h.alias('numberOfContributingSpectralBands', 'NB')

    with h.list('listOfContributingSpectralBands'):
        for i in range(0, h.get_l('numberOfContributingSpectralBands')):
            h.add(_.Unsigned('satelliteSeries', 2))
            h.add(_.Unsigned('satelliteNumber', 2))
            h.add(_.Unsigned('instrumentType', 2))
            h.add(_.Unsigned('scaleFactorOfCentralWaveNumber', 1))
            h.add(_.Unsigned('scaledValueOfCentralWaveNumber', 4))
