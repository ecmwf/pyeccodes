import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 1 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 228228

        if table2Version == 1 and indicatorOfParameter == 71:
            return 228164

        if table2Version == 1 and indicatorOfParameter == 65:
            return 228144

        if table2Version == 1 and indicatorOfParameter == 85:
            return 228139

        if table2Version == 1 and indicatorOfParameter == 86:
            return 228039

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 228002

        if table2Version == 1 and indicatorOfParameter == 87:
            return 160199

        if table2Version == 1 and indicatorOfParameter == 127:
            return 3127

        if table2Version == 1 and indicatorOfParameter == 126:
            return 3126

        if table2Version == 1 and indicatorOfParameter == 125:
            return 3125

        if table2Version == 1 and indicatorOfParameter == 124:
            return 3124

        if table2Version == 1 and indicatorOfParameter == 120:
            return 3120

        if table2Version == 1 and indicatorOfParameter == 119:
            return 3119

        if table2Version == 1 and indicatorOfParameter == 117:
            return 3117

        if table2Version == 1 and indicatorOfParameter == 116:
            return 3116

        if table2Version == 1 and indicatorOfParameter == 115:
            return 3115

        if table2Version == 1 and indicatorOfParameter == 114:
            return 3114

        if table2Version == 1 and indicatorOfParameter == 113:
            return 3113

        if table2Version == 1 and indicatorOfParameter == 112:
            return 3112

        if table2Version == 1 and indicatorOfParameter == 111:
            return 3111

        if table2Version == 1 and indicatorOfParameter == 110:
            return 3110

        if table2Version == 1 and indicatorOfParameter == 109:
            return 3109

        if table2Version == 1 and indicatorOfParameter == 108:
            return 3108

        if table2Version == 1 and indicatorOfParameter == 107:
            return 3107

        if table2Version == 1 and indicatorOfParameter == 106:
            return 3106

        if table2Version == 1 and indicatorOfParameter == 105:
            return 3105

        if table2Version == 1 and indicatorOfParameter == 104:
            return 3104

        if table2Version == 1 and indicatorOfParameter == 103:
            return 3103

        if table2Version == 1 and indicatorOfParameter == 102:
            return 3102

        if table2Version == 1 and indicatorOfParameter == 101:
            return 3101

        if table2Version == 1 and indicatorOfParameter == 100:
            return 3100

        if table2Version == 1 and indicatorOfParameter == 99:
            return 3099

        if table2Version == 1 and indicatorOfParameter == 98:
            return 3098

        if table2Version == 1 and indicatorOfParameter == 97:
            return 3097

        if table2Version == 1 and indicatorOfParameter == 96:
            return 3096

        if table2Version == 1 and indicatorOfParameter == 95:
            return 3095

        if table2Version == 1 and indicatorOfParameter == 94:
            return 3094

        if table2Version == 1 and indicatorOfParameter == 93:
            return 3093

        if table2Version == 1 and indicatorOfParameter == 92:
            return 3092

        if table2Version == 1 and indicatorOfParameter == 91:
            return 3091

        if table2Version == 1 and indicatorOfParameter == 89:
            return 3089

        if table2Version == 1 and indicatorOfParameter == 88:
            return 3088

        if table2Version == 1 and indicatorOfParameter == 86:
            return 3086

        if table2Version == 1 and indicatorOfParameter == 82:
            return 3082

        if table2Version == 1 and indicatorOfParameter == 80:
            return 3080

        if table2Version == 1 and indicatorOfParameter == 77:
            return 3077

        if table2Version == 1 and indicatorOfParameter == 70:
            return 3070

        if table2Version == 1 and indicatorOfParameter == 69:
            return 3069

        if table2Version == 1 and indicatorOfParameter == 68:
            return 3068

        if table2Version == 1 and indicatorOfParameter == 67:
            return 3067

        if table2Version == 1 and indicatorOfParameter == 64:
            return 3064

        if table2Version == 1 and indicatorOfParameter == 63:
            return 3063

        if table2Version == 1 and indicatorOfParameter == 60:
            return 3060

        if table2Version == 1 and indicatorOfParameter == 59:
            return 3059

        if table2Version == 1 and indicatorOfParameter == 56:
            return 3056

        if table2Version == 1 and indicatorOfParameter == 55:
            return 3055

        if table2Version == 1 and indicatorOfParameter == 54:
            return 3054

        if table2Version == 1 and indicatorOfParameter == 53:
            return 3053

        if table2Version == 1 and indicatorOfParameter == 50:
            return 3050

        if table2Version == 1 and indicatorOfParameter == 49:
            return 3049

        if table2Version == 1 and indicatorOfParameter == 48:
            return 3048

        if table2Version == 1 and indicatorOfParameter == 47:
            return 3047

        if table2Version == 1 and indicatorOfParameter == 46:
            return 3046

        if table2Version == 1 and indicatorOfParameter == 45:
            return 3045

        if table2Version == 1 and indicatorOfParameter == 42:
            return 3042

        if table2Version == 1 and indicatorOfParameter == 41:
            return 3041

        if table2Version == 1 and indicatorOfParameter == 38:
            return 3038

        if table2Version == 1 and indicatorOfParameter == 37:
            return 3037

        if table2Version == 1 and indicatorOfParameter == 31:
            return 3031

        if table2Version == 1 and indicatorOfParameter == 30:
            return 3030

        if table2Version == 1 and indicatorOfParameter == 29:
            return 3029

        if table2Version == 1 and indicatorOfParameter == 28:
            return 3028

        if table2Version == 1 and indicatorOfParameter == 27:
            return 3027

        if table2Version == 1 and indicatorOfParameter == 26:
            return 3026

        if table2Version == 1 and indicatorOfParameter == 25:
            return 3025

        if table2Version == 1 and indicatorOfParameter == 24:
            return 3024

        if table2Version == 1 and indicatorOfParameter == 23:
            return 3023

        if table2Version == 1 and indicatorOfParameter == 22:
            return 3022

        if table2Version == 1 and indicatorOfParameter == 21:
            return 3021

        if table2Version == 1 and indicatorOfParameter == 20:
            return 3020

        if table2Version == 1 and indicatorOfParameter == 19:
            return 3019

        if table2Version == 1 and indicatorOfParameter == 18:
            return 3018

        if table2Version == 1 and indicatorOfParameter == 17:
            return 3017

        if table2Version == 1 and indicatorOfParameter == 16:
            return 3016

        if table2Version == 1 and indicatorOfParameter == 15:
            return 3015

        if table2Version == 1 and indicatorOfParameter == 14:
            return 3014

        if table2Version == 1 and indicatorOfParameter == 9:
            return 3009

        if table2Version == 1 and indicatorOfParameter == 8:
            return 3008

        if table2Version == 1 and indicatorOfParameter == 5:
            return 3005

        if table2Version == 1 and indicatorOfParameter == 3:
            return 3003

        if table2Version == 1 and indicatorOfParameter == 84:
            return 260509

        if table2Version == 1 and indicatorOfParameter == 76:
            return 260102

        if table2Version == 1 and indicatorOfParameter == 78:
            return 260011

        if table2Version == 1 and indicatorOfParameter == 123:
            return 3123

        if table2Version == 1 and indicatorOfParameter == 122:
            return 3122

        if table2Version == 1 and indicatorOfParameter == 121:
            return 3121

        if table2Version == 1 and indicatorOfParameter == 79:
            return 3079

        if table2Version == 1 and indicatorOfParameter == 75:
            return 3075

        if table2Version == 1 and indicatorOfParameter == 74:
            return 3074

        if table2Version == 1 and indicatorOfParameter == 73:
            return 3073

        if table2Version == 1 and indicatorOfParameter == 72:
            return 3072

        if table2Version == 1 and indicatorOfParameter == 66:
            return 3066

        if table2Version == 1 and indicatorOfParameter == 62:
            return 3062

        if table2Version == 1 and indicatorOfParameter == 10:
            return 206

        if table2Version == 1 and indicatorOfParameter == 90:
            return 205

        if table2Version == 1 and indicatorOfParameter == 118:
            return 194

        if table2Version == 1 and indicatorOfParameter == 57:
            return 182

        if table2Version == 1 and indicatorOfParameter == 83:
            return 173

        if table2Version == 1 and indicatorOfParameter == 81:
            return 172

        if table2Version == 1 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 168

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 167

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 166

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 165

        if table2Version == 1 and indicatorOfParameter == 52:
            return 157

        if table2Version == 1 and indicatorOfParameter == 7:
            return 156

        if table2Version == 1 and indicatorOfParameter == 44:
            return 155

        if table2Version == 1 and indicatorOfParameter == 2:
            return 151

        if table2Version == 1 and indicatorOfParameter == 43:
            return 138

        if table2Version == 1 and indicatorOfParameter == 39:
            return 135

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 134

        if table2Version == 1 and indicatorOfParameter == 51:
            return 133

        if table2Version == 1 and indicatorOfParameter == 34:
            return 132

        if table2Version == 1 and indicatorOfParameter == 33:
            return 131

        if table2Version == 1 and indicatorOfParameter == 11:
            return 130

        if table2Version == 1 and indicatorOfParameter == 6:
            return 129

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 122

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 121

        if table2Version == 1 and indicatorOfParameter == 4:
            return 60

        if table2Version == 1 and indicatorOfParameter == 1:
            return 54

        if table2Version == 1 and indicatorOfParameter == 32:
            return 10

        if table2Version == 1 and indicatorOfParameter == 13:
            return 3

        if table2Version == 1 and indicatorOfParameter == 36:
            return 2

        if table2Version == 1 and indicatorOfParameter == 35:
            return 1

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 228228

        if table2Version == 2 and indicatorOfParameter == 71:
            return 228164

        if table2Version == 2 and indicatorOfParameter == 65:
            return 228144

        if table2Version == 2 and indicatorOfParameter == 85:
            return 228139

        if table2Version == 2 and indicatorOfParameter == 86:
            return 228039

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 228002

        if table2Version == 2 and indicatorOfParameter == 87:
            return 160199

        if table2Version == 2 and indicatorOfParameter == 127:
            return 3127

        if table2Version == 2 and indicatorOfParameter == 126:
            return 3126

        if table2Version == 2 and indicatorOfParameter == 125:
            return 3125

        if table2Version == 2 and indicatorOfParameter == 124:
            return 3124

        if table2Version == 2 and indicatorOfParameter == 120:
            return 3120

        if table2Version == 2 and indicatorOfParameter == 119:
            return 3119

        if table2Version == 2 and indicatorOfParameter == 117:
            return 3117

        if table2Version == 2 and indicatorOfParameter == 116:
            return 3116

        if table2Version == 2 and indicatorOfParameter == 115:
            return 3115

        if table2Version == 2 and indicatorOfParameter == 114:
            return 3114

        if table2Version == 2 and indicatorOfParameter == 113:
            return 3113

        if table2Version == 2 and indicatorOfParameter == 112:
            return 3112

        if table2Version == 2 and indicatorOfParameter == 111:
            return 3111

        if table2Version == 2 and indicatorOfParameter == 110:
            return 3110

        if table2Version == 2 and indicatorOfParameter == 109:
            return 3109

        if table2Version == 2 and indicatorOfParameter == 108:
            return 3108

        if table2Version == 2 and indicatorOfParameter == 107:
            return 3107

        if table2Version == 2 and indicatorOfParameter == 106:
            return 3106

        if table2Version == 2 and indicatorOfParameter == 105:
            return 3105

        if table2Version == 2 and indicatorOfParameter == 104:
            return 3104

        if table2Version == 2 and indicatorOfParameter == 103:
            return 3103

        if table2Version == 2 and indicatorOfParameter == 102:
            return 3102

        if table2Version == 2 and indicatorOfParameter == 101:
            return 3101

        if table2Version == 2 and indicatorOfParameter == 100:
            return 3100

        if table2Version == 2 and indicatorOfParameter == 99:
            return 3099

        if table2Version == 2 and indicatorOfParameter == 98:
            return 3098

        if table2Version == 2 and indicatorOfParameter == 97:
            return 3097

        if table2Version == 2 and indicatorOfParameter == 96:
            return 3096

        if table2Version == 2 and indicatorOfParameter == 95:
            return 3095

        if table2Version == 2 and indicatorOfParameter == 94:
            return 3094

        if table2Version == 2 and indicatorOfParameter == 93:
            return 3093

        if table2Version == 2 and indicatorOfParameter == 92:
            return 3092

        if table2Version == 2 and indicatorOfParameter == 91:
            return 3091

        if table2Version == 2 and indicatorOfParameter == 89:
            return 3089

        if table2Version == 2 and indicatorOfParameter == 88:
            return 3088

        if table2Version == 2 and indicatorOfParameter == 86:
            return 3086

        if table2Version == 2 and indicatorOfParameter == 82:
            return 3082

        if table2Version == 2 and indicatorOfParameter == 80:
            return 3080

        if table2Version == 2 and indicatorOfParameter == 77:
            return 3077

        if table2Version == 2 and indicatorOfParameter == 70:
            return 3070

        if table2Version == 2 and indicatorOfParameter == 69:
            return 3069

        if table2Version == 2 and indicatorOfParameter == 68:
            return 3068

        if table2Version == 2 and indicatorOfParameter == 67:
            return 3067

        if table2Version == 2 and indicatorOfParameter == 64:
            return 3064

        if table2Version == 2 and indicatorOfParameter == 63:
            return 3063

        if table2Version == 2 and indicatorOfParameter == 60:
            return 3060

        if table2Version == 2 and indicatorOfParameter == 59:
            return 3059

        if table2Version == 2 and indicatorOfParameter == 56:
            return 3056

        if table2Version == 2 and indicatorOfParameter == 55:
            return 3055

        if table2Version == 2 and indicatorOfParameter == 54:
            return 3054

        if table2Version == 2 and indicatorOfParameter == 53:
            return 3053

        if table2Version == 2 and indicatorOfParameter == 50:
            return 3050

        if table2Version == 2 and indicatorOfParameter == 49:
            return 3049

        if table2Version == 2 and indicatorOfParameter == 48:
            return 3048

        if table2Version == 2 and indicatorOfParameter == 47:
            return 3047

        if table2Version == 2 and indicatorOfParameter == 46:
            return 3046

        if table2Version == 2 and indicatorOfParameter == 45:
            return 3045

        if table2Version == 2 and indicatorOfParameter == 42:
            return 3042

        if table2Version == 2 and indicatorOfParameter == 41:
            return 3041

        if table2Version == 2 and indicatorOfParameter == 38:
            return 3038

        if table2Version == 2 and indicatorOfParameter == 37:
            return 3037

        if table2Version == 2 and indicatorOfParameter == 31:
            return 3031

        if table2Version == 2 and indicatorOfParameter == 30:
            return 3030

        if table2Version == 2 and indicatorOfParameter == 29:
            return 3029

        if table2Version == 2 and indicatorOfParameter == 28:
            return 3028

        if table2Version == 2 and indicatorOfParameter == 27:
            return 3027

        if table2Version == 2 and indicatorOfParameter == 26:
            return 3026

        if table2Version == 2 and indicatorOfParameter == 25:
            return 3025

        if table2Version == 2 and indicatorOfParameter == 24:
            return 3024

        if table2Version == 2 and indicatorOfParameter == 23:
            return 3023

        if table2Version == 2 and indicatorOfParameter == 22:
            return 3022

        if table2Version == 2 and indicatorOfParameter == 21:
            return 3021

        if table2Version == 2 and indicatorOfParameter == 20:
            return 3020

        if table2Version == 2 and indicatorOfParameter == 19:
            return 3019

        if table2Version == 2 and indicatorOfParameter == 18:
            return 3018

        if table2Version == 2 and indicatorOfParameter == 17:
            return 3017

        if table2Version == 2 and indicatorOfParameter == 16:
            return 3016

        if table2Version == 2 and indicatorOfParameter == 15:
            return 3015

        if table2Version == 2 and indicatorOfParameter == 14:
            return 3014

        if table2Version == 2 and indicatorOfParameter == 9:
            return 3009

        if table2Version == 2 and indicatorOfParameter == 8:
            return 3008

        if table2Version == 2 and indicatorOfParameter == 5:
            return 3005

        if table2Version == 2 and indicatorOfParameter == 3:
            return 3003

        if table2Version == 2 and indicatorOfParameter == 84:
            return 260509

        if table2Version == 2 and indicatorOfParameter == 76:
            return 260102

        if table2Version == 2 and indicatorOfParameter == 78:
            return 260011

        if table2Version == 2 and indicatorOfParameter == 123:
            return 3123

        if table2Version == 2 and indicatorOfParameter == 122:
            return 3122

        if table2Version == 2 and indicatorOfParameter == 121:
            return 3121

        if table2Version == 2 and indicatorOfParameter == 79:
            return 3079

        if table2Version == 2 and indicatorOfParameter == 75:
            return 3075

        if table2Version == 2 and indicatorOfParameter == 74:
            return 3074

        if table2Version == 2 and indicatorOfParameter == 73:
            return 3073

        if table2Version == 2 and indicatorOfParameter == 72:
            return 3072

        if table2Version == 2 and indicatorOfParameter == 66:
            return 3066

        if table2Version == 2 and indicatorOfParameter == 62:
            return 3062

        if table2Version == 2 and indicatorOfParameter == 10:
            return 206

        if table2Version == 2 and indicatorOfParameter == 90:
            return 205

        if table2Version == 2 and indicatorOfParameter == 118:
            return 194

        if table2Version == 2 and indicatorOfParameter == 57:
            return 182

        if table2Version == 2 and indicatorOfParameter == 83:
            return 173

        if table2Version == 2 and indicatorOfParameter == 81:
            return 172

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 168

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 167

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 166

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 165

        if table2Version == 2 and indicatorOfParameter == 52:
            return 157

        if table2Version == 2 and indicatorOfParameter == 7:
            return 156

        if table2Version == 2 and indicatorOfParameter == 44:
            return 155

        if table2Version == 2 and indicatorOfParameter == 2:
            return 151

        if table2Version == 2 and indicatorOfParameter == 43:
            return 138

        if table2Version == 2 and indicatorOfParameter == 39:
            return 135

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 134

        if table2Version == 2 and indicatorOfParameter == 51:
            return 133

        if table2Version == 2 and indicatorOfParameter == 34:
            return 132

        if table2Version == 2 and indicatorOfParameter == 33:
            return 131

        if table2Version == 2 and indicatorOfParameter == 11:
            return 130

        if table2Version == 2 and indicatorOfParameter == 6:
            return 129

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 122

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 121

        if table2Version == 2 and indicatorOfParameter == 4:
            return 60

        if table2Version == 2 and indicatorOfParameter == 1:
            return 54

        if table2Version == 2 and indicatorOfParameter == 32:
            return 10

        if table2Version == 2 and indicatorOfParameter == 13:
            return 3

        if table2Version == 2 and indicatorOfParameter == 36:
            return 2

        if table2Version == 2 and indicatorOfParameter == 35:
            return 1

        if table2Version == 3 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 228228

        if table2Version == 3 and indicatorOfParameter == 71:
            return 228164

        if table2Version == 3 and indicatorOfParameter == 65:
            return 228144

        if table2Version == 3 and indicatorOfParameter == 85:
            return 228139

        if table2Version == 3 and indicatorOfParameter == 86:
            return 228039

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 228002

        if table2Version == 3 and indicatorOfParameter == 87:
            return 160199

        if table2Version == 3 and indicatorOfParameter == 127:
            return 3127

        if table2Version == 3 and indicatorOfParameter == 126:
            return 3126

        if table2Version == 3 and indicatorOfParameter == 125:
            return 3125

        if table2Version == 3 and indicatorOfParameter == 124:
            return 3124

        if table2Version == 3 and indicatorOfParameter == 120:
            return 3120

        if table2Version == 3 and indicatorOfParameter == 119:
            return 3119

        if table2Version == 3 and indicatorOfParameter == 117:
            return 3117

        if table2Version == 3 and indicatorOfParameter == 116:
            return 3116

        if table2Version == 3 and indicatorOfParameter == 115:
            return 3115

        if table2Version == 3 and indicatorOfParameter == 114:
            return 3114

        if table2Version == 3 and indicatorOfParameter == 113:
            return 3113

        if table2Version == 3 and indicatorOfParameter == 112:
            return 3112

        if table2Version == 3 and indicatorOfParameter == 111:
            return 3111

        if table2Version == 3 and indicatorOfParameter == 110:
            return 3110

        if table2Version == 3 and indicatorOfParameter == 109:
            return 3109

        if table2Version == 3 and indicatorOfParameter == 108:
            return 3108

        if table2Version == 3 and indicatorOfParameter == 107:
            return 3107

        if table2Version == 3 and indicatorOfParameter == 106:
            return 3106

        if table2Version == 3 and indicatorOfParameter == 105:
            return 3105

        if table2Version == 3 and indicatorOfParameter == 104:
            return 3104

        if table2Version == 3 and indicatorOfParameter == 103:
            return 3103

        if table2Version == 3 and indicatorOfParameter == 102:
            return 3102

        if table2Version == 3 and indicatorOfParameter == 101:
            return 3101

        if table2Version == 3 and indicatorOfParameter == 100:
            return 3100

        if table2Version == 3 and indicatorOfParameter == 99:
            return 3099

        if table2Version == 3 and indicatorOfParameter == 98:
            return 3098

        if table2Version == 3 and indicatorOfParameter == 97:
            return 3097

        if table2Version == 3 and indicatorOfParameter == 96:
            return 3096

        if table2Version == 3 and indicatorOfParameter == 95:
            return 3095

        if table2Version == 3 and indicatorOfParameter == 94:
            return 3094

        if table2Version == 3 and indicatorOfParameter == 93:
            return 3093

        if table2Version == 3 and indicatorOfParameter == 92:
            return 3092

        if table2Version == 3 and indicatorOfParameter == 91:
            return 3091

        if table2Version == 3 and indicatorOfParameter == 89:
            return 3089

        if table2Version == 3 and indicatorOfParameter == 88:
            return 3088

        if table2Version == 3 and indicatorOfParameter == 86:
            return 3086

        if table2Version == 3 and indicatorOfParameter == 82:
            return 3082

        if table2Version == 3 and indicatorOfParameter == 80:
            return 3080

        if table2Version == 3 and indicatorOfParameter == 77:
            return 3077

        if table2Version == 3 and indicatorOfParameter == 70:
            return 3070

        if table2Version == 3 and indicatorOfParameter == 69:
            return 3069

        if table2Version == 3 and indicatorOfParameter == 68:
            return 3068

        if table2Version == 3 and indicatorOfParameter == 67:
            return 3067

        if table2Version == 3 and indicatorOfParameter == 64:
            return 3064

        if table2Version == 3 and indicatorOfParameter == 63:
            return 3063

        if table2Version == 3 and indicatorOfParameter == 60:
            return 3060

        if table2Version == 3 and indicatorOfParameter == 59:
            return 3059

        if table2Version == 3 and indicatorOfParameter == 56:
            return 3056

        if table2Version == 3 and indicatorOfParameter == 55:
            return 3055

        if table2Version == 3 and indicatorOfParameter == 54:
            return 3054

        if table2Version == 3 and indicatorOfParameter == 53:
            return 3053

        if table2Version == 3 and indicatorOfParameter == 50:
            return 3050

        if table2Version == 3 and indicatorOfParameter == 49:
            return 3049

        if table2Version == 3 and indicatorOfParameter == 48:
            return 3048

        if table2Version == 3 and indicatorOfParameter == 47:
            return 3047

        if table2Version == 3 and indicatorOfParameter == 46:
            return 3046

        if table2Version == 3 and indicatorOfParameter == 45:
            return 3045

        if table2Version == 3 and indicatorOfParameter == 42:
            return 3042

        if table2Version == 3 and indicatorOfParameter == 41:
            return 3041

        if table2Version == 3 and indicatorOfParameter == 38:
            return 3038

        if table2Version == 3 and indicatorOfParameter == 37:
            return 3037

        if table2Version == 3 and indicatorOfParameter == 31:
            return 3031

        if table2Version == 3 and indicatorOfParameter == 30:
            return 3030

        if table2Version == 3 and indicatorOfParameter == 29:
            return 3029

        if table2Version == 3 and indicatorOfParameter == 28:
            return 3028

        if table2Version == 3 and indicatorOfParameter == 27:
            return 3027

        if table2Version == 3 and indicatorOfParameter == 26:
            return 3026

        if table2Version == 3 and indicatorOfParameter == 25:
            return 3025

        if table2Version == 3 and indicatorOfParameter == 24:
            return 3024

        if table2Version == 3 and indicatorOfParameter == 23:
            return 3023

        if table2Version == 3 and indicatorOfParameter == 22:
            return 3022

        if table2Version == 3 and indicatorOfParameter == 21:
            return 3021

        if table2Version == 3 and indicatorOfParameter == 20:
            return 3020

        if table2Version == 3 and indicatorOfParameter == 19:
            return 3019

        if table2Version == 3 and indicatorOfParameter == 18:
            return 3018

        if table2Version == 3 and indicatorOfParameter == 17:
            return 3017

        if table2Version == 3 and indicatorOfParameter == 16:
            return 3016

        if table2Version == 3 and indicatorOfParameter == 15:
            return 3015

        if table2Version == 3 and indicatorOfParameter == 14:
            return 3014

        if table2Version == 3 and indicatorOfParameter == 9:
            return 3009

        if table2Version == 3 and indicatorOfParameter == 8:
            return 3008

        if table2Version == 3 and indicatorOfParameter == 5:
            return 3005

        if table2Version == 3 and indicatorOfParameter == 3:
            return 3003

        if table2Version == 3 and indicatorOfParameter == 12:
            return 300012

        if table2Version == 2 and indicatorOfParameter == 12:
            return 300012

        if table2Version == 1 and indicatorOfParameter == 12:
            return 300012

        if table2Version == 3 and indicatorOfParameter == 84:
            return 260509

        if table2Version == 3 and indicatorOfParameter == 76:
            return 260102

        if table2Version == 3 and indicatorOfParameter == 78:
            return 260011

        if table2Version == 3 and indicatorOfParameter == 123:
            return 3123

        if table2Version == 3 and indicatorOfParameter == 122:
            return 3122

        if table2Version == 3 and indicatorOfParameter == 121:
            return 3121

        if table2Version == 3 and indicatorOfParameter == 79:
            return 3079

        if table2Version == 3 and indicatorOfParameter == 75:
            return 3075

        if table2Version == 3 and indicatorOfParameter == 74:
            return 3074

        if table2Version == 3 and indicatorOfParameter == 73:
            return 3073

        if table2Version == 3 and indicatorOfParameter == 72:
            return 3072

        if table2Version == 3 and indicatorOfParameter == 66:
            return 3066

        if table2Version == 3 and indicatorOfParameter == 62:
            return 3062

        if table2Version == 3 and indicatorOfParameter == 10:
            return 206

        if table2Version == 3 and indicatorOfParameter == 90:
            return 205

        if table2Version == 3 and indicatorOfParameter == 118:
            return 194

        if table2Version == 3 and indicatorOfParameter == 57:
            return 182

        if table2Version == 3 and indicatorOfParameter == 83:
            return 173

        if table2Version == 3 and indicatorOfParameter == 81:
            return 172

        if table2Version == 3 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 168

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 167

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 166

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 165

        if table2Version == 3 and indicatorOfParameter == 52:
            return 157

        if table2Version == 3 and indicatorOfParameter == 7:
            return 156

        if table2Version == 3 and indicatorOfParameter == 44:
            return 155

        if table2Version == 3 and indicatorOfParameter == 2:
            return 151

        if table2Version == 3 and indicatorOfParameter == 43:
            return 138

        if table2Version == 3 and indicatorOfParameter == 39:
            return 135

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 134

        if table2Version == 3 and indicatorOfParameter == 51:
            return 133

        if table2Version == 3 and indicatorOfParameter == 34:
            return 132

        if table2Version == 3 and indicatorOfParameter == 33:
            return 131

        if table2Version == 3 and indicatorOfParameter == 11:
            return 130

        if table2Version == 3 and indicatorOfParameter == 6:
            return 129

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 122

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 121

        if table2Version == 3 and indicatorOfParameter == 4:
            return 60

        if table2Version == 3 and indicatorOfParameter == 1:
            return 54

        if table2Version == 3 and indicatorOfParameter == 32:
            return 10

        if table2Version == 3 and indicatorOfParameter == 13:
            return 3

        if table2Version == 3 and indicatorOfParameter == 36:
            return 2

        if table2Version == 3 and indicatorOfParameter == 35:
            return 1

    return wrapped
