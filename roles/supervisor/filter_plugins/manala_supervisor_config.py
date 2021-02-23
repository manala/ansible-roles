from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.filter.core import flatten

from numbers import Number


def config(sections, exclude=[]):
    if not isinstance(sections, dict):
        raise AnsibleFilterError('manala_supervisor_config expects a dict but was given a %s' % type(sections))
    [sections.pop(key, None) for key in exclude]
    result = ''
    for section, parameters in sorted(iteritems(sections)):
        result += '[%s]%s\n\n' % (
            section,
            config_section(parameters)
        )
    return result.rsplit('\n', 1)[0]


def config_section(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_supervisor_config_section expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = config_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result


def config_parameter(parameters, key, required=False, default=None, comment=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_supervisor_config_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_supervisor_config_parameter key expects a string but was given a %s' % type(key))
    if required and key not in parameters:
        raise AnsibleFilterError('manala_supervisor_config_parameter requires a value for key %s' % key)

    value = parameters.get(key, default)

    if isinstance(value, dict):
        result = '%s=' % key
        for k, v in sorted(iteritems(value)):
            result += '%s="%s",' % (k, v)
        result = result.rsplit(',', 1)[0]
    elif isinstance(value, list):
        value = flatten(value)
        result = '%s=%s' % (key, ','.join(value))
    else:
        if value is True:
            value = 'true'
        elif value is False:
            value = 'false'
        elif isinstance(value, (string_types, Number)):
            pass
        else:
            AnsibleFilterError('manala_supervisor_config_parameter value of an unknown type %s' % type(value))

        result = '%s=%s' % (key, value)

    if key not in parameters:
        if comment is True:
            result = ';' + result.replace('\n', '\n;')
        elif isinstance(comment, string_types):
            result = comment

    return result


class FilterModule(object):
    ''' Manala supervisor config jinja2 filters '''

    def filters(self):
        filters = {
            'manala_supervisor_config': config,
            'manala_supervisor_config_section': config_section,
            'manala_supervisor_config_parameter': config_parameter,
        }

        return filters
