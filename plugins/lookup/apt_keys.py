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


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        keys = self._flatten(terms[0])
        keysPatterns = terms[1]
        repositories = terms[2]

        itemDefault = {}

        # Handle repositories defined as reversed preferences
        for repository in repositories[::-1]:
            key = repository.get('key')
            if key:
                keys.insert(0, key)

        for key in keys:

            items = []

            item = itemDefault.copy()

            # Short syntax
            if isinstance(key, string_types):
                item.update(
                    keysPatterns.get(key)
                )
            else:
                # Must be a dict
                if not isinstance(key, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(key))

                # Check id key
                if 'id' not in key:
                    raise AnsibleError('Missing "id" key')

                item.update(key)

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['id'] == item['id']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
