# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: php_sapis
    author: Manala (@manala)
    short_description: returns a curated sapis list
    description:
      - Takes an sapis list and returns it curated and optionally state filtered.
    options:
      wantstate:
        description: filter list items by enabled
      wantmap:
        description: format result list as a map
'''


from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        if wantstate and wantstate not in ['present', 'absent']:
            raise AnsibleError('Expected a wanstate of "present" or "absent" but was "%s"' % to_text(wantstate))

        wantmap = kwargs.pop('wantmap', False)

        sapis = self._flatten(terms[0])
        sapisAvailable = terms[1]

        itemDefault = {
            'state': 'present'
        }

        for sapi in sapis:

            items = []

            # Short syntax
            if isinstance(sapi, string_types):
                item = itemDefault.copy()
                item.update({
                    'sapi': sapi
                })
            else:

                # Must be a dict
                if not isinstance(sapi, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(sapi))

                # Check index key
                if 'sapi' not in sapi:
                    raise AnsibleError('Missing "sapi" key')

                item = itemDefault.copy()
                item.update(sapi)

            # Known sapi ?
            if item['sapi'] not in sapisAvailable:
                raise AnsibleError('Unknown "%s" sapi' % item['sapi'])

            if item['state'] not in ['present', 'absent', 'ignore']:
                raise AnsibleError('Expected a state of "present", "absent" or "ignore" but was "%s"' % to_text(item['state']))

            if item['state'] == 'ignore':
                continue

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['sapi'] == item['sapi']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        # Filter by state
        if wantstate is not None:
            results = [result for result in results if result.get('state') == wantstate]

        # Map
        if wantmap:
            results = [result.get('sapi') for result in results]

        return results
