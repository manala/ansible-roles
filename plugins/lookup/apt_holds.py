# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: apt_holds
    author: Manala (@manala)
    short_description: returns a curated holds list
    description:
      - Takes a holds list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types
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
                    raise AnsibleError('Expected a dict but was a %s' % type(hold))

                # Check package key
                if 'package' not in hold:
                    raise AnsibleError('Missing "package" key')

                item.update(hold)

                if item['state'] not in ['present', 'absent', 'ignore']:
                    raise AnsibleError('Expected a state of "present", "absent" or "ignore" but was "%s"' % to_text(item['state']))

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
