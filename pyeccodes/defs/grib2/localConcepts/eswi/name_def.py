import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 19:
            return 'Wind speed (space)'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return 'Atmospheric divergence'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return 'Reflectance in 3.9 micron channel'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return 'Reflectance in 1.6 micron channel'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return 'Reflectance in 0.8 micron channel'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return 'Reflectance in 0.6 micron channel'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 8:
            return 'Relative azimuth angle'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 'Solar zenith angle'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 'Number of pixel used'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 'Estimated v component of wind'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 'Estimated u component of wind'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 'Cloud top height quality indicator'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 'Cloud top height'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 'Instananeous rain rate'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 'Estimated precipitation'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 9:
            return 'Fire detection indicator'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 8:
            return 'Pixel scene type'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 'Cloud mask'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 6:
            return 'Scaled skin temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 5:
            return 'Scaled cloud top pressure'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 4:
            return 'Scaled lifted index'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 3:
            return 'Scaled precipitable water'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2:
            return 'Scaled brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1:
            return 'Scaled albedo'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 0:
            return 'Scaled radiance'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 'Saturation of soil moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 16:
            return 'Volumetric saturation of soil moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 15:
            return 'Soil porosity'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 14:
            return 'Direct evaporation cease (soil moisture)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 13:
            return 'Volumetric direct evaporation cease (soil moisture)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12:
            return 'Transpiration stress-onset (soil moisture)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 11:
            return 'Volumetric transpiration stress-onset (soil moisture)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 10:
            return 'Liquid volumetric soil moisture (non-frozen)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 'Number of soil layers in root zone'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 'Volumetric wilting point'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26:
            return 'Wilting point'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 'Volumetric soil moisture'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 'Heat flux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 'Column-integrated soil water'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'Soil moisture'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 'Soil moisture parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 'Humidity parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 19:
            return 'Temperature parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 'Solar parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 'Minimal stomatal resistance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 'Canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 'Blackadar mixing length scale'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 'Plant canopy surface water'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 'Exchange coefficient'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return 'Moisture availability'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 'Volumetric soil moisture content'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 'Land use'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'Model terrain height'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 'Evapotranspiration'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'Low cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'Total cloud cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'Snow depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'Precipitable water'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'Specific humidity'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pressure'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25:
            return 'Natural logarithm of pressure in Pa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24:
            return 'Anisotropy of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23:
            return 'Gravity wave dissipation'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'Slope of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21:
            return 'Angle of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'Standard deviation of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return '5-wave geopotential height anomaly'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 'Planetary boundary layer height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 'Meridional flux of gravity wave stress'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 'Zonal flux of gravity wave stress'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return '5-wave geopotential height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 'Density altitude'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 'Pressure altitude'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 'Thickness'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 'Altimeter setting'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 32:
            return 'Eta coordinate vertical velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 'Drag coefficient'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 'v-component storm motion'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 'u-component storm motion'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 'Horizontal momentum flux'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 'Vertical speed shear'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'v-component of wind (gust)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 'u-component of wind (gust)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'Specific snow water content'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'Specific rain water content'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 84:
            return 'Specific cloud ice water content'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 83:
            return 'Specific cloud liquid water content'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 'Ice pellets precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 'Freezing rain precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66:
            return 'Snow precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65:
            return 'Rain precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 'Total column integrated water vapour'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 62:
            return 'Snow evaporation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60:
            return 'Snow depth water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 'Large scale snowfall rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 'Convective snowfall rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 57:
            return 'Total snowfall rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 'Large scale snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 'Convective snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54:
            return 'Large scale precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'Total column water (Vertically integrated total water)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'Total snow precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'Total water precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'Total column integrated snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'Total column integrated rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'Rain factor'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'Rain fraction of total cloud water'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 23:
            return 'Angstrom coefficient'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 22:
            return 'Aerosol optical thickness at 1.640 micro-m'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 21:
            return 'Aerosol optical thickness at 0.810 micro-m'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 20:
            return 'Aerosol optical thickness at 0.635 micro-m'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 'Volcanic ash'

        atmosphericChemicalConsituentType = h.get_l('atmosphericChemicalConsituentType')

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10006:
            return 'HCN/Vaetecyanid'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10022:
            return 'TOLUENE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10021:
            return 'BENZENE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10012:
            return 'C2H5OOH/Ethyl hydroperoxide'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10002:
            return 'CH3O2H/Methyl hydroperoxide'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10001:
            return 'CH3O2/Methyl peroxy radical'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 12:
            return 'O/Oxygen atomic ground state (3P)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 20:
            return 'H2/Molecular hydrogen'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 14:
            return 'HO2/Hydroperhydroxyl radical'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 16:
            return 'HONO'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 18:
            return 'HO2NO2/HO2NO2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 15:
            return 'N2O5/Dinitrogen pentoxide'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 13:
            return 'NO3/Nitrate radical'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63011:
            return 'PAN/Peroxy acetyl nitrate'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60013:
            return 'NMVOC_C/Total NMVOC as C'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10004:
            return 'CH3OH/Metanol'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10011:
            return 'C2H5OH/Ethanol'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10017:
            return 'C5H8/Isoprene'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 7:
            return 'HCHO/Formalydehyde'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10023:
            return 'OXYLENE/O-xylene'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10015:
            return 'C3H6/Propene'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10009:
            return 'C2H4/Ethene'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10016:
            return 'NC4H10/N-butane'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10008:
            return 'C2H6/Ethane'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'Turbulent Kinetic Energy'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 1:
            return 'Meridional overturning stream function'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 'Seconds prior to initial reference time (defined in section1) (oceonography)'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return 'Probability if 0.01 inch of precipitation'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return 'Per cent precipitation in a sub-period of an overall period'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 'Conditional per cent precipitation amount fractile for an overall period'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 'Storm surface runoff'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 'Baseflow-groundwater runoff'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return 'Snow water equivalent per cent of normal'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return 'Elevation of snow-covered terrain'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return 'Remotely-sensed snow cover'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 'Flash flood runoff'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 'Flash flood guidance'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'Mean direction of Waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 'Mean period of waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 'Secondary wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'Secondary wave direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 'Primary wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'Primary wave direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 'Mean Period Swell Waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'Sign Height Swell Waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'Direction of Swell Waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'Mean Period Wind Waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'Sign Height Wind Waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'Direction of Wind Waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'Significant wave height'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 'Ice divergence'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 'Ice growth rate'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'Speed of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'Direction of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'Total ice thickness'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'Ice Cover'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'Density'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'Water temperature'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'Total Cloud Cover'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'Main thermocline anomaly'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'Main thermocline depth'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'Transient thermocline depth'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'Mixed layer depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'Snow Depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'Specific humidity'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'V-comp of Current'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'U-comp of Current'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'Speed of horizontal current'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'Direction of horizontal current'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'Montgomery stream function'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'Velocity potential'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'Stream function'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'Wind speed'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'Wind direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'Wave spectra (3)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'Wave spectra (2)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'Wave spectra (1)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'Potential temperature'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'Turbulent Kintetic Energy'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'Current north'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'Current east'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 'Seconds prior to initial reference time (defined in section1) (meteorology)'

        if discipline == 0 and parameterCategory == 190 and parameterNumber == 0:
            return 'Arbitrary text string'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return 'Supercooled large droplet probability'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return 'Clear air turbulence (CAT)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return 'In-cloud turbulence'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return 'Icing'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return 'Snow free albedo'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 'Contrail base'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 'Contrail top'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 'Contrail engine type'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 'Contrail intensity'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 'Planetary boundary-layer regime'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 'Turbulence'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 'Turbulence base'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 'Turbulence top'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'Icing'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 6:
            return 'Icing base'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 5:
            return 'Icing top'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5:
            return 'Composite reflectivity (radar)'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 4:
            return 'Reflectivity (radar)'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 3:
            return 'Echo top (radar)'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 2:
            return 'Equivalent radar reflectivity factor for paramterized convection'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 1:
            return 'Equivalent radar reflectivity factor for snow'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 0:
            return 'Equivalent radar reflectivity factor for rain'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5:
            return 'Precipitation (radar)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 'Layer-maximum base reflectivity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 'Vertically integrated liquid'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 'Base radial velocity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 'Base reflectivity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 'Base spectrum width'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 'Total column integrated ozone'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'Ozone mixing ratio'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'Aerosol type'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 12:
            return 'Richardson number'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return 'Best (4-layer) lifted index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 'Surface lifted index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 'Energy helicity index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 'Storm relative helicity'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 'Sweat index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 'Total totals index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 'KO index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 'K index'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 33:
            return 'Sunshine duration'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 32:
            return 'Fraction of cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return 'Horizontal extent of cumulunimbus (CB)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24:
            return 'Sunshine'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 'Cloud ice mixing ratio'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return 'Cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 21:
            return 'Ice fraction of total condensate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'Total column-integrated condensate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 19:
            return 'Total column-integrated cloud ice'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 18:
            return 'Total column-integrated cloud water'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 17:
            return 'Total condensate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 16:
            return 'Convective cloud efficiency'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 15:
            return 'Cloud work function'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return 'Non-convective cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 'Ceiling'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'Cloud top'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'Cloud base'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 10:
            return 'Thunderstorm coverage'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 9:
            return 'Thunderstorm maximum tops'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 8:
            return 'Cloud type'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return 'Cloud amount'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'Net long-wave radiation flux, clear sky'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5:
            return 'Net long wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'Upward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'Downward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 'UV index'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50:
            return 'UV index (under clear sky)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 'Downward UV radiation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 'Net short-wave radiation flux, clear sky'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10:
            return 'Photosynthetically active radiation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9:
            return 'Net short wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8:
            return 'Upward short-wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 'Downward short-wave radiation flux'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'Precipitation intensity snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'Precipitation intensity total'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'Wind gust'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 'cloud mask'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'High cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'Medium cloud cove'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'Low cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return 'Convective cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'Total cloud cover'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 'Probability thunderstorm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'Relative humidity'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'Visibility'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return 'Snow cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 'Potential evaporation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 'Potential evaporation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return 'Percent frozen precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 38:
            return 'Horizontal moisture divergence'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37:
            return 'Convective precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return 'Categorical snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return 'Categorical ice pellets'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return 'Categorical freezing rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return 'Categorical rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'Graupel'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 'Hail'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 'Precipitable water category'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 'Horizontal moisture convergence'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 'Snow mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 'Rain mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 'Ice water mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 'Cloud mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 21:
            return 'Condensate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 20:
            return 'Integrated liquid water'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 19:
            return 'Precipitation type'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18:
            return 'Absolute humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 17:
            return 'Snow age'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17:
            return 'Skin temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'Snow phase change heat flux'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'Wind chill factor'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'Heat index'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'Virtual potential temperature'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 'Cloud top of significant clouds'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 'Cloud base of significant clouds'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'High cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'Medium cloud cove'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'Low cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'Total cloud cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'Relative humidity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'Wind gusts'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'Visibility'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'Minimum temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'Maximum temperature'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'VIS/Visibility [m]'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62000:
            return 'PM/Total particulate matter'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40009:
            return 'PM2.5/PM2.5 particles'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62012:
            return 'SOA/Secondary Organic Aerosol'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63016:
            return 'PNHX/Particulate ammonium'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63015:
            return 'PNOX/Particulate nitrate'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63014:
            return 'PSOX/Particulate sulfate'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40008:
            return 'PM10/PM10 particles'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63018:
            return 'PMASS/Particle mass conc'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63017:
            return 'PNUMBER/Number concentration'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62001:
            return 'DUST/Dust (particles)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40008:
            return 'PMCOARSE/Coarse particles'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 40009:
            return 'PMFINE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 62008:
            return 'NACL'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 23:
            return 'Rn222/Rn222'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63012:
            return 'EC/Elementary carbon (particles)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63013:
            return 'OC/Organic carbon (particles)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 2:
            return 'CH4/CH4'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 3:
            return 'CO2/CO2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 4:
            return 'CO/CO'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10000:
            return 'OH/OH'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 19:
            return 'H2O2/H2O2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 0:
            return 'O3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63004:
            return 'NHX_N/All reduced nitrogen (as nitrogen)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10:
            return 'NH4(+1)/NH4'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 9:
            return 'NH3/NH3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60004:
            return 'NOY_N/All oxidised N-compounds (as nitrogen)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 60003:
            return 'NOX_N/NO2+NO (NOx) as nitrogen'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63001:
            return 'NOX/NOX as NO2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63009:
            return 'NITRATE/NITRATE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63007:
            return 'NH4NO3/NH4NO3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 17:
            return 'HNO3/HNO3'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 5:
            return 'NO2/NO2'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 11:
            return 'NO'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63005:
            return 'SOX_S/All oxidised sulphur compounds (as sulphur)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63008:
            return 'SULFATE/SULFATE'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 63006:
            return 'NH42SO4/(NH4)2SO4'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 10500:
            return 'DMS/DMS'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 22:
            return 'SO4(2-)/SO4(2-) (sulphate)'

        if discipline == 0 and parameterCategory == 20 and atmosphericChemicalConsituentType == 8:
            return 'SO2/SO2'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'Wind gust'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'Friction velocity'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'CAPE'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'Convective inhibation'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'Turbulent Kinetic Energy'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0:
            return 'Soil type'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 'Snow density'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 19:
            return 'Snow albedo'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'Slope fraction'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'Snow depth, cold snow'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 'Integrated cloud condensate'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'Maximum wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'Wind mixing energy'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18:
            return 'Momentum flux, v component'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17:
            return 'Momentum flux, u component'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'Boundary layer dissipation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11:
            return 'Sensible heat net flux'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10:
            return 'Latent heat net flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'Radiance (with respect to wave length)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'Radiance (with respect to wave number)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'Brightness temperature'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'Global radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 2:
            return 'Short wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 2:
            return 'Long wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'Net long wave radiation flux (top of atmos.)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'Net short wave radiation flux (top of atmos.)'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'Net long wave radiation flux (surface)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'Net short wave radiation flux (surface)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 'Secondary wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'Secondary wave direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 'Primary wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'Primary wave direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 'Mean period of swell waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 'Significant height of swell waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 'Direction of swell waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'Mean period of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'Significant height of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'Direction of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'Significant height of combined wind waves and swell'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16:
            return 'Snow melt'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 'Ice divergence'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 'Ice growth rate'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 'v-component of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 'u-component of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'Speed of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'Direction of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'Ice thickness'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'Ice cover (ice=1 no ice=0)(see note)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5:
            return 'Water run off'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'Density'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 'Salinity'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return 'Vegetation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 'Soil moisture content'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'Soil temperature'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return 'Albedo'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'Surface roughness'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'Deviation of sea level from mean'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'Land-sea mask (1=land 0=sea) (see note)'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'Water Temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 'Large scale snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 'Convective snow'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 'Best lifted index (to 500 hPa)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'Cloud water'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'High cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'Medium cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'Low cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return 'Convective cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'Total cloud cover'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'Main thermocline anomaly'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'Main thermocline depth'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'Transient thermocline depth'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'Mixed layer depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'Snow depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'Water equiv. of accum. snow depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 'Snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'Convective precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 'Large scale precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 8:
            return 'Total precipitation'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 'Thunderstorm probability'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 'Precipitation rate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 'Cloud Ice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 6:
            return 'Evaporation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 'Saturation deficit'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'Vapour pressure'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'Precipitable water'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2:
            return 'Humidity mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'Relative humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'Specific humidity'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'v-component of current'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'u-component of current'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'Speed of current'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'Direction of current'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 'Vertical v-component shear'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 'Vertical u-component shear'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 'Relative divergence'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 'Relative vorticity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 'Absolute divergence'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'Absolute vorticity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'Geometric Vertical velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'Pressure Vertical velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 'Sigma coord. vertical velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'Montgomery stream function'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'Velocity potential'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'Stream function'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'v-component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'u-component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'Wind speed'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'Wind direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'Wave Spectra (3)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'Wave Spectra (2)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'Wave Spectra (1)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 'Geopotential height anomaly'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 'Pressure anomaly'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 'Temperature anomaly'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 'Parcel lifted index (to 500 hPa)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return 'Radar Spectra (3)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return 'Radar Spectra (2)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6:
            return 'Radar Spectra (1)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'Visibility'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 'Lapse rate'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7:
            return 'Dew point depression (or deficit)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'Dew point temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'Minimum temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'Maximum temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'Pseudo-adiabatic potential temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'Potential temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'Virtual temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'Temperature'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0:
            return 'Total ozone'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'Standard deviation of height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'Geometric height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'Geopotential height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'Geopotential'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'ICAO Standard Atmosphere reference height'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'Potential vorticity'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2:
            return 'Pressure tendency'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pressure'

    return wrapped
