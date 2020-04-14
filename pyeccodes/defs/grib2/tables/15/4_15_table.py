def load(h):
    return ({'abbr': 0,
             'code': 0,
             'title': 'Data is calculated directly from the source grid with no '
                      'interpolation'},
            {'abbr': 1,
             'code': 1,
             'title': 'Bilinear interpolation using the 4 source grid grid-point values '
                      'surrounding the nominal grid-point'},
            {'abbr': 2,
             'code': 2,
             'title': 'Bicubic interpolation using the 4 source grid grid-point values '
                      'surrounding the nominal grid-point'},
            {'abbr': 3,
             'code': 3,
             'title': 'Using the value from the source grid grid-point which is nearest '
                      'to the nominal grid-point'},
            {'abbr': 4,
             'code': 4,
             'title': 'Budget interpolation using the 4 source grid grid-point values '
                      'surrounding the nominal grid-point'},
            {'abbr': 5,
             'code': 5,
             'title': 'Spectral interpolation using the 4 source grid grid-point values '
                      'surrounding the nominal grid-point'},
            {'abbr': 6,
             'code': 6,
             'title': 'Neighbor-budget interpolation using the 4 source grid grid-point '
                      'values surrounding the nominal grid-point'},
            {'abbr': None, 'code': 255, 'title': 'Missing'})
