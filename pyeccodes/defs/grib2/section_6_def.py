import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection6'))
    h.add(_.Position('offsetBSection6'))
    h.add(_.Section_length('section6Length', 4))
    h.add(_.Section_pointer('section6', _.Get('offsetSection6'), _.Get('section6Length'), 6))
    h.add(_.Unsigned('numberOfSection', 1))
    h.add(_.Codetable('bitMapIndicator', 1, "6.0.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.G2bitmap_present('bitmapPresent', _.Get('bitMapIndicator')))
    h.alias('geography.bitmapPresent', 'bitmapPresent')
    h.add(_.Transient('missingValuesPresent', _.Get('bitmapPresent')))

    if (h.get_l('bitMapIndicator') == 0):

        if (h.get_l('dataRepresentationTemplateNumber') == 1):

            if (h.get_l('matrixBitmapsPresent') == 1):
                h.add(_.G2bitmap('primaryBitmap', _.Get('tableReference'), _.Get('missingValue'), _.Get('offsetBSection6'), _.Get('section6Length'), _.Get('numberOfDataMatrices')))
            else:
                h.add(_.G2bitmap('bitmap', _.Get('tableReference'), _.Get('missingValue'), _.Get('offsetBSection6'), _.Get('section6Length'), _.Get('numberOfDataPoints')))
                h.alias('geography.bitmap', 'bitmap')

        else:
            h.add(_.G2bitmap('bitmap', _.Get('tableReference'), _.Get('missingValue'), _.Get('offsetBSection6'), _.Get('section6Length'), _.Get('numberOfDataPoints')))
            h.alias('geography.bitmap', 'bitmap')


    if (h.get_l('bitMapIndicator') == 255):

        if ((h.get_l('dataRepresentationTemplateNumber') == 2) or (h.get_l('dataRepresentationTemplateNumber') == 3)):
            h.add(_.Transient('missingValuesPresent', (_.Get('missingValueManagementUsed') != 0)))


    h.add(_.Md5('md5Section6', _.Get('offsetSection6'), _.Get('section6Length')))
