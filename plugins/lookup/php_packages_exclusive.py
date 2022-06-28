# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: php_packages_exclusive
    author: Manala (@manala)
    short_description: returns a curated absent packages list
    description:
      - Takes some packages list and returns a curated absent packages list.
'''


from ansible.plugins.lookup import LookupBase

import re


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        packagesAbsents = []

        # Packages
        packages = self._flatten(terms[0])

        # Packages availables sapis
        packagesAvailablesSapis = terms[1]

        # Packages presents
        packagesPresents = []
        for term in self._flatten(terms[2]):
            # package[0] -> Status
            # package[1] -> Name
            package = term.split('    ')
            if package[0] == 'install ok installed' and (package[1].startswith('php-') or re.search('^php[1-9]+', package[1])):
                packagesPresents.append(package[1])

        # Packages dependencies
        packagesDependencies = []
        for term in self._flatten(terms[3]):
            if not term.startswith('Package '):
                packagesDependencies = list(set(packagesDependencies) | set(term.split()))

        # Exclusive - Sapis
        exclusiveSapis = terms[4]

        if exclusiveSapis:
            # Packages sapis we *WANT*
            packagesSapis = list(set(packages) & set(packagesAvailablesSapis))
            # Packages sapis *ALREADY PRESENTS*
            packagesSapisPresents = list(set(packagesPresents) & set(packagesAvailablesSapis))

            # Simple diff to get packages sapis we *DON'T WANT*
            packagesAbsents += list(set(packagesSapisPresents) - set(packagesSapis))

        # Exclusive - Extensions
        exclusiveExtensions = terms[5]

        if exclusiveExtensions:
            # Packages extensions we *WANT*
            packagesExtensions = list(set(packages) - set(packagesAvailablesSapis))
            # Packages extensions *ALREADY PRESENTS*
            packagesExtensionsPresents = list(set(packagesPresents) - set(packagesAvailablesSapis))

            packagesAbsents += list(set(packagesExtensionsPresents) - set(packagesExtensions))

        # Remove packages dependencies
        packagesAbsents = list(set(packagesAbsents) - set(packagesDependencies))

        return packagesAbsents
