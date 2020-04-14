import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 133:
            return 'upward_sea_water_velocity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 138:
            return 'sea_water_sigma_theta'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 129:
            return 'sea_water_potential_temperature'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 130:
            return 'sea_water_practical_salinity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 153:
            return 'surface_downward_eastward_stress'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 154:
            return 'surface_downward_northward_stress'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 147:
            return 'ocean_barotropic_streamfunction'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 163:
            return 'depth_of_isosurface_of_sea_water_potential_temperature'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 238:
            return 'temperature_in_surface_snow'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 185:
            return 'convective_cloud_area_fraction'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 182:
            return 'lwe_thickness_of_water_evaporation_amount'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 178:
            return 'toa_net_upward_shortwave_flux'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 174:
            return 'surface_albedo'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 164:
            return 'cloud_area_fraction'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 158:
            return 'tendency_of_surface_air_pressure'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 144:
            return 'lwe_thickness_of_snowfall_amount'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 'lwe_thickness_of_convective_precipitation_amount'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 142:
            return 'lwe_thickness_of_stratiform_precipitation_amount'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'lwe_thickness_of_surface_snow_amount'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 140:
            return 'lwe_thickness_of_soil_moisture_content'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 139:
            return 'surface_temperature'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 137:
            return 'lwe_thickness_of_atmosphere_mass_content_of_water_vapor'

        if discipline == 2 and parameterNumber == 1 and parameterCategory == 0:
            return 'surface_roughness_length'

        if discipline == 0 and parameterNumber == 1 and parameterCategory == 1:
            return 'relative_humidity'

        if discipline == 0 and parameterNumber == 13 and parameterCategory == 2:
            return 'divergence_of_wind'

        if discipline == 0 and parameterNumber == 20 and parameterCategory == 2:
            return 'kinetic_energy_dissipation_in_atmosphere_boundary_layer'

        unitsFactor = h.get_l('unitsFactor')

        if discipline == 0 and parameterNumber == 10 and parameterCategory == 1 and unitsFactor == 1000:
            return 'lwe_thickness_of_convective_precipitation_amount'

        if discipline == 0 and parameterNumber == 11 and parameterCategory == 1 and unitsFactor == 1000:
            return 'lwe_thickness_of_surface_snow_amount'

        if discipline == 0 and parameterNumber == 12 and parameterCategory == 2:
            return 'atmosphere_relative_vorticity'

        if discipline == 0 and parameterNumber == 4 and parameterCategory == 3:
            return 'geopotential'

    return wrapped
