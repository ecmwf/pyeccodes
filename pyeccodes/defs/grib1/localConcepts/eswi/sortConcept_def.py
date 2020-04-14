import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        matchSort = h.get('matchSort')

        if matchSort == 0:
            return 'none'

        if matchSort == 1:
            return 'cm'

        if matchSort == 2:
            return 'lncm'

        if matchSort == 3:
            return 'c'

        if matchSort == 3:
            return 'cc'

        if matchSort == 4:
            return 'lnc'

        if matchSort == 7:
            return 'nr'

        if matchSort == 9:
            return 'cbq'

        if matchSort == 10:
            return 'lncbq'

        if matchSort == 11:
            return 'cmrefh'

        if matchSort == 12:
            return 'crefh'

        if matchSort == 13:
            return 'lncrefh'

        if matchSort == 14:
            return 'totcolumn'

        if matchSort == 14:
            return 'loncolumn'

        if matchSort == 14:
            return 'highcolumn'

        if matchSort == 14:
            return 'lowmax'

        if matchSort == 14:
            return 'highmax'

        if matchSort == 15:
            return 'lowmaxz'

        if matchSort == 15:
            return 'highmaxz'

        if matchSort == 21:
            return 'icm'

        if matchSort == 22:
            return 'lnicm'

        if matchSort == 23:
            return 'ic'

        if matchSort == 24:
            return 'lnic'

        if matchSort == 27:
            return 'inr'

        if matchSort == 29:
            return 'icbq'

        if matchSort == 30:
            return 'lnicbq'

        if matchSort == 51:
            return 'clw'

        if matchSort == 53:
            return 'ceqlw'

        if matchSort == 54:
            return 'cnrlw'

        if matchSort == 55:
            return 'cbqlwc'

        if matchSort == 61:
            return 'ciw'

        if matchSort == 63:
            return 'ceqiw'

        if matchSort == 64:
            return 'cnriw'

        if matchSort == 65:
            return 'cbqiw'

        if matchSort == 71:
            return 'cprec'

        if matchSort == 73:
            return 'ceqprec'

        if matchSort == 74:
            return 'cnprec'

        if matchSort == 75:
            return 'cbqprec'

        if matchSort == 81:
            return 'drydep'

        if matchSort == 82:
            return 'lndrydep'

        if matchSort == 84:
            return 'drydepnr'

        if matchSort == 85:
            return 'drydepbq'

        if matchSort == 91:
            return 'wetdep'

        if matchSort == 92:
            return 'lnwetdep'

        if matchSort == 94:
            return 'wetdepnr'

        if matchSort == 95:
            return 'wetdepbq'

        if matchSort == 101:
            return 'totdep'

        if matchSort == 102:
            return 'lntotdep'

        if matchSort == 104:
            return 'totdepnr'

        if matchSort == 105:
            return 'totdepbq'

        if matchSort == 110:
            return 'qton'

        if matchSort == 111:
            return 'qkg'

        if matchSort == 112:
            return 'qg'

        if matchSort == 114:
            return 'qnr'

        if matchSort == 115:
            return 'qbq'

        if matchSort == 121:
            return 'qkgs'

        if matchSort == 122:
            return 'qgs'

        if matchSort == 124:
            return 'qns'

        if matchSort == 125:
            return 'qbqs'

        if matchSort == 131:
            return 'aqkgs'

        if matchSort == 132:
            return 'aqgs'

        if matchSort == 134:
            return 'aqnrs'

        if matchSort == 135:
            return 'aqbqs'

        if matchSort == 136:
            return 'aq0kgs'

        if matchSort == 137:
            return 'aq0gs'

        if matchSort == 138:
            return 'aq0nrs'

        if matchSort == 139:
            return 'aq0bqs'

        if matchSort == 150:
            return 'inhdose'

        if matchSort == 151:
            return 'grddose'

        if matchSort == 152:
            return 'clddose'

        if matchSort == 153:
            return 'sumdose'

        if matchSort == 201:
            return 'vd'

        if matchSort == 202:
            return 'vs'

        if matchSort == 203:
            return 'lamda'

        if matchSort == 205:
            return 'tsum'

        if matchSort == 206:
            return 'hsum'

        if matchSort == 207:
            return 'hcrit'

        if matchSort == 208:
            return 'raccum'

        if matchSort == 209:
            return 'corr'

        if matchSort == 210:
            return 'aod'

        if matchSort == 240:
            return 'timearr'

        if matchSort == 241:
            return 'timelat'

        if matchSort == 242:
            return 'timemax'

        if matchSort == 243:
            return 'maxactiv'

        if matchSort == 244:
            return 'lnmaxactiv'

        if matchSort == 250:
            return 'freq'

        if matchSort == 251:
            return 'flux'

        if matchSort == 252:
            return 'fluxmol'

        if matchSort == 255:
            return 'missing'

    return wrapped
