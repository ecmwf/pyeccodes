import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 225:
            return 'Climate correction for total pollen'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 224:
            return 'Pollen total per m2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 223:
            return 'Pollen left fraction'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 222:
            return 'Heatsum for pollen'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 221:
            return 'Ready to fly allergen'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 220:
            return 'Ready to fly pollen'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 210:
            return 'Radioactive concentration'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 204:
            return 'Column integrated radioactive concentration'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 203:
            return 'Column integrated molar concentration'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202:
            return 'Column integrated number concentration'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201:
            return 'Column integrated mass concentration'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199:
            return 'Wet deposition Radioactive Flux'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198:
            return 'Wet deposition Molar Flux'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197:
            return 'Wet deposition Number Flux'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194:
            return 'Dry deposition radioactive flux'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193:
            return 'Dry deposition molar flux'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192:
            return 'Dry deposition number flux'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 197:
            return 'Scavenging coefficient'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 196:
            return 'Humidity scale h_star'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 'Temperature scale T_star'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194:
            return 'Convective velocity scale'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 'mixing velocity scale "Kz_1m" at surface'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 'MO_length_inv'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'NWP Boundary layer height'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 'NWP sensible heat net flux'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'NWP latent heat net flux'

    return wrapped
