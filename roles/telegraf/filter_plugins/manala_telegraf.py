from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import string_types

import re


# See: https://github.com/jtyr/ansible-config_encoder_filters
def _is_num(data):
    """Verify if data is either int or float.
    Could be replaced by:
        from numbers import Number as number
        isinstance(data, number)
    but that requires Python v2.6+.
    """

    return isinstance(data, int) or isinstance(data, float)

# See: https://github.com/jtyr/ansible-config_encoder_filters
def _escape(data, quote='"', format=None):
    """Escape special characters in a string."""

    if format == 'xml':
        return (
            str(data).
            replace('&', '&amp;').
            replace('<', '&lt;').
            replace('>', '&gt;'))
    elif format == 'control':
        return (
            str(data).
            replace('\b', '\\b').
            replace('\f', '\\f').
            replace('\n', '\\n').
            replace('\r', '\\r').
            replace('\t', '\\t'))
    elif quote is not None and len(quote):
        return str(data).replace('\\', '\\\\').replace(quote, "\\%s" % quote)
    else:
        return data

# See: https://github.com/jtyr/ansible-config_encoder_filters
def _str_is_int(data):
    """Verify if data is integer."""

    return re.match(r"^[-+]?(0|[1-9][0-9]*)$", str(data))

# See: https://github.com/jtyr/ansible-config_encoder_filters
def _str_is_float(data):
    """Verify if data is float."""

    return re.match(
        r"^[-+]?(0|[1-9][0-9]*)(\.[0-9]*)?(e[-+]?[0-9]+)?$",
        str(data), flags=re.IGNORECASE)

# See: https://github.com/jtyr/ansible-config_encoder_filters
def _str_is_num(data):
    """Verify if data is either integer or float."""

    return _str_is_int(data) or _str_is_float(data)

# See: https://github.com/jtyr/ansible-config_encoder_filters
def _str_is_bool(data):
    """Verify if data is boolean."""

    return re.match(r"^(true|false)$", str(data), flags=re.IGNORECASE)

# See: https://github.com/jtyr/ansible-config_encoder_filters
def encode_toml(
        data, convert_bools=False, convert_nums=False, first=True, quote='"',
        table_name="", table_type=None):
    """Convert Python data structure to TOML format."""

    # Return value
    rv = ""

    if isinstance(data, dict):
        # It's a dict

        tn = table_name

        # First process all keys with elementar value (num/str/bool/array)
        for k, v in sorted(data.items()):

            if not (isinstance(v, dict) or isinstance(v, list)):
                if tn:
                    if not first:
                        rv += "\n"

                    if table_type == 'table':
                        rv += "[%s]\n" % tn
                    else:
                        rv += "[[%s]]\n" % tn

                rv += "%s = %s\n" % (
                    k,
                    encode_toml(
                        v,
                        convert_bools=convert_bools,
                        convert_nums=convert_nums,
                        first=first,
                        quote=quote))

                first = False
                tn = ''
            elif isinstance(v, list) and not isinstance(v[0], dict):
                if tn:
                    if not first:
                        rv += "\n"

                    if table_type == 'table':
                        rv += "[%s]\n" % tn
                    else:
                        rv += "[[%s]]\n" % tn

                rv += "%s = %s\n" % (
                    k,
                    encode_toml(
                        v,
                        convert_bools=convert_bools,
                        convert_nums=convert_nums,
                        first=first,
                        quote=quote))

                first = False
                tn = ''

        if not data and table_type is not None:
            if not first:
                rv += "\n"

            if table_type == 'table':
                rv += "[%s]\n" % tn
            else:
                rv += "[[%s]]\n" % tn

        # Then process tables and arrays of tables
        for k, v in sorted(data.items()):
            tn = table_name

            if isinstance(v, dict):
                # Table
                tk = k

                if '.' in k:
                    tk = "%s%s%s" % (quote, _escape(k, quote), quote)

                if tn:
                    tn += ".%s" % tk
                else:
                    tn += "%s" % tk

                rv += encode_toml(
                    v,
                    convert_bools=convert_bools,
                    convert_nums=convert_nums,
                    first=first,
                    quote=quote,
                    table_name=tn,
                    table_type='table')

                first = False
            elif isinstance(v, list) and isinstance(v[0], dict):
                # Array of tables
                tk = k

                if '.' in k:
                    tk = "%s%s%s" % (quote, _escape(k, quote), quote)

                if tn:
                    tn += ".%s" % tk
                else:
                    tn += "%s" % tk

                for t in v:
                    rv += encode_toml(
                        t,
                        convert_bools=convert_bools,
                        convert_nums=convert_nums,
                        first=first,
                        quote=quote,
                        table_name=tn,
                        table_type='table_array')

                    first = False

    elif isinstance(data, list):

        # Check if all values are elementar (num/str/bool/array)
        def is_elem(a):
            all_elementar = True

            for lv in a:
                if (
                        isinstance(lv, dict) or (
                            isinstance(lv, list) and
                            not is_elem(lv))):
                    all_elementar = False
                    break

            return all_elementar

        if is_elem(data):
            v_len = len(data)

            array = ''

            for i, lv in enumerate(data):
                array += "%s" % encode_toml(
                    lv,
                    convert_bools=convert_bools,
                    convert_nums=convert_nums,
                    first=first,
                    quote=quote)

                if i+1 < v_len:
                    array += ', '

            rv += "[%s]" % (array)

    elif (
            _is_num(data) or
            isinstance(data, bool) or
            (convert_nums and _str_is_num(data)) or
            (convert_bools and _str_is_bool(data))):
        # It's number or boolean

        rv += str(data).lower()

    elif isinstance(data, basestring):
        # It's a string

        rv += "%s%s%s" % (quote, _escape(data, quote), quote)

    return rv


def config(config, exclude=[]):
    if not isinstance(config, dict):
        raise AnsibleFilterError('manala_telegraf_config expects a dict but was given a %s' % type(config))
    [config.pop(key) for key in exclude]
    return encode_toml(config)


def config_parameters(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_telegraf_config_parameters expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key) for key in exclude]
    result = ''
    for key in sorted(parameters):
        result += '\n  %s' % config_parameter(parameters, key)
    return result


def config_parameter(parameters, key, default=None, comment=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_telegraf_config_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_telegraf_config_parameter key expects a string but was given a %s' % type(key))
    result = encode_toml({
        key: parameters.get(key, default)
    })
    if comment and not key in parameters:
        result = '# %s' % result
    return result.strip()


class FilterModule(object):
    ''' Manala telegraf jinja2 filters '''

    def filters(self):
        filters = {
            'manala_telegraf_config': config,
            'manala_telegraf_config_parameters': config_parameters,
            'manala_telegraf_config_parameter': config_parameter,
        }

        return filters
