from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        dirs    = self._flatten(terms[0])
        default = terms[1]

        for dir in dirs:

            items = []

            # Dir as a single line
            if isinstance(dir, string_types):
                item = default.copy()
                item.update({
                    'dir': dir
                })
                items.append(item)
            else:

                # Must be a dict
                if not isinstance(dir, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if 'dir' not in dir:
                    raise AnsibleError('Expect "dir" key')

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
