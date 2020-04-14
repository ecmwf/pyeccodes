import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', 0))
    _.Template('grib1/mars_labeling.def').load(h)
    h.add(_.Transient('localFlag', 1))
    h.add(_.Constant('oceanStream', 1090))

    if (h.get_l('marsStream') == h.get_l('oceanStream')):
        h.add(_.Unsigned('perturbationNumber', 2))

    if (h.get_l('marsStream') != h.get_l('oceanStream')):
        h.add(_.Unsigned('perturbationNumber', 1))
        h.add(_.Pad('padding_loc4_2', 1))

    h.add(_.Unsigned('flagShowingPostAuxiliaryArrayInUse', 1))
    h.add(_.Unsigned('systemNumber', 1))
    h.alias('system', 'systemNumber')
    h.add(_.Unsigned('methodNumber', 1))
    h.add(_.Unsigned('spaceUnitFlag', 1))
    h.add(_.Unsigned('verticalCoordinateDefinition', 1))
    h.add(_.Unsigned('horizontalCoordinateDefinition', 1))
    h.add(_.Unsigned('timeUnitFlag', 1))
    h.add(_.Unsigned('timeCoordinateDefinition', 1))
    h.add(_.Unsigned('mixedCoordinateFieldFlag', 1))
    h.add(_.Unsigned('coordinate1Flag', 1))
    h.add(_.Unsigned('averaging1Flag', 1))
    h.add(_.Signed('coordinate1Start', 4))
    h.add(_.Signed('coordinate1End', 4))
    h.add(_.Unsigned('coordinate2Flag', 1))
    h.add(_.Unsigned('averaging2Flag', 1))
    h.add(_.Signed('coordinate2Start', 4))
    h.add(_.Signed('coordinate2End', 4))
    h.add(_.Unsigned('coordinate3Flag', 1))
    h.add(_.Unsigned('coordinate4Flag', 1))
    h.add(_.Signed('coordinate4OfFirstGridPoint', 4))
    h.add(_.Signed('coordinate3OfFirstGridPoint', 4))
    h.add(_.Signed('coordinate4OfLastGridPoint', 4))
    h.add(_.Signed('coordinate3OfLastGridPoint', 4))
    h.add(_.Signed('iIncrement', 4))
    h.add(_.Signed('jIncrement', 4))
    h.add(_.Codeflag('flagForIrregularGridCoordinateList', 1, "grib1/ocean.1.table"))
    h.add(_.Codeflag('flagForNormalOrStaggeredGrid', 1, "grib1/ocean.1.table"))
    h.add(_.Codeflag('flagForAnyFurtherInformation', 1, "grib1/ocean.1.table"))
    h.add(_.Unsigned('numberInHorizontalCoordinates', 1))
    h.add(_.Unsigned('numberInMixedCoordinateDefinition', 2))
    h.add(_.Unsigned('numberInTheGridCoordinateList', 2))
    h.add(_.Unsigned('numberInTheAuxiliaryArray', 2))
    h.add(_.Unsigned('horizontalCoordinateSupplement', 4, _.Get('numberInHorizontalCoordinates')))
    h.add(_.Unsigned('mixedCoordinateDefinition', 4, _.Get('numberInMixedCoordinateDefinition')))

    if (h.get_l('numberInTheGridCoordinateList') > 0):
        h.add(_.Signed('gridCoordinate', 4, _.Get('numberInTheGridCoordinateList')))

    h.add(_.Unsigned('auxiliary', 4, _.Get('numberInTheAuxiliaryArray')))
    h.add(_.Constant('postAuxiliaryArrayPresent', 1))

    if (h.get_l('flagShowingPostAuxiliaryArrayInUse') == h.get_l('postAuxiliaryArrayPresent')):
        h.add(_.Unsigned('sizeOfPostAuxiliaryArrayPlusOne', 4))
        h.add(_.Evaluate('sizeOfPostAuxiliaryArray', (_.Get('sizeOfPostAuxiliaryArrayPlusOne') - 1)))

        if (h.get_l('sizeOfPostAuxiliaryArray') > 0):
            h.add(_.Unsigned('postAuxiliary', 4, _.Get('sizeOfPostAuxiliaryArray')))

            if (h.get_l('sizeOfPostAuxiliaryArray') > 3):
                h.add(_.Element('referenceDate', _.Get('postAuxiliary'), 3))

        else:
            h.add(_.Transient('referenceDate', 0))


    h.alias('hdate', 'dataDate')
    _.Template('grib1/mars_labeling.4.def').load(h)
