def load(h):
    return ({'abbr': 'ocpt', 'code': 129, 'title': 'Ocean potential temperature deg C'},
            {'abbr': 's', 'code': 130, 'title': 'Salinity psu'},
            {'abbr': 'ocu',
             'code': 131,
             'title': 'Ocean current zonal component',
             'units': 'm s**-1'},
            {'abbr': 'ocv',
             'code': 132,
             'title': 'Ocean current meridional component',
             'units': 'm s**-1'},
            {'abbr': 'ocw',
             'code': 133,
             'title': 'Ocean current vertical component',
             'units': 'm s**-1'},
            {'abbr': 'mst', 'code': 134, 'title': 'Modulus of strain rate tensor s**-1'},
            {'abbr': 'vvs', 'code': 135, 'title': 'Vertical viscosity m**2 s**-1'},
            {'abbr': 'vdf', 'code': 136, 'title': 'Vertical diffusivity m**2 s**-1'},
            {'abbr': 'dep', 'code': 137, 'title': 'Bottom level Depth', 'units': 'm'},
            {'abbr': 'sth', 'code': 138, 'title': 'Sigma-theta kg m**-3'},
            {'abbr': 'rn', 'code': 139, 'title': 'Richardson number'},
            {'abbr': 'uv', 'code': 140, 'title': 'UV product m**2 s**-2'},
            {'abbr': 'ut', 'code': 141, 'title': 'UT product m s**-1 degC'},
            {'abbr': 'vt', 'code': 142, 'title': 'VT product m s**-1 deg C'},
            {'abbr': 'uu', 'code': 143, 'title': 'UU product m**2 s**-2'},
            {'abbr': 'vv', 'code': 144, 'title': 'VV product m**2 s**-2'},
            {'abbr': 'sl', 'code': 145, 'title': 'Sea level m'},
            {'abbr': 'sl_1', 'code': 146, 'title': 'Sea level previous timestep m'},
            {'abbr': 'bsf', 'code': 147, 'title': 'Barotropic stream function m**3 s**-1'},
            {'abbr': 'mld', 'code': 148, 'title': 'Mixed layer depth m'},
            {'abbr': 'btp',
             'code': 149,
             'title': 'Bottom Pressure (equivalent height)',
             'units': 'm'},
            {'abbr': 'crl', 'code': 151, 'title': 'Curl of Wind Stress N m**-3'},
            {'abbr': 152,
             'code': 152,
             'title': 'Divergence of wind stress',
             'units': 'Nm**-3'},
            {'abbr': 'tax', 'code': 153, 'title': 'U stress Pa'},
            {'abbr': 'tay', 'code': 154, 'title': 'V stress Pa'},
            {'abbr': 'tki',
             'code': 155,
             'title': 'Turbulent kinetic energy input W m**-2'},
            {'abbr': 'nsf', 'code': 156, 'title': 'Net surface heat flux W m**-2'},
            {'abbr': 'asr', 'code': 157, 'title': 'Absorbed solar radiation W m**-2'},
            {'abbr': 'pme', 'code': 158, 'title': 'Precipitation - evaporation m s**-1'},
            {'abbr': 'sst',
             'code': 159,
             'title': 'Specified sea surface temperature deg C'},
            {'abbr': 'shf', 'code': 160, 'title': 'Specified surface heat flux W m**-2'},
            {'abbr': 'dte',
             'code': 161,
             'title': 'Diagnosed sea surface temperature error deg C'},
            {'abbr': 'hfc', 'code': 162, 'title': 'Heat flux correction W m**-2'},
            {'abbr': '20d', 'code': 163, 'title': '20 degrees isotherm depth m'},
            {'abbr': 'tav300',
             'code': 164,
             'title': 'Average potential temperature in the upper 300m degrees C'},
            {'abbr': 'uba1',
             'code': 165,
             'title': 'Vertically integrated zonal velocity (previous time step) m**2 '
                      's**-1'},
            {'abbr': 'vba1',
             'code': 166,
             'title': 'Vertically Integrated meridional velocity (previous time step) '
                      'm**2 s**-1'},
            {'abbr': 'ztr',
             'code': 167,
             'title': 'Vertically integrated zonal volume transport m**2 s**-1'},
            {'abbr': 'mtr',
             'code': 168,
             'title': 'Vertically integrated meridional volume transport m**2 s**-1'},
            {'abbr': 'zht',
             'code': 169,
             'title': 'Vertically integrated zonal heat transport J m**-1 s**-1'},
            {'abbr': 'mht',
             'code': 170,
             'title': 'Vertically integrated meridional heat transport J m**-1 s**-1'},
            {'abbr': 'umax', 'code': 171, 'title': 'U velocity maximum m s**-1'},
            {'abbr': 'dumax', 'code': 172, 'title': 'Depth of the velocity maximum m'},
            {'abbr': 'smax', 'code': 173, 'title': 'Salinity maximum psu'},
            {'abbr': 'dsmax', 'code': 174, 'title': 'Depth of salinity maximum m'},
            {'abbr': 'sav300',
             'code': 175,
             'title': 'Average salinity in the upper 300m psu'},
            {'abbr': 'ldp',
             'code': 176,
             'title': 'Layer Thickness at scalar points',
             'units': 'm'},
            {'abbr': 'ldu',
             'code': 177,
             'title': 'Layer Thickness at vector points',
             'units': 'm'},
            {'abbr': 'pti', 'code': 178, 'title': 'Potential temperature increment deg C'},
            {'abbr': 'ptae',
             'code': 179,
             'title': 'Potential temperature analysis error deg C'},
            {'abbr': 'bpt',
             'code': 180,
             'title': 'Background potential temperature deg C'},
            {'abbr': 'apt', 'code': 181, 'title': 'Analysed potential temperature deg C'},
            {'abbr': 'ptbe',
             'code': 182,
             'title': 'Potential temperature background error deg C'},
            {'abbr': 'as', 'code': 183, 'title': 'Analysed salinity psu'},
            {'abbr': 'sali', 'code': 184, 'title': 'Salinity increment psu'},
            {'abbr': 'ebt', 'code': 185, 'title': 'Estimated Bias in Temperature deg C'},
            {'abbr': 'ebs', 'code': 186, 'title': 'Estimated Bias in Salinity psu'},
            {'abbr': 'uvi',
             'code': 187,
             'title': 'Zonal Velocity increment (from balance operator) m/s per time '
                      'step'},
            {'abbr': 'vvi',
             'code': 188,
             'title': 'Meridional Velocity increment',
             'units': 'from balance operator'},
            {'abbr': 'subi',
             'code': 190,
             'title': 'Salinity increment (from salinity data) psu per time step'},
            {'abbr': 'sale', 'code': 191, 'title': 'Salinity analysis error psu'},
            {'abbr': 'bsal', 'code': 192, 'title': 'Background Salinity psu'},
            {'abbr': 193, 'code': 193, 'title': '- Reserved'},
            {'abbr': 'salbe', 'code': 194, 'title': 'Salinity background error psu'},
            {'abbr': 'ebta',
             'code': 199,
             'title': 'Estimated temperature bias from assimilation deg C'},
            {'abbr': 'ebsa',
             'code': 200,
             'title': 'Estimated salinity bias from assimilation psu'},
            {'abbr': 'lti',
             'code': 201,
             'title': 'Temperature increment from relaxation term deg C per time step'},
            {'abbr': 'lsi',
             'code': 202,
             'title': 'Salinity increment from relaxation term psu per time step'},
            {'abbr': 'bzpga',
             'code': 203,
             'title': 'Bias in the zonal pressure gradient (applied)',
             'units': 'Pa**m-1'},
            {'abbr': 'bmpga',
             'code': 204,
             'title': 'Bias in the meridional pressure gradient (applied)',
             'units': 'Pa**m-1'},
            {'abbr': 'ebtl',
             'code': 205,
             'title': 'Estimated temperature bias from relaxation deg C'},
            {'abbr': 'ebsl',
             'code': 206,
             'title': 'Estimated salinity bias from relaxation psu'},
            {'abbr': 'fgbt',
             'code': 207,
             'title': 'First guess bias in temperature deg C'},
            {'abbr': 'fgbs', 'code': 208, 'title': 'First guess bias in salinity psu'},
            {'abbr': 'bpa', 'code': 209, 'title': 'Applied bias in pressure Pa'},
            {'abbr': 'fgbp', 'code': 210, 'title': 'FG bias in pressure Pa'},
            {'abbr': 'pta',
             'code': 211,
             'title': 'Bias in temperature(applied)',
             'units': 'deg C'},
            {'abbr': 'psa',
             'code': 212,
             'title': 'Bias in salinity (applied)',
             'units': 'psu'},
            {'abbr': None, 'code': 255, 'title': '- Indicates a missing value'})
