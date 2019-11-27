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

            item = itemDefault.copy()

            # Short syntax
            if isinstance(preference, string_types):
                item.update({
                    'preference': preference
                })
            else:
                # Must be a dict
                if not isinstance(preference, dict):
                    raise AnsibleError('Expect a dict')
                item.update(preference)

            if 'preference' in item:
                pattern = item['preference']
                if 'file' not in item:
                    item.update({
                        'file': pattern
                            .split('@')[0]
                            .split(':')[0]
                            .replace('.', '_')
                    })
                if 'package' not in item:
                    item.update({
                        'package': preferencesPatterns.get(
                            pattern.split('@')[0],
                            (pattern.split('@')[0])
                                if len(pattern.split('@')) > 1 else
                            ('*')
                        )
                    })
                if 'pin' not in item:
                    item.update({
                        'pin': repositoriesPatterns[
                            (
                                (pattern.split('@')[1])
                                    if len(pattern.split('@')) > 1 else
                                (pattern)
                            ).split(':')[0]
                        ].get(
                            'pin',
                            'origin ' + re.sub(
                                'deb (\\[.+\\] )?https?:\\/\\/([^\\/ ]+)[\\/ ].*$',
                                '\\2',
                                repositoriesPatterns[
                                    (
                                        (pattern.split('@')[1])
                                            if len(pattern.split('@')) > 1 else
                                        (pattern)
                                    ).split(':')[0]
                                ].get('source')
                            )
                        )
                    })
                if 'priority' not in item:
                    item.update({
                        'priority': int(
                            (pattern.split(':')[1])
                                if len(pattern.split(':')) > 1 else
                            (900)
                        )
                    })

            # Check index key
            if 'file' not in item:
                raise AnsibleError('Expect "file" key')

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
