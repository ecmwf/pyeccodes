import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        indicatorOfParameter = h.get_l('indicatorOfParameter')
        table2Version = h.get_l('table2Version')

        if indicatorOfParameter == 72 and table2Version == 1:
            return 'convective_cloud_area_fraction'

        if indicatorOfParameter == 57 and table2Version == 1:
            return 'lwe_thickness_of_water_evaporation_amount'

        if indicatorOfParameter == 84 and table2Version == 1:
            return 'surface_albedo'

        if indicatorOfParameter == 83 and table2Version == 1:
            return 'surface_roughness_length'

        if indicatorOfParameter == 81 and table2Version == 1:
            return 'land_binary_mask'

        if indicatorOfParameter == 52 and table2Version == 1:
            return 'relative_humidity'

        if indicatorOfParameter == 7 and table2Version == 1:
            return 'geopotential_height'

        if indicatorOfParameter == 44 and table2Version == 1:
            return 'divergence_of_wind'

        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if indicatorOfParameter == 2 and table2Version == 1 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'air_pressure_at_mean_sea_level'

        if indicatorOfParameter == 121 and table2Version == 1:
            return 'surface_upward_latent_heat_flux'

        if indicatorOfParameter == 122 and table2Version == 1:
            return 'surface_upward_sensible_heat_flux'

        if indicatorOfParameter == 123 and table2Version == 1:
            return 'kinetic_energy_dissipation_in_atmosphere_boundary_layer'

        if indicatorOfParameter == 43 and table2Version == 1:
            return 'atmosphere_relative_vorticity'

        if indicatorOfParameter == 40 and table2Version == 1:
            return 'lagrangian_tendency_of_air_pressure'

        if indicatorOfParameter == 1 and table2Version == 1 and indicatorOfTypeOfLevel == 1:
            return 'surface_air_pressure'

        if indicatorOfParameter == 51 and table2Version == 1:
            return 'specific_humidity'

        if indicatorOfParameter == 34 and table2Version == 1:
            return 'northward_wind'

        if indicatorOfParameter == 33 and table2Version == 1:
            return 'eastward_wind'

        if indicatorOfParameter == 11 and table2Version == 1:
            return 'air_temperature'

        if indicatorOfParameter == 6 and table2Version == 1:
            return 'geopotential'

        if indicatorOfParameter == 72 and table2Version == 2:
            return 'convective_cloud_area_fraction'

        if indicatorOfParameter == 57 and table2Version == 2:
            return 'lwe_thickness_of_water_evaporation_amount'

        if indicatorOfParameter == 84 and table2Version == 2:
            return 'surface_albedo'

        if indicatorOfParameter == 83 and table2Version == 2:
            return 'surface_roughness_length'

        if indicatorOfParameter == 81 and table2Version == 2:
            return 'land_binary_mask'

        if indicatorOfParameter == 52 and table2Version == 2:
            return 'relative_humidity'

        if indicatorOfParameter == 7 and table2Version == 2:
            return 'geopotential_height'

        if indicatorOfParameter == 44 and table2Version == 2:
            return 'divergence_of_wind'

        if indicatorOfParameter == 2 and table2Version == 2 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'air_pressure_at_mean_sea_level'

        if indicatorOfParameter == 121 and table2Version == 2:
            return 'surface_upward_latent_heat_flux'

        if indicatorOfParameter == 122 and table2Version == 2:
            return 'surface_upward_sensible_heat_flux'

        if indicatorOfParameter == 123 and table2Version == 2:
            return 'kinetic_energy_dissipation_in_atmosphere_boundary_layer'

        if indicatorOfParameter == 43 and table2Version == 2:
            return 'atmosphere_relative_vorticity'

        if indicatorOfParameter == 40 and table2Version == 2:
            return 'lagrangian_tendency_of_air_pressure'

        if indicatorOfParameter == 1 and table2Version == 2 and indicatorOfTypeOfLevel == 1:
            return 'surface_air_pressure'

        if indicatorOfParameter == 51 and table2Version == 2:
            return 'specific_humidity'

        if indicatorOfParameter == 34 and table2Version == 2:
            return 'northward_wind'

        if indicatorOfParameter == 33 and table2Version == 2:
            return 'eastward_wind'

        if indicatorOfParameter == 11 and table2Version == 2:
            return 'air_temperature'

        if indicatorOfParameter == 6 and table2Version == 2:
            return 'geopotential'

        if indicatorOfParameter == 72 and table2Version == 3:
            return 'convective_cloud_area_fraction'

        if indicatorOfParameter == 57 and table2Version == 3:
            return 'lwe_thickness_of_water_evaporation_amount'

        if indicatorOfParameter == 84 and table2Version == 3:
            return 'surface_albedo'

        if indicatorOfParameter == 83 and table2Version == 3:
            return 'surface_roughness_length'

        if indicatorOfParameter == 81 and table2Version == 3:
            return 'land_binary_mask'

        if indicatorOfParameter == 52 and table2Version == 3:
            return 'relative_humidity'

        if indicatorOfParameter == 7 and table2Version == 3:
            return 'geopotential_height'

        if indicatorOfParameter == 44 and table2Version == 3:
            return 'divergence_of_wind'

        if indicatorOfParameter == 2 and table2Version == 3 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'air_pressure_at_mean_sea_level'

        if indicatorOfParameter == 121 and table2Version == 3:
            return 'surface_upward_latent_heat_flux'

        if indicatorOfParameter == 122 and table2Version == 3:
            return 'surface_upward_sensible_heat_flux'

        if indicatorOfParameter == 123 and table2Version == 3:
            return 'kinetic_energy_dissipation_in_atmosphere_boundary_layer'

        if indicatorOfParameter == 43 and table2Version == 3:
            return 'atmosphere_relative_vorticity'

        if indicatorOfParameter == 40 and table2Version == 3:
            return 'lagrangian_tendency_of_air_pressure'

        if indicatorOfParameter == 1 and table2Version == 3 and indicatorOfTypeOfLevel == 1:
            return 'surface_air_pressure'

        if indicatorOfParameter == 51 and table2Version == 3:
            return 'specific_humidity'

        if indicatorOfParameter == 34 and table2Version == 3:
            return 'northward_wind'

        if indicatorOfParameter == 33 and table2Version == 3:
            return 'eastward_wind'

        if indicatorOfParameter == 11 and table2Version == 3:
            return 'air_temperature'

        if indicatorOfParameter == 6 and table2Version == 3:
            return 'geopotential'

    return wrapped
