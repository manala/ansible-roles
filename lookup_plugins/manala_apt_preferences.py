from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

import re

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        preferences_patterns  = terms[1]
        repositories_patterns = terms[2]

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, basestring):
                items.append({
                    'file': term
                        .split('@')[0]
                        .split(':')[0]
                        .replace('.', '_'),
                    'package': preferences_patterns.get(
                        term.split('@')[0],
                        (term.split('@')[0])
                            if len(term.split('@')) > 1 else
                        ('*')
                    ),
                    'pin': repositories_patterns[
                        (
                            (term.split('@')[1])
                                if len(term.split('@')) > 1 else
                            (term)
                        ).split(':')[0]
                    ].get(
                        'pin',
                        'origin ' + re.sub(
                            'deb (\\[.+\\] )?https?:\\/\\/([^\\/ ]+)[\\/ ].*$',
                            '\\2',
                            repositories_patterns[
                                (
                                    (term.split('@')[1])
                                        if len(term.split('@')) > 1 else
                                    (term)
                                ).split(':')[0]
                            ].get('source')
                        )
                    ),
                    'priority': int(
                        (term.split(':')[1])
                            if len(term.split(':')) > 1 else
                        (900)
                    )
                })

            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if not term.has_key('file'):
                    raise AnsibleError('Expect "file" key')

                items.append(term)

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
