from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types

from numbers import Number


def config(config, exclude=[]):
    if not isinstance(config, dict):
        raise AnsibleFilterError('manala_rsyslog_config expects a dict but was given a %s' % type(config))
    [config.pop(key, None) for key in exclude]
    result = config_parameters(config)
    return result.lstrip()


def config_parameters(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_rsyslog_config_parameters expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = config_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result


def config_parameter(parameters, key, default=None, comment=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_rsyslog_config_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_rsyslog_config_parameter key expects a string but was given a %s' % type(key))
    result = ''
    value = parameters.get(key, default)
    if isinstance(value, string_types):
        result = '%s %s' % (key, value)
    elif isinstance(value, Number):
        result = '%s %s' % (key, value)
    else:
        AnsibleFilterError('manala_rsyslog_config_parameter value of an unknown type %s' % type(value))
    if comment and key not in parameters:
        result = '#%s' % result
    return result


class FilterModule(object):
    ''' Manala rsyslog jinja2 filters '''

    def filters(self):
        filters = {
            'manala_rsyslog_config': config,
            'manala_rsyslog_config_parameters': config_parameters,
            'manala_rsyslog_config_parameter': config_parameter,
        }

        return filters
