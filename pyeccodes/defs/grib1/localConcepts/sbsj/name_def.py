import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 254 and indicatorOfParameter == 255:
            return 'Time mean zonal wind (u)'

        if table2Version == 254 and indicatorOfParameter == 254:
            return 'Time mean vorticity'

        if table2Version == 254 and indicatorOfParameter == 253:
            return 'Time mean virtual temperature'

        if table2Version == 254 and indicatorOfParameter == 252:
            return 'Time mean velocity potential'

        if table2Version == 254 and indicatorOfParameter == 251:
            return 'Time mean surface temperature'

        if table2Version == 254 and indicatorOfParameter == 250:
            return 'Time mean surface pressure'

        if table2Version == 254 and indicatorOfParameter == 249:
            return 'Time mean stream function'

        if table2Version == 254 and indicatorOfParameter == 248:
            return 'Time mean specific humidity'

        if table2Version == 254 and indicatorOfParameter == 247:
            return 'Time mean sigmadot'

        if table2Version == 254 and indicatorOfParameter == 246:
            return 'Time mean sea level pressure'

        if table2Version == 254 and indicatorOfParameter == 245:
            return 'Time mean relative humidity'

        if table2Version == 254 and indicatorOfParameter == 244:
            return 'Time mean precip. water'

        if table2Version == 254 and indicatorOfParameter == 243:
            return 'Time mean potential temperature'

        if table2Version == 254 and indicatorOfParameter == 242:
            return 'Time mean omega'

        if table2Version == 254 and indicatorOfParameter == 241:
            return 'Time mean meridional wind (v)'

        if table2Version == 254 and indicatorOfParameter == 240:
            return 'Time mean mask'

        if table2Version == 254 and indicatorOfParameter == 239:
            return 'Time mean log surface pressure'

        if table2Version == 254 and indicatorOfParameter == 238:
            return 'Time mean geopotential height'

        if table2Version == 254 and indicatorOfParameter == 237:
            return 'Time mean divergence'

        if table2Version == 254 and indicatorOfParameter == 236:
            return 'Time mean derived omega'

        if table2Version == 254 and indicatorOfParameter == 235:
            return 'Time mean deep soil temperature'

        if table2Version == 254 and indicatorOfParameter == 234:
            return 'Time mean absolute temperature'

        if table2Version == 254 and indicatorOfParameter == 233:
            return 'Time mean surface relative humidity'

        if table2Version == 254 and indicatorOfParameter == 232:
            return 'Time mean surface absolute temperature'

        if table2Version == 254 and indicatorOfParameter == 231:
            return 'Time mean surface meridional wind (v)'

        if table2Version == 254 and indicatorOfParameter == 230:
            return 'Time mean surface zonal wind (u)'

        if table2Version == 254 and indicatorOfParameter == 227:
            return 'Vertical dist total cloud cover'

        if table2Version == 254 and indicatorOfParameter == 226:
            return 'Surface relative humidity'

        if table2Version == 254 and indicatorOfParameter == 225:
            return 'Vertical diffusion heating'

        if table2Version == 254 and indicatorOfParameter == 224:
            return 'Vertical diffusion dv/dt'

        if table2Version == 254 and indicatorOfParameter == 223:
            return 'Vertical diffusion du/dt'

        if table2Version == 254 and indicatorOfParameter == 222:
            return 'Vertical diff. moisture source'

        if table2Version == 254 and indicatorOfParameter == 221:
            return 'Horizontal vorticity diffusion'

        if table2Version == 254 and indicatorOfParameter == 220:
            return 'Horizontal divergence diffusion'

        if table2Version == 254 and indicatorOfParameter == 219:
            return 'Horizontal moisture diffusion'

        if table2Version == 254 and indicatorOfParameter == 218:
            return 'Horizontal heating diffusion'

        if table2Version == 254 and indicatorOfParameter == 215:
            return 'Upward short wave at top (clear)'

        if table2Version == 254 and indicatorOfParameter == 214:
            return 'Upward short wave at top'

        if table2Version == 254 and indicatorOfParameter == 213:
            return 'Upward short wave at ground (clear)'

        if table2Version == 254 and indicatorOfParameter == 212:
            return 'Upward short wave at ground'

        if table2Version == 254 and indicatorOfParameter == 211:
            return 'Upward long wave at bottom'

        if table2Version == 254 and indicatorOfParameter == 210:
            return 'Downward short wave at ground (clear)'

        if table2Version == 254 and indicatorOfParameter == 209:
            return 'Downward short wave at ground'

        if table2Version == 254 and indicatorOfParameter == 208:
            return 'Downward long wave at bottom (clear)'

        if table2Version == 254 and indicatorOfParameter == 207:
            return 'Downward long wave at bottom'

        if table2Version == 254 and indicatorOfParameter == 206:
            return 'Short wave radiative heating'

        if table2Version == 254 and indicatorOfParameter == 205:
            return 'Long wave radiative heating'

        if table2Version == 254 and indicatorOfParameter == 203:
            return 'Short wave absorbed at ground (clear)'

        if table2Version == 254 and indicatorOfParameter == 202:
            return 'Short wv absrbd by earth/atmos (clear)'

        if table2Version == 254 and indicatorOfParameter == 201:
            return 'Outgoing long wave at top (clear)'

        if table2Version == 254 and indicatorOfParameter == 200:
            return 'Net long wave at bottom (clear)'

        if table2Version == 254 and indicatorOfParameter == 198:
            return 'Time ave ground ht flx'

        if table2Version == 254 and indicatorOfParameter == 197:
            return 'Incident short wave flux'

        if table2Version == 254 and indicatorOfParameter == 196:
            return 'Surface momentum flux'

        if table2Version == 254 and indicatorOfParameter == 195:
            return 'Surface meridional wind stress'

        if table2Version == 254 and indicatorOfParameter == 194:
            return 'Surface meridional wind (v)'

        if table2Version == 254 and indicatorOfParameter == 193:
            return 'Surface zonal wind stress'

        if table2Version == 254 and indicatorOfParameter == 192:
            return 'Surface zonal wind (u)'

        if table2Version == 254 and indicatorOfParameter == 191:
            return 'Ground/surface cover temperature'

        if table2Version == 254 and indicatorOfParameter == 190:
            return 'Temperature at canopy'

        if table2Version == 254 and indicatorOfParameter == 189:
            return 'Temperature of canopy air space'

        if table2Version == 254 and indicatorOfParameter == 188:
            return 'Surface absolute temperature'

        if table2Version == 254 and indicatorOfParameter == 187:
            return 'Surface temperature'

        if table2Version == 254 and indicatorOfParameter == 186:
            return 'Storage on ground'

        if table2Version == 254 and indicatorOfParameter == 185:
            return 'Storage on canopy'

        if table2Version == 254 and indicatorOfParameter == 184:
            return 'Soil wetness of drainage zone'

        if table2Version == 254 and indicatorOfParameter == 183:
            return 'Soil wetness of root zone'

        if table2Version == 254 and indicatorOfParameter == 182:
            return 'Soil wetness of surface'

        if table2Version == 254 and indicatorOfParameter == 181:
            return 'Surface spec humidity'

        if table2Version == 254 and indicatorOfParameter == 180:
            return 'Vapor pressure of canopy air space'

        if table2Version == 254 and indicatorOfParameter == 179:
            return 'Interception loss'

        if table2Version == 254 and indicatorOfParameter == 178:
            return 'Runoff'

        if table2Version == 254 and indicatorOfParameter == 177:
            return 'Potential sfc evaporation'

        if table2Version == 254 and indicatorOfParameter == 176:
            return 'Bare soil latent heat'

        if table2Version == 254 and indicatorOfParameter == 175:
            return 'Soil temperature of root zone'

        if table2Version == 254 and indicatorOfParameter == 174:
            return 'Soil moisture availability'

        if table2Version == 254 and indicatorOfParameter == 173:
            return 'Large scale moisture source'

        if table2Version == 254 and indicatorOfParameter == 172:
            return 'Large scale latent heating'

        if table2Version == 254 and indicatorOfParameter == 171:
            return 'Neg. hum. corr. moisture source'

        if table2Version == 254 and indicatorOfParameter == 170:
            return 'Vertical moisture advection'

        if table2Version == 254 and indicatorOfParameter == 169:
            return 'Vert. integrated moisture flux conv.'

        if table2Version == 254 and indicatorOfParameter == 168:
            return 'Horiz. moisture flux conv.'

        if table2Version == 254 and indicatorOfParameter == 167:
            return 'Divergence of specific humidity'

        if table2Version == 254 and indicatorOfParameter == 165:
            return 'Gravity wave drag sfc meridional stress'

        if table2Version == 254 and indicatorOfParameter == 164:
            return 'Gravity wave drag sfc zonal stress'

        if table2Version == 254 and indicatorOfParameter == 163:
            return 'Gravity wave drag dv/dt'

        if table2Version == 254 and indicatorOfParameter == 162:
            return 'Gravity wave drag du/dt'

        if table2Version == 254 and indicatorOfParameter == 160:
            return 'Tropopause v-wind component'

        if table2Version == 254 and indicatorOfParameter == 159:
            return 'Tropopause u-wind component'

        if table2Version == 254 and indicatorOfParameter == 158:
            return 'Tropopause temperature'

        if table2Version == 254 and indicatorOfParameter == 157:
            return 'Tropopause pressure'

        if table2Version == 254 and indicatorOfParameter == 156:
            return 'Flight levels v-wind'

        if table2Version == 254 and indicatorOfParameter == 155:
            return 'Flight levels u-wind'

        if table2Version == 254 and indicatorOfParameter == 154:
            return 'Flight levels temperature'

        if table2Version == 254 and indicatorOfParameter == 153:
            return 'Freezing level relative humidity'

        if table2Version == 254 and indicatorOfParameter == 152:
            return 'Freezing level height'

        if table2Version == 254 and indicatorOfParameter == 151:
            return 'Pressure at cloud top'

        if table2Version == 254 and indicatorOfParameter == 150:
            return 'Pressure at cloud base'

        if table2Version == 254 and indicatorOfParameter == 149:
            return 'Mean cloud cover'

        if table2Version == 254 and indicatorOfParameter == 148:
            return 'Storm motion v-component'

        if table2Version == 254 and indicatorOfParameter == 147:
            return 'Storm motion u-component'

        if table2Version == 254 and indicatorOfParameter == 146:
            return 'Maximum wind press. lvl'

        if table2Version == 254 and indicatorOfParameter == 145:
            return 'Shallow convective heating'

        if table2Version == 254 and indicatorOfParameter == 144:
            return 'Shallow conv. moisture source'

        if table2Version == 254 and indicatorOfParameter == 143:
            return 'Convective moisture source'

        if table2Version == 254 and indicatorOfParameter == 142:
            return 'Convective latent heating'

        if table2Version == 254 and indicatorOfParameter == 141:
            return 'Convective inhib. energy'

        if table2Version == 254 and indicatorOfParameter == 140:
            return 'Convective avail. pot.energy'

        if table2Version == 254 and indicatorOfParameter == 139:
            return 'Maximum v-wind'

        if table2Version == 254 and indicatorOfParameter == 138:
            return 'Maximum u-wind'

        if table2Version == 254 and indicatorOfParameter == 137:
            return 'Mask'

        if table2Version == 254 and indicatorOfParameter == 136:
            return 'M s l pressure (mesinger method)'

        if table2Version == 254 and indicatorOfParameter == 135:
            return 'Surface pressure'

        if table2Version == 254 and indicatorOfParameter == 134:
            return 'Ln surface pressure'

        if table2Version == 254 and indicatorOfParameter == 133:
            return 'Geometric mean surface pressure'

        if table2Version == 254 and indicatorOfParameter == 132:
            return 'Topography'

        if table2Version == 254 and indicatorOfParameter == 131:
            return '10 metre v-wind component'

        if table2Version == 254 and indicatorOfParameter == 130:
            return '10 metre u-wind component'

        if table2Version == 254 and indicatorOfParameter == 129:
            return '2 metre dewpoint temperature'

        if table2Version == 254 and indicatorOfParameter == 128:
            return '2 metre temperature'

        if table2Version == 254 and indicatorOfParameter == 127:
            return 'Image'

        if table2Version == 254 and indicatorOfParameter == 123:
            return 'Bound layer dissipation'

        if table2Version == 254 and indicatorOfParameter == 122:
            return 'Sensible heat flux from surface'

        if table2Version == 254 and indicatorOfParameter == 121:
            return 'Latent heat flux from surface'

        if table2Version == 254 and indicatorOfParameter == 117:
            return 'Global radiation'

        if table2Version == 254 and indicatorOfParameter == 116:
            return 'Short wave absorbed by earth/atmosphere'

        if table2Version == 254 and indicatorOfParameter == 115:
            return 'Long-wav rad'

        if table2Version == 254 and indicatorOfParameter == 114:
            return 'Outgoing long wave at top'

        if table2Version == 254 and indicatorOfParameter == 113:
            return 'Net short-wav rad(top)'

        if table2Version == 254 and indicatorOfParameter == 112:
            return 'Net long wave at bottom'

        if table2Version == 254 and indicatorOfParameter == 111:
            return 'Short wave absorbed at ground'

        if table2Version == 254 and indicatorOfParameter == 110:
            return 'Second wave mean period'

        if table2Version == 254 and indicatorOfParameter == 109:
            return 'Second wave direction'

        if table2Version == 254 and indicatorOfParameter == 108:
            return 'Prim wave mean period'

        if table2Version == 254 and indicatorOfParameter == 107:
            return 'Primary wave direction'

        if table2Version == 254 and indicatorOfParameter == 106:
            return 'Mean period swell waves'

        if table2Version == 254 and indicatorOfParameter == 105:
            return 'Sig height swell waves'

        if table2Version == 254 and indicatorOfParameter == 104:
            return 'Direction of swell wave'

        if table2Version == 254 and indicatorOfParameter == 103:
            return 'Mean period wind waves'

        if table2Version == 254 and indicatorOfParameter == 102:
            return 'Sig hght of wind waves'

        if table2Version == 254 and indicatorOfParameter == 101:
            return 'Direction of wind wave'

        if table2Version == 254 and indicatorOfParameter == 100:
            return 'Sig hgt com wave/swell'

        if table2Version == 254 and indicatorOfParameter == 98:
            return 'Ice divergence'

        if table2Version == 254 and indicatorOfParameter == 97:
            return 'Ice growth'

        if table2Version == 254 and indicatorOfParameter == 96:
            return 'V-comp of ice drift'

        if table2Version == 254 and indicatorOfParameter == 95:
            return 'U-comp of ice drift'

        if table2Version == 254 and indicatorOfParameter == 94:
            return 'Speed of ice drift'

        if table2Version == 254 and indicatorOfParameter == 93:
            return 'Direction of ice drift'

        if table2Version == 254 and indicatorOfParameter == 92:
            return 'Ice thickness'

        if table2Version == 254 and indicatorOfParameter == 91:
            return 'Ice concentration'

        if table2Version == 254 and indicatorOfParameter == 89:
            return 'Density'

        if table2Version == 254 and indicatorOfParameter == 87:
            return 'Vegetation'

        if table2Version == 254 and indicatorOfParameter == 86:
            return 'Soil moisture content'

        if table2Version == 254 and indicatorOfParameter == 85:
            return 'Deep soil temperature'

        if table2Version == 254 and indicatorOfParameter == 84:
            return 'Albedo'

        if table2Version == 254 and indicatorOfParameter == 83:
            return 'Roughness length'

        if table2Version == 254 and indicatorOfParameter == 82:
            return 'Dev sea_lev from mean'

        if table2Version == 254 and indicatorOfParameter == 81:
            return 'Land sea mask'

        if table2Version == 254 and indicatorOfParameter == 77:
            return 'Best lifted index (to 500 hpa)'

        if table2Version == 254 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 254 and indicatorOfParameter == 75:
            return 'High cloud cover'

        if table2Version == 254 and indicatorOfParameter == 74:
            return 'Medium cloud cover'

        if table2Version == 254 and indicatorOfParameter == 73:
            return 'Low cloud cover'

        if table2Version == 254 and indicatorOfParameter == 72:
            return 'Convective cloud cover'

        if table2Version == 254 and indicatorOfParameter == 71:
            return 'Cloud cover'

        if table2Version == 254 and indicatorOfParameter == 70:
            return 'Main thermocline anom'

        if table2Version == 254 and indicatorOfParameter == 69:
            return 'Main thermocline depth'

        if table2Version == 254 and indicatorOfParameter == 68:
            return 'Trans thermocline depth'

        if table2Version == 254 and indicatorOfParameter == 67:
            return 'Mixed layer depth'

        if table2Version == 254 and indicatorOfParameter == 66:
            return 'Snow depth'

        if table2Version == 254 and indicatorOfParameter == 65:
            return 'Wat equiv acc snow depth'

        if table2Version == 254 and indicatorOfParameter == 64:
            return 'Snowfall'

        if table2Version == 254 and indicatorOfParameter == 63:
            return 'Convective precipitation'

        if table2Version == 254 and indicatorOfParameter == 62:
            return 'Large scale precipitation'

        if table2Version == 254 and indicatorOfParameter == 61:
            return 'Total precipitation'

        if table2Version == 254 and indicatorOfParameter == 60:
            return 'Thunder probability'

        if table2Version == 254 and indicatorOfParameter == 59:
            return 'Precipitation rate'

        if table2Version == 254 and indicatorOfParameter == 57:
            return 'Evaporation'

        if table2Version == 254 and indicatorOfParameter == 56:
            return 'Saturation deficit'

        if table2Version == 254 and indicatorOfParameter == 55:
            return 'Vapour pressure'

        if table2Version == 254 and indicatorOfParameter == 54:
            return 'Inst. precipitable water'

        if table2Version == 254 and indicatorOfParameter == 53:
            return 'Humidity mixing ratio'

        if table2Version == 254 and indicatorOfParameter == 52:
            return 'Relative humidity'

        if table2Version == 254 and indicatorOfParameter == 51:
            return 'Specific humidity'

        if table2Version == 254 and indicatorOfParameter == 50:
            return 'V-component of current'

        if table2Version == 254 and indicatorOfParameter == 49:
            return 'U-component of current'

        if table2Version == 254 and indicatorOfParameter == 48:
            return 'Speed of current'

        if table2Version == 254 and indicatorOfParameter == 47:
            return 'Direction of current'

        if table2Version == 254 and indicatorOfParameter == 46:
            return 'Vert v-comp shear'

        if table2Version == 254 and indicatorOfParameter == 45:
            return 'Vertical u-comp shear'

        if table2Version == 254 and indicatorOfParameter == 44:
            return 'Divergence'

        if table2Version == 254 and indicatorOfParameter == 43:
            return 'Vorticity'

        if table2Version == 254 and indicatorOfParameter == 42:
            return 'Absolute divergence'

        if table2Version == 254 and indicatorOfParameter == 41:
            return 'Absolute vorticity'

        if table2Version == 254 and indicatorOfParameter == 40:
            return 'Vertical velocity'

        if table2Version == 254 and indicatorOfParameter == 39:
            return 'Omega'

        if table2Version == 254 and indicatorOfParameter == 38:
            return 'Sigma coord vert vel'

        if table2Version == 254 and indicatorOfParameter == 36:
            return 'Velocity potential'

        if table2Version == 254 and indicatorOfParameter == 35:
            return 'Stream function'

        if table2Version == 254 and indicatorOfParameter == 34:
            return 'Meridional wind (v)'

        if table2Version == 254 and indicatorOfParameter == 33:
            return 'Zonal wind (u)'

        if table2Version == 254 and indicatorOfParameter == 32:
            return 'Wind speed'

        if table2Version == 254 and indicatorOfParameter == 31:
            return 'Wind direction'

        if table2Version == 254 and indicatorOfParameter == 30:
            return 'Wave spectra(3)'

        if table2Version == 254 and indicatorOfParameter == 29:
            return 'Wave spectra(2)'

        if table2Version == 254 and indicatorOfParameter == 28:
            return 'Wave spectra(1)'

        if table2Version == 254 and indicatorOfParameter == 27:
            return 'Geopot height anomaly'

        if table2Version == 254 and indicatorOfParameter == 26:
            return 'Pressure anomaly'

        if table2Version == 254 and indicatorOfParameter == 25:
            return 'Temperature anomaly'

        if table2Version == 254 and indicatorOfParameter == 23:
            return 'Radar spectra(3)'

        if table2Version == 254 and indicatorOfParameter == 22:
            return 'Radar spectra(2)'

        if table2Version == 254 and indicatorOfParameter == 21:
            return 'Radar spectra(1)'

        if table2Version == 254 and indicatorOfParameter == 19:
            return 'Lapse rate'

        if table2Version == 254 and indicatorOfParameter == 18:
            return 'Dew point depression'

        if table2Version == 254 and indicatorOfParameter == 17:
            return 'Dew point temperature'

        if table2Version == 254 and indicatorOfParameter == 16:
            return 'Minimum temperature'

        if table2Version == 254 and indicatorOfParameter == 15:
            return 'Maximum temperature'

        if table2Version == 254 and indicatorOfParameter == 14:
            return 'Pseudo-adiabatic potential temperature'

        if table2Version == 254 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 254 and indicatorOfParameter == 12:
            return 'Virtual temperature'

        if table2Version == 254 and indicatorOfParameter == 11:
            return 'Absolute temperature'

        if table2Version == 254 and indicatorOfParameter == 8:
            return 'Geometric height'

        if table2Version == 254 and indicatorOfParameter == 7:
            return 'Geopotential height'

        if table2Version == 254 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 254 and indicatorOfParameter == 3:
            return 'Pressure tendency'

        if table2Version == 254 and indicatorOfParameter == 2:
            return 'Pressure reduced to msl'

        if table2Version == 254 and indicatorOfParameter == 1:
            return 'Pressure'

    return wrapped
