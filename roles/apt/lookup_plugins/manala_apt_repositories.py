from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text

import os
import re


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        if wantstate and wantstate not in ['present', 'absent']:
            raise AnsibleError('Expect a wanstate of "present" or "absent" but was "%s"' % to_text(wantstate))

        repositories = self._flatten(terms[0])
        repositoriesPatterns = terms[1]
        preferences = terms[2]
        exclusives = self._flatten(terms[3])
        dir = '/etc/apt/sources.list.d'

        itemDefault = {
            'state': 'present'
        }

        # Mark exclusive repositories as absent
        for repository in exclusives:
            item = itemDefault.copy()
            item.update({
                'file':  repository['path'],
                'state': 'absent'
            })
            results.append(item)

        # Handle repositories defined as reversed preferences
        for preference in preferences[::-1]:
            if 'repository' in preference:
                repositories.insert(0, preference['repository'])

        for repository in repositories:

            items = []

            item = itemDefault.copy()

            # Short syntax
            if isinstance(repository, string_types):
                item.update(
                    repositoriesPatterns.get(repository)
                )
            else:
                # Must be a dict
                if not isinstance(repository, dict):
                    raise AnsibleError('Expect a dict but was a %s' % type(repository))

                if 'pattern' in repository:
                    item.update(
                        repositoriesPatterns.get(repository.get('pattern'))
                    )

                item.update(repository)

                if item['state'] not in ['present', 'absent', 'ignore']:
                    raise AnsibleError('Expect a state of "present", "absent" or "ignore" but was "%s"' % to_text(item['state']))

                if item['state'] == 'ignore':
                    continue

                # Check index key
                if 'source' not in item:
                    raise AnsibleError('Expect "source" key')

            # Force file if not present
            if 'file' not in item:
                item.update({
                    'file': os.path.join(
                        dir,
                        re.sub(
                            '^deb (\\[.+\\] )?https?:\\/\\/([^ ]+)[ ].*$',
                            '\\2',
                            item['source']
                        )
                            .strip('/ ')
                            .replace('.', '_')
                            .replace('/', '_')
                            .replace('-', '_')
                            + '.list'
                    )
                })
            else:
                item.update({
                    'file': os.path.join(
                        dir,
                        item['file']
                    )
                })

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if ('source' in result and result['source'] == item['source']) or (result['file'] == item['file']):
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        # Filter by state
        if wantstate:
            results = [result for result in results if result.get('state') == wantstate]

        return results
