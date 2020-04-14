import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 235:
            return 'Maximum snow height during contiguous accumulating snow period (coupled with snow age)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'Skin conductivity (ratio ground heat flux to temperature difference soil-skin layer)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 235:
            return 'Random pattern for  the stochastically perturbed parametrization tendencies (SPPT) scheme at levels without tapering. If multi-scale random patterns are used, RAPA_SPPT is the sum of those.'

        constituentType = h.get_l('constituentType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62101:
            return 'Number of days since the start of birch (betula) pollen season (if present day is in the season: zero outside season)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62200:
            return 'Pollen number emission flux for ragweed  (ambrosia) '

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62200:
            return 'Length of ragweed  (ambrosia) pollen season'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62200:
            return 'Number of days since the start of ragweed  (ambrosia) pollen season (if present day is outside the season: length of current season)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62200:
            return 'Number of days since the start of ragweed  (ambrosia) pollen season (if present day is in the season: zero outside season)'

        typeOfGeneratingProcess = h.get_l('typeOfGeneratingProcess')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'Cumulated 2m temperature sum threshold for the end of  ragweed  (ambrosia) pollen season (climatological)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'Cumulated 2m temperature sum threshold for the start of  ragweed  (ambrosia) pollen season (climatological)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62200:
            return 'Cumulated weighted 2m temperature sum of daily values for ragweed  (ambrosia) pollen'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'Height correction for emission (decreasing emission with height) for ragweed  (ambrosia) '

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62200:
            return 'State of the ragweed  (ambrosia) season (eq.zero before and after season, the higher, the more plants are flowering)'

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62200:
            return 'Sum of released ragweed  (ambrosia) pollen into the reservoir (daily sum)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62200:
            return 'Number of ragweed  (ambrosia) pollen released into the reservoir (new)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62200:
            return 'Number of ragweed  (ambrosia) pollen in the reservoir (previous timestep)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62300:
            return 'Pollen number emission flux for grasses (poaceae) '

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62300:
            return 'Length of grasses (poaceae) pollen season'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62300:
            return 'Number of days since the start of grasses (poaceae) pollen season (if present day is outside the season: length of current season)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62300:
            return 'Number of days since the start of grasses (poaceae) pollen season (if present day is in the season: zero outside season)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'Cumulated 2m temperature sum threshold for the end of  grasses (poaceae) pollen season (climatological)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'Cumulated 2m temperature sum threshold for the start of  grasses (poaceae) pollen season (climatological)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62300:
            return 'Cumulated weighted 2m temperature sum of daily values for grasses (poaceae) pollen'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'Height correction for emission (decreasing emission with height) for grasses (poaceae) '

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62300:
            return 'State of the grasses (poaceae) season (eq.zero before and after season, the higher, the more plants are flowering)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62300:
            return 'Sum of released grasses (poaceae) pollen into the reservoir (daily sum)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62300:
            return 'Number of grasses (poaceae) pollen released into the reservoir (new)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62300:
            return 'Number of grasses (poaceae) pollen in the reservoir (previous timestep)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62100:
            return 'Pollen number emission flux for alder (alnus) '

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62100:
            return 'Length of alder (alnus) pollen season'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62100:
            return 'Number of days since the start of alder (alnus) pollen season (if present day is outside the season: length of current season)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62100:
            return 'Number of days since the start of alder (alnus) pollen season (if present day is in the season: zero outside season)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'Cumulated 2m temperature sum threshold for the end of  alder (alnus) pollen season (climatological)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'Cumulated 2m temperature sum threshold for the start of  alder (alnus) pollen season (climatological)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62100:
            return 'Cumulated weighted 2m temperature sum of daily values for alder (alnus) pollen'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'Height correction for emission (decreasing emission with height) for alder (alnus) '

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62100:
            return 'State of the alder (alnus) season (eq.zero before and after season, the higher, the more plants are flowering)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62100:
            return 'Sum of released alder (alnus) pollen into the reservoir (daily sum)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62100:
            return 'Number of alder (alnus) pollen released into the reservoir (new)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62100:
            return 'Number of alder (alnus) pollen in the reservoir (previous timestep)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62101:
            return 'Pollen number emission flux for birch (betula) '

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62101:
            return 'Length of birch (betula) pollen season'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62101:
            return 'Number of days since the start of birch (betula) pollen season (if present day is outside the season: length of current season)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'Cumulated 2m temperature sum threshold for the end of birch (betula) pollen season (climatological)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'Cumulated 2m temperature sum threshold for the start of birch (betula) pollen season (climatological)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62101:
            return 'Cumulated weighted 2m temperature sum of daily values for birch (betula) pollen'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'Height correction for emission (decreasing emission with height) for birch (betula) '

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62101:
            return 'State of the birch (betula) season (eq.zero before and after season, the higher, the more plants are flowering)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62101:
            return 'Sum of released birch (betula) pollen into the reservoir (daily sum)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62101:
            return 'Number of birch (betula) pollen released into the reservoir (new)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62101:
            return 'Number of birch (betula) pollen in the reservoir (previous timestep)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'evaporation of plants (integrated since "nightly reset")'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 234:
            return 'Standard deviation of saturation deficit'

        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 205 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'Maximum 10m convective gust'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 4:
            return 'mean radiation temperature of an environment assumed black body related to standing human'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192 and typeOfStatisticalProcessing == 2:
            return 'Maximum of Lightning Potential Index (over given time interval)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 207 and typeOfStatisticalProcessing == 2:
            return 'Maximum updraft track (over given time interval and column)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 206 and typeOfStatisticalProcessing == 2:
            return 'Maximum rotation amplitude (positive or negative)  (over given time interval and column)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 203:
            return 'Threshold friction velocity'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 2:
            return 'Slope angle - topography'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 3:
            return 'Slope aspect - topography'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 1:
            return 'Horizon angle - topography'

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 0:
            return 'Sky-view-factor'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 234:
            return 'sea ice albedo - diffusive solar (0.3 - 5.0 m-6) '

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'Antropogenic heat flux (e.g. urban heating, traffic)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'Impervious (paved or sealed) surface fraction'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 2:
            return 'Liquid water potential temperature - total water specific humidity covariance'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 1:
            return 'Total water specific humidity variance'

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 0:
            return 'Liquid water potential temperature variance'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 192 and typeOfFirstFixedSurface == 10:
            return 'Diagnostic total column of activity concentration of radionuclides'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 202:
            return 'Norm of (vertical) wind shear vector between two levels'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 201:
            return 'Mean vertical wind shear for specified layer or layer-mean vertical wind shear'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 28:
            return 'Wind divergence (3D)'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 27:
            return 'Relative geostrophic vorticity advection'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 26:
            return 'Relative geostrophic vorticity'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 'Universal thermal climate index without direct incident short wave radiation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 195 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m temperature, corrected in presence of snow'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 199:
            return 'Swiss coodinate (west-east)'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 198:
            return 'Swiss coodinate (south-north)'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 2:
            return 'Thunderstorm index for Switzerland (day time)'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 1:
            return 'Thunderstorm index for Switzerland (night time)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 233:
            return 'Percentage of precipitation in snow (from total prec.)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 12:
            return 'Vertical velocity fluctuation (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 11:
            return 'Meridional velocity fluctuation (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 10:
            return 'Zonal velocity fluctuation (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 9:
            return 'Vertical velocity fluctuation (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 8:
            return 'Cross-wind velocity fluctuation (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 7:
            return 'Along-wind velocity fluctuation (Hanna)'

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 197 and typeOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 3:
            return 'Pressure difference between cloud base and cloud top'

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Downward long-wave radiation flux at surface based on T_SO(0) (time average)'

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 2 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Downward long-wave radiation flux at surface based on T_G (time average)'

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Downward long-wave radiation flux at surface based on T_2M (time average)'

        if discipline == 215 and parameterCategory == 19 and parameterNumber == 0:
            return 'Luminosity'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 194:
            return 'Height of level of free convection of mixed (mean) layer parcel'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 6:
            return 'Vertical lagrangian timescale (direct) (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 5:
            return 'Meridional lagrangian timescale (direct) (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 4:
            return 'Zonal lagrangian timescale (direct) (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 3:
            return 'Vertical lagrangian timescale (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 2:
            return 'Cross-wind lagrangian timescale (Hanna)'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 1:
            return 'Along-wind lagrangian timescale (Hanna)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 205:
            return 'Downward short wave radiation flux at surface on vertical surface facing west (time average)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 204:
            return 'Downward short wave radiation flux at surface on vertical surface facing south (time average)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 203:
            return 'Downward short wave radiation flux at surface on vertical surface facing north (time average)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 202:
            return 'Downward short wave radiation flux at surface on vertical surface facing east (time average)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 201:
            return 'Downward short wave radiation flux at surface on horizontal plane (time average)'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Enthalpy'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 'Enthalpy'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 206 and typeOfFirstFixedSurface == 1:
            return 'Relative duration of sunshine (DURSUN * 100 / DURSON M)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 205 and typeOfStatisticalProcessing == 11 and typeOfFirstFixedSurface == 1:
            return 'Possible astronomical maximum of sunshine'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'Wind direction in azimuth class'

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 0:
            return 'Wind direction in azimuth class'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194 and typeOfFirstFixedSurface == 10:
            return 'Deep convection index'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 232:
            return 'Percentage of convective precipitation (from total prec)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 231:
            return 'Cloud ice ratio qi/(qc+qi)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 233:
            return 'Divergence modified turbulence index (Ellrod and Knox)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 232:
            return 'Divergence trend (scaled divergence tendency needed for CAT_DVI)'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 29:
            return 'Deformation of horizontal wind field'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 231:
            return 'Ellrod and Knapp turbulence index2'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 230:
            return 'Ellrod and Knapp turbulence index1'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 197:
            return 'Gauss Boaga Coordinates South to North, West Sector'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 196:
            return 'Gauss Boaga Coordinates West to East, West Sector'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 195:
            return 'Gauss Boaga Coordinates South to North,East Sector'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 194:
            return 'Gauss Boaga Coordinates West to East,East Sector'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 201:
            return 'Downward direct short wave radiation flux at surface on horizontal plane (time average)'

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 0:
            return 'Adedokun 2 Index'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 229:
            return ' probability density function of EDP for turbulence  greater well defined threshold and model grid box'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 196:
            return 'Height of -10 degree Celsius isotherm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 230 and typeOfStatisticalProcessing == 1:
            return 'rain-drain-from-snowpack'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192:
            return 'Lightning Potential Index'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 228:
            return 'Eddy Dissipation Rate Total Col-Max. Lower FIR'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 227:
            return 'Mass density of hail'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 204:
            return 'Mass density of cloud ice'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 203:
            return 'Mass density of cloud droplets'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 226:
            return 'Mass density of graupel'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 225:
            return 'Mass density of snow '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 224:
            return 'Mass density of rain '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 223:
            return 'Number density of hail'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 222:
            return 'Number density of graupel'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 221:
            return 'Number density of snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 219:
            return 'Specific number concentration of hail'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 218:
            return 'Specific number concentration of graupel'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 217:
            return 'Specific number concentration of snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 229:
            return 'Number density of rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 228:
            return 'Specific number concentration of rain'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 201:
            return 'Peak frequency (interpolated)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 200 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'soil moisture index (multilayers)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 220:
            return 'relative humidity over mixed phase'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 193:
            return 'Area weights for regular lon-lat grid '

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 197 and typeOfStatisticalProcessing == 1:
            return 'snow_rate,qualified,BRD'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 196 and typeOfStatisticalProcessing == 1:
            return 'snow_rate,BRD'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 195 and typeOfStatisticalProcessing == 1:
            return 'hail flag,BRD'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 194 and typeOfStatisticalProcessing == 1:
            return 'precipitation phase,BRD'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 193 and typeOfStatisticalProcessing == 1:
            return 'precipitation,BRD'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'precipitation, qualified,BRD'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfFirstFixedSurface == 1:
            return 'Downward diffusive short wave radiation flux at surface ( mean over forecast time)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 216:
            return 'Total column integrated cloud ice (diagnostic) '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 215:
            return 'Total column integrated cloud water (diagnostic) '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 214:
            return 'Total column integrated water vapour (diagnostic) '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 213:
            return 'Specific cloud ice content (diagnostic) '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 212:
            return 'Specific cloud water content (diagnostic)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 211:
            return 'Specific humidity (diagnostic)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 198:
            return 'Height of Radarbeam above Ground'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 197:
            return 'Radar Blacklist'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 196:
            return 'Radar Quality Information'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 195:
            return 'Radar Precipitation Rate'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 227:
            return 'Eddy dissipitation rate of TKE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 226:
            return 'Eddy Dissipation Rate Total Col-Max. Upper UIR'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 225:
            return 'Eddy Dissipation Rate Total Col-Max. Lower UIR'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 224:
            return 'Eddy Dissipation Rate Total Col-Max. Upper FIR'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 223:
            return 'Albedo - near infrared (0.7 - 5.0 m-6)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 223 and typeOfStatisticalProcessing == 0:
            return 'Albedo - near infrared - time average (0.7 - 5.0 m-6) '

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 222:
            return 'Albedo - UV (0.3 - 0.7 m-6)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 222 and typeOfStatisticalProcessing == 0:
            return 'Albedo - diffusive solar  (0.3 - 0.7 m-6)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfFirstFixedSurface == 1:
            return 'Downward direct short wave radiation flux at surface'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 210 and typeOfFirstFixedSurface == 114:
            return 'Liquid water content in the snow in - multi level '

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 254:
            return 'DUMMY_254'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 253:
            return 'DUMMY_253'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 252:
            return 'DUMMY_252'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 251:
            return 'DUMMY_251'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 250:
            return 'DUMMY_250'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 249:
            return 'DUMMY_249'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 248:
            return 'DUMMY_248'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 247:
            return 'DUMMY_247'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 246:
            return 'DUMMY_246'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 245:
            return 'DUMMY_245'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 244:
            return 'DUMMY_244'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 243:
            return 'DUMMY_243'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 242:
            return 'DUMMY_242'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 241:
            return 'DUMMY_241'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 240:
            return 'DUMMY_240'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 239:
            return 'DUMMY_239'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 238:
            return 'DUMMY_238'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 237:
            return 'DUMMY_237'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 236:
            return 'DUMMY_236'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 235:
            return 'DUMMY_235'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 234:
            return 'DUMMY_234'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 233:
            return 'DUMMY_233'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 232:
            return 'DUMMY_232'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 231:
            return 'DUMMY_231'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 230:
            return 'DUMMY_230'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 229:
            return 'DUMMY_229'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 228:
            return 'DUMMY_228'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 227:
            return 'DUMMY_227'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 226:
            return 'DUMMY_226'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 225:
            return 'DUMMY_225'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 224:
            return 'DUMMY_224'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 223:
            return 'DUMMY_223'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 222:
            return 'DUMMY_222'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 221:
            return 'DUMMY_221'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 220:
            return 'DUMMY_220'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 219:
            return 'DUMMY_219'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 218:
            return 'DUMMY_218'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 217:
            return 'DUMMY_217'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 216:
            return 'DUMMY_216'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 215:
            return 'DUMMY_215'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 214:
            return 'DUMMY_214'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 213:
            return 'DUMMY_213'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 212:
            return 'DUMMY_212'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 211:
            return 'DUMMY_211'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 210:
            return 'DUMMY_210'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 209:
            return 'DUMMY_209'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 208:
            return 'DUMMY_208'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 207:
            return 'DUMMY_207'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 206:
            return 'DUMMY_206'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 205:
            return 'DUMMY_205'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 204:
            return 'DUMMY_204'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 203:
            return 'DUMMY_203'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 202:
            return 'DUMMY_202'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 201:
            return 'DUMMY_201'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 200:
            return 'DUMMY_200'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 199:
            return 'DUMMY_199'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 198:
            return 'DUMMY_198'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 197:
            return 'DUMMY_197'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 196:
            return 'DUMMY_196'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 195:
            return 'DUMMY_195'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 194:
            return 'DUMMY_194'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 193:
            return 'DUMMY_193'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 192:
            return 'DUMMY_192'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 191:
            return 'DUMMY_191'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 190:
            return 'DUMMY_190'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 189:
            return 'DUMMY_189'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 188:
            return 'DUMMY_188'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 187:
            return 'DUMMY_187'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 186:
            return 'DUMMY_186'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 185:
            return 'DUMMY_185'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 184:
            return 'DUMMY_184'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 183:
            return 'DUMMY_183'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 182:
            return 'DUMMY_182'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 181:
            return 'DUMMY_181'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 180:
            return 'DUMMY_180'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 179:
            return 'DUMMY_179'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 178:
            return 'DUMMY_178'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 177:
            return 'DUMMY_177'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 176:
            return 'DUMMY_176'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 175:
            return 'DUMMY_175'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 174:
            return 'DUMMY_174'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 173:
            return 'DUMMY_173'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 172:
            return 'DUMMY_172'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 171:
            return 'DUMMY_171'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 170:
            return 'DUMMY_170'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 169:
            return 'DUMMY_169'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 168:
            return 'DUMMY_168'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 167:
            return 'DUMMY_167'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 166:
            return 'DUMMY_166'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 165:
            return 'DUMMY_165'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 164:
            return 'DUMMY_164'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 163:
            return 'DUMMY_163'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 162:
            return 'DUMMY_162'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 161:
            return 'DUMMY_161'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 160:
            return 'DUMMY_160'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 159:
            return 'DUMMY_159'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 158:
            return 'DUMMY_158'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 157:
            return 'DUMMY_157'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 156:
            return 'DUMMY_156'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 155:
            return 'DUMMY_155'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 154:
            return 'DUMMY_154'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 153:
            return 'DUMMY_153'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 152:
            return 'DUMMY_152'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 151:
            return 'DUMMY_151'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 150:
            return 'DUMMY_150'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 149:
            return 'DUMMY_149'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 148:
            return 'DUMMY_148'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 147:
            return 'DUMMY_147'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 146:
            return 'DUMMY_146'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 145:
            return 'DUMMY_145'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 144:
            return 'DUMMY_144'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 143:
            return 'DUMMY_143'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 142:
            return 'DUMMY_142'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 141:
            return 'DUMMY_141'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 140:
            return 'DUMMY_140'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 139:
            return 'DUMMY_139'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 138:
            return 'DUMMY_138'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 137:
            return 'DUMMY_137'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 136:
            return 'DUMMY_136'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 135:
            return 'DUMMY_135'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 134:
            return 'DUMMY_134'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 133:
            return 'DUMMY_133'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 132:
            return 'DUMMY_132'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 131:
            return 'DUMMY_131'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 130:
            return 'DUMMY_130'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 129:
            return 'DUMMY_129'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 128:
            return 'DUMMY_128'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 127:
            return 'DUMMY_127'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 126:
            return 'DUMMY_126'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 125:
            return 'DUMMY_125'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 124:
            return 'DUMMY_124'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 123:
            return 'DUMMY_123'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 122:
            return 'DUMMY_122'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 121:
            return 'DUMMY_121'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 120:
            return 'DUMMY_120'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 119:
            return 'DUMMY_119'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 118:
            return 'DUMMY_118'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 117:
            return 'DUMMY_117'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 116:
            return 'DUMMY_116'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 115:
            return 'DUMMY_115'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 114:
            return 'DUMMY_114'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 113:
            return 'DUMMY_113'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 112:
            return 'DUMMY_112'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 111:
            return 'DUMMY_111'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 110:
            return 'DUMMY_110'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 109:
            return 'DUMMY_109'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 108:
            return 'DUMMY_108'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 107:
            return 'DUMMY_107'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 106:
            return 'DUMMY_106'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 105:
            return 'DUMMY_105'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 104:
            return 'DUMMY_104'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 103:
            return 'DUMMY_103'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 102:
            return 'DUMMY_102'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 101:
            return 'DUMMY_101'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 100:
            return 'DUMMY_100'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 99:
            return 'DUMMY_99'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 98:
            return 'DUMMY_98'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 97:
            return 'DUMMY_97'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 96:
            return 'DUMMY_96'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 95:
            return 'DUMMY_95'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 94:
            return 'DUMMY_94'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 93:
            return 'DUMMY_93'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 92:
            return 'DUMMY_92'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 91:
            return 'DUMMY_91'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 90:
            return 'DUMMY_90'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 89:
            return 'DUMMY_89'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 88:
            return 'DUMMY_88'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 87:
            return 'DUMMY_87'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 86:
            return 'DUMMY_86'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 85:
            return 'DUMMY_85'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 84:
            return 'DUMMY_84'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 83:
            return 'DUMMY_83'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 82:
            return 'DUMMY_82'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 81:
            return 'DUMMY_81'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 80:
            return 'DUMMY_80'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 79:
            return 'DUMMY_79'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 78:
            return 'DUMMY_78'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 77:
            return 'DUMMY_77'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 76:
            return 'DUMMY_76'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 75:
            return 'DUMMY_75'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 74:
            return 'DUMMY_74'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 73:
            return 'DUMMY_73'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 72:
            return 'DUMMY_72'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 71:
            return 'DUMMY_71'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 70:
            return 'DUMMY_70'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 69:
            return 'DUMMY_69'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 68:
            return 'DUMMY_68'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 67:
            return 'DUMMY_67'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 66:
            return 'DUMMY_66'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 65:
            return 'DUMMY_65'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 64:
            return 'DUMMY_64'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 63:
            return 'DUMMY_63'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 62:
            return 'DUMMY_62'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 61:
            return 'DUMMY_61'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 60:
            return 'DUMMY_60'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 59:
            return 'DUMMY_59'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 58:
            return 'DUMMY_58'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 57:
            return 'DUMMY_57'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 56:
            return 'DUMMY_56'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 55:
            return 'DUMMY_55'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 54:
            return 'DUMMY_54'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 53:
            return 'DUMMY_53'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 52:
            return 'DUMMY_52'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 51:
            return 'DUMMY_51'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 50:
            return 'DUMMY_50'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 49:
            return 'DUMMY_49'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 48:
            return 'DUMMY_48'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 47:
            return 'DUMMY_47'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 46:
            return 'DUMMY_46'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 45:
            return 'DUMMY_45'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 44:
            return 'DUMMY_44'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 43:
            return 'DUMMY_43'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 42:
            return 'DUMMY_42'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 41:
            return 'DUMMY_41'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 40:
            return 'DUMMY_40'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 39:
            return 'DUMMY_39'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 38:
            return 'DUMMY_38'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 37:
            return 'DUMMY_37'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 36:
            return 'DUMMY_36'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 35:
            return 'DUMMY_35'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 34:
            return 'DUMMY_34'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 33:
            return 'DUMMY_33'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 32:
            return 'DUMMY_32'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 31:
            return 'DUMMY_31'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 30:
            return 'DUMMY_30'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 29:
            return 'DUMMY_29'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 28:
            return 'DUMMY_28'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 27:
            return 'DUMMY_27'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 26:
            return 'DUMMY_26'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 25:
            return 'DUMMY_25'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 24:
            return 'DUMMY_24'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 23:
            return 'DUMMY_23'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 22:
            return 'DUMMY_22'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 21:
            return 'DUMMY_21'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 20:
            return 'DUMMY_20'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 19:
            return 'DUMMY_19'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 18:
            return 'DUMMY_18'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 17:
            return 'DUMMY_17'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 16:
            return 'DUMMY_16'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 15:
            return 'DUMMY_15'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 14:
            return 'DUMMY_14'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 13:
            return 'DUMMY_13'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 12:
            return 'DUMMY_12'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 11:
            return 'DUMMY_11'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 10:
            return 'DUMMY_10'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 9:
            return 'DUMMY_9'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 8:
            return 'DUMMY_8'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 7:
            return 'DUMMY_7'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 6:
            return 'DUMMY_6'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 5:
            return 'DUMMY_5'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 4:
            return 'DUMMY_4'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 3:
            return 'DUMMY_3'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 2:
            return 'DUMMY_2'

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 1:
            return 'DUMMY_1'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 252:
            return 'number concentration of dust (sum of all modes)'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 251:
            return 'mass concentration of dust (sum of all modes)'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 74:
            return 'number concentration of dust (maximum mode)'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 73:
            return 'number concentration of dust (medium mode)'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 72:
            return 'number concentration of dust (minimum mode)'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 35:
            return 'mass concentration of dust (maximum mode)'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 34:
            return 'mass concentration of dust (medium mode)'

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 33:
            return 'mass concentration of dust (minimum mode)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 197:
            return 'Height of thermals above MSL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 200:
            return 'Atmospheric resistance'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 218:
            return 'production of TKE '

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 219:
            return 'buoyancy-production of TKE due to sub grid scale convection'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 221:
            return 'shear-production of TKE due to separated horizontal shear modes'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 220:
            return 'wake-production of TKE due to sub grid scale orography'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 14 and typeOfGeneratingProcess == 5:
            return 'Prob Starkes Tauwetter'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 13 and typeOfGeneratingProcess == 5:
            return 'Prob Tauwetter'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 12 and typeOfGeneratingProcess == 5:
            return 'Prob Nebel (ueberoertl. Sichtweite < 150 m)'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 'Prob Glatteis'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 10 and typeOfGeneratingProcess == 5:
            return 'Prob oertlich Glatteis'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 9 and typeOfGeneratingProcess == 5:
            return 'Prob Glaette'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 8 and typeOfGeneratingProcess == 5:
            return 'Prob Starke Schneeverwehung'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 7 and typeOfGeneratingProcess == 5:
            return 'Prob Schneeverwehung'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 6 and typeOfGeneratingProcess == 5:
            return 'Prob Extrem ergiebiger Dauerregen'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 5 and typeOfGeneratingProcess == 5:
            return 'Prob Ergiebiger Dauerregen'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 4 and typeOfGeneratingProcess == 5:
            return 'Prob Dauerregen'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 3 and typeOfGeneratingProcess == 5:
            return 'Prob Schweres Gewitter'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 2 and typeOfGeneratingProcess == 5:
            return 'Prob Starkes Gewitter'

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 1 and typeOfGeneratingProcess == 5:
            return 'Prob Gewitter'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 209 and typeOfStatisticalProcessing == 1:
            return 'Niederschlagsdargebot aus Modell SNOW'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 217:
            return 'Ellrod Index'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 216:
            return 'Eddy Dissipation Rate'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 198 and typeOfGeneratingProcess == 6:
            return 'covariance of soil moisture content'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197 and typeOfGeneratingProcess == 6:
            return 'variance of soil moisture content'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 195:
            return '3 hour pressure change'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 192:
            return 'Sea surface temperature interpolated in time in C'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 192:
            return 'tidal tendencies'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 202:
            return 'dry convection top index'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 22:
            return 'Clear Air Turbulence Index'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 21:
            return 'Frontogenesis function'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 20:
            return 'Divergenz Qs'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 19:
            return 'Divergenz Qn'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 18:
            return 'Q-Vektor parallel zu den Isothermen'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 17:
            return 'Divergenz'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 16:
            return 'Frontogenesefunktion'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 15:
            return 'Divergenz Qs geostrophisch'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 14:
            return 'Divergenz Qn geostrophisch'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 13:
            return 'Q-Vektor parallel zu d. Isothermen (geostrophisch)'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 12:
            return 'Q-Vektor senkrecht zu d. Isothermen (geostrophisch)'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 11:
            return 'Divergenz Q (geostrophisch)'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 10:
            return 'Q-Vektor Y-Komponente (geostrophisch)'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 9:
            return 'Q-Vektor X-Komponente (geostrophisch)'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 8:
            return 'Forcing rechte Seite Omegagleichung'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 7:
            return 'geostrophische Vorticity'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 23:
            return 'Potentielle Vorticity (auf Druckflaechen, nicht isentrop)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 199:
            return 'relative vorticity,V-component'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 198:
            return 'relative vorticity,U-component'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 192:
            return 'cloud top temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 192:
            return 'cloud type'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 209:
            return 'current weather (symbol number: 0..9)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208 and typeOfGeneratingProcess == 0:
            return 'Icing Scenario Code (1=general,2=convective,3=stratiform,4=freezing)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207 and typeOfGeneratingProcess == 0:
            return 'Icing Degree Code (1=light,2=moderate,3=severe)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208 and typeOfGeneratingProcess == 2:
            return 'Icing Scenario Code (1=general,2=convective,3=stratiform,4=freezing)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207 and typeOfGeneratingProcess == 2:
            return 'Icing Degree Code (1=light,2=moderate,3=severe)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206 and typeOfGeneratingProcess == 0:
            return 'Icing Signifikant Code (1=general,2=convective,3=stratiform,4=freezing) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205 and typeOfGeneratingProcess == 0:
            return 'Icing Vertical Code (1=continuous,2=discontinuous) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204 and typeOfGeneratingProcess == 0:
            return 'Icing Top (hft) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203 and typeOfGeneratingProcess == 0:
            return 'Icing Signifikant Top (hft) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202 and typeOfGeneratingProcess == 0:
            return 'Icing Signifikant Base (hft) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201 and typeOfGeneratingProcess == 0:
            return 'Icing Base (hft) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200 and typeOfGeneratingProcess == 0:
            return 'Icing Max Code (1=light,2=moderate,3=severe) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199 and typeOfGeneratingProcess == 0:
            return 'Icing Vertical Code (1=continuous,2=discontinuous) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198 and typeOfGeneratingProcess == 0:
            return 'Icing Top (hft) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197 and typeOfGeneratingProcess == 0:
            return 'Icing Max Top (hft) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196 and typeOfGeneratingProcess == 0:
            return 'Icing Max Base (hft) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195 and typeOfGeneratingProcess == 0:
            return 'Icing Base (hft) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206 and typeOfGeneratingProcess == 2:
            return 'Icing Signifikant Code (1=general,2=convective,3=stratiform,4=freezing) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205 and typeOfGeneratingProcess == 2:
            return 'Icing Vertical Code (1=continuous,2=discontinuous) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204 and typeOfGeneratingProcess == 2:
            return 'Icing Top (hft) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203 and typeOfGeneratingProcess == 2:
            return 'Icing Signifikant Top (hft) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202 and typeOfGeneratingProcess == 2:
            return 'Icing Signifikant Base (hft) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201 and typeOfGeneratingProcess == 2:
            return 'Icing Base (hft) - Icing Scenario Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200 and typeOfGeneratingProcess == 2:
            return 'Icing Max Code (1=light,2=moderate,3=severe) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199 and typeOfGeneratingProcess == 2:
            return 'Icing Vertical Code (1=continuous,2=discontinuous) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198 and typeOfGeneratingProcess == 2:
            return 'Icing Top (hft) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197 and typeOfGeneratingProcess == 2:
            return 'Icing Max Top (hft) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196 and typeOfGeneratingProcess == 2:
            return 'Icing Max Base (hft) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195 and typeOfGeneratingProcess == 2:
            return 'Icing Base (hft) - Icing Degree Composit'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Downward diffusive short wave radiation flux at surface ( mean over forecast time)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Downward direct short wave radiation flux at surface (mean over forecast time)'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 2:
            return 'value of isolation of clothes'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 3:
            return 'probability to perceive sultriness'

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 1:
            return 'perceived temperature'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 201:
            return 'Konvektionsart (0..4)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 194 and typeOfStatisticalProcessing == 2:
            return 'Time of maximum of UV Index, clouded'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 197:
            return 'UV Index, clouded sky; corrected for albedo, aerosol, altitude and clouds'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 196:
            return 'Basic UV Index, clear sky; MSL, fixed albedo, fixed aerosol'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 195:
            return 'UV Index, clear sky; corrected for albedo, aerosol and altitude'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 236 and typeOfStatisticalProcessing == 3 and typeOfGeneratingProcess == 5:
            return 'Probability of temperature <= -10 deg C during 6h'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 232 and typeOfStatisticalProcessing == 3 and typeOfGeneratingProcess == 5:
            return 'Probability of temperature < 0 deg C during 1h'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 213 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of strong snowdrift during 12h'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 212 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of snowdrift during 12h'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 199 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of severe thunderstorm during 1h'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 198 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of heavy thunderstorm during 1h'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 197 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of thunderstorm during 1h'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 191 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of black ice during 1h'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 139 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 1h maximum wind gust speed >= 39m/s'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 138 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 1h maximum wind gust speed >= 33m/s'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 137 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 1h maximum wind gust speed >= 29m/s'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 136 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 1h maximum wind gust speed >= 25m/s'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 134 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 1h maximum wind gust speed >= 18m/s'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 132 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 1h maximum wind gust speed >= 14m/s'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 77 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 12h accumulated snow >= 25cm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 75 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 12h accumulated snow >= 15cm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 74 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 12h accumulated snow >= 10cm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 72 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 12h accumulated snow >=0.5cm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 71 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 6h accumulated snow >= 10cm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 70 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 6h accumulated snow >= 5cm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 69 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 6h accumulated snow >=0.5cm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 32 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 12h total precipitation >= 70mm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 29 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 12h total precipitation >= 40mm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 26 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 12h total precipitation >= 25mm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 17 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 6h total precipitation >= 35mm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 14 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 6h total precipitation >= 20mm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 3 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 1h total precipitation >= 25mm'

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 'Probability of 1h total precipitation >= 10mm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Kinetic Energy'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Kinetic Energy'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199:
            return 'modified cloud cover for media'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198:
            return 'modified cloud depth for media'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 6:
            return 'Wind Y-Komponente auf isentropen Flaechen'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 5:
            return 'Wind X-Komponente auf isentropen Flaechen'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 25 and typeOfFirstFixedSurface == 107:
            return 'Isentrope potentielle Vorticity'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 4:
            return 'Q-Vektor senkrecht zu den Isothermen'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 3:
            return 'Winddivergenz'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 2:
            return 'Schichtdickenadvektion'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 1:
            return 'Geostrophic thickness advection'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 0:
            return 'geostrophische Vorticityadvektion'

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 24 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'Hoehe der Konvektionsuntergrenze ueber nn'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 194:
            return 'Kombination Niederschlag-Bewoelkung-Blauthermik (cl_typ.tab)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 197:
            return 'Absolute vorticity advection'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194:
            return 'v-momentum flux due to SSO-effects'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfStatisticalProcessing == 0:
            return 'v-momentum flux due to SSO-effects'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193:
            return 'u-momentum flux due to SSO-effects'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 'u-momentum flux due to SSO-effects (initialisation)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 194:
            return 'Delay of the GPS signal trough dry atmos.'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 193:
            return 'Delay of the GPS signal trough wet atmos.'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 192:
            return 'Delay of the GPS signal trough the (total) atm.'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193:
            return 'Coriolis parameter'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 'water vapor flux'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207:
            return 'tendency of specific humidity'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192:
            return 'ratio of monthly mean NDVI (normalized differential vegetation index) to annual maximum'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 0:
            return 'ratio of monthly mean NDVI (normalized differential vegetation index) to annual maximum'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193:
            return 'vertically integrated ozone content (climatological)'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192:
            return 'height of ozone maximum (climatological)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196:
            return 'soil type of grid (1...9, local soilType.table)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 199:
            return 'surface emissivity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195:
            return 'meridional wind tendency due to subgrid scale oro.'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194:
            return 'zonal wind tendency due to subgrid scale oro.'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 3 and typeOfGeneratingProcess == 7:
            return 'analysis error(standard deviation), v-comp. of wind'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 2 and typeOfGeneratingProcess == 7:
            return 'analysis error(standard deviation), u-comp. of wind'

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 5 and typeOfGeneratingProcess == 7:
            return 'analysis error(standard deviation), geopotential(gpm)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206:
            return 'moisture convergence for Kuo-type closure'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205 and typeOfFirstFixedSurface == 2:
            return 'Massflux at convective cloud base'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'residuum of soil moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'total forcing at soil surface'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'total transpiration from all soil layers'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'sum of contributions to evaporation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193:
            return 'Effective transmissivity of solar radiation'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 192:
            return 'solution of 2-d Helmholtz equations - needed for restart'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196:
            return 'Kinetic Energy'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 'Tendency of turbulent kinetic energy'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 192:
            return 'Convective Inhibition, mean layer'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 192:
            return 'Convective Available Potential Energy, mean layer'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 193:
            return 'Convective Inhibition, most unstable'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 193:
            return 'Convective Available Potential Energy, most unstable'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 'supercell detection index 2 (only rot. up drafts)'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 'supercell detection index 1 (rot. up+down drafts)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'Pressure perturbation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202:
            return 'tendency of specific cloud ice content due to grid scale precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 'Fresh snow factor (weighting function for albedo indicating freshness of snow)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201:
            return 'tendency of specific cloud liquid water content due to grid scale precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200:
            return 'Specific humitiy tendency due to grid scale precipitation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'Temperature tendency due to grid scale precipation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196:
            return 'Specific content of precipitation particles (needed for water loading)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199:
            return 'tendency of  specific cloud ice content due to convection'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198:
            return 'Tendency of specific cloud liquid water content due to conversion'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 4:
            return 'Height of snow fall limit above MSL'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'Height of top of dry convection above MSL'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193:
            return 'meridional wind tendency due to convection'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192:
            return 'zonal wind tendency due to convection'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197:
            return 'Specific humitiy tendency due to convection'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192:
            return 'Temperature tendency due to convection'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 'top index (vertical level) of main convective cloud (i)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 'base index (vertical level) of main convective cloud (i)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195:
            return 'specific cloud water content, convective cloud'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'Cloud top above msl, shallow convection'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'cloud base above msl, shallow convection'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194:
            return 'subgridscale cloud ice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193:
            return 'subgrid scale cloud water'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'vertical integral of divergence of total water content (s)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 'Stomatal Resistance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 106:
            return 'Latent heat flux from plants'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 'Latent heat flux from bare soil'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192:
            return 'Thermal radiation heating rate'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192:
            return 'Solar radiation heating rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26 and typeOfStatisticalProcessing == 2:
            return 'Maximum horizontal moisture convergence track (over given time interval and column)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 25:
            return 'Echotop-height: largest height where radar reflectivity above a threshold is present'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 25:
            return 'Echotop-pressure: smallest pressure where radar reflectivity above a threshold is present'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62200:
            return 'Precipitation reservoir (liquid water on the flowers, preventing them from flowering) of ragweed  (ambrosia) '

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 'Fraction of land occupied by ragweed  (ambrosia)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62200:
            return 'ragweed  (ambrosia) pollen concentration'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62300:
            return 'Precipitation reservoir (liquid water on the flowers, preventing them from flowering) of grasses (poaceae) '

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 'Fraction of land occupied by grasses (poaceae)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62300:
            return 'Grasses (poaceae) pollen concentration'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62100:
            return 'Precipitation reservoir (liquid water on the flowers, preventing them from flowering) of alder (alnus) '

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 'Fraction of land occupied by alder (alnus)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62100:
            return 'Alder (alnus) pollen concentration'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62101:
            return 'Precipitation reservoir (liquid water on the flowers, preventing them from flowering) of birch (betula) '

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 'Fraction of land occupied by birch (betula)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62101:
            return 'Birch (betula) pollen concentration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'Maximum 10m wind speed without  gust'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'v-component of wind (gust)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Relative Humidity, restricted to land'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Dew Point Temperature, restricted to land'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Temperature, restricted to land'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 'relative vorticity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Maximum reflectivity track (over given time interval and entire atmosphere)'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5:
            return 'Composite reflectivity - forecast (simulation)'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5 and typeOfGeneratingProcess == 8:
            return 'Composite reflectivity - observation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 81 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Maximum total-column integrated condensed  water (over given time interval)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 81 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 20 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 26315:
            return 'Maximum total-column integrated condensed water above -10 C isotherm (over given time interval)'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 15 and typeOfStatisticalProcessing == 2:
            return 'Maximum amplitude (positive or negative) of updraft helicity  (over given time interval)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 23:
            return 'Base for given threshold of air concentration of radionuclides'

        modeNumber = h.get_l('modeNumber')
        typeOfDistributionFunction = h.get_l('typeOfDistributionFunction')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 8:
            return 'Accumulated dust Emission for mode 3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 8:
            return 'Accumulated dust Emission for mode 1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 8:
            return 'Accumulated dust Emission for mode 2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 8:
            return 'Emission rate of dust for mode 1'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 8:
            return 'Emission rate of dust for mode 3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 8:
            return 'Emission rate of dust for mode 2'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 24:
            return 'Top for given threshold of air concentration of radionuclides'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 22 and constituentType == 62001:
            return 'Top for given threshold of mass density for mineral dust cloud'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 22 and constituentType == 62025:
            return 'Top for given threshold of mass density for volcanic ash cloud'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 21 and constituentType == 62001:
            return 'Base for given threshold of mass density for mineral dust cloud'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 21 and constituentType == 62025:
            return 'Base for given threshold of mass density for volcanic ash cloud'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 17 and typeOfFirstFixedSurface == 10:
            return 'Diagnostic total column of activity concentration of radionuclides'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 99:
            return 'Mass density of hail'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 39:
            return 'Mass density of cloud ice'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 38:
            return 'Mass density of cloud droplets'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 98:
            return 'Mass density of graupel'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 97:
            return 'Mass density of snow '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 96:
            return 'Mass density of rain '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 107:
            return 'Number density of hail'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 106:
            return 'Number density of graupel'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 105:
            return 'Number density of snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 103:
            return 'Specific number concentration of hail'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 102:
            return 'Specific number concentration of graupel'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 101:
            return 'Specific number concentration of snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 104:
            return 'Number density of rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 100:
            return 'Specific number concentration of rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 116:
            return 'Specific mass of liquid water coating on snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 113:
            return 'Specific mass of liquid water coating on graupel'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 110:
            return 'Specific mass of liquid water coating on hail'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Surface upward thermal radiation'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'Surface upward thermal radiation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 8:
            return 'TOA downward solar radiation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 'Horizontal moisture convergence'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 'Total precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 4:
            return 'Convective Snowfall Water Equivalent Difference'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 4:
            return 'Convective Rain Difference'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 4:
            return 'Large Scale Snowfall water Equivalent Difference'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 4:
            return 'Large Scale Rain Difference'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102:
            return 'Aerosol optical depth'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and constituentType == 62025:
            return 'Diagnostic maximum total mass concentration of volcanic ash in a layer'

        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 20000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10000 and constituentType == 62025:
            return 'Diagnostic maximum total mass concentration of volcanic ash in layer FL390-FL530'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 38500 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 20000 and constituentType == 62025:
            return 'Diagnostic maximum total mass concentration of volcanic ash in layer FL245-FL390'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 70000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 38500 and constituentType == 62025:
            return 'Diagnostic maximum total mass concentration of volcanic ash in layer FL100-FL245'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 24000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 9100 and constituentType == 62025:
            return 'Diagnostic maximum total mass concentration of volcanic ash in layer FL350-FL550'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 101325 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 70000 and constituentType == 62025:
            return 'Diagnostic maximum total mass concentration of volcanic ash in layer SFC-FL100'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 46500 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 24000 and constituentType == 62025:
            return 'Diagnostic maximum total mass concentration of volcanic ash in layer FL200-FL350'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 15:
            return 'Diagnostic vmaximum activity concentration of radionuclides in a layer'

        aerosolType = h.get_l('aerosolType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62008:
            return 'Diagnostic sea salt optical depth'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62001:
            return 'Diagnostic mineral dust optical depth'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62025:
            return 'Diagnostic volcanic ash optical depth'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 62 and constituentType == 62025:
            return 'Diagnostic height of model layer with maximal total mass concentration of volcanic ash'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and typeOfFirstFixedSurface == 10 and constituentType == 62025:
            return 'Diagnostic total column of mass concentration of volcanic ash'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 101325 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 46500 and constituentType == 62025:
            return 'Diagnostic maximum total mass concentration of volcanic ash in layer SFC-FL200'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 0 and constituentType == 62025:
            return 'Diagnostic total mass concentration of volcanic ash'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30102:
            return 'Prognostic specific activity concentration of Ruthenium 103'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30175:
            return 'Prognostic specific activity concentration of Barium 140'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30139:
            return 'Prognostic specific activity concentration of Iodine 131 organic bounded'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30138:
            return 'Prognostic specific activity concentration of Iodine 131 elementary gaseous'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30161:
            return 'Prognostic specific activity concentration of Xenon 133'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30079:
            return 'Prognostic specific activity concentration of Zirconium 95'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30129:
            return 'Prognostic specific activity concentration of Tellurium 132'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30141:
            return 'Prognostic specific activity concentration of Iodine 131 aerosol'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30172:
            return 'Prognostic specific activity concentration of Caesium 137'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration of sea salt particles (coarse mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration of sea salt particles (medium mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration of sea salt particles (fine mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of sea salt particles (coarse mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of sea salt particles (medium mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of sea salt particles (fine mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration  of mineral dust particles (coarsemode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration  of mineral dust particles (medium mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration  of mineral dust particles (fine mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of mineral dust particles (coarse mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of mineral dust particles (medium mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of mineral dust particles (fine mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration of volcanic ash particles (coarse mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration of volcanic ash particles (medium mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'Modal prognostic specific number concentration of volcanic ash particles (fine mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of volcanic ash particles (coarse mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of volcanic ash particles (medium mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 'Modal prognostic mass mixing ratio of volcanic ash particles (fine mode)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 6 and typeOfDistributionFunction == 1:
            return 'Prognostic mass mixing ratio of volcanic ash particles for bin number 6'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 5 and typeOfDistributionFunction == 1:
            return 'Prognostic mass mixing ratio of volcanic ash particles for bin number 5'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 4 and typeOfDistributionFunction == 1:
            return 'Prognostic mass mixing ratio of volcanic ash particles for bin number 4'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 1:
            return 'Prognostic mass mixing ratio of volcanic ash particles for bin number 3'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 1:
            return 'Prognostic mass mixing ratio of volcanic ash particles for bin number 2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 1:
            return 'Prognostic mass mixing ratio of volcanic ash particles for bin number 1'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 42:
            return 'v-component of geostrophic wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 41:
            return 'u-component of geostrophic wind'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 21:
            return 'Universal thermal climate index with direct incident short wave radiation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 27 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m wet bulb temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 27:
            return 'Wet bulb temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 3:
            return 'Temperature at cloud top'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m virtual potential temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m equivalentTemperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 'Dew point temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m potential temperature'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10 and typeOfFirstFixedSurface == 10:
            return 'Surface lifted index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 13:
            return 'Showalter index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 17:
            return 'Gradient Richardson number'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 94:
            return 'relative humidity over ice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Humidity mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2:
            return 'Humidity mixing ratio'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 5:
            return 'Height of lifting condensation level of mixed (mean) layer parcel'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Downward short wave radiation flux at surface (time average)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 44:
            return 'Geostrophic wind speed'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m dewpoint depression'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7:
            return 'Dewpoint depression'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 43:
            return 'Geostrophic wind direction'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 3000:
            return 'Cape of mixed (mean) layer parcel, ascent up to 3 km'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 16:
            return 'Bulk Richardson number'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m absolute humidity'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Downward long-wave radiation flux accum'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Downward long-wave radiation flux avg'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 'Downward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 31:
            return 'Number density of cloud ice particles'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 30:
            return 'Number density of cloud droplets'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 73 and typeOfStatisticalProcessing == 1:
            return 'Hail  precipitation rate, accumulation'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 14:
            return 'Reflectivity of hail'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 13:
            return 'Reflectivity of graupel'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 12:
            return 'Reflectivity of rain'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 11:
            return 'Reflectivity of snow'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 10:
            return 'Reflectivity of  cloud ice'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 9:
            return 'Reflectivity of cloud droplets'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 73:
            return 'Hail  precipitation rate '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 72:
            return 'Hail  '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 71:
            return 'Hail  mixing ratio'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 20:
            return 'Meansquare slope'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 23:
            return 'Maximum wave period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 24:
            return 'Maximum individual wave height'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 44:
            return 'Benjamin-Feir index'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 43:
            return 'Spectral kurtosis'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 45:
            return 'Goda peakedness parameter'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 33:
            return 'Directional width of total swell'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 30:
            return 'Inverse mean zero crossing period of total swell'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 27:
            return 'Inverse mean frequency of total swell'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 32:
            return 'Directional width of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 29:
            return 'Mean zero-crossing period of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 26:
            return 'Inverse mean frequency of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 19:
            return 'Normalized wave stress'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 16:
            return 'Coefficient of drag with waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 17:
            return 'Friction velocity'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14:
            return 'Water depth'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 35:
            return 'Land use class'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfStatisticalProcessing == 0:
            return 'Gravity wave dissipation '

        numberOfGridInReference = h.get_l('numberOfGridInReference')

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and numberOfGridInReference == 2 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 1:
            return 'Geometric height of the earths surface above mean sea level at vertex point (ICON) '

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'Momentum Flux, V-Component (m)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'Momentum Flux, U-Component (m)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfFirstFixedSurface == 1:
            return 'Upward diffusive short wave radiation flux at surface ( mean over forecast time)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 'Saturation of soil moisture'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 36:
            return 'Land use class fraction'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 'Vapor pressure'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 'Snow phase change heat flux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 'Wilting point'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 'Soil Temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 'Wind mixing energy'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'Convective inhibition'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 'Radiance (with respect to wave length)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 'Radiance (with respect to wave number)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 'Net short-wave radiation flux (surface)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 'Secondary wave direction'

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
            return 'V-component of current'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 'U-component of current'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 'Absolute divergence'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 'Sigma coordinate vertical velocity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 'Montgomery stream Function'

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

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 'Visibility'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 'Minimum temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 'Maximum temperature'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 'Standard deviation of height'

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 'Seconds prior to initial reference time (defined in Section 1)'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 'Deviation of sea level from mea'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 'Secondary wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 'Primary wave mean period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 'Primary wave direction'

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

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 'Solar zenith angle'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 'Number of pixels used'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 'Estimated v component of wind'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 'Estimated u component of wind'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 'Cloud top height quality indicator'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 'Instantaneous rain rate'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 'Estimated precipitation'

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

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 'Solar parameter in canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 'Canopy conductance'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 'Blackadar mixing length scale'

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

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 'Evapotranspiration'

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

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return 'Supercooled large droplet probability (see Note 4)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return 'Clear air turbulence (CAT)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return 'In-cloud turbulence '

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return 'Horizontal extent of cumulonimbus (CB)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return 'Icing'

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

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 'Turbulence'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 'Turbulence base'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 'Turbulence top'

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

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5 and typeOfStatisticalProcessing == 1:
            return 'Precipitation'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 'Layer-maximum base reflectivity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 'Vertically-integrated liquid'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 'Base radial velocity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 'Base spectrum width'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 'Aerosol type'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return 'Best (4-layer) lifted index '

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 'Surface lifted index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 'Energy helicity index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 'Sweat index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 'Total totals index'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 'K index'

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
            return 'Net long-wave radiation flux, clear sky '

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 'Upward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 'Downward long-wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 'Net long wave radiation flux (top of atmosphere)'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 'Net long wave radiation flux (surface)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 'Downward UV radiation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 'Net short-wave radiation flux, clear sky'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 'Downward short-wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 'Net short-wave radiation flux (top of atmosphere)'

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

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 14:
            return 'Minimum dew point depression'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 'Thickness'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 'V-component storm motion'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 'U-component storm motion'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 'Horizontal momentum flux'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 'v-component of wind (gust)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 'u-component of wind (gust)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 'Maximum wind speed'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 'Ice pellets precipitation rate '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 'Freezing rain precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 'Water equivalent of accumulated snow depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 'Large scale snowfall rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 'Convective snowfall rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 'Snow Fall water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 'Total snow precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 'Total water precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 48:
            return 'Convective water precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 47:
            return 'Large scale water precipitation (non-convective)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 'Rime factor'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 'Rain fraction of total cloud water'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 'Potential evaporation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 'Potential evaporation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return 'Percent frozen precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return 'Categorical snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return 'Categorical ice pellets'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return 'Categorical freezing rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return 'Categorical rain'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 'Ice water mixing ratio'

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

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 'Total column water'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 'Heat index'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 'Brightness temperature'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Sunshine duration'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 'Boundary layer dissipation'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 'Potential temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 'Vertical v-component shear'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 'Vertical u-component shear'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 'Virtual Temperature'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 1:
            return 'Water Runoff'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 'Water Runoff (s)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 80000:
            return 'Cloud Cover (800 hPa - Soil)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 80000 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 40000:
            return 'Cloud Cover (400 - 800 hPa)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 40000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 'Cloud Cover (0 - 400 hPa)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return 'Snow cover '

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 'Skin temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 'Velocity potential'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 'Stream function'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 12:
            return 'salinity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 114:
            return 'Water equivalent  of accumulated snoe depth in - multi level '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 114:
            return 'Snow density in  - multi level '

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 114:
            return 'Snow depth  - multi level '

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18 and typeOfFirstFixedSurface == 114:
            return 'Snow temperature  - multi level '

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'Net short wave radiation flux - accumulated _ model top'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 'Net long wave radiation flux  - accumulated _ model top'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Net long wave radiation flux - accumulated _  surface'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Net short wave radiation flux - accumulated _ surface'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Sensible Heat Net Flux - accumulated _ surface'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Latent Heat Net Flux - accumulated _ surface'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 'Sensible Heat Net Flux - instant - at surface'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'Latent Heat Net Flux - instant - at surface'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 29:
            return 'Number of cloud ice particles per unit mass of air'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 28:
            return 'Number of cloud droplets per unit mass of air'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 2:
            return 'vertex longitude'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 2:
            return 'vertex latitude'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 3:
            return 'edge midpoint longitude'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 3:
            return 'edge midpoint latitude'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 1:
            return 'center longitude'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 1:
            return 'center latitude'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return 'Albedo - diffusive solar (0.3 - 5.0 m-6)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18 and typeOfStatisticalProcessing == 0:
            return 'Albedo - diffusive solar - time average (0.3 - 5.0 m-6)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Specific Humidity (S)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 'Lapse rate'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 'Current Speed'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 'Current Direction'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 'virtual potential temperature'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 35:
            return 'tangential wind component'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 34:
            return 'normal wind component'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 26:
            return 'exner pressure'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 'Global radiation flux'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 'ICAO Standard Atmosphere reference height'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16 and typeOfStatisticalProcessing == 1:
            return 'Snow melt'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 33 and typeOfStatisticalProcessing == 1:
            return 'Sunshine duration'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 50 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 7:
            return 'Soil Moisture Content (7-50 cm)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 7 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'Soil Moisture Content (0-7 cm)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'Soil Temperature (layer)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25:
            return 'Logarithm of Pressure'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 'Relative Divergenz'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 'Geopotential height'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 'Soil moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 19:
            return 'Soil moisture'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 4:
            return 'Convective Precipitation (difference)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 'Altimeter Settings'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 'Density'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 'Potential vorticity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 'vertical vorticity'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 'cloud top height'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 3 and typeOfSecondFixedSurface == 165 and typeOfFirstFixedSurface == 162:
            return 'Sediment thickness of the upper layer of bottom sediments'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 4 and typeOfFirstFixedSurface == 165:
            return 'Temperature at the lower boundary of the upper layer of bottom sediment (penetrated by thermal wave)'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 10 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 166:
            return 'Shape factor with respect to the temperature profile in the thermocline'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 0 and typeOfSecondFixedSurface == 166 and typeOfFirstFixedSurface == 1:
            return 'Mixed-layer depth'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 162:
            return 'Bottom temperature (temperature at the water-bottom sediment interface)'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfSecondFixedSurface == 166 and typeOfFirstFixedSurface == 1:
            return 'Mixed-layer temperature'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'Mean temperature of the water column'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 4 and typeOfFirstFixedSurface == 164:
            return 'Temperature at the lower boundary of the thermally active layer of bottom sediment'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 3 and typeOfSecondFixedSurface == 164 and typeOfFirstFixedSurface == 162:
            return 'Depth of thermally active layer of bottom sediment'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 11 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'Attenuation coefficient of water with respect to solar radiation'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 33:
            return 'Wind fetch'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 0 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 'Lake depth'

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 2:
            return 'Water Fraction'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Upward diffusive short wave radiation flux at surface ( mean over forecast time)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 'Absolute Vorticity'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 'Water temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 'wind chill factor'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0 and typeOfStatisticalProcessing == 1:
            return 'Total ozone'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50 and typeOfStatisticalProcessing == 2:
            return 'UV Index, clear sky, maximum'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 'Net long wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 'Net short wave radiation flux (at the surface)'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8 and typeOfGeneratingProcess == 1:
            return 'Net long wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8 and typeOfGeneratingProcess == 1:
            return 'Net short wave radiation flux'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 4:
            return 'Total Precipitation Difference'

        satelliteSeries = h.get_l('satelliteSeries')
        satelliteNumber = h.get_l('satelliteNumber')
        instrumentType = h.get_l('instrumentType')
        scaledValueOfCentralWaveNumber = h.get_l('scaledValueOfCentralWaveNumber')

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 83333:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'Obser. Sat. Meteosat sec. generation brightness temperature'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1250000:
            return 'Obser. Sat. Meteosat sec. generation Albedo (scaled)'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1666666:
            return 'Obser. Sat. Meteosat sec. generation Albedo (scaled)'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 625000:
            return 'Obser. Sat. Meteosat sec. generation Albedo (scaled)'

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 2000000:
            return 'Obser. Sat. Meteosat sec. generation Albedo (scaled)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 198:
            return 'calibrated forecast, wind speed (gust)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 198:
            return 'calibrated forecast, large-scale snowfall'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 198:
            return 'calibrated forecast, total precipitation  (Accumulation)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, wind speed (gust)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, soil temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, large-scale snowfall'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, cloud cover high'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, cloud cover medium'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, cloud cover low'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, total cloud cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, total precipitation (Accumulation)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, v comp. of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, u comp. of wind'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, dew point temp.'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, minimum temp.'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, maximum temp.'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 'smoothed forecast, temperature'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'Synth. Sat. radiance clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'Synth. Sat. radiance cloudy'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'Synth. Sat. brightness temperature clear sky'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 'Synth. Sat. brightness temperature cloudy'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of vert.velocity (pressure)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Monthly Mean of RMS of difference FG-AN of vert.velocity (pressure)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Monthly Mean of RMS of difference FG-AN of temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of relative humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Monthly Mean of RMS of difference FG-AN of relative humidity'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of geopotential'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Monthly Mean of RMS of difference FG-AN of geopotential'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of v-component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Monthly Mean of RMS of difference FG-AN of v-component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of u-component of wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Monthly Mean of RMS of difference FG-AN of u-component of wind'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 'Monthly Mean of RMS of difference IA-AN of pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 'Monthly Mean of RMS of difference FG-AN of pressure reduced to MSL'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 'Icing Grade (1=LGT,2=MOD,3=SEV)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 'Ceiling'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 'Aequivalentpotentielle Temperatur'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 'KO index'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 107:
            return 'Druck einer isentropen Flaeche'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 25:
            return 'weather interpretation (WMO)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 2:
            return 'Hoehe der Konvektionsuntergrenze ueber Grund'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 'storm relative helicity'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 'Vertical speed shear'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51 and typeOfStatisticalProcessing == 2:
            return 'UV Index, clouded sky, maximum'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23:
            return 'Gravity wave dissipation (vertical integral)'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30175:
            return 'Ba140 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30175:
            return 'Ba140 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30175:
            return 'Air concentration of Barium 140'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30139:
            return 'I131o - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30139:
            return 'I131o - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30139:
            return 'Air concentration of Iodine 131 organic bounded'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30138:
            return 'I131g - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30138:
            return 'I131g - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30138:
            return 'Air concentration of Iodine 131 elementary gaseous'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30161:
            return 'Xe133 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30161:
            return 'Xe133 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30161:
            return 'Air concentration of Xenon 133'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30000:
            return 'TRACER - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30000:
            return 'TRACER - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30000:
            return 'TRACER - concentration'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30059:
            return 'Kr85 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30059:
            return 'Kr85 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30059:
            return 'Air concentration of Krypton 85'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30079:
            return 'Zr95 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30079:
            return 'Zr95 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30079:
            return 'Air concentration of Zirconium 95'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30129:
            return 'Te132 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30129:
            return 'Te132 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30129:
            return 'Air concentration of Tellurium 132'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30172:
            return 'Cs137 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30172:
            return 'Cs137 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30172:
            return 'Air concentration of Caesium 137'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30141:
            return 'I131 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30141:
            return 'I131 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30141:
            return 'Air concentration of Iodine 131 aerosol'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30067:
            return 'Sr90 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30067:
            return 'Sr90 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30067:
            return 'Air concentration of Strontium 90'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30102:
            return 'Ru103 - wet deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30102:
            return 'Ru103 - dry deposition'

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30102:
            return 'Air concentration of Ruthenium 103'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 'Ozone Mixing Ratio'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 'Friction velocity'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2:
            return 'geographical longitude'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1:
            return 'geographical latitude'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62008:
            return 'Sea salt aerosol (12M)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62008:
            return 'Sea salt aerosol'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62009:
            return 'Black carbon aerosol (12M)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62009:
            return 'Black carbon aerosol'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62010:
            return 'Organic aerosol (12M)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62010:
            return 'Organic aerosol'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62001:
            return 'Total soil dust aerosol (climatology,12M)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62001:
            return 'Total soil dust aerosol (climatology)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62006:
            return 'Total sulfate aerosol (12M)'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62006:
            return 'Total sulfate aerosol'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 2:
            return 'normalized differential vegetation index (NDVI)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 0:
            return 'normalized differential vegetation index'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 30:
            return 'deciduous forest'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 29:
            return 'evergreen forest'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 'Orographie + Land-Meer-Verteilung'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 3:
            return 'Min Leaf area index'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 2:
            return 'Max Leaf area index'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 3:
            return 'Plant covering degree in the quiescent phas'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 2:
            return 'Plant covering degree in the vegetation phase'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 32:
            return 'root depth of vegetation'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28:
            return 'Leaf area index'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 'Slope of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21:
            return 'Angle of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24:
            return 'Anisotropy of sub-gridscale orography'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 'Standard deviation of sub-grid scale orography'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 31:
            return 'Wave directional width'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 'Mean zero-crossing wave period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 25:
            return 'Inverse mean wave frequency'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 'Mean period of combined wind waves and swell'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 'Peak wave period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 35:
            return 'Peak period of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 36:
            return 'Peak period of total swell'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 'Direction of combined wind waves and swell'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'Convective Available Potential Energy'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Base reflectivity (cmax)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 'Base reflectivity'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 'Base reflectivity'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 'Sea Ice Temperature'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 'Minimal Stomatal Resistance'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18:
            return 'Snow temperature (top of snow)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 'Plant Canopy Surface Water'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'soil ice content (multilayers)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 'Column-integrated Soil Moisture (multilayers)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106:
            return 'Soil Temperature (multilayer model)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'maximum Wind 10m'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 'mixed layer depth'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 19:
            return 'Turbulent transfer coefficient for heat (and Moisture)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 'Turbulent transfer coefficient for impulse'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20:
            return 'Turbulent diffusion coefficient for heat (and moisture)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 31:
            return 'Turbulent diffusioncoefficient for momentum'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 'Turbulent Kinetic Energy'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 24:
            return 'Convective turbulent kinetic enery'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 'Snow density'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfStatisticalProcessing == 1:
            return 'Graupel (snow pellets) precipitation (Accumulation)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75:
            return 'Graupel (snow pellets) precipitation rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfStatisticalProcessing == 1:
            return 'snow amount, grid-scale plus convective'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfStatisticalProcessing == 1:
            return 'rain amount, grid-scale plus convective'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 1:
            return 'Convective rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 'Convective snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76:
            return 'Convective rain rate'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 1:
            return 'Large scale rain (Accumulation)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 'Large scale snowfall rate water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77:
            return 'Large scale rain rate'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 4:
            return 'Height of 0 degree Celsius isotherm above msl'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 'Height of Convective Cloud Top above msl'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 'Height of Convective Cloud Base above msl'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 78:
            return 'Total Column integrated water (all components incl. precipitation)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 74:
            return 'Total column integrated grauple'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 'Grauple'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 'Total column integrated snow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 'Total column integrated rain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 'Snow mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 'Rain mixing ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82:
            return 'Cloud Ice Mixing Ratio'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 'Cloud Mixing Ratio'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return 'Non-Convective Cloud Cover, grid scale'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return 'Cloud cover'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 'Photosynthetically active radiation'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Photosynthetically active radiation (m) (at the surface)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Momentum Flux, V-Component (m)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Momentum Flux, U-Component (m)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Sensible Heat Net Flux (m)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Latent Heat Net Flux (m)'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 8:
            return 'Net long wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8:
            return 'Net long wave radiation flux (m) (on the model top)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 8:
            return 'Net short wave radiation flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8:
            return 'Net short wave radiation flux (on the model top)'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 'Net long wave radiation flux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Net long wave radiation flux (m) (at the surface)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 'Net short wave radiation flux (at the surface)'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Net short wave radiation flux (at the surface)'

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

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 'Sea Ice Thickness'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'Sea Ice Cover ( 0= free, 1=cover)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'Water Runoff (s)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 10:
            return 'Water Runoff'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return 'Plant cover'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 100 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 10:
            return 'Column-integrated Soil Moisture (2) 10-100cm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 10 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 'Column-integrated Soil Moisture (1) 0 -10 cm'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 190 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 100:
            return 'Column-integrated Soil Moisture'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 'Soil Temperature'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 9:
            return 'Soil Temperature'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 41:
            return 'Soil Temperature (41 cm depth)'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 36:
            return 'Soil Temperature  ( 36 cm depth, vv=0h)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfStatisticalProcessing == 0:
            return 'Albedo (in short-wave, average)'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return 'Albedo (in short-wave)'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 'Surface Roughness length Surface Roughness'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 'Land Cover (1=land, 0=sea)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1:
            return 'Large-Scale snowfall - water equivalent (Accumulation)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 1:
            return 'Convective Snowfall water equivalent (s)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69:
            return 'Total Column-Integrated Cloud Water'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0:
            return 'Cloud Cover (0 - 400 hPa)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400:
            return 'Cloud Cover (400 - 800 hPa)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800:
            return 'Cloud Cover (800 hPa - Soil)'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return 'Convective Cloud Cover'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'Total Cloud Cover'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'Snow Depth'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60:
            return 'Snow depth water equivalent'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1:
            return 'Convective Precipitation (Accumulation)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1:
            return 'Large-Scale Precipitation (Accumulation)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1:
            return 'Total Precipitation (Accumulation)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70:
            return 'Total Column-Integrated Cloud Ice'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'Evaporation (s)'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 'Total column integrated water vapour'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 'Relative Humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Relative Humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 'Specific Humidity'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'Specific Humidity (2m)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 'Vertical Velocity (Geometric) (w)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 'Vertical Velocity (Pressure) ( omega=dp/dt )'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 'V-Component of Wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'V-Component of Wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 'U-Component of Wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'U-Component of Wind'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 'Wind speed (SP)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'Wind speed (SP_10M)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 'Wind Direction (DD)'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 'Wind Direction (DD_10M)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 'Wave spectra (3)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 'Wave spectra (2)'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 'Wave spectra (1)'

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Radar spectra (1)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Dew Point Temperature (AV)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Dew Point Temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'Min 2m Temperature (i)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 'Max 2m Temperature (i)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 'Temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 9:
            return 'Climat. temperature, 2m Temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Temperature (AV)'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return '2m Temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Temperature (G)'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 'Total Column Integrated Ozone'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101:
            return 'Geometric Height of the layer limits above sea level(NN)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 1:
            return 'Geometric Height of the earths surface above sea level'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 'Geopotential'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfSecondFixedSurface == 105 and typeOfFirstFixedSurface == 105:
            return 'Geopotential (full lev)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 'Geopotential (S)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 'Pressure Tendency (S)'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 'Pressure Reduced to MSL'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 'Pressure'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 'Pressure (S) (not reduced)'

    return wrapped
