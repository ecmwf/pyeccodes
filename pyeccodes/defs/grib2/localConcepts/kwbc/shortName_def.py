import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 8:
            return 'tp'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 'tcc'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 'cin'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 224:
            return 'VRATE'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 234:
            return 'ICSEV'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 201:
            return 'SUNSD'

        if discipline == 255 and parameterCategory == 255 and parameterNumber == 255:
            return 'imgd'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 197:
            return 'ohc'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 196:
            return 'intfd'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 195:
            return 'dbss'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 194:
            return 'bkeng'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 193:
            return 'salin'

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 192:
            return 'wtmpc'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 202:
            return 'sltfl'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 201:
            return 'keng'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 200:
            return 'ssst'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 199:
            return 'sstt'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 198:
            return 'ashfl'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 197:
            return 'aohflx'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 196:
            return 'p2omlt'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 195:
            return 'sshg'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 194:
            return 'elevhtml'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 193:
            return 'etsrg'

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 192:
            return 'surge'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 195:
            return 'vbaro'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 194:
            return 'ubaro'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 193:
            return 'omlv'

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 192:
            return 'omlu'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 192:
            return 'wstp'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 193:
            return 'vsct'

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 192:
            return 'usct'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 203:
            return 'fldcp'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 202:
            return 'radt'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 201:
            return 'avsft'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 200:
            return 'baret'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 199:
            return 'lspa'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 198:
            return 'evbs'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 'sltyp'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 230:
            return 'trans'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 229:
            return 'evcw'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 228:
            return 'acond'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 227:
            return 'wcvflx'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 226:
            return 'wcuflx'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 225:
            return 'wvvflx'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 224:
            return 'wvuflx'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 223:
            return 'wcconv'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 222:
            return 'wvconv'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 221:
            return 'wcinc'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 220:
            return 'wvinc'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 219:
            return 'amixl'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 218:
            return 'landn'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 217:
            return 'ndvi'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 216:
            return 'sfcrh'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 215:
            return 'qrec'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 214:
            return 'gwrec'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 213:
            return 'ewatr'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 212:
            return 'lsoil'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 211:
            return 'sstor'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 210:
            return 'vegt'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 209:
            return 'akms'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 208:
            return 'akhs'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 207:
            return 'icwat'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 206:
            return 'rdrip'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 201:
            return 'wilt'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'vgtyp'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 195:
            return 'cwr'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 194:
            return 'ppffg'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 192:
            return 'cpozp'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 197:
            return 'elonn'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 196:
            return 'nlatn'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 195:
            return 'mlyno'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 193:
            return 'elon'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 192:
            return 'nlat'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 232:
            return 'vaftd'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 219:
            return 'tpfi'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 218:
            return 'epsr'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 217:
            return 'sipd'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 216:
            return 'prsigsvr'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 215:
            return 'prsvr'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 214:
            return 'nwsalb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 213:
            return 'nbsalb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 212:
            return 'swsalb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 211:
            return 'sbsalb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 210:
            return 'havni'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 209:
            return 'lavni'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208:
            return 'ciflt'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207:
            return 'civis'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206:
            return 'cicel'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205:
            return 'flght'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204:
            return 'mixly'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203:
            return 'tstmc'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202:
            return 'swindpro'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201:
            return 'shailpro'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200:
            return 'storprob'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199:
            return 'windprob'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198:
            return 'hailprob'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197:
            return 'torprob'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196:
            return 'hrcono'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195:
            return 'mrcono'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 194:
            return 'srcono'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192:
            return 'ltng'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 196:
            return 'refc'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 195:
            return 'refd'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 194:
            return 'refzc'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 193:
            return 'refzi'

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 192:
            return 'refzr'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 199:
            return 'pozo'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 198:
            return 'pozt'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 197:
            return 'toz'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 196:
            return 'poz'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 195:
            return 'vdfoz'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 194:
            return 'ozcat'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193:
            return 'ozcon'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195:
            return 'lipmf'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194:
            return 'lpmtf'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193:
            return 'pmtf'

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192:
            return 'pmtc'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 198:
            return 'lai'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 197:
            return 'uphl'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 'cwdi'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194:
            return 'ri'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 200:
            return 'mflux'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 197:
            return 'cfnlf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 196:
            return 'csdlf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 195:
            return 'csulf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 194:
            return 'lwhr'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 205:
            return 'utrf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 204:
            return 'dtrf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 203:
            return 'nddsf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 202:
            return 'nbdsf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 201:
            return 'vddsf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 200:
            return 'vbdsf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199:
            return 'cfnsf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198:
            return 'csusf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 197:
            return 'swhr'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 196:
            return 'csdsf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 195:
            return 'cduvb'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 194:
            return 'duvb'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 212:
            return 'presn'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 211:
            return 'hgtn'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 210:
            return 'lmh'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 209:
            return 'cnvdemf'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 208:
            return 'cnvdmf'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 207:
            return 'cnvumf'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 206:
            return 'nlgsp'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 205:
            return 'layth'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 204:
            return 'hgty'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 203:
            return 'hgtx'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 202:
            return 'lpsy'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 201:
            return 'lpsx'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 200:
            return 'plpl'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 199:
            return 'tslsa'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 198:
            return 'mslma'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 'mslet'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 219:
            return 'pvmww'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 218:
            return 'lmv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 217:
            return 'cngwdv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 216:
            return 'cngwdu'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 215:
            return 'omgalf'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 214:
            return 'wtend'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 213:
            return 'cnvv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 212:
            return 'cnvu'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 211:
            return 'gwdv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 210:
            return 'gwdu'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 209:
            return 'vdfva'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 208:
            return 'vdfua'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 207:
            return 'covtm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 206:
            return 'covtz'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 205:
            return 'covmz'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 204:
            return 'vedh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 203:
            return 'lopp'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 202:
            return 'lapp'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 201:
            return 'lovv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 200:
            return 'lavv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 199:
            return 'louv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 198:
            return 'lauv'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 225:
            return 'frzr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 224:
            return 'acpcpn'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 223:
            return 'apcpn'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 222:
            return 'snowt'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 221:
            return 'arain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 220:
            return 'qmin'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 219:
            return 'qmax'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 218:
            return 'qz0'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 217:
            return 'lrgmr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 216:
            return 'condp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 215:
            return 'vdfmr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 214:
            return 'shamr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 213:
            return 'cnvmr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 212:
            return 'sbsno'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 211:
            return 'emnp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 210:
            return 'tcolm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 209:
            return 'tclsw'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 'snot'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207:
            return 'ncip'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206:
            return 'tipd'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198:
            return 'minrh'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 204:
            return 'tchp'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 203:
            return 'thz0'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 202:
            return 'vdfhr'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 201:
            return 'shahr'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 200:
            return 'tsd1d'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 199:
            return 'ttphy'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 198:
            return 'ttdia'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 197:
            return 'thflx'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 196:
            return 'cnvhr'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 195:
            return 'lrghr'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 'rev'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 'ttrad'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197:
            return 'poros'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196:
            return 'smdry'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 'smref'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 'rlyrs'

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 'soill'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 204:
            return 'rcq'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 205:
            return 'rcsol'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 203:
            return 'rct'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 202:
            return 'rcs'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 200:
            return 'rsmin'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'ccond'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'bmixl'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'cnwat'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 'sfexc'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194:
            return 'mstav'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193:
            return 'gflux'

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192:
            return 'soilw'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 193:
            return 'ssrun'

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 192:
            return 'bgrun'

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 194:
            return 'tsec'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193:
            return 'snfalb'

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 'mxsalb'

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192:
            return 'o3mr'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return '4lftx'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 'lftx'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199:
            return 'fice'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198:
            return 'tcolc'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 197:
            return 'tcoli'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196:
            return 'tcolw'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194:
            return 'cuefi'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193:
            return 'cwork'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192:
            return 'cdlyr'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 193:
            return 'ulwrf'

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192:
            return 'dlwrf'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 196:
            return 'uvi'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193:
            return 'uswrf'

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192:
            return 'dswrf'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 197:
            return '5wava'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 196:
            return 'hpbl'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 195:
            return 'v-gwd'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194:
            return 'u-gwd'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193:
            return '5wavh'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 197:
            return 'fricv'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196:
            return 'cd'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195:
            return 'vstm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194:
            return 'ustm'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193:
            return 'mflx'

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192:
            return 'vwsh'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 'sdwe'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205:
            return 'tcols'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204:
            return 'tcolr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 'rime'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202:
            return 'frain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201:
            return 'snowc'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200:
            return 'pevpr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199:
            return 'pevap'

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 193:
            return 'cpofp'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196:
            return 'cprat'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195:
            return 'csnow'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194:
            return 'cicep'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193:
            return 'cfrzr'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192:
            return 'crain'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197:
            return 'mconv'

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195:
            return 'tcond'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192:
            return 'snohf'

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 'cape'

    return wrapped
