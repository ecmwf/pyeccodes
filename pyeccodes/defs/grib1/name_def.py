import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 1 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'Total Precipitation'

        if table2Version == 1 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'Snow Fall water equivalent'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'Soil Temperature'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'Soil Moisture'

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'Orography'

        if table2Version == 1 and indicatorOfParameter == 87:
            return 'Percentage of vegetation'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'Momentum flux, v-component'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'Momentum flux, u-component'

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
            return 'Net short-wave radiation flux(atmosph.top)'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'Net long-wave radiation flux (surface)'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'Net short-wave radiation flux (surface)'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 'Secondary wave mean period'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 1 and indicatorOfParameter == 108:
            return 'Primary wave mean period'

        if table2Version == 1 and indicatorOfParameter == 107:
            return 'Primary wave direction'

        if table2Version == 1 and indicatorOfParameter == 106:
            return 'Mean period of swell waves'

        if table2Version == 1 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 1 and indicatorOfParameter == 104:
            return 'Direction of swell waves'

        if table2Version == 1 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 1 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 1 and indicatorOfParameter == 101:
            return 'Mean direction of wind waves'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'Signific.height,combined wind waves+swell'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 'Ice divergence'

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
            return 'Ice thickness'

        if table2Version == 1 and indicatorOfParameter == 91:
            return 'Ice cover (1=ice, 0=no ice)'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 'Salinity'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'Soil moisture content'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'Deviation of sea-level from mean'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'Main thermocline anomaly'

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
            return 'V-component of current '

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'U-component of current '

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
            return 'Absolute vorticity'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'Montgomery stream Function'

        if table2Version == 1 and indicatorOfParameter == 31:
            return 'Wind direction'

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
            return 'Dew point depression (or deficit)'

        if table2Version == 1 and indicatorOfParameter == 17:
            return 'Dew point temperature'

        if table2Version == 1 and indicatorOfParameter == 16:
            return 'Minimum temperature'

        if table2Version == 1 and indicatorOfParameter == 15:
            return 'Maximum temperature'

        if table2Version == 1 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential temperature'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'Standard deviation of height'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'Geometrical height'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'Pressure tendency'

        if table2Version == 1 and indicatorOfParameter == 84:
            return 'Albedo'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'Convective snow'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'Boundary layer dissipation'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'Sensible heat flux'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'Latent heat flux'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'Large scale snow'

        if table2Version == 1 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 1 and indicatorOfParameter == 74:
            return 'Medium cloud cover'

        if table2Version == 1 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 1 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'Snow depth'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'large scale precipitation'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'Total column ozone'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'Runoff'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'Brightness temperature'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'Evaporation'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'Surface roughness'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'Land-sea mask'

        if table2Version == 1 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre dewpoint temperature'

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre temperature'

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10 metre V wind component'

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10 metre U wind component'

        if table2Version == 1 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'Geopotential Height'

        if table2Version == 1 and indicatorOfParameter == 44:
            return 'Divergence'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'Mean sea level pressure'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 'Vorticity (relative)'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'Vertical velocity'

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Surface pressure'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'V component of wind'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'U component of wind'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Minimum temperature at 2 metres in the last 6 hours'

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Maximum temperature at 2 metres in the last 6 hours'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'Wind speed'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'Total Precipitation'

        if table2Version == 2 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 2 and indicatorOfParameter == 65:
            return 'Snow Fall water equivalent'

        if table2Version == 2 and indicatorOfParameter == 85:
            return 'Soil Temperature'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'Soil Moisture'

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'Orography'

        if table2Version == 2 and indicatorOfParameter == 87:
            return 'Percentage of vegetation'

        if table2Version == 2 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 2 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 2 and indicatorOfParameter == 125:
            return 'Momentum flux, v-component'

        if table2Version == 2 and indicatorOfParameter == 124:
            return 'Momentum flux, u-component'

        if table2Version == 2 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 2 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 2 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 2 and indicatorOfParameter == 116:
            return 'Short wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 115:
            return 'Long wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 114:
            return 'Net long-wave radiation flux(atmosph.top)'

        if table2Version == 2 and indicatorOfParameter == 113:
            return 'Net short-wave radiation flux(atmosph.top)'

        if table2Version == 2 and indicatorOfParameter == 112:
            return 'Net long-wave radiation flux (surface)'

        if table2Version == 2 and indicatorOfParameter == 111:
            return 'Net short-wave radiation flux (surface)'

        if table2Version == 2 and indicatorOfParameter == 110:
            return 'Secondary wave mean period'

        if table2Version == 2 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 2 and indicatorOfParameter == 108:
            return 'Primary wave mean period'

        if table2Version == 2 and indicatorOfParameter == 107:
            return 'Primary wave direction'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 'Mean period of swell waves'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'Direction of swell waves'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'Mean direction of wind waves'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'Signific.height,combined wind waves+swell'

        if table2Version == 2 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 2 and indicatorOfParameter == 98:
            return 'Ice divergence'

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

        if table2Version == 2 and indicatorOfParameter == 92:
            return 'Ice thickness'

        if table2Version == 2 and indicatorOfParameter == 91:
            return 'Ice cover (1=ice, 0=no ice)'

        if table2Version == 2 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 2 and indicatorOfParameter == 88:
            return 'Salinity'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'Soil moisture content'

        if table2Version == 2 and indicatorOfParameter == 82:
            return 'Deviation of sea-level from mean'

        if table2Version == 2 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 2 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 2 and indicatorOfParameter == 70:
            return 'Main thermocline anomaly'

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

        if table2Version == 2 and indicatorOfParameter == 54:
            return 'Precipitable water'

        if table2Version == 2 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 2 and indicatorOfParameter == 50:
            return 'V-component of current '

        if table2Version == 2 and indicatorOfParameter == 49:
            return 'U-component of current '

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

        if table2Version == 2 and indicatorOfParameter == 41:
            return 'Absolute vorticity'

        if table2Version == 2 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 2 and indicatorOfParameter == 37:
            return 'Montgomery stream Function'

        if table2Version == 2 and indicatorOfParameter == 31:
            return 'Wind direction'

        if table2Version == 2 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 2 and indicatorOfParameter == 29:
            return 'Wave spectra (2)'

        if table2Version == 2 and indicatorOfParameter == 28:
            return 'Wave spectra (1)'

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

        if table2Version == 2 and indicatorOfParameter == 21:
            return 'Radar spectra (1)'

        if table2Version == 2 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 2 and indicatorOfParameter == 19:
            return 'Lapse rate'

        if table2Version == 2 and indicatorOfParameter == 18:
            return 'Dew point depression (or deficit)'

        if table2Version == 2 and indicatorOfParameter == 17:
            return 'Dew point temperature'

        if table2Version == 2 and indicatorOfParameter == 16:
            return 'Minimum temperature'

        if table2Version == 2 and indicatorOfParameter == 15:
            return 'Maximum temperature'

        if table2Version == 2 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential temperature'

        if table2Version == 2 and indicatorOfParameter == 9:
            return 'Standard deviation of height'

        if table2Version == 2 and indicatorOfParameter == 8:
            return 'Geometrical height'

        if table2Version == 2 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 2 and indicatorOfParameter == 3:
            return 'Pressure tendency'

        if table2Version == 2 and indicatorOfParameter == 84:
            return 'Albedo'

        if table2Version == 2 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 2 and indicatorOfParameter == 78:
            return 'Convective snow'

        if table2Version == 2 and indicatorOfParameter == 123:
            return 'Boundary layer dissipation'

        if table2Version == 2 and indicatorOfParameter == 122:
            return 'Sensible heat flux'

        if table2Version == 2 and indicatorOfParameter == 121:
            return 'Latent heat flux'

        if table2Version == 2 and indicatorOfParameter == 79:
            return 'Large scale snow'

        if table2Version == 2 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 2 and indicatorOfParameter == 74:
            return 'Medium cloud cover'

        if table2Version == 2 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 2 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 2 and indicatorOfParameter == 66:
            return 'Snow depth'

        if table2Version == 2 and indicatorOfParameter == 62:
            return 'large scale precipitation'

        if table2Version == 2 and indicatorOfParameter == 10:
            return 'Total column ozone'

        if table2Version == 2 and indicatorOfParameter == 90:
            return 'Runoff'

        if table2Version == 2 and indicatorOfParameter == 118:
            return 'Brightness temperature'

        if table2Version == 2 and indicatorOfParameter == 57:
            return 'Evaporation'

        if table2Version == 2 and indicatorOfParameter == 83:
            return 'Surface roughness'

        if table2Version == 2 and indicatorOfParameter == 81:
            return 'Land-sea mask'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre dewpoint temperature'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre temperature'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10 metre V wind component'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10 metre U wind component'

        if table2Version == 2 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 2 and indicatorOfParameter == 7:
            return 'Geopotential Height'

        if table2Version == 2 and indicatorOfParameter == 44:
            return 'Divergence'

        if table2Version == 2 and indicatorOfParameter == 2:
            return 'Mean sea level pressure'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 'Vorticity (relative)'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'Vertical velocity'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Surface pressure'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'V component of wind'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'U component of wind'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Minimum temperature at 2 metres in the last 6 hours'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Maximum temperature at 2 metres in the last 6 hours'

        if table2Version == 2 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 2 and indicatorOfParameter == 32:
            return 'Wind speed'

        if table2Version == 2 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 2 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 2 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 3 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'Total Precipitation'

        if table2Version == 3 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 3 and indicatorOfParameter == 65:
            return 'Snow Fall water equivalent'

        if table2Version == 3 and indicatorOfParameter == 85:
            return 'Soil Temperature'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'Soil Moisture'

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'Orography'

        if table2Version == 3 and indicatorOfParameter == 87:
            return 'Percentage of vegetation'

        if table2Version == 3 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 3 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 3 and indicatorOfParameter == 125:
            return 'Momentum flux, v-component'

        if table2Version == 3 and indicatorOfParameter == 124:
            return 'Momentum flux, u-component'

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
            return 'Net short-wave radiation flux(atmosph.top)'

        if table2Version == 3 and indicatorOfParameter == 112:
            return 'Net long-wave radiation flux (surface)'

        if table2Version == 3 and indicatorOfParameter == 111:
            return 'Net short-wave radiation flux (surface)'

        if table2Version == 3 and indicatorOfParameter == 110:
            return 'Secondary wave mean period'

        if table2Version == 3 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 3 and indicatorOfParameter == 108:
            return 'Primary wave mean period'

        if table2Version == 3 and indicatorOfParameter == 107:
            return 'Primary wave direction'

        if table2Version == 3 and indicatorOfParameter == 106:
            return 'Mean period of swell waves'

        if table2Version == 3 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 3 and indicatorOfParameter == 104:
            return 'Direction of swell waves'

        if table2Version == 3 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 3 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 3 and indicatorOfParameter == 101:
            return 'Mean direction of wind waves'

        if table2Version == 3 and indicatorOfParameter == 100:
            return 'Signific.height,combined wind waves+swell'

        if table2Version == 3 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 3 and indicatorOfParameter == 98:
            return 'Ice divergence'

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
            return 'Ice thickness'

        if table2Version == 3 and indicatorOfParameter == 91:
            return 'Ice cover (1=ice, 0=no ice)'

        if table2Version == 3 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 3 and indicatorOfParameter == 88:
            return 'Salinity'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'Soil moisture content'

        if table2Version == 3 and indicatorOfParameter == 82:
            return 'Deviation of sea-level from mean'

        if table2Version == 3 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 3 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 3 and indicatorOfParameter == 70:
            return 'Main thermocline anomaly'

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
            return 'V-component of current '

        if table2Version == 3 and indicatorOfParameter == 49:
            return 'U-component of current '

        if table2Version == 3 and indicatorOfParameter == 48:
            return 'Speed of current'

        if table2Version == 3 and indicatorOfParameter == 47:
            return 'Direction of current'

        if table2Version == 3 and indicatorOfParameter == 46:
            return 'Vertical v-component shear'

        if table2Version == 3 and indicatorOfParameter == 45:
            return 'Vertical u-component shear'

        if table2Version == 3 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 3 and indicatorOfParameter == 41:
            return 'Absolute vorticity'

        if table2Version == 3 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 3 and indicatorOfParameter == 37:
            return 'Montgomery stream Function'

        if table2Version == 3 and indicatorOfParameter == 31:
            return 'Wind direction'

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
            return 'Dew point depression (or deficit)'

        if table2Version == 3 and indicatorOfParameter == 17:
            return 'Dew point temperature'

        if table2Version == 3 and indicatorOfParameter == 16:
            return 'Minimum temperature'

        if table2Version == 3 and indicatorOfParameter == 15:
            return 'Maximum temperature'

        if table2Version == 3 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential temperature'

        if table2Version == 3 and indicatorOfParameter == 9:
            return 'Standard deviation of height'

        if table2Version == 3 and indicatorOfParameter == 8:
            return 'Geometrical height'

        if table2Version == 3 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 3 and indicatorOfParameter == 3:
            return 'Pressure tendency'

        if table2Version == 3 and indicatorOfParameter == 12:
            return 'Virtual temperature'

        if table2Version == 2 and indicatorOfParameter == 12:
            return 'Virtual temperature'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'Virtual temperature'

        if table2Version == 3 and indicatorOfParameter == 84:
            return 'Albedo'

        if table2Version == 3 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 3 and indicatorOfParameter == 78:
            return 'Convective snow'

        if table2Version == 3 and indicatorOfParameter == 123:
            return 'Boundary layer dissipation'

        if table2Version == 3 and indicatorOfParameter == 122:
            return 'Sensible heat flux'

        if table2Version == 3 and indicatorOfParameter == 121:
            return 'Latent heat flux'

        if table2Version == 3 and indicatorOfParameter == 79:
            return 'Large scale snow'

        if table2Version == 3 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 3 and indicatorOfParameter == 74:
            return 'Medium cloud cover'

        if table2Version == 3 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 3 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 3 and indicatorOfParameter == 66:
            return 'Snow depth'

        if table2Version == 3 and indicatorOfParameter == 62:
            return 'large scale precipitation'

        if table2Version == 3 and indicatorOfParameter == 10:
            return 'Total column ozone'

        if table2Version == 3 and indicatorOfParameter == 90:
            return 'Runoff'

        if table2Version == 3 and indicatorOfParameter == 118:
            return 'Brightness temperature'

        if table2Version == 3 and indicatorOfParameter == 57:
            return 'Evaporation'

        if table2Version == 3 and indicatorOfParameter == 83:
            return 'Surface roughness'

        if table2Version == 3 and indicatorOfParameter == 81:
            return 'Land-sea mask'

        if table2Version == 3 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre dewpoint temperature'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre temperature'

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10 metre V wind component'

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10 metre U wind component'

        if table2Version == 3 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 3 and indicatorOfParameter == 7:
            return 'Geopotential Height'

        if table2Version == 3 and indicatorOfParameter == 44:
            return 'Divergence'

        if table2Version == 3 and indicatorOfParameter == 2:
            return 'Mean sea level pressure'

        if table2Version == 3 and indicatorOfParameter == 43:
            return 'Vorticity (relative)'

        if table2Version == 3 and indicatorOfParameter == 39:
            return 'Vertical velocity'

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Surface pressure'

        if table2Version == 3 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 3 and indicatorOfParameter == 34:
            return 'V component of wind'

        if table2Version == 3 and indicatorOfParameter == 33:
            return 'U component of wind'

        if table2Version == 3 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 3 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Minimum temperature at 2 metres in the last 6 hours'

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Maximum temperature at 2 metres in the last 6 hours'

        if table2Version == 3 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 3 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 3 and indicatorOfParameter == 32:
            return 'Wind speed'

        if table2Version == 3 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 3 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 3 and indicatorOfParameter == 35:
            return 'Stream function'

    return wrapped
