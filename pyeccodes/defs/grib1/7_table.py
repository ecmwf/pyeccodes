def load(h):
    return ({'bit': 1, 'on': 0, 'title': 'Direction increments not given'},
            {'bit': 1, 'on': 1, 'title': 'Direction increments given'},
            {'bit': 2,
             'on': 0,
             'title': 'Earth assumed spherical with radius = 6367.47 km'},
            {'bit': 2,
             'on': 1,
             'title': 'Earth assumed oblate spheroid with size as determined by IAU in '
                      '1965: 6378.160 km, 6356.775 km, f = 1/297.0'},
            {'bit': 5,
             'on': 0,
             'title': 'u and v components resolved relative to easterly and northerly '
                      'directions'},
            {'bit': 5,
             'on': 1,
             'title': 'u and v components resolved relative to the defined grid'})
