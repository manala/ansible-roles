from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        keys_patterns = terms[1]
        repositories  = terms[2]

        # Repositories
        repositoryPosition = 0
        for repository in repositories:

            if repository.has_key('key'):
                terms[0].insert(repositoryPosition, repository.get('key'))
                repositoryPosition += 1

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, basestring):
                items.append(
                    keys_patterns.get(term)
                )
            else:
                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if not term.has_key('id'):
                    raise AnsibleError('Expect "id" key')

                items.append(term)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['id'] == item['id']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
