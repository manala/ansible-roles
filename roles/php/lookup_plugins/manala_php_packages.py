from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        packages = self._flatten(terms[0])
        version = terms[1]

        extensionsPecl = terms[2]
        extensionsPeclVersioned = terms[3]

        for package in packages:

            items = []

            # Extensions
            if (package in extensionsPecl) and (not extensionsPeclVersioned):
                items.append('php-%s' % package)
            else:
                items.append('php%s-%s' % (version, package))

            # Merge
            for item in items:
                if item not in results:
                    results.append(item)

        return results
