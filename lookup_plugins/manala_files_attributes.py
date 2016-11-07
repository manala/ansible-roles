from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

import re

class LookupModule(LookupBase):

    def _default(self, defaults, path):
        result = {}
        for default in defaults:
            if re.search(default['path'], path):
                result.update(default)
        return result

    def run(self, terms, variables=None, **kwargs):

        results = []

        attributes = self._flatten(terms[0])
        defaults   = self._flatten(terms[1])

        for attribute in attributes:

            # Check index key
            if not attribute.has_key('path'):
                raise AnsibleError('Expect "path" key')

            items = []

            # State - Link Directory
            if attribute.has_key('state') and (attribute['state'] == 'link_directory'):
                item = self._default(defaults, attribute['path'])
                item.update(attribute)
                item.update({
                    'task': 'link_directory'
                })
                items.append(item)
            # State - Link File
            elif attribute.has_key('state') and (attribute['state'] == 'link_file'):
                item = self._default(defaults, attribute['path'])
                item.update(attribute)
                item.update({
                    'task': 'link_file'
                })
                items.append(item)
            else:
                # Template
                if attribute.has_key('template'):
                    item = self._default(defaults, attribute['path'])
                    item.update(attribute)
                    item.update({
                        'task': 'template'
                    })
                    items.append(item)
                # Content
                elif attribute.has_key('content'):
                    item = self._default(defaults, attribute['path'])
                    item.update(attribute)
                    item.update({
                        'task': 'content'
                    })
                    items.append(item)
                # Copy
                elif attribute.has_key('copy'):
                    item = self._default(defaults, attribute['path'])
                    item.update(attribute)
                    item.update({
                        'task': 'copy'
                    })
                    items.append(item)
                # Url
                elif attribute.has_key('url'):
                    item = self._default(defaults, attribute['path'])
                    item.update(attribute)
                    item.update({
                        'task': 'url'
                    })
                    items.append(item)
                # File
                else:
                    item = self._default(defaults, attribute['path'])
                    item.update(attribute)
                    item.update({
                        'task': 'file'
                    })
                    items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['path'] == item['path']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
