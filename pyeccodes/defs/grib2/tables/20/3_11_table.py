def load(h):
    return ({'abbr': 0, 'code': 0, 'title': 'There is no appended list'},
            {'abbr': 1,
             'code': 1,
             'title': 'Numbers define number of points corresponding to full coordinate '
                      'circles (i.e. parallels), coordinate values on each circle are '
                      'multiple of the circle mesh, and extreme coordinate values given '
                      'in grid definition (i.e. extreme longitudes) may not be reached in '
                      'all rows'},
            {'abbr': 2,
             'code': 2,
             'title': 'Numbers define number of points corresponding to coordinate lines '
                      'delimited by extreme coordinate values given in grid definition '
                      '(i.e. extreme longitudes) which are present in each row'},
            {'abbr': 3,
             'code': 3,
             'title': 'Numbers define the actual latitudes for each row in the grid. The '
                      'list of numbers are integer values of the valid latitudes in '
                      'microdegrees (scaled by 10-6) or in unit equal to the ratio of the '
                      'basic angle and the subdivisions number for each row, in the same '
                      'order as specified in the scanning mode flag',
             'units': 'bit no. 2'},
            {'abbr': None, 'code': 255, 'title': 'Missing'})
