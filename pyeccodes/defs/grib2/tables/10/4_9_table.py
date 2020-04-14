def load(h):
    return ({'abbr': 0, 'code': 0, 'title': 'Probability of event below lower limit'},
            {'abbr': 1, 'code': 1, 'title': 'Probability of event above upper limit'},
            {'abbr': 2,
             'code': 2,
             'title': 'Probability of event between lower and upper limits',
             'units': 'the range includes the lower limit but not the upper limit'},
            {'abbr': 3, 'code': 3, 'title': 'Probability of event above lower limit'},
            {'abbr': 4, 'code': 4, 'title': 'Probability of event below upper limit'},
            {'abbr': None, 'code': 255, 'title': 'Missing'})
