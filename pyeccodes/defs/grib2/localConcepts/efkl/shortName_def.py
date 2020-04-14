import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 225:
            return 'pollen_corr'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 224:
            return 'poll_tot_m2'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 223:
            return 'poll_left'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 222:
            return 'heatsum'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 221:
            return 'alrg_rdy2fly'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 220:
            return 'poll_rdy2fly'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 210:
            return 'radconc'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 204:
            return 'ciradconc'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 203:
            return 'cimolconc'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202:
            return 'cinumconc'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201:
            return 'cimassconc'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199:
            return 'wdradf'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198:
            return 'wdmolf'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197:
            return 'wdnumf'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194:
            return 'ddradf'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193:
            return 'ddmolf'

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192:
            return 'ddnumf'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 197:
            return 'scav_coef'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 196:
            return 'humid_scale'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 'turb_temp'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194:
            return 'cnv_vel_scale'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 'Kz_1m'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 'MO_len_inv'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'nwp_blh'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 'nwpshf'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'nwplhf'

    return wrapped
