def load(h):
    return ({'abbr': 1,
             'code': 1,
             'title': 'Successive times processed have same forecast time, start time of '
                      'forecast is incremented'},
            {'abbr': 2,
             'code': 2,
             'title': 'Successive times processed have same start time of forecast, '
                      'forecast time is incremented'},
            {'abbr': 3,
             'code': 3,
             'title': 'Successive times processed have start time of forecast incremented '
                      'and forecast time decremented so that valid time remains constant'},
            {'abbr': 4,
             'code': 4,
             'title': 'Successive times processed have start time of forecast decremented '
                      'and forecast time incremented so that valid time remains constant'},
            {'abbr': 5,
             'code': 5,
             'title': 'Floating subinterval of time between forecast time and end of '
                      'overall time interval'},
            {'abbr': None, 'code': 255, 'title': 'Missing'})
