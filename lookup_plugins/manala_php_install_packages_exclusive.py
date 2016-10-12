from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        packagesAbsents = []

        # Packages
        packages = self._flatten(terms[0])

        # Packages presents
        packagesPresents = self._flatten(terms[1])

        # Packages dependencies
        packagesDependencies = self._flatten(terms[2])

        # Version parameters
        version = terms[5]

        # Exclusive - Sapis
        exclusive = terms[3]

        if exclusive:
            packagesSapis         = list(set(packages) & set(version['sapis']))
            packagesSapisPresents = list(set(packagesPresents) & set(version['sapis']))

            packagesAbsents += list(set(packagesSapisPresents) - set(packagesSapis))

        # Exclusive - Extensions
        exclusive = terms[4]

        if exclusive:
            packagesExtensions         = list(set(packages) - set(version['sapis']))
            packagesExtensionsPresents = list(set(packagesPresents) - set(version['sapis']))

            packagesAbsents += list(set(packagesExtensionsPresents) - set(packagesExtensions))

        # Remove packages dependencies
        packagesAbsents = list(set(packagesAbsents) - set(packagesDependencies))

        return packagesAbsents
