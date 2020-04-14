def load(h):
    return ({'abbr': 'ERS-1', 'code': 1, 'title': 'ERS 1'},
            {'abbr': 'ERS-2', 'code': 2, 'title': 'ERS 2'},
            {'abbr': 'METOP-B', 'code': 3, 'title': 'METOP-B'},
            {'abbr': 'METOP-A', 'code': 4, 'title': 'METOP-A'},
            {'abbr': 'CHAMP', 'code': 41, 'title': 'CHAMP'},
            {'abbr': 'TERRA-SAR-X', 'code': 42, 'title': 'TERRA-SAR-X'},
            {'abbr': 'SMOS', 'code': 46, 'title': 'SMOS'},
            {'abbr': 'METEOSAT-7', 'code': 54, 'title': 'METEOSAT 7'},
            {'abbr': 'METEOSAT-8', 'code': 55, 'title': 'METEOSAT 8'},
            {'abbr': 'METEOSAT-9', 'code': 56, 'title': 'METEOSAT 9'},
            {'abbr': 'METEOSAT-10', 'code': 57, 'title': 'METEOSAT 10'},
            {'abbr': 'METEOSAT-1', 'code': 58, 'title': 'METEOSAT 1'},
            {'abbr': 'METEOSAT-2', 'code': 59, 'title': 'METEOSAT 2'},
            {'abbr': 'ENVISAT', 'code': 60, 'title': 'ENVISAT'},
            {'abbr': 'METEOSAT-11', 'code': 70, 'title': 'METEOSAT-11'},
            {'abbr': 'GCOM-W1', 'code': 122, 'title': 'GCOM-W1'},
            {'abbr': 'GOSAT', 'code': 140, 'title': 'GOSAT'},
            {'abbr': 'MTSAT-1R', 'code': 171, 'title': 'MTSAT-1R'},
            {'abbr': 'MTSAT-2', 'code': 172, 'title': 'MTSAT-2'},
            {'abbr': 'NOAA-8', 'code': 200, 'title': 'NOAA-8'},
            {'abbr': 'NOAA-9', 'code': 201, 'title': 'NOAA-9'},
            {'abbr': 'NOAA-10', 'code': 202, 'title': 'NOAA-10'},
            {'abbr': 'NOAA-11', 'code': 203, 'title': 'NOAA-11'},
            {'abbr': 'NOAA-12', 'code': 204, 'title': 'NOAA-12'},
            {'abbr': 'NOAA-14', 'code': 205, 'title': 'NOAA 14'},
            {'abbr': 'NOAA-15', 'code': 206, 'title': 'NOAA 15'},
            {'abbr': 'NOAA-16', 'code': 207, 'title': 'NOAA 16'},
            {'abbr': 'NOAA-17', 'code': 208, 'title': 'NOAA 17'},
            {'abbr': 'NOAA-18', 'code': 209, 'title': 'NOAA 18'},
            {'abbr': 'AQUA', 'code': 222, 'title': 'AQUA'},
            {'abbr': 'NOAA-19', 'code': 223, 'title': 'NOAA 19'},
            {'abbr': 'NPP', 'code': 224, 'title': 'NPP'},
            {'abbr': 'DMSP-7', 'code': 240, 'title': 'DMSP-7'},
            {'abbr': 'DMSP-8', 'code': 241, 'title': 'DMSP-8'},
            {'abbr': 'DMSP-9', 'code': 242, 'title': 'DMSP-9'},
            {'abbr': 'DMSP-10', 'code': 243, 'title': 'DMSP-10'},
            {'abbr': 'DMSP-11', 'code': 244, 'title': 'DMSP-11'},
            {'abbr': 'DMSP-13', 'code': 246, 'title': 'DMSP-13'},
            {'abbr': 'DMSP-13', 'code': 246, 'title': 'DMSP 13'},
            {'abbr': 'DMSP-14', 'code': 247, 'title': 'DMSP 14'},
            {'abbr': 'DMSP-15', 'code': 248, 'title': 'DMSP 15'},
            {'abbr': 'DMSP-16', 'code': 249, 'title': 'DMSP 16'},
            {'abbr': 'GOES-9', 'code': 253, 'title': 'GOES 9'},
            {'abbr': 'GOES-10', 'code': 254, 'title': 'GOES 10'},
            {'abbr': 'GEOS-11', 'code': 255, 'title': 'GOES 11'},
            {'abbr': 'GEOS-12', 'code': 256, 'title': 'GOES 12'},
            {'abbr': 'GEOS-13', 'code': 257, 'title': 'GOES 13'},
            {'abbr': 'GEOS-14', 'code': 258, 'title': 'GOES 14'},
            {'abbr': 'GEOS-15', 'code': 259, 'title': 'GOES 15'},
            {'abbr': 'JASON-1', 'code': 260, 'title': 'JASON-1'},
            {'abbr': 'JASON-2', 'code': 261, 'title': 'JASON-2'},
            {'abbr': 'QUIKSCAT', 'code': 281, 'title': 'QUIKSCAT'},
            {'abbr': 'TRMM', 'code': 282, 'title': 'TRMM'},
            {'abbr': 'CORIOLIS', 'code': 283, 'title': 'CORIOLIS'},
            {'abbr': 'DMSP17', 'code': 285, 'title': 'DMSP 17'},
            {'abbr': 'DMSP18', 'code': 286, 'title': 'DMSP 18'},
            {'abbr': 'OCEANSAT-2', 'code': 421, 'title': 'OCEANSAT-2'},
            {'abbr': 'FY-1C', 'code': 500, 'title': 'FY-1C'},
            {'abbr': 'FY-1D', 'code': 501, 'title': 'FY-1D'},
            {'abbr': 'FY-2', 'code': 510, 'title': 'FY-2'},
            {'abbr': 'FY-2B', 'code': 512, 'title': 'FY-2B'},
            {'abbr': 'FY-2C', 'code': 513, 'title': 'FY-2C'},
            {'abbr': 'FY-2D', 'code': 514, 'title': 'FY-2D'},
            {'abbr': 'FY-2E', 'code': 515, 'title': 'FY-2E'},
            {'abbr': 'FY-3A', 'code': 520, 'title': 'FY-3A'},
            {'abbr': 'FY-3B', 'code': 521, 'title': 'FY-3B'},
            {'abbr': 'GRACE-A', 'code': 722, 'title': 'GRACE-A'},
            {'abbr': 'NOAA-6', 'code': 706, 'title': 'NOAA-6'},
            {'abbr': 'NOAA-7', 'code': 707, 'title': 'NOAA-7'},
            {'abbr': 'TIROS-N', 'code': 708, 'title': 'TIROS-N'},
            {'abbr': 'COSMIC-1', 'code': 740, 'title': 'COSMIC-1'},
            {'abbr': 'COSMIC-2', 'code': 741, 'title': 'COSMIC-2'},
            {'abbr': 'COSMIC-3', 'code': 742, 'title': 'COSMIC-3'},
            {'abbr': 'COSMIC-4', 'code': 743, 'title': 'COSMIC-4'},
            {'abbr': 'COSMIC-5', 'code': 744, 'title': 'COSMIC-5'},
            {'abbr': 'COSMIC-6', 'code': 745, 'title': 'COSMIC-6'},
            {'abbr': 'TERRA', 'code': 783, 'title': 'TERRA'},
            {'abbr': 'AQUA', 'code': 784, 'title': 'AQUA'},
            {'abbr': 'AURA', 'code': 785, 'title': 'AURA'},
            {'abbr': 'C-NOFS', 'code': 786, 'title': 'C-NOFS'},
            {'abbr': 'SAC-C', 'code': 820, 'title': 'SAC-C'})
