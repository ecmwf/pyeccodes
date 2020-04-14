import pyeccodes.accessors as _


def load(h):

    h.alias('mars.fcmonth', 'marsForecastMonth')
    h.alias('mars.number', 'perturbationNumber')
    h.alias('mars.origin', 'centre')
    h.unalias('mars.step')
    h.alias('mars.method', 'methodNumber')

    if (h.get_s('class') == "od"):
        h.alias('mars.system', 'systemNumber')

    if (h.get_s('class') == "me"):
        h.alias('mars.system', 'systemNumber')

    if (h.get_s('class') == "en"):
        h.alias('mars.system', 'systemNumber')

    if (h.get_s('class') == "c3"):
        h.alias('mars.system', 'systemNumber')

    if (((h.get_l('centre') == 80) and (h.get_l('subCentre') == 98)) and (h.get_s('class') == "c3")):
        h.add(_.Constant('cnmc_cmcc', "cmcc"))
        h.alias('mars.origin', 'cnmc_cmcc')

