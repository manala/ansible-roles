from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.filter.core import to_nice_yaml

def yaml(parameters, exclude=[]):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_yaml expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = ''
    for key in sorted(parameters):
        parameter = yaml_parameter(parameters, key)
        if parameter:
            result += '\n%s' % parameter
    return result.lstrip()

def yaml_parameter(parameters, key, required=False, default=None, comment=False):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_yaml_parameter parameters expects a dict but was given a %s' % type(parameters))
    if not isinstance(key, string_types):
        raise AnsibleFilterError('manala_yaml_parameter key expects a string but was given a %s' % type(key))
    if required and key not in parameters:
        raise AnsibleFilterError('manala_yaml_parameter requires a value for key %s' % key)
    value = parameters.get(key, default)
    result = to_nice_yaml({key: value},).rstrip()
    if key not in parameters:
        if comment is True:
            result = '#' + result.replace('\n', '\n#')
        elif isinstance(comment, string_types):
            result = comment
    return result

def yaml_flatten(parameters, parent='', separator='.'):
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('manala_yaml_flatten expects a dict but was given a %s' % type(parameters))
    items = []
    for key, value in parameters.items():
        key = (parent + separator + key) if parent else key
        if isinstance(value, dict):
            items.extend(yaml_flatten(value, key, separator=separator).items())
        else:
            items.append((key, value))
    return dict(items)


class FilterModule(object):
    ''' Manala yaml jinja2 filters '''

    def filters(self):
        filters = {
            'manala_yaml': yaml,
            'manala_yaml_parameter': yaml_parameter,
            'manala_yaml_flatten': yaml_flatten,
        }

        return filters
