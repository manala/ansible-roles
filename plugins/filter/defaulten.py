from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_text
from ansible.module_utils.common._collections_compat import Iterable


def defaulten(values, **kwargs):
    if not isinstance(values, Iterable):
        raise AnsibleFilterError('Expected an iterable but was a %s' % type(values))

    results = []

    default = kwargs.pop('default', None)

    # default must be a dict
    if not isinstance(default, dict):
        raise AnsibleFilterError('Expected default as a dict but was a "%s"' % to_text(default))

    for value in values:
        # value must be a dict
        if not isinstance(value, dict):
            raise AnsibleFilterError('Expected value from values as a dict but was a "%s"' % to_text(value))

        item = default.copy()
        item.update(value)

        results.append(item)

    return results


class FilterModule(object):
    ''' Manala defaulten filter '''

    def filters(self):
        filters = {
            'defaulten': defaulten,
        }

        return filters
