# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

import numpy as np

from .base import *
from .expression import *
from .iterators import *
from .notimp import *
from .padding import *
from .data import *
from .grib1 import *
from .utils import *
from .packing import *
from .tables import *
from .templates import *
from .concepts import *
from .dates import *

from .expression import evaluate
from .base import NoSize


class Transient(NoSize):

    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def get(self, handle):
        return evaluate(self.value, handle)

    def set(self, value):
        self.value = value


class Constant(NoSize):

    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def get(self, handle):
        return evaluate(self.value, handle)


class Lookup(NoSize):

    def __init__(self, name, count, where, *ignore):
        super().__init__(name)
        self.where = where
        self.count = count

    def get(self, handle):
        result = 0
        for i in range(self.count):
            result = result * 256 + int(handle._buffer[self.where + self.offset + i])
        return result


class Bit(NoSize):

    def __init__(self, name, accessor, which):
        super().__init__(name)
        self.which = which
        self.accessor = accessor

    def get(self, handle):
        flags = self.accessor.evaluate(handle)
        return 1 if flags & (1 << self.which) else 0


class Section_length(Unsigned):
    pass



class Ksec1expver(Ascii):

    def get(self, handle):
        return super().get(handle).decode()


class Label(NoSize):
    pass


##########################################################


class Headers_only(NoSize):

    def get(self, handle):
        return 0


class Gds_is_present(NoSize):

    def __init__(self, name, gridDescriptionSectionPresent, gridDefinition, bitmapPresent, values):
        super().__init__(name)
        self.gridDescriptionSectionPresent = gridDescriptionSectionPresent

    def get(self, handle):
        return evaluate(self.gridDescriptionSectionPresent, handle)

##########################################################


class Check_internal_version(NoSize):

    def __init__(self, name, version):
        super().__init__(name)

    def get(self, handle):
        return 1


##########################################################


##########################################################

class Offset_file(NoSize):

    def get(self, handle):
        return handle.offset


class Count_file(NoSize):

    def get(self, handle):
        return handle.count


class Count_total(NoSize):

    def get(self, handle):
        return handle.reader.count


class G2date(NoSize):

    def __init__(self, name, year, month, day):
        super().__init__(name)
        self.year = year
        self.month = month
        self.day = day

    def get(self, handle):
        year = evaluate(self.year, handle)
        month = evaluate(self.month, handle)
        day = evaluate(self.day, handle)
        return year * 10000 + month * 100 + day


class Time(NoSize):

    def __init__(self, name, hour, minute, second):
        super().__init__(name)
        self.hour = hour
        self.minute = minute
        self.second = second

    def get(self, handle):
        hour = evaluate(self.hour, handle)
        minute = evaluate(self.minute, handle)
        second = evaluate(self.second, handle)
        assert second == 0
        return hour * 100 + minute


class Latlon_increment(NoSize):

    def __init__(self, name,
                 directionIncrementGiven,
                 directionIncrement,
                 scansPositively,
                 first,
                 last,
                 numberOfPoints,
                 angleMultiplier,
                 angleDivisor,
                 isLongitude):
        super().__init__(name)

        self.directionIncrementGiven = directionIncrementGiven
        self.directionIncrement = directionIncrement
        self.angleDivisor = angleDivisor
        self.angleMultiplier = angleMultiplier

    def get(self, handle):
        directionIncrementGiven = evaluate(self.directionIncrementGiven, handle)
        # scansPositively = evaluate(self.scansPositively, handle)
        directionIncrement = evaluate(self.directionIncrement, handle)
        # first = evaluate(self.first, handle)
        # last = evaluate(self.last, handle)
        # numberOfPoints = evaluate(self.numberOfPoints, handle)
        angleMultiplier = evaluate(self.angleMultiplier, handle)
        angleDivisor = evaluate(self.angleDivisor, handle)
        # isLongitude = evaluate(self.isLongitude, handle)

        # if isLongitude:
        #     if last < first and scansPositively:
        #         last += 360

        assert directionIncrementGiven

        return float(directionIncrement) / float(angleDivisor) * float(angleMultiplier)


class Number_of_coded_values(NoSize):

    def __init__(self, name, bitsPerValue, offsetBeforeData,
                 offsetAfterData, unusedBits, numberOfValues):
        super().__init__(name)
        self.bitsPerValue = bitsPerValue
        self.offsetAfterData = offsetAfterData
        self.offsetBeforeData = offsetBeforeData
        self.unusedBits = unusedBits

    def get(self, handle):
        bitsPerValue = evaluate(self.bitsPerValue, handle)
        offsetBeforeData = evaluate(self.offsetBeforeData, handle)
        offsetAfterData = evaluate(self.offsetAfterData, handle)
        unusedBits = evaluate(self.unusedBits, handle)

        return ((offsetAfterData - offsetBeforeData) * 8 - unusedBits) // bitsPerValue


class GXbitmap(Accessor):

    def __init__(self, name,
                 tableReference,
                 missingValue,
                 offsetSection,
                 sectionLength,
                 numberOfUnusedBitsAtEndOfSection):
        super().__init__(name)
        self.sectionLength = sectionLength
        self.offsetSection = offsetSection
        self.numberOfUnusedBitsAtEndOfSection = numberOfUnusedBitsAtEndOfSection

    @property
    def length(self):
        sectionLength = evaluate(self.sectionLength, self.handle)
        offsetSection = evaluate(self.offsetSection, self.handle)
        return sectionLength - (self.offset - offsetSection)

    def get(self, handle):
        numberOfUnusedBitsAtEndOfSection = evaluate(self.numberOfUnusedBitsAtEndOfSection, self.handle)
        data = handle._buffer[self.offset:]
        values = np.frombuffer(data, dtype=np.uint8, count=self.length)
        values = np.unpackbits(values)
        if numberOfUnusedBitsAtEndOfSection:
            values = np.resize(values, self.length * 8 - numberOfUnusedBitsAtEndOfSection)
        return values


class G1bitmap(GXbitmap):
    pass


class G2bitmap(GXbitmap):
    pass


class Data_apply_bitmap(NoSize):

    def __init__(self, name, codedValues, bitmap, missingValue, binaryScaleFactor, numberOfDataPoints=None, numberOfValues=None):
        super().__init__(name)
        self.codedValues = codedValues
        self.bitmap = bitmap
        self.missingValue = missingValue
        self.binaryScaleFactor = binaryScaleFactor

    def get(self, handle):

        # TODO: grib2 alwats call apply_bitmap with bitmap undefined
        if not handle._defined(self.bitmap):
            return evaluate(self.codedValues, handle)

        codedValues = evaluate(self.codedValues, handle)
        bitmap = evaluate(self.bitmap, handle)
        # missingValue = evaluate(self.missingValue, handle)
        missingValue = np.NaN

        values = np.empty(bitmap.shape)
        values[:] = missingValue

        j = 0
        for i in range(0, len(bitmap)):
            if bitmap[i]:
                values[i] = codedValues[j]
                j += 1

        return values


class G2_mars_labeling(NoSize):
    def __init__(self,
                 name,
                 index,
                 marsClass,
                 marsType,
                 marsStream,
                 experimentVersionNumber,
                 typeOfProcessedData,
                 productDefinitionTemplateNumber,
                 stepType,
                 derivedForecast,
                 typeOfGeneratingProcess
                 ):
        super().__init__(name)
        self.index = index
        self.marsClass = marsClass
        self.marsType = marsType
        self.marsStream = marsStream

    def get(self, handle):
        index = evaluate(self.index, handle)

        if index == 0:
            return evaluate(self.marsClass, handle)

        if index == 1:
            return evaluate(self.marsType, handle)

        if index == 2:
            return evaluate(self.marsStream, handle)

        raise NotImplementedError("G2_mars_labeling(%s)" % (index,))


class G2_template_check(NoSize):
    def __init__(self, name, productDefinitionTemplateNumber, stepType, optical):
        super().__init__(name)
        self.productDefinitionTemplateNumber = productDefinitionTemplateNumber
        self.optical = optical

    def get(self, handle):
        return evaluate(self.productDefinitionTemplateNumber, handle) in self.templates


class G2_aerosol(G2_template_check):

    @property
    def templates(self):
        return (48, 49) if self.optical else (44, 45, 46, 47, 48, 49)


class G2latlon(NoSize):
    def __init__(self, name, g2grid, index, given=None):
        super().__init__(name)
        self.g2grid = g2grid
        self.index = index
        self.given = given

    def get(self, handle):
        g2grid = evaluate(self.g2grid, handle)
        index = evaluate(self.index, handle)

        if self.given:
            given = evaluate(self.given, handle)
            if not given:
                return None

        return g2grid[index]


class G2grid(NoSize):
    def __init__(self, name,
                 latitudeOfFirstGridPoint,
                 longitudeOfFirstGridPoint,
                 latitudeOfLastGridPoint,
                 longitudeOfLastGridPoint,
                 iDirectionIncrement,
                 jDirectionIncrement,
                 basicAngleOfTheInitialProductionDomain,
                 subdivisionsOfBasicAngle):
        super().__init__(name)
        self.latitudeOfFirstGridPoint = latitudeOfFirstGridPoint
        self.longitudeOfFirstGridPoint = longitudeOfFirstGridPoint
        self.latitudeOfLastGridPoint = latitudeOfLastGridPoint
        self.longitudeOfLastGridPoint = longitudeOfLastGridPoint
        self.iDirectionIncrement = iDirectionIncrement
        self.jDirectionIncrement = jDirectionIncrement
        self.basicAngleOfTheInitialProductionDomain = basicAngleOfTheInitialProductionDomain
        self.subdivisionsOfBasicAngle = subdivisionsOfBasicAngle

    def get(self, handle):
        latitudeOfFirstGridPoint = evaluate(self.latitudeOfFirstGridPoint, handle)
        longitudeOfFirstGridPoint = evaluate(self.longitudeOfFirstGridPoint, handle)
        latitudeOfLastGridPoint = evaluate(self.latitudeOfLastGridPoint, handle)
        longitudeOfLastGridPoint = evaluate(self.longitudeOfLastGridPoint, handle)
        iDirectionIncrement = evaluate(self.iDirectionIncrement, handle)
        jDirectionIncrement = evaluate(self.jDirectionIncrement, handle)
        basicAngleOfTheInitialProductionDomain = evaluate(self.basicAngleOfTheInitialProductionDomain, handle)
        subdivisionsOfBasicAngle = evaluate(self.subdivisionsOfBasicAngle, handle)

        if basicAngleOfTheInitialProductionDomain == 0:
            basicAngleOfTheInitialProductionDomain = 1

        if subdivisionsOfBasicAngle == 0xffffffff:
            subdivisionsOfBasicAngle = 1000000

        values = (latitudeOfFirstGridPoint,
                  longitudeOfFirstGridPoint,
                  latitudeOfLastGridPoint,
                  longitudeOfLastGridPoint,
                  iDirectionIncrement,
                  jDirectionIncrement)

        basicAngleOfTheInitialProductionDomain = float(basicAngleOfTheInitialProductionDomain)
        subdivisionsOfBasicAngle = float(subdivisionsOfBasicAngle)
        values = tuple(float(x) / subdivisionsOfBasicAngle * basicAngleOfTheInitialProductionDomain for x in values)

        return values


class G2bitmap_present(NoSize):

    def __init__(self, name, bitMapIndicator):
        super().__init__(name)
        self.bitMapIndicator = bitMapIndicator

    def get(self, handle):
        bitMapIndicator = evaluate(self.bitMapIndicator, handle)
        return 0 if bitMapIndicator in (0, 255) else 1


class Spd(Accessor):

    def __init__(self, name, widthOfSPD, orderOfSPD):
        super().__init__(name)
        self.widthOfSPD = widthOfSPD
        self.orderOfSPD = orderOfSPD

    @property
    def length(self):
        widthOfSPD = evaluate(self.widthOfSPD, self.handle)
        orderOfSPD = evaluate(self.orderOfSPD, self.handle) + 1
        return (widthOfSPD * orderOfSPD + 7) // 8


class Gts_header(NoSize):

    def __init__(self, name, offset=None, length=None):
        super().__init__(name)

    def get(self, handle):
        return "missing"


class Statistics(NoSize):

    def __init__(self, name, missingValue, values):
        super().__init__(name)
        self.missingValue = missingValue
        self.values = values

    def get(self, handle):
        return (None, None, None, None, None, None, None, None)


class Latitudes(NoSize):

    def __init__(self, name, values, distinct):
        super().__init__(name)
        self.values = values
        self.distinct = distinct

    def get(self, handle):
        distinct = evaluate(self.distinct, handle)
        iterator = handle.get('ITERATOR')
        if distinct:
            return iterator.distinct_latitudes()
        else:
            return np.array([lat for (lat, lon, val) in iterator])


class Longitudes(NoSize):

    def __init__(self, name, values, distinct):
        super().__init__(name)
        self.values = values
        self.distinct = distinct

    def get(self, handle):
        distinct = evaluate(self.distinct, handle)
        iterator = handle.get('ITERATOR')
        if distinct:
            return iterator.distinct_longitudes()
        else:
            return np.array([lon for (lat, lon, val) in iterator])


class Iterator(NoSize):

    def __init__(self, name, kind, *args):
        super().__init__(name)
        self.kind = kind
        self.args = args

    def get(self, handle):
        kind = self.kind.name
        args = [evaluate(a, handle) for a in self.args]
        return ITERATORS[kind](handle, *args)


class Number_of_points(NoSize):

    def __init__(self, name, Ni, Nj, PLPresent, pl):
        super().__init__(name)
        self.Ni = Ni
        self.Nj = Nj
        self.PLPresent = PLPresent
        self.pl = pl

    def get(self, handle):

        Nj = evaluate(self.Nj, handle)
        assert Nj > 0

        PLPresent = evaluate(self.PLPresent, handle)

        if PLPresent:
            pl = evaluate(self.pl)
            assert Nj == len(pl)
            return np.sum(pl)

        Ni = evaluate(self.Ni, handle)
        return Ni * Nj
