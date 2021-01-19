from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.filter.core import flatten

from numbers import Number


def config(sections, exclude=[]):
    if not isinstance(sections, dict):
        raise AnsibleFilterError('manala_php_blackfire_config expects a dict but was given a %s' % type(sections))
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
        raise AnsibleFilterError('manala_php_blackfire_config_section expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = config_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result


def config_parameter(parameters, key, required=False, default=None, comment=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_php_blackfire_config_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_php_blackfire_config_parameter key expects a string but was given a %s' % type(key))
    if required and key not in parameters:
        raise AnsibleFilterError('manala_php_blackfire_config_parameter requires a value for key %s' % key)

    value = parameters.get(key, default)

    if isinstance(value, (string_types, Number)):
        pass
    else:
        AnsibleFilterError('manala_php_blackfire_config_parameter value of an unknown type %s' % type(value))

    result = '%s=%s' % (key, value)

    if key not in parameters:
        if comment is True:
            result = '; ' + result.replace('\n', '\n; ')
        elif isinstance(comment, string_types):
            result = comment

    return result


class FilterModule(object):
    ''' Manala php blackfire config jinja2 filters '''

    def filters(self):
        filters = {
            'manala_php_blackfire_config': config,
            'manala_php_blackfire_config_section': config_section,
            'manala_php_blackfire_config_parameter': config_parameter,
        }

        return filters
