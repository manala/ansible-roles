from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.filter.core import to_nice_json


def json(parameters, exclude=None):
    exclude = exclude or []
    if not isinstance(parameters, dict):
        raise AnsibleFilterError('json expects a dict but was given a %s' % type(parameters))
    [parameters.pop(key, None) for key in exclude]
    result = to_nice_json(parameters)
    return result


class FilterModule(object):
    ''' Manala json jinja2 filters '''

    def filters(self):
        filters = {
            'json': json,
        }

        return filters
