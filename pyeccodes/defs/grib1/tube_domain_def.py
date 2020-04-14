import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        northLatitudeOfDomainOfTubing = h.get('northLatitudeOfDomainOfTubing')
        westLongitudeOfDomainOfTubing = h.get('westLongitudeOfDomainOfTubing')
        southLatitudeOfDomainOfTubing = h.get('southLatitudeOfDomainOfTubing')
        eastLongitudeOfDomainOfTubing = h.get('eastLongitudeOfDomainOfTubing')

        if northLatitudeOfDomainOfTubing == 70000 and westLongitudeOfDomainOfTubing == 332500 and southLatitudeOfDomainOfTubing == 40000 and eastLongitudeOfDomainOfTubing == 10000:
            return 'a'

        if northLatitudeOfDomainOfTubing == 72500 and westLongitudeOfDomainOfTubing == 0 and southLatitudeOfDomainOfTubing == 50000 and eastLongitudeOfDomainOfTubing == 45000:
            return 'b'

        if northLatitudeOfDomainOfTubing == 57500 and westLongitudeOfDomainOfTubing == 345000 and southLatitudeOfDomainOfTubing == 32500 and eastLongitudeOfDomainOfTubing == 17500:
            return 'c'

        if northLatitudeOfDomainOfTubing == 57500 and westLongitudeOfDomainOfTubing == 2500 and southLatitudeOfDomainOfTubing == 32500 and eastLongitudeOfDomainOfTubing == 42500:
            return 'd'

        if northLatitudeOfDomainOfTubing == 75000 and westLongitudeOfDomainOfTubing == 340000 and southLatitudeOfDomainOfTubing == 30000 and eastLongitudeOfDomainOfTubing == 45000:
            return 'e'

        if northLatitudeOfDomainOfTubing == 60000 and westLongitudeOfDomainOfTubing == 310000 and southLatitudeOfDomainOfTubing == 40000 and eastLongitudeOfDomainOfTubing == 0:
            return 'f'

    return wrapped
