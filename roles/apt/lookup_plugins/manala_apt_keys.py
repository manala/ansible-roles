from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        keys = self._flatten(terms[0])
        keysPatterns = terms[1]
        repositories = terms[2]

        itemDefault = {}

        # Handle repositories defined as reversed preferences
        for repository in repositories[::-1]:
            if 'key' in repository:
                keys.insert(0, repository.get('key'))

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
                    raise AnsibleError('Expect a dict but was a %s' % type(key))

                # Check id key
                if 'id' not in key:
                    raise AnsibleError('Expect "id" key')

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
