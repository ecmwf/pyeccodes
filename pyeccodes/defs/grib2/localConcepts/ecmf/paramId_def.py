import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 254:
            return 228254

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 253:
            return 228253

        localTablesVersion = h.get_l('localTablesVersion')

        if localTablesVersion == 228 and discipline == 0 and parameterCategory == 254 and parameterNumber == 136:
            return 228136

        if localTablesVersion == 228 and discipline == 0 and parameterCategory == 254 and parameterNumber == 134:
            return 228134

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 101:
            return 211101

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 117:
            return 210117

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 116:
            return 210116

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 115:
            return 210115

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 114:
            return 210114

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 113:
            return 210113

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 112:
            return 210112

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 111:
            return 210111

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 110:
            return 210110

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 109:
            return 210109

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 108:
            return 210108

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 107:
            return 210107

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 106:
            return 210106

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 105:
            return 210105

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 104:
            return 210104

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 103:
            return 210103

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 102:
            return 210102

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 101:
            return 210101

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 216:
            return 140216

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 215:
            return 140215

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 228:
            return 234228

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 167:
            return 234167

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 151:
            return 234151

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 139:
            return 234139

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 132:
            return 228132

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 131:
            return 228131

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 19:
            return 228019

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 18:
            return 228018

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 17:
            return 228017

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 16:
            return 228016

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 15:
            return 228015

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 14:
            return 228014

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 13:
            return 228013

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 12:
            return 228012

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 11:
            return 228011

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 10:
            return 228010

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 9:
            return 228009

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 8:
            return 228008

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 7:
            return 228007

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 6:
            return 228006

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 5:
            return 228005

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 4:
            return 228004

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 3:
            return 228003

        if discipline == 192 and parameterCategory == 220 and parameterNumber == 228:
            return 220228

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 216:
            return 211216

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 215:
            return 211215

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 214:
            return 211214

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 213:
            return 211213

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 212:
            return 211212

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 211:
            return 211211

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 210:
            return 211210

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 209:
            return 211209

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 208:
            return 211208

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 207:
            return 211207

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 206:
            return 211206

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 203:
            return 211203

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 185:
            return 211185

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 184:
            return 211184

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 183:
            return 211183

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 182:
            return 211182

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 181:
            return 211181

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 166:
            return 211166

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 165:
            return 211165

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 164:
            return 211164

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 163:
            return 211163

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 162:
            return 211162

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 161:
            return 211161

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 160:
            return 211160

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 159:
            return 211159

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 158:
            return 211158

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 157:
            return 211157

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 156:
            return 211156

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 155:
            return 211155

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 154:
            return 211154

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 153:
            return 211153

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 152:
            return 211152

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 151:
            return 211151

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 150:
            return 211150

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 149:
            return 211149

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 148:
            return 211148

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 147:
            return 211147

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 146:
            return 211146

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 145:
            return 211145

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 144:
            return 211144

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 143:
            return 211143

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 142:
            return 211142

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 141:
            return 211141

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 140:
            return 211140

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 139:
            return 211139

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 138:
            return 211138

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 137:
            return 211137

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 136:
            return 211136

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 135:
            return 211135

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 134:
            return 211134

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 133:
            return 211133

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 132:
            return 211132

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 131:
            return 211131

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 130:
            return 211130

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 129:
            return 211129

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 128:
            return 211128

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 127:
            return 211127

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 126:
            return 211126

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 125:
            return 211125

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 124:
            return 211124

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 123:
            return 211123

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 122:
            return 211122

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 121:
            return 211121

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 100:
            return 211100

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 99:
            return 211099

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 98:
            return 211098

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 97:
            return 211097

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 96:
            return 211096

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 95:
            return 211095

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 94:
            return 211094

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 93:
            return 211093

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 92:
            return 211092

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 71:
            return 211071

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 70:
            return 211070

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 69:
            return 211069

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 68:
            return 211068

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 67:
            return 211067

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 66:
            return 211066

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 65:
            return 211065

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 64:
            return 211064

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 63:
            return 211063

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 62:
            return 211062

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 61:
            return 211061

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 54:
            return 211054

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 53:
            return 211053

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 52:
            return 211052

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 51:
            return 211051

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 50:
            return 211050

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 49:
            return 211049

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 48:
            return 211048

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 47:
            return 211047

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 46:
            return 211046

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 42:
            return 211042

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 41:
            return 211041

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 40:
            return 211040

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 39:
            return 211039

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 38:
            return 211038

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 37:
            return 211037

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 36:
            return 211036

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 35:
            return 211035

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 34:
            return 211034

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 33:
            return 211033

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 32:
            return 211032

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 31:
            return 211031

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 27:
            return 211027

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 26:
            return 211026

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 25:
            return 211025

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 24:
            return 211024

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 23:
            return 211023

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 22:
            return 211022

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 21:
            return 211021

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 20:
            return 211020

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 19:
            return 211019

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 18:
            return 211018

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 17:
            return 211017

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 16:
            return 211016

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 12:
            return 211012

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 11:
            return 211011

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 10:
            return 211010

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 9:
            return 211009

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 8:
            return 211008

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 7:
            return 211007

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 6:
            return 211006

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 5:
            return 211005

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 4:
            return 211004

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 3:
            return 211003

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 2:
            return 211002

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 1:
            return 211001

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 216:
            return 210216

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 215:
            return 210215

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 214:
            return 210214

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 213:
            return 210213

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 212:
            return 210212

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 211:
            return 210211

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 210:
            return 210210

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 209:
            return 210209

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 208:
            return 210208

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 207:
            return 210207

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 206:
            return 210206

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 203:
            return 210203

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 185:
            return 210185

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 184:
            return 210184

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 183:
            return 210183

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 182:
            return 210182

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 181:
            return 210181

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 166:
            return 210166

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 165:
            return 210165

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 164:
            return 210164

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 163:
            return 210163

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 162:
            return 210162

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 161:
            return 210161

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 160:
            return 210160

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 159:
            return 210159

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 158:
            return 210158

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 157:
            return 210157

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 156:
            return 210156

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 155:
            return 210155

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 154:
            return 210154

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 153:
            return 210153

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 152:
            return 210152

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 151:
            return 210151

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 150:
            return 210150

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 149:
            return 210149

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 148:
            return 210148

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 147:
            return 210147

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 146:
            return 210146

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 145:
            return 210145

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 144:
            return 210144

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 143:
            return 210143

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 142:
            return 210142

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 141:
            return 210141

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 140:
            return 210140

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 139:
            return 210139

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 138:
            return 210138

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 137:
            return 210137

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 136:
            return 210136

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 135:
            return 210135

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 134:
            return 210134

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 133:
            return 210133

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 132:
            return 210132

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 131:
            return 210131

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 130:
            return 210130

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 129:
            return 210129

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 128:
            return 210128

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 127:
            return 210127

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 126:
            return 210126

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 125:
            return 210125

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 124:
            return 210124

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 123:
            return 210123

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 122:
            return 210122

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 121:
            return 210121

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 100:
            return 210100

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 99:
            return 210099

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 98:
            return 210098

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 97:
            return 210097

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 96:
            return 210096

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 95:
            return 210095

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 94:
            return 210094

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 93:
            return 210093

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 92:
            return 210092

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 91:
            return 210091

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 90:
            return 210090

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 89:
            return 210089

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 88:
            return 210088

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 87:
            return 210087

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 86:
            return 210086

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 85:
            return 210085

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 84:
            return 210084

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 83:
            return 210083

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 82:
            return 210082

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 81:
            return 210081

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 80:
            return 210080

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 71:
            return 210071

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 70:
            return 210070

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 69:
            return 210069

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 68:
            return 210068

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 67:
            return 210067

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 66:
            return 210066

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 65:
            return 210065

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 64:
            return 210064

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 63:
            return 210063

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 62:
            return 210062

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 61:
            return 210061

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 54:
            return 210054

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 53:
            return 210053

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 52:
            return 210052

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 51:
            return 210051

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 50:
            return 210050

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 49:
            return 210049

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 48:
            return 210048

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 47:
            return 210047

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 46:
            return 210046

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 42:
            return 210042

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 41:
            return 210041

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 40:
            return 210040

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 39:
            return 210039

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 38:
            return 210038

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 37:
            return 210037

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 36:
            return 210036

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 35:
            return 210035

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 34:
            return 210034

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 33:
            return 210033

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 32:
            return 210032

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 31:
            return 210031

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 27:
            return 210027

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 26:
            return 210026

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 25:
            return 210025

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 24:
            return 210024

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 23:
            return 210023

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 22:
            return 210022

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 21:
            return 210021

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 20:
            return 210020

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 19:
            return 210019

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 18:
            return 210018

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 17:
            return 210017

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 16:
            return 210016

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 12:
            return 210012

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 11:
            return 210011

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 10:
            return 210010

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 9:
            return 210009

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 8:
            return 210008

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 7:
            return 210007

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 6:
            return 210006

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 5:
            return 210005

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 4:
            return 210004

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 3:
            return 210003

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 2:
            return 210002

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 1:
            return 210001

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 255:
            return 201255

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 241:
            return 201241

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 215:
            return 201215

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 203:
            return 201203

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 200:
            return 201200

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 187:
            return 201187

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 150:
            return 201150

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 139:
            return 201139

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 113:
            return 201113

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 112:
            return 201112

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 111:
            return 201111

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 102:
            return 201102

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 101:
            return 201101

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 100:
            return 201100

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 99:
            return 201099

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 85:
            return 201085

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 84:
            return 201084

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 83:
            return 201083

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 82:
            return 201082

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 81:
            return 201081

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 80:
            return 201080

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 79:
            return 201079

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 78:
            return 201078

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 77:
            return 201077

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 76:
            return 201076

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 75:
            return 201075

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 74:
            return 201074

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 73:
            return 201073

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 72:
            return 201072

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 71:
            return 201071

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 70:
            return 201070

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 69:
            return 201069

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 68:
            return 201068

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 67:
            return 201067

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 66:
            return 201066

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 65:
            return 201065

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 64:
            return 201064

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 63:
            return 201063

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 62:
            return 201062

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 61:
            return 201061

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 60:
            return 201060

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 56:
            return 201056

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 55:
            return 201055

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 54:
            return 201054

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 53:
            return 201053

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 52:
            return 201052

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 51:
            return 201051

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 50:
            return 201050

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 42:
            return 201042

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 41:
            return 201041

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 38:
            return 201038

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 37:
            return 201037

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 36:
            return 201036

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 35:
            return 201035

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 34:
            return 201034

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 33:
            return 201033

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 32:
            return 201032

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 31:
            return 201031

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 30:
            return 201030

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 29:
            return 201029

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 17:
            return 201017

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 16:
            return 201016

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 15:
            return 201015

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 14:
            return 201014

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 13:
            return 201013

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 12:
            return 201012

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 11:
            return 201011

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 10:
            return 201010

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 9:
            return 201009

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 8:
            return 201008

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 7:
            return 201007

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 6:
            return 201006

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 5:
            return 201005

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 4:
            return 201004

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 3:
            return 201003

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 2:
            return 201002

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 1:
            return 201001

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 168:
            return 200168

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 229:
            return 190229

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 173:
            return 190173

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 171:
            return 190171

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 170:
            return 190170

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 179:
            return 180179

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 178:
            return 180178

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 177:
            return 180177

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 176:
            return 180176

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 149:
            return 180149

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 255:
            return 175255

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 236:
            return 175236

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 202:
            return 175202

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 201:
            return 175201

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 183:
            return 175183

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 175:
            return 175175

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 170:
            return 175170

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 168:
            return 175168

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 167:
            return 175167

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 164:
            return 175164

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 139:
            return 175139

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 111:
            return 175111

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 110:
            return 175110

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 90:
            return 175090

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 89:
            return 175089

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 88:
            return 175088

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 87:
            return 175087

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 86:
            return 175086

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 85:
            return 175085

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 83:
            return 175083

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 55:
            return 175055

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 49:
            return 175049

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 42:
            return 175042

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 41:
            return 175041

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 40:
            return 175040

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 39:
            return 175039

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 34:
            return 175034

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 31:
            return 175031

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 6:
            return 175006

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 255:
            return 174255

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 236:
            return 174236

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 202:
            return 174202

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 201:
            return 174201

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 183:
            return 174183

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 175:
            return 174175

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 170:
            return 174170

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 168:
            return 174168

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 167:
            return 174167

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 164:
            return 174164

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 139:
            return 174139

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 111:
            return 174111

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 110:
            return 174110

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 99:
            return 174099

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 95:
            return 174095

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 94:
            return 174094

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 90:
            return 174090

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 89:
            return 174089

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 88:
            return 174088

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 87:
            return 174087

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 86:
            return 174086

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 85:
            return 174085

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 83:
            return 174083

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 55:
            return 174055

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 49:
            return 174049

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 42:
            return 174042

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 41:
            return 174041

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 40:
            return 174040

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 39:
            return 174039

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 34:
            return 174034

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 31:
            return 174031

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 9:
            return 174009

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 6:
            return 174006

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 255:
            return 173255

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 240:
            return 173240

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 239:
            return 173239

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 228:
            return 173228

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 212:
            return 173212

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 211:
            return 173211

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 210:
            return 173210

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 209:
            return 173209

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 208:
            return 173208

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 205:
            return 173205

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 197:
            return 173197

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 196:
            return 173196

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 195:
            return 173195

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 189:
            return 173189

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 182:
            return 173182

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 181:
            return 173181

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 180:
            return 173180

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 179:
            return 173179

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 178:
            return 173178

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 177:
            return 173177

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 176:
            return 173176

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 175:
            return 173175

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 169:
            return 173169

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 154:
            return 173154

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 153:
            return 173153

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 149:
            return 173149

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 147:
            return 173147

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 146:
            return 173146

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 145:
            return 173145

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 144:
            return 173144

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 143:
            return 173143

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 142:
            return 173142

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 50:
            return 173050

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 48:
            return 173048

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 45:
            return 173045

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 44:
            return 173044

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 255:
            return 172255

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 240:
            return 172240

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 239:
            return 172239

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 228:
            return 172228

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 212:
            return 172212

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 211:
            return 172211

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 210:
            return 172210

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 209:
            return 172209

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 208:
            return 172208

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 205:
            return 172205

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 197:
            return 172197

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 196:
            return 172196

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 195:
            return 172195

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 189:
            return 172189

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 182:
            return 172182

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 181:
            return 172181

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 180:
            return 172180

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 179:
            return 172179

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 178:
            return 172178

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 177:
            return 172177

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 176:
            return 172176

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 175:
            return 172175

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 169:
            return 172169

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 154:
            return 172154

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 153:
            return 172153

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 149:
            return 172149

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 147:
            return 172147

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 146:
            return 172146

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 145:
            return 172145

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 144:
            return 172144

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 143:
            return 172143

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 142:
            return 172142

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 50:
            return 172050

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 48:
            return 172048

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 45:
            return 172045

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 44:
            return 172044

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 255:
            return 171255

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 254:
            return 171254

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 253:
            return 171253

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 252:
            return 171252

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 251:
            return 171251

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 250:
            return 171250

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 249:
            return 171249

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 248:
            return 171248

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 247:
            return 171247

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 246:
            return 171246

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 245:
            return 171245

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 244:
            return 171244

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 243:
            return 171243

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 242:
            return 171242

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 241:
            return 171241

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 240:
            return 171240

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 239:
            return 171239

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 238:
            return 171238

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 237:
            return 171237

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 236:
            return 171236

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 235:
            return 171235

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 234:
            return 171234

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 233:
            return 171233

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 232:
            return 171232

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 231:
            return 171231

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 230:
            return 171230

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 229:
            return 171229

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 228:
            return 171228

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 227:
            return 171227

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 226:
            return 171226

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 225:
            return 171225

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 224:
            return 171224

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 223:
            return 171223

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 222:
            return 171222

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 221:
            return 171221

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 220:
            return 171220

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 219:
            return 171219

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 218:
            return 171218

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 217:
            return 171217

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 216:
            return 171216

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 215:
            return 171215

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 214:
            return 171214

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 212:
            return 171212

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 211:
            return 171211

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 210:
            return 171210

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 209:
            return 171209

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 208:
            return 171208

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 207:
            return 171207

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 206:
            return 171206

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 205:
            return 171205

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 204:
            return 171204

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 203:
            return 171203

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 202:
            return 171202

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 201:
            return 171201

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 200:
            return 171200

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 199:
            return 171199

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 198:
            return 171198

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 197:
            return 171197

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 196:
            return 171196

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 195:
            return 171195

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 194:
            return 171194

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 193:
            return 171193

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 192:
            return 171192

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 191:
            return 171191

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 190:
            return 171190

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 189:
            return 171189

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 188:
            return 171188

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 187:
            return 171187

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 186:
            return 171186

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 185:
            return 171185

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 184:
            return 171184

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 183:
            return 171183

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 182:
            return 171182

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 181:
            return 171181

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 180:
            return 171180

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 179:
            return 171179

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 178:
            return 171178

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 177:
            return 171177

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 176:
            return 171176

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 175:
            return 171175

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 174:
            return 171174

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 173:
            return 171173

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 171:
            return 171171

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 170:
            return 171170

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 169:
            return 171169

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 168:
            return 171168

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 167:
            return 171167

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 166:
            return 171166

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 165:
            return 171165

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 164:
            return 171164

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 163:
            return 171163

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 162:
            return 171162

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 161:
            return 171161

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 160:
            return 171160

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 159:
            return 171159

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 158:
            return 171158

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 157:
            return 171157

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 156:
            return 171156

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 155:
            return 171155

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 154:
            return 171154

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 153:
            return 171153

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 152:
            return 171152

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 151:
            return 171151

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 150:
            return 171150

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 149:
            return 171149

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 148:
            return 171148

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 147:
            return 171147

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 146:
            return 171146

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 145:
            return 171145

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 144:
            return 171144

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 143:
            return 171143

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 142:
            return 171142

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 141:
            return 171141

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 140:
            return 171140

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 139:
            return 171139

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 138:
            return 171138

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 137:
            return 171137

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 136:
            return 171136

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 135:
            return 171135

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 134:
            return 171134

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 133:
            return 171133

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 132:
            return 171132

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 131:
            return 171131

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 130:
            return 171130

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 129:
            return 171129

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 128:
            return 171128

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 127:
            return 171127

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 126:
            return 171126

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 125:
            return 171125

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 79:
            return 171079

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 78:
            return 171078

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 65:
            return 171065

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 64:
            return 171064

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 63:
            return 171063

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 62:
            return 171062

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 61:
            return 171061

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 60:
            return 171060

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 59:
            return 171059

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 58:
            return 171058

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 57:
            return 171057

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 56:
            return 171056

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 55:
            return 171055

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 54:
            return 171054

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 53:
            return 171053

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 52:
            return 171052

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 51:
            return 171051

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 50:
            return 171050

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 49:
            return 171049

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 48:
            return 171048

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 47:
            return 171047

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 46:
            return 171046

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 45:
            return 171045

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 44:
            return 171044

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 43:
            return 171043

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 42:
            return 171042

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 41:
            return 171041

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 40:
            return 171040

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 39:
            return 171039

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 38:
            return 171038

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 37:
            return 171037

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 36:
            return 171036

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 35:
            return 171035

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 34:
            return 171034

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 33:
            return 171033

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 32:
            return 171032

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 31:
            return 171031

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 30:
            return 171030

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 29:
            return 171029

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 28:
            return 171028

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 27:
            return 171027

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 26:
            return 171026

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 23:
            return 171023

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 22:
            return 171022

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 21:
            return 171021

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 14:
            return 171014

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 13:
            return 171013

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 12:
            return 171012

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 11:
            return 171011

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 5:
            return 171005

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 4:
            return 171004

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 3:
            return 171003

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 2:
            return 171002

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 1:
            return 171001

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 179:
            return 170179

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 171:
            return 170171

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 149:
            return 170149

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 255:
            return 162255

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 233:
            return 162233

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 232:
            return 162232

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 231:
            return 162231

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 230:
            return 162230

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 229:
            return 162229

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 227:
            return 162227

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 226:
            return 162226

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 225:
            return 162225

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 224:
            return 162224

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 223:
            return 162223

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 222:
            return 162222

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 221:
            return 162221

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 220:
            return 162220

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 219:
            return 162219

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 218:
            return 162218

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 217:
            return 162217

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 216:
            return 162216

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 215:
            return 162215

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 214:
            return 162214

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 213:
            return 162213

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 212:
            return 162212

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 211:
            return 162211

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 210:
            return 162210

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 209:
            return 162209

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 208:
            return 162208

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 207:
            return 162207

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 206:
            return 162206

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 113:
            return 162113

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 112:
            return 162112

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 111:
            return 162111

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 110:
            return 162110

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 109:
            return 162109

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 108:
            return 162108

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 107:
            return 162107

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 106:
            return 162106

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 105:
            return 162105

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 104:
            return 162104

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 103:
            return 162103

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 102:
            return 162102

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 101:
            return 162101

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 100:
            return 162100

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 87:
            return 162087

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 86:
            return 162086

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 85:
            return 162085

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 84:
            return 162084

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 83:
            return 162083

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 82:
            return 162082

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 81:
            return 162081

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 78:
            return 162078

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 77:
            return 162077

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 76:
            return 162076

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 75:
            return 162075

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 74:
            return 162074

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 73:
            return 162073

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 72:
            return 162072

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 71:
            return 162071

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 70:
            return 162070

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 69:
            return 162069

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 68:
            return 162068

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 67:
            return 162067

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 66:
            return 162066

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 65:
            return 162065

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 64:
            return 162064

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 63:
            return 162063

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 62:
            return 162062

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 61:
            return 162061

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 60:
            return 162060

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 59:
            return 162059

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 58:
            return 162058

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 57:
            return 162057

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 56:
            return 162056

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 55:
            return 162055

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 54:
            return 162054

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 53:
            return 162053

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 51:
            return 162051

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 254:
            return 160254

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 249:
            return 160249

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 247:
            return 160247

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 246:
            return 160246

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 243:
            return 160243

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 242:
            return 160242

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 241:
            return 160241

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 240:
            return 160240

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 239:
            return 160239

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 231:
            return 160231

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 226:
            return 160226

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 225:
            return 160225

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 224:
            return 160224

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 223:
            return 160223

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 222:
            return 160222

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 221:
            return 160221

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 220:
            return 160220

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 219:
            return 160219

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 218:
            return 160218

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 217:
            return 160217

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 216:
            return 160216

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 215:
            return 160215

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 214:
            return 160214

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 213:
            return 160213

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 212:
            return 160212

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 211:
            return 160211

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 210:
            return 160210

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 209:
            return 160209

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 208:
            return 160208

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 207:
            return 160207

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 206:
            return 160206

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 205:
            return 160205

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 202:
            return 160202

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 201:
            return 160201

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 199:
            return 160199

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 198:
            return 160198

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 184:
            return 160184

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 182:
            return 160182

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 181:
            return 160181

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 180:
            return 160180

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 171:
            return 160171

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 157:
            return 160157

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 156:
            return 160156

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 144:
            return 160144

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 143:
            return 160143

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 142:
            return 160142

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 140:
            return 160140

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 137:
            return 160137

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 135:
            return 160135

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 49:
            return 160049

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 255:
            return 151255

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 212:
            return 151212

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 211:
            return 151211

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 210:
            return 151210

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 209:
            return 151209

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 208:
            return 151208

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 207:
            return 151207

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 206:
            return 151206

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 205:
            return 151205

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 204:
            return 151204

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 203:
            return 151203

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 202:
            return 151202

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 201:
            return 151201

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 200:
            return 151200

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 199:
            return 151199

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 194:
            return 151194

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 192:
            return 151192

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 191:
            return 151191

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 190:
            return 151190

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 188:
            return 151188

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 187:
            return 151187

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 186:
            return 151186

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 185:
            return 151185

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 184:
            return 151184

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 183:
            return 151183

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 182:
            return 151182

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 181:
            return 151181

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 180:
            return 151180

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 179:
            return 151179

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 178:
            return 151178

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 177:
            return 151177

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 176:
            return 151176

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 174:
            return 151174

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 173:
            return 151173

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 172:
            return 151172

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 171:
            return 151171

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 170:
            return 151170

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 169:
            return 151169

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 168:
            return 151168

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 167:
            return 151167

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 166:
            return 151166

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 165:
            return 151165

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 164:
            return 151164

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 162:
            return 151162

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 161:
            return 151161

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 160:
            return 151160

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 159:
            return 151159

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 158:
            return 151158

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 157:
            return 151157

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 156:
            return 151156

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 155:
            return 151155

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 154:
            return 151154

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 153:
            return 151153

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 152:
            return 151152

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 151:
            return 151151

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 150:
            return 151150

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 149:
            return 151149

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 148:
            return 151148

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 147:
            return 151147

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 146:
            return 151146

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 144:
            return 151144

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 143:
            return 151143

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 142:
            return 151142

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 141:
            return 151141

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 140:
            return 151140

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 139:
            return 151139

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 138:
            return 151138

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 137:
            return 151137

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 136:
            return 151136

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 135:
            return 151135

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 134:
            return 151134

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 133:
            return 151133

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 130:
            return 151130

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 129:
            return 151129

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 128:
            return 151128

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 255:
            return 150255

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 183:
            return 150183

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 182:
            return 150182

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 181:
            return 150181

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 180:
            return 150180

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 173:
            return 150173

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 172:
            return 150172

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 171:
            return 150171

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 170:
            return 150170

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 169:
            return 150169

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 168:
            return 150168

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 155:
            return 150155

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 154:
            return 150154

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 153:
            return 150153

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 152:
            return 150152

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 148:
            return 150148

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 147:
            return 150147

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 146:
            return 150146

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 145:
            return 150145

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 144:
            return 150144

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 143:
            return 150143

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 142:
            return 150142

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 141:
            return 150141

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 140:
            return 150140

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 139:
            return 150139

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 137:
            return 150137

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 135:
            return 150135

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 134:
            return 150134

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 133:
            return 150133

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 131:
            return 150131

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 130:
            return 150130

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 129:
            return 150129

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 255:
            return 140255

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 254:
            return 140254

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 253:
            return 140253

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 252:
            return 140252

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 251:
            return 140251

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 250:
            return 140250

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 249:
            return 140249

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 248:
            return 140248

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 247:
            return 140247

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 246:
            return 140246

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 245:
            return 140245

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 244:
            return 140244

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 243:
            return 140243

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 242:
            return 140242

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 241:
            return 140241

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 240:
            return 140240

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 239:
            return 140239

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 238:
            return 140238

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 237:
            return 140237

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 140236

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 235:
            return 140235

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 140234

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 233:
            return 140233

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 231:
            return 140231

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 140231

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 228:
            return 140228

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 227:
            return 140227

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 226:
            return 140226

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 225:
            return 140225

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 224:
            return 140224

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 223:
            return 140223

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 222:
            return 140222

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 221:
            return 140221

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 140221

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 220:
            return 140220

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 219:
            return 140219

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 218:
            return 140218

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 217:
            return 140217

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 200:
            return 140200

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 92:
            return 133092

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 91:
            return 133091

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 90:
            return 133090

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 89:
            return 133089

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 88:
            return 133088

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 87:
            return 133087

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 86:
            return 133086

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 85:
            return 133085

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 84:
            return 133084

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 83:
            return 133083

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 82:
            return 133082

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 81:
            return 133081

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 80:
            return 133080

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 79:
            return 133079

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 78:
            return 133078

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 77:
            return 133077

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 76:
            return 133076

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 75:
            return 133075

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 74:
            return 133074

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 73:
            return 133073

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 72:
            return 133072

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 71:
            return 133071

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 70:
            return 133070

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 69:
            return 133069

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 68:
            return 133068

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 67:
            return 133067

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 66:
            return 133066

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 65:
            return 133065

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 64:
            return 133064

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 63:
            return 133063

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 62:
            return 133062

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 61:
            return 133061

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 60:
            return 133060

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 59:
            return 133059

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 58:
            return 133058

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 57:
            return 133057

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 56:
            return 133056

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 55:
            return 133055

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 54:
            return 133054

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 53:
            return 133053

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 52:
            return 133052

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 51:
            return 133051

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 50:
            return 133050

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 49:
            return 133049

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 48:
            return 133048

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 47:
            return 133047

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 46:
            return 133046

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 45:
            return 133045

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 44:
            return 133044

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 43:
            return 133043

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 42:
            return 133042

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 41:
            return 133041

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 40:
            return 133040

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 39:
            return 133039

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 38:
            return 133038

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 37:
            return 133037

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 36:
            return 133036

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 35:
            return 133035

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 34:
            return 133034

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 33:
            return 133033

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 32:
            return 133032

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 31:
            return 133031

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 30:
            return 133030

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 29:
            return 133029

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 28:
            return 133028

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 27:
            return 133027

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 26:
            return 133026

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 25:
            return 133025

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 24:
            return 133024

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 23:
            return 133023

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 22:
            return 133022

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 21:
            return 133021

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 20:
            return 133020

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 19:
            return 133019

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 18:
            return 133018

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 17:
            return 133017

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 16:
            return 133016

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 15:
            return 133015

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 14:
            return 133014

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 13:
            return 133013

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 12:
            return 133012

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 11:
            return 133011

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 10:
            return 133010

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 9:
            return 133009

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 8:
            return 133008

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 7:
            return 133007

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 6:
            return 133006

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 5:
            return 133005

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 4:
            return 133004

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 3:
            return 133003

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 2:
            return 133002

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 1:
            return 133001

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 255:
            return 131255

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 232:
            return 131232

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 229:
            return 131229

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 228:
            return 131228

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 202:
            return 131202

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 201:
            return 131201

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 167:
            return 131167

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 165:
            return 131165

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 164:
            return 131164

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 151:
            return 131151

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 144:
            return 131144

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 139:
            return 131139

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 130:
            return 131130

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 129:
            return 131129

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 81:
            return 131081

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 80:
            return 131080

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 79:
            return 131079

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 78:
            return 131078

        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        probabilityType = h.get_l('probabilityType')
        scaleFactorOfLowerLimit = h.get_l('scaleFactorOfLowerLimit')
        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')
        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and typeOfFirstFixedSurface == 101 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 8 and productDefinitionTemplateNumber == 5:
            return 131077

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaledValueOfLowerLimit == 6 and productDefinitionTemplateNumber == 5 and typeOfFirstFixedSurface == 101 and scaleFactorOfLowerLimit == 0 and probabilityType == 3:
            return 131076

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaledValueOfLowerLimit == 4 and productDefinitionTemplateNumber == 5 and typeOfFirstFixedSurface == 101 and scaleFactorOfLowerLimit == 0 and probabilityType == 3:
            return 131075

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and productDefinitionTemplateNumber == 5 and typeOfFirstFixedSurface == 101 and probabilityType == 3 and scaledValueOfLowerLimit == 2 and scaleFactorOfLowerLimit == 0:
            return 131074

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 73:
            return 131073

        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 2 and scaledValueOfLowerLimit == 25:
            return 131072

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 69:
            return 131069

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 68:
            return 131068

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 67:
            return 131067

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 66:
            return 131066

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 65:
            return 131065

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 64:
            return 131064

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 59:
            return 131059

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 49:
            return 131049

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 25:
            return 131025

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 24:
            return 131024

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 23:
            return 131023

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 22:
            return 131022

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 21:
            return 131021

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 20:
            return 131020

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 18:
            return 131018

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 17:
            return 131017

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 16:
            return 131016

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 15:
            return 131015

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 10:
            return 131010

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 9:
            return 131009

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 8:
            return 131008

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 7:
            return 131007

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 6:
            return 131006

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 5:
            return 131005

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 4:
            return 131004

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 3:
            return 131003

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 2:
            return 131002

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 1:
            return 131001

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 232:
            return 130232

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 231:
            return 130231

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 230:
            return 130230

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 229:
            return 130229

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 228:
            return 130228

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 226:
            return 130226

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 225:
            return 130225

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 224:
            return 130224

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 221:
            return 130221

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 220:
            return 130220

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 219:
            return 130219

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 218:
            return 130218

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 217:
            return 130217

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 216:
            return 130216

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 215:
            return 130215

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 214:
            return 130214

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 213:
            return 130213

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 212:
            return 130212

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 211:
            return 130211

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 210:
            return 130210

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 209:
            return 130209

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 208:
            return 130208

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 255:
            return 129255

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 254:
            return 129254

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 253:
            return 129253

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 252:
            return 129252

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 251:
            return 129251

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 250:
            return 129250

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 249:
            return 129249

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 248:
            return 129248

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 247:
            return 129247

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 246:
            return 129246

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 245:
            return 129245

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 244:
            return 129244

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 243:
            return 129243

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 242:
            return 129242

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 241:
            return 129241

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 240:
            return 129240

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 239:
            return 129239

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 238:
            return 129238

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 237:
            return 129237

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 236:
            return 129236

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 235:
            return 129235

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 234:
            return 129234

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 233:
            return 129233

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 232:
            return 129232

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 231:
            return 129231

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 230:
            return 129230

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 229:
            return 129229

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 228:
            return 129228

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 227:
            return 129227

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 226:
            return 129226

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 225:
            return 129225

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 224:
            return 129224

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 223:
            return 129223

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 222:
            return 129222

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 221:
            return 129221

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 220:
            return 129220

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 219:
            return 129219

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 218:
            return 129218

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 217:
            return 129217

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 216:
            return 129216

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 215:
            return 129215

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 214:
            return 129214

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 212:
            return 129212

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 211:
            return 129211

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 210:
            return 129210

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 209:
            return 129209

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 208:
            return 129208

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 207:
            return 129207

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 206:
            return 129206

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 205:
            return 129205

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 204:
            return 129204

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 203:
            return 129203

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 202:
            return 129202

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 201:
            return 129201

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 200:
            return 129200

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 199:
            return 129199

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 198:
            return 129198

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 197:
            return 129197

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 196:
            return 129196

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 195:
            return 129195

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 194:
            return 129194

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 193:
            return 129193

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 192:
            return 129192

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 191:
            return 129191

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 190:
            return 129190

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 189:
            return 129189

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 188:
            return 129188

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 187:
            return 129187

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 186:
            return 129186

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 185:
            return 129185

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 184:
            return 129184

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 183:
            return 129183

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 182:
            return 129182

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 181:
            return 129181

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 180:
            return 129180

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 179:
            return 129179

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 178:
            return 129178

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 177:
            return 129177

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 176:
            return 129176

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 175:
            return 129175

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 174:
            return 129174

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 173:
            return 129173

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 172:
            return 129172

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 171:
            return 129171

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 170:
            return 129170

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 169:
            return 129169

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 168:
            return 129168

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 167:
            return 129167

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 166:
            return 129166

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 165:
            return 129165

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 164:
            return 129164

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 163:
            return 129163

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 162:
            return 129162

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 161:
            return 129161

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 160:
            return 129160

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 159:
            return 129159

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 158:
            return 129158

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 157:
            return 129157

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 156:
            return 129156

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 155:
            return 129155

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 154:
            return 129154

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 153:
            return 129153

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 152:
            return 129152

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 151:
            return 129151

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 150:
            return 129150

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 149:
            return 129149

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 148:
            return 129148

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 147:
            return 129147

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 146:
            return 129146

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 145:
            return 129145

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 144:
            return 129144

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 143:
            return 129143

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 142:
            return 129142

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 141:
            return 129141

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 140:
            return 129140

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 139:
            return 129139

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 138:
            return 129138

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 137:
            return 129137

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 136:
            return 129136

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 135:
            return 129135

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 134:
            return 129134

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 133:
            return 129133

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 132:
            return 129132

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 131:
            return 129131

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 130:
            return 129130

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 129:
            return 129129

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 128:
            return 129128

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 127:
            return 129127

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 126:
            return 129126

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 125:
            return 129125

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 123:
            return 129123

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 122:
            return 129122

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 121:
            return 129121

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 120:
            return 129120

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 119:
            return 129119

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 118:
            return 129118

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 117:
            return 129117

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 116:
            return 129116

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 115:
            return 129115

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 114:
            return 129114

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 113:
            return 129113

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 112:
            return 129112

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 111:
            return 129111

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 110:
            return 129110

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 109:
            return 129109

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 108:
            return 129108

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 107:
            return 129107

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 106:
            return 129106

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 105:
            return 129105

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 104:
            return 129104

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 103:
            return 129103

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 102:
            return 129102

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 101:
            return 129101

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 100:
            return 129100

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 99:
            return 129099

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 98:
            return 129098

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 97:
            return 129097

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 96:
            return 129096

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 95:
            return 129095

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 94:
            return 129094

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 93:
            return 129093

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 92:
            return 129092

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 91:
            return 129091

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 90:
            return 129090

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 89:
            return 129089

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 88:
            return 129088

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 87:
            return 129087

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 86:
            return 129086

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 85:
            return 129085

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 84:
            return 129084

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 83:
            return 129083

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 82:
            return 129082

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 81:
            return 129081

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 80:
            return 129080

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 79:
            return 129079

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 78:
            return 129078

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 71:
            return 129071

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 70:
            return 129070

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 69:
            return 129069

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 68:
            return 129068

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 67:
            return 129067

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 66:
            return 129066

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 65:
            return 129065

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 64:
            return 129064

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 63:
            return 129063

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 62:
            return 129062

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 61:
            return 129061

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 60:
            return 129060

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 59:
            return 129059

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 58:
            return 129058

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 57:
            return 129057

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 56:
            return 129056

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 55:
            return 129055

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 54:
            return 129054

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 53:
            return 129053

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 52:
            return 129052

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 51:
            return 129051

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 50:
            return 129050

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 49:
            return 129049

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 48:
            return 129048

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 47:
            return 129047

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 46:
            return 129046

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 45:
            return 129045

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 44:
            return 129044

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 43:
            return 129043

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 42:
            return 129042

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 41:
            return 129041

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 40:
            return 129040

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 39:
            return 129039

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 38:
            return 129038

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 37:
            return 129037

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 36:
            return 129036

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 35:
            return 129035

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 34:
            return 129034

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 33:
            return 129033

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 32:
            return 129032

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 31:
            return 129031

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 30:
            return 129030

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 29:
            return 129029

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 28:
            return 129028

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 27:
            return 129027

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 26:
            return 129026

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 25:
            return 129025

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 24:
            return 129024

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 23:
            return 129023

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 22:
            return 129022

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 21:
            return 129021

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 14:
            return 129014

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 13:
            return 129013

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 12:
            return 129012

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 11:
            return 129011

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 5:
            return 129005

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 4:
            return 129004

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 3:
            return 129003

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 2:
            return 129002

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 1:
            return 129001

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 255:
            return 228255

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 252:
            return 228252

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 251:
            return 228251

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 250:
            return 228250

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 248:
            return 228248

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 130:
            return 228130

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 129:
            return 228129

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 103:
            return 228103

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 102:
            return 228102

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 101:
            return 228101

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 100:
            return 228100

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 94:
            return 228094

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 93:
            return 228093

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 92:
            return 228092

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 91:
            return 228091

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 90:
            return 228090

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 89:
            return 228089

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 228085

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 228084

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 228083

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 1:
            return 228082

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 1:
            return 228081

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 228080

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 228079

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 228078

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 60:
            return 228060

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        lengthOfTimeRange = h.get_l('lengthOfTimeRange')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1:
            return 228060

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 59:
            return 228059

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 3 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228059

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 58:
            return 228058

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 6 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfSecondFixedSurface == 8:
            return 228058

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 57:
            return 228057

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 3 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1:
            return 228057

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 53:
            return 228053

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 1:
            return 228053

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 52:
            return 228052

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228052

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 51:
            return 228051

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 1 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1:
            return 228051

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 50:
            return 228050

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228050

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 48:
            return 228048

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 47:
            return 228047

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 43:
            return 228043

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 42:
            return 228042

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 41:
            return 228041

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 40:
            return 228040

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 28:
            return 228028

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 3 and lengthOfTimeRange == 3 and typeOfFirstFixedSurface == 103 and indicatorOfUnitForTimeRange == 1 and scaleFactorOfFirstFixedSurface == 0:
            return 228027

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 2 and lengthOfTimeRange == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and indicatorOfUnitForTimeRange == 1:
            return 228026

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 25:
            return 228025

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 23:
            return 228023

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 22:
            return 228022

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 21:
            return 228021

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 206:
            return 221206

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 205:
            return 221205

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 204:
            return 221204

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 203:
            return 221203

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 202:
            return 221202

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 201:
            return 221201

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 200:
            return 221200

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 199:
            return 221199

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 198:
            return 221198

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 197:
            return 221197

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 196:
            return 221196

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 195:
            return 221195

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 194:
            return 221194

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 193:
            return 221193

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 192:
            return 221192

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 191:
            return 221191

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 190:
            return 221190

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 189:
            return 221189

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 188:
            return 221188

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 187:
            return 221187

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 186:
            return 221186

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 185:
            return 221185

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 184:
            return 221184

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 183:
            return 221183

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 182:
            return 221182

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 181:
            return 221181

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 180:
            return 221180

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 179:
            return 221179

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 178:
            return 221178

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 177:
            return 221177

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 176:
            return 221176

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 175:
            return 221175

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 174:
            return 221174

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 173:
            return 221173

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 172:
            return 221172

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 171:
            return 221171

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 170:
            return 221170

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 169:
            return 221169

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 168:
            return 221168

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 167:
            return 221167

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 166:
            return 221166

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 165:
            return 221165

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 164:
            return 221164

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 163:
            return 221163

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 162:
            return 221162

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 161:
            return 221161

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 160:
            return 221160

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 159:
            return 221159

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 158:
            return 221158

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 157:
            return 221157

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 156:
            return 221156

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 155:
            return 221155

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 154:
            return 221154

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 153:
            return 221153

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 152:
            return 221152

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 151:
            return 221151

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 150:
            return 221150

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 149:
            return 221149

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 148:
            return 221148

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 147:
            return 221147

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 146:
            return 221146

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 145:
            return 221145

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 144:
            return 221144

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 143:
            return 221143

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 142:
            return 221142

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 141:
            return 221141

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 140:
            return 221140

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 139:
            return 221139

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 138:
            return 221138

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 137:
            return 221137

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 136:
            return 221136

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 135:
            return 221135

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 134:
            return 221134

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 133:
            return 221133

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 132:
            return 221132

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 131:
            return 221131

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 130:
            return 221130

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 129:
            return 221129

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 128:
            return 221128

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 127:
            return 221127

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 126:
            return 221126

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 125:
            return 221125

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 124:
            return 221124

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 123:
            return 221123

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 122:
            return 221122

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 121:
            return 221121

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 120:
            return 221120

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 119:
            return 221119

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 118:
            return 221118

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 117:
            return 221117

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 116:
            return 221116

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 115:
            return 221115

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 114:
            return 221114

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 113:
            return 221113

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 112:
            return 221112

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 111:
            return 221111

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 110:
            return 221110

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 109:
            return 221109

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 108:
            return 221108

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 107:
            return 221107

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 106:
            return 221106

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 105:
            return 221105

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 104:
            return 221104

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 103:
            return 221103

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 102:
            return 221102

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 101:
            return 221101

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 100:
            return 221100

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 99:
            return 221099

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 98:
            return 221098

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 97:
            return 221097

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 96:
            return 221096

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 95:
            return 221095

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 94:
            return 221094

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 93:
            return 221093

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 92:
            return 221092

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 91:
            return 221091

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 90:
            return 221090

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 89:
            return 221089

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 88:
            return 221088

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 87:
            return 221087

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 86:
            return 221086

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 85:
            return 221085

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 84:
            return 221084

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 83:
            return 221083

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 82:
            return 221082

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 81:
            return 221081

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 80:
            return 221080

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 79:
            return 221079

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 78:
            return 221078

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 77:
            return 221077

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 76:
            return 221076

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 75:
            return 221075

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 74:
            return 221074

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 73:
            return 221073

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 72:
            return 221072

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 71:
            return 221071

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 70:
            return 221070

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 69:
            return 221069

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 68:
            return 221068

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 67:
            return 221067

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 66:
            return 221066

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 65:
            return 221065

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 64:
            return 221064

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 63:
            return 221063

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 62:
            return 221062

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 61:
            return 221061

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 60:
            return 221060

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 59:
            return 221059

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 58:
            return 221058

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 57:
            return 221057

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 56:
            return 221056

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 55:
            return 221055

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 54:
            return 221054

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 53:
            return 221053

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 52:
            return 221052

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 51:
            return 221051

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 50:
            return 221050

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 49:
            return 221049

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 48:
            return 221048

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 47:
            return 221047

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 46:
            return 221046

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 45:
            return 221045

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 44:
            return 221044

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 43:
            return 221043

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 42:
            return 221042

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 41:
            return 221041

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 40:
            return 221040

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 39:
            return 221039

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 38:
            return 221038

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 37:
            return 221037

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 36:
            return 221036

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 35:
            return 221035

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 34:
            return 221034

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 33:
            return 221033

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 32:
            return 221032

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 31:
            return 221031

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 30:
            return 221030

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 29:
            return 221029

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 28:
            return 221028

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 27:
            return 221027

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 26:
            return 221026

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 25:
            return 221025

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 24:
            return 221024

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 23:
            return 221023

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 22:
            return 221022

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 21:
            return 221021

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 20:
            return 221020

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 19:
            return 221019

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 18:
            return 221018

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 17:
            return 221017

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 16:
            return 221016

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 15:
            return 221015

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 14:
            return 221014

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 13:
            return 221013

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 12:
            return 221012

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 11:
            return 221011

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 10:
            return 221010

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 9:
            return 221009

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 8:
            return 221008

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 7:
            return 221007

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 6:
            return 221006

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 5:
            return 221005

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 4:
            return 221004

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 3:
            return 221003

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 2:
            return 221002

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 1:
            return 221001

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 220:
            return 219220

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 219:
            return 219219

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 218:
            return 219218

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 217:
            return 219217

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 216:
            return 219216

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 215:
            return 219215

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 214:
            return 219214

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 213:
            return 219213

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 212:
            return 219212

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 211:
            return 219211

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 210:
            return 219210

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 209:
            return 219209

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 208:
            return 219208

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 207:
            return 219207

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 206:
            return 219206

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 205:
            return 219205

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 204:
            return 219204

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 203:
            return 219203

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 202:
            return 219202

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 201:
            return 219201

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 200:
            return 219200

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 199:
            return 219199

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 198:
            return 219198

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 197:
            return 219197

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 196:
            return 219196

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 195:
            return 219195

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 194:
            return 219194

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 193:
            return 219193

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 192:
            return 219192

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 191:
            return 219191

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 190:
            return 219190

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 189:
            return 219189

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 188:
            return 219188

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 187:
            return 219187

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 186:
            return 219186

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 185:
            return 219185

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 184:
            return 219184

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 183:
            return 219183

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 182:
            return 219182

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 181:
            return 219181

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 180:
            return 219180

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 179:
            return 219179

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 178:
            return 219178

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 177:
            return 219177

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 176:
            return 219176

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 175:
            return 219175

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 174:
            return 219174

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 173:
            return 219173

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 172:
            return 219172

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 171:
            return 219171

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 170:
            return 219170

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 169:
            return 219169

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 168:
            return 219168

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 167:
            return 219167

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 166:
            return 219166

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 165:
            return 219165

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 164:
            return 219164

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 163:
            return 219163

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 162:
            return 219162

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 161:
            return 219161

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 160:
            return 219160

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 159:
            return 219159

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 158:
            return 219158

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 157:
            return 219157

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 156:
            return 219156

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 155:
            return 219155

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 154:
            return 219154

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 153:
            return 219153

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 152:
            return 219152

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 151:
            return 219151

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 150:
            return 219150

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 149:
            return 219149

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 148:
            return 219148

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 147:
            return 219147

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 146:
            return 219146

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 145:
            return 219145

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 144:
            return 219144

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 143:
            return 219143

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 142:
            return 219142

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 141:
            return 219141

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 140:
            return 219140

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 139:
            return 219139

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 138:
            return 219138

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 137:
            return 219137

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 136:
            return 219136

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 135:
            return 219135

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 134:
            return 219134

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 133:
            return 219133

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 132:
            return 219132

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 131:
            return 219131

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 130:
            return 219130

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 129:
            return 219129

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 128:
            return 219128

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 127:
            return 219127

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 126:
            return 219126

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 125:
            return 219125

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 124:
            return 219124

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 123:
            return 219123

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 122:
            return 219122

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 121:
            return 219121

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 120:
            return 219120

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 119:
            return 219119

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 118:
            return 219118

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 117:
            return 219117

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 116:
            return 219116

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 115:
            return 219115

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 114:
            return 219114

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 113:
            return 219113

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 112:
            return 219112

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 111:
            return 219111

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 110:
            return 219110

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 109:
            return 219109

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 108:
            return 219108

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 107:
            return 219107

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 106:
            return 219106

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 105:
            return 219105

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 104:
            return 219104

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 103:
            return 219103

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 102:
            return 219102

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 101:
            return 219101

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 100:
            return 219100

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 99:
            return 219099

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 98:
            return 219098

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 97:
            return 219097

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 96:
            return 219096

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 95:
            return 219095

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 94:
            return 219094

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 93:
            return 219093

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 92:
            return 219092

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 91:
            return 219091

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 90:
            return 219090

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 89:
            return 219089

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 88:
            return 219088

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 87:
            return 219087

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 86:
            return 219086

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 85:
            return 219085

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 84:
            return 219084

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 83:
            return 219083

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 82:
            return 219082

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 81:
            return 219081

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 80:
            return 219080

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 79:
            return 219079

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 78:
            return 219078

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 77:
            return 219077

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 76:
            return 219076

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 75:
            return 219075

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 74:
            return 219074

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 73:
            return 219073

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 72:
            return 219072

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 71:
            return 219071

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 70:
            return 219070

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 69:
            return 219069

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 68:
            return 219068

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 67:
            return 219067

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 66:
            return 219066

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 65:
            return 219065

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 64:
            return 219064

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 63:
            return 219063

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 62:
            return 219062

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 61:
            return 219061

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 60:
            return 219060

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 59:
            return 219059

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 58:
            return 219058

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 57:
            return 219057

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 56:
            return 219056

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 55:
            return 219055

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 54:
            return 219054

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 53:
            return 219053

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 52:
            return 219052

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 51:
            return 219051

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 50:
            return 219050

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 49:
            return 219049

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 48:
            return 219048

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 47:
            return 219047

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 46:
            return 219046

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 45:
            return 219045

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 44:
            return 219044

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 43:
            return 219043

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 42:
            return 219042

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 41:
            return 219041

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 40:
            return 219040

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 39:
            return 219039

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 38:
            return 219038

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 37:
            return 219037

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 36:
            return 219036

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 35:
            return 219035

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 34:
            return 219034

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 33:
            return 219033

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 32:
            return 219032

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 31:
            return 219031

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 30:
            return 219030

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 29:
            return 219029

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 28:
            return 219028

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 27:
            return 219027

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 26:
            return 219026

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 25:
            return 219025

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 24:
            return 219024

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 23:
            return 219023

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 22:
            return 219022

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 21:
            return 219021

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 20:
            return 219020

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 19:
            return 219019

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 18:
            return 219018

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 17:
            return 219017

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 16:
            return 219016

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 15:
            return 219015

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 14:
            return 219014

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 13:
            return 219013

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 12:
            return 219012

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 11:
            return 219011

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 10:
            return 219010

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 9:
            return 219009

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 8:
            return 219008

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 7:
            return 219007

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 6:
            return 219006

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 5:
            return 219005

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 4:
            return 219004

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 3:
            return 219003

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 2:
            return 219002

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 1:
            return 219001

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 206:
            return 218206

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 205:
            return 218205

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 204:
            return 218204

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 203:
            return 218203

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 202:
            return 218202

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 201:
            return 218201

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 200:
            return 218200

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 199:
            return 218199

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 198:
            return 218198

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 197:
            return 218197

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 196:
            return 218196

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 195:
            return 218195

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 194:
            return 218194

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 193:
            return 218193

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 192:
            return 218192

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 191:
            return 218191

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 190:
            return 218190

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 189:
            return 218189

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 188:
            return 218188

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 187:
            return 218187

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 186:
            return 218186

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 185:
            return 218185

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 184:
            return 218184

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 183:
            return 218183

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 182:
            return 218182

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 181:
            return 218181

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 180:
            return 218180

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 179:
            return 218179

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 178:
            return 218178

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 177:
            return 218177

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 176:
            return 218176

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 175:
            return 218175

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 174:
            return 218174

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 173:
            return 218173

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 172:
            return 218172

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 171:
            return 218171

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 170:
            return 218170

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 169:
            return 218169

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 168:
            return 218168

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 167:
            return 218167

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 166:
            return 218166

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 165:
            return 218165

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 164:
            return 218164

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 163:
            return 218163

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 162:
            return 218162

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 161:
            return 218161

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 160:
            return 218160

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 159:
            return 218159

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 158:
            return 218158

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 157:
            return 218157

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 156:
            return 218156

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 155:
            return 218155

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 154:
            return 218154

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 153:
            return 218153

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 152:
            return 218152

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 151:
            return 218151

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 150:
            return 218150

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 149:
            return 218149

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 148:
            return 218148

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 147:
            return 218147

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 146:
            return 218146

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 145:
            return 218145

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 144:
            return 218144

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 143:
            return 218143

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 142:
            return 218142

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 141:
            return 218141

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 140:
            return 218140

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 139:
            return 218139

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 138:
            return 218138

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 137:
            return 218137

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 136:
            return 218136

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 135:
            return 218135

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 134:
            return 218134

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 133:
            return 218133

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 132:
            return 218132

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 131:
            return 218131

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 130:
            return 218130

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 129:
            return 218129

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 128:
            return 218128

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 127:
            return 218127

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 126:
            return 218126

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 125:
            return 218125

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 124:
            return 218124

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 123:
            return 218123

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 122:
            return 218122

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 121:
            return 218121

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 120:
            return 218120

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 119:
            return 218119

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 118:
            return 218118

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 117:
            return 218117

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 116:
            return 218116

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 115:
            return 218115

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 114:
            return 218114

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 113:
            return 218113

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 112:
            return 218112

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 111:
            return 218111

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 110:
            return 218110

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 109:
            return 218109

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 108:
            return 218108

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 107:
            return 218107

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 106:
            return 218106

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 105:
            return 218105

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 104:
            return 218104

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 103:
            return 218103

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 102:
            return 218102

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 101:
            return 218101

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 100:
            return 218100

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 99:
            return 218099

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 98:
            return 218098

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 97:
            return 218097

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 96:
            return 218096

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 95:
            return 218095

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 94:
            return 218094

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 93:
            return 218093

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 92:
            return 218092

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 91:
            return 218091

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 90:
            return 218090

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 89:
            return 218089

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 88:
            return 218088

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 87:
            return 218087

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 86:
            return 218086

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 85:
            return 218085

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 84:
            return 218084

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 83:
            return 218083

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 82:
            return 218082

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 81:
            return 218081

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 80:
            return 218080

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 79:
            return 218079

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 78:
            return 218078

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 77:
            return 218077

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 76:
            return 218076

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 75:
            return 218075

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 74:
            return 218074

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 73:
            return 218073

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 72:
            return 218072

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 71:
            return 218071

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 70:
            return 218070

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 69:
            return 218069

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 68:
            return 218068

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 67:
            return 218067

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 66:
            return 218066

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 65:
            return 218065

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 64:
            return 218064

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 63:
            return 218063

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 62:
            return 218062

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 61:
            return 218061

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 60:
            return 218060

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 59:
            return 218059

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 58:
            return 218058

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 57:
            return 218057

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 56:
            return 218056

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 55:
            return 218055

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 54:
            return 218054

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 53:
            return 218053

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 52:
            return 218052

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 51:
            return 218051

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 50:
            return 218050

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 49:
            return 218049

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 48:
            return 218048

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 47:
            return 218047

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 46:
            return 218046

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 45:
            return 218045

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 44:
            return 218044

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 43:
            return 218043

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 42:
            return 218042

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 41:
            return 218041

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 40:
            return 218040

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 39:
            return 218039

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 38:
            return 218038

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 37:
            return 218037

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 36:
            return 218036

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 35:
            return 218035

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 34:
            return 218034

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 33:
            return 218033

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 32:
            return 218032

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 30:
            return 218030

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 29:
            return 218029

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 28:
            return 218028

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 27:
            return 218027

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 26:
            return 218026

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 24:
            return 218024

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 23:
            return 218023

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 22:
            return 218022

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 21:
            return 218021

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 20:
            return 218020

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 19:
            return 218019

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 18:
            return 218018

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 16:
            return 218016

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 15:
            return 218015

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 14:
            return 218014

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 13:
            return 218013

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 12:
            return 218012

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 11:
            return 218011

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 10:
            return 218010

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 9:
            return 218009

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 7:
            return 218007

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 6:
            return 218006

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 4:
            return 218004

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 3:
            return 218003

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 206:
            return 217206

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 205:
            return 217205

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 204:
            return 217204

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 203:
            return 217203

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 202:
            return 217202

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 201:
            return 217201

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 200:
            return 217200

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 199:
            return 217199

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 198:
            return 217198

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 197:
            return 217197

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 196:
            return 217196

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 195:
            return 217195

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 194:
            return 217194

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 193:
            return 217193

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 192:
            return 217192

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 191:
            return 217191

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 190:
            return 217190

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 189:
            return 217189

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 188:
            return 217188

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 187:
            return 217187

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 186:
            return 217186

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 185:
            return 217185

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 184:
            return 217184

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 183:
            return 217183

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 182:
            return 217182

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 181:
            return 217181

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 180:
            return 217180

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 179:
            return 217179

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 178:
            return 217178

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 177:
            return 217177

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 176:
            return 217176

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 175:
            return 217175

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 174:
            return 217174

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 173:
            return 217173

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 172:
            return 217172

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 171:
            return 217171

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 170:
            return 217170

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 169:
            return 217169

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 168:
            return 217168

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 167:
            return 217167

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 166:
            return 217166

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 165:
            return 217165

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 164:
            return 217164

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 163:
            return 217163

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 162:
            return 217162

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 161:
            return 217161

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 160:
            return 217160

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 159:
            return 217159

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 158:
            return 217158

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 157:
            return 217157

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 156:
            return 217156

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 155:
            return 217155

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 154:
            return 217154

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 153:
            return 217153

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 152:
            return 217152

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 151:
            return 217151

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 150:
            return 217150

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 149:
            return 217149

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 148:
            return 217148

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 147:
            return 217147

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 146:
            return 217146

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 145:
            return 217145

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 144:
            return 217144

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 143:
            return 217143

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 142:
            return 217142

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 141:
            return 217141

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 140:
            return 217140

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 139:
            return 217139

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 138:
            return 217138

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 137:
            return 217137

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 136:
            return 217136

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 135:
            return 217135

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 134:
            return 217134

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 133:
            return 217133

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 132:
            return 217132

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 131:
            return 217131

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 130:
            return 217130

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 129:
            return 217129

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 128:
            return 217128

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 127:
            return 217127

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 126:
            return 217126

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 125:
            return 217125

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 124:
            return 217124

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 123:
            return 217123

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 122:
            return 217122

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 121:
            return 217121

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 120:
            return 217120

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 119:
            return 217119

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 118:
            return 217118

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 117:
            return 217117

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 116:
            return 217116

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 115:
            return 217115

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 114:
            return 217114

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 113:
            return 217113

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 112:
            return 217112

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 111:
            return 217111

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 110:
            return 217110

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 109:
            return 217109

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 108:
            return 217108

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 107:
            return 217107

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 106:
            return 217106

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 105:
            return 217105

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 104:
            return 217104

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 103:
            return 217103

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 102:
            return 217102

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 101:
            return 217101

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 100:
            return 217100

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 99:
            return 217099

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 98:
            return 217098

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 97:
            return 217097

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 96:
            return 217096

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 95:
            return 217095

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 94:
            return 217094

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 93:
            return 217093

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 92:
            return 217092

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 91:
            return 217091

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 90:
            return 217090

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 89:
            return 217089

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 88:
            return 217088

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 87:
            return 217087

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 86:
            return 217086

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 85:
            return 217085

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 84:
            return 217084

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 83:
            return 217083

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 82:
            return 217082

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 81:
            return 217081

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 80:
            return 217080

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 79:
            return 217079

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 78:
            return 217078

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 77:
            return 217077

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 76:
            return 217076

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 75:
            return 217075

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 74:
            return 217074

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 73:
            return 217073

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 72:
            return 217072

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 71:
            return 217071

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 70:
            return 217070

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 69:
            return 217069

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 68:
            return 217068

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 67:
            return 217067

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 66:
            return 217066

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 65:
            return 217065

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 64:
            return 217064

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 63:
            return 217063

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 62:
            return 217062

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 61:
            return 217061

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 60:
            return 217060

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 59:
            return 217059

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 58:
            return 217058

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 57:
            return 217057

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 56:
            return 217056

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 55:
            return 217055

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 54:
            return 217054

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 53:
            return 217053

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 52:
            return 217052

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 51:
            return 217051

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 50:
            return 217050

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 49:
            return 217049

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 48:
            return 217048

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 47:
            return 217047

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 46:
            return 217046

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 45:
            return 217045

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 44:
            return 217044

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 43:
            return 217043

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 42:
            return 217042

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 41:
            return 217041

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 40:
            return 217040

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 39:
            return 217039

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 38:
            return 217038

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 37:
            return 217037

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 36:
            return 217036

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 35:
            return 217035

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 34:
            return 217034

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 33:
            return 217033

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 32:
            return 217032

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 30:
            return 217030

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 29:
            return 217029

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 28:
            return 217028

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 27:
            return 217027

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 26:
            return 217026

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 24:
            return 217024

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 23:
            return 217023

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 22:
            return 217022

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 21:
            return 217021

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 20:
            return 217020

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 19:
            return 217019

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 18:
            return 217018

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 16:
            return 217016

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 15:
            return 217015

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 14:
            return 217014

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 13:
            return 217013

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 12:
            return 217012

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 11:
            return 217011

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 10:
            return 217010

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 9:
            return 217009

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 7:
            return 217007

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 6:
            return 217006

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 4:
            return 217004

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 3:
            return 217003

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 255:
            return 216255

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 254:
            return 216254

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 253:
            return 216253

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 252:
            return 216252

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 251:
            return 216251

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 250:
            return 216250

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 249:
            return 216249

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 248:
            return 216248

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 247:
            return 216247

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 246:
            return 216246

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 245:
            return 216245

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 244:
            return 216244

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 243:
            return 216243

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 242:
            return 216242

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 241:
            return 216241

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 240:
            return 216240

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 239:
            return 216239

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 238:
            return 216238

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 237:
            return 216237

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 236:
            return 216236

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 235:
            return 216235

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 234:
            return 216234

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 233:
            return 216233

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 232:
            return 216232

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 231:
            return 216231

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 230:
            return 216230

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 229:
            return 216229

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 228:
            return 216228

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 227:
            return 216227

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 226:
            return 216226

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 225:
            return 216225

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 224:
            return 216224

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 223:
            return 216223

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 222:
            return 216222

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 221:
            return 216221

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 220:
            return 216220

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 219:
            return 216219

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 218:
            return 216218

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 217:
            return 216217

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 216:
            return 216216

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 215:
            return 216215

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 214:
            return 216214

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 213:
            return 216213

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 212:
            return 216212

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 211:
            return 216211

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 210:
            return 216210

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 209:
            return 216209

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 208:
            return 216208

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 207:
            return 216207

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 206:
            return 216206

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 205:
            return 216205

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 204:
            return 216204

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 203:
            return 216203

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 202:
            return 216202

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 201:
            return 216201

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 200:
            return 216200

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 199:
            return 216199

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 198:
            return 216198

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 197:
            return 216197

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 196:
            return 216196

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 195:
            return 216195

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 194:
            return 216194

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 193:
            return 216193

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 192:
            return 216192

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 191:
            return 216191

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 190:
            return 216190

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 189:
            return 216189

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 188:
            return 216188

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 187:
            return 216187

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 186:
            return 216186

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 185:
            return 216185

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 184:
            return 216184

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 183:
            return 216183

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 182:
            return 216182

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 181:
            return 216181

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 180:
            return 216180

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 179:
            return 216179

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 178:
            return 216178

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 177:
            return 216177

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 176:
            return 216176

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 175:
            return 216175

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 174:
            return 216174

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 173:
            return 216173

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 172:
            return 216172

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 171:
            return 216171

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 170:
            return 216170

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 169:
            return 216169

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 168:
            return 216168

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 167:
            return 216167

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 166:
            return 216166

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 165:
            return 216165

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 164:
            return 216164

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 163:
            return 216163

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 162:
            return 216162

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 161:
            return 216161

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 160:
            return 216160

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 159:
            return 216159

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 158:
            return 216158

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 157:
            return 216157

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 156:
            return 216156

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 155:
            return 216155

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 154:
            return 216154

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 153:
            return 216153

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 152:
            return 216152

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 151:
            return 216151

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 150:
            return 216150

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 149:
            return 216149

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 148:
            return 216148

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 147:
            return 216147

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 146:
            return 216146

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 145:
            return 216145

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 144:
            return 216144

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 143:
            return 216143

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 142:
            return 216142

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 141:
            return 216141

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 140:
            return 216140

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 139:
            return 216139

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 138:
            return 216138

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 137:
            return 216137

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 136:
            return 216136

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 135:
            return 216135

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 134:
            return 216134

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 133:
            return 216133

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 132:
            return 216132

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 131:
            return 216131

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 130:
            return 216130

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 129:
            return 216129

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 128:
            return 216128

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 127:
            return 216127

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 126:
            return 216126

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 125:
            return 216125

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 124:
            return 216124

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 123:
            return 216123

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 122:
            return 216122

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 121:
            return 216121

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 120:
            return 216120

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 119:
            return 216119

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 118:
            return 216118

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 117:
            return 216117

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 116:
            return 216116

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 115:
            return 216115

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 114:
            return 216114

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 113:
            return 216113

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 112:
            return 216112

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 111:
            return 216111

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 110:
            return 216110

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 109:
            return 216109

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 108:
            return 216108

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 107:
            return 216107

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 106:
            return 216106

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 105:
            return 216105

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 104:
            return 216104

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 103:
            return 216103

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 102:
            return 216102

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 101:
            return 216101

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 100:
            return 216100

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 99:
            return 216099

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 98:
            return 216098

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 97:
            return 216097

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 96:
            return 216096

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 95:
            return 216095

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 94:
            return 216094

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 93:
            return 216093

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 92:
            return 216092

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 91:
            return 216091

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 90:
            return 216090

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 89:
            return 216089

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 88:
            return 216088

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 87:
            return 216087

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 86:
            return 216086

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 85:
            return 216085

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 84:
            return 216084

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 83:
            return 216083

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 82:
            return 216082

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 81:
            return 216081

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 80:
            return 216080

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 79:
            return 216079

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 78:
            return 216078

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 77:
            return 216077

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 76:
            return 216076

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 75:
            return 216075

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 74:
            return 216074

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 73:
            return 216073

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 72:
            return 216072

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 71:
            return 216071

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 70:
            return 216070

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 69:
            return 216069

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 68:
            return 216068

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 67:
            return 216067

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 66:
            return 216066

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 65:
            return 216065

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 64:
            return 216064

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 63:
            return 216063

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 62:
            return 216062

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 61:
            return 216061

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 60:
            return 216060

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 59:
            return 216059

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 58:
            return 216058

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 57:
            return 216057

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 56:
            return 216056

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 55:
            return 216055

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 54:
            return 216054

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 53:
            return 216053

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 52:
            return 216052

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 51:
            return 216051

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 50:
            return 216050

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 49:
            return 216049

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 48:
            return 216048

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 47:
            return 216047

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 46:
            return 216046

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 45:
            return 216045

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 44:
            return 216044

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 43:
            return 216043

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 42:
            return 216042

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 41:
            return 216041

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 40:
            return 216040

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 39:
            return 216039

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 38:
            return 216038

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 37:
            return 216037

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 36:
            return 216036

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 35:
            return 216035

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 34:
            return 216034

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 33:
            return 216033

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 32:
            return 216032

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 31:
            return 216031

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 30:
            return 216030

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 29:
            return 216029

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 28:
            return 216028

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 27:
            return 216027

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 26:
            return 216026

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 25:
            return 216025

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 24:
            return 216024

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 23:
            return 216023

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 22:
            return 216022

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 21:
            return 216021

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 20:
            return 216020

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 19:
            return 216019

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 18:
            return 216018

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 17:
            return 216017

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 16:
            return 216016

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 15:
            return 216015

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 14:
            return 216014

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 13:
            return 216013

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 12:
            return 216012

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 11:
            return 216011

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 10:
            return 216010

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 9:
            return 216009

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 8:
            return 216008

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 7:
            return 216007

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 6:
            return 216006

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 5:
            return 216005

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 4:
            return 216004

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 3:
            return 216003

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 2:
            return 216002

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 1:
            return 216001

        aerosolType = h.get_l('aerosolType')
        is_aerosol = h.get_l('is_aerosol')

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and aerosolType == 62003 and is_aerosol == 1:
            return 215210

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 62003 and is_aerosol == 1:
            return 215205

        is_aerosol_optical = h.get_l('is_aerosol_optical')
        typeOfWavelengthInterval = h.get_l('typeOfWavelengthInterval')
        scaleFactorOfFirstWavelength = h.get_l('scaleFactorOfFirstWavelength')
        scaledValueOfFirstWavelength = h.get_l('scaledValueOfFirstWavelength')
        typeOfSizeInterval = h.get_l('typeOfSizeInterval')

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 65533 and is_aerosol_optical == 1 and typeOfWavelengthInterval == 11 and scaleFactorOfFirstWavelength == 8 and scaledValueOfFirstWavelength == 55 and typeOfSizeInterval == 255:
            return 215204

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfSizeInterval == 255 and aerosolType == 65534 and is_aerosol_optical == 1 and typeOfWavelengthInterval == 11 and scaleFactorOfFirstWavelength == 8 and scaledValueOfFirstWavelength == 55:
            return 215203

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and aerosolType == 65533 and is_aerosol == 1:
            return 215202

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and aerosolType == 65534 and is_aerosol == 1:
            return 215201

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and aerosolType == 65533 and is_aerosol == 1:
            return 215200

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and aerosolType == 65534 and is_aerosol == 1:
            return 215199

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and aerosolType == 65533 and is_aerosol == 1:
            return 215198

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and aerosolType == 65534 and is_aerosol == 1:
            return 215197

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and aerosolType == 65533 and is_aerosol == 1:
            return 215196

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and aerosolType == 65534 and is_aerosol == 1:
            return 215195

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 65533 and is_aerosol == 1:
            return 215194

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and is_aerosol == 1 and aerosolType == 65534:
            return 215193

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 65533 and is_aerosol == 1:
            return 215192

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 65534 and is_aerosol == 1:
            return 215191

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 65533 and is_aerosol == 1:
            return 215190

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 65534 and is_aerosol == 1:
            return 215189

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 188:
            return 215188

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 187:
            return 215187

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 186:
            return 215186

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 185:
            return 215185

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 184:
            return 215184

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 183:
            return 215183

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 182:
            return 215182

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 181:
            return 215181

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 180:
            return 215180

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 179:
            return 215179

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 178:
            return 215178

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 177:
            return 215177

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 176:
            return 215176

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 175:
            return 215175

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 174:
            return 215174

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 173:
            return 215173

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 172:
            return 215172

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 171:
            return 215171

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 170:
            return 215170

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 169:
            return 215169

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 168:
            return 215168

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 167:
            return 215167

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 166:
            return 215166

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 165:
            return 215165

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 164:
            return 215164

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 163:
            return 215163

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 162:
            return 215162

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 161:
            return 215161

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 160:
            return 215160

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 159:
            return 215159

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 158:
            return 215158

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 157:
            return 215157

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 156:
            return 215156

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 155:
            return 215155

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 154:
            return 215154

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 153:
            return 215153

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 152:
            return 215152

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 151:
            return 215151

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 150:
            return 215150

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 149:
            return 215149

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 148:
            return 215148

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 147:
            return 215147

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 146:
            return 215146

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 145:
            return 215145

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 144:
            return 215144

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 143:
            return 215143

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 142:
            return 215142

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 141:
            return 215141

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 140:
            return 215140

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 139:
            return 215139

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 138:
            return 215138

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 137:
            return 215137

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 136:
            return 215136

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 135:
            return 215135

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 134:
            return 215134

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 133:
            return 215133

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 132:
            return 215132

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 131:
            return 215131

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 130:
            return 215130

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 129:
            return 215129

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 128:
            return 215128

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 127:
            return 215127

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 126:
            return 215126

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 125:
            return 215125

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 124:
            return 215124

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 123:
            return 215123

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 122:
            return 215122

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 121:
            return 215121

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 120:
            return 215120

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 119:
            return 215119

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 118:
            return 215118

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 117:
            return 215117

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 116:
            return 215116

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 115:
            return 215115

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 114:
            return 215114

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 113:
            return 215113

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 112:
            return 215112

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 111:
            return 215111

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 110:
            return 215110

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 109:
            return 215109

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 108:
            return 215108

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 107:
            return 215107

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 106:
            return 215106

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 105:
            return 215105

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 104:
            return 215104

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 103:
            return 215103

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 102:
            return 215102

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 101:
            return 215101

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 100:
            return 215100

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 99:
            return 215099

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 98:
            return 215098

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 97:
            return 215097

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 96:
            return 215096

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 95:
            return 215095

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 94:
            return 215094

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 93:
            return 215093

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 92:
            return 215092

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 91:
            return 215091

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 90:
            return 215090

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 89:
            return 215089

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 88:
            return 215088

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 87:
            return 215087

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 86:
            return 215086

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 85:
            return 215085

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 84:
            return 215084

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 83:
            return 215083

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 82:
            return 215082

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 81:
            return 215081

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 80:
            return 215080

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 79:
            return 215079

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 78:
            return 215078

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 77:
            return 215077

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 76:
            return 215076

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 75:
            return 215075

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 74:
            return 215074

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 73:
            return 215073

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 72:
            return 215072

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 71:
            return 215071

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 70:
            return 215070

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 69:
            return 215069

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 68:
            return 215068

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 67:
            return 215067

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 66:
            return 215066

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 65:
            return 215065

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 64:
            return 215064

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 63:
            return 215063

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 62:
            return 215062

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 61:
            return 215061

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 60:
            return 215060

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 59:
            return 215059

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 58:
            return 215058

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 57:
            return 215057

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 56:
            return 215056

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 55:
            return 215055

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 54:
            return 215054

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 53:
            return 215053

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 52:
            return 215052

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 51:
            return 215051

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 50:
            return 215050

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 49:
            return 215049

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 48:
            return 215048

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 47:
            return 215047

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 46:
            return 215046

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 45:
            return 215045

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 44:
            return 215044

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 43:
            return 215043

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 42:
            return 215042

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 41:
            return 215041

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 40:
            return 215040

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 39:
            return 215039

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 38:
            return 215038

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 37:
            return 215037

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 36:
            return 215036

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 35:
            return 215035

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 34:
            return 215034

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 33:
            return 215033

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 32:
            return 215032

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 31:
            return 215031

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 30:
            return 215030

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 29:
            return 215029

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 28:
            return 215028

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 27:
            return 215027

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 26:
            return 215026

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 25:
            return 215025

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 24:
            return 215024

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 23:
            return 215023

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 22:
            return 215022

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 21:
            return 215021

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 20:
            return 215020

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 19:
            return 215019

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 18:
            return 215018

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 17:
            return 215017

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 16:
            return 215016

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 15:
            return 215015

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 14:
            return 215014

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 13:
            return 215013

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 12:
            return 215012

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 11:
            return 215011

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 10:
            return 215010

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 9:
            return 215009

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 8:
            return 215008

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 7:
            return 215007

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 6:
            return 215006

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 5:
            return 215005

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 4:
            return 215004

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 3:
            return 215003

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 2:
            return 215002

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 1:
            return 215001

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 52:
            return 214052

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 51:
            return 214051

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 50:
            return 214050

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 49:
            return 214049

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 48:
            return 214048

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 47:
            return 214047

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 46:
            return 214046

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 45:
            return 214045

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 44:
            return 214044

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 43:
            return 214043

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 42:
            return 214042

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 41:
            return 214041

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 40:
            return 214040

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 39:
            return 214039

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 38:
            return 214038

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 37:
            return 214037

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 36:
            return 214036

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 35:
            return 214035

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 34:
            return 214034

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 33:
            return 214033

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 32:
            return 214032

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 31:
            return 214031

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 30:
            return 214030

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 29:
            return 214029

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 28:
            return 214028

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 27:
            return 214027

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 26:
            return 214026

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 25:
            return 214025

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 24:
            return 214024

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 23:
            return 214023

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 22:
            return 214022

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 21:
            return 214021

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 20:
            return 214020

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 19:
            return 214019

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 18:
            return 214018

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 17:
            return 214017

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 16:
            return 214016

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 15:
            return 214015

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 14:
            return 214014

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 13:
            return 214013

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 12:
            return 214012

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 11:
            return 214011

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 10:
            return 214010

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 9:
            return 214009

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 8:
            return 214008

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 7:
            return 214007

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 6:
            return 214006

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 5:
            return 214005

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 4:
            return 214004

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 3:
            return 214003

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 2:
            return 214002

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 1:
            return 214001

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 150:
            return 213150

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 149:
            return 213149

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 148:
            return 213148

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 147:
            return 213147

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 146:
            return 213146

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 145:
            return 213145

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 144:
            return 213144

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 143:
            return 213143

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 142:
            return 213142

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 141:
            return 213141

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 140:
            return 213140

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 139:
            return 213139

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 138:
            return 213138

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 137:
            return 213137

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 136:
            return 213136

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 135:
            return 213135

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 134:
            return 213134

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 133:
            return 213133

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 132:
            return 213132

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 131:
            return 213131

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 130:
            return 213130

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 129:
            return 213129

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 128:
            return 213128

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 127:
            return 213127

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 126:
            return 213126

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 125:
            return 213125

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 124:
            return 213124

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 123:
            return 213123

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 122:
            return 213122

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 121:
            return 213121

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 120:
            return 213120

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 119:
            return 213119

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 118:
            return 213118

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 117:
            return 213117

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 116:
            return 213116

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 115:
            return 213115

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 114:
            return 213114

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 113:
            return 213113

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 112:
            return 213112

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 111:
            return 213111

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 110:
            return 213110

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 109:
            return 213109

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 108:
            return 213108

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 107:
            return 213107

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 106:
            return 213106

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 105:
            return 213105

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 104:
            return 213104

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 103:
            return 213103

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 102:
            return 213102

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 101:
            return 213101

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 5:
            return 213005

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 4:
            return 213004

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 3:
            return 213003

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 2:
            return 213002

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 1:
            return 213001

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 255:
            return 212255

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 254:
            return 212254

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 253:
            return 212253

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 252:
            return 212252

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 251:
            return 212251

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 250:
            return 212250

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 249:
            return 212249

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 248:
            return 212248

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 247:
            return 212247

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 246:
            return 212246

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 245:
            return 212245

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 244:
            return 212244

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 243:
            return 212243

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 242:
            return 212242

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 241:
            return 212241

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 240:
            return 212240

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 239:
            return 212239

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 238:
            return 212238

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 237:
            return 212237

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 236:
            return 212236

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 235:
            return 212235

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 234:
            return 212234

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 233:
            return 212233

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 232:
            return 212232

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 231:
            return 212231

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 230:
            return 212230

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 229:
            return 212229

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 228:
            return 212228

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 227:
            return 212227

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 226:
            return 212226

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 225:
            return 212225

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 224:
            return 212224

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 223:
            return 212223

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 222:
            return 212222

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 221:
            return 212221

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 220:
            return 212220

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 219:
            return 212219

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 218:
            return 212218

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 217:
            return 212217

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 216:
            return 212216

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 215:
            return 212215

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 214:
            return 212214

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 213:
            return 212213

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 212:
            return 212212

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 211:
            return 212211

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 210:
            return 212210

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 209:
            return 212209

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 208:
            return 212208

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 207:
            return 212207

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 206:
            return 212206

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 205:
            return 212205

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 204:
            return 212204

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 203:
            return 212203

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 202:
            return 212202

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 201:
            return 212201

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 200:
            return 212200

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 199:
            return 212199

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 198:
            return 212198

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 197:
            return 212197

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 196:
            return 212196

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 195:
            return 212195

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 194:
            return 212194

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 193:
            return 212193

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 192:
            return 212192

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 191:
            return 212191

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 190:
            return 212190

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 189:
            return 212189

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 188:
            return 212188

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 187:
            return 212187

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 186:
            return 212186

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 185:
            return 212185

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 184:
            return 212184

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 183:
            return 212183

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 182:
            return 212182

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 181:
            return 212181

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 180:
            return 212180

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 179:
            return 212179

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 178:
            return 212178

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 177:
            return 212177

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 176:
            return 212176

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 175:
            return 212175

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 174:
            return 212174

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 173:
            return 212173

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 172:
            return 212172

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 171:
            return 212171

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 170:
            return 212170

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 169:
            return 212169

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 168:
            return 212168

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 167:
            return 212167

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 166:
            return 212166

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 165:
            return 212165

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 164:
            return 212164

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 163:
            return 212163

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 162:
            return 212162

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 161:
            return 212161

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 160:
            return 212160

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 159:
            return 212159

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 158:
            return 212158

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 157:
            return 212157

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 156:
            return 212156

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 155:
            return 212155

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 154:
            return 212154

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 153:
            return 212153

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 152:
            return 212152

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 151:
            return 212151

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 150:
            return 212150

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 149:
            return 212149

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 148:
            return 212148

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 147:
            return 212147

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 146:
            return 212146

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 145:
            return 212145

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 144:
            return 212144

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 143:
            return 212143

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 142:
            return 212142

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 141:
            return 212141

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 140:
            return 212140

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 139:
            return 212139

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 138:
            return 212138

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 137:
            return 212137

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 136:
            return 212136

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 135:
            return 212135

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 134:
            return 212134

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 133:
            return 212133

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 132:
            return 212132

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 131:
            return 212131

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 130:
            return 212130

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 129:
            return 212129

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 128:
            return 212128

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 127:
            return 212127

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 126:
            return 212126

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 125:
            return 212125

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 124:
            return 212124

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 123:
            return 212123

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 122:
            return 212122

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 121:
            return 212121

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 120:
            return 212120

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 119:
            return 212119

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 118:
            return 212118

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 117:
            return 212117

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 116:
            return 212116

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 115:
            return 212115

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 114:
            return 212114

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 113:
            return 212113

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 112:
            return 212112

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 111:
            return 212111

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 110:
            return 212110

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 109:
            return 212109

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 108:
            return 212108

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 107:
            return 212107

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 106:
            return 212106

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 105:
            return 212105

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 104:
            return 212104

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 103:
            return 212103

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 102:
            return 212102

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 101:
            return 212101

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 100:
            return 212100

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 99:
            return 212099

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 98:
            return 212098

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 97:
            return 212097

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 96:
            return 212096

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 95:
            return 212095

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 94:
            return 212094

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 93:
            return 212093

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 92:
            return 212092

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 91:
            return 212091

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 90:
            return 212090

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 89:
            return 212089

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 88:
            return 212088

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 87:
            return 212087

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 86:
            return 212086

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 85:
            return 212085

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 84:
            return 212084

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 83:
            return 212083

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 82:
            return 212082

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 81:
            return 212081

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 80:
            return 212080

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 79:
            return 212079

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 78:
            return 212078

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 77:
            return 212077

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 76:
            return 212076

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 75:
            return 212075

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 74:
            return 212074

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 73:
            return 212073

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 72:
            return 212072

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 71:
            return 212071

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 70:
            return 212070

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 69:
            return 212069

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 68:
            return 212068

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 67:
            return 212067

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 66:
            return 212066

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 65:
            return 212065

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 64:
            return 212064

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 63:
            return 212063

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 62:
            return 212062

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 61:
            return 212061

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 60:
            return 212060

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 59:
            return 212059

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 58:
            return 212058

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 57:
            return 212057

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 56:
            return 212056

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 55:
            return 212055

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 54:
            return 212054

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 53:
            return 212053

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 52:
            return 212052

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 51:
            return 212051

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 50:
            return 212050

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 49:
            return 212049

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 48:
            return 212048

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 47:
            return 212047

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 46:
            return 212046

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 45:
            return 212045

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 44:
            return 212044

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 43:
            return 212043

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 42:
            return 212042

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 41:
            return 212041

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 40:
            return 212040

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 39:
            return 212039

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 38:
            return 212038

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 37:
            return 212037

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 36:
            return 212036

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 35:
            return 212035

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 34:
            return 212034

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 33:
            return 212033

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 32:
            return 212032

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 31:
            return 212031

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 30:
            return 212030

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 29:
            return 212029

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 28:
            return 212028

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 27:
            return 212027

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 26:
            return 212026

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 25:
            return 212025

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 24:
            return 212024

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 23:
            return 212023

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 22:
            return 212022

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 21:
            return 212021

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 20:
            return 212020

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 19:
            return 212019

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 18:
            return 212018

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 17:
            return 212017

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 16:
            return 212016

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 15:
            return 212015

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 14:
            return 212014

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 13:
            return 212013

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 12:
            return 212012

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 11:
            return 212011

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 10:
            return 212010

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 9:
            return 212009

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 8:
            return 212008

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 7:
            return 212007

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 6:
            return 212006

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 5:
            return 212005

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 4:
            return 212004

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 3:
            return 212003

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 2:
            return 212002

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 1:
            return 212001

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 120:
            return 211120

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 119:
            return 211119

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 56:
            return 211056

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 55:
            return 211055

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 45:
            return 211045

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 44:
            return 211044

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 43:
            return 211043

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 30:
            return 211030

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 29:
            return 211029

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 28:
            return 211028

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 15:
            return 211015

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 14:
            return 211014

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 13:
            return 211013

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and aerosolType == 65533 and is_aerosol == 1:
            return 210248

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and aerosolType == 65534 and is_aerosol == 1:
            return 210247

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 246:
            return 210246

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 245:
            return 210245

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 244:
            return 210244

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 243:
            return 210243

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 242:
            return 210242

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 241:
            return 210241

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 240:
            return 210240

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 239:
            return 210239

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 238:
            return 210238

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 237:
            return 210237

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 236:
            return 210236

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 235:
            return 210235

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 234:
            return 210234

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 233:
            return 210233

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 232:
            return 210232

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 231:
            return 210231

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 230:
            return 210230

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 229:
            return 210229

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 228:
            return 210228

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 227:
            return 210227

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 226:
            return 210226

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 225:
            return 210225

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 224:
            return 210224

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 223:
            return 210223

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 222:
            return 210222

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 221:
            return 210221

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 220:
            return 210220

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 219:
            return 210219

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 218:
            return 210218

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 217:
            return 210217

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 197:
            return 210197

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 196:
            return 210196

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 195:
            return 210195

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 194:
            return 210194

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 193:
            return 210193

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 192:
            return 210192

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 191:
            return 210191

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 190:
            return 210190

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 189:
            return 210189

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 188:
            return 210188

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 187:
            return 210187

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 186:
            return 210186

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 179:
            return 210179

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 177:
            return 210177

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 169:
            return 210169

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 167:
            return 210167

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 120:
            return 210120

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 119:
            return 210119

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 118:
            return 210118

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 79:
            return 210079

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 74:
            return 210074

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 73:
            return 210073

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 72:
            return 210072

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 60:
            return 210060

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 59:
            return 210059

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 58:
            return 210058

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 57:
            return 210057

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 56:
            return 210056

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 55:
            return 210055

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 45:
            return 210045

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 44:
            return 210044

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 43:
            return 210043

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 30:
            return 210030

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 29:
            return 210029

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 28:
            return 210028

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 15:
            return 210015

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 14:
            return 210014

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 13:
            return 210013

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 122:
            return 171122

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 121:
            return 171121

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 7:
            return 171007

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 6:
            return 171006

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 141:
            return 162141

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 140:
            return 162140

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 139:
            return 162139

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 138:
            return 162138

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 137:
            return 162137

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 136:
            return 162136

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 135:
            return 162135

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 134:
            return 162134

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 133:
            return 162133

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 132:
            return 162132

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 131:
            return 162131

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 130:
            return 162130

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 129:
            return 162129

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 128:
            return 162128

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 127:
            return 162127

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 126:
            return 162126

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 125:
            return 162125

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 124:
            return 162124

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 123:
            return 162123

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 122:
            return 162122

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 121:
            return 162121

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 120:
            return 162120

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 119:
            return 162119

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 118:
            return 162118

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 117:
            return 162117

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 116:
            return 162116

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 115:
            return 162115

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 114:
            return 162114

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 193:
            return 151193

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 255:
            return 200255

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 254:
            return 200254

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 253:
            return 200253

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 252:
            return 200252

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 251:
            return 200251

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 250:
            return 200250

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 249:
            return 200249

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 248:
            return 200248

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 247:
            return 200247

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 246:
            return 200246

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 245:
            return 200245

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 244:
            return 200244

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 243:
            return 200243

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 242:
            return 200242

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 241:
            return 200241

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 240:
            return 200240

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 239:
            return 200239

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 238:
            return 200238

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 237:
            return 200237

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 236:
            return 200236

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 235:
            return 200235

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 234:
            return 200234

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 233:
            return 200233

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 232:
            return 200232

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 231:
            return 200231

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 230:
            return 200230

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 229:
            return 200229

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 228:
            return 200228

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 227:
            return 200227

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 226:
            return 200226

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 225:
            return 200225

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 224:
            return 200224

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 223:
            return 200223

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 222:
            return 200222

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 221:
            return 200221

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 220:
            return 200220

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 219:
            return 200219

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 218:
            return 200218

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 217:
            return 200217

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 216:
            return 200216

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 215:
            return 200215

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 214:
            return 200214

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 212:
            return 200212

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 211:
            return 200211

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 210:
            return 200210

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 209:
            return 200209

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 208:
            return 200208

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 207:
            return 200207

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 206:
            return 200206

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 205:
            return 200205

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 204:
            return 200204

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 203:
            return 200203

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 202:
            return 200202

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 201:
            return 200201

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 200:
            return 200200

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 199:
            return 200199

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 198:
            return 200198

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 197:
            return 200197

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 196:
            return 200196

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 195:
            return 200195

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 194:
            return 200194

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 193:
            return 200193

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 192:
            return 200192

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 191:
            return 200191

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 190:
            return 200190

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 189:
            return 200189

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 188:
            return 200188

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 187:
            return 200187

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 186:
            return 200186

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 185:
            return 200185

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 184:
            return 200184

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 183:
            return 200183

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 182:
            return 200182

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 181:
            return 200181

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 180:
            return 200180

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 179:
            return 200179

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 178:
            return 200178

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 177:
            return 200177

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 176:
            return 200176

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 175:
            return 200175

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 174:
            return 200174

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 173:
            return 200173

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 172:
            return 200172

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 171:
            return 200171

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 170:
            return 200170

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 169:
            return 200169

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 167:
            return 200167

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 166:
            return 200166

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 165:
            return 200165

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 164:
            return 200164

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 163:
            return 200163

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 162:
            return 200162

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 161:
            return 200161

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 160:
            return 200160

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 159:
            return 200159

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 158:
            return 200158

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 157:
            return 200157

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 156:
            return 200156

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 155:
            return 200155

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 154:
            return 200154

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 153:
            return 200153

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 152:
            return 200152

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 151:
            return 200151

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 150:
            return 200150

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 149:
            return 200149

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 148:
            return 200148

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 147:
            return 200147

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 146:
            return 200146

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 145:
            return 200145

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 144:
            return 200144

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 143:
            return 200143

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 142:
            return 200142

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 141:
            return 200141

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 140:
            return 200140

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 139:
            return 200139

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 138:
            return 200138

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 137:
            return 200137

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 136:
            return 200136

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 135:
            return 200135

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 134:
            return 200134

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 133:
            return 200133

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 132:
            return 200132

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 131:
            return 200131

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 130:
            return 200130

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 129:
            return 200129

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 128:
            return 200128

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 127:
            return 200127

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 126:
            return 200126

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 125:
            return 200125

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 123:
            return 200123

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 122:
            return 200122

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 121:
            return 200121

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 120:
            return 200120

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 119:
            return 200119

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 118:
            return 200118

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 117:
            return 200117

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 116:
            return 200116

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 115:
            return 200115

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 114:
            return 200114

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 113:
            return 200113

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 112:
            return 200112

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 111:
            return 200111

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 110:
            return 200110

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 109:
            return 200109

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 108:
            return 200108

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 107:
            return 200107

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 106:
            return 200106

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 105:
            return 200105

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 104:
            return 200104

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 103:
            return 200103

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 102:
            return 200102

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 101:
            return 200101

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 100:
            return 200100

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 99:
            return 200099

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 98:
            return 200098

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 97:
            return 200097

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 96:
            return 200096

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 95:
            return 200095

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 94:
            return 200094

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 93:
            return 200093

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 92:
            return 200092

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 91:
            return 200091

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 90:
            return 200090

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 89:
            return 200089

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 88:
            return 200088

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 87:
            return 200087

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 86:
            return 200086

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 85:
            return 200085

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 84:
            return 200084

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 83:
            return 200083

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 82:
            return 200082

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 81:
            return 200081

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 80:
            return 200080

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 79:
            return 200079

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 78:
            return 200078

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 71:
            return 200071

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 70:
            return 200070

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 69:
            return 200069

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 68:
            return 200068

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 67:
            return 200067

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 66:
            return 200066

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 65:
            return 200065

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 64:
            return 200064

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 63:
            return 200063

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 62:
            return 200062

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 61:
            return 200061

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 60:
            return 200060

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 59:
            return 200059

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 58:
            return 200058

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 57:
            return 200057

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 56:
            return 200056

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 55:
            return 200055

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 54:
            return 200054

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 53:
            return 200053

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 52:
            return 200052

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 51:
            return 200051

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 50:
            return 200050

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 49:
            return 200049

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 48:
            return 200048

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 47:
            return 200047

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 46:
            return 200046

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 45:
            return 200045

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 44:
            return 200044

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 43:
            return 200043

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 42:
            return 200042

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 41:
            return 200041

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 40:
            return 200040

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 39:
            return 200039

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 38:
            return 200038

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 37:
            return 200037

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 36:
            return 200036

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 35:
            return 200035

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 34:
            return 200034

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 33:
            return 200033

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 32:
            return 200032

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 31:
            return 200031

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 30:
            return 200030

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 29:
            return 200029

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 28:
            return 200028

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 27:
            return 200027

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 26:
            return 200026

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 25:
            return 200025

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 24:
            return 200024

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 23:
            return 200023

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 22:
            return 200022

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 21:
            return 200021

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 14:
            return 200014

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 13:
            return 200013

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 12:
            return 200012

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 11:
            return 200011

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 5:
            return 200005

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 4:
            return 200004

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 3:
            return 200003

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 2:
            return 200002

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 1:
            return 200001

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 254:
            return 254

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 253:
            return 253

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 252:
            return 252

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 251:
            return 251

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 250:
            return 250

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 249:
            return 249

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 245:
            return 245

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 244:
            return 244

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 243:
            return 243

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 242:
            return 242

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 241:
            return 241

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 240:
            return 240

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 239:
            return 239

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 238:
            return 238

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 237:
            return 237

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 236:
            return 236

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 234:
            return 234

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 233:
            return 233

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 232:
            return 232

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 231:
            return 231

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 230:
            return 230

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 229:
            return 229

        unitsFactor = h.get_l('unitsFactor')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and unitsFactor == 1000:
            return 228

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 227:
            return 227

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 226:
            return 226

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 225:
            return 225

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 224:
            return 224

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 223:
            return 223

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 222:
            return 222

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 221:
            return 221

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 220:
            return 220

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 219:
            return 219

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 218:
            return 218

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 217:
            return 217

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 216:
            return 216

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 215:
            return 215

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 214:
            return 214

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 213:
            return 213

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 212:
            return 212

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 209:
            return 209

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 208:
            return 208

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 206:
            return 206

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 205:
            return 205

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 204:
            return 204

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 200:
            return 200

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 199:
            return 199

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 198:
            return 198

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 197:
            return 197

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 196:
            return 196

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 195:
            return 195

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 193:
            return 193

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 192:
            return 192

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 191:
            return 191

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 190:
            return 190

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 188:
            return 188

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 187:
            return 187

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 186:
            return 186

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 185:
            return 185

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 184:
            return 184

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 183:
            return 183

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 182:
            return 182

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 178:
            return 178

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 174:
            return 174

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 171:
            return 171

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 170:
            return 170

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 164:
            return 164

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 163:
            return 163

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 162:
            return 162

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 161:
            return 161

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 160:
            return 160

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 159:
            return 159

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 158:
            return 158

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 154:
            return 154

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 153:
            return 153

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25 and typeOfFirstFixedSurface == 105:
            return 152

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 150:
            return 150

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 149:
            return 149

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 148:
            return 148

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 144:
            return 144

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10 and unitsFactor == 1000:
            return 143

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 142:
            return 142

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and unitsFactor == 1000:
            return 141

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 140:
            return 140

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 139:
            return 139

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 137:
            return 137

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 128:
            return 128

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 127:
            return 127

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 126:
            return 126

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 125:
            return 125

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 124:
            return 124

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 123:
            return 123

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 120:
            return 120

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 119:
            return 119

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 118:
            return 118

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 117:
            return 117

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 116:
            return 116

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 115:
            return 115

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 114:
            return 114

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 113:
            return 113

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 112:
            return 112

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 111:
            return 111

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 110:
            return 110

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 109:
            return 109

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 108:
            return 108

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 107:
            return 107

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 106:
            return 106

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 105:
            return 105

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 104:
            return 104

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 103:
            return 103

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 102:
            return 102

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 101:
            return 101

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 100:
            return 100

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 99:
            return 99

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 98:
            return 98

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 97:
            return 97

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 96:
            return 96

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 95:
            return 95

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 94:
            return 94

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 93:
            return 93

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 92:
            return 92

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 91:
            return 91

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 90:
            return 90

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 89:
            return 89

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 88:
            return 88

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 87:
            return 87

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 86:
            return 86

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 85:
            return 85

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 84:
            return 84

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 83:
            return 83

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 82:
            return 82

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 81:
            return 81

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 80:
            return 80

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 79:
            return 79

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 78:
            return 78

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 74:
            return 74

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 73:
            return 73

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 72:
            return 72

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 71:
            return 71

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 70:
            return 70

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 69:
            return 69

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 68:
            return 68

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 67:
            return 67

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 66:
            return 66

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 65:
            return 65

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 64:
            return 64

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 63:
            return 63

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 62:
            return 62

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 58:
            return 58

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 57:
            return 57

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 56:
            return 56

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 55:
            return 55

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 53:
            return 53

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 3 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103 and lengthOfTimeRange == 24 and indicatorOfUnitForTimeRange == 1:
            return 52

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103 and lengthOfTimeRange == 24 and indicatorOfUnitForTimeRange == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2:
            return 51

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 50:
            return 50

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 48:
            return 48

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 47:
            return 47

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 46:
            return 46

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 45:
            return 45

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 44:
            return 44

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 42:
            return 42

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 41:
            return 41

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 40:
            return 40

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 39:
            return 39

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 38:
            return 38

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 37:
            return 37

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 36:
            return 36

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 35:
            return 35

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 32:
            return 32

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 30:
            return 30

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 29:
            return 29

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 28:
            return 28

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 27:
            return 27

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 26:
            return 26

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 25:
            return 25

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 24:
            return 24

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 23:
            return 23

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 22:
            return 22

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 21:
            return 21

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 20:
            return 20

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 19:
            return 19

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 18:
            return 18

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 17:
            return 17

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 16:
            return 16

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 15:
            return 15

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 14:
            return 14

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 13:
            return 13

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 12:
            return 12

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 11:
            return 11

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 9:
            return 9

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 8:
            return 8

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 7:
            return 7

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 6:
            return 6

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 5:
            return 5

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 4:
            return 4

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 85:
            return 131085

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 100 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9:
            return 131085

    return wrapped
