# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: php_packages
    author: Manala (@manala)
    short_description: returns a curated packages list
    description:
      - Takes an packages list and returns it curated.
'''


from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        packages = self._flatten(terms[0])
        version = terms[1]

        for package in packages:

            items = []

            # Extensions
            items.append('php%s-%s' % (version, package))

            # Merge
            for item in items:
                if item not in results:
                    results.append(item)

        return results
