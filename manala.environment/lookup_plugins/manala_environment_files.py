from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        patterns = terms[1]
        terms    = terms[0]

        for term in self._flatten(terms):

            items = []

            if isinstance(term, basestring):
                # Pattern
                if not patterns.has_key(term):
                    raise AnsibleError('"%s" is not a valid pattern' % (term))
                items.append({
                    'file':   patterns.get(term).get('file'),
                    'export': patterns.get(term).get('export', False)
                })
            else:
                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')
                # Expanded syntax
                items.append({
                    'file':   term.get('file'),
                    'export': term.get('export', False)
                })


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

        return results
