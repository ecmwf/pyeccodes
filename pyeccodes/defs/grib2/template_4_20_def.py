import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('parameterCategory', 1, "4.1.[discipline:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('parameterNumber', 1, "4.2.[discipline:l].[parameterCategory:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_units('parameterUnits', _.Get('parameterNumber')))
    h.add(_.Codetable_title('parameterName', _.Get('parameterNumber')))
    h.add(_.Codetable('typeOfGeneratingProcess', 1, "4.3.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('numberOfRadarSitesUsed', 1))
    h.add(_.Codetable('indicatorOfUnitOfTimeRange', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('defaultStepUnits', 'one')
    _.Template('grib2/localConcepts/[centre:s]/default_step_units.def', True).load(h)
    h.add(_.TransientCodetable('stepUnits', 1, "stepUnits.table"))
    h.add(_.Unsigned('siteLatitude', 4))
    h.add(_.Unsigned('siteLongitude', 4))
    h.add(_.Unsigned('siteElevation', 2))
    h.add(_.Unsigned('siteId', 4))
    h.add(_.Unsigned('siteId', 2))
    h.add(_.Codetable('operatingMode', 1, "4.12.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('reflectivityCalibrationConstant', 1))
    h.add(_.Codetable('qualityControlIndicator', 1, "4.13.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('clutterFilterIndicator', 1, "4.14.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('constantAntennaElevationAngle', 1))
    h.add(_.Unsigned('accumulationInterval', 2))
    h.add(_.Unsigned('referenceReflectivityForEchoTop', 1))
    h.add(_.Unsigned('rangeBinSpacing', 3))
    h.add(_.Unsigned('radialAngularSpacing', 2))
