def load(h):
    return ({'bit': 1, 'on': 0, 'title': 'Points scan in +i direction'},
            {'bit': 1, 'on': 1, 'title': 'Points scan in -i direction'},
            {'bit': 2, 'on': 0, 'title': 'Points scan in -j direction'},
            {'bit': 2, 'on': 1, 'title': 'Points scan in +j direction'},
            {'bit': 3, 'on': 0, 'title': 'Adjacent points in i direction are consecutive'},
            {'bit': 3, 'on': 1, 'title': 'Adjacent points in j direction are consecutive'})
