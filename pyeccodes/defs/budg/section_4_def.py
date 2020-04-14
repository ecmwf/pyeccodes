import pyeccodes.accessors as _


def load(h):

    h.add(_.Section_length('section4Length', 3))
    h.add(_.Unsigned('reserved1', 1))

    if (h.get_l('reserved1') == 0):
        h.add(_.Codeflag('missingDataFlag', 1, "grib1/1.table"))
        h.add(_.Unsigned('numberOfBytesPerInteger', 1))
        h.add(_.Unsigned('reserved', 2))
        h.add(_.Unsigned('numberOfChars', 3))
        h.add(_.Unsigned('numberOfFloats', 3))
        h.add(_.Unsigned('numberOfIntegers', 3))
        h.alias('numberOfInts', 'numberOfIntegers')
        h.add(_.Unsigned('numberOfLogicals', 3))
        h.add(_.Unsigned('numberOfReservedBytes', 3))
        h.add(_.Unsigned('reserved', 4))
        h.add(_.Unsigned('reserved', 4))
        h.add(_.Unsigned('reserved', 1))
        h.add(_.Ibmfloat('floatValues', 4, _.Get('numberOfFloats')))
        h.alias('floatVal', 'floatValues')

        if (h.get_l('numberOfBytesPerInteger') == 1):
            h.add(_.Signed('integerValues', 1, _.Get('numberOfIntegers')))

        if (h.get_l('numberOfBytesPerInteger') == 2):
            h.add(_.Signed('integerValues', 2, _.Get('numberOfIntegers')))

        if (h.get_l('numberOfBytesPerInteger') == 3):
            h.add(_.Signed('integerValues', 3, _.Get('numberOfIntegers')))

        if (h.get_l('numberOfBytesPerInteger') == 4):
            h.add(_.Signed('integerValues', 4, _.Get('numberOfIntegers')))

        if (h.get_l('numberOfChars') >= 12):
            h.add(_.Ascii('marsClass', 2))
            h.add(_.Ascii('dummy1', 2))
            h.add(_.Ascii('marsType', 2))
            h.add(_.Ascii('dummy2', 2))
            h.add(_.Ascii('experimentVersionNumber', 4))
            h.alias('expver', 'experimentVersionNumber')
            h.alias('marsExpver', 'experimentVersionNumber')
            h.add(_.Constant('numberOfRemaininChars', (_.Get('numberOfChars') - 12)))

            with h.list('charValues'):
                for i in range(0, h.get_l('numberOfRemaininChars')):
                    h.add(_.Ascii('char', 1))
            h.add(_.Constant('zero', 0))

            def isEps_inline_concept(h):
                def wrapped(h):

                    marsType = h.get_s('marsType')

                    if marsType == "pf":
                        return 1

                return wrapped

            h.add(_.Concept('isEps', 'zero', concepts=isEps_inline_concept(h)))

            def isSens_inline_concept(h):
                def wrapped(h):

                    marsType = h.get_s('marsType')

                    if marsType == "sf":
                        return 1

                return wrapped

            h.add(_.Concept('isSens', 'zero', concepts=isSens_inline_concept(h)))

            h.add(_.Constant('oper', "oper"))

            def marsStream_inline_concept(h):
                def wrapped(h):

                    marsType = h.get_s('marsType')

                    if marsType == "pf":
                        return 'enfo'

                    if marsType == "cf":
                        return 'enfo'

                    if marsType == "sf":
                        return 'sens'

                return wrapped

            h.add(_.Concept('marsStream', 'oper', concepts=marsStream_inline_concept(h)))

            if h.get_l('isEps'):
                h.add(_.Constant('perturbationNumber', 0))
                h.alias('mars.number', 'perturbationNumber')

            if h.get_l('isSens'):
                h.add(_.Constant('iterationNumber', 0))
                h.add(_.Constant('diagnosticNumber', 0))
                h.alias('mars.iteration', 'iterationNumber')
                h.alias('mars.diagnostic', 'diagnosticNumber')

            h.alias('mars.stream', 'marsStream')
            h.alias('mars.class', 'marsClass')
            h.alias('mars.type', 'marsType')
            h.alias('mars.expver', 'marsExpver')
        else:

            with h.list('charValues'):
                for i in range(0, h.get_l('numberOfChars')):
                    h.add(_.Ascii('char', 1))

    else:
        h.add(_.Section_padding('padding'))

