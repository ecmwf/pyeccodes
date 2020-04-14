import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        northernLatitudeOfDomain = h.get('northernLatitudeOfDomain')
        westernLongitudeOfDomain = h.get('westernLongitudeOfDomain')
        southernLatitudeOfDomain = h.get('southernLatitudeOfDomain')
        easternLongitudeOfDomain = h.get('easternLongitudeOfDomain')

        if northernLatitudeOfDomain == 70000 and westernLongitudeOfDomain == 332500 and southernLatitudeOfDomain == 40000 and easternLongitudeOfDomain == 10000:
            return 'a'

        if northernLatitudeOfDomain == 72500 and westernLongitudeOfDomain == 0 and southernLatitudeOfDomain == 50000 and easternLongitudeOfDomain == 45000:
            return 'b'

        if northernLatitudeOfDomain == 57500 and westernLongitudeOfDomain == 345000 and southernLatitudeOfDomain == 32500 and easternLongitudeOfDomain == 17500:
            return 'c'

        if northernLatitudeOfDomain == 57500 and westernLongitudeOfDomain == 2500 and southernLatitudeOfDomain == 32500 and easternLongitudeOfDomain == 42500:
            return 'd'

        if northernLatitudeOfDomain == 75000 and westernLongitudeOfDomain == 340000 and southernLatitudeOfDomain == 30000 and easternLongitudeOfDomain == 45000:
            return 'e'

        if northernLatitudeOfDomain == 60000 and westernLongitudeOfDomain == 310000 and southernLatitudeOfDomain == 40000 and easternLongitudeOfDomain == 0:
            return 'f'

    return wrapped
