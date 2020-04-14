import pyeccodes.accessors as _


def load(h):

    h.add(_.DoubleConstant('default_min_val', -1e+09))
    h.add(_.DoubleConstant('default_max_val', 1e+09))

    def param_value_min_inline_concept(h):
        def wrapped(h):

            paramId = h.get_l('paramId')

            if paramId == 165:
                return '-150'

            if paramId == 166:
                return '-100'

            if paramId == 260260:
                return 0

            if paramId == 228028:
                return 0

            if paramId == 49:
                return 0

            if paramId == 207:
                return 0

            if paramId == 168:
                return 25

            if paramId == 260242:
                return 0

            if paramId == 167:
                return 160

            if paramId == 260509:
                return 0

            if paramId == 151175:
                return 5

            if paramId == 260257:
                return 0

            if paramId == 59:
                return 0

            if paramId == 228001:
                return '-60000'

            if paramId == 151163:
                return 0

            if paramId == 151131:
                return '-3.5'

            if paramId == 260259:
                return '-10'

            if paramId == 129:
                return '-13000'

            if paramId == 156:
                return '-1300'

            if paramId == 3075:
                return 0

            if paramId == 172:
                return 0

            if paramId == 3062:
                return '-0.05'

            if paramId == 260210:
                return 0

            if paramId == 3073:
                return 0

            one = h.get_l('one')

            if one == (_.Get('step') > 0) and paramId == 121:
                return 160

            if one == (_.Get('step') > 0) and paramId == 122:
                return 150

            if paramId == 151:
                return 85000

            if paramId == 151126:
                return 270

            if paramId == 140230:
                return '-1'

            if paramId == 140221:
                return 0

            if paramId == 3074:
                return 0

            if paramId == 140214:
                return 0

            if paramId == 151132:
                return '-3.5'

            if paramId == 151225:
                return 0

            if paramId == 228002:
                return '-1300'

            if paramId == 140231:
                return 0

            if paramId == 260430:
                return 0

            if paramId == 3:
                return 170

            if paramId == 60:
                return '-1'

            if paramId == 54:
                return 100

            if paramId == 157:
                return 0

            if paramId == 151145:
                return '-4'

            if paramId == 151219:
                return 0

            if paramId == 34:
                return 160

            if paramId == 31:
                return 0

            if paramId == 174098:
                return 0

            if paramId == 140229:
                return 0

            if paramId == 235:
                return 120

            if paramId == 228032:
                return 20

            if paramId == 33:
                return 10

            if paramId == 3066:
                return 0

            if paramId == 228141:
                return '-1e-10'

            if paramId == 260367:
                return '0.005'

            if paramId == 260364:
                return '-1000'

            if paramId == 228039:
                return 0

            if paramId == 228087:
                return 0

            if paramId == 228086:
                return '-20'

            if paramId == 260360:
                return 170

            if paramId == 228139:
                return 170

            if paramId == 228096:
                return 170

            if paramId == 228095:
                return 170

            if paramId == 43:
                return 0

            if paramId == 247:
                return '-0.001'

            if paramId == 246:
                return '-0.001'

            if paramId == 133:
                return '-0.1'

            if paramId == 134:
                return 43000

            if paramId == 173:
                return 0

            if paramId == 130:
                return 140

            if paramId == 260057:
                return '-3'

            if paramId == 136:
                return '-50'

            if paramId == 131:
                return '-250'

            if paramId == 132:
                return '-250'

            if paramId == 135:
                return '-30'

            if paramId == 260199:
                return 0

            if paramId == 3031:
                return 0

            if paramId == 10:
                return 0

        return wrapped

    h.add(_.Concept('param_value_min', 'default_min_val', concepts=param_value_min_inline_concept(h)))

    def param_value_max_inline_concept(h):
        def wrapped(h):

            paramId = h.get_l('paramId')

            if paramId == 165:
                return 150

            if paramId == 166:
                return 100

            if paramId == 260260:
                return '360.1'

            if paramId == 228028:
                return 140

            if paramId == 49:
                return 100

            if paramId == 207:
                return 300

            if paramId == 168:
                return 350

            if paramId == 260242:
                return 160

            if paramId == 167:
                return 370

            if paramId == 260509:
                return 100

            if paramId == 151175:
                return 50

            if paramId == 260257:
                return 100

            if paramId == 59:
                return 40000

            if paramId == 228001:
                return 1000

            if paramId == 151163:
                return 1500

            if paramId == 151131:
                return '3.5'

            if paramId == 260259:
                return 5

            if paramId == 129:
                return 350000

            if paramId == 156:
                return 35000

            if paramId == 3075:
                return 100

            if paramId == 172:
                return 1

            if paramId == 3062:
                return 130

            if paramId == 260210:
                return 1

            if paramId == 3073:
                return 100

            if paramId == 121:
                return 380

            if paramId == 151:
                return 125000

            if paramId == 151126:
                return 308

            if paramId == 140230:
                return '360.5'

            if paramId == 140221:
                return 50

            if paramId == 3074:
                return 100

            if paramId == 122:
                return 330

            if paramId == 140214:
                return 150

            if paramId == 151132:
                return '3.5'

            if paramId == 151225:
                return 4000

            if paramId == 228002:
                return 8888

            if paramId == 140231:
                return 50

            if paramId == 260430:
                return 30

            if paramId == 3:
                return 1200

            if paramId == 60:
                return 1

            if paramId == 54:
                return 108000

            if paramId == 157:
                return 180

            if paramId == 151145:
                return 4

            if paramId == 151219:
                return 50

            if paramId == 34:
                return 320

            if paramId == 31:
                return '1.001'

            if paramId == 174098:
                return 15

            if paramId == 140229:
                return 100

            if paramId == 235:
                return 380

            if paramId == 228032:
                return 100

            if paramId == 33:
                return 1000

            if paramId == 3066:
                return 5

            if paramId == 228141:
                return 15000

            if paramId == 260367:
                return 100

            if paramId == 260364:
                return 1000

            if paramId == 228039:
                return 2000

            if paramId == 228087:
                return 2000

            if paramId == 228086:
                return 2000

            if paramId == 260360:
                return 350

            if paramId == 228139:
                return 350

            if paramId == 228096:
                return 350

            if paramId == 228095:
                return 350

            if paramId == 43:
                return 10

            if paramId == 247:
                return '0.01'

            if paramId == 246:
                return '1e+06'

            if paramId == 133:
                return '0.1'

            if paramId == 134:
                return 115000

            if paramId == 173:
                return 10

            if paramId == 130:
                return 400

            if paramId == 260057:
                return 150

            if paramId == 136:
                return 220

            if paramId == 131:
                return 250

            if paramId == 132:
                return 250

            if paramId == 135:
                return 30

            if paramId == 260199:
                return 1

            if paramId == 3031:
                return '360.1'

            if paramId == 10:
                return 300

        return wrapped

    h.add(_.Concept('param_value_max', 'default_max_val', concepts=param_value_max_inline_concept(h)))

