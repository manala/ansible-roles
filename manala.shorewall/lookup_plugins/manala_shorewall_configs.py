from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

import os

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        configs    = self._flatten(terms[0])
        configsDir = terms[1]

        itemDefault = {}

        for config in configs:

            items = []

            # Must be a dict
            if not isinstance(config, dict):
                raise AnsibleError('Expect a dict')

            # Check index key
            if 'file' not in config:
                raise AnsibleError('Expect "file" key')

            item = itemDefault.copy()
            item.update(config)
            item.update({
                'file': os.path.join(configsDir, item['file'])
            })

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['file'] == item['file']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
