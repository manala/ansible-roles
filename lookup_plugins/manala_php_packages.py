from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        # Pecl
        pecl = terms[1]

        # Version parameters
        version = terms[2]

        for term in self._flatten(terms[0]):

            items = []

            # Pecl
            if term in pecl.get('extensions'):
                items.append(version.get('package_pecl_prefix') + term)
            else:
                items.append(version.get('package_prefix') + term)

            # Merge
            for item in items:
                if item not in results:
                    results.append(item)

        return results
