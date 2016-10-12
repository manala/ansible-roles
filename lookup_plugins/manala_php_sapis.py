from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        # Version parameters
        version = terms[1]

        wantstate = kwargs.pop('wantstate', None)
        wantmap   = kwargs.pop('wantmap', False)

        #########
        # Sapis #
        #########

        itemDefault = {
            'state': 'present'
        }

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, basestring):
                item = itemDefault.copy()
                item.update({
                    'sapi': term
                })
            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if not term.has_key('sapi'):
                    raise AnsibleError('Expect "sapi" key')

                item = itemDefault.copy()
                item.update(term)

            # Known sapi ?
            if item.get('sapi') not in version['sapis']:
                raise AnsibleError('Unknown sapi "' + item.get('sapi') + '"')

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
