import pyeccodes.accessors as _


def load(h):

    _.Template('grib1/mars_labeling.def').load(h)
    h.alias('grib2LocalSectionPresent', 'present')
    h.add(_.Constant('grib2LocalSectionNumber', 39))

    if (h.get_s('stepType') == "instant"):
        h.alias('productDefinitionTemplateNumber', 'zero')
    else:
        h.alias('productDefinitionTemplateNumber', 'eight')

    h.add(_.Constant('GRIBEXSection1Problem', (56 - _.Get('section1Length'))))
    h.add(_.Unsigned('componentIndex', 1))
    h.alias('mars.number', 'componentIndex')
    h.add(_.Unsigned('numberOfComponents', 1))
    h.add(_.Unsigned('modelErrorType', 1))
    h.add(_.Unsigned('offsetToEndOf4DvarWindow', 2))
    h.add(_.Unsigned('lengthOf4DvarWindow', 2))
    h.alias('anoffset', 'offsetToEndOf4DvarWindow')
    h.alias('local.componentIndex', 'componentIndex')
    h.alias('local.numberOfComponents', 'numberOfComponents')
    h.alias('local.modelErrorType', 'modelErrorType')
