import pyeccodes.accessors as _


def load(h):

    h.add(_.Codeflag('resolutionAndComponentFlags', 1, "grib1/7.table"))
    h.add(_.Bit('ijDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 7))
    h.alias('iDirectionIncrementGiven', 'ijDirectionIncrementGiven')
    h.alias('jDirectionIncrementGiven', 'ijDirectionIncrementGiven')
    h.alias('DiGiven', 'ijDirectionIncrementGiven')
    h.alias('DjGiven', 'ijDirectionIncrementGiven')
    h.add(_.Bit('earthIsOblate', _.Get('resolutionAndComponentFlags'), 6))

    if h.get_l('earthIsOblate'):
        h.add(_.Transient('earthMajorAxis', 6.37816e+06))
        h.add(_.Transient('earthMinorAxis', 6.35678e+06))
        h.alias('earthMajorAxisInMetres', 'earthMajorAxis')
        h.alias('earthMinorAxisInMetres', 'earthMinorAxis')

    h.add(_.Bit('resolutionAndComponentFlags3', _.Get('resolutionAndComponentFlags'), 5))
    h.add(_.Bit('resolutionAndComponentFlags4', _.Get('resolutionAndComponentFlags'), 4))
    h.add(_.Bit('uvRelativeToGrid', _.Get('resolutionAndComponentFlags'), 3))
    h.add(_.Bit('resolutionAndComponentFlags6', _.Get('resolutionAndComponentFlags'), 2))
    h.add(_.Bit('resolutionAndComponentFlags7', _.Get('resolutionAndComponentFlags'), 1))
    h.add(_.Bit('resolutionAndComponentFlags8', _.Get('resolutionAndComponentFlags'), 0))
