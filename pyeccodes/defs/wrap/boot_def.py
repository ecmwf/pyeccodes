import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('startOfHeaders'))
    h.add(_.Ascii('identifier', 4))
    h.alias('ls.identifier', 'identifier')
    h.add(_.Uint64('totalLength', 8))
    h.add(_.Uint8('version', 1))
    h.add(_.Uint8('spare', 1))
    _.Template('wrap/metadata.[version].def').load(h)
    h.add(_.Position('endOfHeadersMarker'))
    h.add(_.Constant('dataLength', ((_.Get('totalLength') - _.Get('endOfHeadersMarker')) - 4)))
    h.add(_.Blob('data', _.Get('dataLength')))
    h.add(_.Ascii('endMark', 4))
    h.add(_.Position('totalLength'))
