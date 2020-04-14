# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

from .defs import VERSION
from . import Reader

CODES_PRODUCT_ANY = None
CODES_PRODUCT_GRIB = None

KeyValueNotFoundError = KeyError


def codes_get_api_version():
    return VERSION


def codes_new_from_file(file, product_kind=None):
    handle = Reader(file).next_handle()
    if handle is not None:
        handle.compat = True
    return handle


def codes_release(handle):
    pass


def codes_get_array(handle, item, key_type):

    result = handle.get(item)

    try:
        len(result)
        return result
    except TypeError:
        if result is None:
            raise KeyValueNotFoundError(item)
        return [result]
