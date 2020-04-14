import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 254:
            return 'ascat_sm_cdfb'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 253:
            return 'ascat_sm_cdfa'

        localTablesVersion = h.get_l('localTablesVersion')

        if localTablesVersion == 228 and discipline == 0 and parameterCategory == 254 and parameterNumber == 136:
            return 'utnowd'

        if localTablesVersion == 228 and discipline == 0 and parameterCategory == 254 and parameterNumber == 134:
            return 'vtnowd'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 101:
            return 'maxfrpfirediff'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 117:
            return 'c2h6sfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 116:
            return 'nh3fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 115:
            return 'c3h6ofire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 114:
            return 'c2h4ofire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 113:
            return 'ch2ofire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 112:
            return 'hialkanesfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 111:
            return 'hialkenesfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 110:
            return 'toluenefire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 109:
            return 'terpenesfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 108:
            return 'c5h8fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 107:
            return 'c3h6fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 106:
            return 'c2h4fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 105:
            return 'c3h8fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 104:
            return 'c2h5ohfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 103:
            return 'ch3ohfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 102:
            return 'so2fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 101:
            return 'maxfrpfire'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 216:
            return 'vst'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 215:
            return 'ust'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 228:
            return 'tps'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 167:
            return '2ts'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 151:
            return 'msls'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 139:
            return 'sts'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 132:
            return 'v10n'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 131:
            return 'u10n'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 19:
            return 'tplt'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 18:
            return 'tplb'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 17:
            return 'dctb'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 16:
            return 'dndza'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 15:
            return 'dndzn'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 14:
            return 'licd'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 13:
            return 'lict'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 12:
            return 'lshf'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 11:
            return 'ltlt'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 10:
            return 'lblt'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 9:
            return 'lmld'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 8:
            return 'lmlt'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 7:
            return 'dl'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 6:
            return 'meantcc'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 5:
            return 'mean10ws'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 4:
            return 'mean2t'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 3:
            return 'zust'

        if discipline == 192 and parameterCategory == 220 and parameterNumber == 228:
            return 'tpoc'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 216:
            return 'aod1240diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 215:
            return 'aod865diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 214:
            return 'aod670diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 213:
            return 'aod469diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 212:
            return 'suaod550diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 211:
            return 'bcaod550diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 210:
            return 'omaod550diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 209:
            return 'duaod550diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 208:
            return 'ssaod550diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 207:
            return 'aod550diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 206:
            return 'gtco3diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 203:
            return 'go3diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 185:
            return 'sf6apfdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 184:
            return 'tcsf6diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 183:
            return 'tcradiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 182:
            return 'sf6diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 181:
            return 'radiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 166:
            return 'sfgr10diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 165:
            return 'sfgr9diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 164:
            return 'sfgr8diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 163:
            return 'sfgr7diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 162:
            return 'sfgr6diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 161:
            return 'sfgr5diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 160:
            return 'sfgr4diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 159:
            return 'sfgr3diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 158:
            return 'sfgr2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 157:
            return 'sfgr1diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 156:
            return 'sfgo3diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 155:
            return 'sfhchodiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 154:
            return 'sfco2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 153:
            return 'sfso2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 152:
            return 'sfno2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 151:
            return 'sfnoxdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 150:
            return 'tcgrg10diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 149:
            return 'grg10diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 148:
            return 'tcgrg9diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 147:
            return 'grg9diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 146:
            return 'tcgrg8diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 145:
            return 'grg8diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 144:
            return 'tcgrg7diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 143:
            return 'grg7diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 142:
            return 'tcgrg6diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 141:
            return 'grg6diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 140:
            return 'tcgrg5diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 139:
            return 'grg5diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 138:
            return 'tcgrg4diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 137:
            return 'grg4diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 136:
            return 'tcgrg3diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 135:
            return 'grg3diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 134:
            return 'tcgrg2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 133:
            return 'grg2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 132:
            return 'tcgrg1diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 131:
            return 'grg1diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 130:
            return 'tcnoxdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 129:
            return 'noxdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 128:
            return 'tchchodiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 127:
            return 'tccodiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 126:
            return 'tcso2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 125:
            return 'tcno2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 124:
            return 'hchodiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 123:
            return 'codiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 122:
            return 'so2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 121:
            return 'no2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 100:
            return 'crfirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 99:
            return 'frpfirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 98:
            return 'oafirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 97:
            return 'offirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 96:
            return 'flfirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 95:
            return 'ccfirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 94:
            return 'vegfirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 93:
            return 'c4ffirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 92:
            return 'cfirediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 71:
            return 'kch4diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 70:
            return 'ch4fdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 69:
            return 'co2apfdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 68:
            return 'co2nbfdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 67:
            return 'co2ofdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 66:
            return 'tcn2odiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 65:
            return 'tcch4diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 64:
            return 'tcco2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 63:
            return 'n2odiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 62:
            return 'ch4diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 61:
            return 'co2diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 54:
            return 'aersccdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 53:
            return 'aerltsdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 52:
            return 'aerdepdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 51:
            return 'aodlgdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 50:
            return 'aodsmdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 49:
            return 'aodprdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 48:
            return 'aerlgdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 47:
            return 'aersmdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 46:
            return 'aerprdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 42:
            return 'aerls12diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 41:
            return 'aerls11diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 40:
            return 'aerls10diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 39:
            return 'aerls09diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 38:
            return 'aerls08diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 37:
            return 'aerls07diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 36:
            return 'aerls06diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 35:
            return 'aerls05diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 34:
            return 'aerls04diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 33:
            return 'aerls03diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 32:
            return 'aerls02diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 31:
            return 'aerls01diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 27:
            return 'aergn12diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 26:
            return 'aergn11diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 25:
            return 'aergn10diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 24:
            return 'aergn09diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 23:
            return 'aergn08diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 22:
            return 'aergn07diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 21:
            return 'aergn06diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 20:
            return 'aergn05diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 19:
            return 'aergn04diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 18:
            return 'aergn03diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 17:
            return 'aergn02diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 16:
            return 'aergn01diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 12:
            return 'aermr12diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 11:
            return 'aermr11diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 10:
            return 'aermr10diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 9:
            return 'aermr09diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 8:
            return 'aermr08diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 7:
            return 'aermr07diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 6:
            return 'aermr06diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 5:
            return 'aermr05diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 4:
            return 'aermr04diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 3:
            return 'aermr03diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 2:
            return 'aermr02diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 1:
            return 'aermr01diff'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 216:
            return 'aod1240'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 215:
            return 'aod865'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 214:
            return 'aod670'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 213:
            return 'aod469'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 212:
            return 'suaod550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 211:
            return 'bcaod550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 210:
            return 'omaod550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 209:
            return 'duaod550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 208:
            return 'ssaod550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 207:
            return 'aod550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 206:
            return 'gtco3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 203:
            return 'go3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 185:
            return 'sf6apf'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 184:
            return 'tcsf6'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 183:
            return 'tcra'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 182:
            return 'sf6'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 181:
            return 'ra'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 166:
            return 'sfgr10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 165:
            return 'sfgr9'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 164:
            return 'sfgr8'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 163:
            return 'sfgr7'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 162:
            return 'sfgr6'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 161:
            return 'sfgr5'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 160:
            return 'sfgr4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 159:
            return 'sfgr3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 158:
            return 'sfgr2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 157:
            return 'sfgr1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 156:
            return 'sfgo3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 155:
            return 'sfhcho'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 154:
            return 'sfco2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 153:
            return 'sfso2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 152:
            return 'sfno2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 151:
            return 'sfnox'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 150:
            return 'tcgrg10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 149:
            return 'grg10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 148:
            return 'tcgrg9'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 147:
            return 'grg9'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 146:
            return 'tcgrg8'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 145:
            return 'grg8'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 144:
            return 'tcgrg7'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 143:
            return 'grg7'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 142:
            return 'tcgrg6'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 141:
            return 'grg6'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 140:
            return 'tcgrg5'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 139:
            return 'grg5'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 138:
            return 'tcgrg4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 137:
            return 'grg4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 136:
            return 'tcgrg3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 135:
            return 'grg3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 134:
            return 'tcgrg2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 133:
            return 'grg2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 132:
            return 'tcgrg1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 131:
            return 'grg1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 130:
            return 'tcnox'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 129:
            return 'nox'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 128:
            return 'tchcho'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 127:
            return 'tcco'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 126:
            return 'tcso2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 125:
            return 'tcno2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 124:
            return 'hcho'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 123:
            return 'co'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 122:
            return 'so2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 121:
            return 'no2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 100:
            return 'crfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 99:
            return 'frpfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 98:
            return 'nofrp'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 97:
            return 'offire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 96:
            return 'flfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 95:
            return 'ccfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 94:
            return 'vegfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 93:
            return 'c4ffire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 92:
            return 'cfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 91:
            return 'bcfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 90:
            return 'ocfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 89:
            return 'tcfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 88:
            return 'tpmfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 87:
            return 'pm2p5fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 86:
            return 'n2ofire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 85:
            return 'noxfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 84:
            return 'h2fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 83:
            return 'nmhcfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 82:
            return 'ch4fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 81:
            return 'cofire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 80:
            return 'co2fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 71:
            return 'kch4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 70:
            return 'ch4f'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 69:
            return 'co2apf'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 68:
            return 'co2nbf'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 67:
            return 'co2of'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 66:
            return 'tcn2o'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 65:
            return 'tcch4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 64:
            return 'tcco2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 63:
            return 'n2o'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 62:
            return 'ch4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 61:
            return 'co2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 54:
            return 'aerscc'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 53:
            return 'aerlts'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 52:
            return 'aerdep'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 51:
            return 'aodlg'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 50:
            return 'aodsm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 49:
            return 'aodpr'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 48:
            return 'aerlg'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 47:
            return 'aersm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 46:
            return 'aerpr'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 42:
            return 'aerls12'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 41:
            return 'aerls11'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 40:
            return 'aerls10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 39:
            return 'aerls09'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 38:
            return 'aerls08'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 37:
            return 'aerls07'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 36:
            return 'aerls06'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 35:
            return 'aerls05'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 34:
            return 'aerls04'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 33:
            return 'aerls03'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 32:
            return 'aerls02'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 31:
            return 'aerls01'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 27:
            return 'aergn12'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 26:
            return 'aergn11'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 25:
            return 'aergn10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 24:
            return 'aergn09'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 23:
            return 'aergn08'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 22:
            return 'aergn07'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 21:
            return 'aergn06'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 20:
            return 'aergn05'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 19:
            return 'aergn04'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 18:
            return 'aergn03'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 17:
            return 'aergn02'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 16:
            return 'aergn01'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 12:
            return 'aermr12'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 11:
            return 'aermr11'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 10:
            return 'aermr10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 9:
            return 'aermr09'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 8:
            return 'aermr08'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 7:
            return 'aermr07'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 6:
            return 'aermr06'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 5:
            return 'aermr05'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 4:
            return 'aermr04'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 3:
            return 'aermr03'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 2:
            return 'aermr02'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 1:
            return 'aermr01'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 241:
            return 'cape_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 215:
            return 't_ice'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 203:
            return 't_snow'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 200:
            return 'w_i'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 187:
            return 'vmax_10m'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 139:
            return 'pp'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 113:
            return 'rain_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 112:
            return 'prs_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 111:
            return 'prr_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 102:
            return 'rain_gsp'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 101:
            return 'prs_gsp'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 100:
            return 'prr_gsp'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 99:
            return 'qrs_gsp'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 85:
            return 'snowlmt'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 84:
            return 'hzerocl'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 82:
            return 'htop_dc'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 79:
            return 'dv_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 78:
            return 'du_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 77:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 76:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 75:
            return 'dqv_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 74:
            return 'dt_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 73:
            return 'top_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 72:
            return 'bas_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 71:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 70:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 69:
            return 'htop_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 68:
            return 'hbas_con'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 67:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 66:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 65:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 64:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 63:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 61:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 60:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 54:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 53:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 52:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 51:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 50:
            return 'ch_cm_cl'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 42:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 41:
            return 'twater'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 38:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 37:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 36:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 35:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 34:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 33:
            return 'qi'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 32:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 31:
            return 'qc'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 29:
            return 'clc'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 17:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 16:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 15:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 14:
            return 'thhr_rad'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 13:
            return 'sohr_rad'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 12:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 11:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 10:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 9:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 8:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 7:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 6:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 5:
            return 'apab_s'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 4:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 3:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 2:
            return '~'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 1:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 168:
            return '2ddiff'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 229:
            return 'tsm'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 173:
            return 'sr'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 171:
            return 'wiltsien'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 170:
            return 'cap'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 179:
            return 'ttr'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 178:
            return 'tsr'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 177:
            return 'str'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 176:
            return 'ssr'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 149:
            return 'tsw'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 236:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 202:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 201:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 183:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 175:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 170:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 168:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 167:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 164:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 139:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 49:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 42:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 41:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 40:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 39:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 34:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 31:
            return '~'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 6:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 236:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 202:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 201:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 183:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 175:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 170:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 168:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 167:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 164:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 139:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 49:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 42:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 41:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 40:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 39:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 34:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 31:
            return '~'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 9:
            return 'ssro'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 6:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 240:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 239:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 228:
            return 'tpara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 212:
            return 'soiara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 205:
            return 'roara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 197:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 196:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 195:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 189:
            return 'sundara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 182:
            return 'evara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 181:
            return 'nsssara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 180:
            return 'ewssara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 179:
            return 'ttrara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 178:
            return 'tsrara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 177:
            return 'strara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 176:
            return 'ssrara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 175:
            return 'strdara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 169:
            return 'ssrdara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 154:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 153:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 149:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 147:
            return 'slhfara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 146:
            return 'sshfara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 145:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 144:
            return 'sfara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 143:
            return 'mcpra'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 142:
            return 'lspara'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 50:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 48:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 45:
            return '~'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 44:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 240:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 239:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 228:
            return 'tprate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 212:
            return 'soira'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 205:
            return 'mrort'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 197:
            return 'gwdrate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 196:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 195:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 189:
            return 'msdr'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 182:
            return 'erate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 181:
            return 'nsssra'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 180:
            return 'ewssra'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 179:
            return 'mtntrf'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 178:
            return 'mtnsrf'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 177:
            return 'msntrf'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 176:
            return 'msnsrf'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 175:
            return 'msdtrf'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 169:
            return 'msdsrf'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 154:
            return 'mlwhr'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 153:
            return 'mswhr'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 149:
            return 'msnrf'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 147:
            return 'mslhfl'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 146:
            return 'msshfl'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 145:
            return 'bldrate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 144:
            return 'mtsfr'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 143:
            return 'cprate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 142:
            return 'mlsprt'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 50:
            return 'mlspfr'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 48:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 45:
            return '~'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 44:
            return 'esrate'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 254:
            return 'atmwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 253:
            return 'atzea'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 252:
            return 'athea'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 251:
            return 'attea'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 250:
            return 'iaa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 249:
            return 'aiwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 248:
            return 'cca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 247:
            return 'ciwca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 246:
            return 'clwca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 245:
            return 'flsra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 244:
            return 'fsra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 243:
            return 'fala'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 242:
            return 'alwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 241:
            return 'acfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 240:
            return 'lsfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 239:
            return 'csfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 238:
            return 'tsna'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 237:
            return 'swal4'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 236:
            return 'stal4'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 235:
            return 'skta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 234:
            return 'lsrha'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 233:
            return 'asqa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 232:
            return 'iea'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 231:
            return 'ishfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 230:
            return 'inssa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 229:
            return 'iewsa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 228:
            return 'tpa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 227:
            return 'crnha'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 226:
            return 'htlca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 225:
            return 'htcca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 224:
            return 'vdha'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 223:
            return 'ctmwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 222:
            return 'ctzwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 221:
            return 'nsgda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 220:
            return 'ewgda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 219:
            return 'vdmwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 218:
            return 'vdzwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 217:
            return 'dhlca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 216:
            return 'dhcca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 215:
            return 'dhvda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 214:
            return 'dhra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 212:
            return 'sia'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 211:
            return 'strca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 210:
            return 'ssrca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 209:
            return 'ttrca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 208:
            return 'tsrca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 207:
            return '10sia'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 206:
            return 'tco3a'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 205:
            return 'roa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 204:
            return 'pawa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 203:
            return 'o3a'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 202:
            return 'mn2ta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 201:
            return 'mx2ta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 200:
            return 'vsoa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 199:
            return 'vfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 198:
            return 'srca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 197:
            return 'gwda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 196:
            return 'mgwsa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 195:
            return 'lgwsa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 194:
            return 'btmpa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 193:
            return 'neova'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 192:
            return 'nwova'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 191:
            return 'nsova'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 190:
            return 'ewova'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 189:
            return 'sunda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 188:
            return 'hcca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 187:
            return 'mcca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 186:
            return 'lcca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 185:
            return 'ccca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 184:
            return 'swal3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 183:
            return 'stal3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 182:
            return 'ea'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 181:
            return 'nsssa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 180:
            return 'eqssa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 179:
            return 'ttra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 178:
            return 'tsra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 177:
            return 'stra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 176:
            return 'ssra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 175:
            return 'strda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 174:
            return 'ala'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 173:
            return 'sra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 171:
            return 'swal2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 170:
            return 'stal2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 169:
            return 'ssrda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 168:
            return '2da'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 167:
            return '2ta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 166:
            return '10va'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 165:
            return '10ua'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 164:
            return 'tcca'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 163:
            return 'slora'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 162:
            return 'anora'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 161:
            return 'isora'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 160:
            return 'sdora'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 159:
            return 'blha'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 158:
            return 'tspa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 157:
            return 'ra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 156:
            return 'gha'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 155:
            return 'da'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 154:
            return 'lwhra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 153:
            return 'swhra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 152:
            return 'lspa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 151:
            return 'msla'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 150:
            return 'tnra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 149:
            return 'snra'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 148:
            return 'chnka'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 147:
            return 'slhfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 146:
            return 'sshfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 145:
            return 'blda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 144:
            return 'sfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 143:
            return 'cpa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 142:
            return 'lspa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 141:
            return 'sda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 140:
            return 'swal1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 139:
            return 'stal1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 138:
            return 'voa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 137:
            return 'tcwva'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 136:
            return 'tcwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 135:
            return 'wa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 134:
            return 'spa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 133:
            return 'qa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 132:
            return 'va'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 131:
            return 'ua'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 130:
            return 'ta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 129:
            return 'za'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 128:
            return 'bva'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 127:
            return 'ata'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 125:
            return 'vitea'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 79:
            return 'tciwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 78:
            return 'tclwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 65:
            return 'sktda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 64:
            return 'ftsktda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 63:
            return 'stsktda'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 62:
            return 'obcta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 61:
            return 'tpoa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 60:
            return 'pva'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 59:
            return 'capea'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 58:
            return 'para'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 57:
            return 'uvba'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 56:
            return 'mn2d24a'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 55:
            return 'mn2t24a'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 54:
            return 'pa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 53:
            return 'monta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 52:
            return 'mn2t24a'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 51:
            return 'mx2t24a'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 50:
            return 'lspfa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 49:
            return '10fga'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 48:
            return 'magssa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 47:
            return 'dsrpa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 46:
            return 'sdura'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 45:
            return 'smlta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 44:
            return 'esa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 43:
            return 'slta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 42:
            return 'swval4'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 41:
            return 'swval3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 40:
            return 'swval2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 39:
            return 'swval1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 38:
            return 'istal4'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 37:
            return 'istal3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 36:
            return 'istal2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 35:
            return 'istal1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 34:
            return 'ssta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 33:
            return 'rsna'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 32:
            return 'asna'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 31:
            return 'sica'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 30:
            return 'tvha'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 29:
            return 'tvla'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 28:
            return 'cvha'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 27:
            return 'cvla'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 26:
            return 'cla'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 23:
            return 'ucdva'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 22:
            return 'uclna'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 21:
            return 'uctpa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 14:
            return 'vrwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 13:
            return 'urwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 12:
            return 'vdwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 11:
            return 'udwa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 5:
            return 'septa'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 4:
            return 'epta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 3:
            return 'pta'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 2:
            return 'vpota'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 1:
            return 'strfa'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 179:
            return 'ttr'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 171:
            return 'swl2'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 149:
            return 'tsw'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 233:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 232:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 231:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 230:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 229:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 227:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 226:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 225:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 224:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 223:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 222:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 221:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 220:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 219:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 218:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 217:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 216:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 215:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 214:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 213:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 212:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 207:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 206:
            return '~'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 113:
            return 'vtpha'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 112:
            return 'utpha'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 111:
            return 'qtpha'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 110:
            return 'ttpha'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 109:
            return 'tdcha'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 108:
            return 'tpfa'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 107:
            return 'ddra'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 106:
            return 'udra'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 105:
            return 'dmfa'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 104:
            return 'umfa'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 103:
            return 'trtca'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 102:
            return 'srtca'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 101:
            return 'trta'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 100:
            return 'srta'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 87:
            return 'viozd'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 86:
            return 'vitoed'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 85:
            return 'vigd'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 84:
            return 'viwvd'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 83:
            return 'vithed'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 82:
            return 'viked'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 81:
            return 'vimad'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 78:
            return 'viozn'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 77:
            return 'vioze'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 76:
            return 'vitoen'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 75:
            return 'vitoee'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 74:
            return 'vign'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 73:
            return 'vige'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 72:
            return 'viwvn'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 71:
            return 'viwve'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 70:
            return 'vithen'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 69:
            return 'vithee'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 68:
            return 'viken'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 67:
            return 'vikee'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 66:
            return 'viman'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 65:
            return 'vimae'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 64:
            return 'viec'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 63:
            return 'vitoe'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 62:
            return 'vipile'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 61:
            return 'vipie'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 60:
            return 'vithe'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 59:
            return 'vike'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 58:
            return 'vioz'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 57:
            return 'viiw'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 56:
            return 'vilw'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 55:
            return 'viwv'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 54:
            return 'vit'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 53:
            return 'vima'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 51:
            return '~'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 254:
            return 'hsdrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 249:
            return '~'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 247:
            return 'moflrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 246:
            return '10wsrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 243:
            return 'falrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 242:
            return 'ccrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 241:
            return 'clwcerrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 240:
            return 'lsfrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 239:
            return 'csfrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 231:
            return 'ishfrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 226:
            return 'wwrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 225:
            return 'wvrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 224:
            return 'wurea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 223:
            return 'wqrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 222:
            return 'wtrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 221:
            return 'wzrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 220:
            return 'vvrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 219:
            return 'vurea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 218:
            return 'vqrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 217:
            return 'vtrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 216:
            return 'vzrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 215:
            return 'uurea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 214:
            return 'uqrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 213:
            return 'utrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 212:
            return 'uzrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 211:
            return 'qqrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 210:
            return 'qtrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 209:
            return 'qzrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 208:
            return 'ttrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 207:
            return 'tzrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 206:
            return 'zzrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 205:
            return 'rorea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 202:
            return 'mn2trea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 201:
            return 'mx2trea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 199:
            return 'vegrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 198:
            return 'srcrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 184:
            return 'swl3rea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 182:
            return 'erea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 181:
            return 'nsssrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 180:
            return 'ewssrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 171:
            return 'swl2rea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 157:
            return 'rrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 156:
            return 'ghrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 144:
            return 'sfrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 143:
            return 'cprea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 142:
            return 'lsprea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 140:
            return 'swl1rea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 137:
            return 'pwcrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 135:
            return 'wrea'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 49:
            return '10fgrea'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 212:
            return 'psa'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 211:
            return 'pta'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 210:
            return 'fgbp'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 209:
            return 'bpa'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 208:
            return 'fgbs'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 207:
            return 'fgbt'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 206:
            return 'ebsl'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 205:
            return 'ebtl'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 204:
            return 'bmpga'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 203:
            return 'bzpga'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 202:
            return 'lsi'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 201:
            return 'lti'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 200:
            return 'ebsa'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 199:
            return 'ebta'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 194:
            return 'salbe'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 192:
            return 'bsal'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 191:
            return 'sale'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 190:
            return 'subi'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 188:
            return 'vvi'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 187:
            return 'uvi'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 186:
            return 'ebs'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 185:
            return 'ebt'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 184:
            return 'sali'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 183:
            return 'as'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 182:
            return 'ptbe'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 181:
            return 'apt'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 180:
            return 'bpt'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 179:
            return 'ptae'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 178:
            return 'pti'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 177:
            return 'ldu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 176:
            return 'ldp'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 174:
            return 'dsmax'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 173:
            return 'smax'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 172:
            return 'dumax'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 171:
            return 'umax'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 170:
            return 'mht'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 169:
            return 'zht'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 168:
            return 'mtr'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 167:
            return 'ztr'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 166:
            return 'vba1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 165:
            return 'uba1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 164:
            return 'tav300'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 162:
            return 'hfc'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 161:
            return 'dte'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 160:
            return 'shf'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 159:
            return 'sst'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 158:
            return 'pme'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 157:
            return 'asr'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 156:
            return 'nsf'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 155:
            return 'tki'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 154:
            return 'tauno'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 153:
            return 'taueo'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 152:
            return '~'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 151:
            return 'crl'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 150:
            return 'sh'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 149:
            return 'btp'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 148:
            return 'mld'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 147:
            return 'stfbarot'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 146:
            return 'sl_1'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 144:
            return 'vv'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 143:
            return 'uu'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 142:
            return 'vt'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 141:
            return 'ut'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 140:
            return 'uv'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 139:
            return 'rn'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 138:
            return 'sigmat'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 137:
            return 'dep'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 136:
            return 'vdf'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 135:
            return 'vvs'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 134:
            return 'mst'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 133:
            return 'wo'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 130:
            return 'so'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 129:
            return 'thetao'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 183:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 182:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 181:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 180:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 173:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 172:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 171:
            return 'nsf'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 170:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 169:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 168:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 155:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 154:
            return 'mld'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 153:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 152:
            return 'sl'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 147:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 146:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 145:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 144:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 143:
            return 'vv'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 142:
            return 'uu'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 141:
            return 'vt'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 140:
            return 'ut'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 139:
            return 'uv'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 137:
            return 'rn'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 135:
            return 'ocw'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 134:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 133:
            return '~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 131:
            return 'ocpd'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 130:
            return 'ocs'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 129:
            return 'ocpt'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 254:
            return 'wsp'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 253:
            return 'bfi'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 252:
            return 'wsk'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 251:
            return '2dfd'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 250:
            return '2dsp'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 249:
            return 'dwi'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 248:
            return 'arrc'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 247:
            return 'acwh'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 246:
            return 'awh'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 245:
            return 'wind'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 244:
            return 'msqs'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 243:
            return 'sdu'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 242:
            return 'mdwi'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 241:
            return 'mu10'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 240:
            return 'sdhs'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 239:
            return 'mpts'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 238:
            return 'mdts'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 237:
            return 'shts'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'mpww'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 235:
            return 'mdww'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'shww'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 233:
            return 'cdww'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 231:
            return 'pp1d'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 'pp1d'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 228:
            return 'dwps'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 227:
            return 'p2ps'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 226:
            return 'p1ps'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 225:
            return 'dwww'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 224:
            return 'p2ww'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 223:
            return 'p1ww'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 222:
            return 'wdw'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 221:
            return 'mp2'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 'mp2'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 220:
            return 'mp1'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 219:
            return 'wmb'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 218:
            return 'hmax'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 217:
            return 'tmax'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 200:
            return 'maxswh'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 92:
            return 'lccpg99'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 91:
            return 'lccpg90'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 90:
            return 'lccpg80'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 89:
            return 'lccpg70'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 88:
            return 'lccpg60'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 87:
            return 'lccpg50'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 86:
            return 'lccpg40'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 85:
            return 'lccpg30'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 84:
            return 'lccpg20'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 83:
            return 'lccpg10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 82:
            return 'mccpg99'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 81:
            return 'mccpg90'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 80:
            return 'mccpg80'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 79:
            return 'mccpg70'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 78:
            return 'mccpg60'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 77:
            return 'mccpg50'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 76:
            return 'mccpg40'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 75:
            return 'mccpg30'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 74:
            return 'mccpg20'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 73:
            return 'mccpg10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 72:
            return 'hccpg99'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 71:
            return 'hccpg90'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 70:
            return 'hccpg80'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 69:
            return 'hccpg70'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 68:
            return 'hccpg60'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 67:
            return 'hccpg50'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 66:
            return 'hccpg40'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 65:
            return 'hccpg30'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 64:
            return 'hccpg20'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 63:
            return 'hccpg10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 62:
            return 'tccpg99'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 61:
            return 'tccpg90'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 60:
            return 'tccpg80'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 59:
            return 'tccpg70'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 58:
            return 'tccpg60'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 57:
            return 'tccpg50'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 56:
            return 'tccpg40'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 55:
            return 'tccpg30'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 54:
            return 'tccpg20'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 53:
            return 'tccpg10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 52:
            return 'sfpg300'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 51:
            return 'sfpg200'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 50:
            return 'sfpg150'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 49:
            return 'sfpg100'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 48:
            return 'sfpg80'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 47:
            return 'sfpg60'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 46:
            return 'sfpg40'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 45:
            return 'sfpg20'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 44:
            return 'sfpg10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 43:
            return 'sfpg5'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 42:
            return 'sfpg1'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 41:
            return 'tppg300'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 40:
            return 'tppg200'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 39:
            return 'tppg150'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 38:
            return 'tppg100'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 37:
            return 'tppg80'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 36:
            return 'tppg60'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 35:
            return 'tppg40'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 34:
            return 'tppg20'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 33:
            return 'tppg10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 32:
            return 'tppg5'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 31:
            return 'tppg1'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 30:
            return '10gpg100'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 29:
            return '10gpg75'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 28:
            return '10gpg50'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 27:
            return '10gpg35'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 26:
            return '10gpg20'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 25:
            return '10spg50'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 24:
            return '10spg35'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 23:
            return '10spg20'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 22:
            return '10spg15'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 21:
            return '10spg10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 20:
            return 'mx2tpg45'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 19:
            return 'mx2tpg40'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 18:
            return 'mx2tpg35'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 17:
            return 'mx2tpg30'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 16:
            return 'mx2tpg25'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 15:
            return 'mn2tpl10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 14:
            return 'mn2tpl5'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 13:
            return 'mn2tpl0'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 12:
            return 'mn2tplm5'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 11:
            return 'mn2tplm10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 10:
            return '2tpg45'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 9:
            return '2tpg40'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 8:
            return '2tpg35'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 7:
            return '2tpg30'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 6:
            return '2tpg25'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 5:
            return '2tpl10'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 4:
            return '2tpl5'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 3:
            return '2tpl0'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 2:
            return '2tplm5'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 1:
            return '2tplm10'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 232:
            return 'mwpp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 229:
            return 'swhp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 228:
            return 'tpp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 202:
            return 'mn2tp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 201:
            return 'mx2tp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 167:
            return '2tp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 165:
            return '10sp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 164:
            return 'tccp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 151:
            return 'mslpp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 144:
            return 'sfp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 139:
            return 'stl1p'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 130:
            return 'tap'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 129:
            return 'zp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 81:
            return 'mwpg15'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 80:
            return 'mwpg12'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 79:
            return 'mwpg10'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 78:
            return 'mwpg8'

        probabilityType = h.get_l('probabilityType')
        scaleFactorOfLowerLimit = h.get_l('scaleFactorOfLowerLimit')
        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 8 and typeOfFirstFixedSurface == 101 and productDefinitionTemplateNumber == 5:
            return 'swhg8'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaledValueOfLowerLimit == 6 and productDefinitionTemplateNumber == 5 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 101 and probabilityType == 3:
            return 'swhg6'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaleFactorOfLowerLimit == 0 and probabilityType == 3 and scaledValueOfLowerLimit == 4 and productDefinitionTemplateNumber == 5 and typeOfFirstFixedSurface == 101:
            return 'swhg4'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 101 and productDefinitionTemplateNumber == 5 and probabilityType == 3 and scaledValueOfLowerLimit == 2:
            return 'swhg2'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 73:
            return '2tl273'

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and scaledValueOfLowerLimit == 25 and typeOfFirstFixedSurface == 103 and probabilityType == 3 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == 0:
            return '10fgg25'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 69:
            return '10spg15'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 68:
            return '10spg10'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 67:
            return 'tprg5'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 66:
            return 'tprg3'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 65:
            return 'tprl1'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 64:
            return 'tpl01'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 59:
            return 'capep'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 49:
            return '10gp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 25:
            return 'tag8'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 24:
            return 'tag4'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 23:
            return 'talm4'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 22:
            return 'talm8'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 21:
            return 'tag2'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 20:
            return 'talm2'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 18:
            return 'whip'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 17:
            return 'saip'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 16:
            return 'hslp'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 15:
            return 'h0dip'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 10:
            return 'mslag0'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 9:
            return 'stag0'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 8:
            return 'tpag0'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 7:
            return 'tpag10'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 6:
            return 'tpag20'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 5:
            return '2talm2'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 4:
            return '2talm1'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 3:
            return '2tag0'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 2:
            return '2tag1'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 1:
            return '2tag2'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 232:
            return 'mvv'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 231:
            return 'atmwax'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 230:
            return 'atzw'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 229:
            return 'ath'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 228:
            return 'att'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 226:
            return 'htlc'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 225:
            return 'htcc'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 224:
            return 'vdh'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 221:
            return 'nsgd'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 220:
            return 'ewgd'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 219:
            return 'vdmw'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 218:
            return 'vdzw'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 217:
            return 'dhlc'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 216:
            return 'dhcc'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 215:
            return 'dhvd'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 214:
            return 'dhr'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 213:
            return 'cf'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 212:
            return 'clw'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 211:
            return 'ttuc'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 210:
            return 'tsuc'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 209:
            return 'ttru'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 208:
            return 'tsru'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 254:
            return 'atmwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 253:
            return 'atzegrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 252:
            return 'athegrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 251:
            return 'attegrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 250:
            return 'icegrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 249:
            return 'aiwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 248:
            return 'ccgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 247:
            return 'ciwcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 246:
            return 'clwcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 245:
            return 'flsrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 244:
            return 'fsrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 243:
            return 'falgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 242:
            return 'alwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 241:
            return 'acfgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 240:
            return 'lsfgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 239:
            return 'csfgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 238:
            return 'tsngrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 237:
            return 'swl4grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 236:
            return 'stl4grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 235:
            return 'sktgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 234:
            return 'lsrhgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 233:
            return 'asqgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 232:
            return 'iegrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 231:
            return 'ishfgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 230:
            return 'inssgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 229:
            return 'iewsgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 228:
            return 'tpgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 227:
            return 'crnhgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 226:
            return 'htlcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 225:
            return 'htccgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 224:
            return 'vdhgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 223:
            return 'ctmwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 222:
            return 'ctzwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 221:
            return 'nsgdgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 220:
            return 'ewgdgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 219:
            return 'vdmwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 218:
            return 'vdzwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 217:
            return 'dhlcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 216:
            return 'dhccgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 215:
            return 'dhvdgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 214:
            return 'dhrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 212:
            return 'tisrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 211:
            return 'strcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 210:
            return 'ssrcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 209:
            return 'ttrcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 208:
            return 'tsrcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 207:
            return '10sigrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 206:
            return 'tco3grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 205:
            return 'rogrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 204:
            return 'pawgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 203:
            return 'o3grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 202:
            return 'mn2tgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 201:
            return 'mx2tgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 200:
            return 'vsogrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 199:
            return 'veggrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 198:
            return 'srcgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 197:
            return 'gwdgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 196:
            return 'mgwsgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 195:
            return 'lgwsgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 194:
            return 'btmpgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 193:
            return 'neovgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 192:
            return 'nwovgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 191:
            return 'nsovgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 190:
            return 'ewovgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 189:
            return 'sundgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 188:
            return 'hccgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 187:
            return 'mccgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 186:
            return 'lccgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 185:
            return 'cccgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 184:
            return 'swl3grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 183:
            return 'stl3grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 182:
            return 'egrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 181:
            return 'nsssgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 180:
            return 'ewssgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 179:
            return 'ttrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 178:
            return 'tsrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 177:
            return 'strgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 176:
            return 'ssrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 175:
            return 'strdgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 174:
            return 'algrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 173:
            return 'srgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 172:
            return 'lsmgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 171:
            return 'swl2grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 170:
            return 'stl2grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 169:
            return 'ssrdgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 168:
            return '2dgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 167:
            return '2tgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 166:
            return '10vgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 165:
            return '10ugrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 164:
            return 'tccgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 163:
            return 'slorgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 162:
            return 'anorgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 161:
            return 'isorgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 160:
            return 'sdorgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 159:
            return 'blhgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 158:
            return 'tspgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 157:
            return 'rgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 156:
            return 'ghgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 155:
            return 'dgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 154:
            return 'lwhrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 153:
            return 'swhrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 152:
            return 'lnspgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 151:
            return 'mslgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 150:
            return 'tnrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 149:
            return 'snrgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 148:
            return 'chnkgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 147:
            return 'slhfgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 146:
            return 'sshfgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 145:
            return 'bldgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 144:
            return 'sfgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 143:
            return 'cpgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 142:
            return 'lspgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 141:
            return 'sdgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 140:
            return 'swl1grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 139:
            return 'stl1grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 138:
            return 'vogrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 137:
            return 'tcwvgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 136:
            return 'tcwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 135:
            return 'wgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 134:
            return 'spgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 133:
            return 'qgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 132:
            return 'vgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 131:
            return 'ugrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 130:
            return 'tgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 129:
            return 'zgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 128:
            return 'bvgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 127:
            return 'atgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 125:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 123:
            return '10fg6grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 122:
            return 'mn2t6grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 121:
            return 'mx2t6grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 79:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 78:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 71:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 70:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 69:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 68:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 67:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 66:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 65:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 64:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 63:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 62:
            return 'obctgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 61:
            return 'tpogrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 60:
            return 'pvgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 59:
            return 'capegrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 58:
            return 'pargrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 57:
            return 'uvbgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 56:
            return 'mn2d24grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 55:
            return 'mean2t24grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 54:
            return 'presgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 53:
            return 'montgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 52:
            return 'mn2t24grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 51:
            return 'mx2t24grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 50:
            return 'lspfgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 49:
            return '10fggrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 48:
            return 'magssgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 47:
            return 'dsrpgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 46:
            return 'sdurgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 45:
            return 'smltgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 44:
            return 'esgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 43:
            return 'sltgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 42:
            return 'swvl4grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 41:
            return 'swvl3grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 40:
            return 'swvl2grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 39:
            return 'swvl1grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 38:
            return 'istl4grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 37:
            return 'istl3grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 36:
            return 'istl2grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 35:
            return 'istl1grd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 34:
            return 'sstkgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 33:
            return 'rsngrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 32:
            return 'asngrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 31:
            return 'sicgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 30:
            return 'tvhgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 29:
            return 'tvlgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 28:
            return 'cvhgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 27:
            return 'cvlgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 26:
            return 'clgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 23:
            return 'ucdvgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 22:
            return 'uclngrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 21:
            return 'uctpgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 14:
            return 'vrtwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 13:
            return 'urtwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 12:
            return 'vdvwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 11:
            return 'udvwgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 5:
            return 'septgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 4:
            return 'eqptgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 3:
            return 'ptgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 2:
            return 'vpotgrd'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 1:
            return 'strfgrd'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 255:
            return 'tcclw'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 252:
            return 'irr'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 251:
            return 'pev'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 250:
            return 'irrfr'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 248:
            return 'tccsw'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 130:
            return 'strdc'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 129:
            return 'ssrdc'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 103:
            return 'evavt'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 102:
            return 'evaow'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 101:
            return 'evabs'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 100:
            return 'evatc'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 94:
            return 'ist'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 93:
            return 'swv'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 92:
            return 'stf'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 91:
            return 'ccf'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 90:
            return 'tcsw'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 89:
            return 'tcrw'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'fco2rec'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'fco2gpp'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 'fco2nee'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 1:
            return 'aco2rec'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 1:
            return 'aco2gpp'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'aco2nee'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'recbfas'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'gppbfas'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 60:
            return 'licga6'

        lengthOfTimeRange = h.get_l('lengthOfTimeRange')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 6 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1:
            return 'licga6'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 59:
            return 'licga3'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 3 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1:
            return 'licga3'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 58:
            return 'litota6'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1:
            return 'litota6'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 57:
            return 'litota3'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 3:
            return 'litota3'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 53:
            return 'licga1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and lengthOfTimeRange == 1 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'licga1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 52:
            return 'licgi'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'licgi'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 51:
            return 'litota1'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 1 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'litota1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 50:
            return 'litoti'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'litoti'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 48:
            return 'hwbt1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 47:
            return 'hwbt0'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 43:
            return 'swi4'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 42:
            return 'swi3'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 41:
            return 'swi2'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 40:
            return 'swi1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 28:
            return '10fg3'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and indicatorOfUnitForTimeRange == 1 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 3 and lengthOfTimeRange == 3 and typeOfFirstFixedSurface == 103:
            return 'mn2t3'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and lengthOfTimeRange == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and indicatorOfUnitForTimeRange == 1 and scaledValueOfFirstFixedSurface == 2:
            return 'mx2t3'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 25:
            return 'hvis'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 23:
            return 'cbh'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 22:
            return 'cdir'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 21:
            return 'fdir'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 206:
            return 'dv_strataer'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 205:
            return 'dv_o3p'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 204:
            return 'dv_o1d'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 203:
            return 'dv_o'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 202:
            return 'dv_hf'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 201:
            return 'dv_hco'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 200:
            return 'dv_hcl'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 199:
            return 'dv_h2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 198:
            return 'dv_cloo'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 197:
            return 'dv_chbr3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 196:
            return 'dv_ch3o'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 195:
            return 'dv_ch2br2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 194:
            return 'dv_brono2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 193:
            return 'dv_brcl'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 192:
            return 'dv_br2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 191:
            return 'dv_br'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 190:
            return 'dv_ocs_c'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 189:
            return 'dv_so3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 188:
            return 'dv_sog2b'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 187:
            return 'dv_sog2a'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 186:
            return 'dv_sog1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 185:
            return 'dv_soa2b'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 184:
            return 'dv_soa2a'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 183:
            return 'dv_soa1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 182:
            return 'dv_addc'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 181:
            return 'dv_nh4no3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 180:
            return 'dv_addx'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 179:
            return 'dv_addt'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 178:
            return 'dv_ch3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 177:
            return 'dv_h_c'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 176:
            return 'dv_bro'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 175:
            return 'dv_cl_c'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 174:
            return 'dv_clo'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 173:
            return 'dv_n'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 172:
            return 'dv_terpooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 171:
            return 'dv_bry'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 170:
            return 'dv_terpo2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 169:
            return 'dv_cly'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 168:
            return 'dv_noy'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 167:
            return 'dv_xoh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 166:
            return 'dv_h2s'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 165:
            return 'dv_tolooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 164:
            return 'dv_tolo2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 163:
            return 'dv_dmso'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 162:
            return 'dv_toluene'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 161:
            return 'dv_isopooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 160:
            return 'dv_xooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 159:
            return 'dv_brox'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 158:
            return 'dv_clox'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 157:
            return 'dv_onitr'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 156:
            return 'dv_isopno3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 155:
            return 'dv_ox'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 154:
            return 'dv_sulf'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 153:
            return 'dv_hydrald'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 152:
            return 'dv_bigald'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 151:
            return 'dv_olnd'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 150:
            return 'dv_alkooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 149:
            return 'dv_olnn'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 148:
            return 'dv_alko2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 147:
            return 'dv_ketp'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 146:
            return 'dv_tco3_c'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 145:
            return 'dv_mpan'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 144:
            return 'dv_cslp'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 143:
            return 'dv_macrooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 142:
            return 'dv_xylp'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 141:
            return 'dv_macro2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 140:
            return 'dv_tolp'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 139:
            return 'dv_pho'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 138:
            return 'dv_mvk'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 137:
            return 'dv_limp'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 136:
            return 'dv_mco3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 135:
            return 'dv_apip'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 134:
            return 'dv_mekooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 133:
            return 'dv_isopo2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 132:
            return 'dv_meko2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 131:
            return 'dv_olip'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 130:
            return 'dv_eneo2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 129:
            return 'dv_oltp'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 128:
            return 'dv_mek'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 127:
            return 'dv_etep'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 126:
            return 'dv_bigalk'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 125:
            return 'dv_hc8p'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 124:
            return 'dv_bigene'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 123:
            return 'dv_hc5p'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 122:
            return 'dv_hc3p'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 121:
            return 'dv_ethp'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 120:
            return 'dv_ro2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 119:
            return 'dv_paa'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 118:
            return 'dv_hyac'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 117:
            return 'dv_op2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 116:
            return 'dv_pooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 115:
            return 'dv_po2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 114:
            return 'dv_c3h7ooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 113:
            return 'dv_hket'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 112:
            return 'dv_c3h7o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 111:
            return 'dv_udd'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 110:
            return 'dv_macr'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 109:
            return 'dv_dcb'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 108:
            return 'dv_eo'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 107:
            return 'dv_glyoxal'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 106:
            return 'dv_eo2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 105:
            return 'dv_ket'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 104:
            return 'dv_ch3coooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 103:
            return 'dv_ald'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 102:
            return 'dv_cresol'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 101:
            return 'dv_glyald'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 100:
            return 'dv_xyl'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 99:
            return 'dv_tol'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 98:
            return 'dv_ch3cho'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 97:
            return 'dv_lim'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 96:
            return 'dv_ch3cooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 95:
            return 'dv_api'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 94:
            return 'dv_c2h5ooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 93:
            return 'dv_dien'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 92:
            return 'dv_c2h5o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 91:
            return 'dv_oli'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 90:
            return 'dv_olt'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 89:
            return 'dv_hc8'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 88:
            return 'dv_hc5'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 87:
            return 'dv_hc3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 86:
            return 'dv_hono'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 85:
            return 'dv_h2so4'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 84:
            return 'dv_ha2402'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 83:
            return 'dv_ha1301'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 82:
            return 'dv_ha1211'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 81:
            return 'dv_ha1202'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 80:
            return 'dv_ch3br'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 79:
            return 'dv_hcfc22'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 78:
            return 'dv_ch3cl'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 77:
            return 'dv_ch3ccl3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 76:
            return 'dv_ccl4'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 75:
            return 'dv_cfc115'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 74:
            return 'dv_cfc114'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 73:
            return 'dv_cfc113'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 72:
            return 'dv_cfc12'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 71:
            return 'dv_cfc11'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 70:
            return 'dv_hobr'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 69:
            return 'dv_cl2o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 68:
            return 'dv_hbr'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 67:
            return 'dv_clno2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 66:
            return 'dv_cl2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 65:
            return 'dv_hocl'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 64:
            return 'dv_clono2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 63:
            return 'dv_oclo'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 62:
            return 'dv_o2_1d'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 61:
            return 'dv_o2_1s'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 60:
            return 'dv_o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 59:
            return 'dv_h2o'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 58:
            return 'dv_n2o_c'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 57:
            return 'dv_co2_c'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 56:
            return 'dv_noxa'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 55:
            return 'dv_hypropo2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 54:
            return 'dv_ic3h7o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 53:
            return 'dv_aco2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 52:
            return 'dv_ch3coch3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 51:
            return 'dv_no3_a'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 50:
            return 'dv_ispd'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 49:
            return 'dv_c10h16'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 48:
            return 'dv_c3h6'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 47:
            return 'dv_c3h8'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 46:
            return 'dv_c2h5oh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 45:
            return 'dv_c2h6'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 44:
            return 'dv_mcooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 43:
            return 'dv_hcooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 42:
            return 'dv_ch3oh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 41:
            return 'dv_psc'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 40:
            return 'dv_nh2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 39:
            return 'dv_xo2n'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 38:
            return 'dv_xo2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 37:
            return 'dv_rxpar'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 36:
            return 'dv_ror'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 35:
            return 'dv_c2o3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 34:
            return 'dv_ho2no2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 33:
            return 'dv_n2o5'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 32:
            return 'dv_no3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 31:
            return 'dv_no2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 30:
            return 'dv_oh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 29:
            return 'dv_ch3o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 28:
            return 'dv_ho2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 27:
            return 'dv_no'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 26:
            return 'dv_pb'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 25:
            return 'dv_ra'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 24:
            return 'dv_o3s'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 23:
            return 'dv_ch3cocho'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 22:
            return 'dv_msa'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 21:
            return 'dv_nh4'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 20:
            return 'dv_so4'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 19:
            return 'dv_nh3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 18:
            return 'dv_dms'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 17:
            return 'dv_so2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 16:
            return 'dv_c5h8'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 15:
            return 'dv_onit'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 14:
            return 'dv_rooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 13:
            return 'dv_pan'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 12:
            return 'dv_ald2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 11:
            return 'dv_ole'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 10:
            return 'dv_c2h4'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 9:
            return 'dv_par'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 8:
            return 'dv_hcho'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 7:
            return 'dv_ch3ooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 6:
            return 'dv_hno3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 5:
            return 'dv_co'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 4:
            return 'dv_ch4'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 3:
            return 'dv_h2o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 2:
            return 'dv_nox'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 1:
            return 'dv_go3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 220:
            return 'ch3cnfire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 219:
            return 'hcnfire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 218:
            return 'hc8fire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 217:
            return 'hc5fire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 216:
            return 'hc3fire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 215:
            return 'oltfire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 214:
            return 'limfire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 213:
            return 'xylfire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 212:
            return 'tolfire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 211:
            return 'apifire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 210:
            return 'ketfire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 209:
            return 'ald2fire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 208:
            return 'olefire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 207:
            return 'parfire'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 206:
            return 'e_strataer'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 205:
            return 'e_o3p'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 204:
            return 'e_o1d'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 203:
            return 'e_o'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 202:
            return 'e_hf'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 201:
            return 'e_hco'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 200:
            return 'e_hcl'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 199:
            return 'e_h2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 198:
            return 'e_cloo'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 197:
            return 'e_chbr3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 196:
            return 'e_ch3o'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 195:
            return 'e_ch2br2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 194:
            return 'e_brono2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 193:
            return 'e_brcl'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 192:
            return 'e_br2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 191:
            return 'e_br'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 190:
            return 'e_ocs_c'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 189:
            return 'e_so3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 188:
            return 'e_sog2b'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 187:
            return 'e_sog2a'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 186:
            return 'e_sog1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 185:
            return 'e_soa2b'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 184:
            return 'e_soa2a'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 183:
            return 'e_soa1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 182:
            return 'e_addc'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 181:
            return 'e_nh4no3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 180:
            return 'e_addx'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 179:
            return 'e_addt'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 178:
            return 'e_ch3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 177:
            return 'e_h_c'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 176:
            return 'e_bro'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 175:
            return 'e_cl_c'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 174:
            return 'e_clo'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 173:
            return 'e_n'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 172:
            return 'e_terpooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 171:
            return 'e_bry'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 170:
            return 'e_terpo2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 169:
            return 'e_cly'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 168:
            return 'e_noy'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 167:
            return 'e_xoh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 166:
            return 'e_h2s'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 165:
            return 'e_tolooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 164:
            return 'e_tolo2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 163:
            return 'e_dmso'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 162:
            return 'e_toluene'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 161:
            return 'e_isopooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 160:
            return 'e_xooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 159:
            return 'e_brox'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 158:
            return 'e_clox'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 157:
            return 'e_onitr'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 156:
            return 'e_isopno3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 155:
            return 'e_ox'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 154:
            return 'e_sulf'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 153:
            return 'e_hydrald'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 152:
            return 'e_bigald'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 151:
            return 'e_olnd'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 150:
            return 'e_alkooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 149:
            return 'e_olnn'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 148:
            return 'e_alko2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 147:
            return 'e_ketp'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 146:
            return 'e_tco3_c'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 145:
            return 'e_mpan'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 144:
            return 'e_cslp'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 143:
            return 'e_macrooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 142:
            return 'e_xylp'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 141:
            return 'e_macro2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 140:
            return 'e_tolp'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 139:
            return 'e_pho'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 138:
            return 'e_mvk'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 137:
            return 'e_limp'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 136:
            return 'e_mco3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 135:
            return 'e_apip'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 134:
            return 'e_mekooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 133:
            return 'e_isopo2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 132:
            return 'e_meko2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 131:
            return 'e_olip'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 130:
            return 'e_eneo2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 129:
            return 'e_oltp'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 128:
            return 'e_mek'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 127:
            return 'e_etep'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 126:
            return 'e_bigalk'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 125:
            return 'e_hc8p'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 124:
            return 'e_bigene'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 123:
            return 'e_hc5p'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 122:
            return 'e_hc3p'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 121:
            return 'e_ethp'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 120:
            return 'e_ro2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 119:
            return 'e_paa'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 118:
            return 'e_hyac'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 117:
            return 'e_op2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 116:
            return 'e_pooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 115:
            return 'e_po2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 114:
            return 'e_c3h7ooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 113:
            return 'e_hket'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 112:
            return 'e_c3h7o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 111:
            return 'e_udd'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 110:
            return 'e_macr'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 109:
            return 'e_dcb'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 108:
            return 'e_eo'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 107:
            return 'e_glyoxal'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 106:
            return 'e_eo2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 105:
            return 'e_ket'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 104:
            return 'e_ch3coooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 103:
            return 'e_ald'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 102:
            return 'e_cresol'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 101:
            return 'e_glyald'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 100:
            return 'e_xyl'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 99:
            return 'e_tol'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 98:
            return 'e_ch3cho'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 97:
            return 'e_lim'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 96:
            return 'e_ch3cooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 95:
            return 'e_api'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 94:
            return 'e_c2h5ooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 93:
            return 'e_dien'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 92:
            return 'e_c2h5o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 91:
            return 'e_oli'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 90:
            return 'e_olt'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 89:
            return 'e_hc8'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 88:
            return 'e_hc5'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 87:
            return 'e_hc3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 86:
            return 'e_hono'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 85:
            return 'e_h2so4'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 84:
            return 'e_ha2402'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 83:
            return 'e_ha1301'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 82:
            return 'e_ha1211'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 81:
            return 'e_ha1202'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 80:
            return 'e_ch3br'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 79:
            return 'e_hcfc22'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 78:
            return 'e_ch3cl'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 77:
            return 'e_ch3ccl3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 76:
            return 'e_ccl4'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 75:
            return 'e_cfc115'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 74:
            return 'e_cfc114'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 73:
            return 'e_cfc113'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 72:
            return 'e_cfc12'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 71:
            return 'e_cfc11'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 70:
            return 'e_hobr'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 69:
            return 'e_cl2o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 68:
            return 'e_hbr'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 67:
            return 'e_clno2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 66:
            return 'e_cl2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 65:
            return 'e_hocl'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 64:
            return 'e_clono2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 63:
            return 'e_oclo'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 62:
            return 'e_o2_1d'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 61:
            return 'e_o2_1s'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 60:
            return 'e_o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 59:
            return 'e_h2o'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 58:
            return 'e_n2o_c'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 57:
            return 'e_co2_c'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 56:
            return 'e_noxa'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 55:
            return 'e_hypropo2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 54:
            return 'e_ic3h7o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 53:
            return 'e_aco2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 52:
            return 'e_ch3coch3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 51:
            return 'e_no3_a'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 50:
            return 'e_ispd'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 49:
            return 'e_c10h16'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 48:
            return 'e_c3h6'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 47:
            return 'e_c3h8'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 46:
            return 'e_c2h5oh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 45:
            return 'e_c2h6'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 44:
            return 'e_mcooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 43:
            return 'e_hcooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 42:
            return 'e_ch3oh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 41:
            return 'e_psc'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 40:
            return 'e_nh2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 39:
            return 'e_xo2n'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 38:
            return 'e_xo2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 37:
            return 'e_rxpar'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 36:
            return 'e_ror'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 35:
            return 'e_c2o3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 34:
            return 'e_ho2no2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 33:
            return 'e_n2o5'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 32:
            return 'e_no3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 31:
            return 'e_no2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 30:
            return 'e_oh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 29:
            return 'e_ch3o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 28:
            return 'e_ho2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 27:
            return 'e_no'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 26:
            return 'e_pb'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 25:
            return 'e_ra'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 24:
            return 'e_o3s'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 23:
            return 'e_ch3cocho'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 22:
            return 'e_msa'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 21:
            return 'e_nh4'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 20:
            return 'e_so4'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 19:
            return 'e_nh3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 18:
            return 'e_dms'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 17:
            return 'e_so2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 16:
            return 'e_c5h8'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 15:
            return 'e_onit'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 14:
            return 'e_rooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 13:
            return 'e_pan'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 12:
            return 'e_ald2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 11:
            return 'e_ole'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 10:
            return 'e_c2h4'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 9:
            return 'e_par'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 8:
            return 'e_hcho'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 7:
            return 'e_ch3ooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 6:
            return 'e_hno3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 5:
            return 'e_co'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 4:
            return 'e_ch4'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 3:
            return 'e_h2o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 2:
            return 'e_nox'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 1:
            return 'e_go3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 206:
            return 'tc_strataer'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 205:
            return 'tc_o3p'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 204:
            return 'tc_o1d'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 203:
            return 'tc_o'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 202:
            return 'tc_hf'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 201:
            return 'tc_hco'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 200:
            return 'tc_hcl'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 199:
            return 'tc_h2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 198:
            return 'tc_cloo'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 197:
            return 'tc_chbr3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 196:
            return 'tc_ch3o'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 195:
            return 'tc_ch2br2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 194:
            return 'tc_brono2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 193:
            return 'tc_brcl'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 192:
            return 'tc_br2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 191:
            return 'tc_br'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 190:
            return 'tc_ocs_c'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 189:
            return 'tc_so3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 188:
            return 'tc_sog2b'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 187:
            return 'tc_sog2a'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 186:
            return 'tc_sog1'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 185:
            return 'tc_soa2b'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 184:
            return 'tc_soa2a'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 183:
            return 'tc_soa1'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 182:
            return 'tc_addc'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 181:
            return 'tc_nh4no3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 180:
            return 'tc_addx'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 179:
            return 'tc_addt'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 178:
            return 'tc_ch3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 177:
            return 'tc_h_c'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 176:
            return 'tc_bro'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 175:
            return 'tc_cl_c'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 174:
            return 'tc_clo'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 173:
            return 'tc_n'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 172:
            return 'tc_terpooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 171:
            return 'tc_bry'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 170:
            return 'tc_terpo2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 169:
            return 'tc_cly'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 168:
            return 'tc_noy'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 167:
            return 'tc_xoh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 166:
            return 'tc_h2s'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 165:
            return 'tc_tolooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 164:
            return 'tc_tolo2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 163:
            return 'tc_dmso'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 162:
            return 'tc_toluene'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 161:
            return 'tc_isopooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 160:
            return 'tc_xooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 159:
            return 'tc_brox'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 158:
            return 'tc_clox'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 157:
            return 'tc_onitr'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 156:
            return 'tc_isopno3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 155:
            return 'tc_ox'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 154:
            return 'tc_sulf'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 153:
            return 'tc_hydrald'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 152:
            return 'tc_bigald'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 151:
            return 'tc_olnd'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 150:
            return 'tc_alkooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 149:
            return 'tc_olnn'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 148:
            return 'tc_alko2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 147:
            return 'tc_ketp'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 146:
            return 'tc_tco3_c'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 145:
            return 'tc_mpan'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 144:
            return 'tc_cslp'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 143:
            return 'tc_macrooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 142:
            return 'tc_xylp'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 141:
            return 'tc_macro2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 140:
            return 'tc_tolp'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 139:
            return 'tc_pho'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 138:
            return 'tc_mvk'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 137:
            return 'tc_limp'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 136:
            return 'tc_mco3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 135:
            return 'tc_apip'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 134:
            return 'tc_mekooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 133:
            return 'tc_isopo2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 132:
            return 'tc_meko2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 131:
            return 'tc_olip'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 130:
            return 'tc_eneo2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 129:
            return 'tc_oltp'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 128:
            return 'tc_mek'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 127:
            return 'tc_etep'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 126:
            return 'tc_bigalk'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 125:
            return 'tc_hc8p'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 124:
            return 'tc_bigene'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 123:
            return 'tc_hc5p'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 122:
            return 'tc_hc3p'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 121:
            return 'tc_ethp'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 120:
            return 'tc_ro2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 119:
            return 'tc_paa'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 118:
            return 'tc_hyac'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 117:
            return 'tc_op2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 116:
            return 'tc_pooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 115:
            return 'tc_po2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 114:
            return 'tc_c3h7ooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 113:
            return 'tc_hket'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 112:
            return 'tc_c3h7o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 111:
            return 'tc_udd'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 110:
            return 'tc_macr'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 109:
            return 'tc_dcb'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 108:
            return 'tc_eo'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 107:
            return 'tc_glyoxal'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 106:
            return 'tc_eo2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 105:
            return 'tc_ket'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 104:
            return 'tc_ch3coooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 103:
            return 'tc_ald'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 102:
            return 'tc_cresol'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 101:
            return 'tc_glyald'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 100:
            return 'tc_xyl'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 99:
            return 'tc_tol'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 98:
            return 'tc_ch3cho'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 97:
            return 'tc_lim'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 96:
            return 'tc_ch3cooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 95:
            return 'tc_api'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 94:
            return 'tc_c2h5ooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 93:
            return 'tc_dien'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 92:
            return 'tc_c2h5o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 91:
            return 'tc_oli'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 90:
            return 'tc_olt'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 89:
            return 'tc_hc8'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 88:
            return 'tc_hc5'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 87:
            return 'tc_hc3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 86:
            return 'tc_hono'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 85:
            return 'tc_h2so4'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 84:
            return 'tc_ha2402'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 83:
            return 'tc_ha1301'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 82:
            return 'tc_ha1211'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 81:
            return 'tc_ha1202'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 80:
            return 'tc_ch3br'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 79:
            return 'tc_hcfc22'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 78:
            return 'tc_ch3cl'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 77:
            return 'tc_ch3ccl3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 76:
            return 'tc_ccl4'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 75:
            return 'tc_cfc115'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 74:
            return 'tc_cfc114'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 73:
            return 'tc_cfc113'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 72:
            return 'tc_cfc12'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 71:
            return 'tc_cfc11'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 70:
            return 'tc_hobr'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 69:
            return 'tc_cl2o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 68:
            return 'tc_hbr'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 67:
            return 'tc_clno2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 66:
            return 'tc_cl2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 65:
            return 'tc_hocl'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 64:
            return 'tc_clono2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 63:
            return 'tc_oclo'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 62:
            return 'tc_o2_1d'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 61:
            return 'tc_o2_1s'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 60:
            return 'tc_o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 59:
            return 'tc_h2o'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 58:
            return 'tc_n2o_c'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 57:
            return 'tc_co2_c'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 56:
            return 'tc_noxa'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 55:
            return 'tc_hypropo2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 54:
            return 'tc_ic3h7o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 53:
            return 'tc_aco2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 52:
            return 'tc_ch3coch3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 51:
            return 'tc_no3_a'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 50:
            return 'tc_ispd'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 49:
            return 'tc_c10h16'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 48:
            return 'tc_c3h6'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 47:
            return 'tc_c3h8'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 46:
            return 'tc_c2h5oh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 45:
            return 'tc_c2h6'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 44:
            return 'tc_mcooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 43:
            return 'tc_hcooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 42:
            return 'tc_ch3oh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 41:
            return 'tc_psc'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 40:
            return 'tc_nh2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 39:
            return 'tc_xo2n'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 38:
            return 'tc_xo2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 37:
            return 'tc_rxpar'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 36:
            return 'tc_ror'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 35:
            return 'tc_c2o3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 34:
            return 'tc_ho2no2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 33:
            return 'tc_n2o5'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 32:
            return 'tc_no3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 30:
            return 'tc_oh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 29:
            return 'tc_ch3o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 28:
            return 'tc_ho2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 27:
            return 'tc_no'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 26:
            return 'tc_pb'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 24:
            return 'tc_o3s'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 23:
            return 'tc_ch3cocho'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 22:
            return 'tc_msa'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 21:
            return 'tc_nh4'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 20:
            return 'tc_so4'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 19:
            return 'tc_nh3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 18:
            return 'tc_dms'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 16:
            return 'tc_c5h8'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 15:
            return 'tc_onit'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 14:
            return 'tc_rooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 13:
            return 'tc_pan'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 12:
            return 'tc_ald2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 11:
            return 'tc_ole'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 10:
            return 'tc_c2h4'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 9:
            return 'tc_par'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 7:
            return 'tc_ch3ooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 6:
            return 'tc_hno3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 4:
            return 'tc_ch4'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 3:
            return 'tc_h2o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 206:
            return 'strataer'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 205:
            return 'o3p'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 204:
            return 'o1d'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 203:
            return 'o'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 202:
            return 'hf'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 201:
            return 'hco'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 200:
            return 'hcl'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 199:
            return 'h2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 198:
            return 'cloo'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 197:
            return 'chbr3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 196:
            return 'ch3o'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 195:
            return 'ch2br2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 194:
            return 'brono2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 193:
            return 'brcl'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 192:
            return 'br2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 191:
            return 'br'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 190:
            return 'ocs_c'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 189:
            return 'so3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 188:
            return 'sog2b'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 187:
            return 'sog2a'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 186:
            return 'sog1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 185:
            return 'soa2b'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 184:
            return 'soa2a'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 183:
            return 'soa1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 182:
            return 'addc'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 181:
            return 'nh4no3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 180:
            return 'addx'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 179:
            return 'addt'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 178:
            return 'ch3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 177:
            return 'h_c'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 176:
            return 'bro'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 175:
            return 'cl_c'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 174:
            return 'clo'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 173:
            return 'n'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 172:
            return 'terpooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 171:
            return 'bry'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 170:
            return 'terpo2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 169:
            return 'cly'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 168:
            return 'noy'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 167:
            return 'xoh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 166:
            return 'h2s'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 165:
            return 'tolooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 164:
            return 'tolo2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 163:
            return 'dmso'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 162:
            return 'toluene'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 161:
            return 'isopooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 160:
            return 'xooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 159:
            return 'brox'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 158:
            return 'clox'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 157:
            return 'onitr'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 156:
            return 'isopno3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 155:
            return 'ox'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 154:
            return 'sulf'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 153:
            return 'hydrald'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 152:
            return 'bigald'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 151:
            return 'olnd'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 150:
            return 'alkooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 149:
            return 'olnn'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 148:
            return 'alko2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 147:
            return 'ketp'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 146:
            return 'tco3_c'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 145:
            return 'mpan'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 144:
            return 'cslp'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 143:
            return 'macrooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 142:
            return 'xylp'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 141:
            return 'macro2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 140:
            return 'tolp'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 139:
            return 'pho'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 138:
            return 'mvk'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 137:
            return 'limp'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 136:
            return 'mco3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 135:
            return 'apip'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 134:
            return 'mekooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 133:
            return 'isopo2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 132:
            return 'meko2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 131:
            return 'olip'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 130:
            return 'eneo2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 129:
            return 'oltp'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 128:
            return 'mek'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 127:
            return 'etep'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 126:
            return 'bigalk'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 125:
            return 'hc8p'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 124:
            return 'bigene'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 123:
            return 'hc5p'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 122:
            return 'hc3p'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 121:
            return 'ethp'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 120:
            return 'ro2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 119:
            return 'paa'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 118:
            return 'hyac'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 117:
            return 'op2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 116:
            return 'pooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 115:
            return 'po2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 114:
            return 'c3h7ooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 113:
            return 'hket'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 112:
            return 'c3h7o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 111:
            return 'udd'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 110:
            return 'macr'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 109:
            return 'dcb'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 108:
            return 'eo'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 107:
            return 'glyoxal'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 106:
            return 'eo2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 105:
            return 'ket'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 104:
            return 'ch3coooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 103:
            return 'ald'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 102:
            return 'cresol'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 101:
            return 'glyald'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 100:
            return 'xyl'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 99:
            return 'tol'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 98:
            return 'ch3cho'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 97:
            return 'lim'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 96:
            return 'ch3cooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 95:
            return 'api'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 94:
            return 'c2h5ooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 93:
            return 'dien'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 92:
            return 'c2h5o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 91:
            return 'oli'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 90:
            return 'olt'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 89:
            return 'hc8'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 88:
            return 'hc5'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 87:
            return 'hc3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 86:
            return 'hono'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 85:
            return 'h2so4'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 84:
            return 'ha2402'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 83:
            return 'ha1301'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 82:
            return 'ha1211'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 81:
            return 'ha1202'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 80:
            return 'ch3br'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 79:
            return 'hcfc22'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 78:
            return 'ch3cl'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 77:
            return 'ch3ccl3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 76:
            return 'ccl4'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 75:
            return 'cfc115'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 74:
            return 'cfc114'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 73:
            return 'cfc113'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 72:
            return 'cfc12'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 71:
            return 'cfc11'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 70:
            return 'hobr'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 69:
            return 'cl2o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 68:
            return 'hbr'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 67:
            return 'clno2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 66:
            return 'cl2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 65:
            return 'hocl'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 64:
            return 'clono2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 63:
            return 'oclo'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 62:
            return 'o2_1d'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 61:
            return 'o2_1s'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 60:
            return 'o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 59:
            return 'h2o'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 58:
            return 'n2o_c'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 57:
            return 'co2_c'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 56:
            return 'noxa'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 55:
            return 'hypropo2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 54:
            return 'ic3h7o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 53:
            return 'aco2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 52:
            return 'ch3coch3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 51:
            return 'no3_a'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 50:
            return 'ispd'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 49:
            return 'c10h16'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 48:
            return 'c3h6'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 47:
            return 'c3h8'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 46:
            return 'c2h5oh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 45:
            return 'c2h6'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 44:
            return 'mcooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 43:
            return 'hcooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 42:
            return 'ch3oh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 41:
            return 'psc'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 40:
            return 'nh2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 39:
            return 'xo2n'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 38:
            return 'xo2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 37:
            return 'rxpar'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 36:
            return 'ror'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 35:
            return 'c2o3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 34:
            return 'ho2no2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 33:
            return 'n2o5'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 32:
            return 'no3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 30:
            return 'oh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 29:
            return 'ch3o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 28:
            return 'ho2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 27:
            return 'no'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 26:
            return 'pb'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 24:
            return 'o3s'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 23:
            return 'ch3cocho'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 22:
            return 'msa'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 21:
            return 'nh4'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 20:
            return 'so4'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 19:
            return 'nh3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 18:
            return 'dms'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 16:
            return 'c5h8'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 15:
            return 'onit'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 14:
            return 'rooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 13:
            return 'pan'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 12:
            return 'ald2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 11:
            return 'ole'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 10:
            return 'c2h4'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 9:
            return 'par'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 7:
            return 'ch3ooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 6:
            return 'hno3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 4:
            return 'ch4_c'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 3:
            return 'h2o2'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 254:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 253:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 252:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 251:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 250:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 249:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 248:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 247:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 246:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 245:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 244:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 243:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 242:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 241:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 240:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 239:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 238:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 237:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 236:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 235:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 234:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 233:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 232:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 231:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 230:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 229:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 228:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 227:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 226:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 225:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 224:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 223:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 222:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 221:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 220:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 219:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 218:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 217:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 216:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 215:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 214:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 213:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 212:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 207:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 206:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 205:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 204:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 203:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 202:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 201:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 200:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 199:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 198:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 197:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 196:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 195:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 194:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 193:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 192:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 191:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 190:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 189:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 188:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 187:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 186:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 185:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 184:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 183:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 182:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 181:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 180:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 179:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 178:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 177:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 176:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 175:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 174:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 173:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 172:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 171:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 170:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 169:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 168:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 167:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 166:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 165:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 164:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 162:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 159:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 158:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 157:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 156:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 155:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 154:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 153:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 152:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 151:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 149:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 147:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 146:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 145:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 144:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 143:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 142:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 141:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 140:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 139:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 138:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 137:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 136:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 135:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 134:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 133:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 132:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 131:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 130:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 129:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 125:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 124:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 123:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 122:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 121:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 79:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 78:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 77:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 76:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 75:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 74:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 73:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 72:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 71:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 70:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 69:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 68:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 67:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 66:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 65:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 64:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 63:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 61:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 60:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 59:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 58:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 57:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 54:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 53:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 52:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 51:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 50:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 49:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 48:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 47:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 46:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 45:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 44:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 43:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 42:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 41:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 40:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 39:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 38:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 37:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 36:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 35:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 34:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 33:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 32:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 31:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 29:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 28:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 27:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 26:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 23:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 21:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 20:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 19:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 18:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 17:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 16:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 15:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 14:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 13:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 12:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 11:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 10:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 9:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 8:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 7:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 6:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 5:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 4:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 3:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 2:
            return '~'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 1:
            return '~'

        aerosolType = h.get_l('aerosolType')
        is_aerosol = h.get_l('is_aerosol')

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and aerosolType == 62003 and is_aerosol == 1:
            return 'aerngtam'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 62003 and is_aerosol == 1:
            return 'aersrcam'

        typeOfSizeInterval = h.get_l('typeOfSizeInterval')
        is_aerosol_optical = h.get_l('is_aerosol_optical')
        typeOfWavelengthInterval = h.get_l('typeOfWavelengthInterval')
        scaleFactorOfFirstWavelength = h.get_l('scaleFactorOfFirstWavelength')
        scaledValueOfFirstWavelength = h.get_l('scaledValueOfFirstWavelength')

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfSizeInterval == 255 and aerosolType == 65533 and is_aerosol_optical == 1 and typeOfWavelengthInterval == 11 and scaleFactorOfFirstWavelength == 8 and scaledValueOfFirstWavelength == 55:
            return 'aerodnic'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and is_aerosol_optical == 1 and typeOfWavelengthInterval == 11 and scaleFactorOfFirstWavelength == 8 and scaledValueOfFirstWavelength == 55 and typeOfSizeInterval == 255 and aerosolType == 65534:
            return 'aerodnif'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and aerosolType == 65533 and is_aerosol == 1:
            return 'aermssnic'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and aerosolType == 65534 and is_aerosol == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'aermssnif'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and aerosolType == 65533 and is_aerosol == 1:
            return 'aerngtnic'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and aerosolType == 65534 and is_aerosol == 1:
            return 'aerngtnif'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and aerosolType == 65533 and is_aerosol == 1:
            return 'aerwdcnic'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and aerosolType == 65534 and is_aerosol == 1:
            return 'aerwdcnif'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and aerosolType == 65533 and is_aerosol == 1:
            return 'aerwdlnic'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and aerosolType == 65534 and is_aerosol == 1:
            return 'aerwdlnif'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 65533 and is_aerosol == 1:
            return 'aersdmnic'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 65534 and is_aerosol == 1:
            return 'aersdmnif'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and is_aerosol == 1 and aerosolType == 65533:
            return 'aerddpnic'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 65534 and is_aerosol == 1:
            return 'aerddpnif'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and is_aerosol == 1 and aerosolType == 65533:
            return 'aersrcnic'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 65534 and is_aerosol == 1:
            return 'aersrcnif'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 188:
            return 'aerbackscatgnd1064'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 187:
            return 'aerbackscatgnd532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 186:
            return 'aerbackscatgnd355'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 185:
            return 'aerbackscattoa1064'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 184:
            return 'aerbackscattoa532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 183:
            return 'aerbackscattoa355'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 182:
            return 'aerext1064'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 181:
            return 'aerext532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 180:
            return 'aerext355'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 179:
            return 'asymmetry2130'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 178:
            return 'ssa2130'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 177:
            return 'aodfm2130'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 176:
            return 'aodabs2130'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 175:
            return 'aerodso2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 174:
            return 'aermssso2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 173:
            return 'aerngtso2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 172:
            return 'aerwdccso2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 171:
            return 'aerwdlsso2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 170:
            return 'aersdmso2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 169:
            return 'aerddpso2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 168:
            return 'aersrcso2'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 167:
            return 'asymmetry1640'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 166:
            return 'asymmetry1240'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 165:
            return 'asymmetry1064'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 164:
            return 'asymmetry1020'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 163:
            return 'asymmetry865'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 162:
            return 'asymmetry858'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 161:
            return 'asymmetry800'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 160:
            return 'asymmetry670'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 159:
            return 'asymmetry645'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 158:
            return 'asymmetry550'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 157:
            return 'asymmetry532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 156:
            return 'asymmetry500'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 155:
            return 'asymmetry469'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 154:
            return 'asymmetry440'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 153:
            return 'asymmetry400'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 152:
            return 'asymmetry380'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 151:
            return 'asymmetry355'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 150:
            return 'asymmetry340'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 149:
            return 'ssa1640'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 148:
            return 'ssa1240'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 147:
            return 'ssa1064'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 146:
            return 'ssa1020'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 145:
            return 'ssa865'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 144:
            return 'ssa858'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 143:
            return 'ssa800'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 142:
            return 'ssa670'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 141:
            return 'ssa645'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 140:
            return 'ssa550'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 139:
            return 'ssa532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 138:
            return 'ssa500'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 137:
            return 'ssa469'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 136:
            return 'ssa440'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 135:
            return 'ssa400'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 134:
            return 'ssa380'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 133:
            return 'ssa355'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 132:
            return 'ssa340'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 131:
            return 'aodfm1640'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 130:
            return 'aodfm1240'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 129:
            return 'aodfm1064'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 128:
            return 'aodfm1020'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 127:
            return 'aodfm865'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 126:
            return 'aodfm858'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 125:
            return 'aodfm800'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 124:
            return 'aodfm670'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 123:
            return 'aodfm645'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 122:
            return 'aodfm550'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 121:
            return 'aodfm532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 120:
            return 'aodfm500'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 119:
            return 'aodfm469'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 118:
            return 'aodfm440'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 117:
            return 'aodfm400'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 116:
            return 'aodfm380'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 115:
            return 'aodfm355'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 114:
            return 'aodfm340'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 113:
            return 'aodabs1640'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 112:
            return 'aodabs1240'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 111:
            return 'aodabs1064'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 110:
            return 'aodabs1020'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 109:
            return 'aodabs865'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 108:
            return 'aodabs858'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 107:
            return 'aodabs800'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 106:
            return 'aodabs670'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 105:
            return 'aodabs645'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 104:
            return 'aodabs550'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 103:
            return 'aodabs532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 102:
            return 'aodabs500'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 101:
            return 'aodabs469'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 100:
            return 'aodabs440'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 99:
            return 'aodabs400'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 98:
            return 'aodabs380'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 97:
            return 'aodabs355'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 96:
            return 'aodabs340'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 95:
            return 'aaot532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 94:
            return 'naot532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 93:
            return 'aot532'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 92:
            return 'aerdep10fg'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 91:
            return 'aerdep10si'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 90:
            return 'aluvpsn'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 89:
            return 'accaod550'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 88:
            return 'aerodsu'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 87:
            return 'aermsssu'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 86:
            return 'aerngtsu'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 85:
            return 'aerwdccsu'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 84:
            return 'aerwdlssu'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 83:
            return 'aersdmsu'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 82:
            return 'aerddpsu'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 81:
            return 'aersrcsu'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 80:
            return 'aerodbchphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 79:
            return 'aerodbchphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 78:
            return 'aermssbchphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 77:
            return 'aermssbchphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 76:
            return 'aerngtbchphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 75:
            return 'aerngtbchphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 74:
            return 'aerwdccbchphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 73:
            return 'aerwdccbchphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 72:
            return 'aerwdlsbchphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 71:
            return 'aerwdlsbchphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 70:
            return 'aersdmbchphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 69:
            return 'aersdmbchphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 68:
            return 'aerddpbchphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 67:
            return 'aerddpbchphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 66:
            return 'aersrcbchphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 65:
            return 'aersrcbchphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 64:
            return 'aerodomhphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 63:
            return 'aerodomhphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 62:
            return 'aermssomhphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 61:
            return 'aermssomhphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 60:
            return 'aerngtomhphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 59:
            return 'aerngtomhphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 58:
            return 'aerwdccomhphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 57:
            return 'aerwdccomhphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 56:
            return 'aerwdlsomhphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 55:
            return 'aerwdlsomhphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 54:
            return 'aersdmomhphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 53:
            return 'aersdmomhphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 52:
            return 'aerddpomhphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 51:
            return 'aerddpomhphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 50:
            return 'aersrcomhphil'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 49:
            return 'aersrcomhphob'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 48:
            return 'aeroddul'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 47:
            return 'aeroddum'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 46:
            return 'aeroddus'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 45:
            return 'aermssdul'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 44:
            return 'aermssdum'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 43:
            return 'aermssdus'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 42:
            return 'aerngtdul'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 41:
            return 'aerngtdum'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 40:
            return 'aerngtdus'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 39:
            return 'aerwdccdul'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 38:
            return 'aerwdccdum'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 37:
            return 'aerwdccdus'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 36:
            return 'aerwdlsdul'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 35:
            return 'aerwdlsdum'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 34:
            return 'aerwdlsdus'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 33:
            return 'aersdmdul'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 32:
            return 'aersdmdum'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 31:
            return 'aersdmdus'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 30:
            return 'aerddpdul'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 29:
            return 'aerddpdum'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 28:
            return 'aerddpdus'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 27:
            return 'aersrcdul'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 26:
            return 'aersrcdum'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 25:
            return 'aersrcdus'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 24:
            return 'aerodssl'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 23:
            return 'aerodssm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 22:
            return 'aerodsss'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 21:
            return 'aermssssl'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 20:
            return 'aermssssm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 19:
            return 'aermsssss'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 18:
            return 'aerngtssl'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 17:
            return 'aerngtssm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 16:
            return 'aerngtsss'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 15:
            return 'aerwdccssl'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 14:
            return 'aerwdccssm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 13:
            return 'aerwdccsss'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 12:
            return 'aerwdlsssl'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 11:
            return 'aerwdlsssm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 10:
            return 'aerwdlssss'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 9:
            return 'aersdmssl'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 8:
            return 'aersdmssm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 7:
            return 'aersdmsss'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 6:
            return 'aerddpssl'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 5:
            return 'aerddpssm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 4:
            return 'aerddpsss'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 3:
            return 'aersrcssl'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 2:
            return 'aersrcssm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 1:
            return 'aersrcsss'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 52:
            return 'aot340'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 51:
            return 'uvsflxcs395400'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 50:
            return 'uvsflxcs390395'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 49:
            return 'uvsflxcs385390'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 48:
            return 'uvsflxcs380385'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 47:
            return 'uvsflxcs375380'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 46:
            return 'uvsflxcs370375'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 45:
            return 'uvsflxcs365370'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 44:
            return 'uvsflxcs360365'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 43:
            return 'uvsflxcs355360'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 42:
            return 'uvsflxcs350355'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 41:
            return 'uvsflxcs345350'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 40:
            return 'uvsflxcs340345'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 39:
            return 'uvsflxcs335340'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 38:
            return 'uvsflxcs330335'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 37:
            return 'uvsflxcs325330'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 36:
            return 'uvsflxcs320325'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 35:
            return 'uvsflxcs315320'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 34:
            return 'uvsflxcs310315'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 33:
            return 'uvsflxcs305310'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 32:
            return 'uvsflxcs300305'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 31:
            return 'uvsflxcs295300'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 30:
            return 'uvsflxcs290295'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 29:
            return 'uvsflxcs285290'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 28:
            return 'uvsflxcs280285'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 27:
            return 'uvsflxt395400'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 26:
            return 'uvsflxt390395'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 25:
            return 'uvsflxt385390'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 24:
            return 'uvsflxt380385'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 23:
            return 'uvsflxt375380'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 22:
            return 'uvsflxt370375'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 21:
            return 'uvsflxt365370'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 20:
            return 'uvsflxt360365'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 19:
            return 'uvsflxt355360'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 18:
            return 'uvsflxt350355'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 17:
            return 'uvsflxt345350'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 16:
            return 'uvsflxt340345'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 15:
            return 'uvsflxt335340'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 14:
            return 'uvsflxt330335'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 13:
            return 'uvsflxt325330'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 12:
            return 'uvsflxt320325'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 11:
            return 'uvsflxt315320'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 10:
            return 'uvsflxt310315'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 9:
            return 'uvsflxt305310'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 8:
            return 'uvsflxt300305'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 7:
            return 'uvsflxt295300'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 6:
            return 'uvsflxt290295'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 5:
            return 'uvsflxt285290'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 4:
            return 'uvsflxt280285'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 3:
            return 'uvbedcs'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 2:
            return 'uvbed'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 1:
            return 'uvcossza'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 150:
            return 'spp50'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 149:
            return 'spp49'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 148:
            return 'spp48'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 147:
            return 'spp47'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 146:
            return 'spp46'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 145:
            return 'spp45'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 144:
            return 'spp44'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 143:
            return 'spp43'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 142:
            return 'spp42'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 141:
            return 'spp41'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 140:
            return 'spp40'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 139:
            return 'spp39'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 138:
            return 'spp38'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 137:
            return 'spp37'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 136:
            return 'spp36'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 135:
            return 'spp35'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 134:
            return 'spp34'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 133:
            return 'spp33'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 132:
            return 'spp32'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 131:
            return 'spp31'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 130:
            return 'spp30'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 129:
            return 'spp29'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 128:
            return 'spp28'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 127:
            return 'spp27'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 126:
            return 'spp26'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 125:
            return 'spp25'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 124:
            return 'spp24'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 123:
            return 'spp23'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 122:
            return 'spp22'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 121:
            return 'spp21'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 120:
            return 'spp20'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 119:
            return 'spp19'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 118:
            return 'spp18'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 117:
            return 'spp17'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 116:
            return 'spp16'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 115:
            return 'spp15'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 114:
            return 'spp14'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 113:
            return 'spp13'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 112:
            return 'spp12'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 111:
            return 'spp11'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 110:
            return 'spp10'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 109:
            return 'spp9'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 108:
            return 'spp8'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 107:
            return 'spp7'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 106:
            return 'spp6'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 105:
            return 'spp5'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 104:
            return 'spp4'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 103:
            return 'spp3'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 102:
            return 'spp2'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 101:
            return 'spp1'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 5:
            return 'sppt5'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 4:
            return 'sppt4'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 3:
            return 'sppt3'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 2:
            return 'sppt2'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 1:
            return 'sppt1'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 254:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 253:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 252:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 251:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 250:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 249:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 248:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 247:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 246:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 245:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 244:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 243:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 242:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 241:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 240:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 239:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 238:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 237:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 236:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 235:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 234:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 233:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 232:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 231:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 230:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 229:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 228:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 227:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 226:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 225:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 224:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 223:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 222:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 221:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 220:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 219:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 218:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 217:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 216:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 215:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 214:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 213:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 212:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 211:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 210:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 209:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 208:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 207:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 206:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 205:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 204:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 203:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 202:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 201:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 200:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 199:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 198:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 197:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 196:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 195:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 194:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 193:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 192:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 191:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 190:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 189:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 188:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 187:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 186:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 185:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 184:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 183:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 182:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 181:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 180:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 179:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 178:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 177:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 176:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 175:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 174:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 173:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 172:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 171:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 170:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 169:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 168:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 167:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 166:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 165:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 164:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 163:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 162:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 161:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 160:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 159:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 158:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 157:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 156:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 155:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 154:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 153:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 152:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 151:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 150:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 149:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 148:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 147:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 146:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 145:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 144:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 143:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 142:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 141:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 140:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 139:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 138:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 137:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 136:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 135:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 134:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 133:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 132:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 131:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 130:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 129:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 128:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 127:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 125:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 124:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 123:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 122:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 121:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 79:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 78:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 77:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 76:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 75:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 74:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 73:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 72:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 71:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 70:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 69:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 68:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 67:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 66:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 65:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 64:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 63:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 62:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 61:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 60:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 59:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 58:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 57:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 54:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 53:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 52:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 51:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 50:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 49:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 48:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 47:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 46:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 45:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 44:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 43:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 42:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 41:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 40:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 39:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 38:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 37:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 36:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 35:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 34:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 33:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 32:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 31:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 30:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 29:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 28:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 27:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 26:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 23:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 22:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 21:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 20:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 19:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 18:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 17:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 16:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 15:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 14:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 13:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 12:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 11:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 10:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 9:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 8:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 7:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 6:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 5:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 4:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 3:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 2:
            return '~'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 1:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 120:
            return 'aptdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 119:
            return 'alediff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 45:
            return 'aerwv04diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 44:
            return 'aerwv03diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 43:
            return 'emdmsdiff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 30:
            return 'aerwv02diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 29:
            return 'aerwv01diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 28:
            return 'aerpr03diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 15:
            return 'aermr15diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 14:
            return 'aermr14diff'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 13:
            return 'aermr13diff'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and aerosolType == 65533 and is_aerosol == 1:
            return 'aermr17'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and aerosolType == 65534 and is_aerosol == 1:
            return 'aermr16'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 246:
            return 'taedab550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 245:
            return 'taedec550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 244:
            return 'vashaod550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 243:
            return 'vsuaod550'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 242:
            return 'apb'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 241:
            return 'c7h16fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 240:
            return 'c6h14fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 239:
            return 'c5h12fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 238:
            return 'c4h10fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 237:
            return 'c8h16fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 236:
            return 'c6h12fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 235:
            return 'c5h10fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 234:
            return 'c4h8fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 233:
            return 'c8h10fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 232:
            return 'c6h6fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 231:
            return 'c7h8fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 230:
            return 'aod2130'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 229:
            return 'aod1640'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 228:
            return 'aod1064'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 227:
            return 'aod1020'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 226:
            return 'aod858'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 225:
            return 'aod800'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 224:
            return 'aod645'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 223:
            return 'aod532'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 222:
            return 'aod500'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 221:
            return 'aod440'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 220:
            return 'aod400'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 219:
            return 'aod380'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 218:
            return 'aod355'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 217:
            return 'aod340'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 197:
            return 'alnidg'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 196:
            return 'alnidv'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 195:
            return 'alnidi'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 194:
            return 'aluvdg'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 193:
            return 'aluvdv'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 192:
            return 'aluvdi'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 191:
            return 'alnipg'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 190:
            return 'alnipv'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 189:
            return 'alnipi'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 188:
            return 'aluvpg'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 187:
            return 'aluvpv'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 186:
            return 'aluvpi'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 179:
            return 'frpngtivar'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 177:
            return 'frpdayivar'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 169:
            return 'frpngtfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 167:
            return 'frpdayfire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 120:
            return 'apt'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 119:
            return 'mami'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 118:
            return 'c2h6fire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 79:
            return 'vafire'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 74:
            return 'pm10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 73:
            return 'pm2p5'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 72:
            return 'pm1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 60:
            return 'injh'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 59:
            return 'soapr'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 58:
            return 'monot'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 57:
            return 'ocnuc'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 56:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 55:
            return '~'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 45:
            return 'aerwv04'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 44:
            return 'aerwv03'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 43:
            return 'emdms'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 30:
            return 'aerwv02'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 29:
            return 'aerwv01'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 28:
            return 'aerpr03'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 15:
            return 'aermr15'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 14:
            return 'aermr14'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 13:
            return 'aermr13'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 122:
            return 'mn2t6a'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 121:
            return 'mx2t6a'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 7:
            return '100va'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 6:
            return '100ua'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 141:
            return 'qtendsc'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 140:
            return 'ttendsc'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 139:
            return 'vtendcs'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 138:
            return 'utendcs'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 137:
            return 'ipcs'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 136:
            return 'lpcs'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 135:
            return 'qitendcs'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 134:
            return 'qltendcs'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 133:
            return 'qtendcs'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 132:
            return 'ttendcs'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 131:
            return 'ipc'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 130:
            return 'lpc'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 129:
            return 'qtendcds'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 128:
            return 'ttendcds'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 127:
            return 'vtendcds'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 126:
            return 'utendcds'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 125:
            return 'ttends'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 124:
            return 'vtends'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 123:
            return 'utends'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 122:
            return 'qtendt'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 121:
            return 'ttendts'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 120:
            return 'vtendts'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 119:
            return 'utendts'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 118:
            return 'ttendr'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 117:
            return 'qtendd'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 116:
            return 'ttendd'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 115:
            return 'vtendd'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 114:
            return 'utendd'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 193:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 255:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 254:
            return 'atmwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 253:
            return 'atzediff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 252:
            return 'athediff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 251:
            return 'attediff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 250:
            return 'icediff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 249:
            return 'aiwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 248:
            return 'ccdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 247:
            return 'ciwcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 246:
            return 'clwcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 245:
            return 'flsrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 244:
            return 'fsrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 243:
            return 'faldiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 242:
            return 'alwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 241:
            return 'acfdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 240:
            return 'lsfdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 239:
            return 'csfdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 238:
            return 'tsndiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 237:
            return 'swl4diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 236:
            return 'stl4diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 235:
            return 'sktdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 234:
            return 'lsrhdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 233:
            return 'asqdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 232:
            return 'iediff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 231:
            return 'ishfdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 230:
            return 'inssdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 229:
            return 'iewsdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 228:
            return 'tpdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 227:
            return 'crnhdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 226:
            return 'htlcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 225:
            return 'htccdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 224:
            return 'vdhdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 223:
            return 'ctmwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 222:
            return 'ctzwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 221:
            return 'nsgddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 220:
            return 'ewgddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 219:
            return 'vdmwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 218:
            return 'vdzwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 217:
            return 'dhlcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 216:
            return 'dhccdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 215:
            return 'dhvddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 214:
            return 'dhrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 212:
            return 'tisrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 211:
            return 'strcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 210:
            return 'ssrcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 209:
            return 'ttrcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 208:
            return 'tsrcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 207:
            return '10sidiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 206:
            return 'tco3diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 205:
            return 'rodiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 204:
            return 'pawdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 203:
            return 'o3diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 202:
            return 'mn2tdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 201:
            return 'mx2tdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 200:
            return 'vsodiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 199:
            return 'vegdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 198:
            return 'srcdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 197:
            return 'gwddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 196:
            return 'mgwsdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 195:
            return 'lgwsdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 194:
            return 'btmpdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 193:
            return 'neovdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 192:
            return 'nwovdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 191:
            return 'nsovdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 190:
            return 'ewovdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 189:
            return 'sunddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 188:
            return 'hccdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 187:
            return 'mccdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 186:
            return 'lccdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 185:
            return 'cccdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 184:
            return 'swl3diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 183:
            return 'stl3diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 182:
            return 'ediff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 181:
            return 'nsssdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 180:
            return 'ewssdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 179:
            return 'ttrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 178:
            return 'tsrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 177:
            return 'strdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 176:
            return 'ssrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 175:
            return 'strddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 174:
            return 'aldiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 173:
            return 'srdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 172:
            return 'lsmdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 171:
            return 'swl2diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 170:
            return 'stl2diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 169:
            return 'ssrddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 167:
            return '2tdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 166:
            return '10vdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 165:
            return '10udiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 164:
            return 'tccdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 163:
            return 'slordiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 162:
            return 'anordiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 161:
            return 'isordiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 160:
            return 'sdordiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 159:
            return 'blhdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 158:
            return 'tspdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 157:
            return 'rdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 156:
            return 'ghdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 155:
            return 'ddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 154:
            return 'lwhrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 153:
            return 'swhrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 152:
            return 'lnspdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 151:
            return 'msldiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 150:
            return 'tnrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 149:
            return 'snrdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 148:
            return 'chnkdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 147:
            return 'slhfdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 146:
            return 'sshfdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 145:
            return 'blddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 144:
            return 'sfdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 143:
            return 'cpdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 142:
            return 'lspdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 141:
            return 'sddiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 140:
            return 'swl1diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 139:
            return 'stl1diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 138:
            return 'vodiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 137:
            return 'tcwvdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 136:
            return 'tcwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 135:
            return 'wdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 134:
            return 'spdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 133:
            return 'qdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 132:
            return 'vdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 131:
            return 'udiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 130:
            return 'tdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 129:
            return 'zdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 128:
            return 'bvdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 127:
            return 'atdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 125:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 123:
            return '10fg6diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 122:
            return 'mn2t6diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 121:
            return 'mx2t6diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 79:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 78:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 71:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 70:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 69:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 68:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 67:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 66:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 65:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 64:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 63:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 62:
            return 'obctdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 61:
            return 'tpodiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 60:
            return 'pvdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 59:
            return 'capediff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 58:
            return 'pardiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 57:
            return 'uvbdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 56:
            return 'mn2d24diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 55:
            return 'mean2t24diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 54:
            return 'presdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 53:
            return 'montdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 52:
            return 'mn2t24diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 51:
            return 'mx2t24diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 50:
            return 'lspfdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 49:
            return '10fgdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 48:
            return 'magssdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 47:
            return 'dsrpdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 46:
            return 'sdurdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 45:
            return 'smltdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 44:
            return 'esdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 43:
            return 'sltdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 42:
            return 'swvl4diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 41:
            return 'swvl3diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 40:
            return 'swvl2diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 39:
            return 'swvl1diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 38:
            return 'istl4diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 37:
            return 'istl3diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 36:
            return 'istl2diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 35:
            return 'istl1diff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 34:
            return 'sstdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 33:
            return 'rsndiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 32:
            return 'asndiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 31:
            return 'sicdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 30:
            return 'tvhdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 29:
            return 'tvldiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 28:
            return 'cvhdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 27:
            return 'cvldiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 26:
            return 'cldiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 23:
            return 'ucdvdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 22:
            return 'uclndiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 21:
            return 'uctpdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 14:
            return 'vrtwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 13:
            return 'urtwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 12:
            return 'vdvwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 11:
            return 'udvwdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 5:
            return 'septdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 4:
            return 'eqptdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 3:
            return 'ptdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 2:
            return 'vpotdiff'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 1:
            return 'strfdiff'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 254:
            return 'atmw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 253:
            return 'atze'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 252:
            return 'athe'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 251:
            return 'atte'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 250:
            return 'ice'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 249:
            return 'aiw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 245:
            return 'flsr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 244:
            return 'fsr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 243:
            return 'fal'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 242:
            return 'alw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 241:
            return 'acf'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 240:
            return 'lsf'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 239:
            return 'csf'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 238:
            return 'tsn'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 237:
            return 'swl4'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 236:
            return 'stl4'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 234:
            return 'lsrh'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 233:
            return 'asq'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 232:
            return 'ie'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 231:
            return 'ishf'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 230:
            return 'inss'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 229:
            return 'iews'

        unitsFactor = h.get_l('unitsFactor')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and unitsFactor == 1000:
            return 'tp'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 227:
            return 'crnh'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 226:
            return 'htlc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 225:
            return 'htcc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 224:
            return 'vdh'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 223:
            return 'ctmw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 222:
            return 'ctzw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 221:
            return 'nsgd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 220:
            return 'ewgd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 219:
            return 'vdmw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 218:
            return 'vdzw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 217:
            return 'dhlc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 216:
            return 'dhcc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 215:
            return 'dhvd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 214:
            return 'dhr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 213:
            return 'vimd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 212:
            return 'tisr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 209:
            return 'ttrc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 208:
            return 'tsrc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 206:
            return 'tco3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 205:
            return 'ro'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 204:
            return 'paw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 200:
            return 'vso'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 199:
            return 'veg'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 198:
            return 'src'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 197:
            return 'gwd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 196:
            return 'mgws'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 195:
            return 'lgws'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 193:
            return 'neov'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 192:
            return 'nwov'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 191:
            return 'nsov'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 190:
            return 'ewov'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 188:
            return 'hcc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 187:
            return 'mcc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 186:
            return 'lcc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 185:
            return 'ccc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 184:
            return 'swl3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 183:
            return 'stl3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 182:
            return 'e'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 178:
            return 'tsr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 174:
            return 'al'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 171:
            return 'swl2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 170:
            return 'stl2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 164:
            return 'tcc'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 163:
            return 'slor'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 162:
            return 'anor'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 161:
            return 'isor'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 160:
            return 'sdor'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 159:
            return 'blh'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 158:
            return 'tsp'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 154:
            return 'lwhr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 153:
            return 'swhr'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25 and typeOfFirstFixedSurface == 105:
            return 'lnsp'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 150:
            return 'tnr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 149:
            return 'snr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 148:
            return 'chnk'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 144:
            return 'sf'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10 and unitsFactor == 1000:
            return 'cp'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 142:
            return 'lsp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and unitsFactor == 1000:
            return 'sd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 140:
            return 'swl1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 139:
            return 'stl1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 137:
            return 'tcwv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 128:
            return 'bv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 127:
            return 'at'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 126:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 125:
            return 'vite'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 124:
            return 'emis'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 123:
            return '10fg6'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 120:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 119:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 118:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 117:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 116:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 115:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 114:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 113:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 112:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 111:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 110:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 109:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 108:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 107:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 106:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 105:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 104:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 103:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 102:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 101:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 100:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 99:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 98:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 97:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 96:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 95:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 94:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 93:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 92:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 91:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 90:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 89:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 88:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 87:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 86:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 85:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 84:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 83:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 82:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 81:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 80:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 79:
            return 'tciw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 78:
            return 'tclw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 74:
            return 'sdfor'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 73:
            return 'istrd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 72:
            return 'issrd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 71:
            return 'bc_hv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 70:
            return 'bc_lv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 69:
            return 'msr_hv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 68:
            return 'msr_lv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 67:
            return 'lai_hv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 66:
            return 'lai_lv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 65:
            return 'sktd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 64:
            return 'ftsktd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 63:
            return 'stsktd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 62:
            return 'obct'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 58:
            return 'par'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 57:
            return 'uvb'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 56:
            return 'mn2d24'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 55:
            return 'mean2t24'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 53:
            return 'mont'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and lengthOfTimeRange == 24 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 3 and indicatorOfUnitForTimeRange == 1 and scaledValueOfFirstFixedSurface == 2:
            return 'mn2t24'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 103 and lengthOfTimeRange == 24 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2:
            return 'mx2t24'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 50:
            return 'lspf'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 48:
            return 'magss'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 47:
            return 'dsrp'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 46:
            return 'sdur'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 45:
            return 'smlt'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 44:
            return 'es'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 42:
            return 'swvl4'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 41:
            return 'swvl3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 40:
            return 'swvl2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 39:
            return 'swvl1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 38:
            return 'istl4'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 37:
            return 'istl3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 36:
            return 'istl2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 35:
            return 'istl1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 32:
            return 'asn'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 30:
            return 'tvh'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 29:
            return 'tvl'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 28:
            return 'cvh'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 27:
            return 'cvl'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 26:
            return 'cl'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 25:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 24:
            return '~'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 23:
            return 'ucdv'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 22:
            return 'ucln'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 21:
            return 'uctp'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 20:
            return 'parcs'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 19:
            return 'uvcs'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 18:
            return 'alnid'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 17:
            return 'alnip'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 16:
            return 'aluvd'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 15:
            return 'aluvp'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 14:
            return 'vrtw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 13:
            return 'urtw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 12:
            return 'vdvw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 11:
            return 'udvw'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 9:
            return 'ssro'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 8:
            return 'sro'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 7:
            return 'scfr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 6:
            return 'ssfr'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 5:
            return 'sept'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 4:
            return 'eqpt'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 85:
            return 'tpg100'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 100 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1:
            return 'tpg100'

    return wrapped
