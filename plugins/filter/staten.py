from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_text
from ansible.module_utils.common._collections_compat import Iterable


def staten_ignore(values):
    if not isinstance(values, Iterable):
        raise AnsibleFilterError('Expected an iterable but was a %s' % type(values))

    results = []

    for value in values:
        if isinstance(value, dict) and value.get('state') == 'ignore':
            continue

        results.append(value)

    return results


def staten(values, **kwargs):
    if not isinstance(values, Iterable):
        raise AnsibleFilterError('Expected an iterable but was a %s' % type(values))

    results = []

    want = kwargs.pop('want', None)

    if want and want not in ['present', 'absent']:
        raise AnsibleFilterError('Expected a want of "present" or "absent" but was "%s"' % to_text(want))

    values = staten_ignore(values)

    for value in values:
        # Short syntax
        if not isinstance(value, dict):
            item = value

            # In short syntax, 'present' state is implicit
            if want and want != 'present':
                continue
        else:
            # Default state
            item = {
                'state': 'present'
            }
            item.update(value)

            if item['state'] not in ['present', 'absent']:
                raise AnsibleFilterError('Expected a state of "present" or "absent" but was "%s"' % to_text(item['state']))

            if want and want != item['state']:
                continue

        results.append(item)

    return results


class FilterModule(object):
    ''' Manala staten filter '''

    def filters(self):
        filters = {
            'staten_ignore': staten_ignore,
            'staten': staten,
        }

        return filters
