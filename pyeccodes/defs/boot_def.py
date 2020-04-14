import pyeccodes.accessors as _


def load(h):

    h.add(_.Transient('parametersVersion', 1))
    h.add(_.Constant('definitionFilesVersion', "2.0.0.0"))
    h.add(_.Constant('internalVersion', 30))
    h.add(_.Check_internal_version('checkInternalVersion', _.Get('internalVersion')))
    h.add(_.Getenv('UseEcmfConventions', "ECCODES_USE_ECMF_CONVENTIONS", "1"))
    h.add(_.Constant('defaultTypeOfLevel', "unknown"))
    h.add(_.Getenv('gribDataQualityChecks', "ECCODES_GRIB_DATA_QUALITY_CHECKS", "0"))

    if h.get_l('gribDataQualityChecks'):
        _.Template('param_limits.def').load(h)

    h.add(_.Getenv('GRIBEX_boustrophedonic', "ECCODES_GRIBEX_BOUSTROPHEDONIC", "0"))
    h.add(_.Constant('zero', 0))
    h.add(_.Constant('one', 1))
    h.add(_.Constant('hundred', 100))
    h.add(_.Transient('truncateLaplacian', 0))
    h.add(_.Constant('marsDir', "mars"))
    h.add(_.Constant('present', 1))
    h.add(_.Constant('defaultParameter', 0))
    h.add(_.Constant('defaultName', "unknown"))
    h.add(_.Constant('defaultShortName', "unknown"))
    h.add(_.Transient('truncateDegrees', 0))
    h.add(_.Transient('dummy', 1))
    h.add(_.Constant('unknown', "unknown"))
    h.add(_.Constant('oneConstant', 1))
    h.add(_.Constant('thousand', 1000))
    h.add(_.Constant('oneMillionConstant', 1000000))
    h.add(_.Constant('grib1divider', 1000))
    h.add(_.Offset_file('offset'))
    h.add(_.Count_file('count'))
    h.add(_.Count_total('countTotal'))
    h.add(_.Transient('file', "unknown"))
    h.add(_.Transient('changingPrecision', 0))
    h.add(_.Transient('unitsFactor', 1))
    h.add(_.Transient('unitsBias', 0))
    h.add(_.Constant('globalDomain', "g"))
    h.add(_.Transient('timeRangeIndicatorFromStepRange', -1))
    h.add(_.Transient('produceLargeConstantFields', 0))
    h.add(_.Library_version('libraryVersion'))
    h.add(_.Lookup('kindOfProduct', 4, 0, _.Get('identifier')))

    if (h.get_l('kindOfProduct') == 1196575042):
        h.add(_.Lookup('GRIBEditionNumber', 1, 7, _.Get('editionNumber')))
        _.Template('grib[GRIBEditionNumber:l]/boot.def').load(h)

    if (h.get_l('kindOfProduct') == 1112884295):
        _.Template('budg/boot.def').load(h)

    if (h.get_l('kindOfProduct') == 1145651527):
        _.Template('diag/boot.def').load(h)

    if (h.get_l('kindOfProduct') == 1414087749):
        _.Template('tide/boot.def').load(h)

    if (h.get_l('kindOfProduct') == 1112884818):
        _.Template('bufr/boot.def').load(h)

    if (h.get_l('kindOfProduct') == 1128547928):
        _.Template('cdf/boot.def').load(h)
        h.add(_.Constant('CDFstr', "netCDF"))
        h.alias('ls.identifier', 'CDFstr')

    if (h.get_l('kindOfProduct') == 17632522):
        _.Template('gts/boot.def').load(h)
        h.add(_.Constant('GTSstr', "GTS"))
        h.alias('ls.identifier', 'GTSstr')

    if (h.get_l('kindOfProduct') == 1296389185):
        _.Template('metar/boot.def').load(h)
        h.add(_.Constant('METARstr', "METAR"))
        h.alias('identifier', 'METARstr')

    if (h.get_l('kindOfProduct') == 1413563936):
        _.Template('taf/boot.def').load(h)
        h.add(_.Constant('TAFstr', "TAF"))
        h.alias('ls.identifier', 'TAFstr')

    if (h.get_l('kindOfProduct') == 2303214662):
        _.Template('hdf5/boot.def').load(h)
        h.add(_.Constant('HDF5str', "HDF5"))
        h.alias('ls.identifier', 'HDF5str')

    if (h.get_l('kindOfProduct') == 1465008464):
        _.Template('wrap/boot.def').load(h)
        h.add(_.Constant('WRAPstr', "WRAP"))
        h.alias('ls.identifier', 'WRAPstr')

