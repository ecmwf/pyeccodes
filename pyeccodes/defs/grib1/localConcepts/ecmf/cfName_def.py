import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 151 and indicatorOfParameter == 133:
            return 'upward_sea_water_velocity'

        if table2Version == 151 and indicatorOfParameter == 131:
            return 'eastward_sea_water_velocity'

        if table2Version == 151 and indicatorOfParameter == 132:
            return 'northward_sea_water_velocity'

        if table2Version == 151 and indicatorOfParameter == 138:
            return 'sea_water_sigma_theta'

        if table2Version == 151 and indicatorOfParameter == 129:
            return 'sea_water_potential_temperature'

        if table2Version == 151 and indicatorOfParameter == 130:
            return 'sea_water_practical_salinity'

        if table2Version == 151 and indicatorOfParameter == 145:
            return 'sea_surface_height_above_geoid'

        if table2Version == 151 and indicatorOfParameter == 153:
            return 'surface_downward_eastward_stress'

        if table2Version == 151 and indicatorOfParameter == 154:
            return 'surface_downward_northward_stress'

        if table2Version == 151 and indicatorOfParameter == 147:
            return 'ocean_barotropic_streamfunction'

        if table2Version == 151 and indicatorOfParameter == 163:
            return 'depth_of_isosurface_of_sea_water_potential_temperature'

        if table2Version == 174 and indicatorOfParameter == 97:
            return 'surface_snow_thickness'

        if table2Version == 128 and indicatorOfParameter == 31:
            return 'sea_ice_area_fraction'

        if table2Version == 174 and indicatorOfParameter == 98:
            return 'sea_ice_thickness'

        if indicatorOfParameter == 238 and table2Version == 128:
            return 'temperature_in_surface_snow'

        if indicatorOfParameter == 211 and table2Version == 128:
            return 'surface_net_downward_longwave_flux_assuming_clear_sky'

        if indicatorOfParameter == 210 and table2Version == 128:
            return 'surface_net_downward_shortwave_flux_assuming_clear_sky'

        if indicatorOfParameter == 185 and table2Version == 128:
            return 'convective_cloud_area_fraction'

        if indicatorOfParameter == 182 and table2Version == 128:
            return 'lwe_thickness_of_water_evaporation_amount'

        if indicatorOfParameter == 181 and table2Version == 128:
            return 'surface_downward_northward_stress'

        if indicatorOfParameter == 180 and table2Version == 128:
            return 'surface_downward_eastward_stress'

        if indicatorOfParameter == 179 and table2Version == 128:
            return 'toa_outgoing_longwave_flux'

        if indicatorOfParameter == 178 and table2Version == 128:
            return 'toa_net_upward_shortwave_flux'

        if indicatorOfParameter == 177 and table2Version == 128:
            return 'surface_net_upward_longwave_flux'

        if indicatorOfParameter == 176 and table2Version == 128:
            return 'surface_net_downward_shortwave_flux'

        if indicatorOfParameter == 174 and table2Version == 128:
            return 'surface_albedo'

        if indicatorOfParameter == 173 and table2Version == 128:
            return 'surface_roughness_length'

        if indicatorOfParameter == 172 and table2Version == 128:
            return 'land_binary_mask'

        if indicatorOfParameter == 169 and table2Version == 128:
            return 'surface_downwelling_shortwave_flux_in_air'

        if indicatorOfParameter == 164 and table2Version == 128:
            return 'cloud_area_fraction'

        if indicatorOfParameter == 158 and table2Version == 128:
            return 'tendency_of_surface_air_pressure'

        if indicatorOfParameter == 157 and table2Version == 128:
            return 'relative_humidity'

        if indicatorOfParameter == 156 and table2Version == 128:
            return 'geopotential_height'

        if indicatorOfParameter == 155 and table2Version == 128:
            return 'divergence_of_wind'

        if indicatorOfParameter == 151 and table2Version == 128:
            return 'air_pressure_at_mean_sea_level'

        if indicatorOfParameter == 147 and table2Version == 128:
            return 'surface_upward_latent_heat_flux'

        if indicatorOfParameter == 146 and table2Version == 128:
            return 'surface_upward_sensible_heat_flux'

        if indicatorOfParameter == 145 and table2Version == 128:
            return 'kinetic_energy_dissipation_in_atmosphere_boundary_layer'

        if indicatorOfParameter == 144 and table2Version == 128:
            return 'lwe_thickness_of_snowfall_amount'

        if indicatorOfParameter == 143 and table2Version == 128:
            return 'lwe_thickness_of_convective_precipitation_amount'

        if indicatorOfParameter == 142 and table2Version == 128:
            return 'lwe_thickness_of_stratiform_precipitation_amount'

        if indicatorOfParameter == 141 and table2Version == 128:
            return 'lwe_thickness_of_surface_snow_amount'

        if indicatorOfParameter == 140 and table2Version == 128:
            return 'lwe_thickness_of_soil_moisture_content'

        if indicatorOfParameter == 139 and table2Version == 128:
            return 'surface_temperature'

        if indicatorOfParameter == 138 and table2Version == 128:
            return 'atmosphere_relative_vorticity'

        if indicatorOfParameter == 137 and table2Version == 128:
            return 'lwe_thickness_of_atmosphere_mass_content_of_water_vapor'

        if indicatorOfParameter == 135 and table2Version == 128:
            return 'lagrangian_tendency_of_air_pressure'

        if indicatorOfParameter == 134 and table2Version == 128:
            return 'surface_air_pressure'

        if indicatorOfParameter == 133 and table2Version == 128:
            return 'specific_humidity'

        if indicatorOfParameter == 132 and table2Version == 128:
            return 'northward_wind'

        if indicatorOfParameter == 131 and table2Version == 128:
            return 'eastward_wind'

        if indicatorOfParameter == 130 and table2Version == 128:
            return 'air_temperature'

        if indicatorOfParameter == 129 and table2Version == 128:
            return 'geopotential'

    return wrapped
