import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 202 and indicatorOfParameter == 39:
            return 'Skin conductivity (ratio ground heat flux to temperature difference soil-skin layer)'

        if table2Version == 202 and indicatorOfParameter == 37:
            return 'Echotop-height: largest height where radar reflectivity above a threshold is present'

        if table2Version == 202 and indicatorOfParameter == 36:
            return 'Echotop-pressure: smallest pressure where radar reflectivity above a threshold is present'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 'relative vorticity'

        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200 and timeRangeIndicator == 2:
            return 'Maximum reflectivity track (over given time interval and entire atmosphere)'

        if table2Version == 201 and indicatorOfParameter == 196 and timeRangeIndicator == 2:
            return 'Maximum of Lightning Potential Index (over given time interval)'

        if table2Version == 201 and indicatorOfParameter == 234:
            return 'Composite reflectivity - forecast (simulation)'

        if table2Version == 201 and indicatorOfParameter == 235:
            return 'Composite reflectivity - observation'

        if table2Version == 201 and indicatorOfParameter == 48 and indicatorOfTypeOfLevel == 200 and timeRangeIndicator == 2:
            return 'Maximum total-column integrated condensed  water (over given time interval)'

        if table2Version == 201 and indicatorOfParameter == 49 and timeRangeIndicator == 2:
            return 'Maximum total-column integrated condensed water above -10 C isotherm (over given time interval)'

        if table2Version == 203 and indicatorOfParameter == 37 and timeRangeIndicator == 2:
            return 'Maximum updraft track (over given time interval and column)'

        if table2Version == 203 and indicatorOfParameter == 36 and timeRangeIndicator == 2:
            return 'Maximum rotation amplitude (positive or negative)  (over given time interval and column)'

        if table2Version == 203 and indicatorOfParameter == 35 and timeRangeIndicator == 2:
            return 'Maximum amplitude (positive or negative) of updraft helicity  (over given time interval)'

        if table2Version == 201 and indicatorOfParameter == 196:
            return 'Lightning Potential Index'

        if table2Version == 202 and indicatorOfParameter == 34:
            return 'Antropogenic heat flux (e.g. urban heating, traffic)'

        if table2Version == 202 and indicatorOfParameter == 33:
            return 'Impervious (paved or sealed) surface fraction'

        if table2Version == 201 and indicatorOfParameter == 196:
            return 'Lightning Potential Index'

        if table2Version == 3 and indicatorOfParameter == 149:
            return 'wind_gust_10m'

        if table2Version == 3 and indicatorOfParameter == 148:
            return 'orography'

        if table2Version == 201 and indicatorOfParameter == 25 and timeRangeIndicator == 4:
            return 'Downward long-wave radiation flux accum'

        if table2Version == 201 and indicatorOfParameter == 25 and timeRangeIndicator == 3:
            return 'Downward long-wave radiation flux avg'

        if table2Version == 201 and indicatorOfParameter == 25:
            return 'Downward long-wave radiation flux'

        if table2Version == 3 and indicatorOfParameter == 162:
            return 'freezing_level_ICAO_height'

        if table2Version == 3 and indicatorOfParameter == 152:
            return 'wet_bulb_freezing_level_ht'

        if table2Version == 3 and indicatorOfParameter == 151:
            return 'Lowest_cloud_base_height'

        if table2Version == 3 and indicatorOfParameter == 207:
            return 'cloud_fraction_below_1000ft'

        if table2Version == 3 and indicatorOfParameter == 140:
            return 'accumulated_convective_rain'

        if table2Version == 3 and indicatorOfParameter == 138:
            return 'Fog_fraction'

        if table2Version == 3 and indicatorOfParameter == 40:
            return 'Vertical Velocity (Geometric) (w)'

        if table2Version == 202 and indicatorOfParameter == 120:
            return 'Friction Velocity'

        if table2Version == 250 and indicatorOfParameter == 20:
            return 'relative humidity over mixed phase'

        if table2Version == 202 and indicatorOfParameter == 233 and timeRangeIndicator == 3:
            return 'Gravity wave dissipation '

        if table2Version == 204 and indicatorOfParameter == 46:
            return 'snow rate, qualified,BRD'

        if table2Version == 203 and indicatorOfParameter == 77:
            return 'snow rate,BRD'

        if table2Version == 203 and indicatorOfParameter == 76:
            return 'hail flag,BRD'

        if table2Version == 203 and indicatorOfParameter == 75:
            return 'precipitation phase,BRD'

        if table2Version == 203 and indicatorOfParameter == 73:
            return 'precipitation,BRD'

        if table2Version == 203 and indicatorOfParameter == 72:
            return 'precipitation, qualified,BRD'

        if table2Version == 202 and indicatorOfParameter == 232 and timeRangeIndicator == 1:
            return 'v-momentum flux due to SSO-effects (initialisation)'

        if table2Version == 202 and indicatorOfParameter == 231 and timeRangeIndicator == 1:
            return 'u-momentum flux due to SSO-effects (initialisation)'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1:
            return 'Momentum Flux, V-Component (m)'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1:
            return 'Momentum Flux, U-Component (m)'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1:
            return 'Upward diffusive short wave radiation flux at surface ( mean over forecast time)'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1:
            return 'Downward diffusive short wave radiation flux at surface ( mean over forecast time)'

        if table2Version == 201 and indicatorOfParameter == 151:
            return 'Eddy dissipitation rate of TKE'

        if table2Version == 203 and indicatorOfParameter == 71:
            return 'Precipitation'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 3 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 2 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 2 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'Total Precipitation (Accumulation)'

        if table2Version == 1 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'Snow depth water equivalent'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'Snow Depth water equivalent'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'Soil Temperature'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'Column-integrated Soil Moisture'

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'Geopotential height'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'Momentum Flux, V-Component (m)'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'Momentum Flux, U-Component (m)'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'Short wave radiation flux'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'Long wave radiation flux'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'Net long-wave radiation flux(atmosph.top)'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'Net short wave radiation flux'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'Net long wave radiation flux (m) (at the surface)'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'Net short wave radiation flux (at the surface)'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 'Secondary wave period'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 1 and indicatorOfParameter == 106:
            return 'Swell Mean Period'

        if table2Version == 1 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 1 and indicatorOfParameter == 104:
            return 'Mean direction of total swell'

        if table2Version == 1 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 1 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 1 and indicatorOfParameter == 101:
            return 'Direction of wind waves'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'Significant height of combined wind waves and swell'

        if table2Version == 1 and indicatorOfParameter == 97:
            return 'Ice growth rate'

        if table2Version == 1 and indicatorOfParameter == 96:
            return 'V-component of ice drift'

        if table2Version == 1 and indicatorOfParameter == 95:
            return 'U-component of ice drift'

        if table2Version == 1 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 1 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 1 and indicatorOfParameter == 92:
            return 'sea Ice Thickness'

        if table2Version == 1 and indicatorOfParameter == 91:
            return 'Sea Ice Cover ( 0= free, 1=cover)'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 'salinity'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'Column-integrated Soil Moisture'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'Deviation of sea-elbel from mean'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'Main thermocline depth'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'Transient thermocline depth'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'Snow fall rate water equivalent'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'Convective precipitation (water)'

        if table2Version == 1 and indicatorOfParameter == 60:
            return 'Thunderstorm probability'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'Saturation deficit'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'Vapour pressure'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'Precipitable water'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 1 and indicatorOfParameter == 50:
            return 'V-component of current'

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'U-component of current'

        if table2Version == 1 and indicatorOfParameter == 48:
            return 'Speed of current'

        if table2Version == 1 and indicatorOfParameter == 47:
            return 'Direction of current'

        if table2Version == 1 and indicatorOfParameter == 46:
            return 'Vertical v-component shear'

        if table2Version == 1 and indicatorOfParameter == 45:
            return 'Vertical u-component shear'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 'Absolute Vorticity'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'Montgomery stream Function'

        if table2Version == 1 and indicatorOfParameter == 31:
            return 'Wind Direction (DD)'

        if table2Version == 1 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 1 and indicatorOfParameter == 29:
            return 'Wave spectra (2)'

        if table2Version == 1 and indicatorOfParameter == 28:
            return 'Wave spectra (1)'

        if table2Version == 1 and indicatorOfParameter == 27:
            return 'Geopotential height anomaly'

        if table2Version == 1 and indicatorOfParameter == 26:
            return 'Pressure anomaly'

        if table2Version == 1 and indicatorOfParameter == 25:
            return 'Temperature anomaly'

        if table2Version == 1 and indicatorOfParameter == 24:
            return 'Parcel lifted index (to 500 hPa)'

        if table2Version == 1 and indicatorOfParameter == 23:
            return 'Radar spectra (3)'

        if table2Version == 1 and indicatorOfParameter == 22:
            return 'Radar spectra (2)'

        if table2Version == 1 and indicatorOfParameter == 21:
            return 'Radar spectra (1)'

        if table2Version == 1 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 1 and indicatorOfParameter == 19:
            return 'Lapse rate'

        if table2Version == 1 and indicatorOfParameter == 18:
            return 'Dew point depression(or deficit)'

        if table2Version == 1 and indicatorOfParameter == 17:
            return 'Dew Point Temperature'

        if table2Version == 1 and indicatorOfParameter == 16:
            return 'Min Temperature'

        if table2Version == 1 and indicatorOfParameter == 15:
            return 'Max Temperature '

        if table2Version == 1 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential Temperature'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'Standard devation of height'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'Geometric Height'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'Pressure Tendency '

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'Total Column-Integrated Cloud Water'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'Large-Scale Precipitation '

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'Large-Scale snowfall - water equivalent (Accumulation)'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'Convective Snowfall water equivalent (s)'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'Total Column Integrated Ozone'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'Water Runoff '

        if table2Version == 1 and indicatorOfParameter == 87:
            return 'Plant cover'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'Brightness Temperature'

        if table2Version == 1 and indicatorOfParameter == 75:
            return 'Cloud Cover (0 - 400 hPa)'

        if table2Version == 1 and indicatorOfParameter == 74:
            return 'Cloud Cover (400 - 800 hPa)'

        if table2Version == 1 and indicatorOfParameter == 73:
            return 'Cloud Cover (800 hPa - Soil)'

        if table2Version == 1 and indicatorOfParameter == 72:
            return 'Convective Cloud Cover'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'Evaporation (s)'

        if table2Version == 1 and indicatorOfParameter == 84:
            return 'Albedo (in short-wave, average)'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'Surface Roughness length Surface Roughness'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'Land Cover (1=land, 0=sea)'

        if table2Version == 1 and indicatorOfParameter == 44:
            return 'Relative Divergenz'

        level = h.get_l('level')

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2m Temperature'

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'V-Component of Wind'

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'U-Component of Wind'

        if table2Version == 1 and indicatorOfParameter == 52:
            return 'Relative Humidity'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'Geopotential height'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'Pressure Reduced to MSL'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'Latent Heat Net Flux (m)'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'Sensible Heat Net Flux (m)'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'Boundary Layer Dissipitation'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 'vertical vorticity'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'Vertical Velocity (Pressure) ( omega=dp/dt )'

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pressure (S) (not reduced)'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'Specific Humidity'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'V-Component of Wind'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'U-Component of Wind'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Min 2m Temperature'

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Max 2m Temperature '

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'Wind speed (SP)'

        if table2Version == 3 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 2 and indicatorOfParameter == 85:
            return 'Soil Temperature'

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'Geopotential height'

        if table2Version == 2 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 2 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 2 and indicatorOfParameter == 125:
            return 'Momentum Flux, V-Component (m)'

        if table2Version == 2 and indicatorOfParameter == 124:
            return 'Momentum Flux, U-Component (m)'

        if table2Version == 2 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 2 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 2 and indicatorOfParameter == 116:
            return 'Short wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 115:
            return 'Long wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 114:
            return 'Net long-wave radiation flux(atmosph.top)'

        if table2Version == 2 and indicatorOfParameter == 113:
            return 'Net short wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 112:
            return 'Net long wave radiation flux (m) (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 111:
            return 'Net short wave radiation flux (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 110:
            return 'Secondary wave period'

        if table2Version == 2 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 2 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 2 and indicatorOfParameter == 97:
            return 'Ice growth rate'

        if table2Version == 2 and indicatorOfParameter == 96:
            return 'V-component of ice drift'

        if table2Version == 2 and indicatorOfParameter == 95:
            return 'U-component of ice drift'

        if table2Version == 2 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 2 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'Column-integrated Soil Moisture'

        if table2Version == 2 and indicatorOfParameter == 82:
            return 'Deviation of sea-elbel from mean'

        if table2Version == 2 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 2 and indicatorOfParameter == 70:
            return 'Main thermocline depth'

        if table2Version == 2 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 2 and indicatorOfParameter == 68:
            return 'Transient thermocline depth'

        if table2Version == 2 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 2 and indicatorOfParameter == 64:
            return 'Snow fall rate water equivalent'

        if table2Version == 2 and indicatorOfParameter == 63:
            return 'Convective precipitation (water)'

        if table2Version == 2 and indicatorOfParameter == 60:
            return 'Thunderstorm probability'

        if table2Version == 2 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 2 and indicatorOfParameter == 56:
            return 'Saturation deficit'

        if table2Version == 2 and indicatorOfParameter == 55:
            return 'Vapour pressure'

        if table2Version == 2 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 2 and indicatorOfParameter == 50:
            return 'V-component of current'

        if table2Version == 2 and indicatorOfParameter == 49:
            return 'U-component of current'

        if table2Version == 2 and indicatorOfParameter == 48:
            return 'Speed of current'

        if table2Version == 2 and indicatorOfParameter == 47:
            return 'Direction of current'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 'Vertical v-component shear'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 'Vertical u-component shear'

        if table2Version == 2 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 2 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 3 and indicatorOfParameter == 37:
            return 'Montgomery stream Function'

        if table2Version == 2 and indicatorOfParameter == 37:
            return 'Montgomery stream Function'

        if table2Version == 2 and indicatorOfParameter == 27:
            return 'Geopotential height anomaly'

        if table2Version == 2 and indicatorOfParameter == 26:
            return 'Pressure anomaly'

        if table2Version == 2 and indicatorOfParameter == 25:
            return 'Temperature anomaly'

        if table2Version == 2 and indicatorOfParameter == 24:
            return 'Parcel lifted index (to 500 hPa)'

        if table2Version == 2 and indicatorOfParameter == 23:
            return 'Radar spectra (3)'

        if table2Version == 2 and indicatorOfParameter == 22:
            return 'Radar spectra (2)'

        if table2Version == 2 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 2 and indicatorOfParameter == 18:
            return 'Dew point depression(or deficit)'

        if table2Version == 2 and indicatorOfParameter == 17:
            return 'Dew Point Temperature'

        if table2Version == 2 and indicatorOfParameter == 16:
            return 'Min Temperature'

        if table2Version == 2 and indicatorOfParameter == 15:
            return 'Max Temperature '

        if table2Version == 3 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential Temperature'

        if table2Version == 2 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential Temperature'

        if table2Version == 3 and indicatorOfParameter == 9:
            return 'Standard devation of height'

        if table2Version == 2 and indicatorOfParameter == 9:
            return 'Standard devation of height'

        if table2Version == 2 and indicatorOfParameter == 8:
            return 'Geometric Height'

        if table2Version == 2 and indicatorOfParameter == 90:
            return 'Water Runoff '

        if table2Version == 2 and indicatorOfParameter == 118:
            return 'Brightness Temperature'

        if table2Version == 2 and indicatorOfParameter == 75:
            return 'Cloud Cover (0 - 400 hPa)'

        if table2Version == 2 and indicatorOfParameter == 74:
            return 'Cloud Cover (400 - 800 hPa)'

        if table2Version == 2 and indicatorOfParameter == 73:
            return 'Cloud Cover (800 hPa - Soil)'

        if table2Version == 2 and indicatorOfParameter == 57:
            return 'Evaporation (s)'

        if table2Version == 2 and indicatorOfParameter == 121:
            return 'Latent Heat Net Flux (m)'

        if table2Version == 2 and indicatorOfParameter == 122:
            return 'Sensible Heat Net Flux (m)'

        if table2Version == 2 and indicatorOfParameter == 123:
            return 'Boundary Layer Dissipitation'

        if table2Version == 3 and indicatorOfParameter == 61:
            return 'Total Precipitation (Accumulation)'

        if table2Version == 3 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 3 and indicatorOfParameter == 65:
            return 'Snow depth water equivalent'

        if table2Version == 3 and indicatorOfParameter == 66:
            return 'Snow Depth water equivalent'

        if table2Version == 3 and indicatorOfParameter == 85:
            return 'Soil Temperature'

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'Geopotential height'

        if table2Version == 3 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 3 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 3 and indicatorOfParameter == 125:
            return 'Momentum Flux, V-Component (m)'

        if table2Version == 3 and indicatorOfParameter == 124:
            return 'Momentum Flux, U-Component (m)'

        if table2Version == 3 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 3 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 3 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 3 and indicatorOfParameter == 116:
            return 'Short wave radiation flux'

        if table2Version == 3 and indicatorOfParameter == 115:
            return 'Long wave radiation flux'

        if table2Version == 3 and indicatorOfParameter == 114:
            return 'Net long-wave radiation flux(atmosph.top)'

        if table2Version == 3 and indicatorOfParameter == 113:
            return 'Net short wave radiation flux'

        if table2Version == 3 and indicatorOfParameter == 112:
            return 'Net long wave radiation flux (m) (at the surface)'

        if table2Version == 3 and indicatorOfParameter == 111:
            return 'Net short wave radiation flux (at the surface)'

        if table2Version == 3 and indicatorOfParameter == 110:
            return 'Secondary wave period'

        if table2Version == 3 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 3 and indicatorOfParameter == 106:
            return 'Swell Mean Period'

        if table2Version == 3 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 3 and indicatorOfParameter == 104:
            return 'Mean direction of total swell'

        if table2Version == 3 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 3 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 3 and indicatorOfParameter == 101:
            return 'Direction of wind waves'

        if table2Version == 3 and indicatorOfParameter == 100:
            return 'Significant height of combined wind waves and swell'

        if table2Version == 3 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 3 and indicatorOfParameter == 97:
            return 'Ice growth rate'

        if table2Version == 3 and indicatorOfParameter == 96:
            return 'V-component of ice drift'

        if table2Version == 3 and indicatorOfParameter == 95:
            return 'U-component of ice drift'

        if table2Version == 3 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 3 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 3 and indicatorOfParameter == 92:
            return 'sea Ice Thickness'

        if table2Version == 3 and indicatorOfParameter == 91:
            return 'Sea Ice Cover ( 0= free, 1=cover)'

        if table2Version == 3 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 3 and indicatorOfParameter == 88:
            return 'salinity'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'Column-integrated Soil Moisture'

        if table2Version == 3 and indicatorOfParameter == 82:
            return 'Deviation of sea-elbel from mean'

        if table2Version == 3 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 3 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 3 and indicatorOfParameter == 70:
            return 'Main thermocline depth'

        if table2Version == 3 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 3 and indicatorOfParameter == 68:
            return 'Transient thermocline depth'

        if table2Version == 3 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 3 and indicatorOfParameter == 64:
            return 'Snow fall rate water equivalent'

        if table2Version == 3 and indicatorOfParameter == 63:
            return 'Convective precipitation (water)'

        if table2Version == 3 and indicatorOfParameter == 60:
            return 'Thunderstorm probability'

        if table2Version == 3 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 3 and indicatorOfParameter == 56:
            return 'Saturation deficit'

        if table2Version == 3 and indicatorOfParameter == 55:
            return 'Vapour pressure'

        if table2Version == 3 and indicatorOfParameter == 54:
            return 'Precipitable water'

        if table2Version == 3 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 3 and indicatorOfParameter == 50:
            return 'V-component of current'

        if table2Version == 3 and indicatorOfParameter == 49:
            return 'U-component of current'

        if table2Version == 3 and indicatorOfParameter == 48:
            return 'Speed of current'

        if table2Version == 3 and indicatorOfParameter == 47:
            return 'Direction of current'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 'Vertical v-component shear'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 'Vertical u-component shear'

        if table2Version == 3 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 3 and indicatorOfParameter == 41:
            return 'Absolute Vorticity'

        if table2Version == 3 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 3 and indicatorOfParameter == 31:
            return 'Wind Direction (DD)'

        if table2Version == 3 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 3 and indicatorOfParameter == 29:
            return 'Wave spectra (2)'

        if table2Version == 3 and indicatorOfParameter == 28:
            return 'Wave spectra (1)'

        if table2Version == 3 and indicatorOfParameter == 27:
            return 'Geopotential height anomaly'

        if table2Version == 3 and indicatorOfParameter == 26:
            return 'Pressure anomaly'

        if table2Version == 3 and indicatorOfParameter == 25:
            return 'Temperature anomaly'

        if table2Version == 3 and indicatorOfParameter == 24:
            return 'Parcel lifted index (to 500 hPa)'

        if table2Version == 3 and indicatorOfParameter == 23:
            return 'Radar spectra (3)'

        if table2Version == 3 and indicatorOfParameter == 22:
            return 'Radar spectra (2)'

        if table2Version == 3 and indicatorOfParameter == 21:
            return 'Radar spectra (1)'

        if table2Version == 3 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 3 and indicatorOfParameter == 19:
            return 'Lapse rate'

        if table2Version == 3 and indicatorOfParameter == 18:
            return 'Dew point depression(or deficit)'

        if table2Version == 3 and indicatorOfParameter == 17:
            return 'Dew Point Temperature'

        if table2Version == 3 and indicatorOfParameter == 16:
            return 'Min Temperature'

        if table2Version == 3 and indicatorOfParameter == 15:
            return 'Max Temperature '

        if table2Version == 3 and indicatorOfParameter == 8:
            return 'Geometric Height'

        if table2Version == 3 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 3 and indicatorOfParameter == 3:
            return 'Pressure Tendency '

        if table2Version == 3 and indicatorOfParameter == 123:
            return 'Boundary Layer Dissipitation'

        if table2Version == 3 and indicatorOfParameter == 118:
            return 'Brightness Temperature'

        if table2Version == 3 and indicatorOfParameter == 12:
            return 'Virtual Temperature'

        if table2Version == 2 and indicatorOfParameter == 12:
            return 'Virtual Temperature'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'Virtual Temperature'

        if table2Version == 3 and indicatorOfParameter == 76:
            return 'Total Column-Integrated Cloud Water'

        if table2Version == 3 and indicatorOfParameter == 62:
            return 'Large-Scale Precipitation '

        if table2Version == 3 and indicatorOfParameter == 79:
            return 'Large-Scale snowfall - water equivalent (Accumulation)'

        if table2Version == 3 and indicatorOfParameter == 78:
            return 'Convective Snowfall water equivalent (s)'

        if table2Version == 3 and indicatorOfParameter == 10:
            return 'Total Column Integrated Ozone'

        if table2Version == 3 and indicatorOfParameter == 90:
            return 'Water Runoff '

        if table2Version == 3 and indicatorOfParameter == 87:
            return 'Plant cover'

        if table2Version == 3 and indicatorOfParameter == 75:
            return 'Cloud Cover (0 - 400 hPa)'

        if table2Version == 3 and indicatorOfParameter == 74:
            return 'Cloud Cover (400 - 800 hPa)'

        if table2Version == 3 and indicatorOfParameter == 73:
            return 'Cloud Cover (800 hPa - Soil)'

        if table2Version == 3 and indicatorOfParameter == 72:
            return 'Convective Cloud Cover'

        if table2Version == 3 and indicatorOfParameter == 57:
            return 'Evaporation (s)'

        if table2Version == 3 and indicatorOfParameter == 84:
            return 'Albedo (in short-wave, average)'

        if table2Version == 3 and indicatorOfParameter == 83:
            return 'Surface Roughness length Surface Roughness'

        if table2Version == 3 and indicatorOfParameter == 81:
            return 'Land Cover (1=land, 0=sea)'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2m Temperature'

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'V-Component of Wind'

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'U-Component of Wind'

        if table2Version == 3 and indicatorOfParameter == 52:
            return 'Relative Humidity'

        if table2Version == 3 and indicatorOfParameter == 7:
            return 'Geopotential height'

        if table2Version == 3 and indicatorOfParameter == 44:
            return 'Relative Divergenz'

        if table2Version == 3 and indicatorOfParameter == 2:
            return 'Pressure Reduced to MSL'

        if table2Version == 3 and indicatorOfParameter == 121:
            return 'Latent Heat Net Flux (m)'

        if table2Version == 3 and indicatorOfParameter == 122:
            return 'Sensible Heat Net Flux (m)'

        if table2Version == 3 and indicatorOfParameter == 43:
            return 'vertical vorticity'

        if table2Version == 3 and indicatorOfParameter == 39:
            return 'Vertical Velocity (Pressure) ( omega=dp/dt )'

        if table2Version == 3 and indicatorOfParameter == 51:
            return 'Specific Humidity'

        if table2Version == 3 and indicatorOfParameter == 34:
            return 'V-Component of Wind'

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pressure (S) (not reduced)'

        if table2Version == 3 and indicatorOfParameter == 33:
            return 'U-Component of Wind'

        if table2Version == 3 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Min 2m Temperature'

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Max 2m Temperature '

        if table2Version == 3 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 3 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 3 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 3 and indicatorOfParameter == 32:
            return 'Wind speed (SP)'

        if table2Version == 3 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 3 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 'Temperature (G)'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1:
            return 'Downward direct short wave radiation flux at surface'

        if table2Version == 202 and indicatorOfParameter == 38:
            return 'Skin temperature'

        if table2Version == 2 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 2 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 2 and indicatorOfParameter == 88:
            return 'salinity'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 'Sensible Heat Net Flux - instant - at surface'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1:
            return 'Latent Heat Net Flux - instant - at surface'

        if table2Version == 202 and indicatorOfParameter == 129:
            return 'Albedo - diffusive solar (0.3 - 5.0 m-6)'

        if table2Version == 202 and indicatorOfParameter == 129 and timeRangeIndicator == 3:
            return 'Albedo - diffusive solar - time average (0.3 - 5.0 m-6) '

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 1:
            return 'Specific Humidity (S)'

        if table2Version == 254 and indicatorOfParameter == 254:
            return 'DUMMY_254'

        if table2Version == 254 and indicatorOfParameter == 253:
            return 'DUMMY_253'

        if table2Version == 254 and indicatorOfParameter == 252:
            return 'DUMMY_252'

        if table2Version == 254 and indicatorOfParameter == 251:
            return 'DUMMY_251'

        if table2Version == 254 and indicatorOfParameter == 250:
            return 'DUMMY_250'

        if table2Version == 254 and indicatorOfParameter == 249:
            return 'DUMMY_249'

        if table2Version == 254 and indicatorOfParameter == 248:
            return 'DUMMY_248'

        if table2Version == 254 and indicatorOfParameter == 247:
            return 'DUMMY_247'

        if table2Version == 254 and indicatorOfParameter == 246:
            return 'DUMMY_246'

        if table2Version == 254 and indicatorOfParameter == 245:
            return 'DUMMY_245'

        if table2Version == 254 and indicatorOfParameter == 244:
            return 'DUMMY_244'

        if table2Version == 254 and indicatorOfParameter == 243:
            return 'DUMMY_243'

        if table2Version == 254 and indicatorOfParameter == 242:
            return 'DUMMY_242'

        if table2Version == 254 and indicatorOfParameter == 241:
            return 'DUMMY_241'

        if table2Version == 254 and indicatorOfParameter == 240:
            return 'DUMMY_240'

        if table2Version == 254 and indicatorOfParameter == 239:
            return 'DUMMY_239'

        if table2Version == 254 and indicatorOfParameter == 238:
            return 'DUMMY_238'

        if table2Version == 254 and indicatorOfParameter == 237:
            return 'DUMMY_237'

        if table2Version == 254 and indicatorOfParameter == 236:
            return 'DUMMY_236'

        if table2Version == 254 and indicatorOfParameter == 235:
            return 'DUMMY_235'

        if table2Version == 254 and indicatorOfParameter == 234:
            return 'DUMMY_234'

        if table2Version == 254 and indicatorOfParameter == 233:
            return 'DUMMY_233'

        if table2Version == 254 and indicatorOfParameter == 232:
            return 'DUMMY_232'

        if table2Version == 254 and indicatorOfParameter == 231:
            return 'DUMMY_231'

        if table2Version == 254 and indicatorOfParameter == 230:
            return 'DUMMY_230'

        if table2Version == 254 and indicatorOfParameter == 229:
            return 'DUMMY_229'

        if table2Version == 254 and indicatorOfParameter == 228:
            return 'DUMMY_228'

        if table2Version == 254 and indicatorOfParameter == 227:
            return 'DUMMY_227'

        if table2Version == 254 and indicatorOfParameter == 226:
            return 'DUMMY_226'

        if table2Version == 254 and indicatorOfParameter == 225:
            return 'DUMMY_225'

        if table2Version == 254 and indicatorOfParameter == 224:
            return 'DUMMY_224'

        if table2Version == 254 and indicatorOfParameter == 223:
            return 'DUMMY_223'

        if table2Version == 254 and indicatorOfParameter == 222:
            return 'DUMMY_222'

        if table2Version == 254 and indicatorOfParameter == 221:
            return 'DUMMY_221'

        if table2Version == 254 and indicatorOfParameter == 220:
            return 'DUMMY_220'

        if table2Version == 254 and indicatorOfParameter == 219:
            return 'DUMMY_219'

        if table2Version == 254 and indicatorOfParameter == 218:
            return 'DUMMY_218'

        if table2Version == 254 and indicatorOfParameter == 217:
            return 'DUMMY_217'

        if table2Version == 254 and indicatorOfParameter == 216:
            return 'DUMMY_216'

        if table2Version == 254 and indicatorOfParameter == 215:
            return 'DUMMY_215'

        if table2Version == 254 and indicatorOfParameter == 214:
            return 'DUMMY_214'

        if table2Version == 254 and indicatorOfParameter == 213:
            return 'DUMMY_213'

        if table2Version == 254 and indicatorOfParameter == 212:
            return 'DUMMY_212'

        if table2Version == 254 and indicatorOfParameter == 211:
            return 'DUMMY_211'

        if table2Version == 254 and indicatorOfParameter == 210:
            return 'DUMMY_210'

        if table2Version == 254 and indicatorOfParameter == 209:
            return 'DUMMY_209'

        if table2Version == 254 and indicatorOfParameter == 208:
            return 'DUMMY_208'

        if table2Version == 254 and indicatorOfParameter == 207:
            return 'DUMMY_207'

        if table2Version == 254 and indicatorOfParameter == 206:
            return 'DUMMY_206'

        if table2Version == 254 and indicatorOfParameter == 205:
            return 'DUMMY_205'

        if table2Version == 254 and indicatorOfParameter == 204:
            return 'DUMMY_204'

        if table2Version == 254 and indicatorOfParameter == 203:
            return 'DUMMY_203'

        if table2Version == 254 and indicatorOfParameter == 202:
            return 'DUMMY_202'

        if table2Version == 254 and indicatorOfParameter == 201:
            return 'DUMMY_201'

        if table2Version == 254 and indicatorOfParameter == 200:
            return 'DUMMY_200'

        if table2Version == 254 and indicatorOfParameter == 199:
            return 'DUMMY_199'

        if table2Version == 254 and indicatorOfParameter == 198:
            return 'DUMMY_198'

        if table2Version == 254 and indicatorOfParameter == 197:
            return 'DUMMY_197'

        if table2Version == 254 and indicatorOfParameter == 196:
            return 'DUMMY_196'

        if table2Version == 254 and indicatorOfParameter == 195:
            return 'DUMMY_195'

        if table2Version == 254 and indicatorOfParameter == 194:
            return 'DUMMY_194'

        if table2Version == 254 and indicatorOfParameter == 193:
            return 'DUMMY_193'

        if table2Version == 254 and indicatorOfParameter == 192:
            return 'DUMMY_192'

        if table2Version == 254 and indicatorOfParameter == 191:
            return 'DUMMY_191'

        if table2Version == 254 and indicatorOfParameter == 190:
            return 'DUMMY_190'

        if table2Version == 254 and indicatorOfParameter == 189:
            return 'DUMMY_189'

        if table2Version == 254 and indicatorOfParameter == 188:
            return 'DUMMY_188'

        if table2Version == 254 and indicatorOfParameter == 187:
            return 'DUMMY_187'

        if table2Version == 254 and indicatorOfParameter == 186:
            return 'DUMMY_186'

        if table2Version == 254 and indicatorOfParameter == 185:
            return 'DUMMY_185'

        if table2Version == 254 and indicatorOfParameter == 184:
            return 'DUMMY_184'

        if table2Version == 254 and indicatorOfParameter == 183:
            return 'DUMMY_183'

        if table2Version == 254 and indicatorOfParameter == 182:
            return 'DUMMY_182'

        if table2Version == 254 and indicatorOfParameter == 181:
            return 'DUMMY_181'

        if table2Version == 254 and indicatorOfParameter == 180:
            return 'DUMMY_180'

        if table2Version == 254 and indicatorOfParameter == 179:
            return 'DUMMY_179'

        if table2Version == 254 and indicatorOfParameter == 178:
            return 'DUMMY_178'

        if table2Version == 254 and indicatorOfParameter == 177:
            return 'DUMMY_177'

        if table2Version == 254 and indicatorOfParameter == 176:
            return 'DUMMY_176'

        if table2Version == 254 and indicatorOfParameter == 175:
            return 'DUMMY_175'

        if table2Version == 254 and indicatorOfParameter == 174:
            return 'DUMMY_174'

        if table2Version == 254 and indicatorOfParameter == 173:
            return 'DUMMY_173'

        if table2Version == 254 and indicatorOfParameter == 172:
            return 'DUMMY_172'

        if table2Version == 254 and indicatorOfParameter == 171:
            return 'DUMMY_171'

        if table2Version == 254 and indicatorOfParameter == 170:
            return 'DUMMY_170'

        if table2Version == 254 and indicatorOfParameter == 169:
            return 'DUMMY_169'

        if table2Version == 254 and indicatorOfParameter == 168:
            return 'DUMMY_168'

        if table2Version == 254 and indicatorOfParameter == 167:
            return 'DUMMY_167'

        if table2Version == 254 and indicatorOfParameter == 166:
            return 'DUMMY_166'

        if table2Version == 254 and indicatorOfParameter == 165:
            return 'DUMMY_165'

        if table2Version == 254 and indicatorOfParameter == 164:
            return 'DUMMY_164'

        if table2Version == 254 and indicatorOfParameter == 163:
            return 'DUMMY_163'

        if table2Version == 254 and indicatorOfParameter == 162:
            return 'DUMMY_162'

        if table2Version == 254 and indicatorOfParameter == 161:
            return 'DUMMY_161'

        if table2Version == 254 and indicatorOfParameter == 160:
            return 'DUMMY_160'

        if table2Version == 254 and indicatorOfParameter == 159:
            return 'DUMMY_159'

        if table2Version == 254 and indicatorOfParameter == 158:
            return 'DUMMY_158'

        if table2Version == 254 and indicatorOfParameter == 157:
            return 'DUMMY_157'

        if table2Version == 254 and indicatorOfParameter == 156:
            return 'DUMMY_156'

        if table2Version == 254 and indicatorOfParameter == 155:
            return 'DUMMY_155'

        if table2Version == 254 and indicatorOfParameter == 154:
            return 'DUMMY_154'

        if table2Version == 254 and indicatorOfParameter == 153:
            return 'DUMMY_153'

        if table2Version == 254 and indicatorOfParameter == 152:
            return 'DUMMY_152'

        if table2Version == 254 and indicatorOfParameter == 151:
            return 'DUMMY_151'

        if table2Version == 254 and indicatorOfParameter == 150:
            return 'DUMMY_150'

        if table2Version == 254 and indicatorOfParameter == 149:
            return 'DUMMY_149'

        if table2Version == 254 and indicatorOfParameter == 148:
            return 'DUMMY_148'

        if table2Version == 254 and indicatorOfParameter == 147:
            return 'DUMMY_147'

        if table2Version == 254 and indicatorOfParameter == 146:
            return 'DUMMY_146'

        if table2Version == 254 and indicatorOfParameter == 145:
            return 'DUMMY_145'

        if table2Version == 254 and indicatorOfParameter == 144:
            return 'DUMMY_144'

        if table2Version == 254 and indicatorOfParameter == 143:
            return 'DUMMY_143'

        if table2Version == 254 and indicatorOfParameter == 142:
            return 'DUMMY_142'

        if table2Version == 254 and indicatorOfParameter == 141:
            return 'DUMMY_141'

        if table2Version == 254 and indicatorOfParameter == 140:
            return 'DUMMY_140'

        if table2Version == 254 and indicatorOfParameter == 139:
            return 'DUMMY_139'

        if table2Version == 254 and indicatorOfParameter == 138:
            return 'DUMMY_138'

        if table2Version == 254 and indicatorOfParameter == 137:
            return 'DUMMY_137'

        if table2Version == 254 and indicatorOfParameter == 136:
            return 'DUMMY_136'

        if table2Version == 254 and indicatorOfParameter == 135:
            return 'DUMMY_135'

        if table2Version == 254 and indicatorOfParameter == 134:
            return 'DUMMY_134'

        if table2Version == 254 and indicatorOfParameter == 133:
            return 'DUMMY_133'

        if table2Version == 254 and indicatorOfParameter == 132:
            return 'DUMMY_132'

        if table2Version == 254 and indicatorOfParameter == 131:
            return 'DUMMY_131'

        if table2Version == 254 and indicatorOfParameter == 130:
            return 'DUMMY_130'

        if table2Version == 254 and indicatorOfParameter == 129:
            return 'DUMMY_129'

        if table2Version == 254 and indicatorOfParameter == 128:
            return 'DUMMY_128'

        if table2Version == 254 and indicatorOfParameter == 127:
            return 'DUMMY_127'

        if table2Version == 254 and indicatorOfParameter == 126:
            return 'DUMMY_126'

        if table2Version == 254 and indicatorOfParameter == 125:
            return 'DUMMY_125'

        if table2Version == 254 and indicatorOfParameter == 124:
            return 'DUMMY_124'

        if table2Version == 254 and indicatorOfParameter == 123:
            return 'DUMMY_123'

        if table2Version == 254 and indicatorOfParameter == 122:
            return 'DUMMY_122'

        if table2Version == 254 and indicatorOfParameter == 121:
            return 'DUMMY_121'

        if table2Version == 254 and indicatorOfParameter == 120:
            return 'DUMMY_120'

        if table2Version == 254 and indicatorOfParameter == 119:
            return 'DUMMY_119'

        if table2Version == 254 and indicatorOfParameter == 118:
            return 'DUMMY_118'

        if table2Version == 254 and indicatorOfParameter == 117:
            return 'DUMMY_117'

        if table2Version == 254 and indicatorOfParameter == 116:
            return 'DUMMY_116'

        if table2Version == 254 and indicatorOfParameter == 115:
            return 'DUMMY_115'

        if table2Version == 254 and indicatorOfParameter == 114:
            return 'DUMMY_114'

        if table2Version == 254 and indicatorOfParameter == 113:
            return 'DUMMY_113'

        if table2Version == 254 and indicatorOfParameter == 112:
            return 'DUMMY_112'

        if table2Version == 254 and indicatorOfParameter == 111:
            return 'DUMMY_111'

        if table2Version == 254 and indicatorOfParameter == 110:
            return 'DUMMY_110'

        if table2Version == 254 and indicatorOfParameter == 109:
            return 'DUMMY_109'

        if table2Version == 254 and indicatorOfParameter == 108:
            return 'DUMMY_108'

        if table2Version == 254 and indicatorOfParameter == 107:
            return 'DUMMY_107'

        if table2Version == 254 and indicatorOfParameter == 106:
            return 'DUMMY_106'

        if table2Version == 254 and indicatorOfParameter == 105:
            return 'DUMMY_105'

        if table2Version == 254 and indicatorOfParameter == 104:
            return 'DUMMY_104'

        if table2Version == 254 and indicatorOfParameter == 103:
            return 'DUMMY_103'

        if table2Version == 254 and indicatorOfParameter == 102:
            return 'DUMMY_102'

        if table2Version == 254 and indicatorOfParameter == 101:
            return 'DUMMY_101'

        if table2Version == 254 and indicatorOfParameter == 100:
            return 'DUMMY_100'

        if table2Version == 254 and indicatorOfParameter == 99:
            return 'DUMMY_99'

        if table2Version == 254 and indicatorOfParameter == 98:
            return 'DUMMY_98'

        if table2Version == 254 and indicatorOfParameter == 97:
            return 'DUMMY_97'

        if table2Version == 254 and indicatorOfParameter == 96:
            return 'DUMMY_96'

        if table2Version == 254 and indicatorOfParameter == 95:
            return 'DUMMY_95'

        if table2Version == 254 and indicatorOfParameter == 94:
            return 'DUMMY_94'

        if table2Version == 254 and indicatorOfParameter == 93:
            return 'DUMMY_93'

        if table2Version == 254 and indicatorOfParameter == 92:
            return 'DUMMY_92'

        if table2Version == 254 and indicatorOfParameter == 91:
            return 'DUMMY_91'

        if table2Version == 254 and indicatorOfParameter == 90:
            return 'DUMMY_90'

        if table2Version == 254 and indicatorOfParameter == 89:
            return 'DUMMY_89'

        if table2Version == 254 and indicatorOfParameter == 88:
            return 'DUMMY_88'

        if table2Version == 254 and indicatorOfParameter == 87:
            return 'DUMMY_87'

        if table2Version == 254 and indicatorOfParameter == 86:
            return 'DUMMY_86'

        if table2Version == 254 and indicatorOfParameter == 85:
            return 'DUMMY_85'

        if table2Version == 254 and indicatorOfParameter == 84:
            return 'DUMMY_84'

        if table2Version == 254 and indicatorOfParameter == 83:
            return 'DUMMY_83'

        if table2Version == 254 and indicatorOfParameter == 82:
            return 'DUMMY_82'

        if table2Version == 254 and indicatorOfParameter == 81:
            return 'DUMMY_81'

        if table2Version == 254 and indicatorOfParameter == 80:
            return 'DUMMY_80'

        if table2Version == 254 and indicatorOfParameter == 79:
            return 'DUMMY_79'

        if table2Version == 254 and indicatorOfParameter == 78:
            return 'DUMMY_78'

        if table2Version == 254 and indicatorOfParameter == 77:
            return 'DUMMY_77'

        if table2Version == 254 and indicatorOfParameter == 76:
            return 'DUMMY_76'

        if table2Version == 254 and indicatorOfParameter == 75:
            return 'DUMMY_75'

        if table2Version == 254 and indicatorOfParameter == 74:
            return 'DUMMY_74'

        if table2Version == 254 and indicatorOfParameter == 73:
            return 'DUMMY_73'

        if table2Version == 254 and indicatorOfParameter == 72:
            return 'DUMMY_72'

        if table2Version == 254 and indicatorOfParameter == 71:
            return 'DUMMY_71'

        if table2Version == 254 and indicatorOfParameter == 70:
            return 'DUMMY_70'

        if table2Version == 254 and indicatorOfParameter == 69:
            return 'DUMMY_69'

        if table2Version == 254 and indicatorOfParameter == 68:
            return 'DUMMY_68'

        if table2Version == 254 and indicatorOfParameter == 67:
            return 'DUMMY_67'

        if table2Version == 254 and indicatorOfParameter == 66:
            return 'DUMMY_66'

        if table2Version == 254 and indicatorOfParameter == 65:
            return 'DUMMY_65'

        if table2Version == 254 and indicatorOfParameter == 64:
            return 'DUMMY_64'

        if table2Version == 254 and indicatorOfParameter == 63:
            return 'DUMMY_63'

        if table2Version == 254 and indicatorOfParameter == 62:
            return 'DUMMY_62'

        if table2Version == 254 and indicatorOfParameter == 61:
            return 'DUMMY_61'

        if table2Version == 254 and indicatorOfParameter == 60:
            return 'DUMMY_60'

        if table2Version == 254 and indicatorOfParameter == 59:
            return 'DUMMY_59'

        if table2Version == 254 and indicatorOfParameter == 58:
            return 'DUMMY_58'

        if table2Version == 254 and indicatorOfParameter == 57:
            return 'DUMMY_57'

        if table2Version == 254 and indicatorOfParameter == 56:
            return 'DUMMY_56'

        if table2Version == 254 and indicatorOfParameter == 55:
            return 'DUMMY_55'

        if table2Version == 254 and indicatorOfParameter == 54:
            return 'DUMMY_54'

        if table2Version == 254 and indicatorOfParameter == 53:
            return 'DUMMY_53'

        if table2Version == 254 and indicatorOfParameter == 52:
            return 'DUMMY_52'

        if table2Version == 254 and indicatorOfParameter == 51:
            return 'DUMMY_51'

        if table2Version == 254 and indicatorOfParameter == 50:
            return 'DUMMY_50'

        if table2Version == 254 and indicatorOfParameter == 49:
            return 'DUMMY_49'

        if table2Version == 254 and indicatorOfParameter == 48:
            return 'DUMMY_48'

        if table2Version == 254 and indicatorOfParameter == 47:
            return 'DUMMY_47'

        if table2Version == 254 and indicatorOfParameter == 46:
            return 'DUMMY_46'

        if table2Version == 254 and indicatorOfParameter == 45:
            return 'DUMMY_45'

        if table2Version == 254 and indicatorOfParameter == 44:
            return 'DUMMY_44'

        if table2Version == 254 and indicatorOfParameter == 43:
            return 'DUMMY_43'

        if table2Version == 254 and indicatorOfParameter == 42:
            return 'DUMMY_42'

        if table2Version == 254 and indicatorOfParameter == 41:
            return 'DUMMY_41'

        if table2Version == 254 and indicatorOfParameter == 40:
            return 'DUMMY_40'

        if table2Version == 254 and indicatorOfParameter == 39:
            return 'DUMMY_39'

        if table2Version == 254 and indicatorOfParameter == 38:
            return 'DUMMY_38'

        if table2Version == 254 and indicatorOfParameter == 37:
            return 'DUMMY_37'

        if table2Version == 254 and indicatorOfParameter == 36:
            return 'DUMMY_36'

        if table2Version == 254 and indicatorOfParameter == 35:
            return 'DUMMY_35'

        if table2Version == 254 and indicatorOfParameter == 34:
            return 'DUMMY_34'

        if table2Version == 254 and indicatorOfParameter == 33:
            return 'DUMMY_33'

        if table2Version == 254 and indicatorOfParameter == 32:
            return 'DUMMY_32'

        if table2Version == 254 and indicatorOfParameter == 31:
            return 'DUMMY_31'

        if table2Version == 254 and indicatorOfParameter == 30:
            return 'DUMMY_30'

        if table2Version == 254 and indicatorOfParameter == 29:
            return 'DUMMY_29'

        if table2Version == 254 and indicatorOfParameter == 28:
            return 'DUMMY_28'

        if table2Version == 254 and indicatorOfParameter == 27:
            return 'DUMMY_27'

        if table2Version == 254 and indicatorOfParameter == 26:
            return 'DUMMY_26'

        if table2Version == 254 and indicatorOfParameter == 25:
            return 'DUMMY_25'

        if table2Version == 254 and indicatorOfParameter == 24:
            return 'DUMMY_24'

        if table2Version == 254 and indicatorOfParameter == 23:
            return 'DUMMY_23'

        if table2Version == 254 and indicatorOfParameter == 22:
            return 'DUMMY_22'

        if table2Version == 254 and indicatorOfParameter == 21:
            return 'DUMMY_21'

        if table2Version == 254 and indicatorOfParameter == 20:
            return 'DUMMY_20'

        if table2Version == 254 and indicatorOfParameter == 19:
            return 'DUMMY_19'

        if table2Version == 254 and indicatorOfParameter == 18:
            return 'DUMMY_18'

        if table2Version == 254 and indicatorOfParameter == 17:
            return 'DUMMY_17'

        if table2Version == 254 and indicatorOfParameter == 16:
            return 'DUMMY_16'

        if table2Version == 254 and indicatorOfParameter == 15:
            return 'DUMMY_15'

        if table2Version == 254 and indicatorOfParameter == 14:
            return 'DUMMY_14'

        if table2Version == 254 and indicatorOfParameter == 13:
            return 'DUMMY_13'

        if table2Version == 254 and indicatorOfParameter == 12:
            return 'DUMMY_12'

        if table2Version == 254 and indicatorOfParameter == 11:
            return 'DUMMY_11'

        if table2Version == 254 and indicatorOfParameter == 10:
            return 'DUMMY_10'

        if table2Version == 254 and indicatorOfParameter == 9:
            return 'DUMMY_9'

        if table2Version == 254 and indicatorOfParameter == 8:
            return 'DUMMY_8'

        if table2Version == 254 and indicatorOfParameter == 7:
            return 'DUMMY_7'

        if table2Version == 254 and indicatorOfParameter == 6:
            return 'DUMMY_6'

        if table2Version == 254 and indicatorOfParameter == 5:
            return 'DUMMY_5'

        if table2Version == 254 and indicatorOfParameter == 4:
            return 'DUMMY_4'

        if table2Version == 254 and indicatorOfParameter == 3:
            return 'DUMMY_3'

        if table2Version == 254 and indicatorOfParameter == 2:
            return 'DUMMY_2'

        if table2Version == 254 and indicatorOfParameter == 1:
            return 'DUMMY_1'

        if table2Version == 242 and indicatorOfParameter == 252:
            return 'number concentration of dust (sum of all modes)'

        if table2Version == 242 and indicatorOfParameter == 251:
            return 'mass concentration of dust (sum of all modes)'

        if table2Version == 242 and indicatorOfParameter == 74:
            return 'number concentration of dust (maximum mode)'

        if table2Version == 242 and indicatorOfParameter == 73:
            return 'number concentration of dust (medium mode)'

        if table2Version == 242 and indicatorOfParameter == 72:
            return 'number concentration of dust (minimum mode)'

        if table2Version == 242 and indicatorOfParameter == 35:
            return 'mass concentration of dust (maximum mode)'

        if table2Version == 242 and indicatorOfParameter == 34:
            return 'mass concentration of dust (medium mode)'

        if table2Version == 2 and indicatorOfParameter == 19:
            return 'Lapse rate'

        if table2Version == 242 and indicatorOfParameter == 33:
            return 'mass concentration of dust (minimum mode)'

        if table2Version == 201 and indicatorOfParameter == 90:
            return 'Height of thermals above MSL'

        if table2Version == 201 and indicatorOfParameter == 211:
            return 'Atmospheric Resistance'

        if table2Version == 201 and indicatorOfParameter == 157:
            return 'buoyancy-production of TKE due to sub grid scale convection'

        if table2Version == 201 and indicatorOfParameter == 156:
            return 'shear-production of TKE due to separated horizontal shear modes'

        if table2Version == 201 and indicatorOfParameter == 155:
            return 'wake-production of TKE due to sub grid scale orography'

        if table2Version == 210 and indicatorOfParameter == 34:
            return 'Prob Starkes Tauwetter'

        if table2Version == 210 and indicatorOfParameter == 33:
            return 'Prob Tauwetter'

        if table2Version == 210 and indicatorOfParameter == 32:
            return 'Prob Nebel (ueberoertl. Sichtweite < 150 m)'

        if table2Version == 210 and indicatorOfParameter == 31:
            return 'Prob Glatteis'

        if table2Version == 210 and indicatorOfParameter == 30:
            return 'Prob oertlich Glatteis'

        if table2Version == 210 and indicatorOfParameter == 29:
            return 'Prob Glaette'

        if table2Version == 210 and indicatorOfParameter == 28:
            return 'Prob Starke Schneeverwehung'

        if table2Version == 210 and indicatorOfParameter == 27:
            return 'Prob Schneeverwehung'

        if table2Version == 210 and indicatorOfParameter == 26:
            return 'Prob Extrem ergiebiger Dauerregen'

        if table2Version == 210 and indicatorOfParameter == 25:
            return 'Prob Ergiebiger Dauerregen'

        if table2Version == 210 and indicatorOfParameter == 24:
            return 'Prob Dauerregen'

        if table2Version == 210 and indicatorOfParameter == 23:
            return 'Prob Schweres Gewitter'

        if table2Version == 210 and indicatorOfParameter == 22:
            return 'Prob Starkes Gewitter'

        if table2Version == 210 and indicatorOfParameter == 21:
            return 'Prob Gewitter'

        if table2Version == 210 and indicatorOfParameter == 20:
            return 'Prob Strenger Frost'

        if table2Version == 210 and indicatorOfParameter == 19:
            return 'Prob Frost'

        if table2Version == 210 and indicatorOfParameter == 18:
            return 'Prob Extrem starker Schneefall > 25 cm'

        if table2Version == 210 and indicatorOfParameter == 17:
            return 'Prob Starker Schneefall > 10 cm'

        if table2Version == 210 and indicatorOfParameter == 16:
            return 'Prob Schneefall > 5 cm'

        if table2Version == 210 and indicatorOfParameter == 15:
            return 'Prob Leichter Schneefall > 1 cm'

        if table2Version == 210 and indicatorOfParameter == 14:
            return 'Prob Leichter Schneefall > 0,5 cm'

        if table2Version == 210 and indicatorOfParameter == 13:
            return 'Prob Leichter Schneefall > 0,1 cm'

        if table2Version == 210 and indicatorOfParameter == 12:
            return 'Prob Leichter Schneefall > 0,1 mm'

        if table2Version == 210 and indicatorOfParameter == 11:
            return 'Prob Extrem Heftiger Starkregen > 50 mm'

        if table2Version == 210 and indicatorOfParameter == 10:
            return 'Prob Heftiger Starkregen > 25 mm'

        if table2Version == 210 and indicatorOfParameter == 9:
            return 'Prob Starkregen > 10 mm'

        if table2Version == 210 and indicatorOfParameter == 8:
            return 'Prob Oberoertliche Orkanboeen > 75 kn'

        if table2Version == 210 and indicatorOfParameter == 7:
            return 'Prob Orkanboeen > 63 kn'

        if table2Version == 210 and indicatorOfParameter == 6:
            return 'Prob Orkanartige Boeen > 55 kn'

        if table2Version == 210 and indicatorOfParameter == 5:
            return 'Prob Schwere Sturmboeen > 47 kn'

        if table2Version == 210 and indicatorOfParameter == 4:
            return 'Prob Sturmboeen > 40 kn'

        if table2Version == 210 and indicatorOfParameter == 3:
            return 'Prob Sturmboeen > 33 kn'

        if table2Version == 210 and indicatorOfParameter == 2:
            return 'Prob Windboeen > 27 kn'

        if table2Version == 210 and indicatorOfParameter == 1:
            return 'Prob Windboeen > 25 kn'

        if table2Version == 2 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 203 and indicatorOfParameter == 2:
            return 'Geopotential height'

        if table2Version == 2 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 204 and indicatorOfParameter == 71:
            return 'Ellrod Index'

        if table2Version == 204 and indicatorOfParameter == 70:
            return 'Eddy Dissipation Rate'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 1 and level == 2:
            return 'Min 2m Temperature (i) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 1 and level == 2:
            return 'Max 2m Temperature (i) Initialisation'

        topLevel = h.get_l('topLevel')
        bottomLevel = h.get_l('bottomLevel')

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 7 and bottomLevel == 50:
            return 'Soil Moisture Content (7-50 cm)'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 7:
            return 'Soil Moisture Content (0-7 cm)'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 112:
            return 'Soil Temperature (layer)'

        localElementNumber = h.get_l('localElementNumber')

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 2 and indicatorOfTypeOfLevel == 112 and topLevel == 0:
            return 'covariance of soil moisture content (0-10)'

        if table2Version == 203 and indicatorOfParameter == 10:
            return '3 hour pressure change'

        if table2Version == 202 and indicatorOfParameter == 119:
            return 'Logarithm of Pressure'

        if table2Version == 202 and indicatorOfParameter == 117:
            return 'Sea surface temperature interpolated in time in C'

        if table2Version == 202 and indicatorOfParameter == 101:
            return 'tidal tendencies'

        if table2Version == 201 and indicatorOfParameter == 231:
            return '- FE1 I128A[AMP]ROUTI von 199809 bis 199905'

        if table2Version == 201 and indicatorOfParameter == 83:
            return 'dry convection top index'

        if table2Version == 2 and indicatorOfParameter == 44:
            return 'Relative Divergenz'

        if table2Version == 2 and indicatorOfParameter == 7:
            return 'Geopotential height'

        if table2Version == 203 and indicatorOfParameter == 146:
            return 'Clear Air Turbulence Index'

        if table2Version == 203 and indicatorOfParameter == 128:
            return 'Frontogenesis function'

        if table2Version == 203 and indicatorOfParameter == 127:
            return 'Divergenz Qs'

        if table2Version == 203 and indicatorOfParameter == 126:
            return 'Divergenz Qn'

        if table2Version == 203 and indicatorOfParameter == 125:
            return 'Q-Vektor parallel zu den Isothermen'

        if table2Version == 203 and indicatorOfParameter == 123:
            return 'Divergenz'

        if table2Version == 203 and indicatorOfParameter == 118:
            return 'Frontogenesefunktion'

        if table2Version == 203 and indicatorOfParameter == 117:
            return 'Divergenz Qs geostrophisch'

        if table2Version == 203 and indicatorOfParameter == 116:
            return 'Divergenz Qn geostrophisch'

        if table2Version == 203 and indicatorOfParameter == 115:
            return 'Q-Vektor parallel zu d. Isothermen (geostrophisch)'

        if table2Version == 203 and indicatorOfParameter == 114:
            return 'Q-Vektor senkrecht zu d. Isothermen (geostrophisch)'

        if table2Version == 203 and indicatorOfParameter == 113:
            return 'Divergenz Q (geostrophisch)'

        if table2Version == 203 and indicatorOfParameter == 112:
            return 'Q-Vektor Y-Komponente (geostrophisch)'

        if table2Version == 203 and indicatorOfParameter == 111:
            return 'Q-Vektor X-Komponente (geostrophisch)'

        if table2Version == 203 and indicatorOfParameter == 105:
            return 'Forcing rechte Seite Omegagleichung'

        if table2Version == 203 and indicatorOfParameter == 100:
            return 'geostrophische Vorticity'

        if table2Version == 203 and indicatorOfParameter == 119:
            return 'Potentielle Vorticity (auf Druckflaechen, nicht isentrop)'

        if table2Version == 2 and indicatorOfParameter == 63 and timeRangeIndicator == 5:
            return 'Convective Precipitation (difference)'

        if table2Version == 2 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 2 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 'vertical vorticity'

        if table2Version == 202 and indicatorOfParameter == 134:
            return 'relative vorticity,V-component'

        if table2Version == 202 and indicatorOfParameter == 133:
            return 'relative vorticity,U-component'

        if table2Version == 203 and indicatorOfParameter == 205:
            return 'current weather (symbol number: 0..9)'

        if table2Version == 203 and indicatorOfParameter == 194:
            return 'Diagnose Icing Scenario Code (1=general,2=convective,3=stratiform,4=freezing)'

        if table2Version == 203 and indicatorOfParameter == 193:
            return 'Diagnose Icing Degree Code (1=light,2=moderate,3=severe)'

        if table2Version == 203 and indicatorOfParameter == 192:
            return 'Prognose Icing Scenario Code (1=general,2=convective,3=stratiform,4=freezing)'

        if table2Version == 203 and indicatorOfParameter == 191:
            return 'Prognose Icing Degree Code (1=light,2=moderate,3=severe)'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'Icing Signifikant Code (1=general,2=convective,3=stratiform,4=freezing) - Diagnose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'Icing Vertical Code (1=continuous,2=discontinuous) - Diagnose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'Icing Top (hft) - Diagnose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'Icing Signifikant Top (hft) - Diagnose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'Icing Signifikant Base (hft) - Diagnose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'Icing Base (hft) - Diagnose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'Icing Max Code (1=light,2=moderate,3=severe) - Diagnose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'Icing Vertical Code (1=continuous,2=discontinuous) - Diagnose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'Icing Top (hft) - Diagnose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'Icing Max Top (hft) - Diagnose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'Icing Max Base (hft) - Diagnose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'Icing Base (hft) - Diagnose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'Icing Signifikant Code (1=general,2=convective,3=stratiform,4=freezing) - Prognose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'Icing Vertical Code (1=continuous,2=discontinuous) - Prognose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'Icing Top (hft) - Prognose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'Icing Signifikant Top (hft) - Prognose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'Icing Signifikant Base (hft) - Prognose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'Icing Base (hft) - Prognose Icing Scenario Composit'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 'Icing Max Code (1=light,2=moderate,3=severe) - Prognose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 'Icing Vertical Code (1=continuous,2=discontinuous) - Prognose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 'Icing Top (hft) - Prognose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 'Icing Max Top (hft) - Prognose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 'Icing Max Base (hft) - Prognose Icing Degree Composit'

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 'Icing Base (hft) - Prognose Icing Degree Composit'

        if table2Version == 201 and indicatorOfParameter == 94:
            return 'Sediment thickness of the upper layer of bottom sediments'

        if table2Version == 201 and indicatorOfParameter == 192:
            return 'Temperature at the lower boundary of the upper layer of bottom sediment (penetrated by thermal wave)'

        if table2Version == 201 and indicatorOfParameter == 91:
            return 'Shape factor with respect to the temperature profile in the thermocline'

        if table2Version == 201 and indicatorOfParameter == 95:
            return 'Mixed-layer depth'

        if table2Version == 201 and indicatorOfParameter == 191:
            return 'Bottom temperature (temperature at the water-bottom sediment interface)'

        if table2Version == 201 and indicatorOfParameter == 193:
            return 'Mixed-layer temperature'

        if table2Version == 201 and indicatorOfParameter == 194:
            return 'Mean temperature of the water column'

        if table2Version == 201 and indicatorOfParameter == 190:
            return 'Temperature at the lower boundary of the thermally active layer of bottom sediment'

        if table2Version == 201 and indicatorOfParameter == 93:
            return 'Depth of thermally active layer of bottom sediment'

        if table2Version == 201 and indicatorOfParameter == 92:
            return 'Attenuation coefficient of water with respect to solar radiation'

        if table2Version == 201 and indicatorOfParameter == 97:
            return 'Wind fetch'

        if table2Version == 201 and indicatorOfParameter == 96:
            return 'Lake depth'

        if table2Version == 202 and indicatorOfParameter == 55:
            return 'Water Fraction'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Upward diffusive short wave radiation flux at surface ( mean over forecast time) Initialisation'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Downward diffusive short wave radiation flux at surface ( mean over forecast time) Initialisation'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Downward direct short wave radiation flux at surface (mean over forecast time) Initialisation'

        if table2Version == 201 and indicatorOfParameter == 42 and timeRangeIndicator == 0:
            return 'vertical integral of divergence of total water content (s)'

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Upward diffusive short wave radiation flux at surface ( mean over forecast time)'

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Downward diffusive short wave radiation flux at surface ( mean over forecast time)'

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Downward direct short wave radiation flux at surface (mean over forecast time)'

        if table2Version == 203 and indicatorOfParameter == 58:
            return 'value of isolation of clothes'

        if table2Version == 203 and indicatorOfParameter == 57:
            return 'probability to perceive sultriness'

        if table2Version == 2 and indicatorOfParameter == 41:
            return 'Absolute Vorticity'

        if table2Version == 203 and indicatorOfParameter == 61:
            return 'Water temperature in C'

        if table2Version == 2 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 203 and indicatorOfParameter == 60:
            return 'perceived temperature'

        if table2Version == 203 and indicatorOfParameter == 93:
            return 'Konvektionsart (0..4)'

        if table2Version == 202 and indicatorOfParameter == 249:
            return 'Time of maximum of UV Index, clouded'

        if table2Version == 202 and indicatorOfParameter == 247:
            return 'Total ozone'

        if table2Version == 202 and indicatorOfParameter == 243:
            return 'UV Index, clear sky, maximum'

        if table2Version == 202 and indicatorOfParameter == 242:
            return 'UV Index, clouded sky; corrected for albedo, aerosol, altitude and clouds'

        if table2Version == 202 and indicatorOfParameter == 241:
            return 'Basic UV Index, clear sky; MSL, fixed albedo, fixed aerosol'

        if table2Version == 202 and indicatorOfParameter == 240:
            return 'UV Index, clear sky; corrected for albedo, aerosol and altitude'

        if table2Version == 208 and indicatorOfParameter == 236:
            return 'Probability of temperature <= -10 deg C during 6h'

        if table2Version == 208 and indicatorOfParameter == 232:
            return 'Probability of temperature < 0 deg C during 1h'

        if table2Version == 208 and indicatorOfParameter == 213:
            return 'Probability of strong snowdrift during 12h'

        if table2Version == 208 and indicatorOfParameter == 212:
            return 'Probability of snowdrift during 12h'

        if table2Version == 208 and indicatorOfParameter == 199:
            return 'Probability of severe thunderstorm during 1h'

        if table2Version == 208 and indicatorOfParameter == 198:
            return 'Probability of heavy thunderstorm during 1h'

        if table2Version == 208 and indicatorOfParameter == 197:
            return 'Probability of thunderstorm during 1h'

        if table2Version == 208 and indicatorOfParameter == 191:
            return 'Probability of black ice during 1h'

        if table2Version == 208 and indicatorOfParameter == 139:
            return 'Probability of 1h maximum wind gust speed >= 39m/s'

        if table2Version == 208 and indicatorOfParameter == 138:
            return 'Probability of 1h maximum wind gust speed >= 33m/s'

        if table2Version == 208 and indicatorOfParameter == 137:
            return 'Probability of 1h maximum wind gust speed >= 29m/s'

        if table2Version == 208 and indicatorOfParameter == 136:
            return 'Probability of 1h maximum wind gust speed >= 25m/s'

        if table2Version == 208 and indicatorOfParameter == 134:
            return 'Probability of 1h maximum wind gust speed >= 18m/s'

        if table2Version == 208 and indicatorOfParameter == 132:
            return 'Probability of 1h maximum wind gust speed >= 14m/s'

        if table2Version == 208 and indicatorOfParameter == 77:
            return 'Probability of 12h accumulated snow >= 25cm'

        if table2Version == 208 and indicatorOfParameter == 75:
            return 'Probability of 12h accumulated snow >= 15cm'

        if table2Version == 208 and indicatorOfParameter == 74:
            return 'Probability of 12h accumulated snow >= 10cm'

        if table2Version == 208 and indicatorOfParameter == 72:
            return 'Probability of 12h accumulated snow >=0.5cm'

        if table2Version == 208 and indicatorOfParameter == 71:
            return 'Probability of 6h accumulated snow >= 10cm'

        if table2Version == 208 and indicatorOfParameter == 70:
            return 'Probability of 6h accumulated snow >= 5cm'

        if table2Version == 208 and indicatorOfParameter == 69:
            return 'Probability of 6h accumulated snow >=0.5cm'

        if table2Version == 208 and indicatorOfParameter == 32:
            return 'Probability of 12h total precipitation >= 70mm'

        if table2Version == 208 and indicatorOfParameter == 29:
            return 'Probability of 12h total precipitation >= 40mm'

        if table2Version == 208 and indicatorOfParameter == 26:
            return 'Probability of 12h total precipitation >= 25mm'

        if table2Version == 208 and indicatorOfParameter == 17:
            return 'Probability of 6h total precipitation >= 35mm'

        if table2Version == 208 and indicatorOfParameter == 14:
            return 'Probability of 6h total precipitation >= 20mm'

        if table2Version == 208 and indicatorOfParameter == 3:
            return 'Probability of 1h total precipitation >= 25mm'

        if table2Version == 208 and indicatorOfParameter == 1:
            return 'Probability of 1h total precipitation >= 10mm'

        if table2Version == 201 and indicatorOfParameter == 132 and timeRangeIndicator == 0:
            return 'Graupel (snow pellets) precipitation (Initialisation)'

        if table2Version == 201 and indicatorOfParameter == 113 and timeRangeIndicator == 1:
            return 'Convective rain Initialisation'

        if table2Version == 201 and indicatorOfParameter == 102 and timeRangeIndicator == 1:
            return 'Large scale rain (Accumulation) Initialisation'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Photosynthetically active radiation'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Momentum Flux, V-Component (m) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Momentum Flux, U-Component (m) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Sensible Heat Net Flux (m) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Latent Heat Net Flux (m) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 1:
            return 'Total Precipitation (Accumulation) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 78 and timeRangeIndicator == 1:
            return 'Convective Snowfall water equivalent (s) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 79 and timeRangeIndicator == 1:
            return 'Large-Scale snowfall - water equivalent (Accumulation) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Net long wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 'Net short wave radiation flux (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 1:
            return 'Net long wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 1:
            return 'Net short wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 2:
            return 'Min 2m Temperature (i) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 2:
            return 'Max 2m Temperature (i) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'Evaporation (s) Initialisation'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 10:
            return 'maximum Wind 10m Initialisation'

        if table2Version == 2 and indicatorOfParameter == 78 and timeRangeIndicator == 0:
            return 'Convective Snowfall water equivalent (s) Initialisation'

        if table2Version == 201 and indicatorOfParameter == 113 and timeRangeIndicator == 0:
            return 'Convective rain Initialisation'

        if table2Version == 2 and indicatorOfParameter == 79 and timeRangeIndicator == 0:
            return 'Large-Scale snowfall - water equivalent (Accumulation) Initialisation'

        if table2Version == 201 and indicatorOfParameter == 102 and timeRangeIndicator == 0:
            return 'Large scale rain (Accumulation) Initialisation'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 0:
            return 'Total Precipitation (Accumulation) Initialisation'

        if table2Version == 203 and indicatorOfParameter == 56 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'Min 2m Temperature long periods > h'

        if table2Version == 203 and indicatorOfParameter == 55 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'Max 2m Temperature long periods > h'

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 5:
            return 'Total Precipitation Difference'

        if table2Version == 207 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'calibrated forecast, wind speed (gust)'

        if table2Version == 207 and indicatorOfParameter == 79:
            return 'calibrated forecast, large-scale snowfall'

        if table2Version == 207 and indicatorOfParameter == 61:
            return 'calibrated forecast, total precipitation  (Accumulation)'

        if table2Version == 206 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'smoothed forecast, wind speed (gust)'

        if table2Version == 206 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 'smoothed forecast, soil temperature'

        if table2Version == 206 and indicatorOfParameter == 79:
            return 'smoothed forecast, large-scale snowfall'

        if table2Version == 206 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, cloud cover high'

        if table2Version == 206 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, cloud cover medium'

        if table2Version == 206 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, cloud cover low'

        if table2Version == 206 and indicatorOfParameter == 71:
            return 'smoothed forecast, total cloud cover'

        if table2Version == 206 and indicatorOfParameter == 61:
            return 'smoothed forecast, total precipitation (Accumulation)'

        if table2Version == 206 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'smoothed forecast, v comp. of wind'

        if table2Version == 206 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'smoothed forecast, u comp. of wind'

        if table2Version == 206 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'smoothed forecast, dew point temp.'

        if table2Version == 206 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'smoothed forecast, minimum temp.'

        if table2Version == 206 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 'smoothed forecast, maximum temp.'

        if table2Version == 206 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'smoothed forecast, temperature'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 204 and indicatorOfParameter == 16:
            return 'Monthly Mean of RMS of difference IA-AN of kinetic energy'

        if table2Version == 204 and indicatorOfParameter == 15:
            return 'Monthly Mean of RMS of difference FG-AN of kinetic energy'

        if table2Version == 204 and indicatorOfParameter == 14:
            return 'Monthly Mean of RMS of difference IA-AN of vert.velocity (pressure)'

        if table2Version == 204 and indicatorOfParameter == 13:
            return 'Monthly Mean of RMS of difference FG-AN of vert.velocity (pressure)'

        if table2Version == 204 and indicatorOfParameter == 12:
            return 'Monthly Mean of RMS of difference IA-AN of temperature'

        if table2Version == 204 and indicatorOfParameter == 11:
            return 'Monthly Mean of RMS of difference FG-AN of temperature'

        if table2Version == 204 and indicatorOfParameter == 10:
            return 'Monthly Mean of RMS of difference IA-AN of relative humidity'

        if table2Version == 204 and indicatorOfParameter == 9:
            return 'Monthly Mean of RMS of difference FG-AN of relative humidity'

        if table2Version == 204 and indicatorOfParameter == 8:
            return 'Monthly Mean of RMS of difference IA-AN of geopotential'

        if table2Version == 204 and indicatorOfParameter == 7:
            return 'Monthly Mean of RMS of difference FG-AN of geopotential'

        if table2Version == 204 and indicatorOfParameter == 6:
            return 'Monthly Mean of RMS of difference IA-AN of v-component of wind'

        if table2Version == 204 and indicatorOfParameter == 5:
            return 'Monthly Mean of RMS of difference FG-AN of v-component of wind'

        if table2Version == 204 and indicatorOfParameter == 4:
            return 'Monthly Mean of RMS of difference IA-AN of u-component of wind'

        if table2Version == 204 and indicatorOfParameter == 3:
            return 'Monthly Mean of RMS of difference FG-AN of u-component of wind'

        if table2Version == 204 and indicatorOfParameter == 2:
            return 'Monthly Mean of RMS of difference IA-AN of pressure reduced to MSL'

        if table2Version == 204 and indicatorOfParameter == 1:
            return 'Monthly Mean of RMS of difference FG-AN of pressure reduced to MSL'

        if table2Version == 203 and indicatorOfParameter == 204:
            return 'modified cloud cover for media'

        if table2Version == 203 and indicatorOfParameter == 203:
            return 'modified cloud depth for media'

        if table2Version == 203 and indicatorOfParameter == 196:
            return 'Icing Grade (1=LGT,2=MOD,3=SEV)'

        if table2Version == 203 and indicatorOfParameter == 157:
            return 'Ceiling'

        if table2Version == 203 and indicatorOfParameter == 154:
            return 'Aequivalentpotentielle Temperatur'

        if table2Version == 203 and indicatorOfParameter == 140:
            return 'KO index'

        if table2Version == 203 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 100:
            return 'Druck einer isentropen Flaeche'

        if table2Version == 203 and indicatorOfParameter == 132:
            return 'Wind Y-Komponente auf isentropen Flaechen'

        if table2Version == 203 and indicatorOfParameter == 131:
            return 'Wind X-Komponente auf isentropen Flaechen'

        if table2Version == 203 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 100:
            return 'Isentrope potentielle Vorticity'

        if table2Version == 203 and indicatorOfParameter == 124:
            return 'Q-Vektor senkrecht zu den Isothermen'

        if table2Version == 203 and indicatorOfParameter == 109:
            return 'Winddivergenz'

        if table2Version == 203 and indicatorOfParameter == 107:
            return 'Schichtdickenadvektion'

        if table2Version == 203 and indicatorOfParameter == 103:
            return 'geostrophische Schichtdickenadvektion'

        if table2Version == 203 and indicatorOfParameter == 101:
            return 'geostrophische Vorticityadvektion'

        if table2Version == 203 and indicatorOfParameter == 99:
            return 'weather interpretation (WMO)'

        if table2Version == 203 and indicatorOfParameter == 94 and indicatorOfTypeOfLevel == 1:
            return 'Hoehe der Konvektionsuntergrenze ueber nn'

        if table2Version == 203 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 'Hoehe der Konvektionsuntergrenze ueber Grund'

        if table2Version == 203 and indicatorOfParameter == 90:
            return 'Kombination Niederschlag-Bewoelkung-Blauthermik (cl_typ,tab)'

        if table2Version == 203 and indicatorOfParameter == 33:
            return 'Absolute vorticity advection'

        if table2Version == 203 and indicatorOfParameter == 30:
            return 'storm relative helicity'

        if table2Version == 203 and indicatorOfParameter == 29:
            return 'Vertical speed shear'

        if table2Version == 202 and indicatorOfParameter == 248:
            return 'UV Index, clouded sky, maximum'

        if table2Version == 202 and indicatorOfParameter == 233:
            return 'Gravity wave dissipation (vertical integral)'

        if table2Version == 202 and indicatorOfParameter == 233 and timeRangeIndicator == 1:
            return 'Gravity wave dissipation (initialisation)'

        if table2Version == 202 and indicatorOfParameter == 232:
            return 'v-momentum flux due to SSO-effects'

        if table2Version == 202 and indicatorOfParameter == 232 and timeRangeIndicator == 3:
            return 'v-momentum flux due to SSO-effects (average)'

        if table2Version == 202 and indicatorOfParameter == 231:
            return 'u-momentum flux due to SSO-effects'

        if table2Version == 202 and indicatorOfParameter == 231 and timeRangeIndicator == 3:
            return 'u-momentum flux due to SSO-effects (initialisation)'

        if table2Version == 202 and indicatorOfParameter == 229:
            return 'Ba140 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 228:
            return 'Ba140 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 227:
            return 'Air concentration of Barium 140'

        if table2Version == 202 and indicatorOfParameter == 226:
            return 'I131o - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 225:
            return 'I131o - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 224:
            return 'Air concentration of Iodine 131 organic bounded'

        if table2Version == 202 and indicatorOfParameter == 223:
            return 'I131g - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 222:
            return 'I131g - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 221:
            return 'Air concentration of Iodine 131 elementary gaseous'

        if table2Version == 202 and indicatorOfParameter == 220:
            return 'Xe133 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 219:
            return 'Xe133 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 218:
            return 'Air concentration of Xenon 133'

        if table2Version == 202 and indicatorOfParameter == 217:
            return 'TRACER - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 216:
            return 'TRACER - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 215:
            return 'TRACER - concentration'

        if table2Version == 202 and indicatorOfParameter == 214:
            return 'Kr85 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 213:
            return 'Kr85 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 212:
            return 'Air concentration of Krypton 85'

        if table2Version == 202 and indicatorOfParameter == 211:
            return 'Zr95 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 210:
            return 'Zr95 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 209:
            return 'Air concentration of Zirconium 95'

        if table2Version == 202 and indicatorOfParameter == 208:
            return 'Te132 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 207:
            return 'Te132 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 206:
            return 'Air concentration of Tellurium 132'

        if table2Version == 202 and indicatorOfParameter == 205:
            return 'Cs137 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 204:
            return 'Cs137 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 203:
            return 'Air concentration of Caesium 137'

        if table2Version == 202 and indicatorOfParameter == 202:
            return 'I131 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 201:
            return 'I131 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 200:
            return 'Air concentration of Iodine 131 aerosol'

        if table2Version == 202 and indicatorOfParameter == 199:
            return 'Sr90 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 198:
            return 'Sr90 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 197:
            return 'Air concentration of Strontium 90'

        if table2Version == 202 and indicatorOfParameter == 196:
            return 'Ru103 - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 195:
            return 'Ru103 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 194:
            return 'Air concentration of Ruthenium 103'

        if table2Version == 202 and indicatorOfParameter == 180:
            return 'Ozone Mixing Ratio'

        if table2Version == 202 and indicatorOfParameter == 123:
            return 'Delay of the GPS signal trough dry atmos.'

        if table2Version == 202 and indicatorOfParameter == 122:
            return 'Delay of the GPS signal trough wet atmos.'

        if table2Version == 202 and indicatorOfParameter == 121:
            return 'Delay of the GPS signal trough the (total) atm.'

        if table2Version == 202 and indicatorOfParameter == 115:
            return 'geographical longitude'

        if table2Version == 202 and indicatorOfParameter == 114:
            return 'geographical latitude'

        if table2Version == 202 and indicatorOfParameter == 113:
            return 'Coriolis parameter'

        if table2Version == 202 and indicatorOfParameter == 105:
            return 'water vapor flux'

        if table2Version == 202 and indicatorOfParameter == 104:
            return 'tendency of specific humidity'

        if table2Version == 202 and indicatorOfParameter == 93 and timeRangeIndicator == 3:
            return 'Sea salt aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 93:
            return 'Sea salt aerosol'

        if table2Version == 202 and indicatorOfParameter == 92 and timeRangeIndicator == 3:
            return 'Black carbon aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 92:
            return 'Black carbon aerosol'

        if table2Version == 202 and indicatorOfParameter == 91 and timeRangeIndicator == 3:
            return 'Organic aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 91:
            return 'Organic aerosol'

        if table2Version == 202 and indicatorOfParameter == 86 and timeRangeIndicator == 3:
            return 'Total soil dust aerosol (climatology,12M)'

        if table2Version == 202 and indicatorOfParameter == 86:
            return 'Total soil dust aerosol (climatology)'

        if table2Version == 202 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 'Total sulfate aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 84:
            return 'Total sulfate aerosol'

        if table2Version == 202 and indicatorOfParameter == 79 and timeRangeIndicator == 0:
            return 'current ratio of monthly mean NDVI (normalized differential vegetation index) to annual maximum'

        if table2Version == 202 and indicatorOfParameter == 79 and timeRangeIndicator == 3:
            return 'ratio of monthly mean NDVI (normalized differential vegetation index) to annual maximum'

        if table2Version == 202 and indicatorOfParameter == 78 and timeRangeIndicator == 0:
            return 'normalized differential vegetation index (NDVI)'

        if table2Version == 202 and indicatorOfParameter == 77 and timeRangeIndicator == 3:
            return 'normalized differential vegetation index'

        if table2Version == 202 and indicatorOfParameter == 76:
            return 'deciduous forest'

        if table2Version == 202 and indicatorOfParameter == 75:
            return 'evergreen forest'

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 2 and indicatorOfTypeOfLevel == 112:
            return 'variance of soil moisture content (10-100)'

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 1 and indicatorOfTypeOfLevel == 112 and topLevel == 0:
            return 'variance of soil moisture content (0-10)'

        if table2Version == 202 and indicatorOfParameter == 71:
            return 'Orographie + Land-Meer-Verteilung'

        if table2Version == 202 and indicatorOfParameter == 70:
            return 'Min Leaf area index'

        if table2Version == 202 and indicatorOfParameter == 69:
            return 'Max Leaf area index'

        if table2Version == 202 and indicatorOfParameter == 68:
            return 'Plant covering degree in the quiescent phas'

        if table2Version == 202 and indicatorOfParameter == 67:
            return 'Plant covering degree in the vegetation phase'

        if table2Version == 202 and indicatorOfParameter == 65:
            return 'vertically integrated ozone content (climatological)'

        if table2Version == 202 and indicatorOfParameter == 64:
            return 'height of ozone maximum (climatological)'

        if table2Version == 202 and indicatorOfParameter == 62:
            return 'root depth of vegetation'

        if table2Version == 202 and indicatorOfParameter == 61:
            return 'Leaf area index'

        if table2Version == 202 and indicatorOfParameter == 57:
            return 'soil type of grid (1...9, local soilType.table)'

        if table2Version == 202 and indicatorOfParameter == 56:
            return 'surface emissivity'

        if table2Version == 202 and indicatorOfParameter == 49:
            return 'Slope of sub-gridscale orography'

        if table2Version == 202 and indicatorOfParameter == 48:
            return 'Angle of sub-gridscale orography'

        if table2Version == 202 and indicatorOfParameter == 47:
            return 'Anisotropy of sub-gridscale orography'

        if table2Version == 202 and indicatorOfParameter == 46:
            return 'Standard deviation of sub-grid scale orography'

        if table2Version == 202 and indicatorOfParameter == 45:
            return 'meridional wind tendency due to subgrid scale oro.'

        if table2Version == 202 and indicatorOfParameter == 44:
            return 'zonal wind tendency due to subgrid scale oro.'

        if table2Version == 202 and indicatorOfParameter == 42:
            return 'analysis error(standard deviation), v-comp. of wind'

        if table2Version == 202 and indicatorOfParameter == 41:
            return 'analysis error(standard deviation), u-comp. of wind'

        if table2Version == 202 and indicatorOfParameter == 40:
            return 'analysis error(standard deviation), geopotential(gpm)'

        if table2Version == 202 and indicatorOfParameter == 19:
            return 'Total directional spread'

        if table2Version == 202 and indicatorOfParameter == 18:
            return 'Total Tm2 period'

        if table2Version == 202 and indicatorOfParameter == 17:
            return 'Total Tm1 period'

        if table2Version == 202 and indicatorOfParameter == 10:
            return 'Total wave mean period'

        if table2Version == 202 and indicatorOfParameter == 9:
            return 'Total wave peak period'

        if table2Version == 202 and indicatorOfParameter == 8:
            return 'Swell peak period'

        if table2Version == 202 and indicatorOfParameter == 7:
            return 'Peak period of total swell'

        if table2Version == 202 and indicatorOfParameter == 4:
            return 'Total Wave Direction'

        if table2Version == 201 and indicatorOfParameter == 243:
            return 'moisture convergence for Kuo-type closure'

        if table2Version == 201 and indicatorOfParameter == 241:
            return 'Convective Available Potential Energy'

        if table2Version == 201 and indicatorOfParameter == 240 and indicatorOfTypeOfLevel == 1:
            return 'Massflux at convective cloud base'

        if table2Version == 201 and indicatorOfParameter == 239:
            return 'residuum of soil moisture'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'total forcing at soil surface'

        if table2Version == 201 and indicatorOfParameter == 237:
            return 'total transpiration from all soil layers'

        if table2Version == 201 and indicatorOfParameter == 236:
            return 'sum of contributions to evaporation'

        if table2Version == 201 and indicatorOfParameter == 233:
            return 'Effective transmissivity of solar radiation'

        if table2Version == 201 and indicatorOfParameter == 232:
            return 'solution of 2-d Helmholtz equations - needed for restart'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200:
            return 'Base reflectivity (cmax)'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 110:
            return 'Base reflectivity'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 1:
            return 'Base reflectivity'

        if table2Version == 201 and indicatorOfParameter == 215:
            return 'Sea Ice Temperature'

        if table2Version == 201 and indicatorOfParameter == 212:
            return 'Minimal Stomatal Resistance'

        if table2Version == 201 and indicatorOfParameter == 203:
            return 'Snow temperature (top of snow)'

        if table2Version == 201 and indicatorOfParameter == 200:
            return 'Plant Canopy Surface Water'

        if table2Version == 201 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 111:
            return 'soil ice content (multilayers)'

        if table2Version == 201 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 111:
            return 'Column-integrated Soil Moisture (multilayers)'

        if table2Version == 201 and indicatorOfParameter == 197 and indicatorOfTypeOfLevel == 111:
            return 'Soil Temperature (multilayer model)'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'maximum Wind 10m'

        if table2Version == 201 and indicatorOfParameter == 173:
            return 'mixed layer depth'

        if table2Version == 201 and indicatorOfParameter == 171:
            return 'Turbulent transfer coefficient for heat (and Moisture)'

        if table2Version == 201 and indicatorOfParameter == 170:
            return 'Turbulent transfer coefficient for impulse'

        if table2Version == 201 and indicatorOfParameter == 154:
            return 'Turbulent diffusion coefficient for heat (and moisture)'

        if table2Version == 201 and indicatorOfParameter == 153:
            return 'Turbulent diffusioncoefficient for momentum'

        if table2Version == 201 and indicatorOfParameter == 152:
            return 'Turbulent Kinetic Energy'

        if table2Version == 201 and indicatorOfParameter == 149:
            return 'Kinetic Energy'

        if table2Version == 201 and indicatorOfParameter == 148:
            return 'Tendency of turbulent kinetic energy'

        if table2Version == 201 and indicatorOfParameter == 147:
            return 'Convective turbulent kinetic enery'

        if table2Version == 201 and indicatorOfParameter == 146 and indicatorOfTypeOfLevel == 1:
            return 'Convective Inhibition, mean layer'

        if table2Version == 201 and indicatorOfParameter == 145 and indicatorOfTypeOfLevel == 1:
            return 'Convective Available Potential Energy, mean layer'

        if table2Version == 201 and indicatorOfParameter == 144 and indicatorOfTypeOfLevel == 1:
            return 'Convective Inhibition, most unstable'

        if table2Version == 201 and indicatorOfParameter == 143 and indicatorOfTypeOfLevel == 1:
            return 'Convective Available Potential Energy, most unstable'

        if table2Version == 201 and indicatorOfParameter == 142:
            return 'supercell detection index 2 (only rot. up drafts)'

        if table2Version == 201 and indicatorOfParameter == 141:
            return 'supercell detection index 1 (rot. up+down drafts)'

        if table2Version == 201 and indicatorOfParameter == 139:
            return 'Pressure perturbation'

        if table2Version == 201 and indicatorOfParameter == 133:
            return 'Snow density'

        if table2Version == 201 and indicatorOfParameter == 132:
            return 'Graupel (snow pellets) precipitation (Accumulation)'

        if table2Version == 201 and indicatorOfParameter == 131:
            return 'Graupel (snow pellets) precipitation rate'

        if table2Version == 201 and indicatorOfParameter == 130:
            return 'tendency of specific cloud ice content due to grid scale precipitation'

        if table2Version == 201 and indicatorOfParameter == 129:
            return 'Fresh snow factor (weighting function for albedo indicating freshness of snow)'

        if table2Version == 201 and indicatorOfParameter == 127:
            return 'tendency of specific cloud liquid water content due to grid scale precipitation'

        if table2Version == 201 and indicatorOfParameter == 125:
            return 'Specific humitiy tendency due to grid scale precipitation'

        if table2Version == 201 and indicatorOfParameter == 124:
            return 'Temperature tendency due to grid scale precipation'

        if table2Version == 201 and indicatorOfParameter == 123:
            return 'snow amount, grid-scale plus convective'

        if table2Version == 201 and indicatorOfParameter == 122:
            return 'rain amount, grid-scale plus convective'

        if table2Version == 201 and indicatorOfParameter == 113:
            return 'Convective rain'

        if table2Version == 201 and indicatorOfParameter == 112:
            return 'Convective snowfall rate water equivalent'

        if table2Version == 201 and indicatorOfParameter == 111:
            return 'Convective rain rate'

        if table2Version == 201 and indicatorOfParameter == 102:
            return 'Large scale rain (Accumulation)'

        if table2Version == 201 and indicatorOfParameter == 101:
            return 'Large scale snowfall rate water equivalent'

        if table2Version == 201 and indicatorOfParameter == 100:
            return 'Large scale rain rate'

        if table2Version == 201 and indicatorOfParameter == 99:
            return 'Specific content of precipitation particles (needed for water loading)'

        if table2Version == 201 and indicatorOfParameter == 89:
            return 'tendency of  specific cloud ice content due to convection'

        if table2Version == 201 and indicatorOfParameter == 88:
            return 'Tendency of specific cloud liquid water content due to conversion'

        if table2Version == 201 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 4:
            return 'Height of snow fall limit above MSL'

        if table2Version == 201 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 4:
            return 'Height of 0 degree Celsius isotherm above msl'

        if table2Version == 201 and indicatorOfParameter == 82 and indicatorOfTypeOfLevel == 1:
            return 'Height of top of dry convection above MSL'

        if table2Version == 201 and indicatorOfParameter == 79:
            return 'meridional wind tendency due to convection'

        if table2Version == 201 and indicatorOfParameter == 78:
            return 'zonal wind tendency due to convection'

        if table2Version == 201 and indicatorOfParameter == 75:
            return 'Specific humitiy tendency due to convection'

        if table2Version == 201 and indicatorOfParameter == 74:
            return 'Temperature tendency due to convection'

        if table2Version == 201 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'top index (vertical level) of main convective cloud (i)'

        if table2Version == 201 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1:
            return 'base index (vertical level) of main convective cloud (i)'

        if table2Version == 201 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 3:
            return 'Height of Convective Cloud Top above msl'

        if table2Version == 201 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 2:
            return 'Height of Convective Cloud Base above msl'

        if table2Version == 201 and indicatorOfParameter == 61:
            return 'specific cloud water content, convective cloud'

        if table2Version == 201 and indicatorOfParameter == 59 and indicatorOfTypeOfLevel == 3:
            return 'Cloud top above msl, shallow convection'

        if table2Version == 201 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 2:
            return 'cloud base above msl, shallow convection'

        if table2Version == 201 and indicatorOfParameter == 53:
            return 'cloud cover CL (0..8)'

        if table2Version == 201 and indicatorOfParameter == 52:
            return 'cloud cover CM (0..8)'

        if table2Version == 201 and indicatorOfParameter == 51:
            return 'cloud cover CH (0..8)'

        if table2Version == 201 and indicatorOfParameter == 44:
            return 'subgridscale cloud ice'

        if table2Version == 201 and indicatorOfParameter == 43:
            return 'subgrid scale cloud water'

        if table2Version == 201 and indicatorOfParameter == 42:
            return 'vertical integral of divergence of total water content (s)'

        if table2Version == 201 and indicatorOfParameter == 41:
            return 'Total Column integrated water (all components incl. precipitation)'

        if table2Version == 201 and indicatorOfParameter == 40:
            return 'Total column integrated grauple'

        if table2Version == 201 and indicatorOfParameter == 39:
            return 'Grauple'

        if table2Version == 201 and indicatorOfParameter == 38:
            return 'Total column integrated snow'

        if table2Version == 201 and indicatorOfParameter == 37:
            return 'Total column integrated rain'

        if table2Version == 201 and indicatorOfParameter == 36:
            return 'Snow mixing ratio'

        if table2Version == 201 and indicatorOfParameter == 35:
            return 'Rain mixing ratio'

        if table2Version == 201 and indicatorOfParameter == 33:
            return 'Cloud Ice Mixing Ratio'

        if table2Version == 201 and indicatorOfParameter == 31:
            return 'Cloud Mixing Ratio'

        if table2Version == 201 and indicatorOfParameter == 30:
            return 'Non-Convective Cloud Cover, grid scale'

        if table2Version == 201 and indicatorOfParameter == 29:
            return 'Cloud cover'

        if table2Version == 201 and indicatorOfParameter == 21 and timeRangeIndicator == 0:
            return 'Stomatal Resistance'

        if table2Version == 201 and indicatorOfParameter == 20 and timeRangeIndicator == 4:
            return 'Sunshine duration in h'

        if table2Version == 201 and indicatorOfParameter == 19 and indicatorOfTypeOfLevel == 111 and timeRangeIndicator == 3:
            return 'Latent heat flux from plants'

        if table2Version == 201 and indicatorOfParameter == 18 and timeRangeIndicator == 3:
            return 'Latent heat flux from bare soil'

        if table2Version == 201 and indicatorOfParameter == 14:
            return 'Thermal radiation heating rate'

        if table2Version == 201 and indicatorOfParameter == 13:
            return 'Solar radiation heating rate'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1:
            return 'Photosynthetically active radiation'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Photosynthetically active radiation (m) (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Momentum Flux, V-Component (m)'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Momentum Flux, U-Component (m)'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Sensible Heat Net Flux (m)'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Latent Heat Net Flux (m)'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8:
            return 'Net long wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'Net long wave radiation flux (m) (on the model top)'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8:
            return 'Net short wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'Net short wave radiation flux (on the model top)'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1:
            return 'Net long wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Net long wave radiation flux (m) (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1:
            return 'Net short wave radiation flux (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Net short wave radiation flux (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 'Mean period of total swell'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'Significant height of total swell'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'Mean direction of total swell'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'Direction of wind waves'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'Significant height of combined wind waves and swell'

        if table2Version == 2 and indicatorOfParameter == 92:
            return 'Sea Ice Thickness'

        if table2Version == 2 and indicatorOfParameter == 91:
            return 'Sea Ice Cover ( 0= free, 1=cover)'

        if table2Version == 2 and indicatorOfParameter == 90 and topLevel == 0:
            return 'Water Runoff (s)'

        if table2Version == 2 and indicatorOfParameter == 90 and topLevel == 10:
            return 'Water Runoff'

        if table2Version == 2 and indicatorOfParameter == 87:
            return 'Plant cover'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and bottomLevel == 100:
            return 'Column-integrated Soil Moisture (2) 10-100cm'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 'Column-integrated Soil Moisture (1) 0 -10 cm'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 100 and bottomLevel == 190:
            return 'Column-integrated Soil Moisture'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111:
            return 'Soil Temperature'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 9:
            return 'Soil Temperature'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 41:
            return 'Soil Temperature (41 cm depth)'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 36:
            return 'Soil Temperature  ( 36 cm depth, vv=0h)'

        if table2Version == 2 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 'Albedo (in short-wave, average)'

        if table2Version == 2 and indicatorOfParameter == 84:
            return 'Albedo (in short-wave)'

        if table2Version == 2 and indicatorOfParameter == 83:
            return 'Surface Roughness length Surface Roughness'

        if table2Version == 2 and indicatorOfParameter == 81:
            return 'Land Cover (1=land, 0=sea)'

        if table2Version == 2 and indicatorOfParameter == 79:
            return 'Large-Scale snowfall - water equivalent (Accumulation)'

        if table2Version == 2 and indicatorOfParameter == 78:
            return 'Convective Snowfall water equivalent (s)'

        if table2Version == 2 and indicatorOfParameter == 76:
            return 'Total Column-Integrated Cloud Water'

        if table2Version == 2 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'Cloud Cover (0 - 400 hPa)'

        if table2Version == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 'Cloud Cover (400 - 800 hPa)'

        if table2Version == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'Cloud Cover (800 hPa - Soil)'

        if table2Version == 2 and indicatorOfParameter == 72:
            return 'Convective Cloud Cover'

        if table2Version == 2 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 2 and indicatorOfParameter == 66:
            return 'Snow Depth'

        if table2Version == 2 and indicatorOfParameter == 65:
            return 'Snow depth water equivalent'

        if table2Version == 2 and indicatorOfParameter == 63 and timeRangeIndicator == 4:
            return 'Convective Precipitation (Accumulation)'

        if table2Version == 2 and indicatorOfParameter == 62 and timeRangeIndicator == 4:
            return 'Large-Scale Precipitation (Accumulation)'

        if table2Version == 2 and indicatorOfParameter == 61:
            return 'Total Precipitation (Accumulation)'

        if table2Version == 2 and indicatorOfParameter == 58:
            return 'Total Column-Integrated Cloud Ice'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1:
            return 'Evaporation (s)'

        if table2Version == 2 and indicatorOfParameter == 54:
            return 'Total column integrated water vapour'

        if table2Version == 2 and indicatorOfParameter == 52:
            return 'Relative Humidity'

        if table2Version == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2m Relative Humidity'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'Specific Humidity'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Specific Humidity (2m)'

        if table2Version == 2 and indicatorOfParameter == 40:
            return 'Vertical Velocity (Geometric) (w)'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'Vertical Velocity (Pressure) ( omega=dp/dt )'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'V-Component of Wind'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'V-Component of Wind'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'U-Component of Wind'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'U-Component of Wind'

        if table2Version == 2 and indicatorOfParameter == 32:
            return 'Wind speed (SP)'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'Wind speed (SP_10M)'

        if table2Version == 2 and indicatorOfParameter == 31:
            return 'Wind Direction (DD)'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'Wind Direction (DD_10M)'

        if table2Version == 2 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 2 and indicatorOfParameter == 29:
            return 'Wave spectra (2)'

        if table2Version == 2 and indicatorOfParameter == 28:
            return 'Wave spectra (1)'

        if table2Version == 2 and indicatorOfParameter == 21:
            return 'Radar spectra (1)'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return '2m Dew Point Temperature (AV)'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2m Dew Point Temperature'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Min 2m Temperature (i)'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Max 2m Temperature (i)'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 'Climat. temperature, 2m Temperature'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return '2m Temperature (AV)'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2m Temperature'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 'Temperature (G)'

        if table2Version == 2 and indicatorOfParameter == 10:
            return 'Total Column Integrated Ozone'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 109:
            return 'Geometric Height of the layer limits above sea level(NN)'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 1:
            return 'Geometric Height of the earths surface above sea level'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 110:
            return 'Geopotential (full lev)'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 1:
            return 'Geopotential (S)'

        if table2Version == 2 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 1:
            return 'Pressure Tendency (S)'

        if table2Version == 2 and indicatorOfParameter == 2:
            return 'Pressure Reduced to MSL'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pressure (S) (not reduced)'

    return wrapped
