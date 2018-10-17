from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)
        wantdeb   = kwargs.pop('wantdeb', None)
        wantmap   = kwargs.pop('wantmap', False)

        itemDefault = {
            'state': 'present',
            'deb':   False
        }

        for term in self._flatten(terms):

            items = []

            # Short syntax
            if isinstance(term, string_types):
                item = itemDefault.copy()
                item.update({
                    'package': term
                })
            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if 'package' not in term:
                    raise AnsibleError('Expect "package" key')

                item = itemDefault.copy()
                item.update(term)

            # Is a .deb ?
            if item.get('package').endswith('.deb'):
                item.update({
                    'deb': True
                })

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

        # Filter by deb
        if wantdeb is not None:
            results = [result for result in results if result.get('deb') == wantdeb]

        # Map
        if wantmap:
            results = [result.get('package') for result in results]

        return results
