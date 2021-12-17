from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types

from numbers import Number


def environment(parameters, exclude=None):
    exclude = exclude or []
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('environment expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = environment_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result.lstrip()


def environment_parameter(parameters, key, required=False, comment=False, **kwargs):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('environment_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('environment_parameter key expects a string but was given a %s' % type(key))

    if key in parameters:
        value = parameters.get(key)
    else:
        if required:
            raise AnsibleFilterError('environment_parameter requires a value for key %s' % key)
        if isinstance(comment, string_types):
            return comment
        if 'default' not in kwargs:
            raise AnsibleFilterError('environment_parameter missing a default value for key %s' % key)
        value = kwargs.get('default')

    if value is None:
        result = ''
    elif isinstance(value, string_types):
        result = '%s="%s"' % (key, value)
    elif isinstance(value, Number):
        result = '%s=%s' % (key, value)
    else:
        raise AnsibleFilterError('environment_parameter value of an unknown type %s' % type(value))

    if key not in parameters and comment:
        result = '#' + result.replace('\n', '\n#')

    return result


class FilterModule(object):
    ''' Manala environment jinja2 filters '''

    def filters(self):
        filters = {
            'environment': environment,
            'environment_parameter': environment_parameter,
        }

        return filters
