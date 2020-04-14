def load(h):
    return ({'abbr': 0,
             'code': 0,
             'title': 'Forecast product valid at reference time + P1',
             'units': 'P1>0'},
            {'abbr': 1,
             'code': 1,
             'title': 'Initialized analysis product for reference time (P1=0).'},
            {'abbr': 2,
             'code': 2,
             'title': 'Product with a valid time ranging between reference time + P1 and '
                      'reference time + P2'},
            {'abbr': 3,
             'code': 3,
             'title': 'Average',
             'units': 'reference time + P1 to reference time + P2'},
            {'abbr': 4,
             'code': 4,
             'title': 'Accumulation (reference time + P1 to reference time + P2) product '
                      'considered valid at reference time + P2'},
            {'abbr': 5,
             'code': 5,
             'title': 'Difference (reference time + P2 minus reference time + P1) product '
                      'considered valid at reference time + P2'},
            {'abbr': 6,
             'code': 6,
             'title': 'Average',
             'units': 'reference time - P1 to reference time - P2'},
            {'abbr': 7,
             'code': 7,
             'title': 'Average',
             'units': 'reference time - P1 to reference time + P2'},
            {'abbr': 10,
             'code': 10,
             'title': 'P1 occupies octets 19 and 20; product valid at reference time + '
                      'P1'},
            {'abbr': 51, 'code': 51, 'title': 'Climatological Mean Value:'},
            {'abbr': 113,
             'code': 113,
             'title': 'Average of N forecasts (or initialized analyses); each product has '
                      'forecast period of P1 (P1=0 for initialized analyses); products '
                      'have reference times at intervals of P2, beginning at the given '
                      'reference time.'},
            {'abbr': 114,
             'code': 114,
             'title': 'Accumulation of N forecasts (or initialized analyses); each '
                      'product has forecast period of P1 (P1=0 for initialized analyses); '
                      'products have reference times at intervals of P2, beginning at the '
                      'given reference time.'},
            {'abbr': 115,
             'code': 115,
             'title': 'Average of N forecasts, all with the same reference time; the '
                      'first has a forecast period of P1, the remaining forecasts follow '
                      'at intervals of P2.'},
            {'abbr': 116,
             'code': 116,
             'title': 'Accumulation of N forecasts, all with the same reference time; the '
                      'first has a forecast period of P1, the remaining follow at '
                      'intervals of P2.'},
            {'abbr': 117,
             'code': 117,
             'title': 'Average of N forecasts, the first has a period of P1, the '
                      'subsequent ones have forecast periods reduced from the previous '
                      'one by an interval of P2; the reference time for the first is '
                      'given in octets 13- 17, the subsequent ones have reference times '
                      'increased from the previous one by an interval of P2. Thus all the '
                      'forecasts have the same valid time, given by the initial reference '
                      'time + P1.'},
            {'abbr': 118,
             'code': 118,
             'title': 'Temporal variance, or covariance, of N initialized analyses; each '
                      'product has forecast period P1=0; products have reference times at '
                      'intervals of P2, beginning at the given reference time.'},
            {'abbr': 119,
             'code': 119,
             'title': 'Standard deviation of N forecasts, all with the same reference '
                      'time with respect to the time average of forecasts; the first '
                      'forecast has a forecast period of P1, the remaining forecasts '
                      'follow at intervals of P2'},
            {'abbr': 123,
             'code': 123,
             'title': 'Average of N uninitialized analyses, starting at the reference '
                      'time, at intervals of P2.'},
            {'abbr': 124,
             'code': 124,
             'title': 'Accumulation of N uninitialized analyses, starting at the '
                      'reference time, at intervals of P2.'},
            {'abbr': 125,
             'code': 125,
             'title': 'Standard deviation of N forecasts, all with the same reference '
                      'time with respect to time average of the time tendency of '
                      'forecasts; the first forecast has a forecast period of P1, the '
                      'remaining forecasts follow at intervals of P2'})
