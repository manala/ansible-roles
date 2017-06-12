from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        for term in self._flatten(terms):

            items = []

            # Short syntax
            if isinstance(term, basestring):
                items.append({
                    'src': term
                })
            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if not term.has_key('src'):
                    raise AnsibleError('Expect "src" key')

                items.append(term)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['src'] == item['src']:
                        results[i] = item
                        itemFound = True
                        break
                if not itemFound:
                    results.append(item)

        return results
