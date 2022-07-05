# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: deploy_writable_dirs
    author: Manala (@manala)
    short_description: returns a curated writable dirs list
    description:
      - Takes a writable dirs list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        dirs = self._flatten(terms[0])
        default = terms[1]

        for dir in dirs:

            items = []

            # Short syntax
            if isinstance(dir, string_types):
                item = default.copy()
                item.update({
                    'dir': dir
                })
                items.append(item)
            else:

                # Must be a dict
                if not isinstance(dir, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(dir))

                # Check index key
                if 'dir' not in dir:
                    raise AnsibleError('Missing "dir" key')

                item = default.copy()
                item.update(dir)
                items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['dir'] == item['dir']:
                        results[i] = item
                        itemFound = True
                        break
                if not itemFound:
                    results.append(item)

        return results
