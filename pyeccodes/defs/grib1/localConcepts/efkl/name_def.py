import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 253 and indicatorOfParameter == 228:
            return 'Instantaneous Wind Speed in m/s'

        if table2Version == 253 and indicatorOfParameter == 210:
            return 'Clutter corrected ceflectivity'

        if table2Version == 253 and indicatorOfParameter == 209:
            return 'Multiplicity Of The Flash, Number'

        if table2Version == 253 and indicatorOfParameter == 204:
            return 'Total hail precipitation in kg/m2'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'Instant graupel in kg/m2'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'Graupel precipitation in kg/m2'

        if table2Version == 253 and indicatorOfParameter == 200:
            return 'Kinetic energy of turbulence in J kg-1'

        if table2Version == 253 and indicatorOfParameter == 187:
            return 'Height of cloud top'

        if table2Version == 253 and indicatorOfParameter == 186:
            return 'Cloud base height'

        if table2Version == 253 and indicatorOfParameter == 185:
            return 'Solid precipitation (f.ex. snow+graupel)'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'Instant snowfall rate in mm/s or mm/h'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'Snowfall accumulation  in mm'

        if table2Version == 253 and indicatorOfParameter == 181:
            return 'Instant rain in kg/m2'

        if table2Version == 253 and indicatorOfParameter == 163:
            return 'V-component of wind gust'

        if table2Version == 253 and indicatorOfParameter == 162:
            return 'U-component of wind gust'

        if table2Version == 253 and indicatorOfParameter == 160:
            return 'Convective available potential energy'

        if table2Version == 253 and indicatorOfParameter == 144:
            return 'Precipitation type'

        if table2Version == 253 and indicatorOfParameter == 135:
            return 'Icing warning index, values between 0 ... 4'

        if table2Version == 253 and indicatorOfParameter == 125:
            return 'V-component of momentum flux in N m-2'

        if table2Version == 253 and indicatorOfParameter == 124:
            return 'U-component of momentum flux in N m-2'

        if table2Version == 253 and indicatorOfParameter == 122:
            return 'Sensible heat flux'

        if table2Version == 253 and indicatorOfParameter == 121:
            return 'Latent heat flux'

        if table2Version == 253 and indicatorOfParameter == 117:
            return 'Global radiation accumulation'

        if table2Version == 253 and indicatorOfParameter == 115:
            return 'Long wave radiation accumulation'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'Net long wave radiation accumulation, top of atmosphere'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'Net long wave radiation, top of athmosphere'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'Net short wave radiation accumulation, top of atmosphere'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'Net short wave radiation, top of athmosphere'

        if table2Version == 253 and indicatorOfParameter == 112:
            return 'Net long wave radiation accumulation'

        if table2Version == 253 and indicatorOfParameter == 111:
            return 'Net short wave radiation accumulation'

        if table2Version == 253 and indicatorOfParameter == 103:
            return 'Peak wave period in s'

        if table2Version == 253 and indicatorOfParameter == 102:
            return 'Significant wave height in m'

        if table2Version == 253 and indicatorOfParameter == 101:
            return 'Mean wave direction at spectral peak in degrees'

        if table2Version == 253 and indicatorOfParameter == 91:
            return 'Ice Cover, 1=ice, 0=no ice'

        if table2Version == 253 and indicatorOfParameter == 86:
            return 'Soil Moisture Content in Kg per square meter'

        if table2Version == 253 and indicatorOfParameter == 84:
            return 'ALBEDO 0 to 1'

        if table2Version == 253 and indicatorOfParameter == 83:
            return 'Surface Roughness in Meters'

        if table2Version == 253 and indicatorOfParameter == 81:
            return 'Land Cover, 1=land, 0=sea'

        if table2Version == 253 and indicatorOfParameter == 76:
            return 'Cloud water'

        if table2Version == 253 and indicatorOfParameter == 75:
            return 'High Cloud Amount'

        if table2Version == 253 and indicatorOfParameter == 74:
            return 'Medium Cloud Amount'

        if table2Version == 253 and indicatorOfParameter == 73:
            return 'Low Cloud Amount'

        if table2Version == 253 and indicatorOfParameter == 71:
            return 'Cloudiness 0...1'

        if table2Version == 253 and indicatorOfParameter == 67:
            return 'Mixed layer height in m'

        if table2Version == 253 and indicatorOfParameter == 66:
            return 'Snow Depth in Meters'

        if table2Version == 253 and indicatorOfParameter == 61:
            return 'Total precipitation in kg/m2'

        if table2Version == 253 and indicatorOfParameter == 58:
            return 'Cloud ice'

        if table2Version == 253 and indicatorOfParameter == 57:
            return 'Evaporation in mm'

        if table2Version == 253 and indicatorOfParameter == 54:
            return 'Precipitable water in mm'

        if table2Version == 253 and indicatorOfParameter == 52:
            return 'Relative Humidity in percents'

        if table2Version == 253 and indicatorOfParameter == 51:
            return 'Specific Humidity in kg/kg'

        if table2Version == 253 and indicatorOfParameter == 41:
            return 'Absolute Vorticity in HZ'

        if table2Version == 253 and indicatorOfParameter == 40:
            return 'Vertical Velocity in m/s'

        if table2Version == 253 and indicatorOfParameter == 39:
            return 'Vertical Velocity in pa/s'

        if table2Version == 253 and indicatorOfParameter == 34:
            return 'V wind in m/s'

        if table2Version == 253 and indicatorOfParameter == 33:
            return 'U wind in m/s'

        if table2Version == 253 and indicatorOfParameter == 20:
            return 'Visibility in Meters'

        if table2Version == 253 and indicatorOfParameter == 17:
            return 'Dew point Temperature in K'

        if table2Version == 253 and indicatorOfParameter == 16:
            return 'Minimum Temperature in Celsius'

        if table2Version == 253 and indicatorOfParameter == 15:
            return 'Maximum Temperature in Celsius'

        if table2Version == 253 and indicatorOfParameter == 13:
            return 'Potential temperature'

        if table2Version == 253 and indicatorOfParameter == 11:
            return 'Temperature in Kelvins'

        if table2Version == 253 and indicatorOfParameter == 8:
            return 'Height of level in meters'

        if table2Version == 253 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 253 and indicatorOfParameter == 2:
            return 'Pressure in Pascals'

        if table2Version == 253 and indicatorOfParameter == 1:
            return 'Pressure in Pascals'

        if table2Version == 205 and indicatorOfParameter == 14:
            return 'Ice speed in m/s'

        if table2Version == 205 and indicatorOfParameter == 13:
            return 'Ice Direction in Degrees'

        if table2Version == 205 and indicatorOfParameter == 12:
            return 'Rafted sea ice concentration'

        if table2Version == 205 and indicatorOfParameter == 11:
            return 'Rafted sea ice mean thickness'

        if table2Version == 205 and indicatorOfParameter == 10:
            return 'Ice concentration of ridging'

        if table2Version == 205 and indicatorOfParameter == 9:
            return 'Ice mean thickness'

        if table2Version == 205 and indicatorOfParameter == 8:
            return 'Sea ice velocity (V) in m/s'

        if table2Version == 205 and indicatorOfParameter == 7:
            return 'Sea ice velocity (U) in m/s'

        if table2Version == 205 and indicatorOfParameter == 6:
            return 'Ice degree of ridging'

        if table2Version == 205 and indicatorOfParameter == 5:
            return 'Ice maximum thickness'

        if table2Version == 205 and indicatorOfParameter == 4:
            return 'Ice minimum thickness'

        if table2Version == 205 and indicatorOfParameter == 3:
            return 'Ice thickness'

        if table2Version == 205 and indicatorOfParameter == 2:
            return 'Ice concentration'

        if table2Version == 205 and indicatorOfParameter == 1:
            return 'Sea Temperature in Celsius'

        if table2Version == 203 and indicatorOfParameter == 255:
            return 'Precipitation form, duplicate parameter for HIMAN purposes'

        if table2Version == 203 and indicatorOfParameter == 254:
            return 'Convective inhibition, source data is LFC-500 and EL-500'

        if table2Version == 203 and indicatorOfParameter == 253:
            return 'CAPE, source data is LFC-500 and EL-500, value of CAPE when -40C < T < -10C'

        if table2Version == 203 and indicatorOfParameter == 252:
            return 'CAPE, source data is LFC-500 and EL-500, value of CAPE between 0 .. 3km'

        if table2Version == 203 and indicatorOfParameter == 251:
            return 'Convective available potential energy, value of CAPE between 0 .. 3km'

        if table2Version == 203 and indicatorOfParameter == 250:
            return 'Height of EL in meters, source data is averaged between 0 .. 500m'

        if table2Version == 203 and indicatorOfParameter == 249:
            return 'Height of LFC in meters, source data is averaged between 0 .. 500m'

        if table2Version == 203 and indicatorOfParameter == 248:
            return 'Height of LCL in meters, source data is averaged between 0 .. 500m'

        if table2Version == 203 and indicatorOfParameter == 247:
            return 'Height of EL in hPa, source data is averaged between 0 .. 500m'

        if table2Version == 203 and indicatorOfParameter == 246:
            return 'Height of LFC in hPa, source data is averaged between 0 .. 500m'

        if table2Version == 203 and indicatorOfParameter == 245:
            return 'Height of LCL in hPa, source data is averaged between 0 .. 500m'

        if table2Version == 203 and indicatorOfParameter == 244:
            return 'Convective inhibition (cin)'

        if table2Version == 203 and indicatorOfParameter == 243:
            return 'Convective available potential energy, value of parameter when -40C < T < -10C'

        if table2Version == 203 and indicatorOfParameter == 242:
            return 'Convective available potential energy, source data is LCL-500 and EL-500'

        if table2Version == 203 and indicatorOfParameter == 241:
            return 'Convective available potential energy'

        if table2Version == 203 and indicatorOfParameter == 240:
            return 'Height of EL in meters'

        if table2Version == 203 and indicatorOfParameter == 239:
            return 'Height of LFC in meters'

        if table2Version == 203 and indicatorOfParameter == 238:
            return 'Height of LCL in meters'

        if table2Version == 203 and indicatorOfParameter == 237:
            return 'Height of EL in hPa'

        if table2Version == 203 and indicatorOfParameter == 236:
            return 'Height of LFC in hPa'

        if table2Version == 203 and indicatorOfParameter == 235:
            return 'Height of LCL in hPa'

        if table2Version == 203 and indicatorOfParameter == 234:
            return '100th fractal wind speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 233:
            return '90th fractal wind speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 232:
            return '75th fractal wind speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 231:
            return '50th fractal wind speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 230:
            return '25th fractal wind speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 229:
            return '10th fractal wind speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 228:
            return '0th fractal wind speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 227:
            return '100th fractal wind gust speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 226:
            return '90th fractal wind gust speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 225:
            return '75th fractal wind gust speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 224:
            return '50th fractal wind gust speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 223:
            return '25th fractal wind gust speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 222:
            return '10th fractal wind gust speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 221:
            return '0th fractal wind gust speed in EPS'

        if table2Version == 203 and indicatorOfParameter == 220:
            return '100th fractal cloudiness in EPS'

        if table2Version == 203 and indicatorOfParameter == 219:
            return '90th fractal cloudiness in EPS'

        if table2Version == 203 and indicatorOfParameter == 218:
            return '75th fractal cloudiness in EPS'

        if table2Version == 203 and indicatorOfParameter == 217:
            return '50th fractal cloudiness in EPS'

        if table2Version == 203 and indicatorOfParameter == 216:
            return '25th fractal cloudiness in EPS'

        if table2Version == 203 and indicatorOfParameter == 215:
            return '10th fractal cloudiness in EPS'

        if table2Version == 203 and indicatorOfParameter == 214:
            return '0th fractal cloudiness in EPS'

        if table2Version == 203 and indicatorOfParameter == 213:
            return 'Solid precipitation rate (f.ex. snow+graupel)'

        if table2Version == 203 and indicatorOfParameter == 212:
            return 'Graupel rate in mm/h'

        if table2Version == 203 and indicatorOfParameter == 211:
            return 'Vegetation type'

        if table2Version == 203 and indicatorOfParameter == 210:
            return 'V-component of momentum flux in N m-2'

        if table2Version == 203 and indicatorOfParameter == 209:
            return 'U-component of momentum flux in N m-2'

        if table2Version == 203 and indicatorOfParameter == 208:
            return 'Kinetic energy of turbulence in J kg-1'

        if table2Version == 203 and indicatorOfParameter == 207:
            return 'Soil type'

        if table2Version == 203 and indicatorOfParameter == 206:
            return 'FMIWEATHERSYMBOL1'

        if table2Version == 203 and indicatorOfParameter == 205:
            return 'CAPE, source data is most unstable, value of parameter when -40C < T < -10C'

        if table2Version == 203 and indicatorOfParameter == 204:
            return 'CAPE, source data is most unstable, value of CAPE between 0 .. 3km'

        if table2Version == 203 and indicatorOfParameter == 203:
            return 'Scalar momentum flux in Pa'

        if table2Version == 203 and indicatorOfParameter == 202:
            return 'Sensible heat flux'

        if table2Version == 203 and indicatorOfParameter == 201:
            return 'Latent heat flux'

        if table2Version == 203 and indicatorOfParameter == 200:
            return 'Canopy water'

        if table2Version == 203 and indicatorOfParameter == 199:
            return 'Convective inhibition, source data is most unstable'

        if table2Version == 203 and indicatorOfParameter == 198:
            return 'Ozone anomaly'

        if table2Version == 203 and indicatorOfParameter == 197:
            return 'UV index'

        if table2Version == 203 and indicatorOfParameter == 196:
            return 'UV index maximum'

        if table2Version == 203 and indicatorOfParameter == 195:
            return 'Convective available potential energy, source data is most unstable'

        if table2Version == 203 and indicatorOfParameter == 194:
            return 'Height of EL in meters, source data is found from most unstable level'

        if table2Version == 203 and indicatorOfParameter == 193:
            return '100th fractal precipitation in EPS'

        if table2Version == 203 and indicatorOfParameter == 192:
            return '90th fractal precipitation in EPS'

        if table2Version == 203 and indicatorOfParameter == 191:
            return '75th fractal precipitation in EPS'

        if table2Version == 203 and indicatorOfParameter == 190:
            return '50th fractal precipitation in EPS'

        if table2Version == 203 and indicatorOfParameter == 189:
            return '25th fractal precipitation in EPS'

        if table2Version == 203 and indicatorOfParameter == 188:
            return '10th fractal precipitation in EPS'

        if table2Version == 203 and indicatorOfParameter == 187:
            return '0th fractal precipitation in EPS'

        if table2Version == 203 and indicatorOfParameter == 186:
            return 'Soil Moisture Content in Kg per square meter'

        if table2Version == 203 and indicatorOfParameter == 185:
            return 'Height of LFC in meters, source data is found from most unstable level'

        if table2Version == 203 and indicatorOfParameter == 184:
            return 'Height of LCL in meters, source data is found from most unstable level'

        if table2Version == 203 and indicatorOfParameter == 183:
            return 'Surface Roughness in Meters'

        if table2Version == 203 and indicatorOfParameter == 182:
            return 'Height of EL in hPa, source data is found from most unstable level'

        if table2Version == 203 and indicatorOfParameter == 181:
            return 'Height of LFC in hPa, source data is found from most unstable level'

        if table2Version == 203 and indicatorOfParameter == 180:
            return 'Height of LCL in hPa, source data is found from most unstable level'

        if table2Version == 203 and indicatorOfParameter == 179:
            return '100th fractal (ie. maximum) temperature in EPS'

        if table2Version == 203 and indicatorOfParameter == 178:
            return '90th fractal temperature in EPS'

        if table2Version == 203 and indicatorOfParameter == 177:
            return '75th fractal temperature in EPS'

        if table2Version == 203 and indicatorOfParameter == 176:
            return '50th fractal temperature in EPS'

        if table2Version == 203 and indicatorOfParameter == 175:
            return '25th fractal temperature in EPS'

        if table2Version == 203 and indicatorOfParameter == 174:
            return '10th fractal temperature in EPS'

        if table2Version == 203 and indicatorOfParameter == 173:
            return '0th fractal (ie. minimum) temperature in EPS'

        if table2Version == 203 and indicatorOfParameter == 172:
            return 'Total totals index'

        if table2Version == 203 and indicatorOfParameter == 171:
            return 'Vertical totals index'

        if table2Version == 203 and indicatorOfParameter == 170:
            return 'Cross totals index'

        if table2Version == 203 and indicatorOfParameter == 169:
            return 'Lifted index'

        if table2Version == 203 and indicatorOfParameter == 168:
            return 'Showalter index'

        if table2Version == 203 and indicatorOfParameter == 167:
            return 'Mixed layer height in m'

        if table2Version == 203 and indicatorOfParameter == 166:
            return 'Instant solid precipitation (snow+graupel) in kg/m2'

        if table2Version == 203 and indicatorOfParameter == 165:
            return 'Instant rain in kg/m2'

        if table2Version == 203 and indicatorOfParameter == 164:
            return 'Surface Roughness (momentum) in meters'

        if table2Version == 203 and indicatorOfParameter == 163:
            return 'Inverse of Monin-Obukhov length, i.e. 1/L in m-1'

        if table2Version == 203 and indicatorOfParameter == 161:
            return 'Probability of snow'

        if table2Version == 203 and indicatorOfParameter == 159:
            return 'Extreme forecast index for precipitation'

        if table2Version == 203 and indicatorOfParameter == 158:
            return 'Extreme forecast index for wind gusts'

        if table2Version == 203 and indicatorOfParameter == 157:
            return 'Extreme forecast index for temperature'

        if table2Version == 203 and indicatorOfParameter == 156:
            return 'Extreme forecast index for wind speed'

        if table2Version == 203 and indicatorOfParameter == 155:
            return 'Probability of reaching wind gust speed of 25 m/s in EPS'

        if table2Version == 203 and indicatorOfParameter == 154:
            return 'Probability of reaching wind gust speed of 20 m/s in EPS'

        if table2Version == 203 and indicatorOfParameter == 153:
            return 'Probability of reaching wind gust speed of 15 m/s in EPS'

        if table2Version == 203 and indicatorOfParameter == 152:
            return 'Probability of reaching wind speed of 15 m/s in EPS'

        if table2Version == 203 and indicatorOfParameter == 151:
            return 'Probability of reaching wind speed of 10 m/s in EPS'

        if table2Version == 203 and indicatorOfParameter == 150:
            return 'Equivalent potential temperature from range 0 ..3km in C'

        if table2Version == 203 and indicatorOfParameter == 149:
            return 'Wind speed at 1500 meters in m/s'

        if table2Version == 203 and indicatorOfParameter == 148:
            return 'Storm relative helicity, 0 .. 1 km'

        if table2Version == 203 and indicatorOfParameter == 147:
            return 'Storm relative helicity'

        if table2Version == 203 and indicatorOfParameter == 146:
            return 'Wind shear at 1km in knots'

        if table2Version == 203 and indicatorOfParameter == 145:
            return 'Wind shear in knots'

        if table2Version == 203 and indicatorOfParameter == 144:
            return 'Probability of reaching precipitation of 20 mm in 24 hours in EPS'

        if table2Version == 203 and indicatorOfParameter == 143:
            return 'Probability of reaching precipitation of 10 mm in 24 hours in EPS'

        if table2Version == 203 and indicatorOfParameter == 142:
            return 'Probability of reaching precipitation of 5 mm in 24 hours in EPS'

        if table2Version == 203 and indicatorOfParameter == 141:
            return 'Probability of reaching precipitation of 1 mm in 24 hours in EPS'

        if table2Version == 203 and indicatorOfParameter == 134:
            return 'Probability of big positive temperature anomaly (+8 K) in EPS'

        if table2Version == 203 and indicatorOfParameter == 133:
            return 'Probability of moderate positive temperature anomaly (+4 K) in EPS'

        if table2Version == 203 and indicatorOfParameter == 132:
            return 'Probability of moderate negative temperature anomaly (-4 K) in EPS'

        if table2Version == 203 and indicatorOfParameter == 131:
            return 'Probability of big negative temperature anomaly (-8 K) in EPS'

        if table2Version == 203 and indicatorOfParameter == 130:
            return 'Absolute humidity, kg/m^3'

        if table2Version == 203 and indicatorOfParameter == 129:
            return 'Equivalent potential temperature in K'

        if table2Version == 203 and indicatorOfParameter == 128:
            return 'Net short wave radiation'

        if table2Version == 203 and indicatorOfParameter == 126:
            return 'Net long wave radiation, top of athmosphere'

        if table2Version == 203 and indicatorOfParameter == 122:
            return 'Geopotential in cluster 6 of EPS'

        if table2Version == 203 and indicatorOfParameter == 121:
            return 'Geopotential in cluster 5 of EPS'

        if table2Version == 203 and indicatorOfParameter == 120:
            return 'Geopotential in cluster 4 of EPS'

        if table2Version == 203 and indicatorOfParameter == 119:
            return 'Geopotential in cluster 3 of EPS'

        if table2Version == 203 and indicatorOfParameter == 118:
            return 'Geopotential in cluster 2 of EPS'

        if table2Version == 203 and indicatorOfParameter == 117:
            return 'Geopotential in cluster 1 of EPS'

        if table2Version == 203 and indicatorOfParameter == 116:
            return 'Temperature in cluster 6 of EPS'

        if table2Version == 203 and indicatorOfParameter == 115:
            return 'Temperature in cluster 5 of EPS'

        if table2Version == 203 and indicatorOfParameter == 114:
            return 'Temperature in cluster 4 of EPS'

        if table2Version == 203 and indicatorOfParameter == 113:
            return 'Temperature in cluster 3 of EPS'

        if table2Version == 203 and indicatorOfParameter == 112:
            return 'Temperature in cluster 2 of EPS'

        if table2Version == 203 and indicatorOfParameter == 111:
            return 'Temperature in cluster 1 of EPS'

        if table2Version == 203 and indicatorOfParameter == 110:
            return 'Snowfall rate in mm/s or mm/h'

        if table2Version == 203 and indicatorOfParameter == 109:
            return 'Convective snowfall rate in mm/h'

        if table2Version == 203 and indicatorOfParameter == 108:
            return 'Large scale snowfall rate in mm/h'

        if table2Version == 203 and indicatorOfParameter == 107:
            return 'Convective snow accumulation in kg/m2'

        if table2Version == 203 and indicatorOfParameter == 106:
            return 'Large scale snow accumulation in kg/m2'

        if table2Version == 203 and indicatorOfParameter == 105:
            return 'Cloud condensate'

        if table2Version == 203 and indicatorOfParameter == 104:
            return 'Cloud ice'

        if table2Version == 203 and indicatorOfParameter == 103:
            return 'Icing, code 20041 in BUFR'

        if table2Version == 203 and indicatorOfParameter == 102:
            return 'Sea spray icing for major oceans'

        if table2Version == 203 and indicatorOfParameter == 101:
            return 'Density of dry air in Kg m-3'

        if table2Version == 203 and indicatorOfParameter == 100:
            return 'Ice Cover, 1=ice, 0=no ice'

        if table2Version == 203 and indicatorOfParameter == 99:
            return 'Land Cover, 1=land, 0=sea'

        if table2Version == 203 and indicatorOfParameter == 96:
            return 'Global radiation'

        if table2Version == 203 and indicatorOfParameter == 95:
            return 'Long wave radiation'

        if table2Version == 203 and indicatorOfParameter == 91:
            return 'Simple weather symbol fo HS and others'

        if table2Version == 203 and indicatorOfParameter == 89:
            return 'ALBEDO 0 to 1'

        if table2Version == 203 and indicatorOfParameter == 80:
            return 'Stability index (-50 -> 50)'

        if table2Version == 203 and indicatorOfParameter == 79:
            return 'Total Cloud Cover in %'

        if table2Version == 203 and indicatorOfParameter == 78:
            return 'Cloud water'

        if table2Version == 203 and indicatorOfParameter == 77:
            return 'Loose snow depth in cm'

        if table2Version == 203 and indicatorOfParameter == 75:
            return 'Ground Temperature in Kelvins'

        if table2Version == 203 and indicatorOfParameter == 74:
            return 'Log Surface Pressure'

        if table2Version == 203 and indicatorOfParameter == 73:
            return 'Large Scale Precipitation rate in kg m-2'

        if table2Version == 203 and indicatorOfParameter == 72:
            return 'Convective Precipitation rate in kg m-2'

        if table2Version == 203 and indicatorOfParameter == 71:
            return 'Total Precipitation rate in kg m-2'

        if table2Version == 203 and indicatorOfParameter == 70:
            return 'Height of 0 C level in meters'

        if table2Version == 203 and indicatorOfParameter == 69:
            return 'Net long wave radiation'

        if table2Version == 203 and indicatorOfParameter == 68:
            return 'Snowfall accumulation  in mm'

        if table2Version == 203 and indicatorOfParameter == 63:
            return 'Convective precipitation in 10ths of mm'

        if table2Version == 203 and indicatorOfParameter == 62:
            return 'Large Scale precipitation in 10ths of mm'

        if table2Version == 203 and indicatorOfParameter == 60:
            return 'Calculated smog appearance'

        if table2Version == 203 and indicatorOfParameter == 59:
            return 'Precipitation form'

        if table2Version == 203 and indicatorOfParameter == 58:
            return 'Rain over the last 3 hours in mm'

        if table2Version == 203 and indicatorOfParameter == 57:
            return 'Rain over the last 2 hours in mm'

        if table2Version == 203 and indicatorOfParameter == 56:
            return 'Rain over the last 1 hour in mm'

        if table2Version == 203 and indicatorOfParameter == 55:
            return 'Rain over the last 12 hours in mm'

        if table2Version == 203 and indicatorOfParameter == 54:
            return 'Rain over the last 6 hours in mm'

        if table2Version == 203 and indicatorOfParameter == 53:
            return 'Precalculated weather symbol'

        if table2Version == 203 and indicatorOfParameter == 52:
            return 'Precalculated weather symbol'

        if table2Version == 203 and indicatorOfParameter == 51:
            return 'Snow Depth in Meters'

        if table2Version == 203 and indicatorOfParameter == 50:
            return 'Total precipitation'

        if table2Version == 203 and indicatorOfParameter == 47:
            return 'Precipitable water in mm'

        if table2Version == 203 and indicatorOfParameter == 44:
            return 'Vertical Velocity in m/s'

        if table2Version == 203 and indicatorOfParameter == 43:
            return 'Vertical Velocity in mm/s'

        if table2Version == 203 and indicatorOfParameter == 40:
            return 'Vertical Velocity in pa/s'

        if table2Version == 203 and indicatorOfParameter == 39:
            return 'WindSpeed at 10 m in m/s'

        if table2Version == 203 and indicatorOfParameter == 38:
            return 'FMI Air Quality Index'

        if table2Version == 203 and indicatorOfParameter == 31:
            return 'Absolute Vorticity in HZ/10000'

        if table2Version == 203 and indicatorOfParameter == 28:
            return 'Height of -20 C level in meters'

        if table2Version == 203 and indicatorOfParameter == 27:
            return 'Instantaneous Wind Speed in m/s'

        if table2Version == 203 and indicatorOfParameter == 24:
            return 'V wind in m/s'

        if table2Version == 203 and indicatorOfParameter == 23:
            return 'U wind in m/s'

        if table2Version == 203 and indicatorOfParameter == 22:
            return 'Wind Vector in m/s'

        if table2Version == 203 and indicatorOfParameter == 21:
            return 'Wind speed in m/s'

        if table2Version == 203 and indicatorOfParameter == 20:
            return 'Wind Direction in Degrees'

        if table2Version == 203 and indicatorOfParameter == 19:
            return 'Fog symbol'

        if table2Version == 203 and indicatorOfParameter == 18:
            return 'Front Symbol'

        if table2Version == 203 and indicatorOfParameter == 15:
            return 'Cloud Symbol'

        if table2Version == 203 and indicatorOfParameter == 13:
            return 'Relative Humidity in percents'

        if table2Version == 203 and indicatorOfParameter == 12:
            return 'Specific Humidity in kg/kg'

        if table2Version == 203 and indicatorOfParameter == 10:
            return 'Dew point Temperature in C'

        if table2Version == 203 and indicatorOfParameter == 9:
            return 'Pseudoadiabatic potential temperature in K'

        if table2Version == 203 and indicatorOfParameter == 8:
            return 'Potential temperature'

        if table2Version == 203 and indicatorOfParameter == 4:
            return 'Temperature in Celsius'

        if table2Version == 203 and indicatorOfParameter == 3:
            return 'Height of level in meters'

        if table2Version == 203 and indicatorOfParameter == 2:
            return 'Geopotential'

        if table2Version == 203 and indicatorOfParameter == 1:
            return 'Pressure in hPa'

    return wrapped
