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
            if 'path' not in attribute:
                raise AnsibleError('Expect "path" key')

            items = []

            # State - Link Directory
            if  'state' in attribute and (attribute['state'] == 'link_directory'):
                if 'src' not in attribute:
                    raise AnsibleError('Expect "src" key')
                # Directory (src)
                item = self._default(defaults, attribute['src'])
                item.update(attribute)
                item.update({
                    'path':  attribute['src'],
                    'src': variables['omit'],
                    'state': 'directory',
                    'task':  'file'
                })
                items.append(item)
                # Link (path)
                item = self._default(defaults, attribute['path'])
                item.update({
                    'path':  attribute['path'],
                    'src':   attribute['src'],
                    'state': 'link',
                    'task':  'file'
                })
                items.append(item)
            # State - Link File
            elif 'state' in attribute and (attribute['state'] == 'link_file'):
                item = self._default(defaults, attribute['path'])
                item.update(attribute)
                item.update({
                    'task': 'link_file'
                })
                items.append(item)
            else:
                # Template
                if 'template' in attribute:
                    item = self._default(defaults, attribute['path'])
                    item.update(attribute)
                    item.update({
                        'task': 'template'
                    })
                    items.append(item)
                # Content
                elif 'content' in attribute:
                    item = self._default(defaults, attribute['path'])
                    item.update(attribute)
                    item.update({
                        'task': 'content'
                    })
                    items.append(item)
                # Copy
                elif 'copy' in attribute:
                    item = self._default(defaults, attribute['path'])
                    item.update(attribute)
                    item.update({
                        'task': 'copy'
                    })
                    items.append(item)
                # Url
                elif 'url' in attribute:
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
