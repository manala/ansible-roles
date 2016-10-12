from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        # Version parameters
        version = terms[1]

        wantstate   = kwargs.pop('wantstate', None)
        wantenabled = kwargs.pop('wantenabled', None)
        wantmap     = kwargs.pop('wantmap', False)

        ##############
        # Extensions #
        ##############

        itemDefault = {
            'state':   'present',
            'enabled': None
        }

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, basestring):
                item = itemDefault.copy()
                item.update({
                    'extension': term
                })
            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if not term.has_key('extension'):
                    raise AnsibleError('Expect "extension" key')

                item = itemDefault.copy()
                item.update(term)

            # Known as a sapi ?
            if item.get('extension') in version['sapis']:
                raise AnsibleError('Extension "' + item.get('extension') + '" is known as a sapi')

            # Already embedded extension ?
            if item.get('extension') in version['extensions']:
                continue

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['extension'] == item['extension']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        # Filter by state
        if wantstate is not None:
            results = [result for result in results if result.get('state') == wantstate]

        # Filter by enabled
        if wantenabled is not None:
            results = [result for result in results if result.get('enabled') == wantenabled]

        # Map
        if wantmap:
            results = [result.get('extension') for result in results]

        return results
