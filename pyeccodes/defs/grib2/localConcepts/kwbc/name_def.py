import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 8:
            return 'Total Precipitation'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'Total Cloud Cover'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'Convective inhibition'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 224:
            return 'Ventilation Rate'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 234:
            return 'Icing severity'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 201:
            return 'Sunshine Duration'

        if discipline == 255 and parameterCategory == 255 and parameterNumber == 255:
            return 'Image data'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 197:
            return 'Ocean Heat Content'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 196:
            return 'Interface Depths'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 195:
            return 'Geometric Depth Below Sea Surface'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 194:
            return 'Barotropic Kinectic Energy'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 193:
            return '3-D Salinity'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 192:
            return '3-D Temperature'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 202:
            return 'Salt Flux'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 201:
            return 'Kinetic Energy'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 200:
            return 'Surface Salinity Trend'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 199:
            return 'Surface Temperature Trend'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 198:
            return 'Assimilative Heat Flux'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 197:
            return 'Net Air-Ocean Heat Flux'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 196:
            return 'Ocean Mixed Layer Potential Density (Reference 2000m)<br'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 195:
            return 'Sea Surface Height Relative to Geoid'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 194:
            return 'Ocean Surface Elevation Relative to Geoid'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 193:
            return 'Extra Tropical Storm Surge'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 192:
            return 'Storm Surge'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 195:
            return 'Barotropic V velocity'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 194:
            return 'Barotropic U velocity'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 193:
            return 'Ocean Mixed Layer V Velocity'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 192:
            return 'Ocean Mixed Layer U Velocity'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 192:
            return 'Wave Steepness'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 193:
            return 'Scatterometer Estimated V Wind Component'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 192:
            return 'Scatterometer Estimated U Wind Component'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 203:
            return 'Field Capacity'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 202:
            return 'Effective radiative skin temperature'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 201:
            return 'Average surface skin temperature'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 200:
            return 'Bare soil surface skin temperature'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 199:
            return 'Land Surface Precipitation Accumulation'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 198:
            return 'Direct evaporation from bare soil'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'Surface Slope Type'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 230:
            return 'Transpiration'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 229:
            return 'Canopy water evaporation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 228:
            return 'Aerodynamic conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 227:
            return 'Water Condensate Meridional Flux (Vertical Int)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 226:
            return 'Water Condensate Zonal Flux (Vertical Int)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 225:
            return 'Water Vapor Meridional Flux (Vertical Int)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 224:
            return 'Water Vapor Zonal Flux (Vertical Int)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 223:
            return 'Water Condensate Flux Convergance (Vertical Int)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 222:
            return 'Water Vapor Flux Convergance (Vertical Int)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 221:
            return 'Water condensate added by precip assimilation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 220:
            return 'Water vapor added by precip assimilation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 219:
            return 'Asymptotic mixing length scale'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 218:
            return 'Land-sea coverage (nearest neighbor) [land=1,sea=0]'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 217:
            return 'Normalized Difference Vegetation Index'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 216:
            return 'Roughness length for heat'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 215:
            return 'Flood plain recharge'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 214:
            return 'Groundwater recharge'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 213:
            return 'Open water evaporation (standing water)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 212:
            return 'Liquid soil moisture content (non-frozen)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 211:
            return 'Surface water storage'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 210:
            return 'Vegetation canopy temperature'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 209:
            return 'Surface exchange coefficients for U and V divided by delta z'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 208:
            return 'Surface exchange coefficients for T and Q divided by delta z'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 207:
            return 'Ice-free water surface'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 206:
            return 'Rate of water dropping from canopy to ground'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 201:
            return 'Wilting Point'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'Vegetation Type'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 195:
            return 'Probability of Wetting Rain, exceeding in 0.10 in a given time period'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 194:
            return 'Probability of precipitation exceeding flash flood guidance values'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 192:
            return 'Probability of Freezing Precipitation'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 197:
            return 'East Longitude (nearest neighbor) (0 - 360)'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 196:
            return 'Latitude (nearest neighbor) (-90 to +90)'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 195:
            return 'Model Layer number (From bottom up)'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 193:
            return 'East Longitude (0 - 360)'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 192:
            return 'Latitude (-90 to +90)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 232:
            return 'Volcanic Ash Forecast Transport and Dispersion'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 219:
            return 'Turbulence Potential Forecast Index'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 218:
            return 'Radiative emissivity'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 217:
            return 'Supercooled Large Droplet (SLD) Potential'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 216:
            return 'Total Probability of Extreme Severe Thunderstorms (Days 2,3)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 215:
            return 'Total Probability of Severe Thunderstorms (Days 2,3)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 214:
            return 'Near IR, White Sky Albedo'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 213:
            return 'Near IR, Black Sky Albedo'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 212:
            return 'Visible, White Sky Albedo'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 211:
            return 'Visible, Black Sky Albedo'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 210:
            return 'High-Level aviation interest'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 209:
            return 'Low-Level aviation interest'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208:
            return 'Confidence - Flight Category'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207:
            return 'Confidence - Visibility'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206:
            return 'Confidence - Ceiling'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205:
            return 'Flight Category'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204:
            return 'Number of mixed layers next to surface'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203:
            return 'Categorical Thunderstorm (1-yes, 0-no)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202:
            return 'Significant Wind probability'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201:
            return 'Significant Hail probability'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200:
            return 'Significant Tornado probability'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199:
            return 'Wind probability'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198:
            return 'Hail probability'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197:
            return 'Tornado probability'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196:
            return 'High risk convective outlook'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195:
            return 'Moderate risk convective outlook'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 194:
            return 'Slight risk convective outlook'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192:
            return 'Lightning'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 196:
            return 'Maximum/Composite radar reflectivity'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 195:
            return 'Derived radar reflectivity'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 194:
            return 'Derived radar reflectivity backscatter from parameterized convection'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 193:
            return 'Derived radar reflectivity backscatter from ice'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 192:
            return 'Derived radar reflectivity backscatter from rain'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 199:
            return 'Ozone production from col ozone term'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 198:
            return 'Ozone production from temperature term'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 197:
            return 'Ozone tendency'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 196:
            return 'Ozone production'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 195:
            return 'Ozone vertical diffusion'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 194:
            return 'Categorical Ozone Concentration'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193:
            return 'Ozone Concentration (PPB)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195:
            return 'Integrated column particulate matter (fine)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194:
            return 'Particulate matter (fine)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193:
            return 'Particulate matter (fine)'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192:
            return 'Particulate matter (coarse)'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 198:
            return 'Leaf Area Index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 197:
            return 'Updraft Helicity'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 'Convective Weather Detection Index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194:
            return 'Richardson Number'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 200:
            return 'Convective Cloud Mass Flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 197:
            return 'Cloud Forcing Net Long Wave Flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 196:
            return 'Clear Sky Downward Long Wave Flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 195:
            return 'Clear Sky Upward Long Wave Flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 194:
            return 'Long-Wave Radiative Heating Rate'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 205:
            return 'Upward Total radiation Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 204:
            return 'Downward Total radiation Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 203:
            return 'Near IR Diffuse Downward Solar Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 202:
            return 'Near IR Beam Downward Solar Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 201:
            return 'Visible Diffuse Downward Solar Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 200:
            return 'Visible Beam Downward Solar Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199:
            return 'Cloud Forcing Net Solar Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198:
            return 'Clear Sky Upward Solar Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 197:
            return 'Solar Radiative Heating Rate'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 196:
            return 'Clear Sky Downward Solar Flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 195:
            return 'Clear sky UV-B downward solar flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 194:
            return 'UV-B downward solar flux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 212:
            return 'Pressure (nearest grid point)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 211:
            return 'Geopotential Height (nearest grid point)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 210:
            return 'Mass Point Model Surface'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 209:
            return 'Convective detrainment mass flux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 208:
            return 'Convective downdraft mass flux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 207:
            return 'Convective updraft mass flux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 206:
            return 'Natural Log of Surface Pressure'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 205:
            return 'Layer Thickness'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 204:
            return 'Y-gradient of Height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 203:
            return 'X-gradient of Height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 202:
            return 'Y-gradient of Log Pressure'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 201:
            return 'X-gradient of Log Pressure'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 200:
            return 'Pressure of level from which parcel was lifted'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 199:
            return '3-hr pressure tendency (Std. Atmos. Reduction)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 198:
            return 'MSLP (MAPS System Reduction)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'MSLP (Eta model reduction)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 219:
            return 'Potential Vorticity (Mass-Weighted)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 218:
            return 'Velocity Point Model Surface'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 217:
            return 'Convective Gravity wave drag meridional acceleration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 216:
            return 'Convective Gravity wave drag zonal acceleration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 215:
            return 'Omega (Dp/Dt) divide by density'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 214:
            return 'Tendency of vertical velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 213:
            return 'Convective meridional momentum mixing acceleration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 212:
            return 'Convective zonal momentum mixing acceleration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 211:
            return 'Gravity wave drag meridional acceleration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 210:
            return 'Gravity wave drag zonal acceleration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 209:
            return 'Vertical Diffusion Meridional Acceleration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 208:
            return 'Vertical Diffusion Zonal Acceleration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 207:
            return 'Covariance between Temperature and Meridional Components of the wind.'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 206:
            return 'Covariance between Temperature and Zonal Components of the wind.'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 205:
            return 'Covariance between Meridional and Zonal Components of the wind.'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 204:
            return 'Vertical Eddy Diffusivity Heat exchange'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 203:
            return 'Longitude of Presure Point'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 202:
            return 'Latitude of Presure Point'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 201:
            return 'Longitude of V Wind Component of Velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 200:
            return 'Latitude of V Wind Component of Velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 199:
            return 'Longitude of U Wind Component of Velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 198:
            return 'Latitude of U Wind Component of Velocity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 225:
            return 'Freezing Rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 224:
            return 'Convective precipitation (nearest grid point)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 223:
            return 'Total precipitation (nearest grid point)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 222:
            return 'Snow temperature, depth-avg'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 221:
            return 'Liquid precipitation (rainfall)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 220:
            return 'Minimum specific humidity at 2m'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 219:
            return 'Maximum specific humidity at 2m'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 218:
            return 'Specific humidity at top of viscous sublayer'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 217:
            return 'Large scale moistening rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 216:
            return 'Condensation Pressure of Parcali Lifted From Indicate Surface'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 215:
            return 'Vertical Diffusion Moistening Rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 214:
            return 'Shallow Convective Moistening Rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 213:
            return 'Deep Convective Moistening Rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 212:
            return 'Sublimation (evaporation from snow)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 211:
            return 'Evaporation - Precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 210:
            return 'Total column-integrated melting ice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 209:
            return 'Total column-integrated supercooled liquid water'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 'Snow temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207:
            return 'Number concentration for ice particles'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206:
            return 'Total Icing Potential Diagnostic'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198:
            return 'Minimum Relative Humidity'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 204:
            return 'Tropical Cyclone Heat Potential'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 203:
            return 'Potential temperature at top of viscous sublayer'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 202:
            return 'Vertical Diffusion Heating rate'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 201:
            return 'Shallow Convective Heating rate'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 200:
            return 'Standard Dev. of IR Temp. over 1x1 deg. area'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 199:
            return 'Temperature Tendency By Non-radiation Physics'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 198:
            return 'Temperature Tendency By All Physics'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 197:
            return 'Total Downward Heat Flux at Surface'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 196:
            return 'Deep Convective Heating rate'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 195:
            return 'Large Scale Condensate Heating rate'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 'Relative Error Variance'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'Temperature tendency by all radiation'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197:
            return 'Soil porosity'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196:
            return 'Direct evaporation cease (soil moisture)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'Transpiration stress-onset (soil moisture)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'Number of soil layers in root zone'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'Liquid volumetric soil moisture (non-frozen)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 204:
            return 'Humidity parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 205:
            return 'Soil moisture parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 203:
            return 'Temperature parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 202:
            return 'Solar parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 200:
            return 'Minimal stomatal resistance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'Canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'Blackadar mixing length scale'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'Plant canopy surface water'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 'Exchange coefficient'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194:
            return 'Moisture availability'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193:
            return 'Ground heat flux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192:
            return 'Volumetric soil moisture content'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 193:
            return 'Storm surface runoff'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 192:
            return 'Baseflow-groundwater runoff'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 194:
            return 'Seconds prior to initial reference time (defined in Section 1)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193:
            return 'Snow free albedo'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 'Maximum snow albedo'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192:
            return 'Ozone mixing ratio'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 'Best (4-layer) lifted index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 'Surface lifted index'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199:
            return 'Ice fraction of total condensate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198:
            return 'Total column-integrated condensate'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 197:
            return 'Total column-integrated cloud ice'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196:
            return 'Total column-integrated cloud water'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194:
            return 'Convective cloud efficiency'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193:
            return 'Cloud work function'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192:
            return 'Non-convective cloud cover'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 193:
            return 'Upward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192:
            return 'Downward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 196:
            return 'UV index '

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193:
            return 'Upward short-wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192:
            return 'Downward short-wave radiation flux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 197:
            return '5-wave geopotential height anomaly'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 196:
            return 'Planetary boundary layer height'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 195:
            return 'Meridional flux of gravity wave stress'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194:
            return 'Zonal flux of gravity wave stress'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193:
            return '5-wave geopotential height'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 197:
            return 'Frictional velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196:
            return 'Drag coefficient'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195:
            return 'V-component storm motion'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194:
            return 'U-component storm motion'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193:
            return 'Horizontal momentum flux'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192:
            return 'Vertical speed shear'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'Water equivalent of accumulated snow depth (deprecated)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205:
            return 'Total column integrated snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204:
            return 'Total column integrated rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 'Rime factor'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202:
            return 'Rain fraction of total cloud water'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201:
            return 'Snow cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200:
            return 'Potential evaporation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199:
            return 'Potential evaporation'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 193:
            return 'Percent frozen precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196:
            return 'Convective precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195:
            return 'Categorical snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194:
            return 'Categorical ice pellets'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193:
            return 'Categorical freezing rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192:
            return 'Categorical rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197:
            return 'Horizontal moisture convergence'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195:
            return 'Condensate'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192:
            return 'Snow phase change heat flux'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'Convective available potential energy'

    return wrapped
