import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 200 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 200 and indicatorOfParameter == 65:
            return 'Snow depth water equivalent'

        if table2Version == 200 and indicatorOfParameter == 85:
            return 'Soil Temperature'

        if table2Version == 200 and indicatorOfParameter == 221:
            return 'specific cloud water content'

        if table2Version == 200 and indicatorOfParameter == 152:
            return 'Vertical integral of northward water vapour flux'

        if table2Version == 200 and indicatorOfParameter == 157:
            return 'Vertical integral of eastward water vapour flux'

        if table2Version == 200 and indicatorOfParameter == 191:
            return 'Vertical integral of northward heat flux'

        if table2Version == 200 and indicatorOfParameter == 190:
            return 'Vertical integral of eastward heat flux'

        if table2Version == 200 and indicatorOfParameter == 87:
            return 'Percentage of vegetation'

        if table2Version == 200 and indicatorOfParameter == 228:
            return 'Cloud liquid water'

        if table2Version == 200 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 200 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 200 and indicatorOfParameter == 125:
            return 'Momentum flux, v-component'

        if table2Version == 200 and indicatorOfParameter == 124:
            return 'Momentum flux, u-component'

        if table2Version == 200 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 200 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 200 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 200 and indicatorOfParameter == 116:
            return 'Short wave radiation flux'

        if table2Version == 200 and indicatorOfParameter == 115:
            return 'Long wave radiation flux'

        if table2Version == 200 and indicatorOfParameter == 114:
            return 'Net long-wave radiation flux(atmosph.top)'

        if table2Version == 200 and indicatorOfParameter == 113:
            return 'Net short-wave radiation flux(atmosph.top)'

        if table2Version == 200 and indicatorOfParameter == 112:
            return 'Net long-wave radiation flux (surface)'

        if table2Version == 200 and indicatorOfParameter == 111:
            return 'Net short-wave radiation flux (surface)'

        if table2Version == 200 and indicatorOfParameter == 110:
            return 'Secondary wave mean period'

        if table2Version == 200 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 200 and indicatorOfParameter == 108:
            return 'Primary wave mean period'

        if table2Version == 200 and indicatorOfParameter == 107:
            return 'Primary wave direction'

        if table2Version == 200 and indicatorOfParameter == 106:
            return 'Mean period of swell waves'

        if table2Version == 200 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 200 and indicatorOfParameter == 104:
            return 'Direction of swell waves'

        if table2Version == 200 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 200 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 200 and indicatorOfParameter == 101:
            return 'Mean direction of wind waves'

        if table2Version == 200 and indicatorOfParameter == 100:
            return 'Signific.height,combined wind waves+swell'

        if table2Version == 200 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 200 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 200 and indicatorOfParameter == 97:
            return 'Ice growth rate'

        if table2Version == 200 and indicatorOfParameter == 96:
            return 'V-component of ice drift'

        if table2Version == 200 and indicatorOfParameter == 95:
            return 'U-component of ice drift'

        if table2Version == 200 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 200 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 200 and indicatorOfParameter == 92:
            return 'Ice thickness'

        if table2Version == 200 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 200 and indicatorOfParameter == 88:
            return 'Salinity'

        if table2Version == 200 and indicatorOfParameter == 86:
            return 'Soil moisture content'

        if table2Version == 200 and indicatorOfParameter == 82:
            return 'Deviation of sea-level from mean'

        if table2Version == 200 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 200 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 200 and indicatorOfParameter == 70:
            return 'Main thermocline anomaly'

        if table2Version == 200 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 200 and indicatorOfParameter == 68:
            return 'Transient thermocline depth'

        if table2Version == 200 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 200 and indicatorOfParameter == 60:
            return 'Thunderstorm probability'

        if table2Version == 200 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 200 and indicatorOfParameter == 56:
            return 'Saturation deficit'

        if table2Version == 200 and indicatorOfParameter == 55:
            return 'Vapour pressure'

        if table2Version == 200 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 200 and indicatorOfParameter == 50:
            return 'V-component of current '

        if table2Version == 200 and indicatorOfParameter == 49:
            return 'U-component of current '

        if table2Version == 200 and indicatorOfParameter == 48:
            return 'Speed of current'

        if table2Version == 200 and indicatorOfParameter == 47:
            return 'Direction of current'

        if table2Version == 200 and indicatorOfParameter == 46:
            return 'Vertical v-component shear'

        if table2Version == 200 and indicatorOfParameter == 45:
            return 'Vertical u-component shear'

        if table2Version == 200 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 200 and indicatorOfParameter == 41:
            return 'Absolute vorticity'

        if table2Version == 200 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 200 and indicatorOfParameter == 31:
            return 'Wind direction'

        if table2Version == 200 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 200 and indicatorOfParameter == 29:
            return 'Wave spectra (2)'

        if table2Version == 200 and indicatorOfParameter == 28:
            return 'Wave spectra (1)'

        if table2Version == 200 and indicatorOfParameter == 27:
            return 'Geopotential height anomaly'

        if table2Version == 200 and indicatorOfParameter == 26:
            return 'Pressure anomaly'

        if table2Version == 200 and indicatorOfParameter == 25:
            return 'Temperature anomaly'

        if table2Version == 200 and indicatorOfParameter == 24:
            return 'Parcel lifted index (to 500 hPa)'

        if table2Version == 200 and indicatorOfParameter == 23:
            return 'Radar spectra (3)'

        if table2Version == 200 and indicatorOfParameter == 22:
            return 'Radar spectra (2)'

        if table2Version == 200 and indicatorOfParameter == 21:
            return 'Radar spectra (1)'

        if table2Version == 200 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 200 and indicatorOfParameter == 19:
            return 'Lapse rate'

        if table2Version == 200 and indicatorOfParameter == 18:
            return 'Dew point depression (or deficit)'

        if table2Version == 200 and indicatorOfParameter == 17:
            return 'Dew point temperature'

        if table2Version == 200 and indicatorOfParameter == 16:
            return 'Minimum temperature'

        if table2Version == 200 and indicatorOfParameter == 15:
            return 'Maximum temperature'

        if table2Version == 200 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential temperature'

        if table2Version == 200 and indicatorOfParameter == 9:
            return 'Standard deviation of height'

        if table2Version == 200 and indicatorOfParameter == 8:
            return 'Geometrical height'

        if table2Version == 200 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 200 and indicatorOfParameter == 3:
            return 'Pressure tendency'

        if table2Version == 200 and indicatorOfParameter == 145:
            return 'Ground/surface cover temperature'

        if table2Version == 200 and indicatorOfParameter == 144:
            return 'Temperature at canopy'

        if table2Version == 200 and indicatorOfParameter == 225:
            return 'Soil wetness of surface'

        if table2Version == 200 and indicatorOfParameter == 203:
            return 'Interception loss'

        if table2Version == 200 and indicatorOfParameter == 40:
            return 'Vertical velocity'

        if table2Version == 200 and indicatorOfParameter == 12:
            return 'Virtual temperature'

        if table2Version == 200 and indicatorOfParameter == 252:
            return 'Type of vegetation'

        if table2Version == 200 and indicatorOfParameter == 253:
            return 'Large scale moistening rate'

        if table2Version == 200 and indicatorOfParameter == 251:
            return 'Long wave radiative heating rate'

        if table2Version == 200 and indicatorOfParameter == 250:
            return 'Solar radiative heating rate'

        if table2Version == 200 and indicatorOfParameter == 249:
            return 'Vertical diffusion moistening rate'

        if table2Version == 200 and indicatorOfParameter == 248:
            return 'Vertical diffusion meridional acceleration'

        if table2Version == 200 and indicatorOfParameter == 247:
            return 'Vertical diffusion zonal acceleration'

        if table2Version == 200 and indicatorOfParameter == 246:
            return 'Vertical diffusion heating rate'

        if table2Version == 200 and indicatorOfParameter == 243:
            return 'Convective moistening rate'

        if table2Version == 200 and indicatorOfParameter == 242:
            return 'Convective heating rate'

        if table2Version == 200 and indicatorOfParameter == 241:
            return 'Large scale condensation heating rate'

        if table2Version == 200 and indicatorOfParameter == 240:
            return 'Convective meridional acceleration'

        if table2Version == 200 and indicatorOfParameter == 159:
            return 'Mean zonal momentum flux by short gravity wave'

        if table2Version == 200 and indicatorOfParameter == 154:
            return 'Mean meridional momentum flux by short gravity wave'

        if table2Version == 200 and indicatorOfParameter == 148:
            return 'Mean meridional momentum flux by long gravity wave'

        if table2Version == 200 and indicatorOfParameter == 147:
            return 'Mean zonal momentum flux by long gravity wave'

        if table2Version == 200 and indicatorOfParameter == 239:
            return 'Convective zonal acceleration'

        if table2Version == 200 and indicatorOfParameter == 237:
            return 'Ozone mixing ratio'

        if table2Version == 200 and indicatorOfParameter == 236:
            return 'Adiabatic moistening rate'

        if table2Version == 200 and indicatorOfParameter == 231:
            return 'Upward mass flux'

        if table2Version == 200 and indicatorOfParameter == 230:
            return 'Upward mass flux at cloud base'

        if table2Version == 200 and indicatorOfParameter == 226:
            return 'Mass concentration of condensed water in soil'

        if table2Version == 200 and indicatorOfParameter == 224:
            return 'Moisture storage on ground or cover'

        if table2Version == 200 and indicatorOfParameter == 223:
            return 'Moisture storage on canopy'

        if table2Version == 200 and indicatorOfParameter == 222:
            return 'Adiabatic heating rate'

        if table2Version == 200 and indicatorOfParameter == 202:
            return 'Mean evapotranspiration'

        if table2Version == 200 and indicatorOfParameter == 174:
            return 'Gravity wave meridional acceleration'

        if table2Version == 200 and indicatorOfParameter == 173:
            return 'Gravity wave zonal acceleration'

        if table2Version == 200 and indicatorOfParameter == 172:
            return 'Mean frequency of stratocumulus parameterisation'

        if table2Version == 200 and indicatorOfParameter == 171:
            return 'Mean frequency of shallow convection'

        if table2Version == 200 and indicatorOfParameter == 170:
            return 'Mean frequency of deep convection'

        if table2Version == 200 and indicatorOfParameter == 165:
            return 'Adiabatic meridional acceleration'

        if table2Version == 200 and indicatorOfParameter == 151:
            return 'Adiabatic zonal acceleration'

        if table2Version == 200 and indicatorOfParameter == 132:
            return 'Square of Brunt-Vaisala frequency'

        if table2Version == 200 and indicatorOfParameter == 90:
            return 'Mean surface water runoff'

        if table2Version == 200 and indicatorOfParameter == 64:
            return 'Mean snowfall rate water equivalent'

        if table2Version == 200 and indicatorOfParameter == 63:
            return 'Mean convective precipitation'

        if table2Version == 200 and indicatorOfParameter == 62:
            return 'Mean large scale precipitation'

        if table2Version == 200 and indicatorOfParameter == 61:
            return 'Mean total precipitation'

        if table2Version == 200 and indicatorOfParameter == 57:
            return 'Mean evaporation'

        if table2Version == 200 and indicatorOfParameter == 84:
            return 'Albedo'

        if table2Version == 200 and indicatorOfParameter == 163:
            return 'Clear Sky Downward Long Wave Flux'

        if table2Version == 200 and indicatorOfParameter == 162:
            return 'Clear Sky Upward Long Wave Flux'

        if table2Version == 200 and indicatorOfParameter == 160:
            return 'Clear Sky Upward Solar Flux'

        if table2Version == 200 and indicatorOfParameter == 161:
            return 'Clear Sky Downward Solar Flux'

        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 200 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre relative humidity'

        if table2Version == 200 and indicatorOfParameter == 155:
            return 'Ground heat flux'

        if table2Version == 200 and indicatorOfParameter == 10:
            return 'Total column integrated ozone'

        if table2Version == 200 and indicatorOfParameter == 146:
            return 'Cloud work function'

        if table2Version == 200 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 200 and indicatorOfParameter == 212:
            return 'Upward long-wave radiation flux'

        if table2Version == 200 and indicatorOfParameter == 205:
            return 'Downward long-wave radiation flux'

        if table2Version == 200 and indicatorOfParameter == 211:
            return 'Upward short-wave radiation flux'

        if table2Version == 200 and indicatorOfParameter == 204:
            return 'Downward short-wave radiation flux'

        if table2Version == 200 and indicatorOfParameter == 219:
            return 'Maximum wind speed'

        if table2Version == 200 and indicatorOfParameter == 78:
            return 'Convective snow'

        if table2Version == 200 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre specific humidity'

        if table2Version == 200 and indicatorOfParameter == 123:
            return 'Boundary layer dissipation'

        if table2Version == 200 and indicatorOfParameter == 122:
            return 'Sensible heat flux'

        if table2Version == 200 and indicatorOfParameter == 121:
            return 'Latent heat flux'

        if table2Version == 200 and indicatorOfParameter == 79:
            return 'Large scale snow'

        if table2Version == 200 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 200 and indicatorOfParameter == 74:
            return 'Medium cloud cover'

        if table2Version == 200 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 200 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 200 and indicatorOfParameter == 66:
            return 'Snow depth'

        if table2Version == 200 and indicatorOfParameter == 229:
            return 'Specific cloud ice water content'

        if table2Version == 200 and indicatorOfParameter == 118:
            return 'Brightness temperature'

        if table2Version == 200 and indicatorOfParameter == 83:
            return 'Surface roughness'

        if table2Version == 200 and indicatorOfParameter == 81:
            return 'Land-sea mask'

        if table2Version == 200 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2 metre temperature'

        topLevel = h.get_l('topLevel')

        if table2Version == 200 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and topLevel == 10:
            return '10 metre V wind component'

        if table2Version == 200 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return '10 metre U wind component'

        if table2Version == 200 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 200 and indicatorOfParameter == 7:
            return 'Geopotential Height'

        if table2Version == 200 and indicatorOfParameter == 44:
            return 'Divergence'

        if table2Version == 200 and indicatorOfParameter == 2:
            return 'Mean sea level pressure'

        if table2Version == 200 and indicatorOfParameter == 43:
            return 'Vorticity (relative)'

        if table2Version == 200 and indicatorOfParameter == 54:
            return 'Total column water vapour'

        if table2Version == 200 and indicatorOfParameter == 39:
            return 'Vertical velocity'

        if table2Version == 200 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Surface pressure'

        if table2Version == 200 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 200 and indicatorOfParameter == 34:
            return 'V component of wind'

        if table2Version == 200 and indicatorOfParameter == 33:
            return 'U component of wind'

        if table2Version == 200 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 200 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 200 and indicatorOfParameter == 58:
            return 'Total column cloud ice water'

        if table2Version == 200 and indicatorOfParameter == 227:
            return 'Total column cloud liquid water'

        if table2Version == 200 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 200 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 200 and indicatorOfParameter == 37:
            return 'Montgomery potential'

        if table2Version == 200 and indicatorOfParameter == 91:
            return 'Sea ice area fraction'

        if table2Version == 200 and indicatorOfParameter == 32:
            return 'Wind speed'

        if table2Version == 200 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 200 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 200 and indicatorOfParameter == 35:
            return 'Stream function'

    return wrapped
