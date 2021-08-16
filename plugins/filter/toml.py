from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import string_types

import re

"""
Config Encoder Filters
More information: https://github.com/jtyr/ansible-config_encoder_filters
"""


def _is_num(data):
    """Verify if data is either int or float.
    Could be replaced by:
        from numbers import Number as number
        isinstance(data, number)
    but that requires Python v2.6+.
    """

    return isinstance(data, int) or isinstance(data, float)


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


def _str_is_int(data):
    """Verify if data is integer."""

    return re.match(r"^[-+]?(0|[1-9][0-9]*)$", str(data))


def _str_is_float(data):
    """Verify if data is float."""

    return re.match(
        r"^[-+]?(0|[1-9][0-9]*)(\.[0-9]*)?(e[-+]?[0-9]+)?$",
        str(data), flags=re.IGNORECASE)


def _str_is_num(data):
    """Verify if data is either integer or float."""

    return _str_is_int(data) or _str_is_float(data)


def _str_is_bool(data):
    """Verify if data is boolean."""

    return re.match(r"^(true|false)$", str(data), flags=re.IGNORECASE)


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
            elif isinstance(v, list) and (not v or not isinstance(v[0], dict)):
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
            elif isinstance(v, list) and (not v or isinstance(v[0], dict)):
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

                if i + 1 < v_len:
                    array += ', '

            rv += "[%s]" % (array)

    elif (
            _is_num(data) or
            isinstance(data, bool) or
            (convert_nums and _str_is_num(data)) or
            (convert_bools and _str_is_bool(data))):
        # It's number or boolean

        rv += str(data).lower()

    elif isinstance(data, string_types):
        # It's a string

        rv += "%s%s%s" % (quote, _escape(data, quote), quote)

    return rv


def toml(parameters, exclude=None):
    exclude = exclude or []
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('toml expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key) for key in exclude]
    return encode_toml(parameters).rstrip()


def toml_section(parameters, exclude=None):
    exclude = exclude or []
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('toml_section expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key) for key in exclude]
    result = ''
    for key in sorted(parameters):
        result += '\n  %s' % toml_parameter(parameters, key)
    return result


def toml_parameter(parameters, key, required=False, comment=False, **kwargs):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('toml_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('toml_parameter key expects a string but was given a %s' % type(key))

    if key in parameters:
        value = parameters.get(key)
    else:
        if required:
            raise AnsibleFilterError('toml_parameter requires a value for key %s' % key)
        if isinstance(comment, string_types):
            return comment
        if 'default' not in kwargs:
            raise AnsibleFilterError('toml_parameter missing a default value for key %s' % key)
        value = kwargs.get('default')

    result = encode_toml({
        key: value
    }).strip()

    if key not in parameters and comment:
        result = '# ' + result.replace('\n', '\n# ')

    return result


class FilterModule(object):
    ''' Manala toml jinja2 filters '''

    def filters(self):
        filters = {
            'toml': toml,
            'toml_section': toml_section,
            'toml_parameter': toml_parameter,
        }

        return filters
