import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 253 and indicatorOfParameter == 239:
            return 82253239

        if table2Version == 253 and indicatorOfParameter == 6:
            return 82253006

        if table2Version == 253 and indicatorOfParameter == 161:
            return 82253161

        if table2Version == 253 and indicatorOfParameter == 30:
            return 82253030

        if table2Version == 253 and indicatorOfParameter == 80:
            return 82253080

        if table2Version == 253 and indicatorOfParameter == 32:
            return 82253032

        if table2Version == 253 and indicatorOfParameter == 126:
            return 82253126

        if table2Version == 253 and indicatorOfParameter == 245:
            return 82253245

        if table2Version == 253 and indicatorOfParameter == 31:
            return 82253031

        if table2Version == 253 and indicatorOfParameter == 193:
            return 82253193

        if table2Version == 253 and indicatorOfParameter == 192:
            return 82253192

        if table2Version == 253 and indicatorOfParameter == 39:
            return 82253039

        if table2Version == 253 and indicatorOfParameter == 46:
            return 82253046

        if table2Version == 253 and indicatorOfParameter == 45:
            return 82253045

        if table2Version == 253 and indicatorOfParameter == 12:
            return 82253012

        if table2Version == 253 and indicatorOfParameter == 55:
            return 82253055

        if table2Version == 253 and indicatorOfParameter == 43:
            return 82253043

        if table2Version == 253 and indicatorOfParameter == 20:
            return 82253020

        if table2Version == 253 and indicatorOfParameter == 96:
            return 82253096

        if table2Version == 253 and indicatorOfParameter == 163:
            return 82253163

        if table2Version == 253 and indicatorOfParameter == 125:
            return 82253125

        if table2Version == 253 and indicatorOfParameter == 87:
            return 82253087

        if table2Version == 253 and indicatorOfParameter == 213:
            return 82253213

        if table2Version == 253 and indicatorOfParameter == 50:
            return 82253050

        if table2Version == 253 and indicatorOfParameter == 34:
            return 82253034

        if table2Version == 253 and indicatorOfParameter == 214:
            return 82253214

        if table2Version == 253 and indicatorOfParameter == 216:
            return 82253216

        if table2Version == 253 and indicatorOfParameter == 95:
            return 82253095

        if table2Version == 253 and indicatorOfParameter == 162:
            return 82253162

        if table2Version == 253 and indicatorOfParameter == 124:
            return 82253124

        if table2Version == 253 and indicatorOfParameter == 49:
            return 82253049

        if table2Version == 253 and indicatorOfParameter == 33:
            return 82253033

        if table2Version == 253 and indicatorOfParameter == 40:
            return 82253040

        if table2Version == 253 and indicatorOfParameter == 68:
            return 82253068

        if table2Version == 253 and indicatorOfParameter == 60:
            return 82253060

        if table2Version == 253 and indicatorOfParameter == 185:
            return 82253185

        if table2Version == 253 and indicatorOfParameter == 61:
            return 82253061

        if table2Version == 253 and indicatorOfParameter == 167:
            return 82253167

        if table2Version == 253 and indicatorOfParameter == 16:
            return 82253016

        if table2Version == 253 and indicatorOfParameter == 15:
            return 82253015

        if table2Version == 253 and indicatorOfParameter == 200:
            return 82001200

        if table2Version == 253 and indicatorOfParameter == 17:
            return 82253017

        if table2Version == 253 and indicatorOfParameter == 10:
            return 82253010

        if table2Version == 253 and indicatorOfParameter == 71:
            return 82253071

        if table2Version == 253 and indicatorOfParameter == 25:
            return 82253025

        if table2Version == 253 and indicatorOfParameter == 11:
            return 82253011

        if table2Version == 253 and indicatorOfParameter == 238:
            return 82253238

        if table2Version == 253 and indicatorOfParameter == 120:
            return 82253120

        if table2Version == 253 and indicatorOfParameter == 106:
            return 82253106

        if table2Version == 253 and indicatorOfParameter == 110:
            return 82253110

        if table2Version == 253 and indicatorOfParameter == 100:
            return 82253100

        if table2Version == 253 and indicatorOfParameter == 105:
            return 82253105

        if table2Version == 253 and indicatorOfParameter == 104:
            return 82253104

        if table2Version == 253 and indicatorOfParameter == 116:
            return 82253116

        if table2Version == 253 and indicatorOfParameter == 35:
            return 82253035

        if table2Version == 253 and indicatorOfParameter == 220:
            return 82253220

        if table2Version == 253 and indicatorOfParameter == 122:
            return 82253122

        if table2Version == 253 and indicatorOfParameter == 64:
            return 82253064

        if table2Version == 253 and indicatorOfParameter == 83:
            return 82253083

        if table2Version == 253 and indicatorOfParameter == 182:
            return 82253182

        if table2Version == 253 and indicatorOfParameter == 48:
            return 82253048

        if table2Version == 253 and indicatorOfParameter == 246:
            return 82253246

        if table2Version == 253 and indicatorOfParameter == 184:
            return 82253184

        if table2Version == 253 and indicatorOfParameter == 99:
            return 82253099

        if table2Version == 253 and indicatorOfParameter == 231:
            return 82253231

        if table2Version == 253 and indicatorOfParameter == 86:
            return 82253086

        if table2Version == 253 and indicatorOfParameter == 85:
            return 82253085

        if table2Version == 253 and indicatorOfParameter == 121:
            return 82253121

        if table2Version == 253 and indicatorOfParameter == 226:
            return 82253226

        if table2Version == 253 and indicatorOfParameter == 237:
            return 82253237

        if table2Version == 253 and indicatorOfParameter == 94:
            return 82253094

        if table2Version == 253 and indicatorOfParameter == 102:
            return 82253102

        if table2Version == 253 and indicatorOfParameter == 247:
            return 82253247

        if table2Version == 253 and indicatorOfParameter == 38:
            return 82253038

        if table2Version == 253 and indicatorOfParameter == 65:
            return 82253065

        if table2Version == 253 and indicatorOfParameter == 235:
            return 82253235

        if table2Version == 253 and indicatorOfParameter == 66:
            return 82253066

        if table2Version == 253 and indicatorOfParameter == 56:
            return 82253056

        if table2Version == 253 and indicatorOfParameter == 88:
            return 82253088

        if table2Version == 253 and indicatorOfParameter == 191:
            return 82253191

        if table2Version == 253 and indicatorOfParameter == 90:
            return 82253090

        if table2Version == 253 and indicatorOfParameter == 242:
            return 82253242

        if table2Version == 253 and indicatorOfParameter == 241:
            return 82253241

        if table2Version == 253 and indicatorOfParameter == 240:
            return 82253240

        if table2Version == 253 and indicatorOfParameter == 210:
            return 82253210

        if table2Version == 253 and indicatorOfParameter == 23:
            return 82253023

        if table2Version == 253 and indicatorOfParameter == 181:
            return 82253181

        if table2Version == 253 and indicatorOfParameter == 52:
            return 82253052

        if table2Version == 253 and indicatorOfParameter == 51:
            return 82253051

        if table2Version == 253 and indicatorOfParameter == 54:
            return 82253054

        if table2Version == 253 and indicatorOfParameter == 4:
            return 82253004

        if table2Version == 253 and indicatorOfParameter == 3:
            return 82253003

        if table2Version == 253 and indicatorOfParameter == 13:
            return 82253013

        if table2Version == 253 and indicatorOfParameter == 138:
            return 82253138

        if table2Version == 253 and indicatorOfParameter == 137:
            return 82253137

        if table2Version == 253 and indicatorOfParameter == 139:
            return 82253139

        if table2Version == 253 and indicatorOfParameter == 136:
            return 82253136

        if table2Version == 253 and indicatorOfParameter == 144:
            return 82253144

        if table2Version == 253 and indicatorOfParameter == 26:
            return 82253026

        if table2Version == 253 and indicatorOfParameter == 1:
            return 82253001

        if table2Version == 253 and indicatorOfParameter == 59:
            return 82253059

        if table2Version == 253 and indicatorOfParameter == 24:
            return 82253024

        if table2Version == 253 and indicatorOfParameter == 212:
            return 82253212

        if table2Version == 253 and indicatorOfParameter == 14:
            return 82253014

        if table2Version == 253 and indicatorOfParameter == 113:
            return 82253113

        if table2Version == 253 and indicatorOfParameter == 111:
            return 82253111

        if table2Version == 253 and indicatorOfParameter == 114:
            return 82253114

        if table2Version == 253 and indicatorOfParameter == 112:
            return 82253112

        if table2Version == 253 and indicatorOfParameter == 69:
            return 82253069

        if table2Version == 253 and indicatorOfParameter == 70:
            return 82253070

        if table2Version == 253 and indicatorOfParameter == 2:
            return 82253002

        if table2Version == 253 and indicatorOfParameter == 133:
            return 82253133

        if table2Version == 253 and indicatorOfParameter == 158:
            return 82253158

        if table2Version == 253 and indicatorOfParameter == 103:
            return 82253103

        if table2Version == 253 and indicatorOfParameter == 108:
            return 82253108

        if table2Version == 253 and indicatorOfParameter == 37:
            return 82253037

        if table2Version == 253 and indicatorOfParameter == 67:
            return 82253067

        if table2Version == 253 and indicatorOfParameter == 53:
            return 82253053

        if table2Version == 253 and indicatorOfParameter == 101:
            return 82253101

        if table2Version == 253 and indicatorOfParameter == 107:
            return 82253107

        if table2Version == 253 and indicatorOfParameter == 166:
            return 82253166

        if table2Version == 253 and indicatorOfParameter == 74:
            return 82253074

        if table2Version == 253 and indicatorOfParameter == 119:
            return 82253119

        if table2Version == 253 and indicatorOfParameter == 115:
            return 82253115

        if table2Version == 253 and indicatorOfParameter == 62:
            return 82253062

        if table2Version == 253 and indicatorOfParameter == 81:
            return 82253081

        if table2Version == 253 and indicatorOfParameter == 79:
            return 82253079

        if table2Version == 253 and indicatorOfParameter == 244:
            return 82253244

        if table2Version == 253 and indicatorOfParameter == 132:
            return 82253132

        if table2Version == 253 and indicatorOfParameter == 209:
            return 82253209

        if table2Version == 253 and indicatorOfParameter == 73:
            return 82253073

        if table2Version == 253 and indicatorOfParameter == 19:
            return 82253019

        if table2Version == 253 and indicatorOfParameter == 232:
            return 82253232

        if table2Version == 253 and indicatorOfParameter == 127:
            return 82253127

        if table2Version == 253 and indicatorOfParameter == 92:
            return 82253092

        if table2Version == 253 and indicatorOfParameter == 135:
            return 82253135

        if table2Version == 253 and indicatorOfParameter == 97:
            return 82253097

        if table2Version == 253 and indicatorOfParameter == 98:
            return 82253098

        if table2Version == 253 and indicatorOfParameter == 91:
            return 82253091

        if table2Version == 253 and indicatorOfParameter == 5:
            return 82253005

        if table2Version == 253 and indicatorOfParameter == 9:
            return 82253009

        if table2Version == 253 and indicatorOfParameter == 75:
            return 82253075

        if table2Version == 253 and indicatorOfParameter == 204:
            return 82253204

        if table2Version == 253 and indicatorOfParameter == 8:
            return 82253008

        if table2Version == 253 and indicatorOfParameter == 196:
            return 82253196

        if table2Version == 253 and indicatorOfParameter == 195:
            return 82253195

        if table2Version == 253 and indicatorOfParameter == 201:
            return 82253201

        if table2Version == 253 and indicatorOfParameter == 117:
            return 82253117

        if table2Version == 253 and indicatorOfParameter == 27:
            return 82253027

        if table2Version == 253 and indicatorOfParameter == 7:
            return 82253007

        if table2Version == 253 and indicatorOfParameter == 188:
            return 82253188

        if table2Version == 253 and indicatorOfParameter == 129:
            return 82253129

        if table2Version == 253 and indicatorOfParameter == 228:
            return 82253228

        if table2Version == 253 and indicatorOfParameter == 57:
            return 82253057

        if table2Version == 253 and indicatorOfParameter == 234:
            return 82253234

        if table2Version == 253 and indicatorOfParameter == 243:
            return 82253243

        if table2Version == 253 and indicatorOfParameter == 222:
            return 82253222

        if table2Version == 253 and indicatorOfParameter == 82:
            return 82253082

        if table2Version == 253 and indicatorOfParameter == 215:
            return 82253215

        if table2Version == 253 and indicatorOfParameter == 217:
            return 82253217

        if table2Version == 253 and indicatorOfParameter == 109:
            return 82253109

        if table2Version == 253 and indicatorOfParameter == 47:
            return 82253047

        if table2Version == 253 and indicatorOfParameter == 93:
            return 82253093

        if table2Version == 253 and indicatorOfParameter == 18:
            return 82253018

        if table2Version == 253 and indicatorOfParameter == 89:
            return 82253089

        if table2Version == 253 and indicatorOfParameter == 44:
            return 82253044

        if table2Version == 253 and indicatorOfParameter == 76:
            return 82253076

        if table2Version == 253 and indicatorOfParameter == 187:
            return 82253187

        if table2Version == 253 and indicatorOfParameter == 130:
            return 82253130

        if table2Version == 253 and indicatorOfParameter == 131:
            return 82253131

        if table2Version == 253 and indicatorOfParameter == 78:
            return 82253078

        if table2Version == 253 and indicatorOfParameter == 183:
            return 82253183

        if table2Version == 253 and indicatorOfParameter == 250:
            return 82253250

        if table2Version == 253 and indicatorOfParameter == 225:
            return 82253225

        if table2Version == 253 and indicatorOfParameter == 58:
            return 82253058

        if table2Version == 253 and indicatorOfParameter == 72:
            return 82253072

        if table2Version == 253 and indicatorOfParameter == 186:
            return 82253186

        if table2Version == 253 and indicatorOfParameter == 160:
            return 82253160

        if table2Version == 253 and indicatorOfParameter == 118:
            return 82253118

        if table2Version == 253 and indicatorOfParameter == 249:
            return 82253249

        if table2Version == 253 and indicatorOfParameter == 77:
            return 82253077

        if table2Version == 253 and indicatorOfParameter == 123:
            return 82253123

        if table2Version == 253 and indicatorOfParameter == 221:
            return 82253221

        if table2Version == 253 and indicatorOfParameter == 190:
            return 82253190

        if table2Version == 253 and indicatorOfParameter == 128:
            return 82253128

        if table2Version == 253 and indicatorOfParameter == 248:
            return 82253248

        if table2Version == 253 and indicatorOfParameter == 230:
            return 82253230

        if table2Version == 253 and indicatorOfParameter == 229:
            return 82253229

        if table2Version == 253 and indicatorOfParameter == 84:
            return 82253084

        if table2Version == 253 and indicatorOfParameter == 251:
            return 82253251

        if table2Version == 253 and indicatorOfParameter == 252:
            return 82253252

        if table2Version == 253 and indicatorOfParameter == 254:
            return 82253254

        if table2Version == 253 and indicatorOfParameter == 253:
            return 82253253

        if table2Version == 253 and indicatorOfParameter == 63:
            return 82253063

        if table2Version == 253 and indicatorOfParameter == 41:
            return 82253041

        if table2Version == 253 and indicatorOfParameter == 42:
            return 82253042

        if table2Version == 151 and indicatorOfParameter == 255:
            return 82151255

        if table2Version == 151 and indicatorOfParameter == 57:
            return 82151057

        if table2Version == 151 and indicatorOfParameter == 3:
            return 82151003

        if table2Version == 151 and indicatorOfParameter == 2:
            return 82151002

        if table2Version == 151 and indicatorOfParameter == 1:
            return 82151001

        if table2Version == 151 and indicatorOfParameter == 0:
            return 82151000

        if table2Version == 150 and indicatorOfParameter == 255:
            return 82150255

        if table2Version == 150 and indicatorOfParameter == 58:
            return 82150058

        if table2Version == 150 and indicatorOfParameter == 57:
            return 82150057

        if table2Version == 150 and indicatorOfParameter == 0:
            return 82150000

        if table2Version == 140 and indicatorOfParameter == 255:
            return 82140255

        if table2Version == 140 and indicatorOfParameter == 9:
            return 82140009

        if table2Version == 140 and indicatorOfParameter == 8:
            return 82140008

        if table2Version == 140 and indicatorOfParameter == 7:
            return 82140007

        if table2Version == 140 and indicatorOfParameter == 6:
            return 82140006

        if table2Version == 140 and indicatorOfParameter == 5:
            return 82140005

        if table2Version == 140 and indicatorOfParameter == 4:
            return 82140004

        if table2Version == 140 and indicatorOfParameter == 3:
            return 82140003

        if table2Version == 140 and indicatorOfParameter == 2:
            return 82140002

        if table2Version == 140 and indicatorOfParameter == 1:
            return 82140001

        if table2Version == 140 and indicatorOfParameter == 0:
            return 82140000

        if table2Version == 137 and indicatorOfParameter == 255:
            return 82137255

        if table2Version == 137 and indicatorOfParameter == 137:
            return 82137137

        if table2Version == 137 and indicatorOfParameter == 136:
            return 82137136

        if table2Version == 137 and indicatorOfParameter == 135:
            return 82137135

        if table2Version == 137 and indicatorOfParameter == 134:
            return 82137134

        if table2Version == 137 and indicatorOfParameter == 133:
            return 82137133

        if table2Version == 137 and indicatorOfParameter == 132:
            return 82137132

        if table2Version == 137 and indicatorOfParameter == 131:
            return 82137131

        if table2Version == 137 and indicatorOfParameter == 130:
            return 82137130

        if table2Version == 137 and indicatorOfParameter == 127:
            return 82137127

        if table2Version == 137 and indicatorOfParameter == 126:
            return 82137126

        if table2Version == 137 and indicatorOfParameter == 125:
            return 82137125

        if table2Version == 137 and indicatorOfParameter == 124:
            return 82137124

        if table2Version == 137 and indicatorOfParameter == 123:
            return 82137123

        if table2Version == 137 and indicatorOfParameter == 122:
            return 82137122

        if table2Version == 137 and indicatorOfParameter == 121:
            return 82137121

        if table2Version == 137 and indicatorOfParameter == 120:
            return 82137120

        if table2Version == 137 and indicatorOfParameter == 117:
            return 82137117

        if table2Version == 137 and indicatorOfParameter == 116:
            return 82137116

        if table2Version == 137 and indicatorOfParameter == 115:
            return 82137115

        if table2Version == 137 and indicatorOfParameter == 114:
            return 82137114

        if table2Version == 137 and indicatorOfParameter == 113:
            return 82137113

        if table2Version == 137 and indicatorOfParameter == 112:
            return 82137112

        if table2Version == 137 and indicatorOfParameter == 111:
            return 82137111

        if table2Version == 137 and indicatorOfParameter == 110:
            return 82137110

        if table2Version == 137 and indicatorOfParameter == 107:
            return 82137107

        if table2Version == 137 and indicatorOfParameter == 106:
            return 82137106

        if table2Version == 137 and indicatorOfParameter == 105:
            return 82137105

        if table2Version == 137 and indicatorOfParameter == 104:
            return 82137104

        if table2Version == 137 and indicatorOfParameter == 103:
            return 82137103

        if table2Version == 137 and indicatorOfParameter == 102:
            return 82137102

        if table2Version == 137 and indicatorOfParameter == 101:
            return 82137101

        if table2Version == 137 and indicatorOfParameter == 100:
            return 82137100

        if table2Version == 137 and indicatorOfParameter == 77:
            return 82137077

        if table2Version == 137 and indicatorOfParameter == 76:
            return 82137076

        if table2Version == 137 and indicatorOfParameter == 75:
            return 82137075

        if table2Version == 137 and indicatorOfParameter == 74:
            return 82137074

        if table2Version == 137 and indicatorOfParameter == 73:
            return 82137073

        if table2Version == 137 and indicatorOfParameter == 72:
            return 82137072

        if table2Version == 137 and indicatorOfParameter == 71:
            return 82137071

        if table2Version == 137 and indicatorOfParameter == 70:
            return 82137070

        if table2Version == 137 and indicatorOfParameter == 67:
            return 82137067

        if table2Version == 137 and indicatorOfParameter == 66:
            return 82137066

        if table2Version == 137 and indicatorOfParameter == 65:
            return 82137065

        if table2Version == 137 and indicatorOfParameter == 64:
            return 82137064

        if table2Version == 137 and indicatorOfParameter == 63:
            return 82137063

        if table2Version == 137 and indicatorOfParameter == 62:
            return 82137062

        if table2Version == 137 and indicatorOfParameter == 61:
            return 82137061

        if table2Version == 137 and indicatorOfParameter == 60:
            return 82137060

        if table2Version == 137 and indicatorOfParameter == 57:
            return 82137057

        if table2Version == 137 and indicatorOfParameter == 56:
            return 82137056

        if table2Version == 137 and indicatorOfParameter == 55:
            return 82137055

        if table2Version == 137 and indicatorOfParameter == 54:
            return 82137054

        if table2Version == 137 and indicatorOfParameter == 53:
            return 82137053

        if table2Version == 137 and indicatorOfParameter == 52:
            return 82137052

        if table2Version == 137 and indicatorOfParameter == 51:
            return 82137051

        if table2Version == 137 and indicatorOfParameter == 50:
            return 82137050

        if table2Version == 137 and indicatorOfParameter == 47:
            return 82137047

        if table2Version == 137 and indicatorOfParameter == 46:
            return 82137046

        if table2Version == 137 and indicatorOfParameter == 45:
            return 82137045

        if table2Version == 137 and indicatorOfParameter == 44:
            return 82137044

        if table2Version == 137 and indicatorOfParameter == 43:
            return 82137043

        if table2Version == 137 and indicatorOfParameter == 42:
            return 82137042

        if table2Version == 137 and indicatorOfParameter == 41:
            return 82137041

        if table2Version == 137 and indicatorOfParameter == 40:
            return 82137040

        if table2Version == 137 and indicatorOfParameter == 37:
            return 82137037

        if table2Version == 137 and indicatorOfParameter == 36:
            return 82137036

        if table2Version == 137 and indicatorOfParameter == 35:
            return 82137035

        if table2Version == 137 and indicatorOfParameter == 34:
            return 82137034

        if table2Version == 137 and indicatorOfParameter == 33:
            return 82137033

        if table2Version == 137 and indicatorOfParameter == 32:
            return 82137032

        if table2Version == 137 and indicatorOfParameter == 31:
            return 82137031

        if table2Version == 137 and indicatorOfParameter == 30:
            return 82137030

        if table2Version == 137 and indicatorOfParameter == 27:
            return 82137027

        if table2Version == 137 and indicatorOfParameter == 26:
            return 82137026

        if table2Version == 137 and indicatorOfParameter == 25:
            return 82137025

        if table2Version == 137 and indicatorOfParameter == 24:
            return 82137024

        if table2Version == 137 and indicatorOfParameter == 23:
            return 82137023

        if table2Version == 137 and indicatorOfParameter == 22:
            return 82137022

        if table2Version == 137 and indicatorOfParameter == 21:
            return 82137021

        if table2Version == 137 and indicatorOfParameter == 20:
            return 82137020

        if table2Version == 137 and indicatorOfParameter == 17:
            return 82137017

        if table2Version == 137 and indicatorOfParameter == 16:
            return 82137016

        if table2Version == 137 and indicatorOfParameter == 15:
            return 82137015

        if table2Version == 137 and indicatorOfParameter == 14:
            return 82137014

        if table2Version == 137 and indicatorOfParameter == 13:
            return 82137013

        if table2Version == 137 and indicatorOfParameter == 12:
            return 82137012

        if table2Version == 137 and indicatorOfParameter == 11:
            return 82137011

        if table2Version == 137 and indicatorOfParameter == 10:
            return 82137010

        if table2Version == 137 and indicatorOfParameter == 7:
            return 82137007

        if table2Version == 137 and indicatorOfParameter == 6:
            return 82137006

        if table2Version == 137 and indicatorOfParameter == 5:
            return 82137005

        if table2Version == 137 and indicatorOfParameter == 4:
            return 82137004

        if table2Version == 137 and indicatorOfParameter == 3:
            return 82137003

        if table2Version == 137 and indicatorOfParameter == 2:
            return 82137002

        if table2Version == 137 and indicatorOfParameter == 1:
            return 82137001

        if table2Version == 137 and indicatorOfParameter == 0:
            return 82137000

        if table2Version == 136 and indicatorOfParameter == 255:
            return 82136255

        if table2Version == 136 and indicatorOfParameter == 206:
            return 82136206

        if table2Version == 136 and indicatorOfParameter == 175:
            return 82136175

        if table2Version == 136 and indicatorOfParameter == 165:
            return 82136165

        if table2Version == 136 and indicatorOfParameter == 120:
            return 82136120

        if table2Version == 136 and indicatorOfParameter == 119:
            return 82136119

        if table2Version == 136 and indicatorOfParameter == 118:
            return 82136118

        if table2Version == 136 and indicatorOfParameter == 117:
            return 82136117

        if table2Version == 136 and indicatorOfParameter == 116:
            return 82136116

        if table2Version == 136 and indicatorOfParameter == 91:
            return 82136091

        if table2Version == 136 and indicatorOfParameter == 84:
            return 82136084

        if table2Version == 136 and indicatorOfParameter == 79:
            return 82136079

        if table2Version == 136 and indicatorOfParameter == 78:
            return 82136078

        if table2Version == 136 and indicatorOfParameter == 77:
            return 82136077

        if table2Version == 136 and indicatorOfParameter == 73:
            return 82136073

        if table2Version == 136 and indicatorOfParameter == 71:
            return 82136071

        if table2Version == 136 and indicatorOfParameter == 66:
            return 82136066

        if table2Version == 136 and indicatorOfParameter == 54:
            return 82136054

        if table2Version == 136 and indicatorOfParameter == 51:
            return 82136051

        if table2Version == 136 and indicatorOfParameter == 11:
            return 82136011

        if table2Version == 136 and indicatorOfParameter == 1:
            return 82136001

        if table2Version == 136 and indicatorOfParameter == 0:
            return 82136000

        if table2Version == 135 and indicatorOfParameter == 255:
            return 82135255

        if table2Version == 135 and indicatorOfParameter == 254:
            return 82135254

        if table2Version == 135 and indicatorOfParameter == 253:
            return 82135253

        if table2Version == 135 and indicatorOfParameter == 252:
            return 82135252

        if table2Version == 135 and indicatorOfParameter == 251:
            return 82135251

        if table2Version == 135 and indicatorOfParameter == 250:
            return 82135250

        if table2Version == 135 and indicatorOfParameter == 249:
            return 82135249

        if table2Version == 135 and indicatorOfParameter == 248:
            return 82135248

        if table2Version == 135 and indicatorOfParameter == 247:
            return 82135247

        if table2Version == 135 and indicatorOfParameter == 246:
            return 82135246

        if table2Version == 135 and indicatorOfParameter == 245:
            return 82135245

        if table2Version == 135 and indicatorOfParameter == 244:
            return 82135244

        if table2Version == 135 and indicatorOfParameter == 243:
            return 82135243

        if table2Version == 135 and indicatorOfParameter == 242:
            return 82135242

        if table2Version == 135 and indicatorOfParameter == 241:
            return 82135241

        if table2Version == 135 and indicatorOfParameter == 240:
            return 82135240

        if table2Version == 135 and indicatorOfParameter == 239:
            return 82135239

        if table2Version == 135 and indicatorOfParameter == 238:
            return 82135238

        if table2Version == 135 and indicatorOfParameter == 237:
            return 82135237

        if table2Version == 135 and indicatorOfParameter == 236:
            return 82135236

        if table2Version == 135 and indicatorOfParameter == 235:
            return 82135235

        if table2Version == 135 and indicatorOfParameter == 234:
            return 82135234

        if table2Version == 135 and indicatorOfParameter == 233:
            return 82135233

        if table2Version == 135 and indicatorOfParameter == 232:
            return 82135232

        if table2Version == 135 and indicatorOfParameter == 231:
            return 82135231

        if table2Version == 135 and indicatorOfParameter == 230:
            return 82135230

        if table2Version == 135 and indicatorOfParameter == 229:
            return 82135229

        if table2Version == 135 and indicatorOfParameter == 228:
            return 82135228

        if table2Version == 135 and indicatorOfParameter == 227:
            return 82135227

        if table2Version == 135 and indicatorOfParameter == 226:
            return 82135226

        if table2Version == 135 and indicatorOfParameter == 225:
            return 82135225

        if table2Version == 135 and indicatorOfParameter == 224:
            return 82135224

        if table2Version == 135 and indicatorOfParameter == 223:
            return 82135223

        if table2Version == 135 and indicatorOfParameter == 222:
            return 82135222

        if table2Version == 135 and indicatorOfParameter == 221:
            return 82135221

        if table2Version == 135 and indicatorOfParameter == 220:
            return 82135220

        if table2Version == 135 and indicatorOfParameter == 219:
            return 82135219

        if table2Version == 135 and indicatorOfParameter == 218:
            return 82135218

        if table2Version == 135 and indicatorOfParameter == 217:
            return 82135217

        if table2Version == 135 and indicatorOfParameter == 216:
            return 82135216

        if table2Version == 135 and indicatorOfParameter == 215:
            return 82135215

        if table2Version == 135 and indicatorOfParameter == 214:
            return 82135214

        if table2Version == 135 and indicatorOfParameter == 213:
            return 82135213

        if table2Version == 135 and indicatorOfParameter == 212:
            return 82135212

        if table2Version == 135 and indicatorOfParameter == 211:
            return 82135211

        if table2Version == 135 and indicatorOfParameter == 210:
            return 82135210

        if table2Version == 135 and indicatorOfParameter == 209:
            return 82135209

        if table2Version == 135 and indicatorOfParameter == 208:
            return 82135208

        if table2Version == 135 and indicatorOfParameter == 171:
            return 82135171

        if table2Version == 135 and indicatorOfParameter == 170:
            return 82135170

        if table2Version == 135 and indicatorOfParameter == 169:
            return 82135169

        if table2Version == 135 and indicatorOfParameter == 168:
            return 82135168

        if table2Version == 135 and indicatorOfParameter == 167:
            return 82135167

        if table2Version == 135 and indicatorOfParameter == 166:
            return 82135166

        if table2Version == 135 and indicatorOfParameter == 165:
            return 82135165

        if table2Version == 135 and indicatorOfParameter == 164:
            return 82135164

        if table2Version == 135 and indicatorOfParameter == 163:
            return 82135163

        if table2Version == 135 and indicatorOfParameter == 162:
            return 82135162

        if table2Version == 135 and indicatorOfParameter == 161:
            return 82135161

        if table2Version == 135 and indicatorOfParameter == 160:
            return 82135160

        if table2Version == 135 and indicatorOfParameter == 151:
            return 82135151

        if table2Version == 135 and indicatorOfParameter == 150:
            return 82135150

        if table2Version == 135 and indicatorOfParameter == 149:
            return 82135149

        if table2Version == 135 and indicatorOfParameter == 148:
            return 82135148

        if table2Version == 135 and indicatorOfParameter == 147:
            return 82135147

        if table2Version == 135 and indicatorOfParameter == 146:
            return 82135146

        if table2Version == 135 and indicatorOfParameter == 145:
            return 82135145

        if table2Version == 135 and indicatorOfParameter == 144:
            return 82135144

        if table2Version == 135 and indicatorOfParameter == 143:
            return 82135143

        if table2Version == 135 and indicatorOfParameter == 142:
            return 82135142

        if table2Version == 135 and indicatorOfParameter == 141:
            return 82135141

        if table2Version == 135 and indicatorOfParameter == 140:
            return 82135140

        if table2Version == 135 and indicatorOfParameter == 131:
            return 82135131

        if table2Version == 135 and indicatorOfParameter == 130:
            return 82135130

        if table2Version == 135 and indicatorOfParameter == 129:
            return 82135129

        if table2Version == 135 and indicatorOfParameter == 128:
            return 82135128

        if table2Version == 135 and indicatorOfParameter == 127:
            return 82135127

        if table2Version == 135 and indicatorOfParameter == 126:
            return 82135126

        if table2Version == 135 and indicatorOfParameter == 125:
            return 82135125

        if table2Version == 135 and indicatorOfParameter == 124:
            return 82135124

        if table2Version == 135 and indicatorOfParameter == 123:
            return 82135123

        if table2Version == 135 and indicatorOfParameter == 122:
            return 82135122

        if table2Version == 135 and indicatorOfParameter == 121:
            return 82135121

        if table2Version == 135 and indicatorOfParameter == 120:
            return 82135120

        if table2Version == 135 and indicatorOfParameter == 111:
            return 82135111

        if table2Version == 135 and indicatorOfParameter == 110:
            return 82135110

        if table2Version == 135 and indicatorOfParameter == 109:
            return 82135109

        if table2Version == 135 and indicatorOfParameter == 108:
            return 82135108

        if table2Version == 135 and indicatorOfParameter == 107:
            return 82135107

        if table2Version == 135 and indicatorOfParameter == 106:
            return 82135106

        if table2Version == 135 and indicatorOfParameter == 105:
            return 82135105

        if table2Version == 135 and indicatorOfParameter == 104:
            return 82135104

        if table2Version == 135 and indicatorOfParameter == 103:
            return 82135103

        if table2Version == 135 and indicatorOfParameter == 102:
            return 82135102

        if table2Version == 135 and indicatorOfParameter == 101:
            return 82135101

        if table2Version == 135 and indicatorOfParameter == 100:
            return 82135100

        if table2Version == 135 and indicatorOfParameter == 5:
            return 82135005

        if table2Version == 135 and indicatorOfParameter == 4:
            return 82135004

        if table2Version == 135 and indicatorOfParameter == 3:
            return 82135003

        if table2Version == 135 and indicatorOfParameter == 2:
            return 82135002

        if table2Version == 135 and indicatorOfParameter == 1:
            return 82135001

        if table2Version == 135 and indicatorOfParameter == 0:
            return 82135000

        if table2Version == 134 and indicatorOfParameter == 255:
            return 82134255

        if table2Version == 134 and indicatorOfParameter == 113:
            return 82134113

        if table2Version == 134 and indicatorOfParameter == 112:
            return 82134112

        if table2Version == 134 and indicatorOfParameter == 111:
            return 82134111

        if table2Version == 134 and indicatorOfParameter == 110:
            return 82134110

        if table2Version == 134 and indicatorOfParameter == 108:
            return 82134108

        if table2Version == 134 and indicatorOfParameter == 107:
            return 82134107

        if table2Version == 134 and indicatorOfParameter == 106:
            return 82134106

        if table2Version == 134 and indicatorOfParameter == 105:
            return 82134105

        if table2Version == 134 and indicatorOfParameter == 103:
            return 82134103

        if table2Version == 134 and indicatorOfParameter == 102:
            return 82134102

        if table2Version == 134 and indicatorOfParameter == 101:
            return 82134101

        if table2Version == 134 and indicatorOfParameter == 100:
            return 82134100

        if table2Version == 134 and indicatorOfParameter == 92:
            return 82134092

        if table2Version == 134 and indicatorOfParameter == 91:
            return 82134091

        if table2Version == 134 and indicatorOfParameter == 90:
            return 82134090

        if table2Version == 134 and indicatorOfParameter == 84:
            return 82134084

        if table2Version == 134 and indicatorOfParameter == 83:
            return 82134083

        if table2Version == 134 and indicatorOfParameter == 82:
            return 82134082

        if table2Version == 134 and indicatorOfParameter == 81:
            return 82134081

        if table2Version == 134 and indicatorOfParameter == 80:
            return 82134080

        if table2Version == 134 and indicatorOfParameter == 79:
            return 82134079

        if table2Version == 134 and indicatorOfParameter == 78:
            return 82134078

        if table2Version == 134 and indicatorOfParameter == 77:
            return 82134077

        if table2Version == 134 and indicatorOfParameter == 76:
            return 82134076

        if table2Version == 134 and indicatorOfParameter == 75:
            return 82134075

        if table2Version == 134 and indicatorOfParameter == 74:
            return 82134074

        if table2Version == 134 and indicatorOfParameter == 70:
            return 82134070

        if table2Version == 134 and indicatorOfParameter == 68:
            return 82134068

        if table2Version == 134 and indicatorOfParameter == 67:
            return 82134067

        if table2Version == 134 and indicatorOfParameter == 66:
            return 82134066

        if table2Version == 134 and indicatorOfParameter == 65:
            return 82134065

        if table2Version == 134 and indicatorOfParameter == 64:
            return 82134064

        if table2Version == 134 and indicatorOfParameter == 63:
            return 82134063

        if table2Version == 134 and indicatorOfParameter == 62:
            return 82134062

        if table2Version == 134 and indicatorOfParameter == 61:
            return 82134061

        if table2Version == 134 and indicatorOfParameter == 60:
            return 82134060

        if table2Version == 134 and indicatorOfParameter == 59:
            return 82134059

        if table2Version == 134 and indicatorOfParameter == 58:
            return 82134058

        if table2Version == 134 and indicatorOfParameter == 57:
            return 82134057

        if table2Version == 134 and indicatorOfParameter == 56:
            return 82134056

        if table2Version == 134 and indicatorOfParameter == 55:
            return 82134055

        if table2Version == 134 and indicatorOfParameter == 54:
            return 82134054

        if table2Version == 134 and indicatorOfParameter == 53:
            return 82134053

        if table2Version == 134 and indicatorOfParameter == 52:
            return 82134052

        if table2Version == 134 and indicatorOfParameter == 51:
            return 82134051

        if table2Version == 134 and indicatorOfParameter == 50:
            return 82134050

        if table2Version == 134 and indicatorOfParameter == 49:
            return 82134049

        if table2Version == 134 and indicatorOfParameter == 48:
            return 82134048

        if table2Version == 134 and indicatorOfParameter == 47:
            return 82134047

        if table2Version == 134 and indicatorOfParameter == 46:
            return 82134046

        if table2Version == 134 and indicatorOfParameter == 45:
            return 82134045

        if table2Version == 134 and indicatorOfParameter == 44:
            return 82134044

        if table2Version == 134 and indicatorOfParameter == 43:
            return 82134043

        if table2Version == 134 and indicatorOfParameter == 42:
            return 82134042

        if table2Version == 134 and indicatorOfParameter == 41:
            return 82134041

        if table2Version == 134 and indicatorOfParameter == 40:
            return 82134040

        if table2Version == 134 and indicatorOfParameter == 34:
            return 82134034

        if table2Version == 134 and indicatorOfParameter == 33:
            return 82134033

        if table2Version == 134 and indicatorOfParameter == 32:
            return 82134032

        if table2Version == 134 and indicatorOfParameter == 31:
            return 82134031

        if table2Version == 134 and indicatorOfParameter == 30:
            return 82134030

        if table2Version == 134 and indicatorOfParameter == 29:
            return 82134029

        if table2Version == 134 and indicatorOfParameter == 28:
            return 82134028

        if table2Version == 134 and indicatorOfParameter == 27:
            return 82134027

        if table2Version == 134 and indicatorOfParameter == 26:
            return 82134026

        if table2Version == 134 and indicatorOfParameter == 25:
            return 82134025

        if table2Version == 134 and indicatorOfParameter == 24:
            return 82134024

        if table2Version == 134 and indicatorOfParameter == 23:
            return 82134023

        if table2Version == 134 and indicatorOfParameter == 22:
            return 82134022

        if table2Version == 134 and indicatorOfParameter == 21:
            return 82134021

        if table2Version == 134 and indicatorOfParameter == 20:
            return 82134020

        if table2Version == 134 and indicatorOfParameter == 19:
            return 82134019

        if table2Version == 134 and indicatorOfParameter == 15:
            return 82134015

        if table2Version == 134 and indicatorOfParameter == 14:
            return 82134014

        if table2Version == 134 and indicatorOfParameter == 13:
            return 82134013

        if table2Version == 134 and indicatorOfParameter == 12:
            return 82134012

        if table2Version == 134 and indicatorOfParameter == 11:
            return 82134011

        if table2Version == 134 and indicatorOfParameter == 10:
            return 82134010

        if table2Version == 134 and indicatorOfParameter == 9:
            return 82134009

        if table2Version == 134 and indicatorOfParameter == 8:
            return 82134008

        if table2Version == 134 and indicatorOfParameter == 7:
            return 82134007

        if table2Version == 134 and indicatorOfParameter == 6:
            return 82134006

        if table2Version == 134 and indicatorOfParameter == 5:
            return 82134005

        if table2Version == 134 and indicatorOfParameter == 4:
            return 82134004

        if table2Version == 134 and indicatorOfParameter == 3:
            return 82134003

        if table2Version == 134 and indicatorOfParameter == 2:
            return 82134002

        if table2Version == 134 and indicatorOfParameter == 1:
            return 82134001

        if table2Version == 134 and indicatorOfParameter == 0:
            return 82134000

        if table2Version == 133 and indicatorOfParameter == 255:
            return 82133255

        if table2Version == 133 and indicatorOfParameter == 243:
            return 82133243

        if table2Version == 133 and indicatorOfParameter == 239:
            return 82133239

        if table2Version == 133 and indicatorOfParameter == 233:
            return 82133233

        if table2Version == 133 and indicatorOfParameter == 232:
            return 82133232

        if table2Version == 133 and indicatorOfParameter == 231:
            return 82133231

        if table2Version == 133 and indicatorOfParameter == 223:
            return 82133223

        if table2Version == 133 and indicatorOfParameter == 222:
            return 82133222

        if table2Version == 133 and indicatorOfParameter == 221:
            return 82133221

        if table2Version == 133 and indicatorOfParameter == 220:
            return 82133220

        if table2Version == 133 and indicatorOfParameter == 203:
            return 82133203

        if table2Version == 133 and indicatorOfParameter == 202:
            return 82133202

        if table2Version == 133 and indicatorOfParameter == 201:
            return 82133201

        if table2Version == 133 and indicatorOfParameter == 200:
            return 82133200

        if table2Version == 133 and indicatorOfParameter == 166:
            return 82133166

        if table2Version == 133 and indicatorOfParameter == 165:
            return 82133165

        if table2Version == 133 and indicatorOfParameter == 164:
            return 82133164

        if table2Version == 133 and indicatorOfParameter == 163:
            return 82133163

        if table2Version == 133 and indicatorOfParameter == 162:
            return 82133162

        if table2Version == 133 and indicatorOfParameter == 161:
            return 82133161

        if table2Version == 133 and indicatorOfParameter == 160:
            return 82133160

        if table2Version == 133 and indicatorOfParameter == 159:
            return 82133159

        if table2Version == 133 and indicatorOfParameter == 158:
            return 82133158

        if table2Version == 133 and indicatorOfParameter == 157:
            return 82133157

        if table2Version == 133 and indicatorOfParameter == 156:
            return 82133156

        if table2Version == 133 and indicatorOfParameter == 155:
            return 82133155

        if table2Version == 133 and indicatorOfParameter == 154:
            return 82133154

        if table2Version == 133 and indicatorOfParameter == 153:
            return 82133153

        if table2Version == 133 and indicatorOfParameter == 152:
            return 82133152

        if table2Version == 133 and indicatorOfParameter == 151:
            return 82133151

        if table2Version == 133 and indicatorOfParameter == 131:
            return 82133131

        if table2Version == 133 and indicatorOfParameter == 130:
            return 82133130

        if table2Version == 133 and indicatorOfParameter == 113:
            return 82133113

        if table2Version == 133 and indicatorOfParameter == 112:
            return 82133112

        if table2Version == 133 and indicatorOfParameter == 111:
            return 82133111

        if table2Version == 133 and indicatorOfParameter == 110:
            return 82133110

        if table2Version == 133 and indicatorOfParameter == 109:
            return 82133109

        if table2Version == 133 and indicatorOfParameter == 108:
            return 82133108

        if table2Version == 133 and indicatorOfParameter == 107:
            return 82133107

        if table2Version == 133 and indicatorOfParameter == 106:
            return 82133106

        if table2Version == 133 and indicatorOfParameter == 105:
            return 82133105

        if table2Version == 133 and indicatorOfParameter == 104:
            return 82133104

        if table2Version == 133 and indicatorOfParameter == 103:
            return 82133103

        if table2Version == 133 and indicatorOfParameter == 102:
            return 82133102

        if table2Version == 133 and indicatorOfParameter == 101:
            return 82133101

        if table2Version == 133 and indicatorOfParameter == 100:
            return 82133100

        if table2Version == 133 and indicatorOfParameter == 98:
            return 82133098

        if table2Version == 133 and indicatorOfParameter == 97:
            return 82133097

        if table2Version == 133 and indicatorOfParameter == 96:
            return 82133096

        if table2Version == 133 and indicatorOfParameter == 95:
            return 82133095

        if table2Version == 133 and indicatorOfParameter == 94:
            return 82133094

        if table2Version == 133 and indicatorOfParameter == 93:
            return 82133093

        if table2Version == 133 and indicatorOfParameter == 92:
            return 82133092

        if table2Version == 133 and indicatorOfParameter == 91:
            return 82133091

        if table2Version == 133 and indicatorOfParameter == 89:
            return 82133089

        if table2Version == 133 and indicatorOfParameter == 88:
            return 82133088

        if table2Version == 133 and indicatorOfParameter == 82:
            return 82133082

        if table2Version == 133 and indicatorOfParameter == 80:
            return 82133080

        if table2Version == 133 and indicatorOfParameter == 71:
            return 82133071

        if table2Version == 133 and indicatorOfParameter == 70:
            return 82133070

        if table2Version == 133 and indicatorOfParameter == 69:
            return 82133069

        if table2Version == 133 and indicatorOfParameter == 68:
            return 82133068

        if table2Version == 133 and indicatorOfParameter == 67:
            return 82133067

        if table2Version == 133 and indicatorOfParameter == 66:
            return 82133066

        if table2Version == 133 and indicatorOfParameter == 51:
            return 82133051

        if table2Version == 133 and indicatorOfParameter == 50:
            return 82133050

        if table2Version == 133 and indicatorOfParameter == 49:
            return 82133049

        if table2Version == 133 and indicatorOfParameter == 48:
            return 82133048

        if table2Version == 133 and indicatorOfParameter == 47:
            return 82133047

        if table2Version == 133 and indicatorOfParameter == 46:
            return 82133046

        if table2Version == 133 and indicatorOfParameter == 45:
            return 82133045

        if table2Version == 133 and indicatorOfParameter == 44:
            return 82133044

        if table2Version == 133 and indicatorOfParameter == 43:
            return 82133043

        if table2Version == 133 and indicatorOfParameter == 42:
            return 82133042

        if table2Version == 133 and indicatorOfParameter == 41:
            return 82133041

        if table2Version == 133 and indicatorOfParameter == 40:
            return 82133040

        if table2Version == 133 and indicatorOfParameter == 39:
            return 82133039

        if table2Version == 133 and indicatorOfParameter == 38:
            return 82133038

        if table2Version == 133 and indicatorOfParameter == 37:
            return 82133037

        if table2Version == 133 and indicatorOfParameter == 36:
            return 82133036

        if table2Version == 133 and indicatorOfParameter == 35:
            return 82133035

        if table2Version == 133 and indicatorOfParameter == 34:
            return 82133034

        if table2Version == 133 and indicatorOfParameter == 33:
            return 82133033

        if table2Version == 133 and indicatorOfParameter == 32:
            return 82133032

        if table2Version == 133 and indicatorOfParameter == 31:
            return 82133031

        if table2Version == 133 and indicatorOfParameter == 30:
            return 82133030

        if table2Version == 133 and indicatorOfParameter == 29:
            return 82133029

        if table2Version == 133 and indicatorOfParameter == 28:
            return 82133028

        if table2Version == 133 and indicatorOfParameter == 13:
            return 82133013

        if table2Version == 133 and indicatorOfParameter == 11:
            return 82133011

        if table2Version == 133 and indicatorOfParameter == 1:
            return 82133001

        if table2Version == 133 and indicatorOfParameter == 0:
            return 82133000

        if table2Version == 131 and indicatorOfParameter == 255:
            return 82131255

        if table2Version == 131 and indicatorOfParameter == 252:
            return 82131252

        if table2Version == 131 and indicatorOfParameter == 251:
            return 82131251

        if table2Version == 131 and indicatorOfParameter == 250:
            return 82131250

        if table2Version == 131 and indicatorOfParameter == 246:
            return 82131246

        if table2Version == 131 and indicatorOfParameter == 245:
            return 82131245

        if table2Version == 131 and indicatorOfParameter == 244:
            return 82131244

        if table2Version == 131 and indicatorOfParameter == 241:
            return 82131241

        if table2Version == 131 and indicatorOfParameter == 196:
            return 82131196

        if table2Version == 131 and indicatorOfParameter == 183:
            return 82131183

        if table2Version == 131 and indicatorOfParameter == 180:
            return 82131180

        if table2Version == 131 and indicatorOfParameter == 173:
            return 82131173

        if table2Version == 131 and indicatorOfParameter == 172:
            return 82131172

        if table2Version == 131 and indicatorOfParameter == 171:
            return 82131171

        if table2Version == 131 and indicatorOfParameter == 170:
            return 82131170

        if table2Version == 131 and indicatorOfParameter == 164:
            return 82131164

        if table2Version == 131 and indicatorOfParameter == 163:
            return 82131163

        if table2Version == 131 and indicatorOfParameter == 162:
            return 82131162

        if table2Version == 131 and indicatorOfParameter == 161:
            return 82131161

        if table2Version == 131 and indicatorOfParameter == 160:
            return 82131160

        if table2Version == 131 and indicatorOfParameter == 153:
            return 82131153

        if table2Version == 131 and indicatorOfParameter == 152:
            return 82131152

        if table2Version == 131 and indicatorOfParameter == 151:
            return 82131151

        if table2Version == 131 and indicatorOfParameter == 150:
            return 82131150

        if table2Version == 131 and indicatorOfParameter == 92:
            return 82131092

        if table2Version == 131 and indicatorOfParameter == 91:
            return 82131091

        if table2Version == 131 and indicatorOfParameter == 66:
            return 82131066

        if table2Version == 131 and indicatorOfParameter == 50:
            return 82131050

        if table2Version == 131 and indicatorOfParameter == 49:
            return 82131049

        if table2Version == 131 and indicatorOfParameter == 11:
            return 82131011

        if table2Version == 131 and indicatorOfParameter == 0:
            return 82131000

        if table2Version == 130 and indicatorOfParameter == 255:
            return 82130255

        if table2Version == 130 and indicatorOfParameter == 149:
            return 82130149

        if table2Version == 130 and indicatorOfParameter == 148:
            return 82130148

        if table2Version == 130 and indicatorOfParameter == 147:
            return 82130147

        if table2Version == 130 and indicatorOfParameter == 146:
            return 82130146

        if table2Version == 130 and indicatorOfParameter == 145:
            return 82130145

        if table2Version == 130 and indicatorOfParameter == 143:
            return 82130143

        if table2Version == 130 and indicatorOfParameter == 142:
            return 82130142

        if table2Version == 130 and indicatorOfParameter == 141:
            return 82130141

        if table2Version == 130 and indicatorOfParameter == 140:
            return 82130140

        if table2Version == 130 and indicatorOfParameter == 139:
            return 82130139

        if table2Version == 130 and indicatorOfParameter == 138:
            return 82130138

        if table2Version == 130 and indicatorOfParameter == 137:
            return 82130137

        if table2Version == 130 and indicatorOfParameter == 136:
            return 82130136

        if table2Version == 130 and indicatorOfParameter == 135:
            return 82130135

        if table2Version == 130 and indicatorOfParameter == 131:
            return 82130131

        if table2Version == 130 and indicatorOfParameter == 130:
            return 82130130

        if table2Version == 130 and indicatorOfParameter == 111:
            return 82130111

        if table2Version == 130 and indicatorOfParameter == 110:
            return 82130110

        if table2Version == 130 and indicatorOfParameter == 100:
            return 82130100

        if table2Version == 130 and indicatorOfParameter == 77:
            return 82130077

        if table2Version == 130 and indicatorOfParameter == 75:
            return 82130075

        if table2Version == 130 and indicatorOfParameter == 74:
            return 82130074

        if table2Version == 130 and indicatorOfParameter == 73:
            return 82130073

        if table2Version == 130 and indicatorOfParameter == 72:
            return 82130072

        if table2Version == 130 and indicatorOfParameter == 71:
            return 82130071

        if table2Version == 130 and indicatorOfParameter == 70:
            return 82130070

        if table2Version == 130 and indicatorOfParameter == 69:
            return 82130069

        if table2Version == 130 and indicatorOfParameter == 68:
            return 82130068

        if table2Version == 130 and indicatorOfParameter == 67:
            return 82130067

        if table2Version == 130 and indicatorOfParameter == 65:
            return 82130065

        if table2Version == 130 and indicatorOfParameter == 61:
            return 82130061

        if table2Version == 130 and indicatorOfParameter == 60:
            return 82130060

        if table2Version == 130 and indicatorOfParameter == 58:
            return 82130058

        if table2Version == 130 and indicatorOfParameter == 52:
            return 82130052

        if table2Version == 130 and indicatorOfParameter == 34:
            return 82130034

        if table2Version == 130 and indicatorOfParameter == 33:
            return 82130033

        if table2Version == 130 and indicatorOfParameter == 20:
            return 82130020

        if table2Version == 130 and indicatorOfParameter == 11:
            return 82130011

        if table2Version == 130 and indicatorOfParameter == 1:
            return 82130001

        if table2Version == 130 and indicatorOfParameter == 0:
            return 82130000

        if table2Version == 129 and indicatorOfParameter == 255:
            return 82129255

        if table2Version == 129 and indicatorOfParameter == 239:
            return 82129239

        if table2Version == 129 and indicatorOfParameter == 238:
            return 82129238

        if table2Version == 129 and indicatorOfParameter == 237:
            return 82129237

        if table2Version == 129 and indicatorOfParameter == 236:
            return 82129236

        if table2Version == 129 and indicatorOfParameter == 235:
            return 82129235

        if table2Version == 129 and indicatorOfParameter == 234:
            return 82129234

        if table2Version == 129 and indicatorOfParameter == 233:
            return 82129233

        if table2Version == 129 and indicatorOfParameter == 232:
            return 82129232

        if table2Version == 129 and indicatorOfParameter == 231:
            return 82129231

        if table2Version == 129 and indicatorOfParameter == 229:
            return 82129229

        if table2Version == 129 and indicatorOfParameter == 228:
            return 82129228

        if table2Version == 129 and indicatorOfParameter == 227:
            return 82129227

        if table2Version == 129 and indicatorOfParameter == 226:
            return 82129226

        if table2Version == 129 and indicatorOfParameter == 225:
            return 82129225

        if table2Version == 129 and indicatorOfParameter == 224:
            return 82129224

        if table2Version == 129 and indicatorOfParameter == 223:
            return 82129223

        if table2Version == 129 and indicatorOfParameter == 222:
            return 82129222

        if table2Version == 129 and indicatorOfParameter == 221:
            return 82129221

        if table2Version == 129 and indicatorOfParameter == 219:
            return 82129219

        if table2Version == 129 and indicatorOfParameter == 218:
            return 82129218

        if table2Version == 129 and indicatorOfParameter == 217:
            return 82129217

        if table2Version == 129 and indicatorOfParameter == 216:
            return 82129216

        if table2Version == 129 and indicatorOfParameter == 215:
            return 82129215

        if table2Version == 129 and indicatorOfParameter == 214:
            return 82129214

        if table2Version == 129 and indicatorOfParameter == 213:
            return 82129213

        if table2Version == 129 and indicatorOfParameter == 212:
            return 82129212

        if table2Version == 129 and indicatorOfParameter == 211:
            return 82129211

        if table2Version == 129 and indicatorOfParameter == 209:
            return 82129209

        if table2Version == 129 and indicatorOfParameter == 208:
            return 82129208

        if table2Version == 129 and indicatorOfParameter == 207:
            return 82129207

        if table2Version == 129 and indicatorOfParameter == 206:
            return 82129206

        if table2Version == 129 and indicatorOfParameter == 205:
            return 82129205

        if table2Version == 129 and indicatorOfParameter == 204:
            return 82129204

        if table2Version == 129 and indicatorOfParameter == 203:
            return 82129203

        if table2Version == 129 and indicatorOfParameter == 202:
            return 82129202

        if table2Version == 129 and indicatorOfParameter == 201:
            return 82129201

        if table2Version == 129 and indicatorOfParameter == 199:
            return 82129199

        if table2Version == 129 and indicatorOfParameter == 198:
            return 82129198

        if table2Version == 129 and indicatorOfParameter == 197:
            return 82129197

        if table2Version == 129 and indicatorOfParameter == 196:
            return 82129196

        if table2Version == 129 and indicatorOfParameter == 195:
            return 82129195

        if table2Version == 129 and indicatorOfParameter == 194:
            return 82129194

        if table2Version == 129 and indicatorOfParameter == 193:
            return 82129193

        if table2Version == 129 and indicatorOfParameter == 192:
            return 82129192

        if table2Version == 129 and indicatorOfParameter == 191:
            return 82129191

        if table2Version == 129 and indicatorOfParameter == 189:
            return 82129189

        if table2Version == 129 and indicatorOfParameter == 188:
            return 82129188

        if table2Version == 129 and indicatorOfParameter == 187:
            return 82129187

        if table2Version == 129 and indicatorOfParameter == 186:
            return 82129186

        if table2Version == 129 and indicatorOfParameter == 185:
            return 82129185

        if table2Version == 129 and indicatorOfParameter == 184:
            return 82129184

        if table2Version == 129 and indicatorOfParameter == 183:
            return 82129183

        if table2Version == 129 and indicatorOfParameter == 182:
            return 82129182

        if table2Version == 129 and indicatorOfParameter == 181:
            return 82129181

        if table2Version == 129 and indicatorOfParameter == 179:
            return 82129179

        if table2Version == 129 and indicatorOfParameter == 178:
            return 82129178

        if table2Version == 129 and indicatorOfParameter == 177:
            return 82129177

        if table2Version == 129 and indicatorOfParameter == 176:
            return 82129176

        if table2Version == 129 and indicatorOfParameter == 175:
            return 82129175

        if table2Version == 129 and indicatorOfParameter == 174:
            return 82129174

        if table2Version == 129 and indicatorOfParameter == 173:
            return 82129173

        if table2Version == 129 and indicatorOfParameter == 172:
            return 82129172

        if table2Version == 129 and indicatorOfParameter == 171:
            return 82129171

        if table2Version == 129 and indicatorOfParameter == 169:
            return 82129169

        if table2Version == 129 and indicatorOfParameter == 168:
            return 82129168

        if table2Version == 129 and indicatorOfParameter == 167:
            return 82129167

        if table2Version == 129 and indicatorOfParameter == 166:
            return 82129166

        if table2Version == 129 and indicatorOfParameter == 165:
            return 82129165

        if table2Version == 129 and indicatorOfParameter == 164:
            return 82129164

        if table2Version == 129 and indicatorOfParameter == 163:
            return 82129163

        if table2Version == 129 and indicatorOfParameter == 162:
            return 82129162

        if table2Version == 129 and indicatorOfParameter == 161:
            return 82129161

        if table2Version == 129 and indicatorOfParameter == 146:
            return 82129146

        if table2Version == 129 and indicatorOfParameter == 145:
            return 82129145

        if table2Version == 129 and indicatorOfParameter == 79:
            return 82129079

        if table2Version == 129 and indicatorOfParameter == 78:
            return 82129078

        if table2Version == 129 and indicatorOfParameter == 77:
            return 82129077

        if table2Version == 129 and indicatorOfParameter == 75:
            return 82129075

        if table2Version == 129 and indicatorOfParameter == 74:
            return 82129074

        if table2Version == 129 and indicatorOfParameter == 73:
            return 82129073

        if table2Version == 129 and indicatorOfParameter == 71:
            return 82129071

        if table2Version == 129 and indicatorOfParameter == 52:
            return 82129052

        if table2Version == 129 and indicatorOfParameter == 34:
            return 82129034

        if table2Version == 129 and indicatorOfParameter == 33:
            return 82129033

        if table2Version == 129 and indicatorOfParameter == 32:
            return 82129032

        if table2Version == 129 and indicatorOfParameter == 20:
            return 82129020

        if table2Version == 129 and indicatorOfParameter == 16:
            return 82129016

        if table2Version == 129 and indicatorOfParameter == 15:
            return 82129015

        if table2Version == 129 and indicatorOfParameter == 13:
            return 82129013

        if table2Version == 129 and indicatorOfParameter == 12:
            return 82129012

        if table2Version == 129 and indicatorOfParameter == 11:
            return 82129011

        if table2Version == 129 and indicatorOfParameter == 1:
            return 82129001

        if table2Version == 129 and indicatorOfParameter == 0:
            return 82129000

        if table2Version == 128 and indicatorOfParameter == 255:
            return 82128255

        if table2Version == 128 and indicatorOfParameter == 242:
            return 82128242

        if table2Version == 128 and indicatorOfParameter == 241:
            return 82128241

        if table2Version == 128 and indicatorOfParameter == 240:
            return 82128240

        if table2Version == 128 and indicatorOfParameter == 223:
            return 82128223

        if table2Version == 128 and indicatorOfParameter == 222:
            return 82128222

        if table2Version == 128 and indicatorOfParameter == 221:
            return 82128221

        if table2Version == 128 and indicatorOfParameter == 220:
            return 82128220

        if table2Version == 128 and indicatorOfParameter == 219:
            return 82128219

        if table2Version == 128 and indicatorOfParameter == 218:
            return 82128218

        if table2Version == 128 and indicatorOfParameter == 217:
            return 82128217

        if table2Version == 128 and indicatorOfParameter == 216:
            return 82128216

        if table2Version == 128 and indicatorOfParameter == 215:
            return 82128215

        if table2Version == 128 and indicatorOfParameter == 214:
            return 82128214

        if table2Version == 128 and indicatorOfParameter == 213:
            return 82128213

        if table2Version == 128 and indicatorOfParameter == 212:
            return 82128212

        if table2Version == 128 and indicatorOfParameter == 211:
            return 82128211

        if table2Version == 128 and indicatorOfParameter == 210:
            return 82128210

        if table2Version == 128 and indicatorOfParameter == 204:
            return 82128204

        if table2Version == 128 and indicatorOfParameter == 203:
            return 82128203

        if table2Version == 128 and indicatorOfParameter == 202:
            return 82128202

        if table2Version == 128 and indicatorOfParameter == 201:
            return 82128201

        if table2Version == 128 and indicatorOfParameter == 200:
            return 82128200

        if table2Version == 128 and indicatorOfParameter == 180:
            return 82128180

        if table2Version == 128 and indicatorOfParameter == 175:
            return 82128175

        if table2Version == 128 and indicatorOfParameter == 174:
            return 82128174

        if table2Version == 128 and indicatorOfParameter == 173:
            return 82128173

        if table2Version == 128 and indicatorOfParameter == 172:
            return 82128172

        if table2Version == 128 and indicatorOfParameter == 171:
            return 82128171

        if table2Version == 128 and indicatorOfParameter == 170:
            return 82128170

        if table2Version == 128 and indicatorOfParameter == 169:
            return 82128169

        if table2Version == 128 and indicatorOfParameter == 168:
            return 82128168

        if table2Version == 128 and indicatorOfParameter == 167:
            return 82128167

        if table2Version == 128 and indicatorOfParameter == 166:
            return 82128166

        if table2Version == 128 and indicatorOfParameter == 165:
            return 82128165

        if table2Version == 128 and indicatorOfParameter == 164:
            return 82128164

        if table2Version == 128 and indicatorOfParameter == 163:
            return 82128163

        if table2Version == 128 and indicatorOfParameter == 162:
            return 82128162

        if table2Version == 128 and indicatorOfParameter == 161:
            return 82128161

        if table2Version == 128 and indicatorOfParameter == 160:
            return 82128160

        if table2Version == 128 and indicatorOfParameter == 140:
            return 82128140

        if table2Version == 128 and indicatorOfParameter == 128:
            return 82128128

        if table2Version == 128 and indicatorOfParameter == 126:
            return 82128126

        if table2Version == 128 and indicatorOfParameter == 125:
            return 82128125

        if table2Version == 128 and indicatorOfParameter == 124:
            return 82128124

        if table2Version == 128 and indicatorOfParameter == 123:
            return 82128123

        if table2Version == 128 and indicatorOfParameter == 122:
            return 82128122

        if table2Version == 128 and indicatorOfParameter == 121:
            return 82128121

        if table2Version == 128 and indicatorOfParameter == 120:
            return 82128120

        if table2Version == 128 and indicatorOfParameter == 119:
            return 82128119

        if table2Version == 128 and indicatorOfParameter == 116:
            return 82128116

        if table2Version == 128 and indicatorOfParameter == 115:
            return 82128115

        if table2Version == 128 and indicatorOfParameter == 114:
            return 82128114

        if table2Version == 128 and indicatorOfParameter == 113:
            return 82128113

        if table2Version == 128 and indicatorOfParameter == 112:
            return 82128112

        if table2Version == 128 and indicatorOfParameter == 111:
            return 82128111

        if table2Version == 128 and indicatorOfParameter == 110:
            return 82128110

        if table2Version == 128 and indicatorOfParameter == 108:
            return 82128108

        if table2Version == 128 and indicatorOfParameter == 106:
            return 82128106

        if table2Version == 128 and indicatorOfParameter == 105:
            return 82128105

        if table2Version == 128 and indicatorOfParameter == 104:
            return 82128104

        if table2Version == 128 and indicatorOfParameter == 103:
            return 82128103

        if table2Version == 128 and indicatorOfParameter == 102:
            return 82128102

        if table2Version == 128 and indicatorOfParameter == 101:
            return 82128101

        if table2Version == 128 and indicatorOfParameter == 100:
            return 82128100

        if table2Version == 128 and indicatorOfParameter == 98:
            return 82128098

        if table2Version == 128 and indicatorOfParameter == 97:
            return 82128097

        if table2Version == 128 and indicatorOfParameter == 96:
            return 82128096

        if table2Version == 128 and indicatorOfParameter == 95:
            return 82128095

        if table2Version == 128 and indicatorOfParameter == 93:
            return 82128093

        if table2Version == 128 and indicatorOfParameter == 92:
            return 82128092

        if table2Version == 128 and indicatorOfParameter == 91:
            return 82128091

        if table2Version == 128 and indicatorOfParameter == 88:
            return 82128088

        if table2Version == 128 and indicatorOfParameter == 87:
            return 82128087

        if table2Version == 128 and indicatorOfParameter == 86:
            return 82128086

        if table2Version == 128 and indicatorOfParameter == 85:
            return 82128085

        if table2Version == 128 and indicatorOfParameter == 84:
            return 82128084

        if table2Version == 128 and indicatorOfParameter == 83:
            return 82128083

        if table2Version == 128 and indicatorOfParameter == 82:
            return 82128082

        if table2Version == 128 and indicatorOfParameter == 81:
            return 82128081

        if table2Version == 128 and indicatorOfParameter == 80:
            return 82128080

        if table2Version == 128 and indicatorOfParameter == 75:
            return 82128075

        if table2Version == 128 and indicatorOfParameter == 74:
            return 82128074

        if table2Version == 128 and indicatorOfParameter == 73:
            return 82128073

        if table2Version == 128 and indicatorOfParameter == 72:
            return 82128072

        if table2Version == 128 and indicatorOfParameter == 71:
            return 82128071

        if table2Version == 128 and indicatorOfParameter == 70:
            return 82128070

        if table2Version == 128 and indicatorOfParameter == 65:
            return 82128065

        if table2Version == 128 and indicatorOfParameter == 64:
            return 82128064

        if table2Version == 128 and indicatorOfParameter == 63:
            return 82128063

        if table2Version == 128 and indicatorOfParameter == 62:
            return 82128062

        if table2Version == 128 and indicatorOfParameter == 61:
            return 82128061

        if table2Version == 128 and indicatorOfParameter == 60:
            return 82128060

        if table2Version == 128 and indicatorOfParameter == 59:
            return 82128059

        if table2Version == 128 and indicatorOfParameter == 58:
            return 82128058

        if table2Version == 128 and indicatorOfParameter == 57:
            return 82128057

        if table2Version == 128 and indicatorOfParameter == 56:
            return 82128056

        if table2Version == 128 and indicatorOfParameter == 55:
            return 82128055

        if table2Version == 128 and indicatorOfParameter == 54:
            return 82128054

        if table2Version == 128 and indicatorOfParameter == 52:
            return 82128052

        if table2Version == 128 and indicatorOfParameter == 51:
            return 82128051

        if table2Version == 128 and indicatorOfParameter == 50:
            return 82128050

        if table2Version == 128 and indicatorOfParameter == 49:
            return 82128049

        if table2Version == 128 and indicatorOfParameter == 48:
            return 82128048

        if table2Version == 128 and indicatorOfParameter == 47:
            return 82128047

        if table2Version == 128 and indicatorOfParameter == 46:
            return 82128046

        if table2Version == 128 and indicatorOfParameter == 45:
            return 82128045

        if table2Version == 128 and indicatorOfParameter == 44:
            return 82128044

        if table2Version == 128 and indicatorOfParameter == 43:
            return 82128043

        if table2Version == 128 and indicatorOfParameter == 42:
            return 82128042

        if table2Version == 128 and indicatorOfParameter == 41:
            return 82128041

        if table2Version == 128 and indicatorOfParameter == 40:
            return 82128040

        if table2Version == 128 and indicatorOfParameter == 39:
            return 82128039

        if table2Version == 128 and indicatorOfParameter == 38:
            return 82128038

        if table2Version == 128 and indicatorOfParameter == 37:
            return 82128037

        if table2Version == 128 and indicatorOfParameter == 36:
            return 82128036

        if table2Version == 128 and indicatorOfParameter == 35:
            return 82128035

        if table2Version == 128 and indicatorOfParameter == 34:
            return 82128034

        if table2Version == 128 and indicatorOfParameter == 33:
            return 82128033

        if table2Version == 128 and indicatorOfParameter == 32:
            return 82128032

        if table2Version == 128 and indicatorOfParameter == 31:
            return 82128031

        if table2Version == 128 and indicatorOfParameter == 30:
            return 82128030

        if table2Version == 128 and indicatorOfParameter == 29:
            return 82128029

        if table2Version == 128 and indicatorOfParameter == 28:
            return 82128028

        if table2Version == 128 and indicatorOfParameter == 27:
            return 82128027

        if table2Version == 128 and indicatorOfParameter == 26:
            return 82128026

        if table2Version == 128 and indicatorOfParameter == 25:
            return 82128025

        if table2Version == 128 and indicatorOfParameter == 24:
            return 82128024

        if table2Version == 128 and indicatorOfParameter == 23:
            return 82128023

        if table2Version == 128 and indicatorOfParameter == 11:
            return 82128011

        if table2Version == 128 and indicatorOfParameter == 10:
            return 82128010

        if table2Version == 128 and indicatorOfParameter == 9:
            return 82128009

        if table2Version == 128 and indicatorOfParameter == 8:
            return 82128008

        if table2Version == 128 and indicatorOfParameter == 7:
            return 82128007

        if table2Version == 128 and indicatorOfParameter == 6:
            return 82128006

        if table2Version == 128 and indicatorOfParameter == 5:
            return 82128005

        if table2Version == 128 and indicatorOfParameter == 4:
            return 82128004

        if table2Version == 128 and indicatorOfParameter == 3:
            return 82128003

        if table2Version == 128 and indicatorOfParameter == 2:
            return 82128002

        if table2Version == 128 and indicatorOfParameter == 1:
            return 82128001

        if table2Version == 128 and indicatorOfParameter == 0:
            return 82128000

        if table2Version == 1 and indicatorOfParameter == 255:
            return 82001255

        if table2Version == 1 and indicatorOfParameter == 251:
            return 82001251

        if table2Version == 1 and indicatorOfParameter == 250:
            return 82001250

        if table2Version == 1 and indicatorOfParameter == 228:
            return 82001228

        if table2Version == 1 and indicatorOfParameter == 227:
            return 82001227

        if table2Version == 1 and indicatorOfParameter == 226:
            return 82001226

        if table2Version == 1 and indicatorOfParameter == 225:
            return 82001225

        if table2Version == 1 and indicatorOfParameter == 224:
            return 82001224

        if table2Version == 1 and indicatorOfParameter == 223:
            return 82001223

        if table2Version == 1 and indicatorOfParameter == 222:
            return 82001222

        if table2Version == 1 and indicatorOfParameter == 210:
            return 82001210

        if table2Version == 1 and indicatorOfParameter == 209:
            return 82001209

        if table2Version == 1 and indicatorOfParameter == 208:
            return 82001208

        if table2Version == 1 and indicatorOfParameter == 206:
            return 82001206

        if table2Version == 1 and indicatorOfParameter == 205:
            return 82001205

        if table2Version == 1 and indicatorOfParameter == 204:
            return 82001204

        if table2Version == 1 and indicatorOfParameter == 200:
            return 82001200

        if table2Version == 1 and indicatorOfParameter == 199:
            return 82001199

        if table2Version == 1 and indicatorOfParameter == 198:
            return 82001198

        if table2Version == 1 and indicatorOfParameter == 197:
            return 82001197

        if table2Version == 1 and indicatorOfParameter == 196:
            return 82001196

        if table2Version == 1 and indicatorOfParameter == 195:
            return 82001195

        if table2Version == 1 and indicatorOfParameter == 194:
            return 82001194

        if table2Version == 1 and indicatorOfParameter == 193:
            return 82001193

        if table2Version == 1 and indicatorOfParameter == 192:
            return 82001192

        if table2Version == 1 and indicatorOfParameter == 191:
            return 82001191

        if table2Version == 1 and indicatorOfParameter == 190:
            return 82001190

        if table2Version == 1 and indicatorOfParameter == 189:
            return 82001189

        if table2Version == 1 and indicatorOfParameter == 169:
            return 82001169

        if table2Version == 1 and indicatorOfParameter == 168:
            return 82001168

        if table2Version == 1 and indicatorOfParameter == 167:
            return 82001167

        if table2Version == 1 and indicatorOfParameter == 166:
            return 82001166

        if table2Version == 1 and indicatorOfParameter == 165:
            return 82001165

        if table2Version == 1 and indicatorOfParameter == 164:
            return 82001164

        if table2Version == 1 and indicatorOfParameter == 163:
            return 82001163

        if table2Version == 1 and indicatorOfParameter == 162:
            return 82001162

        if table2Version == 1 and indicatorOfParameter == 161:
            return 82001161

        if table2Version == 1 and indicatorOfParameter == 160:
            return 82001160

        if table2Version == 1 and indicatorOfParameter == 143:
            return 82001143

        if table2Version == 1 and indicatorOfParameter == 142:
            return 82001142

        if table2Version == 1 and indicatorOfParameter == 141:
            return 82001141

        if table2Version == 1 and indicatorOfParameter == 140:
            return 82001140

        if table2Version == 1 and indicatorOfParameter == 139:
            return 82001139

        if table2Version == 1 and indicatorOfParameter == 138:
            return 82001138

        if table2Version == 1 and indicatorOfParameter == 137:
            return 82001137

        if table2Version == 1 and indicatorOfParameter == 136:
            return 82001136

        if table2Version == 1 and indicatorOfParameter == 135:
            return 82001135

        if table2Version == 1 and indicatorOfParameter == 134:
            return 82001134

        if table2Version == 1 and indicatorOfParameter == 133:
            return 82001133

        if table2Version == 1 and indicatorOfParameter == 132:
            return 82001132

        if table2Version == 1 and indicatorOfParameter == 131:
            return 82001131

        if table2Version == 1 and indicatorOfParameter == 130:
            return 82001130

        if table2Version == 1 and indicatorOfParameter == 129:
            return 82001129

        if table2Version == 1 and indicatorOfParameter == 128:
            return 82001128

        if table2Version == 1 and indicatorOfParameter == 127:
            return 82001127

        if table2Version == 1 and indicatorOfParameter == 126:
            return 82001126

        if table2Version == 1 and indicatorOfParameter == 125:
            return 82001125

        if table2Version == 1 and indicatorOfParameter == 124:
            return 82001124

        if table2Version == 1 and indicatorOfParameter == 123:
            return 82001123

        if table2Version == 1 and indicatorOfParameter == 122:
            return 82001122

        if table2Version == 1 and indicatorOfParameter == 121:
            return 82001121

        if table2Version == 1 and indicatorOfParameter == 120:
            return 82001120

        if table2Version == 1 and indicatorOfParameter == 119:
            return 82001119

        if table2Version == 1 and indicatorOfParameter == 118:
            return 82001118

        if table2Version == 1 and indicatorOfParameter == 117:
            return 82001117

        if table2Version == 1 and indicatorOfParameter == 116:
            return 82001116

        if table2Version == 1 and indicatorOfParameter == 115:
            return 82001115

        if table2Version == 1 and indicatorOfParameter == 114:
            return 82001114

        if table2Version == 1 and indicatorOfParameter == 113:
            return 82001113

        if table2Version == 1 and indicatorOfParameter == 112:
            return 82001112

        if table2Version == 1 and indicatorOfParameter == 111:
            return 82001111

        if table2Version == 1 and indicatorOfParameter == 110:
            return 82001110

        if table2Version == 1 and indicatorOfParameter == 109:
            return 82001109

        if table2Version == 1 and indicatorOfParameter == 108:
            return 82001108

        if table2Version == 1 and indicatorOfParameter == 107:
            return 82001107

        if table2Version == 1 and indicatorOfParameter == 106:
            return 82001106

        if table2Version == 1 and indicatorOfParameter == 105:
            return 82001105

        if table2Version == 1 and indicatorOfParameter == 104:
            return 82001104

        if table2Version == 1 and indicatorOfParameter == 103:
            return 82001103

        if table2Version == 1 and indicatorOfParameter == 102:
            return 82001102

        if table2Version == 1 and indicatorOfParameter == 101:
            return 82001101

        if table2Version == 1 and indicatorOfParameter == 100:
            return 82001100

        if table2Version == 1 and indicatorOfParameter == 99:
            return 82001099

        if table2Version == 1 and indicatorOfParameter == 98:
            return 82001098

        if table2Version == 1 and indicatorOfParameter == 97:
            return 82001097

        if table2Version == 1 and indicatorOfParameter == 96:
            return 82001096

        if table2Version == 1 and indicatorOfParameter == 95:
            return 82001095

        if table2Version == 1 and indicatorOfParameter == 94:
            return 82001094

        if table2Version == 1 and indicatorOfParameter == 93:
            return 82001093

        if table2Version == 1 and indicatorOfParameter == 92:
            return 82001092

        if table2Version == 1 and indicatorOfParameter == 91:
            return 82001091

        if table2Version == 1 and indicatorOfParameter == 90:
            return 82001090

        if table2Version == 1 and indicatorOfParameter == 89:
            return 82001089

        if table2Version == 1 and indicatorOfParameter == 88:
            return 82001088

        if table2Version == 1 and indicatorOfParameter == 87:
            return 82001087

        if table2Version == 1 and indicatorOfParameter == 86:
            return 82001086

        if table2Version == 1 and indicatorOfParameter == 85:
            return 82001085

        if table2Version == 1 and indicatorOfParameter == 84:
            return 82001084

        if table2Version == 1 and indicatorOfParameter == 83:
            return 82001083

        if table2Version == 1 and indicatorOfParameter == 82:
            return 82001082

        if table2Version == 1 and indicatorOfParameter == 81:
            return 82001081

        if table2Version == 1 and indicatorOfParameter == 80:
            return 82001080

        if table2Version == 1 and indicatorOfParameter == 79:
            return 82001079

        if table2Version == 1 and indicatorOfParameter == 78:
            return 82001078

        if table2Version == 1 and indicatorOfParameter == 77:
            return 82001077

        if table2Version == 1 and indicatorOfParameter == 76:
            return 82001076

        if table2Version == 1 and indicatorOfParameter == 75:
            return 82001075

        if table2Version == 1 and indicatorOfParameter == 74:
            return 82001074

        if table2Version == 1 and indicatorOfParameter == 73:
            return 82001073

        if table2Version == 1 and indicatorOfParameter == 72:
            return 82001072

        if table2Version == 1 and indicatorOfParameter == 71:
            return 82001071

        if table2Version == 1 and indicatorOfParameter == 70:
            return 82001070

        if table2Version == 1 and indicatorOfParameter == 69:
            return 82001069

        if table2Version == 1 and indicatorOfParameter == 68:
            return 82001068

        if table2Version == 1 and indicatorOfParameter == 67:
            return 82001067

        if table2Version == 1 and indicatorOfParameter == 66:
            return 82001066

        if table2Version == 1 and indicatorOfParameter == 65:
            return 82001065

        if table2Version == 1 and indicatorOfParameter == 64:
            return 82001064

        if table2Version == 1 and indicatorOfParameter == 63:
            return 82001063

        if table2Version == 1 and indicatorOfParameter == 62:
            return 82001062

        if table2Version == 1 and indicatorOfParameter == 61:
            return 82001061

        if table2Version == 1 and indicatorOfParameter == 60:
            return 82001060

        if table2Version == 1 and indicatorOfParameter == 59:
            return 82001059

        if table2Version == 1 and indicatorOfParameter == 58:
            return 82001058

        if table2Version == 1 and indicatorOfParameter == 57:
            return 82001057

        if table2Version == 1 and indicatorOfParameter == 56:
            return 82001056

        if table2Version == 1 and indicatorOfParameter == 55:
            return 82001055

        if table2Version == 1 and indicatorOfParameter == 54:
            return 82001054

        if table2Version == 1 and indicatorOfParameter == 53:
            return 82001053

        if table2Version == 1 and indicatorOfParameter == 52:
            return 82001052

        if table2Version == 1 and indicatorOfParameter == 51:
            return 82001051

        if table2Version == 1 and indicatorOfParameter == 50:
            return 82001050

        if table2Version == 1 and indicatorOfParameter == 49:
            return 82001049

        if table2Version == 1 and indicatorOfParameter == 48:
            return 82001048

        if table2Version == 1 and indicatorOfParameter == 47:
            return 82001047

        if table2Version == 1 and indicatorOfParameter == 46:
            return 82001046

        if table2Version == 1 and indicatorOfParameter == 45:
            return 82001045

        if table2Version == 1 and indicatorOfParameter == 44:
            return 82001044

        if table2Version == 1 and indicatorOfParameter == 43:
            return 82001043

        if table2Version == 1 and indicatorOfParameter == 42:
            return 82001042

        if table2Version == 1 and indicatorOfParameter == 41:
            return 82001041

        if table2Version == 1 and indicatorOfParameter == 40:
            return 82001040

        if table2Version == 1 and indicatorOfParameter == 39:
            return 82001039

        if table2Version == 1 and indicatorOfParameter == 38:
            return 82001038

        if table2Version == 1 and indicatorOfParameter == 37:
            return 82001037

        if table2Version == 1 and indicatorOfParameter == 36:
            return 82001036

        if table2Version == 1 and indicatorOfParameter == 35:
            return 82001035

        if table2Version == 1 and indicatorOfParameter == 34:
            return 82001034

        if table2Version == 1 and indicatorOfParameter == 33:
            return 82001033

        if table2Version == 1 and indicatorOfParameter == 32:
            return 82001032

        if table2Version == 1 and indicatorOfParameter == 31:
            return 82001031

        if table2Version == 1 and indicatorOfParameter == 30:
            return 82001030

        if table2Version == 1 and indicatorOfParameter == 29:
            return 82001029

        if table2Version == 1 and indicatorOfParameter == 28:
            return 82001028

        if table2Version == 1 and indicatorOfParameter == 27:
            return 82001027

        if table2Version == 1 and indicatorOfParameter == 26:
            return 82001026

        if table2Version == 1 and indicatorOfParameter == 25:
            return 82001025

        if table2Version == 1 and indicatorOfParameter == 24:
            return 82001024

        if table2Version == 1 and indicatorOfParameter == 23:
            return 82001023

        if table2Version == 1 and indicatorOfParameter == 22:
            return 82001022

        if table2Version == 1 and indicatorOfParameter == 21:
            return 82001021

        if table2Version == 1 and indicatorOfParameter == 20:
            return 82001020

        if table2Version == 1 and indicatorOfParameter == 19:
            return 82001019

        if table2Version == 1 and indicatorOfParameter == 18:
            return 82001018

        if table2Version == 1 and indicatorOfParameter == 17:
            return 82001017

        if table2Version == 1 and indicatorOfParameter == 16:
            return 82001016

        if table2Version == 1 and indicatorOfParameter == 15:
            return 82001015

        if table2Version == 1 and indicatorOfParameter == 14:
            return 82001014

        if table2Version == 1 and indicatorOfParameter == 13:
            return 82001013

        if table2Version == 1 and indicatorOfParameter == 12:
            return 82001012

        if table2Version == 1 and indicatorOfParameter == 11:
            return 82001011

        if table2Version == 1 and indicatorOfParameter == 10:
            return 82001010

        if table2Version == 1 and indicatorOfParameter == 9:
            return 82001009

        if table2Version == 1 and indicatorOfParameter == 8:
            return 82001008

        if table2Version == 1 and indicatorOfParameter == 7:
            return 82001007

        if table2Version == 1 and indicatorOfParameter == 6:
            return 82001006

        if table2Version == 1 and indicatorOfParameter == 5:
            return 82001005

        if table2Version == 1 and indicatorOfParameter == 4:
            return 82001004

        if table2Version == 1 and indicatorOfParameter == 3:
            return 82001003

        if table2Version == 1 and indicatorOfParameter == 2:
            return 82001002

        if table2Version == 1 and indicatorOfParameter == 1:
            return 82001001

        if table2Version == 1 and indicatorOfParameter == 0:
            return 82001000

    return wrapped
