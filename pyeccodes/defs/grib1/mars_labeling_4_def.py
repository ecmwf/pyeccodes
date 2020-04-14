import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('P_INST', 0))
    h.add(_.Constant('P_TAVG', 1))
    h.add(_.Constant('P_TACC', 3))
    h.add(_.Constant('TYPE_AN', 2))
    h.add(_.Constant('TYPE_FC', 9))
    h.add(_.Constant('TYPE_CF', 10))
    h.add(_.Constant('TYPE_PF', 11))
    h.add(_.Constant('TYPE_FF', 25))
    h.add(_.Constant('TYPE_OF', 26))
    h.add(_.Constant('TYPE_OR', 70))
    h.add(_.Constant('TYPE_FX', 71))
    h.add(_.Constant('coordAveraging0', "inst"))
    h.add(_.Constant('coordAveraging1', "tavg"))
    h.add(_.Constant('coordAveraging2', 2))
    h.add(_.Constant('coordAveraging3', "tacc"))
    h.add(_.Constant('coordAveragingTims', "tims"))
    h.add(_.Constant('isectionNumber2', "h"))
    h.add(_.Constant('isectionNumber3', "m"))
    h.add(_.Constant('isectionNumber4', "z"))
    h.add(_.Constant('tsectionNumber3', "v"))
    h.add(_.Constant('tsectionNumber4', "z"))
    h.add(_.Constant('tsectionNumber5', "m"))
    h.add(_.Constant('GRIB_DEPTH', 2))
    h.add(_.Constant('GRIB_LONGITUDE', 3))
    h.add(_.Constant('GRIB_LATITUDE', 4))
    h.add(_.G1verificationdate('verificationDate', _.Get('dataDate'), _.Get('dataTime'), _.Get('endStep')))

    if (h.get_l('horizontalCoordinateDefinition') == 0):

        if (h.get_l('coordinate1Flag') == 1):

            if (h.get_l('averaging1Flag') == h.get_l('P_TAVG')):

                if ((((h.get_l('marsType') == h.get_l('TYPE_OR')) or (h.get_l('marsType') == h.get_l('TYPE_FC'))) or (h.get_l('marsType') == h.get_l('TYPE_FF'))) or (h.get_l('marsType') == h.get_l('TYPE_FX'))):
                    h.add(_.Evaluate('marsRange', ((_.Get('coordinate1End') - _.Get('coordinate1Start')) / 3600)))
                    h.alias('mars.range', 'marsRange')


            if (h.get_l('coordinate2Flag') == 2):
                h.alias('mars.section', 'isectionNumber2')

            if (h.get_l('coordinate2Flag') == 3):
                h.alias('mars.section', 'isectionNumber3')

            if (h.get_l('coordinate2Flag') == 4):
                h.alias('mars.section', 'isectionNumber4')

            if (h.get_l('coordinate2Flag') == h.get_l('GRIB_DEPTH')):
                h.add(_.Divdouble('marsLevelist', _.Get('coordinate2Start'), 1000))
                h.add(_.Round('roundedMarsLevelist', _.Get('marsLevelist'), 1000))
                h.alias('mars.levelist', 'roundedMarsLevelist')

            if (h.get_l('coordinate2Flag') == h.get_l('GRIB_LONGITUDE')):
                h.add(_.Divdouble('marsLongitude', _.Get('coordinate2Start'), 1000000))
                h.add(_.Round('roundedMarsLongitude', _.Get('marsLongitude'), 1000))
                h.alias('mars.longitude', 'roundedMarsLongitude')

            if (h.get_l('coordinate2Flag') == h.get_l('GRIB_LATITUDE')):
                h.add(_.Divdouble('marsLatitude', _.Get('coordinate2Start'), 1000000))
                h.add(_.Round('roundedMarsLatitude', _.Get('marsLatitude'), 1000))
                h.alias('mars.latitude', 'roundedMarsLatitude')

            if (h.get_l('averaging1Flag') == 0):
                h.alias('mars.product', 'coordAveraging0')

            if (h.get_l('averaging1Flag') == 1):
                h.alias('mars.product', 'coordAveraging1')

            if (h.get_l('averaging1Flag') == 2):
                h.alias('mars.product', 'coordAveraging2')

            if (h.get_l('averaging1Flag') == 3):
                h.alias('mars.product', 'coordAveraging3')

            if ((((h.get_l('marsType') == h.get_l('TYPE_OR')) and (h.get_l('averaging1Flag') == h.get_l('P_TAVG'))) or ((h.get_l('marsType') == h.get_l('TYPE_OR')) and (h.get_l('averaging1Flag') == h.get_l('P_TACC')))) or ((h.get_l('marsType') == h.get_l('TYPE_FX')) and (h.get_l('averaging1Flag') == h.get_l('P_TAVG')))):
                h.alias('mars.date', 'verificationDate')
                h.add(_.Constant('stepZero', 0))
                h.alias('mars.step', 'stepZero')

        else:
            h.add(_.Evaluate('coordinateIndexNumber', (_.Get('coordinate4Flag') + _.Get('coordinate3Flag'))))

            if (h.get_l('coordinateIndexNumber') == 3):
                h.add(_.Divdouble('marsLatitude', _.Get('coordinate1Start'), 1000000))
                h.add(_.Divdouble('marsLongitude', _.Get('coordinate2Start'), 1000000))
                h.add(_.Round('roundedMarsLatitude', _.Get('marsLatitude'), 1000))
                h.add(_.Round('roundedMarsLongitude', _.Get('marsLongitude'), 1000))
                h.alias('mars.latitude', 'roundedMarsLatitude')
                h.alias('mars.longitude', 'roundedMarsLongitude')

            if (h.get_l('coordinateIndexNumber') == 4):
                h.add(_.Divdouble('marsLevelist', _.Get('coordinate1Start'), 1000))
                h.add(_.Divdouble('marsLatitude', _.Get('coordinate2Start'), 1000000))
                h.add(_.Round('roundedMarsLevelist', _.Get('marsLevelist'), 1000))
                h.add(_.Round('roundedMarsLatitude', _.Get('marsLatitude'), 1000))
                h.alias('mars.levelist', 'roundedMarsLevelist')
                h.alias('mars.latitude', 'roundedMarsLatitude')

            if (h.get_l('coordinateIndexNumber') == 5):
                h.add(_.Divdouble('marsLevelist', _.Get('coordinate1Start'), 1000))
                h.add(_.Divdouble('marsLongitude', _.Get('coordinate2Start'), 1000000))
                h.add(_.Round('roundedMarsLevelist', _.Get('marsLevelist'), 1000))
                h.add(_.Round('roundedMarsLongitude', _.Get('marsLongitude'), 1000))
                h.alias('mars.levelist', 'roundedMarsLevelist')
                h.alias('mars.longitude', 'roundedMarsLongitude')

            if (h.get_l('coordinateIndexNumber') == 3):
                h.alias('mars.section', 'tsectionNumber3')

            if (h.get_l('coordinateIndexNumber') == 4):
                h.alias('mars.section', 'tsectionNumber4')

            if (h.get_l('coordinateIndexNumber') == 5):
                h.alias('mars.section', 'tsectionNumber5')

            if (h.get_l('averaging1Flag') == h.get_l('P_INST')):

                if ((((((h.get_l('marsType') == h.get_l('TYPE_OR')) or (h.get_l('marsType') == h.get_l('TYPE_FC'))) or (h.get_l('marsType') == h.get_l('TYPE_CF'))) or (h.get_l('marsType') == h.get_l('TYPE_PF'))) or (h.get_l('marsType') == h.get_l('TYPE_FF'))) or (h.get_l('marsType') == h.get_l('TYPE_OF'))):

                    if (h.get_l('coordinate4Flag') == 1):
                        h.add(_.Evaluate('marsRange', ((_.Get('coordinate4OfLastGridPoint') - _.Get('coordinate4OfFirstGridPoint')) / 3600)))
                    else:
                        h.add(_.Evaluate('marsRange', ((_.Get('coordinate3OfLastGridPoint') - _.Get('coordinate3OfFirstGridPoint')) / 3600)))

                    h.alias('mars.range', 'marsRange')


            h.alias('mars.product', 'coordAveragingTims')

            if ((h.get_l('marsType') == h.get_l('TYPE_OR')) and (h.get_l('averaging1Flag') == h.get_l('P_INST'))):
                h.alias('mars.date', 'verificationDate')
                h.add(_.Constant('stepZero', 0))
                h.alias('mars.step', 'stepZero')


