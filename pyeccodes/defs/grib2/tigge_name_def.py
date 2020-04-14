import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        parameter = h.get_l('parameter')

        if parameter == 99999:
            return 'default'

        if parameter == 228171:
            return 'wilting_point'

        if parameter == 132:
            return 'v_velocity'

        if parameter == 131:
            return 'u_velocity'

        if parameter == 131063:
            return 'total_precipitation_of_at_least_20_mm'

        if parameter == 131062:
            return 'total_precipitation_of_at_least_10_mm'

        if parameter == 228228:
            return 'total_precipitation'

        if parameter == 136:
            return 'total_column_water'

        if parameter == 228164:
            return 'total_cloud_cover'

        if parameter == 146:
            return 'time_integrated_surface_sensible_heat_flux'

        if parameter == 177:
            return 'time_integrated_surface_net_thermal_radiation'

        if parameter == 176:
            return 'time_integrated_surface_net_solar_radiation'

        if parameter == 147:
            return 'time_integrated_surface_latent_heat_flux'

        if parameter == 179:
            return 'time_integrated_outgoing_long_wave_radiation'

        if parameter == 130:
            return 'temperature'

        if parameter == 134:
            return 'surface_pressure'

        if parameter == 167:
            return 'surface_air_temperature'

        if parameter == 122:
            return 'surface_air_minimum_temperature'

        if parameter == 121:
            return 'surface_air_maximum_temperature'

        if parameter == 168:
            return 'surface_air_dew_point_temperature'

        if parameter == 189:
            return 'sunshine_duration'

        if parameter == 133:
            return 'specific_humidity'

        if parameter == 228139:
            return 'soil_temperature'

        if parameter == 228039:
            return 'soil_moisture'

        if parameter == 228144:
            return 'snow_fall_water_equivalent'

        if parameter == 228141:
            return 'snow_depth_water_equivalent'

        if parameter == 235:
            return 'skin_temperature'

        if parameter == 171034:
            return 'sea_surface_temperature_anomaly'

        if parameter == 60:
            return 'potential_vorticity'

        if parameter == 3:
            return 'potential_temperature'

        if parameter == 228002:
            return 'orography'

        if parameter == 151:
            return 'mean_sea_level_pressure'

        if parameter == 49:
            return 'maximum_wind_gust'

        if parameter == 172:
            return 'land_sea_mask'

        if parameter == 156:
            return 'geopotential_height'

        if parameter == 228170:
            return 'field_capacity'

        if parameter == 228001:
            return 'convective_inhibition'

        if parameter == 59:
            return 'convective_available_potential_energy'

        if parameter == 131071:
            return '10_metre_wind_gust_of_at_least_25_m/s'

        if parameter == 131070:
            return '10_metre_wind_gust_of_at_least_15_m/s'

        if parameter == 166:
            return '10_meter_v_velocity'

        if parameter == 165:
            return '10_meter_u_velocity'

    return wrapped
