from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        # Patterns
        patterns = terms[1]

        itemDefault = {
            'version': 'latest'
        }

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, basestring):
                item = itemDefault.copy()

                # Pattern
                if not patterns.has_key(term.split('@')[0]):
                    raise AnsibleError('Unknown pattern')

                item.update(patterns.get(term.split('@')[0]))

                # Version
                if len(term.split('@')) > 1:
                    item.update({
                        'version': term.split('@')[1]
                    })
            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if not term.has_key('application'):
                    raise AnsibleError('Expect "application" key')

                if not term.has_key('image'):
                    raise AnsibleError('Expect "image" key')

                item = itemDefault.copy()

                item.update(term)

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['application'] == item['application']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
