import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('Ni', 4))
    h.alias('numberOfPointsAlongAParallel', 'Ni')
    h.alias('Nx', 'Ni')
    h.add(_.Unsigned('Nj', 4))
    h.alias('numberOfPointsAlongAMeridian', 'Nj')
    h.alias('Ny', 'Nj')
    h.alias('geography.Ni', 'Ni')
    h.alias('geography.Nj', 'Nj')
    h.add(_.Unsigned('basicAngleOfTheInitialProductionDomain', 4))
    h.add(_.Transient('mBasicAngle', (_.Get('basicAngleOfTheInitialProductionDomain') * _.Get('oneMillionConstant'))))
    h.add(_.Transient('angleMultiplier', 1))
    h.add(_.Transient('mAngleMultiplier', 1000000))
    pass  # when block
    h.add(_.Unsigned('subdivisionsOfBasicAngle', 4))
    h.add(_.Transient('angleDivisor', 1000000))
    pass  # when block
    h.add(_.Signed('latitudeOfFirstGridPoint', 4))
    h.alias('La1', 'latitudeOfFirstGridPoint')
    h.add(_.Signed('longitudeOfFirstGridPoint', 4))
    h.alias('Lo1', 'longitudeOfFirstGridPoint')
    h.add(_.Codeflag('resolutionAndComponentFlags', 1, "grib2/tables/[tablesVersion]/3.3.table"))
    h.add(_.Bit('resolutionAndComponentFlags1', _.Get('resolutionAndComponentFlags'), 7))
    h.add(_.Bit('resolutionAndComponentFlags2', _.Get('resolutionAndComponentFlags'), 6))
    h.add(_.Bit('iDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 5))
    h.add(_.Bit('jDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 4))
    h.add(_.Bit('uvRelativeToGrid', _.Get('resolutionAndComponentFlags'), 3))
    h.add(_.Bit('resolutionAndComponentFlags6', _.Get('resolutionAndComponentFlags'), 7))
    h.add(_.Bit('resolutionAndComponentFlags7', _.Get('resolutionAndComponentFlags'), 6))
    h.add(_.Bit('resolutionAndComponentFlags8', _.Get('resolutionAndComponentFlags'), 6))

    def ijDirectionIncrementGiven_inline_concept(h):
        def wrapped(h):

            iDirectionIncrementGiven = h.get_l('iDirectionIncrementGiven')
            jDirectionIncrementGiven = h.get_l('jDirectionIncrementGiven')

            if iDirectionIncrementGiven == 1 and jDirectionIncrementGiven == 1:
                return 1

            if iDirectionIncrementGiven == 1 and jDirectionIncrementGiven == 0:
                return 0

            if iDirectionIncrementGiven == 0 and jDirectionIncrementGiven == 1:
                return 0

            if iDirectionIncrementGiven == 0 and jDirectionIncrementGiven == 0:
                return 0

        return wrapped

    h.add(_.Concept('ijDirectionIncrementGiven', None, concepts=ijDirectionIncrementGiven_inline_concept(h)))

    h.alias('DiGiven', 'iDirectionIncrementGiven')
    h.alias('DjGiven', 'jDirectionIncrementGiven')
    h.add(_.Signed('latitudeOfLastGridPoint', 4))
    h.alias('La2', 'latitudeOfLastGridPoint')
    h.add(_.Signed('longitudeOfLastGridPoint', 4))
    h.alias('Lo2', 'longitudeOfLastGridPoint')
