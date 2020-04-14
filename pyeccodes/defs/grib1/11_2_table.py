def load(h):
    return ({'bit': 1, 'on': 0, 'title': 'Reserved'},
            {'bit': 1, 'on': 1, 'title': 'Reserved'},
            {'bit': 2, 'on': 0, 'title': 'Single datum at each grid point'},
            {'bit': 2, 'on': 1, 'title': 'Matrix of values at each grid point'},
            {'bit': 3, 'on': 0, 'title': 'No secondary bitmap Present'},
            {'bit': 3, 'on': 1, 'title': 'Secondary bitmap Present'},
            {'bit': 4, 'on': 0, 'title': 'Second-order values constant width'},
            {'bit': 4, 'on': 1, 'title': 'Second-order values different widths'},
            {'bit': 5, 'on': 0, 'title': 'no general extended second order packing'},
            {'bit': 5, 'on': 1, 'title': 'general extended second order packing used'},
            {'bit': 6, 'on': 0, 'title': 'standard field ordering in section 4'},
            {'bit': 6, 'on': 1, 'title': 'boustrophedonic ordering in section 4'})
