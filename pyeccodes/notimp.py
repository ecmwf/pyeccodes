# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .base import Accessor


class NoResult:

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title

    def __sub__(self, other):
        return "(%s-%s)" % (self, other)


class NotImp(Accessor):

    length = 0

    def __init__(self, name, *ignore):
        super().__init__(name)

    def get(self, handle):
        return NoResult("%s(<not-implemented>)" % (self.__class__.__name__.split('.')[-1]))


class Bits(NotImp):
    pass


class Bits_per_value(NotImp):
    pass


class Change_scanning_direction(NotImp):
    pass


class Decimal_precision(NotImp):
    pass


class Dirty(NotImp):
    pass


class Ifs_param(NotImp):
    pass


class Latlonvalues(NotImp):
    pass


class Nearest(NotImp):
    pass


class Offset_values(NotImp):
    pass


class Reference_value_error(NotImp):
    pass


class Scale_values(NotImp):
    pass


class Simple_packing_error(NotImp):
    pass


class Data_dummy_field(NotImp):
    pass


class Select_step_template(NotImp):
    pass


class G2_chemical(NotImp):
    pass


class Local_definition(NotImp):
    pass



class G2step_range(NotImp):
    pass


class G1end_of_interval_monthly(NotImp):
    pass


class G1forecastmonth(NotImp):
    pass


class Spectral_truncation(NotImp):
    pass


class Data_sh_packed(NotImp):
    pass


class Data_sh_unpacked(NotImp):
    pass


class Statistics_spectral(NotImp):
    pass


class G2lon(NotImp):
    pass


class Unsigned_bits(NotImp):
    pass


class Sum(NotImp):
    pass


class G1number_of_coded_values_sh_complex(NotImp):
    pass


class Element(NotImp):
    pass


class G1verificationdate(NotImp):
    pass


class Divdouble(NotImp):
    pass


class Round(NotImp):
    pass


class Second_order_bits_per_value(NotImp):
    pass


class Data_apply_boustrophedonic(NotImp):
    pass
