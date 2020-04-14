import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 253 and indicatorOfParameter == 239:
            return 'Thermal roughness length * g '

        if table2Version == 253 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 253 and indicatorOfParameter == 161:
            return 'AROME hail diagnostic'

        if table2Version == 253 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 253 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 253 and indicatorOfParameter == 32:
            return 'Wind speed'

        if table2Version == 253 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 253 and indicatorOfParameter == 245:
            return 'Water evaporation'

        if table2Version == 253 and indicatorOfParameter == 31:
            return 'Wind direction'

        if table2Version == 253 and indicatorOfParameter == 193:
            return 'Water on canopy (Interception content)'

        if table2Version == 253 and indicatorOfParameter == 192:
            return 'Water on canopy (Interception content)'

        if table2Version == 253 and indicatorOfParameter == 39:
            return 'Vertical velocity'

        if table2Version == 253 and indicatorOfParameter == 46:
            return 'Vertical v-component shear'

        if table2Version == 253 and indicatorOfParameter == 45:
            return 'Vertical u-component shear'

        if table2Version == 253 and indicatorOfParameter == 12:
            return 'Virtual potential temperature'

        if table2Version == 253 and indicatorOfParameter == 55:
            return 'Vapour pressure'

        if table2Version == 253 and indicatorOfParameter == 43:
            return 'Vorticity (relative)'

        if table2Version == 253 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 253 and indicatorOfParameter == 96:
            return 'V-component of ice drift'

        if table2Version == 253 and indicatorOfParameter == 163:
            return 'Gust, v-component'

        if table2Version == 253 and indicatorOfParameter == 125:
            return 'Momentum flux, v-component'

        if table2Version == 253 and indicatorOfParameter == 87:
            return 'Vegetation fraction'

        if table2Version == 253 and indicatorOfParameter == 213:
            return 'Vertical Divergence'

        if table2Version == 253 and indicatorOfParameter == 50:
            return 'V-component of current '

        if table2Version == 253 and indicatorOfParameter == 34:
            return 'V component of wind'

        if table2Version == 253 and indicatorOfParameter == 214:
            return 'Updraft omega'

        if table2Version == 253 and indicatorOfParameter == 216:
            return 'Updraft mesh fraction'

        if table2Version == 253 and indicatorOfParameter == 95:
            return 'U-component of ice drift'

        if table2Version == 253 and indicatorOfParameter == 162:
            return 'Gust, u-component'

        if table2Version == 253 and indicatorOfParameter == 124:
            return 'Momentum flux, u-component'

        if table2Version == 253 and indicatorOfParameter == 49:
            return 'U-component of current '

        if table2Version == 253 and indicatorOfParameter == 33:
            return 'U component of wind'

        if table2Version == 253 and indicatorOfParameter == 40:
            return 'Vertical velocity'

        if table2Version == 253 and indicatorOfParameter == 68:
            return 'Transient thermocline depth'

        if table2Version == 253 and indicatorOfParameter == 60:
            return 'Thunderstorm probability'

        if table2Version == 253 and indicatorOfParameter == 185:
            return 'Total solid precipitation'

        if table2Version == 253 and indicatorOfParameter == 61:
            return 'Total precipitation'

        if table2Version == 253 and indicatorOfParameter == 167:
            return 'Total water vapour'

        if table2Version == 253 and indicatorOfParameter == 16:
            return 'Minimum temperature'

        if table2Version == 253 and indicatorOfParameter == 15:
            return 'Maximum temperature'

        if table2Version == 253 and indicatorOfParameter == 200:
            return 'TKE'

        if table2Version == 253 and indicatorOfParameter == 17:
            return 'Dew point temperature'

        if table2Version == 253 and indicatorOfParameter == 10:
            return 'Total column ozone'

        if table2Version == 253 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 253 and indicatorOfParameter == 25:
            return 'Temperature anomaly'

        if table2Version == 253 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 253 and indicatorOfParameter == 238:
            return 'Soil wetness'

        if table2Version == 253 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 253 and indicatorOfParameter == 106:
            return 'Mean period of swell waves'

        if table2Version == 253 and indicatorOfParameter == 110:
            return 'Secondary wave period'

        if table2Version == 253 and indicatorOfParameter == 100:
            return 'Signific.height,combined wind waves+swell'

        if table2Version == 253 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 253 and indicatorOfParameter == 104:
            return 'Direction of swell waves'

        if table2Version == 253 and indicatorOfParameter == 116:
            return 'Short wave radiation flux'

        if table2Version == 253 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 253 and indicatorOfParameter == 220:
            return 'Standard deviation of orography * g '

        if table2Version == 253 and indicatorOfParameter == 122:
            return 'Surface sensible heat flux'

        if table2Version == 253 and indicatorOfParameter == 64:
            return 'Snow fall rate water equivalent'

        if table2Version == 253 and indicatorOfParameter == 83:
            return 'Surface roughness * g'

        if table2Version == 253 and indicatorOfParameter == 182:
            return 'Stratiform rain'

        if table2Version == 253 and indicatorOfParameter == 48:
            return 'Speed of current'

        if table2Version == 253 and indicatorOfParameter == 246:
            return 'Snow Sublimation'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'Snow'

        if table2Version == 253 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 253 and indicatorOfParameter == 231:
            return 'Stomatal minimum resistance '

        if table2Version == 253 and indicatorOfParameter == 86:
            return 'Soil Moisture'

        if table2Version == 253 and indicatorOfParameter == 85:
            return 'Soil Temperature'

        if table2Version == 253 and indicatorOfParameter == 121:
            return 'Surface latent heat flux'

        if table2Version == 253 and indicatorOfParameter == 226:
            return 'Fraction of sand within soil '

        if table2Version == 253 and indicatorOfParameter == 237:
            return 'Soil depth'

        if table2Version == 253 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 253 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 253 and indicatorOfParameter == 247:
            return 'Snow history'

        if table2Version == 253 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 253 and indicatorOfParameter == 65:
            return 'Snow Fall water equivalent'

        if table2Version == 253 and indicatorOfParameter == 235:
            return 'Surface emissivity '

        if table2Version == 253 and indicatorOfParameter == 66:
            return 'Snow depth water equivalent'

        if table2Version == 253 and indicatorOfParameter == 56:
            return 'Saturation deficit'

        if table2Version == 253 and indicatorOfParameter == 88:
            return 'Salinity'

        if table2Version == 253 and indicatorOfParameter == 191:
            return 'Snow density'

        if table2Version == 253 and indicatorOfParameter == 90:
            return 'Runoff'

        if table2Version == 253 and indicatorOfParameter == 242:
            return 'Maximum relative moisture at 2 meters'

        if table2Version == 253 and indicatorOfParameter == 241:
            return 'Minimum relative moisture at 2 meters'

        if table2Version == 253 and indicatorOfParameter == 240:
            return 'Resistance to evapotransiration '

        if table2Version == 253 and indicatorOfParameter == 210:
            return 'Simulated reflectivity '

        if table2Version == 253 and indicatorOfParameter == 23:
            return 'Radar spectra (3)'

        if table2Version == 253 and indicatorOfParameter == 181:
            return 'Rain'

        if table2Version == 253 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 253 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 253 and indicatorOfParameter == 54:
            return 'Precipitable water'

        if table2Version == 253 and indicatorOfParameter == 4:
            return 'Potential vorticity'

        if table2Version == 253 and indicatorOfParameter == 3:
            return 'Pressure tendency'

        if table2Version == 253 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 253 and indicatorOfParameter == 138:
            return 'Pseudo satellite image: water vapour Tb + correction for clouds'

        if table2Version == 253 and indicatorOfParameter == 137:
            return 'Pseudo satellite image: water vapour Tb'

        if table2Version == 253 and indicatorOfParameter == 139:
            return 'Pseudo satellite image: cloud water reflectivity (visible)'

        if table2Version == 253 and indicatorOfParameter == 136:
            return 'Pseudo satellite image: cloud top temperature (infrared)'

        if table2Version == 253 and indicatorOfParameter == 144:
            return 'Precipitation Type'

        if table2Version == 253 and indicatorOfParameter == 26:
            return 'Pressure anomaly'

        if table2Version == 253 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 253 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 253 and indicatorOfParameter == 24:
            return 'Parcel lifted index (to 500 hPa)'

        if table2Version == 253 and indicatorOfParameter == 212:
            return 'Pressure departure'

        if table2Version == 253 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential temperature'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'Net short-wave radiationflux(atmosph.top)'

        if table2Version == 253 and indicatorOfParameter == 111:
            return 'Net short-wave radiation flux (surface)'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'Net long-wave radiation flux(atmosph.top)'

        if table2Version == 253 and indicatorOfParameter == 112:
            return 'Net long-wave radiation flux (surface)'

        if table2Version == 253 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 253 and indicatorOfParameter == 70:
            return 'Main thermocline anomaly'

        if table2Version == 253 and indicatorOfParameter == 2:
            return 'Mean sea level pressure'

        if table2Version == 253 and indicatorOfParameter == 133:
            return 'Mask of significant cloud amount'

        if table2Version == 253 and indicatorOfParameter == 158:
            return 'Surface downward moon radiation'

        if table2Version == 253 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 253 and indicatorOfParameter == 108:
            return 'Mean period of primary swell'

        if table2Version == 253 and indicatorOfParameter == 37:
            return 'Montgomery stream Function'

        if table2Version == 253 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 253 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 253 and indicatorOfParameter == 101:
            return 'Mean direction of wind waves'

        if table2Version == 253 and indicatorOfParameter == 107:
            return 'Mean direction of primary swell'

        if table2Version == 253 and indicatorOfParameter == 166:
            return 'MOCON out of the model '

        if table2Version == 253 and indicatorOfParameter == 74:
            return 'Medium cloud cover'

        if table2Version == 253 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 253 and indicatorOfParameter == 115:
            return 'Long wave radiation flux'

        if table2Version == 253 and indicatorOfParameter == 62:
            return 'large scale precipitation (water)'

        if table2Version == 253 and indicatorOfParameter == 81:
            return 'Land-sea mask'

        if table2Version == 253 and indicatorOfParameter == 79:
            return 'Large-scale snowfall'

        if table2Version == 253 and indicatorOfParameter == 244:
            return 'Latent Heat Sublimation'

        if table2Version == 253 and indicatorOfParameter == 132:
            return 'Latent heat flux through evaporation'

        if table2Version == 253 and indicatorOfParameter == 209:
            return 'Lightning'

        if table2Version == 253 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 253 and indicatorOfParameter == 19:
            return 'Lapse rate'

        if table2Version == 253 and indicatorOfParameter == 232:
            return 'Leaf area index '

        if table2Version == 253 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 253 and indicatorOfParameter == 92:
            return 'Ice thickness'

        if table2Version == 253 and indicatorOfParameter == 135:
            return 'Icing index'

        if table2Version == 253 and indicatorOfParameter == 97:
            return 'Ice growth rate'

        if table2Version == 253 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 253 and indicatorOfParameter == 91:
            return 'Ice cover (1=land, 0=sea)'

        if table2Version == 253 and indicatorOfParameter == 5:
            return 'ICAO Standard Atmosphere reference height'

        if table2Version == 253 and indicatorOfParameter == 9:
            return 'Standard deviation of height'

        if table2Version == 253 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 253 and indicatorOfParameter == 204:
            return 'Hail'

        if table2Version == 253 and indicatorOfParameter == 8:
            return 'Geometrical height'

        if table2Version == 253 and indicatorOfParameter == 196:
            return 'Gravity wave stress V-comp'

        if table2Version == 253 and indicatorOfParameter == 195:
            return 'Gravity wave stress U-comp'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'Graupel'

        if table2Version == 253 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 253 and indicatorOfParameter == 27:
            return 'Geopotential height anomaly'

        if table2Version == 253 and indicatorOfParameter == 7:
            return 'Geopotential Height'

        if table2Version == 253 and indicatorOfParameter == 188:
            return 'Fraction of urban land'

        if table2Version == 253 and indicatorOfParameter == 129:
            return 'Forecast RMS of PHI (CANARI)'

        if table2Version == 253 and indicatorOfParameter == 228:
            return 'Gust'

        if table2Version == 253 and indicatorOfParameter == 57:
            return 'Evaporation'

        if table2Version == 253 and indicatorOfParameter == 234:
            return 'Dominant vegetation index '

        if table2Version == 253 and indicatorOfParameter == 243:
            return 'Duration of total precipitation'

        if table2Version == 253 and indicatorOfParameter == 222:
            return 'Direction of main axis of topography '

        if table2Version == 253 and indicatorOfParameter == 82:
            return 'Deviation of sea-level from mean'

        if table2Version == 253 and indicatorOfParameter == 215:
            return 'Downdraft omega'

        if table2Version == 253 and indicatorOfParameter == 217:
            return 'Downdraft mesh fraction'

        if table2Version == 253 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 253 and indicatorOfParameter == 47:
            return 'Direction of current'

        if table2Version == 253 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 253 and indicatorOfParameter == 18:
            return 'Dew point depression (or deficit)'

        if table2Version == 253 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 253 and indicatorOfParameter == 44:
            return 'Divergence'

        if table2Version == 253 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 253 and indicatorOfParameter == 187:
            return 'Cloud top'

        if table2Version == 253 and indicatorOfParameter == 130:
            return 'SW net clear sky rad'

        if table2Version == 253 and indicatorOfParameter == 131:
            return 'LW net clear sky rad'

        if table2Version == 253 and indicatorOfParameter == 78:
            return 'Convective snowfall'

        if table2Version == 253 and indicatorOfParameter == 183:
            return 'Convective rain'

        if table2Version == 253 and indicatorOfParameter == 250:
            return 'C Ozone'

        if table2Version == 253 and indicatorOfParameter == 225:
            return 'Fraction of clay within soil '

        if table2Version == 253 and indicatorOfParameter == 58:
            return 'Cloud ice water content'

        if table2Version == 253 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 253 and indicatorOfParameter == 186:
            return 'Cloud base'

        if table2Version == 253 and indicatorOfParameter == 160:
            return 'CAPE out of the model'

        if table2Version == 253 and indicatorOfParameter == 118:
            return 'Brightness temperature'

        if table2Version == 253 and indicatorOfParameter == 249:
            return 'B Ozone'

        if table2Version == 253 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hPa)'

        if table2Version == 253 and indicatorOfParameter == 123:
            return 'Boundary layer dissipation'

        if table2Version == 253 and indicatorOfParameter == 221:
            return 'Anisotropy coeff of topography '

        if table2Version == 253 and indicatorOfParameter == 190:
            return 'Snow albedo'

        if table2Version == 253 and indicatorOfParameter == 128:
            return 'Analysed RMS of PHI (CANARI)'

        if table2Version == 253 and indicatorOfParameter == 248:
            return 'A Ozone'

        if table2Version == 253 and indicatorOfParameter == 230:
            return 'Albedo of vegetation '

        if table2Version == 253 and indicatorOfParameter == 229:
            return 'Albedo of bare ground '

        if table2Version == 253 and indicatorOfParameter == 84:
            return 'Albedo'

        if table2Version == 253 and indicatorOfParameter == 251:
            return 'Surface aerosol sea'

        if table2Version == 253 and indicatorOfParameter == 252:
            return 'Surface aerosol land'

        if table2Version == 253 and indicatorOfParameter == 254:
            return 'Surface aerosol desert'

        if table2Version == 253 and indicatorOfParameter == 253:
            return 'Surface aerosol soot (carbon)'

        if table2Version == 253 and indicatorOfParameter == 63:
            return 'Convective precipitation (water)'

        if table2Version == 253 and indicatorOfParameter == 41:
            return 'Absolute vorticity'

        if table2Version == 253 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 151 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 151 and indicatorOfParameter == 57:
            return 'Evaporation Penman formula'

        if table2Version == 151 and indicatorOfParameter == 3:
            return 'Probability total precipitation more than 50 mm'

        if table2Version == 151 and indicatorOfParameter == 2:
            return 'Probability total precipitation between 10 and 50 mm'

        if table2Version == 151 and indicatorOfParameter == 1:
            return 'Probability total precipitation between 1 and 10 mm'

        if table2Version == 151 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 150 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 150 and indicatorOfParameter == 58:
            return 'Spray weather recomendation'

        if table2Version == 150 and indicatorOfParameter == 57:
            return 'Evaporation Penman formula'

        if table2Version == 150 and indicatorOfParameter == 0:
            return 'Reserved '

        if table2Version == 140 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 140 and indicatorOfParameter == 9:
            return 'Significant total discharge count (discharges with absolute peek current above 100kA)'

        if table2Version == 140 and indicatorOfParameter == 8:
            return 'Significant cloud to cloud discharge count (discharges with absolute peek current above 100kA)'

        if table2Version == 140 and indicatorOfParameter == 7:
            return 'Significant cloud to ground discharge count (discharges with absolute peek current above 100kA)'

        if table2Version == 140 and indicatorOfParameter == 6:
            return 'Total accumulated absolute peek current'

        if table2Version == 140 and indicatorOfParameter == 5:
            return 'Cloud to cloud accumulated absolute peek current'

        if table2Version == 140 and indicatorOfParameter == 4:
            return 'Cloud to ground accumulated absolute peek current'

        if table2Version == 140 and indicatorOfParameter == 3:
            return 'Total discharge count'

        if table2Version == 140 and indicatorOfParameter == 2:
            return 'Cloud to cloud discharge count'

        if table2Version == 140 and indicatorOfParameter == 1:
            return 'Cloud to ground discharge count'

        if table2Version == 140 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 137 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 137 and indicatorOfParameter == 137:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 136:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 135:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 134:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 133:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 132:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 131:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 130:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 127:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 126:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 125:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 124:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 123:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 122:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 121:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 120:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 117:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 116:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 115:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 114:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 113:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 112:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 111:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 110:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 107:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 106:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 105:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 104:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 103:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 102:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 101:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 100:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 77:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 76:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 75:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 74:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 73:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 72:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 71:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 70:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 67:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 66:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 65:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 64:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 63:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 62:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 61:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 60:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 57:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 56:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 55:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 54:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 53:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 52:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 51:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 50:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 47:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 46:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 45:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 44:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 43:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 42:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 41:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 40:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 37:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 36:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 35:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 34:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 33:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 32:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 31:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 30:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 27:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 26:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 25:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 24:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 23:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 22:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 21:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 20:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 17:
            return 'Concentration of SOX in air'

        if table2Version == 137 and indicatorOfParameter == 16:
            return 'Total deposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 15:
            return 'Wetdeposition of SOX, excluding seasalt'

        if table2Version == 137 and indicatorOfParameter == 14:
            return 'Drydeposition of SOX, excluding seasalt, Water'

        if table2Version == 137 and indicatorOfParameter == 13:
            return 'Drydeposition of SOX, excluding seasalt, Urban'

        if table2Version == 137 and indicatorOfParameter == 12:
            return 'Drydeposition of SOX, excluding seasalt, Mountain'

        if table2Version == 137 and indicatorOfParameter == 11:
            return 'Drydeposition of SOX, excluding seasalt, Wetland'

        if table2Version == 137 and indicatorOfParameter == 10:
            return 'Drydeposition of SOX, excluding seasalt, Pine'

        if table2Version == 137 and indicatorOfParameter == 7:
            return 'Drydeposition of SOX, excluding seasalt, Spruce'

        if table2Version == 137 and indicatorOfParameter == 6:
            return 'Drydeposition of SOX, excluding seasalt, Deciduous'

        if table2Version == 137 and indicatorOfParameter == 5:
            return 'Drydeposition of SOX, excluding seasalt, Beach Oak'

        if table2Version == 137 and indicatorOfParameter == 4:
            return 'Drydeposition of SOX, excluding seasalt, Arable'

        if table2Version == 137 and indicatorOfParameter == 3:
            return 'Drydeposition of SOX, excluding seasalt, Pasture'

        if table2Version == 137 and indicatorOfParameter == 2:
            return 'Drydeposition of SOX, excluding seasalt, mixed gound'

        if table2Version == 137 and indicatorOfParameter == 1:
            return 'Concentration of SOX, excluding seasalt, in air'

        if table2Version == 137 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 136 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 136 and indicatorOfParameter == 206:
            return 'Total ozone'

        if table2Version == 136 and indicatorOfParameter == 175:
            return 'Accumulated fresh snow, 1 hours'

        if table2Version == 136 and indicatorOfParameter == 165:
            return 'Accumulated precipitation, 1 hours'

        if table2Version == 136 and indicatorOfParameter == 120:
            return 'PAR'

        if table2Version == 136 and indicatorOfParameter == 119:
            return 'Sunshine duration'

        if table2Version == 136 and indicatorOfParameter == 118:
            return 'Beam normal irradiance'

        if table2Version == 136 and indicatorOfParameter == 117:
            return 'Global irradiance'

        if table2Version == 136 and indicatorOfParameter == 116:
            return 'CIE-weighted UV irradiance'

        if table2Version == 136 and indicatorOfParameter == 91:
            return 'Ice concentration'

        if table2Version == 136 and indicatorOfParameter == 84:
            return 'Albedo (lev 0=global radiation lev 1=UV radiation)'

        if table2Version == 136 and indicatorOfParameter == 79:
            return 'Significant cloud top'

        if table2Version == 136 and indicatorOfParameter == 78:
            return 'Significant cloud base'

        if table2Version == 136 and indicatorOfParameter == 77:
            return 'Probability for significant cloud base'

        if table2Version == 136 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 136 and indicatorOfParameter == 71:
            return 'Total cloud cover'

        if table2Version == 136 and indicatorOfParameter == 66:
            return 'Snow depth'

        if table2Version == 136 and indicatorOfParameter == 54:
            return 'Precipitable water'

        if table2Version == 136 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 136 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 136 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 136 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 135 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 135 and indicatorOfParameter == 254:
            return 'Natural logarithm of pressure in Pa'

        if table2Version == 135 and indicatorOfParameter == 253:
            return 'Anisotropy of sub-gridscale orography'

        if table2Version == 135 and indicatorOfParameter == 252:
            return 'Gravity wave dissipation'

        if table2Version == 135 and indicatorOfParameter == 251:
            return 'Slope of sub-gridscale orography'

        if table2Version == 135 and indicatorOfParameter == 250:
            return 'Angle of sub-gridscale orography'

        if table2Version == 135 and indicatorOfParameter == 249:
            return 'Standard deviation of sub-gridscale orography'

        if table2Version == 135 and indicatorOfParameter == 248:
            return '5-wave geopotential height anomaly'

        if table2Version == 135 and indicatorOfParameter == 247:
            return 'Planetary boundary layer height'

        if table2Version == 135 and indicatorOfParameter == 246:
            return 'Meridional flux of gravity wave stress'

        if table2Version == 135 and indicatorOfParameter == 245:
            return 'Zonal flux of gravity wave stress'

        if table2Version == 135 and indicatorOfParameter == 244:
            return '5-wave geopotential height'

        if table2Version == 135 and indicatorOfParameter == 243:
            return 'Density altitude'

        if table2Version == 135 and indicatorOfParameter == 242:
            return 'Pressure altitude'

        if table2Version == 135 and indicatorOfParameter == 241:
            return 'Thickness'

        if table2Version == 135 and indicatorOfParameter == 240:
            return 'Altimeter setting'

        if table2Version == 135 and indicatorOfParameter == 239:
            return 'Eta coordinate vertical velocity'

        if table2Version == 135 and indicatorOfParameter == 238:
            return 'Drag coefficient'

        if table2Version == 135 and indicatorOfParameter == 237:
            return 'v-component storm motion'

        if table2Version == 135 and indicatorOfParameter == 236:
            return 'u-component storm motion'

        if table2Version == 135 and indicatorOfParameter == 235:
            return 'Horizontal momentum flux'

        if table2Version == 135 and indicatorOfParameter == 234:
            return 'Vertical speed shear'

        if table2Version == 135 and indicatorOfParameter == 233:
            return 'v-component of wind (gust)'

        if table2Version == 135 and indicatorOfParameter == 232:
            return 'u-component of wind (gust)'

        if table2Version == 135 and indicatorOfParameter == 231:
            return 'Specific snow water content'

        if table2Version == 135 and indicatorOfParameter == 230:
            return 'Specific rain water content'

        if table2Version == 135 and indicatorOfParameter == 229:
            return 'Specific cloud ice water content'

        if table2Version == 135 and indicatorOfParameter == 228:
            return 'Specific cloud liquid water content'

        if table2Version == 135 and indicatorOfParameter == 227:
            return 'Ice pellets precipitation rate'

        if table2Version == 135 and indicatorOfParameter == 226:
            return 'Freezing rain precipitation rate'

        if table2Version == 135 and indicatorOfParameter == 225:
            return 'Snow precipitation rate'

        if table2Version == 135 and indicatorOfParameter == 224:
            return 'Rain precipitation rate'

        if table2Version == 135 and indicatorOfParameter == 223:
            return 'Total column integrated water vapour'

        if table2Version == 135 and indicatorOfParameter == 222:
            return 'Snow evaporation'

        if table2Version == 135 and indicatorOfParameter == 221:
            return 'Snow depth water equivalent'

        if table2Version == 135 and indicatorOfParameter == 220:
            return 'Large scale snowfall rate'

        if table2Version == 135 and indicatorOfParameter == 219:
            return 'Convective snowfall rate'

        if table2Version == 135 and indicatorOfParameter == 218:
            return 'Total snowfall rate'

        if table2Version == 135 and indicatorOfParameter == 217:
            return 'Large scale snowfall rate water equivalent'

        if table2Version == 135 and indicatorOfParameter == 216:
            return 'Convective snowfall rate water equivalent'

        if table2Version == 135 and indicatorOfParameter == 215:
            return 'Large scale precipitation rate'

        if table2Version == 135 and indicatorOfParameter == 214:
            return 'Total column water (Vertically integrated total water)'

        if table2Version == 135 and indicatorOfParameter == 213:
            return 'Total snow precipitation'

        if table2Version == 135 and indicatorOfParameter == 212:
            return 'Total water precipitation'

        if table2Version == 135 and indicatorOfParameter == 211:
            return 'Total column integrated snow'

        if table2Version == 135 and indicatorOfParameter == 210:
            return 'Total column integrated rain'

        if table2Version == 135 and indicatorOfParameter == 209:
            return 'Rain factor'

        if table2Version == 135 and indicatorOfParameter == 208:
            return 'Rain fraction of total cloud water'

        if table2Version == 135 and indicatorOfParameter == 171:
            return 'AOD-10000/Aerosol optical depth at 10000 nm'

        if table2Version == 135 and indicatorOfParameter == 170:
            return 'AOD-3500/Aerosol optical depth at 3500 nm'

        if table2Version == 135 and indicatorOfParameter == 169:
            return 'AOD-1064/Aerosol optical depth at 1064 nm'

        if table2Version == 135 and indicatorOfParameter == 168:
            return 'AOD-1020/Aerosol optical depth at 1020 nm'

        if table2Version == 135 and indicatorOfParameter == 167:
            return 'AOD-870/Aerosol optical depth at 870 nm'

        if table2Version == 135 and indicatorOfParameter == 166:
            return 'AOD-675/Aerosol optical depth at 675 nm'

        if table2Version == 135 and indicatorOfParameter == 165:
            return 'AOD-532/Aerosol optical depth at 532 nm'

        if table2Version == 135 and indicatorOfParameter == 164:
            return 'AOD-500/Aerosol optical depth at 500 nm'

        if table2Version == 135 and indicatorOfParameter == 163:
            return 'AOD-440/Aerosol optical depth at 440 nm'

        if table2Version == 135 and indicatorOfParameter == 162:
            return 'AOD-380/Aerosol optical depth at 380 nm'

        if table2Version == 135 and indicatorOfParameter == 161:
            return 'AOD-355/Aerosol optical depth at 355 nm'

        if table2Version == 135 and indicatorOfParameter == 160:
            return 'AOD-340/Aerosol optical depth at 340 nm'

        if table2Version == 135 and indicatorOfParameter == 151:
            return 'EXT-10000/Extinction at 10000 nm'

        if table2Version == 135 and indicatorOfParameter == 150:
            return 'EXT-3500/Extinction at 3500 nm'

        if table2Version == 135 and indicatorOfParameter == 149:
            return 'EXT-1064/Extinction at 1064 nm'

        if table2Version == 135 and indicatorOfParameter == 148:
            return 'EXT-1020/Extinction at 1020 nm'

        if table2Version == 135 and indicatorOfParameter == 147:
            return 'EXT-870/Extinction at 870 nm'

        if table2Version == 135 and indicatorOfParameter == 146:
            return 'EXT-675/Extinction at 675 nm'

        if table2Version == 135 and indicatorOfParameter == 145:
            return 'EXT-532/Extinction at 532 nm'

        if table2Version == 135 and indicatorOfParameter == 144:
            return 'EXT-500/Extinction at 500 nm'

        if table2Version == 135 and indicatorOfParameter == 143:
            return 'EXT-440/Extinction at 440 nm'

        if table2Version == 135 and indicatorOfParameter == 142:
            return 'EXT-380/Extinction at 380 nm'

        if table2Version == 135 and indicatorOfParameter == 141:
            return 'EXT-355/Extinction at 355 nm'

        if table2Version == 135 and indicatorOfParameter == 140:
            return 'EXT-340/Extinction at 340 nm'

        if table2Version == 135 and indicatorOfParameter == 131:
            return 'BSCA-10000/Backscatter at 10000 nm'

        if table2Version == 135 and indicatorOfParameter == 130:
            return 'BSCA-3500/Backscatter at 3500 nm'

        if table2Version == 135 and indicatorOfParameter == 129:
            return 'BSCA-1064/Backscatter at 1064 nm'

        if table2Version == 135 and indicatorOfParameter == 128:
            return 'BSCA-1020/Backscatter at 1020 nm'

        if table2Version == 135 and indicatorOfParameter == 127:
            return 'BSCA-870/Backscatter at 870 nm'

        if table2Version == 135 and indicatorOfParameter == 126:
            return 'BSCA-675/Backscatter at 675 nm'

        if table2Version == 135 and indicatorOfParameter == 125:
            return 'BSCA-532/Backscatter at 532 nm'

        if table2Version == 135 and indicatorOfParameter == 124:
            return 'BSCA-500/Backscatter at 500 nm'

        if table2Version == 135 and indicatorOfParameter == 123:
            return 'BSCA-440/Backscatter at 440 nm'

        if table2Version == 135 and indicatorOfParameter == 122:
            return 'BSCA-380/Backscatter at 380 nm'

        if table2Version == 135 and indicatorOfParameter == 121:
            return 'BSCA-355/Backscatter at 355 nm'

        if table2Version == 135 and indicatorOfParameter == 120:
            return 'BSCA-340/Backscatter at 340 nm'

        if table2Version == 135 and indicatorOfParameter == 111:
            return 'VIS-10000/Visibility at 10000 nm'

        if table2Version == 135 and indicatorOfParameter == 110:
            return 'VIS-3500/Visibility at 3500 nm'

        if table2Version == 135 and indicatorOfParameter == 109:
            return 'VIS-1064/Visibility at 1064 nm'

        if table2Version == 135 and indicatorOfParameter == 108:
            return 'VIS-1020/Visibility at 1020 nm'

        if table2Version == 135 and indicatorOfParameter == 107:
            return 'VIS-870/Visibility at 870 nm'

        if table2Version == 135 and indicatorOfParameter == 106:
            return 'VIS-675/Visibility at 675 nm'

        if table2Version == 135 and indicatorOfParameter == 105:
            return 'VIS-532/Visibility at 532 nm'

        if table2Version == 135 and indicatorOfParameter == 104:
            return 'VIS-500/Visibility at 500 nm'

        if table2Version == 135 and indicatorOfParameter == 103:
            return 'VIS-440/Visibility at 440 nm'

        if table2Version == 135 and indicatorOfParameter == 102:
            return 'VIS-380/Visibility at 380 nm'

        if table2Version == 135 and indicatorOfParameter == 101:
            return 'VIS-355/Visibility at 355 nm'

        if table2Version == 135 and indicatorOfParameter == 100:
            return 'VIS-340/Visibility at 340 nm'

        if table2Version == 135 and indicatorOfParameter == 5:
            return 'GRG5/MOZART specie'

        if table2Version == 135 and indicatorOfParameter == 4:
            return 'GRG4/MOZART specie'

        if table2Version == 135 and indicatorOfParameter == 3:
            return 'GRG3/MOZART specie'

        if table2Version == 135 and indicatorOfParameter == 2:
            return 'GRG2/MOZART specie'

        if table2Version == 135 and indicatorOfParameter == 1:
            return 'GRG1/MOZART specie'

        if table2Version == 135 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 134 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 134 and indicatorOfParameter == 113:
            return 'H2CCHCl/Vinylklorid'

        if table2Version == 134 and indicatorOfParameter == 112:
            return 'COCl2/Fosgen'

        if table2Version == 134 and indicatorOfParameter == 111:
            return 'HCN/Vaetecyanid'

        if table2Version == 134 and indicatorOfParameter == 110:
            return 'SF6/Sulphurhexafloride'

        if table2Version == 134 and indicatorOfParameter == 108:
            return 'CH3NH2/Metylamin'

        if table2Version == 134 and indicatorOfParameter == 107:
            return 'CS2/Koldisulfid'

        if table2Version == 134 and indicatorOfParameter == 106:
            return 'Hcl/Vaeteklorid'

        if table2Version == 134 and indicatorOfParameter == 105:
            return 'HF/Vaetefluorid'

        if table2Version == 134 and indicatorOfParameter == 103:
            return 'CH2OC2/Etylenoxid'

        if table2Version == 134 and indicatorOfParameter == 102:
            return 'CH2OC2H3Cl/Epiklorhydrin'

        if table2Version == 134 and indicatorOfParameter == 101:
            return '(CH3)2NNH2/Dimetylhydrazin'

        if table2Version == 134 and indicatorOfParameter == 100:
            return 'CH2CHCN'

        if table2Version == 134 and indicatorOfParameter == 92:
            return 'TOLUENE'

        if table2Version == 134 and indicatorOfParameter == 91:
            return 'BIGALK'

        if table2Version == 134 and indicatorOfParameter == 90:
            return 'BIGENE'

        if table2Version == 134 and indicatorOfParameter == 84:
            return 'CH2CO2HCH3'

        if table2Version == 134 and indicatorOfParameter == 83:
            return 'CH2CCH3'

        if table2Version == 134 and indicatorOfParameter == 82:
            return 'MACOOH'

        if table2Version == 134 and indicatorOfParameter == 81:
            return 'MACO3H'

        if table2Version == 134 and indicatorOfParameter == 80:
            return 'MACRO2'

        if table2Version == 134 and indicatorOfParameter == 79:
            return 'AOH1H'

        if table2Version == 134 and indicatorOfParameter == 78:
            return 'AOH1'

        if table2Version == 134 and indicatorOfParameter == 77:
            return 'MACR'

        if table2Version == 134 and indicatorOfParameter == 76:
            return 'ISNIRH'

        if table2Version == 134 and indicatorOfParameter == 75:
            return 'ISNIR'

        if table2Version == 134 and indicatorOfParameter == 74:
            return 'ISNI'

        if table2Version == 134 and indicatorOfParameter == 70:
            return 'BENZENE'

        if table2Version == 134 and indicatorOfParameter == 68:
            return 'MVKO2H'

        if table2Version == 134 and indicatorOfParameter == 67:
            return 'MVKO2'

        if table2Version == 134 and indicatorOfParameter == 66:
            return 'MVK'

        if table2Version == 134 and indicatorOfParameter == 65:
            return 'ISRO2H'

        if table2Version == 134 and indicatorOfParameter == 64:
            return 'OXYO2/Peroxy radical from o-xylene + oh'

        if table2Version == 134 and indicatorOfParameter == 63:
            return 'XO2'

        if table2Version == 134 and indicatorOfParameter == 62:
            return 'IPRO2'

        if table2Version == 134 and indicatorOfParameter == 61:
            return 'MALO2H/Hydroperoxide from MALO2 + ho2'

        if table2Version == 134 and indicatorOfParameter == 60:
            return 'CH3COCHO2HCH3/hydroperoxide from MEKO2 + HO2'

        if table2Version == 134 and indicatorOfParameter == 59:
            return 'CH3CHOOHCH2OH//hydroperoxide from PRRO2 + HO2'

        if table2Version == 134 and indicatorOfParameter == 58:
            return 'CH2OOHCH2OH'

        if table2Version == 134 and indicatorOfParameter == 57:
            return 'SECC4H9O2H/Buthyl hydroperoxide'

        if table2Version == 134 and indicatorOfParameter == 56:
            return 'OXYO2H/Hydroperoxide from OXYO2'

        if table2Version == 134 and indicatorOfParameter == 55:
            return 'CH3COO2H'

        if table2Version == 134 and indicatorOfParameter == 54:
            return 'C2H5OOH/Ethyl hydroperoxide'

        if table2Version == 134 and indicatorOfParameter == 53:
            return 'ISOPROD/Peroxy radical from ISOPROD'

        if table2Version == 134 and indicatorOfParameter == 52:
            return 'ISRO2/Peroxy radical from isoprene + oh'

        if table2Version == 134 and indicatorOfParameter == 51:
            return 'MALO2/Peroxy radical from MAL + oh'

        if table2Version == 134 and indicatorOfParameter == 50:
            return 'MAL/CH3COCH=CHCHO'

        if table2Version == 134 and indicatorOfParameter == 49:
            return 'CH3CHO2CH2OH/Peroxy radical from C3H6 + OH'

        if table2Version == 134 and indicatorOfParameter == 48:
            return 'CH2O2CH2OH'

        if table2Version == 134 and indicatorOfParameter == 47:
            return 'ACETOL/acetol (hydroxy acetone)'

        if table2Version == 134 and indicatorOfParameter == 46:
            return 'CH3COCHO2CH3/peroxy radical from MEK'

        if table2Version == 134 and indicatorOfParameter == 45:
            return 'SECC4H9O2/Buthyl peroxy radical'

        if table2Version == 134 and indicatorOfParameter == 44:
            return 'CH3COO2/Peroxy acetyl radical'

        if table2Version == 134 and indicatorOfParameter == 43:
            return 'C2H5O2/Ethyl peroxy radical'

        if table2Version == 134 and indicatorOfParameter == 42:
            return 'CH3O2H/Methyl hydroperoxide'

        if table2Version == 134 and indicatorOfParameter == 41:
            return 'CH3O2/Methyl peroxy radical'

        if table2Version == 134 and indicatorOfParameter == 40:
            return 'Reserved'

        if table2Version == 134 and indicatorOfParameter == 34:
            return 'O1D/Oxygen atomic first singlet state'

        if table2Version == 134 and indicatorOfParameter == 33:
            return 'O/Oxygen atomic ground state (3P)'

        if table2Version == 134 and indicatorOfParameter == 32:
            return 'H2/Molecular hydrogen'

        if table2Version == 134 and indicatorOfParameter == 31:
            return 'HO2/Hydroperhydroxyl radical'

        if table2Version == 134 and indicatorOfParameter == 30:
            return 'Reserved'

        if table2Version == 134 and indicatorOfParameter == 29:
            return 'HONO'

        if table2Version == 134 and indicatorOfParameter == 28:
            return 'ISONO3H'

        if table2Version == 134 and indicatorOfParameter == 27:
            return 'MPAN'

        if table2Version == 134 and indicatorOfParameter == 26:
            return 'HO2NO2/HO2NO2'

        if table2Version == 134 and indicatorOfParameter == 25:
            return 'ISONRO2/Isoprene-NO3 adduct'

        if table2Version == 134 and indicatorOfParameter == 24:
            return 'ONIT/Organic nitrate'

        if table2Version == 134 and indicatorOfParameter == 23:
            return 'N2O5/Dinitrogen pentoxide'

        if table2Version == 134 and indicatorOfParameter == 22:
            return 'NO3/Nitrate radical'

        if table2Version == 134 and indicatorOfParameter == 21:
            return 'PAN/Peroxy acetyl nitrate'

        if table2Version == 134 and indicatorOfParameter == 20:
            return 'Reserved'

        if table2Version == 134 and indicatorOfParameter == 19:
            return 'NMVOC_C/Total NMVOC as C'

        if table2Version == 134 and indicatorOfParameter == 15:
            return 'CH3COOH/Acetic acid'

        if table2Version == 134 and indicatorOfParameter == 14:
            return 'HCOOH/Formic acid'

        if table2Version == 134 and indicatorOfParameter == 13:
            return 'CH3OH/Metanol'

        if table2Version == 134 and indicatorOfParameter == 12:
            return 'C2H5OH/Ethanol'

        if table2Version == 134 and indicatorOfParameter == 11:
            return 'C5H8/Isoprene'

        if table2Version == 134 and indicatorOfParameter == 10:
            return 'GLYOX/Glyoxal (HCOCHO)'

        if table2Version == 134 and indicatorOfParameter == 9:
            return 'MGLYOX/Methyl-glyoxal (CH3COCHO)'

        if table2Version == 134 and indicatorOfParameter == 8:
            return 'CH3COC2H5/Ethyl methyl keton'

        if table2Version == 134 and indicatorOfParameter == 7:
            return 'CH3CHO/Acetaldehyde'

        if table2Version == 134 and indicatorOfParameter == 6:
            return 'HCHO/Formalydehyde'

        if table2Version == 134 and indicatorOfParameter == 5:
            return 'OXYLENE/O-xylene'

        if table2Version == 134 and indicatorOfParameter == 4:
            return 'C3H6/Propene'

        if table2Version == 134 and indicatorOfParameter == 3:
            return 'C2H4/Ethene'

        if table2Version == 134 and indicatorOfParameter == 2:
            return 'NC4H10/N-butane'

        if table2Version == 134 and indicatorOfParameter == 1:
            return 'C2H6/Ethane'

        if table2Version == 134 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 133 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 133 and indicatorOfParameter == 243:
            return 'Total depth in meters'

        if table2Version == 133 and indicatorOfParameter == 239:
            return 'Snow temperature'

        if table2Version == 133 and indicatorOfParameter == 233:
            return 'W-mean (prev. timestep)'

        if table2Version == 133 and indicatorOfParameter == 232:
            return 'V-mean (prev. timestep)'

        if table2Version == 133 and indicatorOfParameter == 231:
            return 'U-mean (prev. timestep)'

        if table2Version == 133 and indicatorOfParameter == 223:
            return 'Ice ridge density'

        if table2Version == 133 and indicatorOfParameter == 222:
            return 'Ice ridge height'

        if table2Version == 133 and indicatorOfParameter == 221:
            return 'Ridged ice thickness'

        if table2Version == 133 and indicatorOfParameter == 220:
            return ' Level ice thickness'

        if table2Version == 133 and indicatorOfParameter == 203:
            return 'Eddy diffusivity'

        if table2Version == 133 and indicatorOfParameter == 202:
            return 'Eddy viscosity'

        if table2Version == 133 and indicatorOfParameter == 201:
            return 'Dissipation rate of TKE'

        if table2Version == 133 and indicatorOfParameter == 200:
            return 'Turbulent Kinetic Energy'

        if table2Version == 133 and indicatorOfParameter == 166:
            return 'Nitrate (aggregated)'

        if table2Version == 133 and indicatorOfParameter == 165:
            return 'Flagellates (algae)'

        if table2Version == 133 and indicatorOfParameter == 164:
            return 'Diatomes (algae)'

        if table2Version == 133 and indicatorOfParameter == 163:
            return 'Inorganic suspended matter'

        if table2Version == 133 and indicatorOfParameter == 162:
            return 'Light in water column'

        if table2Version == 133 and indicatorOfParameter == 161:
            return 'Biogenic silica'

        if table2Version == 133 and indicatorOfParameter == 160:
            return 'Silicate'

        if table2Version == 133 and indicatorOfParameter == 159:
            return 'Bentos phosphorus'

        if table2Version == 133 and indicatorOfParameter == 158:
            return 'Bentos nitrogen'

        if table2Version == 133 and indicatorOfParameter == 157:
            return 'Detritus'

        if table2Version == 133 and indicatorOfParameter == 156:
            return 'Zooplankton'

        if table2Version == 133 and indicatorOfParameter == 155:
            return 'Phytoplankton'

        if table2Version == 133 and indicatorOfParameter == 154:
            return 'Oxygen'

        if table2Version == 133 and indicatorOfParameter == 153:
            return 'Phosphate'

        if table2Version == 133 and indicatorOfParameter == 152:
            return 'Ammonium'

        if table2Version == 133 and indicatorOfParameter == 151:
            return 'Nitrate'

        if table2Version == 133 and indicatorOfParameter == 131:
            return 'Skin velocity, y-comp.'

        if table2Version == 133 and indicatorOfParameter == 130:
            return 'Skin velocity, x-comp.'

        if table2Version == 133 and indicatorOfParameter == 113:
            return 'Peak period of 1D spectra'

        if table2Version == 133 and indicatorOfParameter == 112:
            return 'Mean direction of Waves'

        if table2Version == 133 and indicatorOfParameter == 111:
            return 'Mean period of waves'

        if table2Version == 133 and indicatorOfParameter == 110:
            return 'Secondary wave mean period'

        if table2Version == 133 and indicatorOfParameter == 109:
            return 'Secondary wave direction'

        if table2Version == 133 and indicatorOfParameter == 108:
            return 'Primary wave mean period'

        if table2Version == 133 and indicatorOfParameter == 107:
            return 'Primary wave direction'

        if table2Version == 133 and indicatorOfParameter == 106:
            return 'Mean Period Swell Waves'

        if table2Version == 133 and indicatorOfParameter == 105:
            return 'Sign Height Swell Waves'

        if table2Version == 133 and indicatorOfParameter == 104:
            return 'Direction of Swell Waves'

        if table2Version == 133 and indicatorOfParameter == 103:
            return 'Mean Period Wind Waves'

        if table2Version == 133 and indicatorOfParameter == 102:
            return 'Sign Height Wind Waves'

        if table2Version == 133 and indicatorOfParameter == 101:
            return 'Direction of Wind Waves'

        if table2Version == 133 and indicatorOfParameter == 100:
            return 'Significant wave height'

        if table2Version == 133 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 133 and indicatorOfParameter == 97:
            return 'Ice growth rate'

        if table2Version == 133 and indicatorOfParameter == 96:
            return 'V-component of ice drift'

        if table2Version == 133 and indicatorOfParameter == 95:
            return 'U-component of ice drift'

        if table2Version == 133 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 133 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 133 and indicatorOfParameter == 92:
            return 'Total ice thickness'

        if table2Version == 133 and indicatorOfParameter == 91:
            return 'Ice Cover'

        if table2Version == 133 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 133 and indicatorOfParameter == 88:
            return 'Salinity'

        if table2Version == 133 and indicatorOfParameter == 82:
            return 'Deviation of sea level from mean'

        if table2Version == 133 and indicatorOfParameter == 80:
            return 'Water temperature'

        if table2Version == 133 and indicatorOfParameter == 71:
            return 'Total Cloud Cover'

        if table2Version == 133 and indicatorOfParameter == 70:
            return 'Main thermocline anomaly'

        if table2Version == 133 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 133 and indicatorOfParameter == 68:
            return 'Transient thermocline depth'

        if table2Version == 133 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 133 and indicatorOfParameter == 66:
            return 'Snow Depth'

        if table2Version == 133 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 133 and indicatorOfParameter == 50:
            return 'V-comp of Current'

        if table2Version == 133 and indicatorOfParameter == 49:
            return 'U-comp of Current'

        if table2Version == 133 and indicatorOfParameter == 48:
            return 'Speed of horizontal current'

        if table2Version == 133 and indicatorOfParameter == 47:
            return 'Direction of horizontal current'

        if table2Version == 133 and indicatorOfParameter == 46:
            return 'Vertical v-component shear'

        if table2Version == 133 and indicatorOfParameter == 45:
            return 'Vertical u-component shear'

        if table2Version == 133 and indicatorOfParameter == 44:
            return 'Relative divergence'

        if table2Version == 133 and indicatorOfParameter == 43:
            return 'Relative vorticity'

        if table2Version == 133 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 133 and indicatorOfParameter == 41:
            return 'Absolute vorticity'

        if table2Version == 133 and indicatorOfParameter == 40:
            return 'Z-component of velocity (geometric)'

        if table2Version == 133 and indicatorOfParameter == 39:
            return 'Z-component of velocity (pressure)'

        if table2Version == 133 and indicatorOfParameter == 38:
            return 'Sigma coordinate vertical velocity'

        if table2Version == 133 and indicatorOfParameter == 37:
            return 'Montgomery stream function'

        if table2Version == 133 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 133 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 133 and indicatorOfParameter == 34:
            return 'V-component of Wind'

        if table2Version == 133 and indicatorOfParameter == 33:
            return 'U-component of Wind'

        if table2Version == 133 and indicatorOfParameter == 32:
            return 'Wind speed'

        if table2Version == 133 and indicatorOfParameter == 31:
            return 'Wind direction'

        if table2Version == 133 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 133 and indicatorOfParameter == 29:
            return 'Wave spectra (2)'

        if table2Version == 133 and indicatorOfParameter == 28:
            return 'Wave spectra (1)'

        if table2Version == 133 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 133 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 133 and indicatorOfParameter == 1:
            return 'Pressure reduced to MSL'

        if table2Version == 133 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 131 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 131 and indicatorOfParameter == 252:
            return 'Dissipation rate Turbulent Kinetic Energy'

        if table2Version == 131 and indicatorOfParameter == 251:
            return 'Turbulent Kintetic Energy'

        if table2Version == 131 and indicatorOfParameter == 250:
            return 'Heat in Probe'

        if table2Version == 131 and indicatorOfParameter == 246:
            return 'Isfrontlaege i Probe'

        if table2Version == 131 and indicatorOfParameter == 245:
            return 'Internal ice concentration in Probe'

        if table2Version == 131 and indicatorOfParameter == 244:
            return 'Vallad istjocklek i Probe'

        if table2Version == 131 and indicatorOfParameter == 241:
            return 'Black ice thickness in Probe'

        if table2Version == 131 and indicatorOfParameter == 196:
            return 'Fraction lake'

        if table2Version == 131 and indicatorOfParameter == 183:
            return 'Ice concentration (I)'

        if table2Version == 131 and indicatorOfParameter == 180:
            return 'Sea surface temperature (T)'

        if table2Version == 131 and indicatorOfParameter == 173:
            return 'Ice thickness E-lake'

        if table2Version == 131 and indicatorOfParameter == 172:
            return 'Ice thickness D-lake'

        if table2Version == 131 and indicatorOfParameter == 171:
            return 'Ice thickness C-lake'

        if table2Version == 131 and indicatorOfParameter == 170:
            return 'Ice thickness ABC-lake'

        if table2Version == 131 and indicatorOfParameter == 164:
            return 'E-lakes'

        if table2Version == 131 and indicatorOfParameter == 163:
            return 'D-lakes'

        if table2Version == 131 and indicatorOfParameter == 162:
            return 'C-lakes'

        if table2Version == 131 and indicatorOfParameter == 161:
            return 'Depth ABC-lake'

        if table2Version == 131 and indicatorOfParameter == 160:
            return 'Area ABC-lake'

        if table2Version == 131 and indicatorOfParameter == 153:
            return 'Temperature E-lake'

        if table2Version == 131 and indicatorOfParameter == 152:
            return 'Temperature D-lake'

        if table2Version == 131 and indicatorOfParameter == 151:
            return 'Temperature C-lake'

        if table2Version == 131 and indicatorOfParameter == 150:
            return 'Temperature ABC-lake'

        if table2Version == 131 and indicatorOfParameter == 92:
            return 'Ice thickness Probe-lake'

        if table2Version == 131 and indicatorOfParameter == 91:
            return 'Ice concentration (LAKE)'

        if table2Version == 131 and indicatorOfParameter == 66:
            return 'Snowdepth in Probe'

        if table2Version == 131 and indicatorOfParameter == 50:
            return 'Current north'

        if table2Version == 131 and indicatorOfParameter == 49:
            return 'Current east'

        if table2Version == 131 and indicatorOfParameter == 11:
            return 'Sea surface temperature (LAKE)'

        if table2Version == 131 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 130 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 130 and indicatorOfParameter == 149:
            return 'Area_time_median_precipitation'

        if table2Version == 130 and indicatorOfParameter == 148:
            return 'Area_time_mean_precipitation'

        if table2Version == 130 and indicatorOfParameter == 147:
            return 'Vadersymbol'

        if table2Version == 130 and indicatorOfParameter == 146:
            return 'Category of precipitation, 0 no, 1 snow, 2 snow and rain, 3 rain, 4 drizzle, 5, freezing rain, 6 freezing drizzle'

        if table2Version == 130 and indicatorOfParameter == 145:
            return 'Precipitation type, conv 0, large scale 1, no prec -9'

        if table2Version == 130 and indicatorOfParameter == 143:
            return 'Area_time_max_precipitation'

        if table2Version == 130 and indicatorOfParameter == 142:
            return 'Area_time_min_precipitation'

        if table2Version == 130 and indicatorOfParameter == 141:
            return 'Precipitation intensity snow'

        if table2Version == 130 and indicatorOfParameter == 140:
            return 'Precipitation intensity total'

        if table2Version == 130 and indicatorOfParameter == 139:
            return 'Omradesnederbord gridpunkts-medel'

        if table2Version == 130 and indicatorOfParameter == 138:
            return 'Omradesnederbord gridpunkts-max'

        if table2Version == 130 and indicatorOfParameter == 137:
            return 'Omradesnederbord gridpunkts-min'

        if table2Version == 130 and indicatorOfParameter == 136:
            return 'Cloud top (significant)'

        if table2Version == 130 and indicatorOfParameter == 135:
            return 'Cloud base (significant)'

        if table2Version == 130 and indicatorOfParameter == 131:
            return 'Wind gust'

        if table2Version == 130 and indicatorOfParameter == 130:
            return 'Maximum wind (mean 10 min)'

        if table2Version == 130 and indicatorOfParameter == 111:
            return 'EPS T standard deviation'

        if table2Version == 130 and indicatorOfParameter == 110:
            return 'EPS T mean'

        if table2Version == 130 and indicatorOfParameter == 100:
            return 'Index 2m maxtemperatur over 3 dygn'

        if table2Version == 130 and indicatorOfParameter == 77:
            return 'cloud mask'

        if table2Version == 130 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 130 and indicatorOfParameter == 74:
            return 'Medium cloud cove'

        if table2Version == 130 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 130 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 130 and indicatorOfParameter == 71:
            return 'Total cloud cover'

        if table2Version == 130 and indicatorOfParameter == 70:
            return 'Area_time_mean_totalcloudcover'

        if table2Version == 130 and indicatorOfParameter == 69:
            return 'Area_time_median_totalcloudcover'

        if table2Version == 130 and indicatorOfParameter == 68:
            return 'Area_time_max_totalcloudcover'

        if table2Version == 130 and indicatorOfParameter == 67:
            return 'Area_time_min_totalcloudcover'

        if table2Version == 130 and indicatorOfParameter == 65:
            return 'Water_equiv._of_snow_depth'

        if table2Version == 130 and indicatorOfParameter == 61:
            return 'Total_precipitation'

        if table2Version == 130 and indicatorOfParameter == 60:
            return 'Probability thunderstorm'

        if table2Version == 130 and indicatorOfParameter == 58:
            return 'Probability of frozen rain'

        if table2Version == 130 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 130 and indicatorOfParameter == 34:
            return 'v-component of wind'

        if table2Version == 130 and indicatorOfParameter == 33:
            return 'u-component of wind'

        if table2Version == 130 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 130 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 130 and indicatorOfParameter == 1:
            return 'Pressure reduced to MSL'

        if table2Version == 130 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 129 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 129 and indicatorOfParameter == 239:
            return '15 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 238:
            return '9 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 237:
            return '3 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 236:
            return '2 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 235:
            return '1 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 234:
            return '24 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 233:
            return '18 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 232:
            return '12 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 231:
            return '6 hour fresh snow cover, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 229:
            return '15 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 228:
            return '9 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 227:
            return '3 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 226:
            return '2 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 225:
            return '1 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 224:
            return '24 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 223:
            return '18 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 222:
            return '12 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 221:
            return '6 hour precipitation, corrected and standardized'

        if table2Version == 129 and indicatorOfParameter == 219:
            return '15 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 218:
            return '9 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 217:
            return '3 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 216:
            return '2 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 215:
            return '1 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 214:
            return '24 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 213:
            return '18 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 212:
            return '12 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 211:
            return '6 hour fresh snow cover, standardized'

        if table2Version == 129 and indicatorOfParameter == 209:
            return '15 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 208:
            return '9 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 207:
            return '3 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 206:
            return '2 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 205:
            return '1 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 204:
            return '24 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 203:
            return '18 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 202:
            return '12 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 201:
            return '6 hour precipitation, standardized'

        if table2Version == 129 and indicatorOfParameter == 199:
            return '15 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 198:
            return '9 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 197:
            return '3 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 196:
            return '2 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 195:
            return '1 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 194:
            return '24 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 193:
            return '18 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 192:
            return '12 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 191:
            return '6 hour fresh snow cover, corrected'

        if table2Version == 129 and indicatorOfParameter == 189:
            return '15 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 188:
            return '9 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 187:
            return '3 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 186:
            return '2 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 185:
            return '1 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 184:
            return '24 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 183:
            return '18 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 182:
            return '12 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 181:
            return '6 hour precipitation, corrected'

        if table2Version == 129 and indicatorOfParameter == 179:
            return '15 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 178:
            return '9 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 177:
            return '3 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 176:
            return '2 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 175:
            return '1 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 174:
            return '24 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 173:
            return '18 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 172:
            return '12 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 171:
            return '6 hour fresh snow cover'

        if table2Version == 129 and indicatorOfParameter == 169:
            return '15 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 168:
            return '9 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 167:
            return '3 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 166:
            return '2 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 165:
            return '1 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 164:
            return '24 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 163:
            return '18 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 162:
            return '12 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 161:
            return '6 hour precipitation'

        if table2Version == 129 and indicatorOfParameter == 146:
            return 'Sort of precipitation'

        if table2Version == 129 and indicatorOfParameter == 145:
            return 'Type of precipitation'

        if table2Version == 129 and indicatorOfParameter == 79:
            return 'Cloud top of significant clouds'

        if table2Version == 129 and indicatorOfParameter == 78:
            return 'Cloud base of significant clouds'

        if table2Version == 129 and indicatorOfParameter == 77:
            return 'Fraction of significant clouds'

        if table2Version == 129 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 129 and indicatorOfParameter == 74:
            return 'Medium cloud cove'

        if table2Version == 129 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 129 and indicatorOfParameter == 71:
            return 'Total cloud cover'

        if table2Version == 129 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 129 and indicatorOfParameter == 34:
            return 'v-component of wind'

        if table2Version == 129 and indicatorOfParameter == 33:
            return 'u-component of wind'

        if table2Version == 129 and indicatorOfParameter == 32:
            return 'Wind gusts'

        if table2Version == 129 and indicatorOfParameter == 20:
            return 'Visibility'

        if table2Version == 129 and indicatorOfParameter == 16:
            return 'Minimum temperature'

        if table2Version == 129 and indicatorOfParameter == 15:
            return 'Maximum temperature'

        if table2Version == 129 and indicatorOfParameter == 13:
            return '24 hour mean of 2 meter temperature'

        if table2Version == 129 and indicatorOfParameter == 12:
            return 'Wet bulb temperature'

        if table2Version == 129 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 129 and indicatorOfParameter == 1:
            return 'Pressure reduced to MSL'

        if table2Version == 129 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 128 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 128 and indicatorOfParameter == 242:
            return 'LAT/Latitude'

        if table2Version == 128 and indicatorOfParameter == 241:
            return 'LONG/Longitude'

        if table2Version == 128 and indicatorOfParameter == 240:
            return 'EMIS/Sectoral emissions'

        if table2Version == 128 and indicatorOfParameter == 223:
            return 'DXDY/Gridsize [m2]'

        if table2Version == 128 and indicatorOfParameter == 222:
            return 'CONV_TOP/Convective cloud top (unit?)'

        if table2Version == 128 and indicatorOfParameter == 221:
            return 'CONV_BOT/Convective cloud bottom (unit?)'

        if table2Version == 128 and indicatorOfParameter == 220:
            return 'CONV_TIED'

        if table2Version == 128 and indicatorOfParameter == 219:
            return 'DAOD/AOD per layer [1]'

        if table2Version == 128 and indicatorOfParameter == 218:
            return 'AOD/Aerosol opt depth [1]'

        if table2Version == 128 and indicatorOfParameter == 217:
            return 'BSCA/Backscattering coeff [1/m/sr]'

        if table2Version == 128 and indicatorOfParameter == 216:
            return 'EXT/Extinction [1/m]'

        if table2Version == 128 and indicatorOfParameter == 215:
            return 'VIS/Visibility [m]'

        if table2Version == 128 and indicatorOfParameter == 214:
            return 'ASYMPAR/Asymmetry parameter'

        if table2Version == 128 and indicatorOfParameter == 213:
            return 'SSALB/Single scattering albodo [1]'

        if table2Version == 128 and indicatorOfParameter == 212:
            return 'SOILTYPE/Soil type'

        if table2Version == 128 and indicatorOfParameter == 211:
            return 'LAI/Leaf area index'

        if table2Version == 128 and indicatorOfParameter == 210:
            return 'SURFTYPE/Surface type (see link{OCTET45})'

        if table2Version == 128 and indicatorOfParameter == 204:
            return 'Z-D/Z0 minus displacement length [m]'

        if table2Version == 128 and indicatorOfParameter == 203:
            return 'W*/Convective velocity scale [m/s]'

        if table2Version == 128 and indicatorOfParameter == 202:
            return 'U*/Friction velocity [m/s]'

        if table2Version == 128 and indicatorOfParameter == 201:
            return 'L/Monin-Obukhovs length [m]'

        if table2Version == 128 and indicatorOfParameter == 200:
            return 'KZ'

        if table2Version == 128 and indicatorOfParameter == 180:
            return 'BIRCH_POLLEN/Birch pollen'

        if table2Version == 128 and indicatorOfParameter == 175:
            return 'PM/Total particulate matter'

        if table2Version == 128 and indicatorOfParameter == 174:
            return 'PM2.5/PM2.5 particles'

        if table2Version == 128 and indicatorOfParameter == 173:
            return 'SOA/Secondary Organic Aerosol'

        if table2Version == 128 and indicatorOfParameter == 172:
            return 'PPM10/Primary emitted particles'

        if table2Version == 128 and indicatorOfParameter == 171:
            return 'PPMFINE/Primary emitted fine particles'

        if table2Version == 128 and indicatorOfParameter == 170:
            return 'PNHX/Particulate ammonium'

        if table2Version == 128 and indicatorOfParameter == 169:
            return 'PNOX/Particulate nitrate'

        if table2Version == 128 and indicatorOfParameter == 168:
            return 'PSOX/Particulate sulfate'

        if table2Version == 128 and indicatorOfParameter == 167:
            return 'PM10/PM10 particles'

        if table2Version == 128 and indicatorOfParameter == 166:
            return 'PMASS/Particle mass conc'

        if table2Version == 128 and indicatorOfParameter == 165:
            return 'PSURFACE/Particle surface conc'

        if table2Version == 128 and indicatorOfParameter == 164:
            return 'PRADIUS/Particle radius'

        if table2Version == 128 and indicatorOfParameter == 163:
            return 'PNUMBER/Number concentration'

        if table2Version == 128 and indicatorOfParameter == 162:
            return 'DUST/Dust (particles)'

        if table2Version == 128 and indicatorOfParameter == 161:
            return 'PMCOARSE/Coarse particles'

        if table2Version == 128 and indicatorOfParameter == 160:
            return 'PMFINE'

        if table2Version == 128 and indicatorOfParameter == 140:
            return 'Cl2/Cloride'

        if table2Version == 128 and indicatorOfParameter == 128:
            return 'XCA/excess Ca++ (corrected for sea salt)'

        if table2Version == 128 and indicatorOfParameter == 126:
            return 'XK/excess K+ (corrected for sea salt)'

        if table2Version == 128 and indicatorOfParameter == 125:
            return 'XMG/excess Mg++ (corrected for sea salt)'

        if table2Version == 128 and indicatorOfParameter == 124:
            return 'CALCIUM/Ca++'

        if table2Version == 128 and indicatorOfParameter == 123:
            return 'POTASSIUM/K+'

        if table2Version == 128 and indicatorOfParameter == 122:
            return 'MAGNESIUM/Mg++'

        if table2Version == 128 and indicatorOfParameter == 121:
            return 'SODIUM/Na+'

        if table2Version == 128 and indicatorOfParameter == 120:
            return 'NACL'

        if table2Version == 128 and indicatorOfParameter == 119:
            return 'ALL'

        if table2Version == 128 and indicatorOfParameter == 116:
            return 'Pb210/Pb210'

        if table2Version == 128 and indicatorOfParameter == 115:
            return 'Pu241/Pu241'

        if table2Version == 128 and indicatorOfParameter == 114:
            return 'Np239/Np239'

        if table2Version == 128 and indicatorOfParameter == 113:
            return 'Np238/Np238'

        if table2Version == 128 and indicatorOfParameter == 112:
            return 'Ce144/Ce144'

        if table2Version == 128 and indicatorOfParameter == 111:
            return 'Nb95/Nb95'

        if table2Version == 128 and indicatorOfParameter == 110:
            return 'Zr95'

        if table2Version == 128 and indicatorOfParameter == 108:
            return 'Ra228/Ra228'

        if table2Version == 128 and indicatorOfParameter == 106:
            return 'Ra223/Ra123'

        if table2Version == 128 and indicatorOfParameter == 105:
            return 'Cs137/Cs137'

        if table2Version == 128 and indicatorOfParameter == 104:
            return 'Cs134/Cs134'

        if table2Version == 128 and indicatorOfParameter == 103:
            return 'Ru106/Ru106'

        if table2Version == 128 and indicatorOfParameter == 102:
            return 'Ru103/Ru103'

        if table2Version == 128 and indicatorOfParameter == 101:
            return 'Co60/Co60'

        if table2Version == 128 and indicatorOfParameter == 100:
            return 'Sr90'

        if table2Version == 128 and indicatorOfParameter == 98:
            return 'I135/I135'

        if table2Version == 128 and indicatorOfParameter == 97:
            return 'I133/I133'

        if table2Version == 128 and indicatorOfParameter == 96:
            return 'I132/I132'

        if table2Version == 128 and indicatorOfParameter == 95:
            return 'I131/I131'

        if table2Version == 128 and indicatorOfParameter == 93:
            return 'Rn222/Rn222'

        if table2Version == 128 and indicatorOfParameter == 92:
            return 'Xe133/Xe133'

        if table2Version == 128 and indicatorOfParameter == 91:
            return 'Xe131/Xe131'

        if table2Version == 128 and indicatorOfParameter == 88:
            return 'Kr88/Kr88'

        if table2Version == 128 and indicatorOfParameter == 87:
            return 'Kr85/Kr85'

        if table2Version == 128 and indicatorOfParameter == 86:
            return 'Ar41/Ar41'

        if table2Version == 128 and indicatorOfParameter == 85:
            return 'H3'

        if table2Version == 128 and indicatorOfParameter == 84:
            return 'Inert/Inert'

        if table2Version == 128 and indicatorOfParameter == 83:
            return 'TRACER/Tracer'

        if table2Version == 128 and indicatorOfParameter == 82:
            return 'PMCP/PMCP'

        if table2Version == 128 and indicatorOfParameter == 81:
            return 'PMCH/PMCH'

        if table2Version == 128 and indicatorOfParameter == 80:
            return 'CF6'

        if table2Version == 128 and indicatorOfParameter == 75:
            return 'EC/Elementary carbon (particles)'

        if table2Version == 128 and indicatorOfParameter == 74:
            return 'OC/Organic carbon (particles)'

        if table2Version == 128 and indicatorOfParameter == 73:
            return 'CH4/CH4'

        if table2Version == 128 and indicatorOfParameter == 72:
            return 'CO2/CO2'

        if table2Version == 128 and indicatorOfParameter == 71:
            return 'CO/CO'

        if table2Version == 128 and indicatorOfParameter == 70:
            return 'C'

        if table2Version == 128 and indicatorOfParameter == 65:
            return 'OX/Ox=O3+NO2'

        if table2Version == 128 and indicatorOfParameter == 64:
            return 'H2O2_AQ/H2O2 in aqueous phase'

        if table2Version == 128 and indicatorOfParameter == 63:
            return 'O3_AQ/O3 in aqueous phase'

        if table2Version == 128 and indicatorOfParameter == 62:
            return 'OH/OH'

        if table2Version == 128 and indicatorOfParameter == 61:
            return 'H2O2/H2O2'

        if table2Version == 128 and indicatorOfParameter == 60:
            return 'O3'

        if table2Version == 128 and indicatorOfParameter == 59:
            return 'NHX_N/All reduced nitrogen (as nitrogen)'

        if table2Version == 128 and indicatorOfParameter == 58:
            return 'LRT_NHX_N/long-range NHX_N'

        if table2Version == 128 and indicatorOfParameter == 57:
            return 'LRT_NH4_N/long-range NH4_N'

        if table2Version == 128 and indicatorOfParameter == 56:
            return 'LRT_NH3_N/long-range NH3_N'

        if table2Version == 128 and indicatorOfParameter == 55:
            return 'NH4_N/NH4 (as nitrogen)'

        if table2Version == 128 and indicatorOfParameter == 54:
            return 'NH3_N/NH3 (as nitrogen)'

        if table2Version == 128 and indicatorOfParameter == 52:
            return 'AMMONIUM/AMMONIUM'

        if table2Version == 128 and indicatorOfParameter == 51:
            return 'NH4(+1)/NH4'

        if table2Version == 128 and indicatorOfParameter == 50:
            return 'NH3/NH3'

        if table2Version == 128 and indicatorOfParameter == 49:
            return 'NOZ_N/NOy-NOx (as nitrogen)'

        if table2Version == 128 and indicatorOfParameter == 48:
            return 'NOY_N/All oxidised N-compounds (as nitrogen)'

        if table2Version == 128 and indicatorOfParameter == 47:
            return 'NOX_N/NO2+NO (NOx) as nitrogen'

        if table2Version == 128 and indicatorOfParameter == 46:
            return 'NO2_N/NO2 as N'

        if table2Version == 128 and indicatorOfParameter == 45:
            return 'NO_N/NO as N'

        if table2Version == 128 and indicatorOfParameter == 44:
            return 'NOX/NOX as NO2'

        if table2Version == 128 and indicatorOfParameter == 43:
            return 'LRT_NOZ_N/long-range NOZ_N'

        if table2Version == 128 and indicatorOfParameter == 42:
            return 'LRT_NO2_N/long-range NO2_N'

        if table2Version == 128 and indicatorOfParameter == 41:
            return 'LRT_HNO3_N/long-range HNO3_N'

        if table2Version == 128 and indicatorOfParameter == 40:
            return 'LRT_NO3_N/long-range NO3_N'

        if table2Version == 128 and indicatorOfParameter == 39:
            return 'HNO3_N/HNO3 as N'

        if table2Version == 128 and indicatorOfParameter == 38:
            return 'NO3_N/NO3 as N'

        if table2Version == 128 and indicatorOfParameter == 37:
            return 'LRT_NOY_N/long-range NOY_N'

        if table2Version == 128 and indicatorOfParameter == 36:
            return 'PNO3/(COARSE) NITRATE'

        if table2Version == 128 and indicatorOfParameter == 35:
            return 'NITRATE/NITRATE'

        if table2Version == 128 and indicatorOfParameter == 34:
            return 'NH4NO3/NH4NO3'

        if table2Version == 128 and indicatorOfParameter == 33:
            return 'NO3(-1)/NO3(-1) (nitrate)'

        if table2Version == 128 and indicatorOfParameter == 32:
            return 'HNO3/HNO3'

        if table2Version == 128 and indicatorOfParameter == 31:
            return 'NO2/NO2'

        if table2Version == 128 and indicatorOfParameter == 30:
            return 'NO'

        if table2Version == 128 and indicatorOfParameter == 29:
            return 'SOX_S/All oxidised sulphur compounds (as sulphur)'

        if table2Version == 128 and indicatorOfParameter == 28:
            return 'SO4_S/SO4 (as sulphur)'

        if table2Version == 128 and indicatorOfParameter == 27:
            return 'SO2_S/SO2 (as sulphur)'

        if table2Version == 128 and indicatorOfParameter == 26:
            return 'XSOX_S/excess SOX (corrected for sea salt as sulfur)'

        if table2Version == 128 and indicatorOfParameter == 25:
            return 'LRT_SOX_S/LRT-contriubtion to SO4_S'

        if table2Version == 128 and indicatorOfParameter == 24:
            return 'LRT_SO4_S/LRT-contriubtion to SO4_S'

        if table2Version == 128 and indicatorOfParameter == 23:
            return 'LRT_SO2_S/long-range SO2_S'

        if table2Version == 128 and indicatorOfParameter == 11:
            return 'SO4_AQ/sulfate in aqueous phase'

        if table2Version == 128 and indicatorOfParameter == 10:
            return 'SO2_AQ/SO2 in aqueous phase'

        if table2Version == 128 and indicatorOfParameter == 9:
            return 'SULFATE/SULFATE'

        if table2Version == 128 and indicatorOfParameter == 8:
            return 'NH42SO4/(NH4)2SO4'

        if table2Version == 128 and indicatorOfParameter == 7:
            return 'NH4HSO4/NH4HSO4'

        if table2Version == 128 and indicatorOfParameter == 6:
            return 'NH4SO4/(NH4)1.5H0.5SO4'

        if table2Version == 128 and indicatorOfParameter == 5:
            return 'H2S/H2S'

        if table2Version == 128 and indicatorOfParameter == 4:
            return 'MSA/MSA'

        if table2Version == 128 and indicatorOfParameter == 3:
            return 'DMS/DMS'

        if table2Version == 128 and indicatorOfParameter == 2:
            return 'SO4(2-)/SO4(2-) (sulphate)'

        if table2Version == 128 and indicatorOfParameter == 1:
            return 'SO2/SO2'

        if table2Version == 128 and indicatorOfParameter == 0:
            return 'Reserved'

        if table2Version == 1 and indicatorOfParameter == 255:
            return 'Missing'

        if table2Version == 1 and indicatorOfParameter == 251:
            return 'Analysed 12-hour precipitation (-12h/0h)'

        if table2Version == 1 and indicatorOfParameter == 250:
            return 'Analysed 3-hour precipitation (-3h/0h)'

        if table2Version == 1 and indicatorOfParameter == 228:
            return 'Wind gust'

        if table2Version == 1 and indicatorOfParameter == 227:
            return 'Friction velocity'

        if table2Version == 1 and indicatorOfParameter == 226:
            return 'Precipitation type'

        if table2Version == 1 and indicatorOfParameter == 225:
            return 'CAPE'

        if table2Version == 1 and indicatorOfParameter == 224:
            return 'Convective inhibation'

        if table2Version == 1 and indicatorOfParameter == 223:
            return 'Level of neutral buoyancy'

        if table2Version == 1 and indicatorOfParameter == 222:
            return 'Lifting condensation level'

        if table2Version == 1 and indicatorOfParameter == 210:
            return 'Ice existence'

        if table2Version == 1 and indicatorOfParameter == 209:
            return 'Standard deviation of smallest scale orography'

        if table2Version == 1 and indicatorOfParameter == 208:
            return 'Maximum slope of smallest scale orography'

        if table2Version == 1 and indicatorOfParameter == 206:
            return 'X-angle of mesoscale orography'

        if table2Version == 1 and indicatorOfParameter == 205:
            return 'Anisotrophic mesoscale orography'

        if table2Version == 1 and indicatorOfParameter == 204:
            return 'Standard deviation of mesoscale orography'

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
            return 'Soil type'

        if table2Version == 1 and indicatorOfParameter == 194:
            return 'Fraction of surface type'

        if table2Version == 1 and indicatorOfParameter == 193:
            return 'Surface soil ice'

        if table2Version == 1 and indicatorOfParameter == 192:
            return 'Water on canopy level'

        if table2Version == 1 and indicatorOfParameter == 191:
            return 'Snow density'

        if table2Version == 1 and indicatorOfParameter == 190:
            return 'Snow albedo'

        if table2Version == 1 and indicatorOfParameter == 189:
            return 'Soil wetness index'

        if table2Version == 1 and indicatorOfParameter == 169:
            return 'Albedo with solar angle correction'

        if table2Version == 1 and indicatorOfParameter == 168:
            return 'Heat roughness'

        if table2Version == 1 and indicatorOfParameter == 167:
            return 'Fraction of aspect'

        if table2Version == 1 and indicatorOfParameter == 166:
            return 'Sky wiew factor'

        if table2Version == 1 and indicatorOfParameter == 165:
            return 'Surface slope'

        if table2Version == 1 and indicatorOfParameter == 164:
            return 'Momentum vegetation roughness'

        if table2Version == 1 and indicatorOfParameter == 163:
            return 'Shadow parameter RSHB'

        if table2Version == 1 and indicatorOfParameter == 162:
            return 'Shadow parameter RSHA'

        if table2Version == 1 and indicatorOfParameter == 161:
            return 'Shadow fraction'

        if table2Version == 1 and indicatorOfParameter == 160:
            return 'Slope fraction'

        if table2Version == 1 and indicatorOfParameter == 143:
            return 'Dew point over land'

        if table2Version == 1 and indicatorOfParameter == 142:
            return 'Relative humidity over land'

        if table2Version == 1 and indicatorOfParameter == 141:
            return 'Specific humidity over land'

        if table2Version == 1 and indicatorOfParameter == 140:
            return 'Temperature over land'

        if table2Version == 1 and indicatorOfParameter == 139:
            return 'Open land snow depth'

        if table2Version == 1 and indicatorOfParameter == 138:
            return 'Snow depth, cold snow'

        if table2Version == 1 and indicatorOfParameter == 137:
            return 'Integrated cloud condensate'

        if table2Version == 1 and indicatorOfParameter == 136:
            return 'Minimum wind'

        if table2Version == 1 and indicatorOfParameter == 135:
            return 'Maximum wind'

        if table2Version == 1 and indicatorOfParameter == 134:
            return 'Cloud water reflectivity'

        if table2Version == 1 and indicatorOfParameter == 133:
            return 'Water vapor brightness temperature, correction'

        if table2Version == 1 and indicatorOfParameter == 132:
            return 'Water vapor brightness temperature'

        if table2Version == 1 and indicatorOfParameter == 131:
            return 'Cloud top temperature, infrared'

        if table2Version == 1 and indicatorOfParameter == 130:
            return 'Radiation at top of atmosphere'

        if table2Version == 1 and indicatorOfParameter == 129:
            return 'Humidity tendencies'

        if table2Version == 1 and indicatorOfParameter == 128:
            return 'Momentum flux'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 'Image data'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'Wind mixing energy'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'Momentum flux, v component'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'Momentum flux, u component'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'Boundary layer dissipation'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'Sensible heat net flux'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'Latent heat net flux'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'Radiance (with respect to wave length)'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'Radiance (with respect to wave number)'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'Brightness temperature'

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'Global radiation flux'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'Short wave radiation flux'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'Long wave radiation flux'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'Net long wave radiation flux (top of atmos.)'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'Net short wave radiation flux (top of atmos.)'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'Net long wave radiation flux (surface)'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'Net short wave radiation flux (surface)'

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
            return 'Direction of wind waves'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'Significant height of combined wind waves and swell'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'Snow melt'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 1 and indicatorOfParameter == 97:
            return 'Ice growth rate'

        if table2Version == 1 and indicatorOfParameter == 96:
            return 'v-component of ice drift'

        if table2Version == 1 and indicatorOfParameter == 95:
            return 'u-component of ice drift'

        if table2Version == 1 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 1 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 1 and indicatorOfParameter == 92:
            return 'Ice thickness'

        if table2Version == 1 and indicatorOfParameter == 91:
            return 'Ice cover (ice=1 no ice=0)(see note)'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'Water run off'

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
            return 'Deviation of sea level from mean'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'Land-sea mask (1=land 0=sea) (see note)'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'Water Temperature'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'Large scale snow'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'Convective snow'

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
            return 'Water equiv. of accum. snow depth'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'Snowfall rate water equivalent'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'Convective precipitation'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'Large scale precipitation'

        if table2Version == 1 and indicatorOfParameter == 61:
            return 'Total precipitation'

        if table2Version == 1 and indicatorOfParameter == 60:
            return 'Thunderstorm probability'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 1 and indicatorOfParameter == 58:
            return 'Cloud Ice'

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
            return 'v-component of current'

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'u-component of current'

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
            return 'Geometric Vertical velocity'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'Pressure Vertical velocity'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 'Sigma coord. vertical velocity'

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
            return 'Wave Spectra (3)'

        if table2Version == 1 and indicatorOfParameter == 29:
            return 'Wave Spectra (2)'

        if table2Version == 1 and indicatorOfParameter == 28:
            return 'Wave Spectra (1)'

        if table2Version == 1 and indicatorOfParameter == 27:
            return 'Geopotential height anomaly'

        if table2Version == 1 and indicatorOfParameter == 26:
            return 'Pressure anomaly'

        if table2Version == 1 and indicatorOfParameter == 25:
            return 'Temperature anomaly'

        if table2Version == 1 and indicatorOfParameter == 24:
            return 'Parcel lifted index (to 500 hPa)'

        if table2Version == 1 and indicatorOfParameter == 23:
            return 'Radar Spectra (3)'

        if table2Version == 1 and indicatorOfParameter == 22:
            return 'Radar Spectra (2)'

        if table2Version == 1 and indicatorOfParameter == 21:
            return 'Radar Spectra (1)'

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
            return 'Virtual temperature'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'Total ozone'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'Standard deviation of height'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'Geometric height'

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
            return 'Pressure reduced to MSL'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 1 and indicatorOfParameter == 0:
            return 'Reserved'

    return wrapped
