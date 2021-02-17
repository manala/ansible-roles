from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.filter.core import flatten

from numbers import Number


def pools(sections, exclude=[]):
    if not isinstance(sections, dict):
        raise AnsibleFilterError('manala_php_fpm_pools expects a dict but was given a %s' % type(sections))
    [sections.pop(key, None) for key in exclude]
    result = ''
    for section, parameters in sorted(iteritems(sections)):
        result += '[%s]%s\n\n' % (
            section,
            pools_section(parameters)
        )
    return result.rsplit('\n', 1)[0]


def pools_section(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_php_fpm_pools_section expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = pools_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result


def pools_parameter(parameters, key, required=False, default=None, comment=False, quote=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_php_fpm_pools_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_php_fpm_pools_parameter key expects a string but was given a %s' % type(key))
    if required and key not in parameters:
        raise AnsibleFilterError('manala_php_fpm_pools_parameter requires a value for key %s' % key)

    value = parameters.get(key, default)

    if isinstance(value, dict):
        result = ''
        for k, v in sorted(iteritems(value)):
            k = '%s[%s]' % (key, k)
            result += pools_parameter({k: v}, k, quote=quote) + '\n'
        result = result.rsplit('\n', 1)[0]
    else:
        if value is True:
            value = 'yes'
        elif value is False:
            value = 'no'
        elif isinstance(value, (string_types, Number)):
            pass
        else:
            AnsibleFilterError('manala_php_fpm_pools_parameter value of an unknown type %s' % type(value))

        if value == '':
            result = '%s =' % key
        else:
            if quote:
                value = '"%s"' % value
            result = '%s = %s' % (key, value)

    if key not in parameters:
        if comment is True:
            result = ';' + result.replace('\n', '\n;')
        elif isinstance(comment, string_types):
            result = comment

    return result


class FilterModule(object):
    ''' Manala php fpm pools jinja2 filters '''

    def filters(self):
        filters = {
            'manala_php_fpm_pools': pools,
            'manala_php_fpm_pools_section': pools_section,
            'manala_php_fpm_pools_parameter': pools_parameter,
        }

        return filters
