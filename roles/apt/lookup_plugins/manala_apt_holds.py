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
        exclusive = self._flatten(terms[1])

        itemDefault = {
            'hold': False
        }

        # Unhold exclusives
        for hold in exclusive:
            item = itemDefault.copy()
            item.update({
                'package': hold.split()[0],
                'state': hold.split()[1]
            })
            results.append(item)

        for hold in holds:

            items = []

            item = itemDefault.copy()

            # Short syntax
            if isinstance(hold, string_types):
                item.update({
                    'package': hold,
                    'hold': True
                })
            else:
                # Must be a dict
                if not isinstance(hold, dict):
                    raise AnsibleError('Expect a dict but was a %s' % type(hold))

                # Check index key
                if 'package' not in hold:
                    raise AnsibleError('Expect "package" key')

                item.update(hold)

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

        # Filter by applicables
        results = [result for result in results if (
            ('state' not in result)
            or (result.get('hold') and result.get('state') != 'hold')
            or (not result.get('hold') and result.get('state') == 'hold')
        )]

        return results
