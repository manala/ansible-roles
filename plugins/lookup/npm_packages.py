# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: npm_packages
    author: Manala (@manala)
    short_description: returns a curated packages list
    description:
      - Takes a packages list and returns it curated.
'''


from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        packages = self._flatten(terms)

        itemDefault = {}

        for package in packages:

            items = []

            item = itemDefault.copy()

            # Short syntax
            if isinstance(package, string_types):
                item.update({
                    'package': package
                })
            else:

                # Check index key
                if 'package' not in package:
                    raise AnsibleError('Missing "package" key')

                item.update(package)

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['package'] == item['package']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
