import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Total Precipitation'

        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106:
            return 'Wilting point'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1:
            return 'Field capacity'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Total Cloud Cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Snow Fall water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 'Snow depth water equivalent'

        is_tigge = h.get_l('is_tigge')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and is_tigge == 1:
            return 'Soil Temperature'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'Soil Temperature'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and is_tigge == 1:
            return 'Soil Moisture'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'Soil Moisture'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'Orography'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Convective inhibition'

        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')
        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')
        scaleFactorOfLowerLimit = h.get_l('scaleFactorOfLowerLimit')
        probabilityType = h.get_l('probabilityType')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 2 and scaledValueOfLowerLimit == 20 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103 and scaleFactorOfLowerLimit == 0 and scaleFactorOfFirstFixedSurface == 0 and probabilityType == 3:
            return '10 metre wind gust of at least 20 m/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and probabilityType == 3 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == 0 and typeOfStatisticalProcessing == 2 and scaledValueOfLowerLimit == 15 and scaledValueOfFirstFixedSurface == 10:
            return '10 metre wind gust of at least 15 m/s'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'Wind mixing energy'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'Radiance (with respect to wave length)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'Radiance (with respect to wave number)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'Global radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'Net short-wave radiation flux (surface)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'Secondary wave direction'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16:
            return 'Snow melt'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 'Ice divergence'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 'Ice growth rate'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 'V-component of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 'U-component of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 'Speed of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 'Direction of ice drift'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'Ice thickness'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'Density'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 'Salinity'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 'Soil moisture content'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 'Best lifted index (to 500 hPa)'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 'Main thermocline anomaly'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 'Main thermocline depth'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 'Transient thermocline depth'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'Mixed layer depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'Convective precipitation (water)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 'Thunderstorm probability'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 'Precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 'Saturation deficit'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 'Precipitable water'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 'V-component of current '

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'U-component of current '

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 'Vertical v-component shear'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 'Vertical u-component shear'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 'Absolute divergence'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'Absolute vorticity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 'Sigma coordinate vertical velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'Montgomery stream Function'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'Wave spectra (3)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'Wave spectra (2)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'Wave spectra (1)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 'Geopotential height anomaly'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 'Pressure anomaly'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 'Temperature anomaly'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 'Parcel lifted index (to 500 hPa)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return 'Radar spectra (3)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return 'Radar spectra (2)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6:
            return 'Radar spectra (1)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'Visibility'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 'Lapse rate'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'Dew point temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'Minimum temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'Maximum temperature'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'Standard deviation of height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'Geometrical height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'ICAO Standard Atmosphere reference height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2:
            return 'Pressure tendency'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return 'Albedo'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 'Seconds prior to initial reference time (defined in Section 1)'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'Deviation of sea level from mean'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 'Ice temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'Geometric vertical velocity'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'Current speed'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'Current direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 'Secondary wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 'Primary wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'Primary wave direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 'Direction of wind waves'

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
            return 'Number of pixels used'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 'Estimated v component of wind'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 'Estimated u component of wind '

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 'Cloud top height quality indicator'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 'Cloud top height'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 'Instantaneous rain rate'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 'Estimated precipitation'

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

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 9:
            return 'Soil porosity'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 8:
            return 'Direct evaporation cease (soil moisture)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 7:
            return 'Transpiration stress-onset (soil moisture)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 'Number of soil layers in root zone'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 5:
            return 'Liquid volumetric soil moisture (non-frozen)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 4:
            return 'Bottom layer soil temperature'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 3:
            return 'Lower layer soil moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 2:
            return 'Upper layer soil moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 1:
            return 'Upper layer soil temperature'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 'Volumetric wilting point'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 'Volumetric soil moisture'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 'Heat flux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 'Column-integrated soil water'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 'Humidity parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 'Soil moisture parameter in canopy conductance'

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

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 10:
            return 'Ground heat flux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 'Volumetric soil moisture content'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 'Land use'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'Model terrain height'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 'Evapotranspiration'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5:
            return 'Water runoff'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return 'Vegetation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'Land cover (1=land, 0=sea)'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return 'Probability of 0.01 inch of precipitation (POP)'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return 'Percent precipitation in a sub-period of an overall period (Encoded as per cent accumulation over th'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 'Conditional percent precipitation amount fractile for an overall period (Encoded as an accumulation)'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 'Storm surface runoff'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 'Baseflow-groundwater runoff'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return 'Snow water equivalent percent of normal'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return 'Elevation of snow covered terrain'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return 'Remotely sensed snow cover'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 'Flash flood runoff (Encoded as an accumulation over a floating subinterval of time)'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 'Flash flood guidance (Encoded as an accumulation over a floating subinterval of time between the ref'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 'Seconds prior to initial reference time (defined in Section 1)'

        if discipline == 0 and parameterCategory == 190 and parameterNumber == 0:
            return 'Arbitrary text string'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return 'Supercooled large droplet probability (see Note 4)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return 'Relative clear air turbulence (RCAT)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return 'In-cloud turbulence'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return 'Icing'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return 'Snow free albedo'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 17:
            return 'Maximum snow albedo'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 'Contrail base'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 'Contrail top'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 'Contrail engine type'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 'Contrail intensity'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 'Planetary boundary layer regime'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'Turbulent kinetic energy'

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

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 'Volcanic ash'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 8:
            return 'Time-integrated air concentration of radioactive pollutant'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 7:
            return 'Time-integrated air concentration of iodine pollutant'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 6:
            return 'Time-integrated air concentration of caesium pollutant'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 5:
            return 'Ground deposition of radioactive pollutant'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 4:
            return 'Ground deposition of Iodine 131'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 3:
            return 'Ground deposition of Caesium 137'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 2:
            return 'Air concentration of radioactive pollutant'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 1:
            return 'Air concentration of Iodine 131'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 0:
            return 'Air concentration of Caesium 137'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5:
            return 'Precipitation'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 'Layer-maximum base reflectivity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 'Vertically-integrated liquid'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 'Base radial velocity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 'Base reflectivity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 'Base spectrum width'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 'Total column integrated ozone'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0:
            return 'Total ozone'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'Aerosol type'

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

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return 'Horizontal extent of cumulonimbus (CB)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24:
            return 'Sunshine'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 'Cloud ice mixing ratio'

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

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 'Cloud water'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 'Cloud Ice'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 'Net long-wave radiation flux, clear sky'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5:
            return 'Net long wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'Upward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'Downward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'Net long wave radiation flux (top of atmosphere)'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'Net long wave radiation flux (surface)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 'UV index '

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

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'Net short-wave radiation flux (top of atmosphere)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'Standard deviation of sub-grid scale orography'

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

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 'Geometric height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'Frictional velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 'Drag coefficient'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 'V-component storm motion'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 'U-component storm motion'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 'Horizontal momentum flux'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 'Vertical speed shear'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'v-component of wind (gust)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 'u-component of wind (gust)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 'Wind speed (gust)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'Maximum wind speed'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18:
            return 'Momentum flux, v component'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17:
            return 'Momentum flux, u component'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'Water equivalent of accumulated snow depth (deprecated)'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'Total snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'Total precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'Total column water (Vertically integrated total water (vapour + cloud water/ice))'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'Total snow precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'Total water precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 48:
            return 'Convective water precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 47:
            return 'Large scale water precipitation (non-convective)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'Total column integrated snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'Total column integrated rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'Rime factor'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'Rain fraction of total cloud water'

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
            return 'Graupel (snow pellets)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 'Hail'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 'Precipitable water category'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 29:
            return 'Total snowfall'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 28:
            return 'Maximum absolute humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 27:
            return 'Maximum relative humidity'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 'Large scale snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 'Convective snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 'Snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 'Large scale precipitation (non-convective)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'Vapor pressure'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'Snow phase change heat flux'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 14:
            return 'Minimum dew point depression'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'Wind chill factor'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'Heat index'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11:
            return 'Sensible heat net flux'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10:
            return 'Latent heat net flux'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'Skin temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return '10 metre wind speed'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'Brightness temperature'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Sunshine duration'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'Top net thermal radiation'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Surface net thermal radiation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Surface net solar radiation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'Surface roughness'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Land-sea mask'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2 metre dewpoint temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2 metre temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103:
            return '10 metre V wind component'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfFirstFixedSurface == 103:
            return '10 metre U wind component'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'Relative humidity'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'Geopotential Height'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 'Divergence'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 101:
            return 'Mean sea level pressure'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Surface latent heat flux'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Surface sensible heat flux'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'Boundary layer dissipation'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 'Vorticity (relative)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'Total column water'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'Vertical velocity'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Surface pressure'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'Specific humidity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'V component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'U component of wind'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'Temperature'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'Geopotential'

        is_uerra = h.get_l('is_uerra')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')
        lengthOfTimeRange = h.get_l('lengthOfTimeRange')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'Minimum temperature at 2 metres in the last 6 hours'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'Maximum temperature at 2 metres in the last 6 hours'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'Potential vorticity'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Convective available potential energy'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pressure'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'Potential temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'Velocity potential'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'Stream function'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 20 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and productDefinitionTemplateNumber == 9:
            return 'Total precipitation of at least 20 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 10 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and scaleFactorOfLowerLimit == 0:
            return 'Total precipitation of at least 10 mm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return '100 metre V wind component'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return '100 metre U wind component'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'Sea-ice thickness'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 34:
            return 'Surface runoff'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 21 and typeOfSecondFixedSurface == 160 and typeOfFirstFixedSurface == 160 and scaledValueOfSecondFixedSurface == 300 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 0:
            return 'Average salinity in the upper 300m'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 29315 and scaleFactorOfFirstFixedSurface == 2:
            return 'Depth of 20C isotherm'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'Sea surface height'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3 and typeOfFirstFixedSurface == 160:
            return 'Northward sea water velocity'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 160:
            return 'Eastward sea water velocity'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 'Mean wave period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 'Peak wave period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'Mean wave direction'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 'Significant height of combined wind waves and swell'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 'Mean zero-crossing wave period'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'Wind direction'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'Pseudo-adiabatic potential temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'Virtual potential temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'Virtual temperature'

        if discipline == 20 and parameterCategory == 2 and parameterNumber == 0:
            return 'Population density'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 9:
            return 'Fraction of malarial vector reproductive habitat'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 8:
            return 'Anopheles vector density'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 7:
            return 'Anopheles vector to host ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 6:
            return 'Detectable falciparum parasite ratio (after day 10)'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 5:
            return 'Falciparum parasite ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 4:
            return 'Malaria immunity ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 3:
            return 'Human bite rate by anopheles vectors'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 2:
            return 'Plasmodium falciparum entomological inoculation rate'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 1:
            return 'Malaria circumsporozoite protein ratio'

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 0:
            return 'Fraction of Malaria cases'

        if discipline == 20 and parameterCategory == 0 and parameterNumber == 1:
            return 'Mean radiant temperature'

        if discipline == 20 and parameterCategory == 0 and parameterNumber == 0:
            return 'Universal thermal climate index'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 23:
            return 'Angstrom coefficient'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 22:
            return 'Aerosol optical thickness at 1.640 um'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 21:
            return 'Aerosol optical thickness at 0.810 um'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 20:
            return 'Aerosol optical thickness at 0.635 um'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 19:
            return 'Wind speed'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17:
            return 'Clear-sky radiance (with respect to wave number)'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16:
            return 'Cloudy radiance (with respect to wave number)'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 11:
            return 'Fire daily severity rating'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 10:
            return 'Fire buildup index'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 9:
            return 'Initial fire spread index'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 8:
            return 'Drought code'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 7:
            return 'Duff moisture code'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 6:
            return 'Fine fuel moisture code'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 5:
            return 'Forest fire weather index'

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

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15:
            return 'Clear-sky brightness temperature'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14:
            return 'Cloudy brightness temperature'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 16 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 177:
            return 'Percolation'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 8 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Accumulated surface downward long-wave radiation flux, clear sky'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 53 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Accumulated surface upward short-wave radiation flux, clear sky'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Accumulated surface downward short-wave radiation flux, clear sky'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 27:
            return 'Soil depth'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 16:
            return 'Percolation rate'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 26:
            return 'Soil heat flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 8:
            return 'Downward long-wave radiation flux, clear sky'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 53:
            return 'Upward short-wave radiation flux, clear sky'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 52:
            return 'Downward short-wave radiation flux, clear sky'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18:
            return 'Soil temperature'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 28:
            return 'Mountain wave turbulence (eddy dissipation rate)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 29:
            return 'Clear air turbulence (CAT)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 121:
            return 'Fraction of snow cover'

        is_efas = h.get_l('is_efas')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and is_efas == 1 and lengthOfTimeRange == 24:
            return 'Total precipitation in the last 24 hours'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and is_efas == 1 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Total precipitation in the last 6 hours'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and is_uerra == 0 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 24:
            return 'Evaporation in the last 24 hours'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 6 and is_uerra == 0:
            return 'Evaporation in the last 6 hours'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 13 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Time-integrated surface direct short wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 14:
            return 'Diffuse short wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 13:
            return 'Direct short wave radiation flux'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return '10 metre wind direction'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Evaporation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79:
            return 'Evaporation rate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return 'Cloud cover'

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 2:
            return 'Haines Index'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 21:
            return 'Apparent temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return '2 metre relative humidity'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 9:
            return 'Groundwater lower storage'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 8:
            return 'Groundwater upper storage'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 25:
            return 'Snow depth at elevation bands'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7 and lengthOfTimeRange == 24 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Mean discharge in the last 24 hours'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7 and lengthOfTimeRange == 6 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0:
            return 'Mean discharge in the last 6 hours'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 15:
            return 'Upstream accumulated snow melt'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 14:
            return 'Upstream accumulated precipitation'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 13:
            return 'Depth of water on soil surface'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 24:
            return 'Frost index'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 3:
            return 'Days since last observation'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 2:
            return 'Water fraction'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 12:
            return 'Floodplain storage of water'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 11:
            return 'River storage of water'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7:
            return 'Discharge from rivers or streams'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 10:
            return 'Side flow into river channel'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 13:
            return 'Cross sectional area of flow in channel'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20 and typeOfStatisticalProcessing == 0:
            return 'Mean turbulent diffusion coefficient for heat'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 0:
            return 'Mean total precipitation flux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 30 and typeOfStatisticalProcessing == 0:
            return 'Mean downdraught detrainment rate'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 29 and typeOfStatisticalProcessing == 0:
            return 'Mean updraught detrainment rate'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 28 and typeOfStatisticalProcessing == 0:
            return 'Mean downdraught mass flux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 27 and typeOfStatisticalProcessing == 0:
            return 'Mean updraught mass flux'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 40 and typeOfStatisticalProcessing == 0:
            return 'Mean northward wind tendency due to parametrisations'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 39 and typeOfStatisticalProcessing == 0:
            return 'Mean eastward wind tendency due to parametrisations'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 108 and typeOfStatisticalProcessing == 0:
            return 'Mean specific humidity tendency due to parametrisations'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 26 and typeOfStatisticalProcessing == 0:
            return 'Mean temperature tendency due to parametrisations'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 25 and typeOfStatisticalProcessing == 0:
            return 'Mean temperature tendency due to long-wave radiation, clear sky'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 24 and typeOfStatisticalProcessing == 0:
            return 'Mean temperature tendency due to short-wave radiation, clear sky'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 23 and typeOfStatisticalProcessing == 0:
            return 'Mean temperature tendency due to long-wave radiation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 22 and typeOfStatisticalProcessing == 0:
            return 'Mean temperature tendency due to short-wave radiation'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return '100 metre wind speed'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 200:
            return '200 metre wind speed'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 200 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return '200 metre V wind component'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 200 and scaleFactorOfFirstFixedSurface == 0:
            return '200 metre U wind component'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 33:
            return 'Water runoff and drainage'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Convective precipitation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaledValueOfSecondFixedSurface == 10 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1:
            return 'Soil temperature top 100 cm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfSecondFixedSurface == 2:
            return 'Soil temperature top 20 cm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfSecondFixedSurface == 10 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'Soil moisture top 100 cm'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfSecondFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'Soil moisture top 20 cm'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6 and typeOfFirstFixedSurface == 1:
            return 'Averaged cloud-to-ground lightning flash density in the last 6 hours'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 3 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0:
            return 'Averaged cloud-to-ground lightning flash density in the last 3 hours'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 6 and typeOfSecondFixedSurface == 8:
            return 'Averaged total lightning flash density in the last 6 hours'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 3:
            return 'Averaged total lightning flash density in the last 3 hours'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 120:
            return 'Unbalanced component of specific cloud ice water content'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 119:
            return 'Unbalanced component of specific cloud liquid water content'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 118:
            return 'Unbalanced component of specific humidity'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and lengthOfTimeRange == 1 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8:
            return 'Averaged cloud-to-ground lightning flash density in the last hour'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Instantaneous cloud-to-ground lightning flash density'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 1:
            return 'Averaged total lightning flash density in the last hour'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Instantaneous total lightning flash density'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27:
            return 'Height of convective cloud top'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 93 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return '2 metre relative humidity with respect to water'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 19 and lengthOfTimeRange == 6 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfSecondFixedSurface == 8:
            return 'Maximum CAPES in the last 6 hours'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1:
            return 'Maximum CAPE in the last 6 hours'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 37:
            return 'Fraction of convective precipitation cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 36:
            return 'Fraction of stratiform precipitation cover'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 19:
            return 'Snow albedo'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 94:
            return 'Relative humidity with respect to ice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 93:
            return 'Relative humidity with respect to water'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and is_uerra == 0 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 2 and lengthOfTimeRange == 3:
            return '10 metre wind gust in the last 3 hours'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20 and scaledValueOfFirstFixedSurface == 27315 and scaleFactorOfFirstFixedSurface == 2:
            return '0 degrees C isothermal level (atm)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20 and scaledValueOfFirstFixedSurface == 26315 and scaleFactorOfFirstFixedSurface == 2:
            return '-10 degrees C isothermal level (atm)'

        aerosolType = h.get_l('aerosolType')
        is_aerosol = h.get_l('is_aerosol')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and aerosolType == 62003 and is_aerosol == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'Vertically integrated mass of ammonium aerosol'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and aerosolType == 62003 and is_aerosol == 1:
            return 'Wet deposition of ammonium aerosol by convective precipitation'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and is_aerosol == 1 and aerosolType == 62003:
            return 'Wet deposition of ammonium aerosol by large-scale precipitation'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 62003 and is_aerosol == 1:
            return 'Sedimentation of ammonium aerosol'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 62003 and is_aerosol == 1:
            return 'Dry deposition of ammonium aerosol'

        scaledValueOfFirstWavelength = h.get_l('scaledValueOfFirstWavelength')
        typeOfWavelengthInterval = h.get_l('typeOfWavelengthInterval')
        scaleFactorOfFirstWavelength = h.get_l('scaleFactorOfFirstWavelength')
        is_aerosol_optical = h.get_l('is_aerosol_optical')
        typeOfSizeInterval = h.get_l('typeOfSizeInterval')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and scaledValueOfFirstWavelength == 55 and typeOfWavelengthInterval == 11 and aerosolType == 62003 and scaleFactorOfFirstWavelength == 8 and is_aerosol_optical == 1 and typeOfSizeInterval == 255:
            return 'Ammonium aerosol optical depth at 550 nm'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfWavelengthInterval == 11 and aerosolType == 62004 and typeOfSizeInterval == 255 and scaleFactorOfFirstWavelength == 8 and is_aerosol_optical == 1 and scaledValueOfFirstWavelength == 55:
            return 'Nitrate aerosol optical depth at 550 nm'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and is_aerosol == 1 and aerosolType == 62003:
            return 'Ammonium aerosol mass mixing ratio'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and scaledValueOfFirstFixedSurface == 1 and typeOfFirstFixedSurface == 169 and typeOfSecondFixedSurface == 255 and scaleFactorOfFirstFixedSurface == 2:
            return 'Ocean mixed layer thickness defined by sigma theta 0.01 kg/m3'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 3 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'Sea surface practical salinity'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 15 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 'Mean sea water temperature in the upper 300 m'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 18 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 'Mean sea water potential temperature in the upper 300 m'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == -2 and productDefinitionTemplateNumber == 9 and probabilityType == 0 and typeOfStatisticalProcessing == 10:
            return 'Probability of temperature standardized anomaly less than -2 standard deviation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 10 and scaleFactorOfLowerLimit == 1 and scaledValueOfLowerLimit == -15 and productDefinitionTemplateNumber == 9 and probabilityType == 0:
            return 'Probability of temperature standardized anomaly less than -1.5 standard deviation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and probabilityType == 0 and typeOfStatisticalProcessing == 10 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == -1 and productDefinitionTemplateNumber == 9:
            return 'Probability of temperature standardized anomaly less than -1 standard deviation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 10 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 2:
            return 'Probability of temperature standardized anomaly greater than 2 standard deviation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfLowerLimit == 1 and scaledValueOfLowerLimit == 15 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 10:
            return 'Probability of temperature standardized anomaly greater than 1.5 standard deviation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfLowerLimit == 1 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 10 and scaleFactorOfLowerLimit == 0:
            return 'Probability of temperature standardized anomaly greater than 1 standard deviation'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and probabilityType == 3 and typeOfStatisticalProcessing == 2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 10 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 103:
            return '10 metre wind gust of at least 10 m/s'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 50 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'Total precipitation of at least 50 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 25 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1:
            return 'Total precipitation of at least 25 mm'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 'High cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 'Medium cloud cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 'Low cloud cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'Snow depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'large scale precipitation'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 32:
            return 'Fraction of cloud cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 84:
            return 'Specific cloud ice water content'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 83:
            return 'Specific cloud liquid water content'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Surface net thermal radiation, clear sky'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Surface net solar radiation, clear sky'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'Ozone mass mixing ratio'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and is_uerra == 1:
            return 'Minimum temperature at 2 metres since previous post-processing'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 1 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103:
            return 'Maximum temperature at 2 metres since previous post-processing'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 37:
            return 'Northward turbulent surface stress'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 38:
            return 'Eastward turbulent surface stress'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Surface thermal radiation downwards'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'Surface solar radiation downwards'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 32:
            return 'Eta-coordinate vertical velocity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 'Specific snow water content'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 'Specific rain water content'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfFirstFixedSurface == 103 and is_uerra == 1 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2:
            return '10 metre wind gust since previous post-processing'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0:
            return 'Soil type'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Sea surface temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 'Snow density'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'Sea ice area fraction'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 45:
            return 'Unbalanced component of divergence'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 31:
            return 'Unbalanced component of logarithm of surface pressure'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 28:
            return 'Unbalanced component of temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 200 and scaleFactorOfFirstFixedSurface == 0:
            return 'Wind speed'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and is_uerra == 1:
            return 'Wind speed'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'Wind speed'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and probabilityType == 3 and scaledValueOfLowerLimit == 3 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == -2:
            return 'Total precipitation of at least 300 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 200 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'Total precipitation of at least 200 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 150 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and scaleFactorOfLowerLimit == 0:
            return 'Total precipitation of at least 150 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 100 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1:
            return 'Total precipitation of at least 100 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 80 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Total precipitation of at least 80 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and scaledValueOfLowerLimit == 60 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 1:
            return 'Total precipitation of at least 60 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 40 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'Total precipitation of at least 40 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 5 and productDefinitionTemplateNumber == 9:
            return 'Total precipitation of at least 5 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 1:
            return 'Total precipitation of at least 1 mm'

    return wrapped
