import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        northWestLatitudeOfVerficationArea = h.get_l('northWestLatitudeOfVerficationArea')
        northWestLongitudeOfVerficationArea = h.get_l('northWestLongitudeOfVerficationArea')
        southEastLatitudeOfVerficationArea = h.get_l('southEastLatitudeOfVerficationArea')
        southEastLongitudeOfVerficationArea = h.get_l('southEastLongitudeOfVerficationArea')

        if northWestLatitudeOfVerficationArea == 7100 and northWestLongitudeOfVerficationArea == 500 and southEastLatitudeOfVerficationArea == 5200 and southEastLongitudeOfVerficationArea == 2900:
            return 'i'

        if northWestLatitudeOfVerficationArea == 6300 and northWestLongitudeOfVerficationArea == -1900 and southEastLatitudeOfVerficationArea == 4400 and southEastLongitudeOfVerficationArea == 400:
            return 'p'

        if northWestLatitudeOfVerficationArea == 6300 and northWestLongitudeOfVerficationArea == -1600 and southEastLatitudeOfVerficationArea == 4300 and southEastLongitudeOfVerficationArea == 800:
            return 'l'

        if northWestLatitudeOfVerficationArea == 5150 and northWestLongitudeOfVerficationArea == -90 and southEastLatitudeOfVerficationArea == 3200 and southEastLongitudeOfVerficationArea == 2330:
            return 'l'

        if northWestLatitudeOfVerficationArea == 4950 and northWestLongitudeOfVerficationArea == 0 and southEastLatitudeOfVerficationArea == 3009 and southEastLongitudeOfVerficationArea == 2430:
            return 'l'

        if northWestLatitudeOfVerficationArea == 5080 and northWestLongitudeOfVerficationArea == -1050 and southEastLatitudeOfVerficationArea == 3139 and southEastLongitudeOfVerficationArea == 1379:
            return 'k'

        if northWestLatitudeOfVerficationArea == 5030 and northWestLongitudeOfVerficationArea == -59 and southEastLatitudeOfVerficationArea == 3089 and southEastLongitudeOfVerficationArea == 2370:
            return 'k'

        if northWestLatitudeOfVerficationArea == 4910 and northWestLongitudeOfVerficationArea == -1000 and southEastLatitudeOfVerficationArea == 2959 and southEastLongitudeOfVerficationArea == 1429:
            return 'k'

        if northWestLatitudeOfVerficationArea == 6660 and northWestLongitudeOfVerficationArea == -920 and southEastLatitudeOfVerficationArea == 4710 and southEastLongitudeOfVerficationArea == 1510:
            return 'j'

        if northWestLatitudeOfVerficationArea == 6660 and northWestLongitudeOfVerficationArea == -1870 and southEastLatitudeOfVerficationArea == 4710 and southEastLongitudeOfVerficationArea == 550:
            return 'j'

        if northWestLatitudeOfVerficationArea == 4700 and northWestLongitudeOfVerficationArea == -900 and southEastLatitudeOfVerficationArea == 2700 and southEastLongitudeOfVerficationArea == 1400:
            return 'j'

        if northWestLatitudeOfVerficationArea == 6140 and northWestLongitudeOfVerficationArea == -950 and southEastLatitudeOfVerficationArea == 4190 and southEastLongitudeOfVerficationArea == 1479:
            return 'i'

        if northWestLatitudeOfVerficationArea == 5100 and northWestLongitudeOfVerficationArea == -300 and southEastLatitudeOfVerficationArea == 3200 and southEastLongitudeOfVerficationArea == 2000:
            return 'i'

        if northWestLatitudeOfVerficationArea == 5020 and northWestLongitudeOfVerficationArea == -2290 and southEastLatitudeOfVerficationArea == 3070 and southEastLongitudeOfVerficationArea == 130:
            return 'i'

        if northWestLatitudeOfVerficationArea == 4900 and northWestLongitudeOfVerficationArea == -800 and southEastLatitudeOfVerficationArea == 2900 and southEastLongitudeOfVerficationArea == 1500:
            return 'i'

        if northWestLatitudeOfVerficationArea == 4890 and northWestLongitudeOfVerficationArea == 730 and southEastLatitudeOfVerficationArea == 2940 and southEastLongitudeOfVerficationArea == 3160:
            return 'i'

        if northWestLatitudeOfVerficationArea == 0 and northWestLongitudeOfVerficationArea == 0 and southEastLatitudeOfVerficationArea == 0 and southEastLongitudeOfVerficationArea == 0:
            return 'i'

        if northWestLatitudeOfVerficationArea == 6640 and northWestLongitudeOfVerficationArea == -2340 and southEastLatitudeOfVerficationArea == 4690 and southEastLongitudeOfVerficationArea == 90:
            return 'h'

        if northWestLatitudeOfVerficationArea == 6200 and northWestLongitudeOfVerficationArea == -2160 and southEastLatitudeOfVerficationArea == 4260 and southEastLongitudeOfVerficationArea == 260:
            return 'h'

        if northWestLatitudeOfVerficationArea == 5130 and northWestLongitudeOfVerficationArea == -739 and southEastLatitudeOfVerficationArea == 3189 and southEastLongitudeOfVerficationArea == 169:
            return 'h'

        if northWestLatitudeOfVerficationArea == 5130 and northWestLongitudeOfVerficationArea == -739 and southEastLatitudeOfVerficationArea == 3189 and southEastLongitudeOfVerficationArea == 1690:
            return 'h'

        if northWestLatitudeOfVerficationArea == 5020 and northWestLongitudeOfVerficationArea == -720 and southEastLatitudeOfVerficationArea == 3070 and southEastLongitudeOfVerficationArea == 1700:
            return 'h'

        if northWestLatitudeOfVerficationArea == 4940 and northWestLongitudeOfVerficationArea == 0 and southEastLatitudeOfVerficationArea == 2990 and southEastLongitudeOfVerficationArea == 2430:
            return 'h'

        if northWestLatitudeOfVerficationArea == 4800 and northWestLongitudeOfVerficationArea == -300 and southEastLatitudeOfVerficationArea == 2900 and southEastLongitudeOfVerficationArea == 2100:
            return 'h'

        if northWestLatitudeOfVerficationArea == 4760 and northWestLongitudeOfVerficationArea == -2180 and southEastLatitudeOfVerficationArea == 2809 and southEastLongitudeOfVerficationArea == 250:
            return 'h'

        if northWestLatitudeOfVerficationArea == 4630 and northWestLongitudeOfVerficationArea == 719 and southEastLatitudeOfVerficationArea == 2689 and southEastLongitudeOfVerficationArea == 3140:
            return 'h'

    return wrapped
