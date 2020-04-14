def load(h):
    return ({'abbr': 0,
             'code': 0,
             'title': 'No explicit missing values included within data values'},
            {'abbr': 1,
             'code': 1,
             'title': 'Primary missing values included within data values'},
            {'abbr': 2,
             'code': 2,
             'title': 'Primary and secondary missing values included within data values'},
            {'abbr': None, 'code': 255, 'title': 'Missing'})
