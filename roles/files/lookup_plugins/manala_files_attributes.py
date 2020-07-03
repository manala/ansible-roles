from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

import re


class LookupModule(LookupBase):

    def _default(self, defaults, path):
        result = {}
        for default in defaults:
            if ('path' not in default) or (re.search(default['path'], path)):
                result.update(default)
        return result

    def run(self, terms, variables=None, **kwargs):

        results = []

        attributes = self._flatten(terms[0])
        defaults = self._flatten(terms[1])

        for attribute in attributes:

            # Check index key
            if 'path' not in attribute:
                raise AnsibleError('Expect "path" key')

            items = []

            # State - Link Directory
            if 'state' in attribute and (attribute['state'] == 'link_directory'):
                if 'src' not in attribute:
                    raise AnsibleError('Expect "src" key')
                item = {
                    'path': attribute['path'],
                    'src': attribute['src'],
                    'force': attribute.get('force', False),
                    'directory': self._default(defaults, attribute['src']),
                    'link': self._default(defaults, attribute['path']),
                    'task': 'link_directory'
                }
                item['directory'].update(attribute)
                items.append(item)
            # State - Link File
            elif 'state' in attribute and (attribute['state'] == 'link_file'):
                if 'src' not in attribute:
                    raise AnsibleError('Expect "src" key')
                item = {
                    'path': attribute['path'],
                    'src': attribute['src'],
                    'force': attribute.get('force', False),
                    'file': self._default(defaults, attribute['path']),
                    'link': self._default(defaults, attribute['path']),
                    'task': 'link_file'
                }
                item['file'].update(attribute)
                item['link'].update(attribute)
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
