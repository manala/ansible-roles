from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        for term in self._flatten(terms):

            # Check index key
            if not term.has_key('path'):
                raise AnsibleError('Expect "path" key')

            items = []

            # State - Link Directory
            if term.has_key('state') and (term['state'] == 'link_directory'):
                item = term.copy()
                item.update({
                    'task': 'link_directory'
                })
                items.append(item)
            else:
                # Template
                if term.has_key('template'):
                    item = term.copy()
                    item.update({
                        'task': 'template'
                    })
                    items.append(item)
                # Content
                elif term.has_key('content'):
                    item = term.copy()
                    item.update({
                        'task': 'content'
                    })
                    items.append(item)
                # Copy
                elif term.has_key('copy'):
                    item = term.copy()
                    item.update({
                        'task': 'copy'
                    })
                    items.append(item)
                # Url
                elif term.has_key('url'):
                    item = term.copy()
                    item.update({
                        'task': 'url'
                    })
                    items.append(item)
                # File
                else:
                    item = term.copy()
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
