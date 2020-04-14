def load(h):
    return ({'bit': 1, 'on': 0, 'title': 'Grid-point data'},
            {'bit': 1, 'on': 1, 'title': 'Spherical harmonic coefficients'},
            {'bit': 2, 'on': 0, 'title': 'Simple packing'},
            {'bit': 2, 'on': 1, 'title': 'Complex or second-order packing'},
            {'bit': 3, 'on': 0, 'title': 'Floating point values are represented'},
            {'bit': 3, 'on': 1, 'title': 'Integer values are represented'},
            {'bit': 4, 'on': 0, 'title': 'No additional flags at octet 14'},
            {'bit': 4, 'on': 1, 'title': 'Octet 14 contains additional flag bits'})
