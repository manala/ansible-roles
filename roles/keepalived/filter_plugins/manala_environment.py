from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types

from numbers import Number


def environment(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_environment expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = environment_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result.lstrip()

def environment_parameter(parameters, key, required=False, default=None, comment=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_environment_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_environment_parameter key expects a string but was given a %s' % type(key))
    if required and key not in parameters:
        raise AnsibleFilterError('manala_environment_parameter requires a value for key %s' % key)
    result = ''
    value = parameters.get(key, default)
    if isinstance(value, string_types):
        result = '%s="%s"' % (key, value)
    elif isinstance(value, Number):
        result = '%s=%s' % (key, value)
    else:
        AnsibleFilterError('manala_environment_parameter value of an unknown type %s' % type(value))
    if key not in parameters:
        if comment is True:
            result = '#' + result.replace('\n', '\n#')
        elif isinstance(comment, string_types):
            result = comment
    return result


class FilterModule(object):
    ''' Manala environment jinja2 filters '''

    def filters(self):
        filters = {
            'manala_environment': environment,
            'manala_environment_parameter': environment_parameter,
        }

        return filters
