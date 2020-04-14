import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 1 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'tp'

        if table2Version == 1 and indicatorOfParameter == 71:
            return 'tcc'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'sf'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'st'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'sm'

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'orog'

        if table2Version == 1 and indicatorOfParameter == 87:
            return 'vegrea'

        if table2Version == 1 and indicatorOfParameter == 127:
            return 'p3127'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'p3126'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'p3125'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'p3124'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'p3120'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'p3119'

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'p3117'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'p3116'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'p3115'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'p3114'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'p3113'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'p3112'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'p3111'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 'p3110'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'p3109'

        if table2Version == 1 and indicatorOfParameter == 108:
            return 'p3108'

        if table2Version == 1 and indicatorOfParameter == 107:
            return 'p3107'

        if table2Version == 1 and indicatorOfParameter == 106:
            return 'p3106'

        if table2Version == 1 and indicatorOfParameter == 105:
            return 'p3105'

        if table2Version == 1 and indicatorOfParameter == 104:
            return 'p3104'

        if table2Version == 1 and indicatorOfParameter == 103:
            return 'p3103'

        if table2Version == 1 and indicatorOfParameter == 102:
            return 'p3102'

        if table2Version == 1 and indicatorOfParameter == 101:
            return 'p3101'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'p3100'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'p3099'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 'p3098'

        if table2Version == 1 and indicatorOfParameter == 97:
            return 'p3097'

        if table2Version == 1 and indicatorOfParameter == 96:
            return 'p3096'

        if table2Version == 1 and indicatorOfParameter == 95:
            return 'p3095'

        if table2Version == 1 and indicatorOfParameter == 94:
            return 'p3094'

        if table2Version == 1 and indicatorOfParameter == 93:
            return 'p3093'

        if table2Version == 1 and indicatorOfParameter == 92:
            return 'p3092'

        if table2Version == 1 and indicatorOfParameter == 91:
            return 'p3091'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'p3089'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 'p3088'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'p3086'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'p3082'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'p3080'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'p3077'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'p3070'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'p3069'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'p3068'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'p3067'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'p3064'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'p3063'

        if table2Version == 1 and indicatorOfParameter == 60:
            return 'p3060'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'p3059'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'p3056'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'p3055'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'p3054'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'p3053'

        if table2Version == 1 and indicatorOfParameter == 50:
            return 'p3050'

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'p3049'

        if table2Version == 1 and indicatorOfParameter == 48:
            return 'p3048'

        if table2Version == 1 and indicatorOfParameter == 47:
            return 'p3047'

        if table2Version == 1 and indicatorOfParameter == 46:
            return 'p3046'

        if table2Version == 1 and indicatorOfParameter == 45:
            return 'p3045'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 'p3042'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 'p3041'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 'p3038'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'p3037'

        if table2Version == 1 and indicatorOfParameter == 31:
            return 'p3031'

        if table2Version == 1 and indicatorOfParameter == 30:
            return 'p3030'

        if table2Version == 1 and indicatorOfParameter == 29:
            return 'p3029'

        if table2Version == 1 and indicatorOfParameter == 28:
            return 'p3028'

        if table2Version == 1 and indicatorOfParameter == 27:
            return 'p3027'

        if table2Version == 1 and indicatorOfParameter == 26:
            return 'p3026'

        if table2Version == 1 and indicatorOfParameter == 25:
            return 'p3025'

        if table2Version == 1 and indicatorOfParameter == 24:
            return 'p3024'

        if table2Version == 1 and indicatorOfParameter == 23:
            return 'p3023'

        if table2Version == 1 and indicatorOfParameter == 22:
            return 'p3022'

        if table2Version == 1 and indicatorOfParameter == 21:
            return 'p3021'

        if table2Version == 1 and indicatorOfParameter == 20:
            return 'p3020'

        if table2Version == 1 and indicatorOfParameter == 19:
            return 'p3019'

        if table2Version == 1 and indicatorOfParameter == 18:
            return 'p3018'

        if table2Version == 1 and indicatorOfParameter == 17:
            return 'p3017'

        if table2Version == 1 and indicatorOfParameter == 16:
            return 'p3016'

        if table2Version == 1 and indicatorOfParameter == 15:
            return 'p3015'

        if table2Version == 1 and indicatorOfParameter == 14:
            return 'p3014'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'p3009'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'p3008'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'p3005'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'p3003'

        if table2Version == 1 and indicatorOfParameter == 84:
            return 'al'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'p260102'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'snoc'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'bld'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'shf'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'lhf'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'lssf'

        if table2Version == 1 and indicatorOfParameter == 75:
            return 'hcc'

        if table2Version == 1 and indicatorOfParameter == 74:
            return 'mcc'

        if table2Version == 1 and indicatorOfParameter == 73:
            return 'lcc'

        if table2Version == 1 and indicatorOfParameter == 72:
            return 'ccc'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'sd'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'p3062'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'tco3'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'ro'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'btmp'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'e'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'sr'

        if table2Version == 1 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 1 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'd2m'

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 't2m'

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'v10'

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'u10'

        if table2Version == 1 and indicatorOfParameter == 52:
            return 'r'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'gh'

        if table2Version == 1 and indicatorOfParameter == 44:
            return 'd'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'msl'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 'vo'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'w'

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'sp'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'q'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'z'

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mn2t6'

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mx2t6'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'pv'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'pres'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'ws'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'pt'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'vp'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'strf'

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'tp'

        if table2Version == 2 and indicatorOfParameter == 71:
            return 'tcc'

        if table2Version == 2 and indicatorOfParameter == 65:
            return 'sf'

        if table2Version == 2 and indicatorOfParameter == 85:
            return 'st'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'sm'

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'orog'

        if table2Version == 2 and indicatorOfParameter == 87:
            return 'vegrea'

        if table2Version == 2 and indicatorOfParameter == 127:
            return 'p3127'

        if table2Version == 2 and indicatorOfParameter == 126:
            return 'p3126'

        if table2Version == 2 and indicatorOfParameter == 125:
            return 'p3125'

        if table2Version == 2 and indicatorOfParameter == 124:
            return 'p3124'

        if table2Version == 2 and indicatorOfParameter == 120:
            return 'p3120'

        if table2Version == 2 and indicatorOfParameter == 119:
            return 'p3119'

        if table2Version == 2 and indicatorOfParameter == 117:
            return 'p3117'

        if table2Version == 2 and indicatorOfParameter == 116:
            return 'p3116'

        if table2Version == 2 and indicatorOfParameter == 115:
            return 'p3115'

        if table2Version == 2 and indicatorOfParameter == 114:
            return 'p3114'

        if table2Version == 2 and indicatorOfParameter == 113:
            return 'p3113'

        if table2Version == 2 and indicatorOfParameter == 112:
            return 'p3112'

        if table2Version == 2 and indicatorOfParameter == 111:
            return 'p3111'

        if table2Version == 2 and indicatorOfParameter == 110:
            return 'p3110'

        if table2Version == 2 and indicatorOfParameter == 109:
            return 'p3109'

        if table2Version == 2 and indicatorOfParameter == 108:
            return 'p3108'

        if table2Version == 2 and indicatorOfParameter == 107:
            return 'p3107'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 'p3106'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'p3105'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'p3104'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 'p3103'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'p3102'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'p3101'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'p3100'

        if table2Version == 2 and indicatorOfParameter == 99:
            return 'p3099'

        if table2Version == 2 and indicatorOfParameter == 98:
            return 'p3098'

        if table2Version == 2 and indicatorOfParameter == 97:
            return 'p3097'

        if table2Version == 2 and indicatorOfParameter == 96:
            return 'p3096'

        if table2Version == 2 and indicatorOfParameter == 95:
            return 'p3095'

        if table2Version == 2 and indicatorOfParameter == 94:
            return 'p3094'

        if table2Version == 2 and indicatorOfParameter == 93:
            return 'p3093'

        if table2Version == 2 and indicatorOfParameter == 92:
            return 'p3092'

        if table2Version == 2 and indicatorOfParameter == 91:
            return 'p3091'

        if table2Version == 2 and indicatorOfParameter == 89:
            return 'p3089'

        if table2Version == 2 and indicatorOfParameter == 88:
            return 'p3088'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'p3086'

        if table2Version == 2 and indicatorOfParameter == 82:
            return 'p3082'

        if table2Version == 2 and indicatorOfParameter == 80:
            return 'p3080'

        if table2Version == 2 and indicatorOfParameter == 77:
            return 'p3077'

        if table2Version == 2 and indicatorOfParameter == 70:
            return 'p3070'

        if table2Version == 2 and indicatorOfParameter == 69:
            return 'p3069'

        if table2Version == 2 and indicatorOfParameter == 68:
            return 'p3068'

        if table2Version == 2 and indicatorOfParameter == 67:
            return 'p3067'

        if table2Version == 2 and indicatorOfParameter == 64:
            return 'p3064'

        if table2Version == 2 and indicatorOfParameter == 63:
            return 'p3063'

        if table2Version == 2 and indicatorOfParameter == 60:
            return 'p3060'

        if table2Version == 2 and indicatorOfParameter == 59:
            return 'p3059'

        if table2Version == 2 and indicatorOfParameter == 56:
            return 'p3056'

        if table2Version == 2 and indicatorOfParameter == 55:
            return 'p3055'

        if table2Version == 2 and indicatorOfParameter == 54:
            return 'p3054'

        if table2Version == 2 and indicatorOfParameter == 53:
            return 'p3053'

        if table2Version == 2 and indicatorOfParameter == 50:
            return 'p3050'

        if table2Version == 2 and indicatorOfParameter == 49:
            return 'p3049'

        if table2Version == 2 and indicatorOfParameter == 48:
            return 'p3048'

        if table2Version == 2 and indicatorOfParameter == 47:
            return 'p3047'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 'p3046'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 'p3045'

        if table2Version == 2 and indicatorOfParameter == 42:
            return 'p3042'

        if table2Version == 2 and indicatorOfParameter == 41:
            return 'p3041'

        if table2Version == 2 and indicatorOfParameter == 38:
            return 'p3038'

        if table2Version == 2 and indicatorOfParameter == 37:
            return 'p3037'

        if table2Version == 2 and indicatorOfParameter == 31:
            return 'p3031'

        if table2Version == 2 and indicatorOfParameter == 30:
            return 'p3030'

        if table2Version == 2 and indicatorOfParameter == 29:
            return 'p3029'

        if table2Version == 2 and indicatorOfParameter == 28:
            return 'p3028'

        if table2Version == 2 and indicatorOfParameter == 27:
            return 'p3027'

        if table2Version == 2 and indicatorOfParameter == 26:
            return 'p3026'

        if table2Version == 2 and indicatorOfParameter == 25:
            return 'p3025'

        if table2Version == 2 and indicatorOfParameter == 24:
            return 'p3024'

        if table2Version == 2 and indicatorOfParameter == 23:
            return 'p3023'

        if table2Version == 2 and indicatorOfParameter == 22:
            return 'p3022'

        if table2Version == 2 and indicatorOfParameter == 21:
            return 'p3021'

        if table2Version == 2 and indicatorOfParameter == 20:
            return 'p3020'

        if table2Version == 2 and indicatorOfParameter == 19:
            return 'p3019'

        if table2Version == 2 and indicatorOfParameter == 18:
            return 'p3018'

        if table2Version == 2 and indicatorOfParameter == 17:
            return 'p3017'

        if table2Version == 2 and indicatorOfParameter == 16:
            return 'p3016'

        if table2Version == 2 and indicatorOfParameter == 15:
            return 'p3015'

        if table2Version == 2 and indicatorOfParameter == 14:
            return 'p3014'

        if table2Version == 2 and indicatorOfParameter == 9:
            return 'p3009'

        if table2Version == 2 and indicatorOfParameter == 8:
            return 'p3008'

        if table2Version == 2 and indicatorOfParameter == 5:
            return 'p3005'

        if table2Version == 2 and indicatorOfParameter == 3:
            return 'p3003'

        if table2Version == 2 and indicatorOfParameter == 84:
            return 'al'

        if table2Version == 2 and indicatorOfParameter == 76:
            return 'p260102'

        if table2Version == 2 and indicatorOfParameter == 78:
            return 'snoc'

        if table2Version == 2 and indicatorOfParameter == 123:
            return 'bld'

        if table2Version == 2 and indicatorOfParameter == 122:
            return 'shf'

        if table2Version == 2 and indicatorOfParameter == 121:
            return 'lhf'

        if table2Version == 2 and indicatorOfParameter == 79:
            return 'lssf'

        if table2Version == 2 and indicatorOfParameter == 75:
            return 'hcc'

        if table2Version == 2 and indicatorOfParameter == 74:
            return 'mcc'

        if table2Version == 2 and indicatorOfParameter == 73:
            return 'lcc'

        if table2Version == 2 and indicatorOfParameter == 72:
            return 'ccc'

        if table2Version == 2 and indicatorOfParameter == 66:
            return 'sd'

        if table2Version == 2 and indicatorOfParameter == 62:
            return 'p3062'

        if table2Version == 2 and indicatorOfParameter == 10:
            return 'tco3'

        if table2Version == 2 and indicatorOfParameter == 90:
            return 'ro'

        if table2Version == 2 and indicatorOfParameter == 118:
            return 'btmp'

        if table2Version == 2 and indicatorOfParameter == 57:
            return 'e'

        if table2Version == 2 and indicatorOfParameter == 83:
            return 'sr'

        if table2Version == 2 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'd2m'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 't2m'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'v10'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'u10'

        if table2Version == 2 and indicatorOfParameter == 52:
            return 'r'

        if table2Version == 2 and indicatorOfParameter == 7:
            return 'gh'

        if table2Version == 2 and indicatorOfParameter == 44:
            return 'd'

        if table2Version == 2 and indicatorOfParameter == 2:
            return 'msl'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 'vo'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'w'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'sp'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'q'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'z'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mn2t6'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mx2t6'

        if table2Version == 2 and indicatorOfParameter == 4:
            return 'pv'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'pres'

        if table2Version == 2 and indicatorOfParameter == 32:
            return 'ws'

        if table2Version == 2 and indicatorOfParameter == 13:
            return 'pt'

        if table2Version == 2 and indicatorOfParameter == 36:
            return 'vp'

        if table2Version == 2 and indicatorOfParameter == 35:
            return 'strf'

        if table2Version == 3 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'tp'

        if table2Version == 3 and indicatorOfParameter == 71:
            return 'tcc'

        if table2Version == 3 and indicatorOfParameter == 65:
            return 'sf'

        if table2Version == 3 and indicatorOfParameter == 85:
            return 'st'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'sm'

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'orog'

        if table2Version == 3 and indicatorOfParameter == 87:
            return 'vegrea'

        if table2Version == 3 and indicatorOfParameter == 127:
            return 'p3127'

        if table2Version == 3 and indicatorOfParameter == 126:
            return 'p3126'

        if table2Version == 3 and indicatorOfParameter == 125:
            return 'p3125'

        if table2Version == 3 and indicatorOfParameter == 124:
            return 'p3124'

        if table2Version == 3 and indicatorOfParameter == 120:
            return 'p3120'

        if table2Version == 3 and indicatorOfParameter == 119:
            return 'p3119'

        if table2Version == 3 and indicatorOfParameter == 117:
            return 'p3117'

        if table2Version == 3 and indicatorOfParameter == 116:
            return 'p3116'

        if table2Version == 3 and indicatorOfParameter == 115:
            return 'p3115'

        if table2Version == 3 and indicatorOfParameter == 114:
            return 'p3114'

        if table2Version == 3 and indicatorOfParameter == 113:
            return 'p3113'

        if table2Version == 3 and indicatorOfParameter == 112:
            return 'p3112'

        if table2Version == 3 and indicatorOfParameter == 111:
            return 'p3111'

        if table2Version == 3 and indicatorOfParameter == 110:
            return 'p3110'

        if table2Version == 3 and indicatorOfParameter == 109:
            return 'p3109'

        if table2Version == 3 and indicatorOfParameter == 108:
            return 'p3108'

        if table2Version == 3 and indicatorOfParameter == 107:
            return 'p3107'

        if table2Version == 3 and indicatorOfParameter == 106:
            return 'p3106'

        if table2Version == 3 and indicatorOfParameter == 105:
            return 'p3105'

        if table2Version == 3 and indicatorOfParameter == 104:
            return 'p3104'

        if table2Version == 3 and indicatorOfParameter == 103:
            return 'p3103'

        if table2Version == 3 and indicatorOfParameter == 102:
            return 'p3102'

        if table2Version == 3 and indicatorOfParameter == 101:
            return 'p3101'

        if table2Version == 3 and indicatorOfParameter == 100:
            return 'p3100'

        if table2Version == 3 and indicatorOfParameter == 99:
            return 'p3099'

        if table2Version == 3 and indicatorOfParameter == 98:
            return 'p3098'

        if table2Version == 3 and indicatorOfParameter == 97:
            return 'p3097'

        if table2Version == 3 and indicatorOfParameter == 96:
            return 'p3096'

        if table2Version == 3 and indicatorOfParameter == 95:
            return 'p3095'

        if table2Version == 3 and indicatorOfParameter == 94:
            return 'p3094'

        if table2Version == 3 and indicatorOfParameter == 93:
            return 'p3093'

        if table2Version == 3 and indicatorOfParameter == 92:
            return 'p3092'

        if table2Version == 3 and indicatorOfParameter == 91:
            return 'p3091'

        if table2Version == 3 and indicatorOfParameter == 89:
            return 'p3089'

        if table2Version == 3 and indicatorOfParameter == 88:
            return 'p3088'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'p3086'

        if table2Version == 3 and indicatorOfParameter == 82:
            return 'p3082'

        if table2Version == 3 and indicatorOfParameter == 80:
            return 'p3080'

        if table2Version == 3 and indicatorOfParameter == 77:
            return 'p3077'

        if table2Version == 3 and indicatorOfParameter == 70:
            return 'p3070'

        if table2Version == 3 and indicatorOfParameter == 69:
            return 'p3069'

        if table2Version == 3 and indicatorOfParameter == 68:
            return 'p3068'

        if table2Version == 3 and indicatorOfParameter == 67:
            return 'p3067'

        if table2Version == 3 and indicatorOfParameter == 64:
            return 'p3064'

        if table2Version == 3 and indicatorOfParameter == 63:
            return 'p3063'

        if table2Version == 3 and indicatorOfParameter == 60:
            return 'p3060'

        if table2Version == 3 and indicatorOfParameter == 59:
            return 'p3059'

        if table2Version == 3 and indicatorOfParameter == 56:
            return 'p3056'

        if table2Version == 3 and indicatorOfParameter == 55:
            return 'p3055'

        if table2Version == 3 and indicatorOfParameter == 54:
            return 'p3054'

        if table2Version == 3 and indicatorOfParameter == 53:
            return 'p3053'

        if table2Version == 3 and indicatorOfParameter == 50:
            return 'p3050'

        if table2Version == 3 and indicatorOfParameter == 49:
            return 'p3049'

        if table2Version == 3 and indicatorOfParameter == 48:
            return 'p3048'

        if table2Version == 3 and indicatorOfParameter == 47:
            return 'p3047'

        if table2Version == 3 and indicatorOfParameter == 46:
            return 'p3046'

        if table2Version == 3 and indicatorOfParameter == 45:
            return 'p3045'

        if table2Version == 3 and indicatorOfParameter == 42:
            return 'p3042'

        if table2Version == 3 and indicatorOfParameter == 41:
            return 'p3041'

        if table2Version == 3 and indicatorOfParameter == 38:
            return 'p3038'

        if table2Version == 3 and indicatorOfParameter == 37:
            return 'p3037'

        if table2Version == 3 and indicatorOfParameter == 31:
            return 'p3031'

        if table2Version == 3 and indicatorOfParameter == 30:
            return 'p3030'

        if table2Version == 3 and indicatorOfParameter == 29:
            return 'p3029'

        if table2Version == 3 and indicatorOfParameter == 28:
            return 'p3028'

        if table2Version == 3 and indicatorOfParameter == 27:
            return 'p3027'

        if table2Version == 3 and indicatorOfParameter == 26:
            return 'p3026'

        if table2Version == 3 and indicatorOfParameter == 25:
            return 'p3025'

        if table2Version == 3 and indicatorOfParameter == 24:
            return 'p3024'

        if table2Version == 3 and indicatorOfParameter == 23:
            return 'p3023'

        if table2Version == 3 and indicatorOfParameter == 22:
            return 'p3022'

        if table2Version == 3 and indicatorOfParameter == 21:
            return 'p3021'

        if table2Version == 3 and indicatorOfParameter == 20:
            return 'p3020'

        if table2Version == 3 and indicatorOfParameter == 19:
            return 'p3019'

        if table2Version == 3 and indicatorOfParameter == 18:
            return 'p3018'

        if table2Version == 3 and indicatorOfParameter == 17:
            return 'p3017'

        if table2Version == 3 and indicatorOfParameter == 16:
            return 'p3016'

        if table2Version == 3 and indicatorOfParameter == 15:
            return 'p3015'

        if table2Version == 3 and indicatorOfParameter == 14:
            return 'p3014'

        if table2Version == 3 and indicatorOfParameter == 9:
            return 'p3009'

        if table2Version == 3 and indicatorOfParameter == 8:
            return 'p3008'

        if table2Version == 3 and indicatorOfParameter == 5:
            return 'p3005'

        if table2Version == 3 and indicatorOfParameter == 3:
            return 'p3003'

        if table2Version == 3 and indicatorOfParameter == 12:
            return 'p300012'

        if table2Version == 2 and indicatorOfParameter == 12:
            return 'p300012'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'p300012'

        if table2Version == 3 and indicatorOfParameter == 84:
            return 'al'

        if table2Version == 3 and indicatorOfParameter == 76:
            return 'p260102'

        if table2Version == 3 and indicatorOfParameter == 78:
            return 'snoc'

        if table2Version == 3 and indicatorOfParameter == 123:
            return 'bld'

        if table2Version == 3 and indicatorOfParameter == 122:
            return 'shf'

        if table2Version == 3 and indicatorOfParameter == 121:
            return 'lhf'

        if table2Version == 3 and indicatorOfParameter == 79:
            return 'lssf'

        if table2Version == 3 and indicatorOfParameter == 75:
            return 'hcc'

        if table2Version == 3 and indicatorOfParameter == 74:
            return 'mcc'

        if table2Version == 3 and indicatorOfParameter == 73:
            return 'lcc'

        if table2Version == 3 and indicatorOfParameter == 72:
            return 'ccc'

        if table2Version == 3 and indicatorOfParameter == 66:
            return 'sde'

        if table2Version == 3 and indicatorOfParameter == 62:
            return 'p3062'

        if table2Version == 3 and indicatorOfParameter == 10:
            return 'tco3'

        if table2Version == 3 and indicatorOfParameter == 90:
            return 'ro'

        if table2Version == 3 and indicatorOfParameter == 118:
            return 'btmp'

        if table2Version == 3 and indicatorOfParameter == 57:
            return 'e'

        if table2Version == 3 and indicatorOfParameter == 83:
            return 'sr'

        if table2Version == 3 and indicatorOfParameter == 81:
            return 'lsm'

        if table2Version == 3 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'd2m'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 't2m'

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'v10'

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'u10'

        if table2Version == 3 and indicatorOfParameter == 52:
            return 'r'

        if table2Version == 3 and indicatorOfParameter == 7:
            return 'gh'

        if table2Version == 3 and indicatorOfParameter == 44:
            return 'd'

        if table2Version == 3 and indicatorOfParameter == 2:
            return 'msl'

        if table2Version == 3 and indicatorOfParameter == 43:
            return 'vo'

        if table2Version == 3 and indicatorOfParameter == 39:
            return 'w'

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'sp'

        if table2Version == 3 and indicatorOfParameter == 51:
            return 'q'

        if table2Version == 3 and indicatorOfParameter == 34:
            return 'v'

        if table2Version == 3 and indicatorOfParameter == 33:
            return 'u'

        if table2Version == 3 and indicatorOfParameter == 11:
            return 't'

        if table2Version == 3 and indicatorOfParameter == 6:
            return 'z'

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mn2t6'

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'mx2t6'

        if table2Version == 3 and indicatorOfParameter == 4:
            return 'pv'

        if table2Version == 3 and indicatorOfParameter == 1:
            return 'pres'

        if table2Version == 3 and indicatorOfParameter == 32:
            return 'ws'

        if table2Version == 3 and indicatorOfParameter == 13:
            return 'pt'

        if table2Version == 3 and indicatorOfParameter == 36:
            return 'vp'

        if table2Version == 3 and indicatorOfParameter == 35:
            return 'strf'

    return wrapped
