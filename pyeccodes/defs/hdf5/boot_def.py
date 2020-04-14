import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('identifier', "HDF5"))
    h.add(_.Ascii('signature', 8))
    h.add(_.Uint8('versionNumberOfSuperblock', 1))

    if ((h.get_l('versionNumberOfSuperblock') == 0) or (h.get_l('versionNumberOfSuperblock') == 1)):
        h.add(_.Uint8('versionNumOfFilesFreeSpaceStorage', 1))
        h.add(_.Uint8('versionNumOfRootGroupSymbolTableEntry', 1))
        h.add(_.Uint8('reserved1', 1))
        h.add(_.Uint8('versionNumOfSharedHeaderMessageFormat', 1))
        h.add(_.Uint8('sizeOfOffsets', 1))
        h.add(_.Uint8('sizeOfLength', 1))
        h.add(_.Uint8('reserved2', 1))
        h.add(_.Unsigned('groupLeafNodeK', 2))
        h.add(_.Unsigned('groupInternalNodeK', 2))
        h.add(_.Unsigned('fileConsistencyFlags', 4))

        if (h.get_l('versionNumberOfSuperblock') == 1):
            h.add(_.Uint16('indexedStorageInternalNodeK', 2))
            h.add(_.Uint16('reserved3', 2))

        if (h.get_l('sizeOfOffsets') == 8):
            h.add(_.Uint64_little_endian('baseAddress', 8))
            h.add(_.Uint64_little_endian('addressOfFileFreeSpaceInfo', 8))
            h.add(_.Uint64_little_endian('endOfFileAddress', 8))
            h.add(_.Uint64_little_endian('driverInformationBlockAddress', 8))
            h.add(_.Uint64_little_endian('rootGroupSymbolTableEntry', 8))

        if (h.get_l('sizeOfOffsets') == 4):
            h.add(_.Uint32_little_endian('baseAddress', 4))
            h.add(_.Uint32_little_endian('addressOfFileFreeSpaceInfo', 4))
            h.add(_.Uint32_little_endian('endOfFileAddress', 4))
            h.add(_.Uint32_little_endian('driverInformationBlockAddress', 4))
            h.add(_.Uint32_little_endian('rootGroupSymbolTableEntry', 4))


    if ((h.get_l('versionNumberOfSuperblock') == 2) or (h.get_l('versionNumberOfSuperblock') == 3)):
        h.add(_.Uint8('sizeOfOffsets', 1))
        h.add(_.Uint8('sizeOfLength', 1))
        h.add(_.Uint8('fileConsistencyFlags', 1))

        if (h.get_l('sizeOfOffsets') == 8):
            h.add(_.Uint64_little_endian('baseAddress', 8))
            h.add(_.Uint64_little_endian('superblockExtensionAddress', 8))
            h.add(_.Uint64_little_endian('endOfFileAddress', 8))
            h.add(_.Uint64_little_endian('rootGroupObjectHeaderAddress', 8))

        if (h.get_l('sizeOfOffsets') == 4):
            h.add(_.Uint32_little_endian('baseAddress', 4))
            h.add(_.Uint32_little_endian('superblockExtensionAddress', 4))
            h.add(_.Uint32_little_endian('endOfFileAddress', 4))
            h.add(_.Uint32_little_endian('rootGroupObjectHeaderAddress', 4))


