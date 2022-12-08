from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.filter.core import flatten

from numbers import Number


def pools(sections, exclude=None):
    exclude = exclude or []
    if not isinstance(sections, dict):
        raise AnsibleFilterError('php_fpm_pools expects a dict but was given a %s' % type(sections))
    [sections.pop(key, None) for key in exclude]
    result = ''
    for section, parameters in sorted(iteritems(sections)):
        result += '[%s]%s\n\n' % (
            section,
            pools_section(parameters)
        )
    return result.rstrip()


def pools_section(parameters, exclude=None):
    exclude = exclude or []
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('php_fpm_pools_section expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = pools_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result


def pools_parameter(parameters, key, required=False, comment=False, quote=False, **kwargs):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('php_fpm_pools_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('php_fpm_pools_parameter key expects a string but was given a %s' % type(key))

    if key in parameters:
        value = parameters.get(key)
    else:
        if required:
            raise AnsibleFilterError('php_fpm_pools_parameter requires a value for key %s' % key)
        if isinstance(comment, string_types):
            return comment
        if 'default' not in kwargs:
            raise AnsibleFilterError('php_fpm_pools_parameter missing a default value for key %s' % key)
        value = kwargs.get('default')

    if value is True:
        if quote:
            raise AnsibleFilterError('php_fpm_pools_parameter unquotable boolean value')
        result = '%s = yes' % key
    elif value is False:
        if quote:
            raise AnsibleFilterError('php_fpm_pools_parameter unquotable boolean value')
        result = '%s = no' % key
    elif isinstance(value, (string_types, Number)):
        if value == '':
            result = '%s =' % key
        else:
            if quote:
                result = '%s = "%s"' % (key, value)
            else:
                result = '%s = %s' % (key, value)
    elif isinstance(value, dict):
        result = ''
        for k, v in sorted(iteritems(value)):
            k = '%s[%s]' % (key, k)
            result += pools_parameter({k: v}, k, quote=quote) + '\n'
        result = result.rsplit('\n', 1)[0]
    elif isinstance(value, list):
        value = flatten(value)
        if key == 'access.suppress_path':
            # 'access.suppress_path' is a particular option which is internally handled by fpm
            # as a dict with null keys. Such a structure is unavailabl both in yaml and python,
            # so, as a consequence, we handle it as a list.
            # See: https://github.com/php/php-src/pull/8214
            result = '\n'.join(
                pools_parameter({'%s[]' % key: v}, '%s[]' % key, quote=quote) for v in value
            )
        else:
            result = '\n'.join(
                pools_parameter({key: v}, key, quote=quote) for v in value
            )
    else:
        raise AnsibleFilterError('php_fpm_pools_parameter value of an unknown type %s' % type(value))

    if key not in parameters and comment:
        result = ';' + result.replace('\n', '\n;')

    return result


class FilterModule(object):
    ''' Manala php fpm pools jinja2 filters '''

    def filters(self):
        filters = {
            'php_fpm_pools': pools,
            'php_fpm_pools_section': pools_section,
            'php_fpm_pools_parameter': pools_parameter,
        }

        return filters
