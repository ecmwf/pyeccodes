def load(h):
    return ({'abbr': 0,
             'code': 0,
             'title': 'A bit map applies to this product and is specified in this '
                      'Section'},
            {'abbr': 1,
             'code': 1,
             'title': 'A bit map pre-determined by the originating/generating centre '
                      'applies to this product and is not specified in this Section'},
            {'abbr': 254,
             'code': 254,
             'title': 'A bit map defined previously in the same GRIB message applies to '
                      'this product'},
            {'abbr': None,
             'code': 255,
             'title': 'A bit map does not apply to this product'})
