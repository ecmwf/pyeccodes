import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        parameter = h.get_l('parameter')

        if parameter == 99999:
            return 'default'

        if parameter == 228171:
            return 'wilt'

        if parameter == 132:
            return 'v'

        if parameter == 131:
            return 'u'

        if parameter == 228228:
            return 'tp'

        if parameter == 179:
            return 'ttr'

        if parameter == 131063:
            return 'tpg20'

        if parameter == 131062:
            return 'tpg10'

        if parameter == 176:
            return 'ssr'

        if parameter == 228164:
            return 'tcc'

        if parameter == 130:
            return 't'

        if parameter == 134:
            return 'sp'

        if parameter == 146:
            return 'sshf'

        if parameter == 228139:
            return 'st'

        if parameter == 147:
            return 'slhf'

        if parameter == 136:
            return 'tcw'

        if parameter == 167:
            return '2t'

        if parameter == 171034:
            return 'ssta'

        if parameter == 133:
            return 'q'

        if parameter == 122:
            return 'mn2t6'

        if parameter == 189:
            return 'sund'

        if parameter == 177:
            return 'str'

        if parameter == 228039:
            return 'sm'

        if parameter == 235:
            return 'skt'

        if parameter == 228144:
            return 'sf'

        if parameter == 3:
            return 'pt'

        if parameter == 60:
            return 'pv'

        if parameter == 168:
            return '2d'

        if parameter == 121:
            return 'mx2t6'

        if parameter == 228141:
            return 'sd'

        if parameter == 228002:
            return 'orog'

        if parameter == 151:
            return 'msl'

        if parameter == 172:
            return 'lsm'

        if parameter == 156:
            return 'gh'

        if parameter == 59:
            return 'cape'

        if parameter == 228170:
            return 'cap'

        if parameter == 228001:
            return 'ci'

        if parameter == 49:
            return '10u'

        if parameter == 165:
            return '10u'

        if parameter == 166:
            return '10v'

        if parameter == 131070:
            return '10fgg15'

        if parameter == 131071:
            return '10fgg25'

    return wrapped
