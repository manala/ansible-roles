from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        holds = self._flatten(terms[0])
        exclusives = self._flatten(terms[1])

        itemDefault = {
            'state': 'present'
        }

        # Unhold exclusives
        for hold in exclusives:
            item = itemDefault.copy()
            item.update({
                'package': hold,
                'state': 'absent'
            })
            results.append(item)

        for hold in holds:

            items = []

            item = itemDefault.copy()

            # Short syntax
            if isinstance(hold, string_types):
                item.update({
                    'package': hold,
                    'state': 'present'
                })
            else:
                # Must be a dict
                if not isinstance(hold, dict):
                    raise AnsibleError('Expect a dict but was a %s' % type(hold))

                # Check package key
                if 'package' not in hold:
                    raise AnsibleError('Expect "package" key')

                # Deprecated
                if ('hold' in hold) and ('state' not in hold):
                    hold['state'] = 'present' if hold['hold'] else 'absent'

                item.update(hold)

                if item['state'] not in ['present', 'absent', 'ignore']:
                    raise AnsibleError('Expect a state of "present", "absent" or "ignore" but was "%s"' % to_text(item['state']))

                if item['state'] == 'ignore':
                    continue

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['package'] == item['package']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
