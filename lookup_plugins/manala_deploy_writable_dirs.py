from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        itemDefault = {
            'mode': variables['manala_deploy_writable_dirs_mode']
        }

        for term in self._flatten(terms):

            items = []

            # Dir as a single line
            if isinstance(term, basestring):
                item = itemDefault.copy()
                item.update({
                    'dir': term
                })
                items.append(item)
            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if not term.has_key('dir'):
                    raise AnsibleError('Expect "dir" key')

                item = itemDefault.copy()
                item.update(term)
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
