from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        for term in self._flatten(terms):

            items = []

            if isinstance(term, basestring):
                # Short syntax
                items.append({
                    'package': term,
                    'state':   'present'
                })
            else:
                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')
                if not term.has_key('package'):
                    raise AnsibleError('Expect "package" key')
                # Expanded syntax
                items.append(term)

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
