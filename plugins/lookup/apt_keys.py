# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: apt_keys
    author: Manala (@manala)
    short_description: returns a curated keys list
    description:
      - Takes a keys list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types

import os.path


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        if wantstate and wantstate not in ['present', 'absent']:
            raise AnsibleError('Expected a wanstate of "present" or "absent" but was "%s"' % to_text(wantstate))

        keys = self._flatten(terms[0])
        keysPatterns = terms[1]
        repositories = terms[2]
        exclusives = self._flatten(terms[3])
        dir = terms[4]

        itemDefault = {
            'state': 'present'
        }

        # Mark exclusive keys as absent
        for key in exclusives:
            item = itemDefault.copy()
            item.update({
                'file': key['path'],
                'state': 'absent'
            })
            results.append(item)

        # Handle repositories defined as reversed preferences
        for repository in repositories[::-1]:
            if 'key' in repository:
                keys.insert(0, repository['key'])

        for key in keys:

            items = []

            item = itemDefault.copy()

            # Short syntax
            if isinstance(key, string_types):
                item.update({
                    'key': key
                })
            else:
                # Must be a dict
                if not isinstance(key, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(key))

                item.update(key)

                if item['state'] not in ['present', 'absent', 'ignore']:
                    raise AnsibleError('Expected a state of "present", "absent" or "ignore" but was "%s"' % to_text(item['state']))

                if item['state'] == 'ignore':
                    continue

            if 'key' in item:
                keyPattern = item['key']
                if keyPattern not in keysPatterns:
                    raise AnsibleError('unable to find "%s" key pattern' % keyPattern)
                item = {
                    **keysPatterns[keyPattern],
                    **item,
                }

            # Legacy
            if 'keyserver' in item:
                raise AnsibleError('Deprecated "keyserver" key, please use "url" instead')
            if 'id' in item:
                raise AnsibleError('Deprecated "id" key, please use "checksum" instead')

            # Check index key
            if 'file' not in item:
                raise AnsibleError('Missing "file" key')

            item.update({
                'file': os.path.join(
                    dir,
                    item['file']
                )
            })

            # Check required keys
            if 'url' not in item:
                raise AnsibleError('Missing "url" key in key file "%s"' % item['file'])

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['file'] == item['file']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        # Filter by state
        if wantstate:
            results = [result for result in results if result.get('state') == wantstate]

        return results
