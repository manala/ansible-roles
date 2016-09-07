from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        for term in self._flatten(terms):

            # Check index key
            if not term.has_key('user'):
                raise AnsibleError('Expect "user" key')

            items = []

            if term.has_key('authorized_keys'):
                item = term.copy()

                # Authorized Keys
                item.update({
                    'authorized_keys': '\n'.join(term.get('authorized_keys'))
                })

                items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['user'] == item['user']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
