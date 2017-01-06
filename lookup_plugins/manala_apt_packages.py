from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)
        wantmap   = kwargs.pop('wantmap', False)

        itemDefault = {
            'state': 'present'
        }

        for term in self._flatten(terms):

            items = []

            if isinstance(term, basestring):
                # Short syntax
                item = itemDefault.copy()
                item.update({
                    'package': term
                })
            else:
                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')
                if not term.has_key('package'):
                    raise AnsibleError('Expect "package" key')
                # Expanded syntax
                item = itemDefault.copy()
                item.update(term)

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

        # Filter by state
        if wantstate:
            results = [result for result in results if result.get('state') == wantstate]

        # Map
        if wantmap:
            results = [result.get('package') for result in results]

        return results
