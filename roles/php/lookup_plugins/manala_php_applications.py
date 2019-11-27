from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        # Patterns
        patterns = terms[1]

        itemDefault = {
            'version':        None,
            'source':         None,
            'source_version': None
        }

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, string_types):
                item = itemDefault.copy()

                # Pattern
                if term.split('@')[0] not in patterns:
                    print(term.split('@')[0])
                    raise AnsibleError('Unknown pattern')

                item.update(patterns.get(term.split('@')[0]))

                item.update({
                    'application': term.split('@')[0],
                    'version':     (term.split('@')[1])
                        if len(term.split('@')) > 1 else
                    (None)
                })

            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if 'application' not in term:
                    raise AnsibleError('Expect "application" key')

                item = itemDefault.copy()

                # Pattern
                if term.get('application') in patterns:
                    item.update(patterns.get(term.get('application')))

                item.update(term)

            # Source version
            if item.get('source_version') and item.get('version'):
                item.update({
                    'source': item.get('source_version').format(version=item.get('version'))
                })

            # No source
            if not item.get('source'):
                raise AnsibleError('No source')

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
