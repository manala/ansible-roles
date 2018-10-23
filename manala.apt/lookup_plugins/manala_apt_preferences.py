from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

import os
import re

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        preferences          = self._flatten(terms[0])
        preferencesPatterns  = terms[1]
        repositoriesPatterns = terms[2]
        preferencesExclusive = self._flatten(terms[3])
        preferencesDir       = terms[4]

        itemDefault = {
            'state': 'present'
        }

        # Mark exclusive preferences as absent
        for preference in preferencesExclusive:
            item = itemDefault.copy()
            item.update({
                'file':  preference['path'],
                'state': 'absent'
            })
            results.append(item)

        for preference in preferences:

            items = []

            # Short syntax
            if isinstance(preference, string_types):
                item = itemDefault.copy()
                item.update({
                    'file': preference
                        .split('@')[0]
                        .split(':')[0]
                        .replace('.', '_'),
                    'package': preferencesPatterns.get(
                        preference.split('@')[0],
                        (preference.split('@')[0])
                            if len(preference.split('@')) > 1 else
                        ('*')
                    ),
                    'pin': repositoriesPatterns[
                        (
                            (preference.split('@')[1])
                                if len(preference.split('@')) > 1 else
                            (preference)
                        ).split(':')[0]
                    ].get(
                        'pin',
                        'origin ' + re.sub(
                            'deb (\\[.+\\] )?https?:\\/\\/([^\\/ ]+)[\\/ ].*$',
                            '\\2',
                            repositoriesPatterns[
                                (
                                    (preference.split('@')[1])
                                        if len(preference.split('@')) > 1 else
                                    (preference)
                                ).split(':')[0]
                            ].get('source')
                        )
                    ),
                    'priority': int(
                        (preference.split(':')[1])
                            if len(preference.split(':')) > 1 else
                        (900)
                    )
                })

            else:

                # Must be a dict
                if not isinstance(preference, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if 'file' not in preference:
                    raise AnsibleError('Expect "file" key')

                item = itemDefault.copy()
                item.update(preference)

            item.update({
                'file': os.path.join(preferencesDir, item['file'])
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
