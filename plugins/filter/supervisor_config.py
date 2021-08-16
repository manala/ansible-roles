from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.filter.core import flatten

from numbers import Number


def config(sections, exclude=None):
    exclude = exclude or []
    if not isinstance(sections, dict):
        raise AnsibleFilterError('supervisor_config expects a dict but was given a %s' % type(sections))
    [sections.pop(key, None) for key in exclude]
    result = ''
    for section, parameters in sorted(iteritems(sections)):
        result += '[%s]%s\n\n' % (
            section,
            config_section(parameters)
        )
    return result.rstrip()


def config_section(parameters, exclude=None):
    exclude = exclude or []
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('supervisor_config_section expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = config_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result


def config_parameter(parameters, key, required=False, comment=False, **kwargs):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('supervisor_config_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('supervisor_config_parameter key expects a string but was given a %s' % type(key))

    if key in parameters:
        value = parameters.get(key)
    else:
        if required:
            raise AnsibleFilterError('supervisor_config_parameter requires a value for key %s' % key)
        if isinstance(comment, string_types):
            return comment
        if 'default' not in kwargs:
            raise AnsibleFilterError('supervisor_config_parameter missing a default value for key %s' % key)
        value = kwargs.get('default')

    if value is True:
        result = '%s=true' % key
    elif value is False:
        result = '%s=false' % key
    elif isinstance(value, (string_types, Number)):
        result = '%s=%s' % (key, value)
    elif isinstance(value, dict):
        result = '%s=' % key
        for k, v in sorted(iteritems(value)):
            result += '%s="%s",' % (k, v)
        result = result.rsplit(',', 1)[0]
    elif isinstance(value, list):
        value = flatten(value)
        result = '%s=%s' % (key, ','.join(value))
    else:
        raise AnsibleFilterError('supervisor_config_parameter value of an unknown type %s' % type(value))

    if key not in parameters and comment:
        result = ';' + result.replace('\n', '\n;')

    return result


class FilterModule(object):
    ''' Manala supervisor config jinja2 filters '''

    def filters(self):
        filters = {
            'supervisor_config': config,
            'supervisor_config_section': config_section,
            'supervisor_config_parameter': config_parameter,
        }

        return filters
