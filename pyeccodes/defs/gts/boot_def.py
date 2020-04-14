import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('startOfHeaders'))
    h.add(_.Ascii('SOH', 4))
    h.add(_.Ascii('nnn', 3))
    h.add(_.Ascii('crcrlf', 3))
    h.add(_.Ascii('TT', 2))
    h.add(_.Ascii('AA', 2))
    h.add(_.Ascii('II', 2))
    h.add(_.Ascii('sp1', 1))
    h.add(_.Ascii('CCCC', 4))
    h.add(_.Ascii('sp2', 1))
    h.add(_.Ascii('YY', 2))
    h.add(_.Ascii('GG', 2))
    h.add(_.Ascii('gg', 2))
    h.add(_.Lookup('lBB', 2, 29, _.Get('BB')))

    if (((h.get_s('lBB') == "RR") or (h.get_s('lBB') == "CC")) or (h.get_s('lBB') == "AA")):
        h.add(_.Ascii('sp3', 1))
        h.add(_.Ascii('BBB', 3))
    else:
        h.add(_.Constant('BBB', "NNN"))

    h.alias('ls.BBB', 'BBB')
    h.alias('ls.count', 'count')
    h.alias('ls.TT', 'TT')
    h.alias('ls.AA', 'AA')
    h.alias('ls.II', 'II')
    h.alias('ls.CCCC', 'CCCC')
    h.alias('ls.YY', 'YY')
    h.alias('ls.GG', 'GG')
    h.alias('ls.gg', 'gg')
    h.add(_.Position('endOfHeadersMarker'))
    h.add(_.Message('theMessage', 4))
    h.add(_.Evaluate('lengthOfHeaders', (_.Get('endOfHeadersMarker') - _.Get('startOfHeaders'))))
    h.add(_.Md5('md5Headers', _.Get('startOfHeaders'), _.Get('lengthOfHeaders')))
    h.add(_.Ascii('endMark', 4))
    h.add(_.Position('totalLength'))
    h.alias('ls.totalLength', 'totalLength')
