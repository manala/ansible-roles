from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        # Patterns
        patterns = terms[1]

        itemDefault = {
            'tag': None,
            'rm': None,
            'interactive': None,
            'tty': None,
            'command': None,
            'volumes': {},
            'environment': {},
            'workdir': None
        }

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, string_types):
                item = itemDefault.copy()

                item.update({
                    'image': term.split(':')[0],
                    'application': ((term.split('/')[1]).split(':')[0])
                        if len(term.split('/')) > 1 else
                    (term.split(':')[0])
                })

                # Pattern
                if term.split(':')[0] in patterns:
                    item.update(patterns.get(term.split(':')[0]))

                # Tag
                if len(term.split(':')) > 1:
                    item.update({
                        'tag': term.split(':')[1]
                    })
            else:

                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                # Check index key
                if 'application' not in term:
                    raise AnsibleError('Expect "application" key')

                item = itemDefault.copy()

                item.update(term)

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['application'] == item['application']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
