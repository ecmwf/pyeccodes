def load(h):
    return ({'abbr': 0, 'code': 0, 'title': 'No specific distribution function given'},
            {'abbr': 1,
             'code': 1,
             'title': 'Delta functions with spatially variable concentration and fixed '
                      'diameters Dl (p1) in metre'},
            {'abbr': 2,
             'code': 2,
             'title': 'Delta functions with spatially variable concentration and fixed '
                      'masses Ml (p1) in kg'},
            {'abbr': 3,
             'code': 3,
             'title': 'Gaussian',
             'units': 'normal) distribution with spatially variable concentration and '
                      'fixed mean diameter Dl(p1) and variance(p2'},
            {'abbr': 4,
             'code': 4,
             'title': 'Gaussian (normal) distribution with spatially variable '
                      'concentration, mean diameter and variance'},
            {'abbr': 5,
             'code': 5,
             'title': 'Log-normal distribution with spatially variable number density, '
                      'mean diameter and variance'},
            {'abbr': 6,
             'code': 6,
             'title': 'Log-normal distribution with spatially variable number density, '
                      'mean diameter and fixed variance(p1)'},
            {'abbr': 7,
             'code': 7,
             'title': 'Log-normal distribution with spatially variable number density and '
                      'mass density and fixed variance(p1) and fixed particle '
                      'density(p2)'},
            {'abbr': 8,
             'code': 8,
             'title': 'No distribution function. The encoded variable is derived from '
                      'variables characterized by type of distribution function of type '
                      'No. 7',
             'units': 'see above) with fixed variance(p1) and fixed particle density(p2'},
            {'abbr': 65535, 'code': 65535, 'title': 'Missing value'})
