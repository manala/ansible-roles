from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.filter.core import flatten

from numbers import Number


def config(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_nginx_config expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = config_section(parameters)
    return result.lstrip()

def config_section(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_nginx_config_section expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = config_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result

def config_parameter(parameters, key, required=False, default=None, comment=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_nginx_config_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_nginx_config_parameter key expects a string but was given a %s' % type(key))
    if required and key not in parameters:
        raise AnsibleFilterError('manala_nginx_config_parameter requires a value for key %s' % key)

    value = parameters.get(key, default)

    if isinstance(value, list):
        result = '\n'.join(
            config_parameter({key: v}, key) for v in value
        )
    else:
        if value is True:
            value = 'on'
        elif value is False:
            value = 'off'
        elif isinstance(value, (string_types, Number)):
            pass
        else:
            AnsibleFilterError('manala_nginx_config_parameter value of an unknown type %s' % type(value))

        result = '%s %s;' % (key, value)

    if key not in parameters:
        if comment is True:
            result = '#' + result.replace('\n', '\n#')
        elif isinstance(comment, string_types):
            result = comment

    return result


class FilterModule(object):
    ''' Manala nginx config jinja2 filters '''

    def filters(self):
        filters = {
            'manala_nginx_config': config,
            'manala_nginx_config_section': config_section,
            'manala_nginx_config_parameter': config_parameter,
        }

        return filters
