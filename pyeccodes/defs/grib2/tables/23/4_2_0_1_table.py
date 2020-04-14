def load(h):
    return ({'abbr': 0, 'code': 0, 'title': 'Specific humidity', 'units': 'kg/kg'},
            {'abbr': 1, 'code': 1, 'title': 'Relative humidity', 'units': '%'},
            {'abbr': 2, 'code': 2, 'title': 'Humidity mixing ratio', 'units': 'kg/kg'},
            {'abbr': 3, 'code': 3, 'title': 'Precipitable water', 'units': 'kg m-2'},
            {'abbr': 4, 'code': 4, 'title': 'Vapour pressure', 'units': 'Pa'},
            {'abbr': 5, 'code': 5, 'title': 'Saturation deficit', 'units': 'Pa'},
            {'abbr': 6, 'code': 6, 'title': 'Evaporation', 'units': 'kg m-2'},
            {'abbr': 7, 'code': 7, 'title': 'Precipitation rate', 'units': 'kg m-2 s-1'},
            {'abbr': 8, 'code': 8, 'title': 'Total precipitation', 'units': 'kg m-2'},
            {'abbr': 9,
             'code': 9,
             'title': 'Large-scale precipitation (non-convective)',
             'units': 'kg m-2'},
            {'abbr': 10,
             'code': 10,
             'title': 'Convective precipitation',
             'units': 'kg m-2'},
            {'abbr': 11, 'code': 11, 'title': 'Snow depth', 'units': 'm'},
            {'abbr': 12,
             'code': 12,
             'title': 'Snowfall rate water equivalent',
             'units': 'kg m-2 s-1'},
            {'abbr': 13,
             'code': 13,
             'title': 'Water equivalent of accumulated snow depth',
             'units': 'kg m-2'},
            {'abbr': 14, 'code': 14, 'title': 'Convective snow', 'units': 'kg m-2'},
            {'abbr': 15, 'code': 15, 'title': 'Large-scale snow', 'units': 'kg m-2'},
            {'abbr': 16, 'code': 16, 'title': 'Snow melt', 'units': 'kg m-2'},
            {'abbr': 17, 'code': 17, 'title': 'Snow age', 'units': 'd'},
            {'abbr': 18, 'code': 18, 'title': 'Absolute humidity', 'units': 'kg m-3'},
            {'abbr': 19,
             'code': 19,
             'title': 'Precipitation type',
             'units': 'Code table 4.201'},
            {'abbr': 20,
             'code': 20,
             'title': 'Integrated liquid water',
             'units': 'kg m-2'},
            {'abbr': 21, 'code': 21, 'title': 'Condensate', 'units': 'kg/kg'},
            {'abbr': 22, 'code': 22, 'title': 'Cloud mixing ratio', 'units': 'kg/kg'},
            {'abbr': 23, 'code': 23, 'title': 'Ice water mixing ratio', 'units': 'kg/kg'},
            {'abbr': 24, 'code': 24, 'title': 'Rain mixing ratio', 'units': 'kg/kg'},
            {'abbr': 25, 'code': 25, 'title': 'Snow mixing ratio', 'units': 'kg/kg'},
            {'abbr': 26,
             'code': 26,
             'title': 'Horizontal moisture convergence',
             'units': 'kg kg-1 s-1'},
            {'abbr': 27, 'code': 27, 'title': 'Maximum relative humidity', 'units': '%'},
            {'abbr': 28,
             'code': 28,
             'title': 'Maximum absolute humidity',
             'units': 'kg m-3'},
            {'abbr': 29, 'code': 29, 'title': 'Total snowfall', 'units': 'm'},
            {'abbr': 30,
             'code': 30,
             'title': 'Precipitable water category',
             'units': 'Code table 4.202'},
            {'abbr': 31, 'code': 31, 'title': 'Hail', 'units': 'm'},
            {'abbr': 32, 'code': 32, 'title': 'Graupel (snow pellets)', 'units': 'kg/kg'},
            {'abbr': 33,
             'code': 33,
             'title': 'Categorical rain',
             'units': 'Code table 4.222'},
            {'abbr': 34,
             'code': 34,
             'title': 'Categorical freezing rain',
             'units': 'Code table 4.222'},
            {'abbr': 35,
             'code': 35,
             'title': 'Categorical ice pellets',
             'units': 'Code table 4.222'},
            {'abbr': 36,
             'code': 36,
             'title': 'Categorical snow',
             'units': 'Code table 4.222'},
            {'abbr': 37,
             'code': 37,
             'title': 'Convective precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 38,
             'code': 38,
             'title': 'Horizontal moisture divergence',
             'units': 'kg kg-1 s-1'},
            {'abbr': 39,
             'code': 39,
             'title': 'Per cent frozen precipitation',
             'units': '%'},
            {'abbr': 40, 'code': 40, 'title': 'Potential evaporation', 'units': 'kg m-2'},
            {'abbr': 41,
             'code': 41,
             'title': 'Potential evaporation rate',
             'units': 'W m-2'},
            {'abbr': 42, 'code': 42, 'title': 'Snow cover', 'units': '%'},
            {'abbr': 43,
             'code': 43,
             'title': 'Rain fraction of total cloud water',
             'units': 'Proportion'},
            {'abbr': 44, 'code': 44, 'title': 'Rime factor', 'units': 'Numeric'},
            {'abbr': 45,
             'code': 45,
             'title': 'Total column integrated rain',
             'units': 'kg m-2'},
            {'abbr': 46,
             'code': 46,
             'title': 'Total column integrated snow',
             'units': 'kg m-2'},
            {'abbr': 47,
             'code': 47,
             'title': 'Large scale water precipitation (non-convective)',
             'units': 'kg m-2'},
            {'abbr': 48,
             'code': 48,
             'title': 'Convective water precipitation',
             'units': 'kg m-2'},
            {'abbr': 49,
             'code': 49,
             'title': 'Total water precipitation',
             'units': 'kg m-2'},
            {'abbr': 50,
             'code': 50,
             'title': 'Total snow precipitation',
             'units': 'kg m-2'},
            {'abbr': 51,
             'code': 51,
             'title': 'Total column water (Vertically integrated total water (vapour + '
                      'cloud water/ice))',
             'units': 'kg m-2'},
            {'abbr': 52,
             'code': 52,
             'title': 'Total precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 53,
             'code': 53,
             'title': 'Total snowfall rate water equivalent',
             'units': 'kg m-2 s-1'},
            {'abbr': 54,
             'code': 54,
             'title': 'Large scale precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 55,
             'code': 55,
             'title': 'Convective snowfall rate water equivalent',
             'units': 'kg m-2 s-1'},
            {'abbr': 56,
             'code': 56,
             'title': 'Large scale snowfall rate water equivalent',
             'units': 'kg m-2 s-1'},
            {'abbr': 57, 'code': 57, 'title': 'Total snowfall rate', 'units': 'm/s'},
            {'abbr': 58, 'code': 58, 'title': 'Convective snowfall rate', 'units': 'm/s'},
            {'abbr': 59, 'code': 59, 'title': 'Large scale snowfall rate', 'units': 'm/s'},
            {'abbr': 60,
             'code': 60,
             'title': 'Snow depth water equivalent',
             'units': 'kg m-2'},
            {'abbr': 61, 'code': 61, 'title': 'Snow density', 'units': 'kg m-3'},
            {'abbr': 62, 'code': 62, 'title': 'Snow evaporation', 'units': 'kg m-2'},
            {'abbr': 63, 'code': 63, 'title': 'Reserved'},
            {'abbr': 64,
             'code': 64,
             'title': 'Total column integrated water vapour',
             'units': 'kg m-2'},
            {'abbr': 65,
             'code': 65,
             'title': 'Rain precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 66,
             'code': 66,
             'title': 'Snow precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 67,
             'code': 67,
             'title': 'Freezing rain precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 68,
             'code': 68,
             'title': 'Ice pellets precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 69,
             'code': 69,
             'title': 'Total column integrated cloud water',
             'units': 'kg m-2'},
            {'abbr': 70,
             'code': 70,
             'title': 'Total column integrated cloud ice',
             'units': 'kg m-2'},
            {'abbr': 71, 'code': 71, 'title': 'Hail mixing ratio', 'units': 'kg/kg'},
            {'abbr': 72,
             'code': 72,
             'title': 'Total column integrated hail',
             'units': 'kg m-2'},
            {'abbr': 73,
             'code': 73,
             'title': 'Hail precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 74,
             'code': 74,
             'title': 'Total column integrated graupel',
             'units': 'kg m-2'},
            {'abbr': 75,
             'code': 75,
             'title': 'Graupel (snow pellets) precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 76,
             'code': 76,
             'title': 'Convective rain rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 77,
             'code': 77,
             'title': 'Large scale rain rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 78,
             'code': 78,
             'title': 'Total column integrated water (all components including '
                      'precipitation)',
             'units': 'kg m-2'},
            {'abbr': 79, 'code': 79, 'title': 'Evaporation rate', 'units': 'kg m-2 s-1'},
            {'abbr': 80, 'code': 80, 'title': 'Total condensate', 'units': 'kg/kg'},
            {'abbr': 81,
             'code': 81,
             'title': 'Total column-integrated condensate',
             'units': 'kg m-2'},
            {'abbr': 82, 'code': 82, 'title': 'Cloud ice mixing-ratio', 'units': 'kg/kg'},
            {'abbr': 83,
             'code': 83,
             'title': 'Specific cloud liquid water content',
             'units': 'kg/kg'},
            {'abbr': 84,
             'code': 84,
             'title': 'Specific cloud ice water content',
             'units': 'kg/kg'},
            {'abbr': 85,
             'code': 85,
             'title': 'Specific rainwater content',
             'units': 'kg/kg'},
            {'abbr': 86,
             'code': 86,
             'title': 'Specific snow water content',
             'units': 'kg/kg'},
            {'abbr': 87,
             'code': 87,
             'title': 'Stratiform precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 88,
             'code': 88,
             'title': 'Categorical convective precipitation',
             'units': 'Code table 4.222'},
            {'abbr': 90,
             'code': 90,
             'title': 'Total kinematic moisture flux',
             'units': 'kg kg-1 m s-1'},
            {'abbr': 91,
             'code': 91,
             'title': 'u-component (zonal) kinematic moisture flux',
             'units': 'kg kg-1 m s-1'},
            {'abbr': 92,
             'code': 92,
             'title': 'v-component (meridional) kinematic moisture flux',
             'units': 'kg kg-1 m s-1'},
            {'abbr': 93,
             'code': 93,
             'title': 'Relative humidity with respect to water',
             'units': '%'},
            {'abbr': 94,
             'code': 94,
             'title': 'Relative humidity with respect to ice',
             'units': '%'},
            {'abbr': 95,
             'code': 95,
             'title': 'Freezing or frozen precipitation rate',
             'units': 'kg m-2 s-1'},
            {'abbr': 96, 'code': 96, 'title': 'Mass density of rain', 'units': 'kg m-3'},
            {'abbr': 97, 'code': 97, 'title': 'Mass density of snow', 'units': 'kg m-3'},
            {'abbr': 98,
             'code': 98,
             'title': 'Mass density of graupel',
             'units': 'kg m-3'},
            {'abbr': 99, 'code': 99, 'title': 'Mass density of hail', 'units': 'kg m-3'},
            {'abbr': 100,
             'code': 100,
             'title': 'Specific number concentration of rain',
             'units': 'kg-1'},
            {'abbr': 101,
             'code': 101,
             'title': 'Specific number concentration of snow',
             'units': 'kg-1'},
            {'abbr': 102,
             'code': 102,
             'title': 'Specific number concentration of graupel',
             'units': 'kg-1'},
            {'abbr': 103,
             'code': 103,
             'title': 'Specific number concentration of hail',
             'units': 'kg-1'},
            {'abbr': 104, 'code': 104, 'title': 'Number density of rain', 'units': 'm-3'},
            {'abbr': 105, 'code': 105, 'title': 'Number density of snow', 'units': 'm-3'},
            {'abbr': 106,
             'code': 106,
             'title': 'Number density of graupel',
             'units': 'm-3'},
            {'abbr': 107, 'code': 107, 'title': 'Number density of hail', 'units': 'm-3'},
            {'abbr': 108,
             'code': 108,
             'title': 'Specific humidity tendency due to parameterization',
             'units': 'kg kg-1 s-1'},
            {'abbr': 109,
             'code': 109,
             'title': 'Mass density of liquid water coating on hail expressed as mass of '
                      'liquid water per unit volume of air',
             'units': 'kg m-3'},
            {'abbr': 110,
             'code': 110,
             'title': 'Specific mass of liquid water coating on hail expressed as mass of '
                      'liquid water per unit mass of moist air',
             'units': 'kg kg-1'},
            {'abbr': 111,
             'code': 111,
             'title': 'Mass mixing ratio of liquid water coating on hail expressed as '
                      'mass of liquid water per unit mass of dry air',
             'units': 'kg kg-1'},
            {'abbr': 112,
             'code': 112,
             'title': 'Mass density of liquid water coating on graupel expressed as mass '
                      'of liquid water per unit volume of air',
             'units': 'kg m-3'},
            {'abbr': 113,
             'code': 113,
             'title': 'Specific mass of liquid water coating on graupel expressed as mass '
                      'of liquid water per unit mass of moist air',
             'units': 'kg kg-1'},
            {'abbr': 114,
             'code': 114,
             'title': 'Mass mixing ratio of liquid water coating on graupel expressed as '
                      'mass of liquid water per unit mass of dry air',
             'units': 'kg kg-1'},
            {'abbr': 115,
             'code': 115,
             'title': 'Mass density of liquid water coating on snow expressed as mass of '
                      'liquid water per unit volume of air',
             'units': 'kg m-3'},
            {'abbr': 116,
             'code': 116,
             'title': 'Specific mass of liquid water coating on snow expressed as mass of '
                      'liquid water per unit mass of moist air',
             'units': 'kg kg-1'},
            {'abbr': 117,
             'code': 117,
             'title': 'Mass mixing ratio of liquid water coating on snow expressed as '
                      'mass of liquid water per unit mass of dry air',
             'units': 'kg kg-1'},
            {'abbr': 118,
             'code': 118,
             'title': 'Unbalanced component of specific humidity',
             'units': 'kg kg-1'},
            {'abbr': 119,
             'code': 119,
             'title': 'Unbalanced component of specific cloud liquid water content',
             'units': 'kg kg-1'},
            {'abbr': 120,
             'code': 120,
             'title': 'Unbalanced component of specific cloud ice water content',
             'units': 'kg kg-1'},
            {'abbr': 121,
             'code': 121,
             'title': 'Fraction of snow cover',
             'units': 'Proportion'},
            {'abbr': None, 'code': 255, 'title': 'Missing'})
