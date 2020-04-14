import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 253 and indicatorOfParameter == 228:
            return 'FFG-MS'

        if table2Version == 253 and indicatorOfParameter == 210:
            return 'REFLTY-DBZ'

        if table2Version == 253 and indicatorOfParameter == 209:
            return 'FL-MPLTY-N'

        if table2Version == 253 and indicatorOfParameter == 204:
            return 'RRH-KGM2'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'GRI-KGM2'

        if table2Version == 253 and indicatorOfParameter == 201:
            return 'GR-KGM2'

        if table2Version == 253 and indicatorOfParameter == 200:
            return 'TKEN-JKG'

        if table2Version == 253 and indicatorOfParameter == 187:
            return 'CLDTOP-M'

        if table2Version == 253 and indicatorOfParameter == 186:
            return 'CLDBASE-M'

        if table2Version == 253 and indicatorOfParameter == 185:
            return 'RRS-KGM2'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'SNRI-KGM2'

        if table2Version == 253 and indicatorOfParameter == 184:
            return 'SNACC-KGM2'

        if table2Version == 253 and indicatorOfParameter == 181:
            return 'RRI-KGM2'

        if table2Version == 253 and indicatorOfParameter == 163:
            return 'WGV-MS'

        if table2Version == 253 and indicatorOfParameter == 162:
            return 'WGU-MS'

        if table2Version == 253 and indicatorOfParameter == 160:
            return 'CAPE-JKG'

        if table2Version == 253 and indicatorOfParameter == 144:
            return 'PRECTYPE-N'

        if table2Version == 253 and indicatorOfParameter == 135:
            return 'ICINGWARN-N'

        if table2Version == 253 and indicatorOfParameter == 125:
            return 'VFLMOM-NM2'

        if table2Version == 253 and indicatorOfParameter == 124:
            return 'UFLMOM-NM2'

        if table2Version == 253 and indicatorOfParameter == 122:
            return 'FLSEN-JM2'

        if table2Version == 253 and indicatorOfParameter == 121:
            return 'FLLAT-JM2'

        if table2Version == 253 and indicatorOfParameter == 117:
            return 'RADGLOA-JM2'

        if table2Version == 253 and indicatorOfParameter == 115:
            return 'RADLWA-JM2'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'RTOPLWA-JM2'

        if table2Version == 253 and indicatorOfParameter == 114:
            return 'RTOPLW-WM2'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'RTOPSWA-JM2'

        if table2Version == 253 and indicatorOfParameter == 113:
            return 'RTOPSW-WM2'

        if table2Version == 253 and indicatorOfParameter == 112:
            return 'RNETLWA-JM2'

        if table2Version == 253 and indicatorOfParameter == 111:
            return 'RNETSWA-JM2'

        if table2Version == 253 and indicatorOfParameter == 103:
            return 'PWS-S'

        if table2Version == 253 and indicatorOfParameter == 102:
            return 'HWS-M'

        if table2Version == 253 and indicatorOfParameter == 101:
            return 'DW-D'

        if table2Version == 253 and indicatorOfParameter == 91:
            return 'IC-0TO1'

        if table2Version == 253 and indicatorOfParameter == 86:
            return 'SM-KGM2'

        if table2Version == 253 and indicatorOfParameter == 84:
            return 'ALBEDO'

        if table2Version == 253 and indicatorOfParameter == 83:
            return 'SR-M'

        if table2Version == 253 and indicatorOfParameter == 81:
            return 'LC-0TO1'

        if table2Version == 253 and indicatorOfParameter == 76:
            return 'CLDWAT-KGKG'

        if table2Version == 253 and indicatorOfParameter == 75:
            return 'NH-PRCNT'

        if table2Version == 253 and indicatorOfParameter == 74:
            return 'NM-PRCNT'

        if table2Version == 253 and indicatorOfParameter == 73:
            return 'NL-PRCNT'

        if table2Version == 253 and indicatorOfParameter == 71:
            return 'N-0TO1'

        if table2Version == 253 and indicatorOfParameter == 67:
            return 'MIXHGT-M'

        if table2Version == 253 and indicatorOfParameter == 66:
            return 'SD-M'

        if table2Version == 253 and indicatorOfParameter == 61:
            return 'RR-KGM2'

        if table2Version == 253 and indicatorOfParameter == 58:
            return 'CLDICE-KGKG'

        if table2Version == 253 and indicatorOfParameter == 57:
            return 'EVAP-KGM2'

        if table2Version == 253 and indicatorOfParameter == 54:
            return 'PRCWAT-KGM2'

        if table2Version == 253 and indicatorOfParameter == 52:
            return 'RH-PRCNT'

        if table2Version == 253 and indicatorOfParameter == 51:
            return 'Q-KGKG'

        if table2Version == 253 and indicatorOfParameter == 41:
            return 'ABSVO-HZ'

        if table2Version == 253 and indicatorOfParameter == 40:
            return 'VV-MS'

        if table2Version == 253 and indicatorOfParameter == 39:
            return 'VV-PAS'

        if table2Version == 253 and indicatorOfParameter == 34:
            return 'V-MS'

        if table2Version == 253 and indicatorOfParameter == 33:
            return 'U-MS'

        if table2Version == 253 and indicatorOfParameter == 20:
            return 'VV-M'

        if table2Version == 253 and indicatorOfParameter == 17:
            return 'TD-K'

        if table2Version == 253 and indicatorOfParameter == 16:
            return 'TMIN-C'

        if table2Version == 253 and indicatorOfParameter == 15:
            return 'TMAX-C'

        if table2Version == 253 and indicatorOfParameter == 13:
            return 'TP-K'

        if table2Version == 253 and indicatorOfParameter == 11:
            return 'T-K'

        if table2Version == 253 and indicatorOfParameter == 8:
            return 'HL-M'

        if table2Version == 253 and indicatorOfParameter == 6:
            return 'Z-M2S2'

        if table2Version == 253 and indicatorOfParameter == 2:
            return 'P-PA'

        if table2Version == 253 and indicatorOfParameter == 1:
            return 'P-PA'

        if table2Version == 205 and indicatorOfParameter == 14:
            return 'IFF-MS'

        if table2Version == 205 and indicatorOfParameter == 13:
            return 'IDD-D'

        if table2Version == 205 and indicatorOfParameter == 12:
            return 'IRCNCT-PRCNT'

        if table2Version == 205 and indicatorOfParameter == 11:
            return 'IRAFTTHK-CM'

        if table2Version == 205 and indicatorOfParameter == 10:
            return 'IRIDGC-PRCNT'

        if table2Version == 205 and indicatorOfParameter == 9:
            return 'IMEANTHK-CM'

        if table2Version == 205 and indicatorOfParameter == 8:
            return 'IVELV-MS'

        if table2Version == 205 and indicatorOfParameter == 7:
            return 'IVELU-MS'

        if table2Version == 205 and indicatorOfParameter == 6:
            return 'IRIDGE-CM'

        if table2Version == 205 and indicatorOfParameter == 5:
            return 'IMAXTHK-CM'

        if table2Version == 205 and indicatorOfParameter == 4:
            return 'IMINTHK-CM'

        if table2Version == 205 and indicatorOfParameter == 3:
            return 'ITHK-CM'

        if table2Version == 205 and indicatorOfParameter == 2:
            return 'ICNCT-PRCNT'

        if table2Version == 205 and indicatorOfParameter == 1:
            return 'TSEA-C'

        if table2Version == 203 and indicatorOfParameter == 255:
            return 'PRECFORM2-N'

        if table2Version == 203 and indicatorOfParameter == 254:
            return 'CIN-500-N'

        if table2Version == 203 and indicatorOfParameter == 253:
            return 'CAPE1040-500'

        if table2Version == 203 and indicatorOfParameter == 252:
            return 'CAPE-0-3-500'

        if table2Version == 203 and indicatorOfParameter == 251:
            return 'CAPE-0-3'

        if table2Version == 203 and indicatorOfParameter == 250:
            return 'EL-500-M'

        if table2Version == 203 and indicatorOfParameter == 249:
            return 'LFC-500-M'

        if table2Version == 203 and indicatorOfParameter == 248:
            return 'LCL-500-M'

        if table2Version == 203 and indicatorOfParameter == 247:
            return 'EL-500-HPA'

        if table2Version == 203 and indicatorOfParameter == 246:
            return 'LFC-500-HPA'

        if table2Version == 203 and indicatorOfParameter == 245:
            return 'LCL-500-HPA'

        if table2Version == 203 and indicatorOfParameter == 244:
            return 'CIN-N'

        if table2Version == 203 and indicatorOfParameter == 243:
            return 'CAPE1040'

        if table2Version == 203 and indicatorOfParameter == 242:
            return 'CAPE-500'

        if table2Version == 203 and indicatorOfParameter == 241:
            return 'CAPE-JKG'

        if table2Version == 203 and indicatorOfParameter == 240:
            return 'EL-M'

        if table2Version == 203 and indicatorOfParameter == 239:
            return 'LFC-M'

        if table2Version == 203 and indicatorOfParameter == 238:
            return 'LCL-M'

        if table2Version == 203 and indicatorOfParameter == 237:
            return 'EL-HPA'

        if table2Version == 203 and indicatorOfParameter == 236:
            return 'LFC-HPA'

        if table2Version == 203 and indicatorOfParameter == 235:
            return 'LCL-HPA'

        if table2Version == 203 and indicatorOfParameter == 234:
            return 'F100-FF-MS'

        if table2Version == 203 and indicatorOfParameter == 233:
            return 'F90-FF-MS'

        if table2Version == 203 and indicatorOfParameter == 232:
            return 'F75-FF-MS'

        if table2Version == 203 and indicatorOfParameter == 231:
            return 'F50-FF-MS'

        if table2Version == 203 and indicatorOfParameter == 230:
            return 'F25-FF-MS'

        if table2Version == 203 and indicatorOfParameter == 229:
            return 'F10-FF-MS'

        if table2Version == 203 and indicatorOfParameter == 228:
            return 'F0-FF-MS'

        if table2Version == 203 and indicatorOfParameter == 227:
            return 'F100-FFG-MS'

        if table2Version == 203 and indicatorOfParameter == 226:
            return 'F90-FFG-MS'

        if table2Version == 203 and indicatorOfParameter == 225:
            return 'F75-FFG-MS'

        if table2Version == 203 and indicatorOfParameter == 224:
            return 'F50-FFG-MS'

        if table2Version == 203 and indicatorOfParameter == 223:
            return 'F25-FFG-MS'

        if table2Version == 203 and indicatorOfParameter == 222:
            return 'F10-FFG-MS'

        if table2Version == 203 and indicatorOfParameter == 221:
            return 'F0-FFG-MS'

        if table2Version == 203 and indicatorOfParameter == 220:
            return 'F100-N-0TO1'

        if table2Version == 203 and indicatorOfParameter == 219:
            return 'F90-N-0TO1'

        if table2Version == 203 and indicatorOfParameter == 218:
            return 'F75-N-0TO1'

        if table2Version == 203 and indicatorOfParameter == 217:
            return 'F50-N-0TO1'

        if table2Version == 203 and indicatorOfParameter == 216:
            return 'F25-N-0TO1'

        if table2Version == 203 and indicatorOfParameter == 215:
            return 'F10-N-0TO1'

        if table2Version == 203 and indicatorOfParameter == 214:
            return 'F0-N-0TO1'

        if table2Version == 203 and indicatorOfParameter == 213:
            return 'RRRS-KGM2'

        if table2Version == 203 and indicatorOfParameter == 212:
            return 'GRR-MMH'

        if table2Version == 203 and indicatorOfParameter == 211:
            return 'VEGET-N'

        if table2Version == 203 and indicatorOfParameter == 210:
            return 'VFLMOM-NM2'

        if table2Version == 203 and indicatorOfParameter == 209:
            return 'UFLMOM-NM2'

        if table2Version == 203 and indicatorOfParameter == 208:
            return 'TKEN-JKG'

        if table2Version == 203 and indicatorOfParameter == 207:
            return 'SOILTY-N'

        if table2Version == 203 and indicatorOfParameter == 206:
            return 'ILSAA1-N'

        if table2Version == 203 and indicatorOfParameter == 205:
            return 'CAPE1040-MU'

        if table2Version == 203 and indicatorOfParameter == 204:
            return 'CAPE-0-3-MU'

        if table2Version == 203 and indicatorOfParameter == 203:
            return 'FLMOM-PA'

        if table2Version == 203 and indicatorOfParameter == 202:
            return 'FLSEN-JM2'

        if table2Version == 203 and indicatorOfParameter == 201:
            return 'FLLAT-JM2'

        if table2Version == 203 and indicatorOfParameter == 200:
            return 'CANW-KGM2'

        if table2Version == 203 and indicatorOfParameter == 199:
            return 'CIN-MU-N'

        if table2Version == 203 and indicatorOfParameter == 198:
            return 'O3ANOM-PRCNT'

        if table2Version == 203 and indicatorOfParameter == 197:
            return 'UVI-N'

        if table2Version == 203 and indicatorOfParameter == 196:
            return 'UVIMAX-N'

        if table2Version == 203 and indicatorOfParameter == 195:
            return 'CAPE-MU-JKG'

        if table2Version == 203 and indicatorOfParameter == 194:
            return 'EL-MU-M'

        if table2Version == 203 and indicatorOfParameter == 193:
            return 'F100-RR-6'

        if table2Version == 203 and indicatorOfParameter == 192:
            return 'F90-RR-6'

        if table2Version == 203 and indicatorOfParameter == 191:
            return 'F75-RR-6'

        if table2Version == 203 and indicatorOfParameter == 190:
            return 'F50-RR-6'

        if table2Version == 203 and indicatorOfParameter == 189:
            return 'F25-RR-6'

        if table2Version == 203 and indicatorOfParameter == 188:
            return 'F10-RR-6'

        if table2Version == 203 and indicatorOfParameter == 187:
            return 'F0-RR-6'

        if table2Version == 203 and indicatorOfParameter == 186:
            return 'SM-KGM2'

        if table2Version == 203 and indicatorOfParameter == 185:
            return 'LFC-MU-M'

        if table2Version == 203 and indicatorOfParameter == 184:
            return 'LCL-MU-M'

        if table2Version == 203 and indicatorOfParameter == 183:
            return 'SR-M'

        if table2Version == 203 and indicatorOfParameter == 182:
            return 'EL-MU-HPA'

        if table2Version == 203 and indicatorOfParameter == 181:
            return 'LFC-MU-HPA'

        if table2Version == 203 and indicatorOfParameter == 180:
            return 'LCL-MU-HPA'

        if table2Version == 203 and indicatorOfParameter == 179:
            return 'F100-T-K'

        if table2Version == 203 and indicatorOfParameter == 178:
            return 'F90-T-K'

        if table2Version == 203 and indicatorOfParameter == 177:
            return 'F75-T-K'

        if table2Version == 203 and indicatorOfParameter == 176:
            return 'F50-T-K'

        if table2Version == 203 and indicatorOfParameter == 175:
            return 'F25-T-K'

        if table2Version == 203 and indicatorOfParameter == 174:
            return 'F10-T-K'

        if table2Version == 203 and indicatorOfParameter == 173:
            return 'F0-T-K'

        if table2Version == 203 and indicatorOfParameter == 172:
            return 'TTI-N'

        if table2Version == 203 and indicatorOfParameter == 171:
            return 'VTI-N'

        if table2Version == 203 and indicatorOfParameter == 170:
            return 'CTI-N'

        if table2Version == 203 and indicatorOfParameter == 169:
            return 'LI-N'

        if table2Version == 203 and indicatorOfParameter == 168:
            return 'SI-N'

        if table2Version == 203 and indicatorOfParameter == 167:
            return 'MIXHGT-M'

        if table2Version == 203 and indicatorOfParameter == 166:
            return 'RSI-KGM2'

        if table2Version == 203 and indicatorOfParameter == 165:
            return 'RRI-KGM2'

        if table2Version == 203 and indicatorOfParameter == 164:
            return 'SRMOM-M'

        if table2Version == 203 and indicatorOfParameter == 163:
            return 'MOL-M'

        if table2Version == 203 and indicatorOfParameter == 161:
            return 'PROBSN-0TO1'

        if table2Version == 203 and indicatorOfParameter == 159:
            return 'EFI-RR'

        if table2Version == 203 and indicatorOfParameter == 158:
            return 'EFI-WG'

        if table2Version == 203 and indicatorOfParameter == 157:
            return 'EFI-T'

        if table2Version == 203 and indicatorOfParameter == 156:
            return 'EFI-WS'

        if table2Version == 203 and indicatorOfParameter == 155:
            return 'PROB-WG-3'

        if table2Version == 203 and indicatorOfParameter == 154:
            return 'PROB-WG-2'

        if table2Version == 203 and indicatorOfParameter == 153:
            return 'PROB-WG-1'

        if table2Version == 203 and indicatorOfParameter == 152:
            return 'PROB-W-2'

        if table2Version == 203 and indicatorOfParameter == 151:
            return 'PROB-W-1'

        if table2Version == 203 and indicatorOfParameter == 150:
            return 'TPE3-C'

        if table2Version == 203 and indicatorOfParameter == 149:
            return 'FF1500-MS'

        if table2Version == 203 and indicatorOfParameter == 148:
            return 'HLCY-1-M2S2'

        if table2Version == 203 and indicatorOfParameter == 147:
            return 'HLCY-M2S2'

        if table2Version == 203 and indicatorOfParameter == 146:
            return 'WSH-1-KT'

        if table2Version == 203 and indicatorOfParameter == 145:
            return 'WSH-KT'

        if table2Version == 203 and indicatorOfParameter == 144:
            return 'PROB-RR-4'

        if table2Version == 203 and indicatorOfParameter == 143:
            return 'PROB-RR-3'

        if table2Version == 203 and indicatorOfParameter == 142:
            return 'PROB-RR-2'

        if table2Version == 203 and indicatorOfParameter == 141:
            return 'PROB-RR-1'

        if table2Version == 203 and indicatorOfParameter == 134:
            return 'PROB-T-4'

        if table2Version == 203 and indicatorOfParameter == 133:
            return 'PROB-T-3'

        if table2Version == 203 and indicatorOfParameter == 132:
            return 'PROB-T-2'

        if table2Version == 203 and indicatorOfParameter == 131:
            return 'PROB-T-1'

        if table2Version == 203 and indicatorOfParameter == 130:
            return 'ABSH-KGM3'

        if table2Version == 203 and indicatorOfParameter == 129:
            return 'TPE-K'

        if table2Version == 203 and indicatorOfParameter == 128:
            return 'RNETSW-WM2'

        if table2Version == 203 and indicatorOfParameter == 126:
            return 'RTOPLW-WM2'

        if table2Version == 203 and indicatorOfParameter == 122:
            return 'Z-C6-M2S2'

        if table2Version == 203 and indicatorOfParameter == 121:
            return 'Z-C5-M2S2'

        if table2Version == 203 and indicatorOfParameter == 120:
            return 'Z-C4-M2S2'

        if table2Version == 203 and indicatorOfParameter == 119:
            return 'Z-C3-M2S2'

        if table2Version == 203 and indicatorOfParameter == 118:
            return 'Z-C2-M2S2'

        if table2Version == 203 and indicatorOfParameter == 117:
            return 'Z-C1-M2S2'

        if table2Version == 203 and indicatorOfParameter == 116:
            return 'T-C6-C'

        if table2Version == 203 and indicatorOfParameter == 115:
            return 'T-C5-C'

        if table2Version == 203 and indicatorOfParameter == 114:
            return 'T-C4-C'

        if table2Version == 203 and indicatorOfParameter == 113:
            return 'T-C3-C'

        if table2Version == 203 and indicatorOfParameter == 112:
            return 'T-C2-C'

        if table2Version == 203 and indicatorOfParameter == 111:
            return 'T-C1-C'

        if table2Version == 203 and indicatorOfParameter == 110:
            return 'SNR-KGM2'

        if table2Version == 203 and indicatorOfParameter == 109:
            return 'SNRC-KGM2'

        if table2Version == 203 and indicatorOfParameter == 108:
            return 'SNRL-KGM2'

        if table2Version == 203 and indicatorOfParameter == 107:
            return 'SNC-KGM2'

        if table2Version == 203 and indicatorOfParameter == 106:
            return 'SNL-KGM2'

        if table2Version == 203 and indicatorOfParameter == 105:
            return 'CLDCND-KGKG'

        if table2Version == 203 and indicatorOfParameter == 104:
            return 'CLDICE-KGKG'

        if table2Version == 203 and indicatorOfParameter == 103:
            return 'ICING-N'

        if table2Version == 203 and indicatorOfParameter == 102:
            return 'SSICING-N'

        if table2Version == 203 and indicatorOfParameter == 101:
            return 'RHO-KGM3'

        if table2Version == 203 and indicatorOfParameter == 100:
            return 'IC-0TO1'

        if table2Version == 203 and indicatorOfParameter == 99:
            return 'LC-0TO1'

        if table2Version == 203 and indicatorOfParameter == 96:
            return 'RADGLO-WM2'

        if table2Version == 203 and indicatorOfParameter == 95:
            return 'RADLW-WM2'

        if table2Version == 203 and indicatorOfParameter == 91:
            return 'HESSAA-N'

        if table2Version == 203 and indicatorOfParameter == 89:
            return 'ALBEDO'

        if table2Version == 203 and indicatorOfParameter == 80:
            return 'KINDEX-N'

        if table2Version == 203 and indicatorOfParameter == 79:
            return 'N-PRCNT'

        if table2Version == 203 and indicatorOfParameter == 78:
            return 'CLDWAT-KGKG'

        if table2Version == 203 and indicatorOfParameter == 77:
            return 'LSSN-M100'

        if table2Version == 203 and indicatorOfParameter == 75:
            return 'TG-K'

        if table2Version == 203 and indicatorOfParameter == 74:
            return 'LNSP-N'

        if table2Version == 203 and indicatorOfParameter == 73:
            return 'RRRL-KGM2'

        if table2Version == 203 and indicatorOfParameter == 72:
            return 'RRRC-KGM2'

        if table2Version == 203 and indicatorOfParameter == 71:
            return 'RRR-KGM2'

        if table2Version == 203 and indicatorOfParameter == 70:
            return 'H0C-M'

        if table2Version == 203 and indicatorOfParameter == 69:
            return 'RNETLW-WM2'

        if table2Version == 203 and indicatorOfParameter == 68:
            return 'SNACC-KGM2'

        if table2Version == 203 and indicatorOfParameter == 63:
            return 'RRC-MM10'

        if table2Version == 203 and indicatorOfParameter == 62:
            return 'RRL-MM10'

        if table2Version == 203 and indicatorOfParameter == 60:
            return 'SMOGI-N'

        if table2Version == 203 and indicatorOfParameter == 59:
            return 'PRECFORM-N'

        if table2Version == 203 and indicatorOfParameter == 58:
            return 'RR-3-MM'

        if table2Version == 203 and indicatorOfParameter == 57:
            return 'RR-2-MM'

        if table2Version == 203 and indicatorOfParameter == 56:
            return 'RR-1-MM'

        if table2Version == 203 and indicatorOfParameter == 55:
            return 'RR-12-MM'

        if table2Version == 203 and indicatorOfParameter == 54:
            return 'RR-6-MM'

        if table2Version == 203 and indicatorOfParameter == 53:
            return 'HSADE2-N'

        if table2Version == 203 and indicatorOfParameter == 52:
            return 'HSADE1-N'

        if table2Version == 203 and indicatorOfParameter == 51:
            return 'SD-M'

        if table2Version == 203 and indicatorOfParameter == 50:
            return 'RR-MM10'

        if table2Version == 203 and indicatorOfParameter == 47:
            return 'PRCWAT-KGM2'

        if table2Version == 203 and indicatorOfParameter == 44:
            return 'VV-MS'

        if table2Version == 203 and indicatorOfParameter == 43:
            return 'VV-MMS'

        if table2Version == 203 and indicatorOfParameter == 40:
            return 'VV-PAS'

        if table2Version == 203 and indicatorOfParameter == 39:
            return 'FF10-MS'

        if table2Version == 203 and indicatorOfParameter == 38:
            return 'AQI-N'

        if table2Version == 203 and indicatorOfParameter == 31:
            return 'ABSVO-HZ-5'

        if table2Version == 203 and indicatorOfParameter == 28:
            return 'HM20C-M'

        if table2Version == 203 and indicatorOfParameter == 27:
            return 'FFG-MS'

        if table2Version == 203 and indicatorOfParameter == 24:
            return 'V-MS'

        if table2Version == 203 and indicatorOfParameter == 23:
            return 'U-MS'

        if table2Version == 203 and indicatorOfParameter == 22:
            return 'DF-MS'

        if table2Version == 203 and indicatorOfParameter == 21:
            return 'FF-MS'

        if table2Version == 203 and indicatorOfParameter == 20:
            return 'DD-D'

        if table2Version == 203 and indicatorOfParameter == 19:
            return 'FOGSYM-N'

        if table2Version == 203 and indicatorOfParameter == 18:
            return 'FRNTSYM-N'

        if table2Version == 203 and indicatorOfParameter == 15:
            return 'CLDSYM-N'

        if table2Version == 203 and indicatorOfParameter == 13:
            return 'RH-PRCNT'

        if table2Version == 203 and indicatorOfParameter == 12:
            return 'Q-KGKG'

        if table2Version == 203 and indicatorOfParameter == 10:
            return 'TD-C'

        if table2Version == 203 and indicatorOfParameter == 9:
            return 'TPW-K'

        if table2Version == 203 and indicatorOfParameter == 8:
            return 'TP-K'

        if table2Version == 203 and indicatorOfParameter == 4:
            return 'T-C'

        if table2Version == 203 and indicatorOfParameter == 3:
            return 'HL-M'

        if table2Version == 203 and indicatorOfParameter == 2:
            return 'Z-M2S2'

        if table2Version == 203 and indicatorOfParameter == 1:
            return 'P-HPA'

    return wrapped
