from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        repositories_patterns = terms[1]
        preferences           = terms[2]

        # Preferences
        preferencePosition = 0
        for preference in preferences:

            if isinstance(preference, string_types):
                term = ((preference.split('@')[1])
                    if len(preference.split('@')) > 1 else
                (preference)).split(':')[0]
                terms[0].insert(preferencePosition, term)
                preferencePosition += 1

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, string_types):
                items.append(
                    repositories_patterns.get(term)
                )
            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                if 'pattern' in term:
                    item = repositories_patterns.get(term.get('pattern'))
                    item.update(term)
                    items.append(item)
                else:
                    # Check index key
                    if 'source' not in term:
                        raise AnsibleError('Expect "source" key')

                    items.append(term)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['source'] == item['source']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
