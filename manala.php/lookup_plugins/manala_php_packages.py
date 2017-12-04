from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        # Version
        version = terms[1]

        # Extensions - Pecl
        extensionsPecl          = terms[2]
        extensionsPeclVersioned = terms[3]

        for term in self._flatten(terms[0]):

            items = []

            # Extensions
            if (term in extensionsPecl) and (not extensionsPeclVersioned):
                items.append('php-' + term)
            else:
                items.append('php' + version + '-' + term)

            # Merge
            for item in items:
                if item not in results:
                    results.append(item)

        return results
