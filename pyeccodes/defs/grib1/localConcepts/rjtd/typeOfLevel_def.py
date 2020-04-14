import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')

        if indicatorOfTypeOfLevel == 213:
            return 'threeLayers'

        if indicatorOfTypeOfLevel == 212:
            return 'subSurface'

        if indicatorOfTypeOfLevel == 211:
            return 'deepSoil'

        level = h.get_l('level')

        if indicatorOfTypeOfLevel == 201 and level == 0:
            return 'entireOcean'

        if indicatorOfTypeOfLevel == 200 and level == 0:
            return 'entireAtmosphere'

        if indicatorOfTypeOfLevel == 160:
            return 'depthBelowSea'

        if indicatorOfTypeOfLevel == 117:
            return 'potentialVorticity'

        if indicatorOfTypeOfLevel == 116:
            return 'pressureFromGroundLayer'

        if indicatorOfTypeOfLevel == 115:
            return 'pressureFromGround'

        if indicatorOfTypeOfLevel == 114:
            return 'thetaLayer'

        if indicatorOfTypeOfLevel == 113:
            return 'theta'

        if indicatorOfTypeOfLevel == 112:
            return 'depthBelowLandLayer'

        if indicatorOfTypeOfLevel == 111:
            return 'depthBelowLand'

        if indicatorOfTypeOfLevel == 110:
            return 'hybridLayer'

        if indicatorOfTypeOfLevel == 109:
            return 'hybrid'

        if indicatorOfTypeOfLevel == 128:
            return 'sigmaLayerHighPrecision'

        if indicatorOfTypeOfLevel == 108:
            return 'sigmaLayer'

        if indicatorOfTypeOfLevel == 107:
            return 'sigma'

        if indicatorOfTypeOfLevel == 106:
            return 'heightAboveGroundLayer'

        if indicatorOfTypeOfLevel == 105:
            return 'heightAboveGround'

        if indicatorOfTypeOfLevel == 125:
            return 'heightAboveGroundHighPrecision'

        if indicatorOfTypeOfLevel == 104:
            return 'heightAboveSeaLayer'

        if indicatorOfTypeOfLevel == 103:
            return 'heightAboveSea'

        if indicatorOfTypeOfLevel == 141:
            return 'isobaricLayerMixedPrecision'

        if indicatorOfTypeOfLevel == 121:
            return 'isobaricLayerHighPrecision'

        if indicatorOfTypeOfLevel == 102:
            return 'meanSea'

        if indicatorOfTypeOfLevel == 101:
            return 'isobaricLayer'

        if indicatorOfTypeOfLevel == 210:
            return 'isobaricInPa'

        if indicatorOfTypeOfLevel == 100:
            return 'isobaricInhPa'

        if indicatorOfTypeOfLevel == 9:
            return 'seaBottom'

        if indicatorOfTypeOfLevel == 8:
            return 'nominalTop'

        if indicatorOfTypeOfLevel == 7:
            return 'tropopause'

        if indicatorOfTypeOfLevel == 6:
            return 'maxWind'

        if indicatorOfTypeOfLevel == 5:
            return 'adiabaticCondensation'

        if indicatorOfTypeOfLevel == 4:
            return 'isothermZero'

        if indicatorOfTypeOfLevel == 3:
            return 'cloudTop'

        if indicatorOfTypeOfLevel == 2:
            return 'cloudBase'

        if indicatorOfTypeOfLevel == 1:
            return 'surface'

    return wrapped
