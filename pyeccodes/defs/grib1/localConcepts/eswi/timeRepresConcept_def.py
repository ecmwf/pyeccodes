import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        matchTimeRepres = h.get_l('matchTimeRepres')

        if matchTimeRepres == 255:
            return 'missing'

        if matchTimeRepres == 70:
            return 'quality'

        if matchTimeRepres == 62:
            return 'bgErr'

        if matchTimeRepres == 61:
            return 'anaErr'

        if matchTimeRepres == 60:
            return 'anaIncr'

        if matchTimeRepres == 52:
            return 'stdDev'

        if matchTimeRepres == 51:
            return 'firatGuess'

        if matchTimeRepres == 50:
            return 'boundary'

        if matchTimeRepres == 46:
            return 'perc'

        if matchTimeRepres == 45:
            return 'jointProb'

        if matchTimeRepres == 44:
            return 'likelyhood'

        if matchTimeRepres == 43:
            return 'median'

        if matchTimeRepres == 42:
            return 'perc90d1'

        if matchTimeRepres == 41:
            return 'perc98d1'

        if matchTimeRepres == 40:
            return 'perc98h1'

        if matchTimeRepres == 33:
            return 'maxMax8h'

        if matchTimeRepres == 32:
            return 'meanMax8h'

        if matchTimeRepres == 31:
            return 'max8hMean'

        if matchTimeRepres == 30:
            return '8hMean'

        if matchTimeRepres == 26:
            return 'yearAccum'

        if matchTimeRepres == 25:
            return '6monthAccum'

        if matchTimeRepres == 24:
            return '3monthAccum'

        if matchTimeRepres == 23:
            return '3hAccum'

        if matchTimeRepres == 22:
            return 'monthAccum'

        if matchTimeRepres == 21:
            return 'dayAccum'

        if matchTimeRepres == 20:
            return 'accum'

        if matchTimeRepres == 19:
            return 'meanDayMax'

        if matchTimeRepres == 18:
            return 'yMeanDayMax'

        if matchTimeRepres == 17:
            return 'mMeanDayMax'

        if matchTimeRepres == 16:
            return 'yearMax'

        if matchTimeRepres == 14:
            return 'monthlyMax'

        if matchTimeRepres == 12:
            return 'dailyMax'

        if matchTimeRepres == 11:
            return 'min'

        if matchTimeRepres == 10:
            return 'max'

        if matchTimeRepres == 7:
            return 'yearMean'

        if matchTimeRepres == 6:
            return 'mean'

        if matchTimeRepres == 5:
            return 'monthlyMean'

        if matchTimeRepres == 3:
            return '1hMean'

        if matchTimeRepres == 2:
            return 'diurnalMean'

        if matchTimeRepres == 1:
            return '3hMean'

        if matchTimeRepres == 0:
            return 'none'

    return wrapped
