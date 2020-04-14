import pyeccodes.accessors as _


def load(h):

    h.add(_.Position('offsetSection7'))
    h.add(_.Section_length('section7Length', 4))
    h.add(_.Section_pointer('section7', _.Get('offsetSection7'), _.Get('section7Length'), 7))
    h.add(_.Unsigned('numberOfSection', 1))
    h.add(_.Position('offsetBeforeData'))
    _.Template('grib2/template.7.[dataRepresentationTemplateNumber:l].def').load(h)
    h.add(_.Decimal_precision('changeDecimalPrecision', _.Get('bitsPerValue'), _.Get('decimalScaleFactor'), _.Get('changingPrecision'), _.Get('values')))
    h.add(_.Decimal_precision('decimalPrecision', _.Get('bitsPerValue'), _.Get('decimalScaleFactor'), _.Get('changingPrecision')))
    h.alias('setDecimalPrecision', 'changeDecimalPrecision')
    h.add(_.Bits_per_value('setBitsPerValue', _.Get('values'), _.Get('bitsPerValue')))
    h.add(_.Size('getNumberOfValues', _.Get('values')))
    h.add(_.Scale_values('scaleValuesBy', _.Get('values'), _.Get('missingValue')))
    h.add(_.Offset_values('offsetValuesBy', _.Get('values'), _.Get('missingValue')))

    def productType_inline_concept(h):
        def wrapped(h):

            grib2LocalSectionPresent = h.get_l('grib2LocalSectionPresent')
            centre = h.get_l('centre')
            grib2LocalSectionNumber = h.get_l('grib2LocalSectionNumber')
            productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')

            if grib2LocalSectionPresent == 1 and centre == 98 and grib2LocalSectionNumber == 500 and productDefinitionTemplateNumber == 2000:
                return 'obstat'

        return wrapped

    h.add(_.Concept('productType', 'unknown', concepts=productType_inline_concept(h)))

    h.add(_.Position('offsetAfterData'))
    h.add(_.Md5('md5Section7', _.Get('offsetSection7'), _.Get('section7Length')))
    h.alias('md5DataSection', 'md5Section7')
