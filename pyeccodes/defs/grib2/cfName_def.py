import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'sea_surface_height_above_geoid'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'sea_ice_thickness'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3 and typeOfFirstFixedSurface == 160:
            return 'northward_sea_water_velocity'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 160:
            return 'eastward_sea_water_velocity'

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'surface_net_downward_longwave_flux_assuming_clear_sky'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 'surface_net_downward_shortwave_flux_assuming_clear_sky'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 3 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 'sea_surface_salinity'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and typeOfSecondFixedSurface == 255 and scaleFactorOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 169 and scaledValueOfFirstFixedSurface == 1:
            return 'ocean_mixed_layer_thickness_defined_by_sigma_theta'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 29315:
            return 'depth_of_isosurface_of_sea_water_potential_temperature'

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 'sea_ice_area_fraction'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 37:
            return 'surface_downward_northward_stress'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 38:
            return 'surface_downward_eastward_stress'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'surface_net_downward_shortwave_flux'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 'surface_downwelling_shortwave_flux_in_air'

        if discipline == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 8 and parameterCategory == 5 and typeOfStatisticalProcessing == 1:
            return 'toa_outgoing_longwave_flux'

        if discipline == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 1 and parameterCategory == 5 and typeOfStatisticalProcessing == 1:
            return 'surface_net_upward_longwave_flux'

        if discipline == 0 and parameterNumber == 9 and typeOfFirstFixedSurface == 1 and parameterCategory == 4 and typeOfStatisticalProcessing == 1:
            return 'surface_net_upward_longwave_flux'

        if discipline == 2 and parameterNumber == 1 and parameterCategory == 0:
            return 'surface_roughness_length'

        if discipline == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 1 and parameterCategory == 0:
            return 'land_binary_mask'

        if discipline == 0 and parameterNumber == 1 and parameterCategory == 1:
            return 'relative_humidity'

        if discipline == 0 and parameterNumber == 5 and parameterCategory == 3:
            return 'geopotential_height'

        if discipline == 0 and parameterNumber == 13 and parameterCategory == 2:
            return 'divergence_of_wind'

        if discipline == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 101 and parameterCategory == 3:
            return 'air_pressure_at_mean_sea_level'

        if discipline == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and parameterCategory == 0 and typeOfStatisticalProcessing == 1:
            return 'surface_upward_latent_heat_flux'

        if discipline == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and parameterCategory == 0 and typeOfStatisticalProcessing == 1:
            return 'surface_upward_sensible_heat_flux'

        if discipline == 0 and parameterNumber == 20 and parameterCategory == 2:
            return 'kinetic_energy_dissipation_in_atmosphere_boundary_layer'

        if discipline == 0 and parameterNumber == 12 and parameterCategory == 2:
            return 'atmosphere_relative_vorticity'

        if discipline == 0 and parameterNumber == 8 and parameterCategory == 2:
            return 'lagrangian_tendency_of_air_pressure'

        if discipline == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1 and parameterCategory == 3:
            return 'surface_air_pressure'

        if discipline == 0 and parameterNumber == 0 and parameterCategory == 1:
            return 'specific_humidity'

        if discipline == 0 and parameterNumber == 3 and parameterCategory == 2:
            return 'northward_wind'

        if discipline == 0 and parameterNumber == 2 and parameterCategory == 2:
            return 'eastward_wind'

        if discipline == 0 and parameterNumber == 0 and parameterCategory == 0:
            return 'air_temperature'

        if discipline == 0 and parameterNumber == 4 and parameterCategory == 3:
            return 'geopotential'

    return wrapped
