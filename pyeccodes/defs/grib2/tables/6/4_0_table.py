def load(h):
    return ({'abbr': 0,
             'code': 0,
             'title': 'Analysis or forecast at a horizontal level or in a horizontal '
                      'layer at a point in time'},
            {'abbr': 1,
             'code': 1,
             'title': 'Individual ensemble forecast, control and perturbed, at a '
                      'horizontal level or in a horizontal layer at a point in time'},
            {'abbr': 2,
             'code': 2,
             'title': 'Derived forecast based on all ensemble members at a horizontal '
                      'level or in a horizontal layer at a point in time'},
            {'abbr': 3,
             'code': 3,
             'title': 'Derived forecasts based on a cluster of ensemble members over a '
                      'rectangular area at a horizontal level or in a horizontal layer at '
                      'a point in time'},
            {'abbr': 4,
             'code': 4,
             'title': 'Derived forecasts based on a cluster of ensemble members over a '
                      'circular area at a horizontal level or in a horizontal layer at a '
                      'point in time'},
            {'abbr': 5,
             'code': 5,
             'title': 'Probability forecasts at a horizontal level or in a horizontal '
                      'layer at a point in time'},
            {'abbr': 6,
             'code': 6,
             'title': 'Percentile forecasts at a horizontal level or in a horizontal '
                      'layer at a point in time'},
            {'abbr': 7,
             'code': 7,
             'title': 'Analysis or forecast error at a horizontal level or in a '
                      'horizontal layer at a point in time'},
            {'abbr': 8,
             'code': 8,
             'title': 'Average, accumulation, extreme values or other statistically '
                      'processed values at a horizontal level or in a horizontal layer in '
                      'a continuous or non-continuous time interval'},
            {'abbr': 9,
             'code': 9,
             'title': 'Probability forecasts at a horizontal level or in a horizontal '
                      'layer in a continuous or non-continuous time interval'},
            {'abbr': 10,
             'code': 10,
             'title': 'Percentile forecasts at a horizontal level or in a horizontal '
                      'layer in a continuous or non-continuous time interval'},
            {'abbr': 11,
             'code': 11,
             'title': 'Individual ensemble forecast, control and perturbed, at a '
                      'horizontal level or in a horizontal layer, in a continuous or '
                      'non-continuous interval'},
            {'abbr': 12,
             'code': 12,
             'title': 'Derived forecasts based on all ensemble members at a horizontal '
                      'level or in a horizontal layer, in a continuous or non-continuous '
                      'interval'},
            {'abbr': 13,
             'code': 13,
             'title': 'Derived forecasts based on a cluster of ensemble members over a '
                      'rectangular area, at a horizontal level or in a horizontal layer, '
                      'in a continuous or non-continuous interval'},
            {'abbr': 14,
             'code': 14,
             'title': 'Derived forecasts based on a cluster of ensemble members over a '
                      'circular area, at a horizontal level or in a horizontal layer, in '
                      'a continuous or non-continuous interval'},
            {'abbr': 15,
             'code': 15,
             'title': 'Average, accumulation, extreme values, or other '
                      'statistically-processed values over a spatial area at a horizontal '
                      'level or in a horizontal layer at a point in time'},
            {'abbr': 20, 'code': 20, 'title': 'Radar product'},
            {'abbr': 30, 'code': 30, 'title': 'Satellite product'},
            {'abbr': 31, 'code': 31, 'title': 'Satellite product'},
            {'abbr': 311, 'code': 311, 'title': 'Satellite product auxiliary information'},
            {'abbr': 40,
             'code': 40,
             'title': 'Analysis or forecast at a horizontal level or in a horizontal '
                      'layer at a point in time for atmospheric chemical constituents'},
            {'abbr': 41,
             'code': 41,
             'title': 'Individual ensemble forecast, control and perturbed, at a '
                      'horizontal level or in a horizontal layer at a point in time for '
                      'atmospheric chemical constituents'},
            {'abbr': 42,
             'code': 42,
             'title': 'Average, accumulation, extreme values or other statistically '
                      'processed values at a horizontal level or in a horizontal layer in '
                      'a continuous or non-continuous time interval for atmospheric '
                      'chemical constituents'},
            {'abbr': 43,
             'code': 43,
             'title': 'Individual ensemble forecast, control and perturbed, at a '
                      'horizontal level or in a horizontal layer, in a continuous or '
                      'non-continuous interval for atmospheric chemical constituents'},
            {'abbr': 44,
             'code': 44,
             'title': 'Analysis or forecast at a horizontal level or in a horizontal '
                      'layer at a point in time for atmospheric aerosol'},
            {'abbr': 45,
             'code': 45,
             'title': 'Individual ensemble forecast, control and perturbed, at a '
                      'horizontal level or in a horizontal layer at a point in time for '
                      'atmospheric aerosol'},
            {'abbr': 46,
             'code': 46,
             'title': 'Average, accumulation, extreme values or other statistically '
                      'processed values at a horizontal level or in a horizontal layer in '
                      'a continuous or non-continuous time interval for atmospheric '
                      'aerosol'},
            {'abbr': 47,
             'code': 47,
             'title': 'Individual ensemble forecast, control and perturbed, at a '
                      'horizontal level or in a horizontal layer, in a continuous or '
                      'non-continuous interval for atmospheric aerosol'},
            {'abbr': 48,
             'code': 48,
             'title': 'Analysis or forecast at a horizontal level or in a horizontal '
                      'layer at a point in time for optical properties of atmospheric '
                      'aerosol'},
            {'abbr': 51,
             'code': 51,
             'title': 'Categorical forecasts at a horizontal level or in a horizontal '
                      'layer at a point in time'},
            {'abbr': 91,
             'code': 91,
             'title': 'Categorical forecasts at a horizontal level or in a horizontal '
                      'layer in a continuous or non-continuous time interval'},
            {'abbr': 254, 'code': 254, 'title': 'CCITT IA5 character string'},
            {'abbr': 1000,
             'code': 1000,
             'title': 'Cross section of analysis and forecast at a point in time'},
            {'abbr': 1001,
             'code': 1001,
             'title': 'Cross section of averaged or otherwise statistically processed '
                      'analysis or forecast over a range of time'},
            {'abbr': 1002,
             'code': 1002,
             'title': 'Cross-section of analysis and forecast, averaged or otherwise '
                      'statistically processed'},
            {'abbr': 1100,
             'code': 1100,
             'title': 'Hovmoller-type grid with no averaging or other statistical '
                      'processing'},
            {'abbr': 1101,
             'code': 1101,
             'title': 'Hovmoller-type grid with averaging or other statistical '
                      'processing'},
            {'abbr': 50001,
             'code': 50001,
             'title': 'Forecasting Systems with Variable Resolution in a point in time'},
            {'abbr': 50011,
             'code': 50011,
             'title': 'Forecasting Systems with Variable Resolution in a continous or non '
                      'countinous time interval'},
            {'abbr': 65535, 'code': 65335, 'title': 'Missing'})
