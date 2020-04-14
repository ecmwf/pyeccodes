def load(h):
    return ({'bit': 1,
             'on': 0,
             'title': 'Points of first row or column scan in the +i (+x) direction'},
            {'bit': 1,
             'on': 1,
             'title': 'Points of first row or column scan in the -i (-x) direction'},
            {'bit': 2,
             'on': 0,
             'title': 'Points of first row or column scan in the -j (-y) direction'},
            {'bit': 2,
             'on': 1,
             'title': 'Points of first row or column scan in the +j (+y) direction'},
            {'bit': 3,
             'on': 0,
             'title': 'Adjacent points in i (x) direction are consecutive'},
            {'bit': 3,
             'on': 1,
             'title': 'Adjacent points in j (y) direction is consecutive'},
            {'bit': 4, 'on': 0, 'title': 'All rows scan in the same direction'},
            {'bit': 4, 'on': 1, 'title': 'Adjacent rows scans in the opposite direction'})
