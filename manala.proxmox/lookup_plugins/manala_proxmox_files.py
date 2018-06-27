from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

import os

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        files          = self._flatten(terms[0])
        filesExclusive = self._flatten(terms[1])
        filesDir       = terms[2]

        itemDefault = {
            'state': 'present'
        }

        # Mark exclusive files as absent
        for file in filesExclusive:
            item = itemDefault.copy()
            item.update({
                'file':  file['path'],
                'state': 'absent'
            })
            results.append(item)

        for file in files:

            items = []

            # Short syntax
            if isinstance(file, basestring):
                item = itemDefault.copy()
                item.update({
                    'url': file
                })
            else:
                # Must be a dict
                if not isinstance(file, dict):
                    raise AnsibleError('Expect a dict')

                if (not file.has_key('file')) and (not file.has_key('url')):
                    raise AnsibleError('Expect "url" or "file" key')

                if (file.get('state') == 'present') and (not file.has_key('url')):
                    raise AnsibleError('Expect "url" key for present state')

                item = itemDefault.copy()
                item.update(file)

            if item.has_key('url') and not item.has_key('file'):
                item.update({
                    'file': os.path.basename(item['url'])
                })

            item.update({
                'file': os.path.join(filesDir, item['file'])
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

        # Filter by state
        if wantstate:
            results = [result for result in results if result.get('state') == wantstate]

        return results
