from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def format_value(self, value):
        if (value is None):
            return 'null'
        elif (value is True):
            return 'true'
        elif (value is False):
            return 'false'
        else:
            return value

    def run(self, terms, variables=None, **kwargs):

        results = []

        for term in self._flatten(terms):

            # Term must be a dict
            if not isinstance(term, dict):
                raise AnsibleError('Expect a dict')

            items = []

            if term.has_key('name') and term.has_key('value'):
                # Expanded syntax
                items.append({
                    'name':  term.get('name'),
                    'value': self.format_value(term.get('value'))
                })
            else:
                # Short syntax
                items.append({
                    'name':  term.keys()[0],
                    'value': self.format_value(term.values()[0])
                })

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['name'] == item['name']:
                        results[i] = item
                        itemFound = True
                        break
                if not itemFound:
                    results.append(item)

        return results
