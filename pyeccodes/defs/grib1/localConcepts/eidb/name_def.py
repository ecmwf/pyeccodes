import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 253 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 253 and indicatorOfParameter == 254:
            return 'Surface aerosol desert'

        if table2Version == 253 and indicatorOfParameter == 253:
            return 'Surface aerosol soot (carbon)'

        if table2Version == 253 and indicatorOfParameter == 252:
            return 'Surface aerosol land'

        if table2Version == 253 and indicatorOfParameter == 251:
            return 'Surface aerosol sea'

        if table2Version == 253 and indicatorOfParameter == 250:
            return 'C Ozone'

        if table2Version == 253 and indicatorOfParameter == 249:
            return 'B Ozone'

        if table2Version == 253 and indicatorOfParameter == 248:
            return 'A Ozone'

        if table2Version == 253 and indicatorOfParameter == 247:
            return 'Snow history'

        if table2Version == 253 and indicatorOfParameter == 246:
            return 'Snow Sublimation'

        if table2Version == 253 and indicatorOfParameter == 245:
            return 'Water evaporation'

        if table2Version == 253 and indicatorOfParameter == 244:
            return 'Latent Heat Sublimation'

        if table2Version == 253 and indicatorOfParameter == 243:
            return 'Duration of total precipitation'

        if table2Version == 253 and indicatorOfParameter == 242:
            return 'Maximum relative moisture at 2 meters'

        if table2Version == 253 and indicatorOfParameter == 241:
            return 'Minimum relative moisture at 2 meters'

        if table2Version == 253 and indicatorOfParameter == 240:
            return 'Resistance to evapotransiration'

        if table2Version == 253 and indicatorOfParameter == 239:
            return 'Thermal roughness length * g'

        if table2Version == 253 and indicatorOfParameter == 238:
            return 'Soil wetness'

        if table2Version == 253 and indicatorOfParameter == 237:
            return 'Soil depth'

        if table2Version == 253 and indicatorOfParameter == 236:
            return 'Maximum soil depth'

        if table2Version == 253 and indicatorOfParameter == 235:
            return 'Surface emissivity'

        if table2Version == 253 and indicatorOfParameter == 234:
            return 'Dominant vegetation index'

        if table2Version == 253 and indicatorOfParameter == 232:
            return 'Leaf area index'

        if table2Version == 253 and indicatorOfParameter == 231:
            return 'Stomatal minimum resistance'

        if table2Version == 253 and indicatorOfParameter == 230:
            return 'Albedo of vegetation'

        if table2Version == 253 and indicatorOfParameter == 229:
            return 'Albedo of bare ground'

        if table2Version == 253 and indicatorOfParameter == 228:
            return 'Gust'

        if table2Version == 253 and indicatorOfParameter == 227:
            return 'Maximum - of vegetation'

        if table2Version == 253 and indicatorOfParameter == 226:
            return 'Fraction of sand within soil'

        if table2Version == 253 and indicatorOfParameter == 225:
            return 'Fraction of clay within soil'

        if table2Version == 253 and indicatorOfParameter == 224:
            return 'Roughness length for vegetation * g'

        if table2Version == 253 and indicatorOfParameter == 223:
            return 'Roughness length of bare surface * g'

        if table2Version == 253 and indicatorOfParameter == 222:
            return 'Direction of main axis of topography'

        if table2Version == 253 and indicatorOfParameter == 221:
            return 'Anisotropy coeff of topography'

        if table2Version == 253 and indicatorOfParameter == 220:
            return 'Standard deviation of orography * g'

        if table2Version == 253 and indicatorOfParameter == 219:
            return 'Surface albedo for non snow covered areas'

        if table2Version == 253 and indicatorOfParameter == 217:
            return 'Downdraft mesh fraction'

        if table2Version == 253 and indicatorOfParameter == 216:
            return 'Updraft mesh fraction'

        if table2Version == 253 and indicatorOfParameter == 215:
            return 'Downdraft omega'

        if table2Version == 253 and indicatorOfParameter == 214:
            return 'Updraft omega'

        if table2Version == 253 and indicatorOfParameter == 213:
            return 'Vertical Divergence'

        if table2Version == 253 and indicatorOfParameter == 212:
            return 'Pressure departure'

        if table2Version == 253 and indicatorOfParameter == 211:
            return 'Lightning'

        if table2Version == 253 and indicatorOfParameter == 210:
            return 'Simulated reflectivity'

        if table2Version == 253 and indicatorOfParameter == 204:
            return 'Hail'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'Graupel'

        if table2Version == 253 and indicatorOfParameter == 200:
            return 'TKE'

        if table2Version == 253 and indicatorOfParameter == 196:
            return 'Gravity wave stress V-comp'

        if table2Version == 253 and indicatorOfParameter == 195:
            return 'Gravity wave stress U-comp'

        if table2Version == 253 and indicatorOfParameter == 193:
            return 'Soil ice'

        if table2Version == 253 and indicatorOfParameter == 192:
            return 'Water on canopy (Interception content)'

        if table2Version == 253 and indicatorOfParameter == 191:
            return 'Snow density'

        if table2Version == 253 and indicatorOfParameter == 190:
            return 'Snow albedo'

        if table2Version == 253 and indicatorOfParameter == 188:
            return 'Fraction of urban land'

        if table2Version == 253 and indicatorOfParameter == 187:
            return 'Cloud top'

        if table2Version == 253 and indicatorOfParameter == 186:
            return 'Cloud base'

        if table2Version == 253 and indicatorOfParameter == 185:
            return 'Total solid precipitation'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'Snow'

        if table2Version == 253 and indicatorOfParameter == 183:
            return 'Convective rain'

        if table2Version == 253 and indicatorOfParameter == 182:
            return 'Stratiform rain'

        if table2Version == 253 and indicatorOfParameter == 181:
            return 'Rain'

        if table2Version == 253 and indicatorOfParameter == 175:
            return 'Brightness temperature WV cloud'

        if table2Version == 253 and indicatorOfParameter == 174:
            return 'Brightness temperature WV clear'

        if table2Version == 253 and indicatorOfParameter == 173:
            return 'Brightness temperature IR cloud'

        if table2Version == 253 and indicatorOfParameter == 172:
            return 'Brightness temperature IR clear'

        if table2Version == 253 and indicatorOfParameter == 171:
            return 'Brightness temperature OZ cloud'

        if table2Version == 253 and indicatorOfParameter == 170:
            return 'Brightness temperature OZ clear'

        if table2Version == 253 and indicatorOfParameter == 167:
            return 'Total water vapour'

        if table2Version == 253 and indicatorOfParameter == 166:
            return 'MOCON out of the model'

        if table2Version == 253 and indicatorOfParameter == 163:
            return 'Gust, v-component'

        if table2Version == 253 and indicatorOfParameter == 162:
            return 'Gust, u-component'

        if table2Version == 253 and indicatorOfParameter == 161:
            return 'AROME hail diagnostic'

        if table2Version == 253 and indicatorOfParameter == 160:
            return 'CAPE out of the model'

        if table2Version == 253 and indicatorOfParameter == 158:
            return 'Surface downward moon radiation'

        if table2Version == 253 and indicatorOfParameter == 144:
            return 'Precipitation Type'

        if table2Version == 253 and indicatorOfParameter == 140:
            return 'Direct normal irradiance'

        if table2Version == 253 and indicatorOfParameter == 139:
            return 'Pseudo satellite image: cloud water reflectivity (visible)'

        if table2Version == 253 and indicatorOfParameter == 138:
            return 'Pseudo satellite image: water vapour Tb + correction for clouds'

        if table2Version == 253 and indicatorOfParameter == 137:
            return 'Pseudo satellite image: water vapour Tb'

        if table2Version == 253 and indicatorOfParameter == 136:
            return 'Pseudo satellite image: cloud top temperature (infrared)'

        if table2Version == 253 and indicatorOfParameter == 135:
            return 'Icing index'

        if table2Version == 253 and indicatorOfParameter == 133:
            return 'Mask of significant cloud amount'

        if table2Version == 253 and indicatorOfParameter == 132:
            return 'Latent heat flux through evaporation'

        if table2Version == 253 and indicatorOfParameter == 131:
            return 'LW net clear sky rad'

        if table2Version == 253 and indicatorOfParameter == 130:
            return 'SW net clear sky rad'

        if table2Version == 253 and indicatorOfParameter == 129:
            return 'Forecast RMS of PHI (CANARI)'

        if table2Version == 253 and indicatorOfParameter == 128:
            return 'Analysed RMS of PHI (CANARI)'

        if table2Version == 253 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 253 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 253 and indicatorOfParameter == 125:
            return 'Momentum flux, v-component'

        if table2Version == 253 and indicatorOfParameter == 124:
            return 'Momentum flux, u-component'

        if table2Version == 253 and indicatorOfParameter == 123:
            return 'Boundary layer dissipation'

        if table2Version == 253 and indicatorOfParameter == 122:
            return 'Sensible heat flux'

        if table2Version == 253 and indicatorOfParameter == 121:
            return 'Latent heat flux'

        if table2Version == 253 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 253 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 253 and indicatorOfParameter == 118:
            return 'Brightness temperature'

        if table2Version == 253 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 253 and indicatorOfParameter == 116:
            return 'Short-wave radiation flux'

        if table2Version == 253 and indicatorOfParameter == 115:
            return 'Long-wave radiation flux'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'Net long-wave radiation flux (atmosph.top)'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'Net short-wave radiation flux (atmosph.top)'

        if table2Version == 253 and indicatorOfParameter == 112:
            return 'Net long-wave radiation flux (surface)'

        if table2Version == 253 and indicatorOfParameter == 111:
            return 'Net short-wave radiation flux (surface)'

        if table2Version == 253 and indicatorOfParameter == 110:
            return 'Secondary wave mean period'

        if table2Version == 253 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 253 and indicatorOfParameter == 108:
            return 'Mean period of primary swell'

        if table2Version == 253 and indicatorOfParameter == 107:
            return 'Mean direction of primary swell'

        if table2Version == 253 and indicatorOfParameter == 106:
            return 'Mean period of swell waves'

        if table2Version == 253 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 253 and indicatorOfParameter == 104:
            return 'Direction of swell waves'

        if table2Version == 253 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 253 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 253 and indicatorOfParameter == 101:
            return 'Mean direction of wind waves'

        if table2Version == 253 and indicatorOfParameter == 100:
            return 'Signific.height,combined wind waves+swell'

        if table2Version == 253 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 253 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 253 and indicatorOfParameter == 97:
            return 'Ice growth rate'

        if table2Version == 253 and indicatorOfParameter == 96:
            return 'V-component of ice drift'

        if table2Version == 253 and indicatorOfParameter == 95:
            return 'U-component of ice drift'

        if table2Version == 253 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 253 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 253 and indicatorOfParameter == 92:
            return 'Ice thickness'

        if table2Version == 253 and indicatorOfParameter == 91:
            return 'Ice cover (1=land, 0=sea)'

        if table2Version == 253 and indicatorOfParameter == 90:
            return 'Water run-off'

        if table2Version == 253 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 253 and indicatorOfParameter == 88:
            return 'Salinity'

        if table2Version == 253 and indicatorOfParameter == 87:
            return 'Vegetation'

        if table2Version == 253 and indicatorOfParameter == 86:
            return 'Soil moisture content'

        if table2Version == 253 and indicatorOfParameter == 85:
            return 'Soil temperature'

        if table2Version == 253 and indicatorOfParameter == 84:
            return 'Albedo'

        if table2Version == 253 and indicatorOfParameter == 83:
            return 'Surface roughness'

        if table2Version == 253 and indicatorOfParameter == 82:
            return 'Deviation of sea-level from mean'

        if table2Version == 253 and indicatorOfParameter == 81:
            return 'Land cover (1=land, 0=sea)'

        if table2Version == 253 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 253 and indicatorOfParameter == 79:
            return 'Large scale snowfall'

        if table2Version == 253 and indicatorOfParameter == 78:
            return 'Convective snowfall'

        if table2Version == 253 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 253 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 253 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 253 and indicatorOfParameter == 74:
            return 'Medium cloud cover'

        if table2Version == 253 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 253 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 253 and indicatorOfParameter == 71:
            return 'Total cloud cover'

        if table2Version == 253 and indicatorOfParameter == 70:
            return 'Main thermocline anomaly'

        if table2Version == 253 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 253 and indicatorOfParameter == 68:
            return 'Transient thermocline depth'

        if table2Version == 253 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 253 and indicatorOfParameter == 66:
            return 'Snow depth'

        if table2Version == 253 and indicatorOfParameter == 65:
            return 'Water equivalent of accumulated snow depth'

        if table2Version == 253 and indicatorOfParameter == 64:
            return 'Snow fall rate water equivalent'

        if table2Version == 253 and indicatorOfParameter == 63:
            return 'Convective precipitation (water)'

        if table2Version == 253 and indicatorOfParameter == 62:
            return 'Large scale precipitation'

        if table2Version == 253 and indicatorOfParameter == 61:
            return 'Total precipitation'

        if table2Version == 253 and indicatorOfParameter == 60:
            return 'Thunderstorm probability'

        if table2Version == 253 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 253 and indicatorOfParameter == 58:
            return 'Cloud ice'

        if table2Version == 253 and indicatorOfParameter == 57:
            return 'Evaporation'

        if table2Version == 253 and indicatorOfParameter == 56:
            return 'Saturation deficit'

        if table2Version == 253 and indicatorOfParameter == 55:
            return 'Vapour pressure'

        if table2Version == 253 and indicatorOfParameter == 54:
            return 'Precipitable water'

        if table2Version == 253 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 253 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 253 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 253 and indicatorOfParameter == 50:
            return 'V-component of current'

        if table2Version == 253 and indicatorOfParameter == 49:
            return 'U-component of current'

        if table2Version == 253 and indicatorOfParameter == 48:
            return 'Speed of current'

        if table2Version == 253 and indicatorOfParameter == 47:
            return 'Direction of current'

        if table2Version == 253 and indicatorOfParameter == 46:
            return 'Vertical v-component shear'

        if table2Version == 253 and indicatorOfParameter == 45:
            return 'Vertical u-component shear'

        if table2Version == 253 and indicatorOfParameter == 44:
            return 'Relative divergence'

        if table2Version == 253 and indicatorOfParameter == 43:
            return 'Relative vorticity'

        if table2Version == 253 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 253 and indicatorOfParameter == 41:
            return 'Absolute vorticity'

        if table2Version == 253 and indicatorOfParameter == 40:
            return 'Vertical velocity'

        if table2Version == 253 and indicatorOfParameter == 39:
            return 'Pressure Vertical velocity'

        if table2Version == 253 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 253 and indicatorOfParameter == 37:
            return 'Montgomery stream function'

        if table2Version == 253 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 253 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 253 and indicatorOfParameter == 34:
            return 'v-component of wind'

        if table2Version == 253 and indicatorOfParameter == 33:
            return 'u-component of wind'

        if table2Version == 253 and indicatorOfParameter == 32:
            return 'Wind speed'

        if table2Version == 253 and indicatorOfParameter == 31:
            return 'Wind direction'

        if table2Version == 253 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 253 and indicatorOfParameter == 29:
            return 'Wave spectra (2)'

        if table2Version == 253 and indicatorOfParameter == 28:
            return 'Wave spectra (1)'

        if table2Version == 253 and indicatorOfParameter == 27:
            return 'Geopotential height anomaly'

        if table2Version == 253 and indicatorOfParameter == 26:
            return 'Pressure anomaly'

        if table2Version == 253 and indicatorOfParameter == 25:
            return 'Temperature anomaly'

        if table2Version == 253 and indicatorOfParameter == 24:
            return 'Parcel lifted index (to 500 hPa)'

        if table2Version == 253 and indicatorOfParameter == 23:
            return 'Radar spectra (3)'

        if table2Version == 253 and indicatorOfParameter == 22:
            return 'Radar spectra (2)'

        if table2Version == 253 and indicatorOfParameter == 21:
            return 'Radar spectra (1)'

        if table2Version == 253 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 253 and indicatorOfParameter == 19:
            return 'Lapse rate'

        if table2Version == 253 and indicatorOfParameter == 18:
            return 'Dew point depression (or deficit)'

        if table2Version == 253 and indicatorOfParameter == 17:
            return 'Dew point temperature'

        if table2Version == 253 and indicatorOfParameter == 16:
            return 'Minimum temperature'

        if table2Version == 253 and indicatorOfParameter == 15:
            return 'Maximum temperature'

        if table2Version == 253 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential temperature'

        if table2Version == 253 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 253 and indicatorOfParameter == 12:
            return 'Virtual potential temperature'

        if table2Version == 253 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 253 and indicatorOfParameter == 10:
            return 'Total column ozone'

        if table2Version == 253 and indicatorOfParameter == 9:
            return 'Standard deviation of height'

        if table2Version == 253 and indicatorOfParameter == 8:
            return 'Geometrical height'

        if table2Version == 253 and indicatorOfParameter == 7:
            return 'Geopotential height'

        if table2Version == 253 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 253 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 253 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 253 and indicatorOfParameter == 3:
            return 'Pressure tendency'

        if table2Version == 253 and indicatorOfParameter == 2:
            return 'Mean sea level pressure'

        if table2Version == 253 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 1 and indicatorOfParameter == 228:
            return 'Max wind gust'

        if table2Version == 1 and indicatorOfParameter == 209:
            return 'Standard deviation of smallest scale orography'

        if table2Version == 1 and indicatorOfParameter == 208:
            return 'Maximum slope of smallest scale orography'

        if table2Version == 1 and indicatorOfParameter == 200:
            return 'Turbulent Kinetic Energy'

        if table2Version == 1 and indicatorOfParameter == 199:
            return 'Vegetation type (Olsson land use)'

        if table2Version == 1 and indicatorOfParameter == 198:
            return 'Fraction of open land'

        if table2Version == 1 and indicatorOfParameter == 197:
            return 'Fraction of forest'

        if table2Version == 1 and indicatorOfParameter == 196:
            return 'Fraction of lake'

        if table2Version == 1 and indicatorOfParameter == 195:
            return 'Soil type code'

        if table2Version == 1 and indicatorOfParameter == 193:
            return 'Surface soil ice'

        if table2Version == 1 and indicatorOfParameter == 192:
            return 'Water on canopy level'

        if table2Version == 1 and indicatorOfParameter == 191:
            return 'Snow density'

        if table2Version == 1 and indicatorOfParameter == 190:
            return 'Snow albedo'

        if table2Version == 1 and indicatorOfParameter == 167:
            return 'Fraction of aspect'

        if table2Version == 1 and indicatorOfParameter == 166:
            return 'Sky wiew factor'

        if table2Version == 1 and indicatorOfParameter == 165:
            return 'Surface slope'

        if table2Version == 1 and indicatorOfParameter == 163:
            return 'Shadow parameter B'

        if table2Version == 1 and indicatorOfParameter == 162:
            return 'Shadow parameter A'

        if table2Version == 1 and indicatorOfParameter == 161:
            return 'Shadow fraction'

        if table2Version == 1 and indicatorOfParameter == 160:
            return 'Slope fraction'

        if table2Version == 1 and indicatorOfParameter == 143:
            return 'Dew point over land K'

        if table2Version == 1 and indicatorOfParameter == 142:
            return 'Relative humidity over land Fraction'

        if table2Version == 1 and indicatorOfParameter == 141:
            return 'Specific humidity over land'

        if table2Version == 1 and indicatorOfParameter == 140:
            return 'Temperature over land'

        if table2Version == 1 and indicatorOfParameter == 135:
            return 'Max wind speed (at 10m)'

        if table2Version == 1 and indicatorOfParameter == 128:
            return 'Momentum flux'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'Momentum flux, v-component'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'Momentum flux, u-component'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'Boundary layer dissipation'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'Sensible heat flux'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'Latent heat flux'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'Brightness temperature'

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'Short-wave radiation flux'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'Long-wave radiation flux'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'Net long-wave radiation flux (atmosph.top)'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'Net short-wave radiation flux (atmosph.top)'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'Net long-wave radiation flux (surface)'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'Net short-wave radiation flux (surface)'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 'Secondary wave mean period'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 1 and indicatorOfParameter == 108:
            return 'Mean period of primary swell'

        if table2Version == 1 and indicatorOfParameter == 107:
            return 'Mean direction of primary swell'

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
            return 'Mean Direction of wind waves'

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
            return 'Ice cover (1=land, 0=sea)'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'Water run-off'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 'Salinity'

        if table2Version == 1 and indicatorOfParameter == 87:
            return 'Vegetation'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'Soil moisture content'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'Soil temperature'

        if table2Version == 1 and indicatorOfParameter == 84:
            return 'Albedo'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'Surface roughness'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'Deviation of sea-level from mean'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'Land cover (1=land, 0=sea)'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'Large scale snowfall'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'Convective snowfall'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 1 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 1 and indicatorOfParameter == 74:
            return 'Medium cloud cover'

        if table2Version == 1 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 1 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 1 and indicatorOfParameter == 71:
            return 'Total cloud cover'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'Main thermocline anomaly'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'Transient thermocline depth'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'Snow depth'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'Water equivalent of accumulated snow depth'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'Snow fall rate water equivalent'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'Convective precipitation (water)'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'Large scale precipitation'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'Total precipitation'

        if table2Version == 1 and indicatorOfParameter == 60:
            return 'Thunderstorm probability'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 1 and indicatorOfParameter == 58:
            return 'Cloud ice'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'Evaporation'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'Saturation deficit'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'Vapour pressure'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'Precipitable water'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 1 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'Specific humidity'

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

        if table2Version == 1 and indicatorOfParameter == 44:
            return 'Relative divergence'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 'Relative vorticity'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 'Absolute vorticity'

        if table2Version == 1 and indicatorOfParameter == 40:
            return 'Vertical velocity'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'Pressure Vertical velocity'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'Montgomery stream function'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'v-component of wind'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'u-component of wind'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'Wind speed'

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

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'Virtual potential temperature'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'Total column ozone'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'Standard deviation of height'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'Geometrical height'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'Geopotential height'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'Pressure tendency'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'Mean sea level pressure'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 1 and indicatorOfParameter == 0:
            return 'Reserved'

    return wrapped
