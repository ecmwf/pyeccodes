# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .expression import evaluate
from .base import NoSize


class G2level(NoSize):

    def __init__(self, name,
                 typeOfFirstFixedSurface,
                 scaleFactorOfFirstFixedSurface,
                 scaledValueOfFirstFixedSurface,
                 pressureUnits):
        super().__init__(name)
        self.typeOfFirstFixedSurface = typeOfFirstFixedSurface
        self.scaledValueOfFirstFixedSurface = scaledValueOfFirstFixedSurface
        self.scaleFactorOfFirstFixedSurface = scaleFactorOfFirstFixedSurface
        self.pressureUnits = pressureUnits

    def get(self, handle):
        # typeOfFirstFixedSurface = evaluate(self.typeOfFirstFixedSurface, handle)
        scaledValueOfFirstFixedSurface = evaluate(self.scaledValueOfFirstFixedSurface, handle)
        scaleFactorOfFirstFixedSurface = evaluate(self.scaleFactorOfFirstFixedSurface, handle)
        # pressureUnits = evaluate(self.pressureUnits, handle)

        if scaledValueOfFirstFixedSurface is None:
            return None

        while scaleFactorOfFirstFixedSurface < 0:
            scaledValueOfFirstFixedSurface *= 10
            scaleFactorOfFirstFixedSurface += 1

        while scaleFactorOfFirstFixedSurface > 0:
            scaledValueOfFirstFixedSurface //= 10
            scaleFactorOfFirstFixedSurface -= 1

        return scaledValueOfFirstFixedSurface


class G2_eps(NoSize):

    def __init__(self, name,
                 productDefinitionTemplateNumber,
                 type,
                 stream,
                 stepType,
                 derivedForecast):
        super().__init__(name)
        self.productDefinitionTemplateNumber = productDefinitionTemplateNumber

    def get(self, handle):
        productDefinitionTemplateNumber = evaluate(self.productDefinitionTemplateNumber, handle)
        return productDefinitionTemplateNumber in (1, 11, 33, 34, 41, 43, 45, 47)


class G2end_step(NoSize):

    def __init__(self, name,
                 startStep,
                 stepUnits,
                 year=None,
                 month=None,
                 day=None,
                 hour=None,
                 minute=None,
                 second=None,
                 yearOfEndOfOverallTimeInterval=None,
                 monthOfEndOfOverallTimeInterval=None,
                 dayOfEndOfOverallTimeInterval=None,
                 hourOfEndOfOverallTimeInterval=None,
                 minuteOfEndOfOverallTimeInterval=None,
                 secondOfEndOfOverallTimeInterval=None,
                 indicatorOfUnitForTimeRange=None,
                 lengthOfTimeRange=None,
                 typeOfTimeIncrement=None,
                 numberOfTimeRange=None
                 ):
        super().__init__(name)
        self.startStep = startStep
        self.numberOfTimeRange = numberOfTimeRange
        self.year = year

    def get(self, handle):
        year = evaluate(self.year, handle)

        if year is None:
            return evaluate(self.startStep)

        numberOfTimeRange = evaluate(self.numberOfTimeRange, handle)
        assert numberOfTimeRange in (1, 2)

        if numberOfTimeRange == 1:
            pass
