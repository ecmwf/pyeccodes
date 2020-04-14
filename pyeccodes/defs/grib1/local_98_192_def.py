import pyeccodes.accessors as _


def load(h):

    h.add(_.Constant('GRIBEXSection1Problem', 0))
    h.add(_.StringCodetable('thisMarsClass', 1, "mars/class.table"))
    h.add(_.StringCodetable('thisMarsType', 1, "mars/type.table"))
    h.add(_.StringCodetable('thisMarsStream', 2, "mars/stream.table"))
    h.add(_.Ksec1expver('thisExperimentVersionNumber', 4))
    h.alias('ls.dataType', 'thisMarsType')
    h.alias('mars.class', 'thisMarsClass')
    h.alias('mars.type', 'thisMarsType')
    h.alias('mars.stream', 'thisMarsStream')
    h.alias('mars.expver', 'thisExperimentVersionNumber')
    h.add(_.Pad('padding_loc192_1', 2))
    h.add(_.Unsigned('numberOfLocalDefinitions', 1))

    if (h.get_l('numberOfLocalDefinitions') == 2):
        h.add(_.Unsigned('subLocalDefinitionLength1', 2))
        h.add(_.Unsigned('subLocalDefinitionNumber1', 1))
        h.add(_.StringCodetable('marsClass1', 1, "mars/class.table"))
        h.add(_.StringCodetable('marsType1', 1, "mars/type.table"))
        h.add(_.StringCodetable('marsStream1', 2, "mars/stream.table"))
        h.add(_.Ksec1expver('experimentVersionNumber1', 4))
        _.Template('grib1/local_no_mars.98.[subLocalDefinitionNumber1].def').load(h)
        h.add(_.Unsigned('subLocalDefinitionLength2', 2))
        h.add(_.Unsigned('subLocalDefinitionNumber2', 1))
        h.add(_.StringCodetable('marsClass2', 1, "mars/class.table"))
        h.add(_.StringCodetable('marsType2', 1, "mars/type.table"))
        h.add(_.StringCodetable('marsStream2', 2, "mars/stream.table"))
        h.add(_.Ksec1expver('experimentVersionNumber2', 4))
        _.Template('grib1/local_no_mars.98.[subLocalDefinitionNumber2].def').load(h)

