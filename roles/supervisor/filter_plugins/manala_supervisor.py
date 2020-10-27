from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types

from numbers import Number


def config(config, exclude=[]):
    if not isinstance(config, dict):
        raise AnsibleFilterError('manala_supervisor_config expects a dict but was given a %s' % type(config))
    [config.pop(key, None) for key in exclude]
    result = ''
    for section, parameters in sorted(iteritems(config)):
        result += '[%s]%s\n\n' % (
            section,
            config_parameters(parameters)
        )
    return result.rsplit('\n', 1)[0]


def config_parameters(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_supervisor_config_parameters expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = config_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result


def config_parameter(parameters, key, default=None, comment=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_supervisor_config_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_supervisor_config_parameter key expects a string but was given a %s' % type(key))
    result = ''
    value = parameters.get(key, default)
    if value is True:
        result = '%s=true' % key
    elif value is False:
        result = '%s=false' % key
    elif isinstance(value, dict):
        result = '%s=' % key
        for k, v in sorted(iteritems(value)):
            result += '%s="%s",' % (k, v)
        result = result.rsplit(',', 1)[0]
    elif isinstance(value, list):
        result = '%s=' % key
        result += ','.join(value)
    elif isinstance(value, string_types):
        result = '%s=%s' % (key, value)
    elif isinstance(value, Number):
        result = '%s=%s' % (key, value)
    else:
        AnsibleFilterError('manala_supervisor_config_parameter value of an unknown type %s' % type(value))
    if comment and not key in parameters:
        result = ';%s' % result
    return result


class FilterModule(object):
    ''' Manala supervisor jinja2 filters '''

    def filters(self):
        filters = {
            'manala_supervisor_config': config,
            'manala_supervisor_config_parameters': config_parameters,
            'manala_supervisor_config_parameter': config_parameter,
        }

        return filters
