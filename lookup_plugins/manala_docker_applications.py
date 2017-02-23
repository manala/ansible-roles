from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        # Patterns
        patterns = terms[1]

        itemDefault = {
            'tag':         None,
            'rm':          None,
            'interactive': None,
            'tty':         None,
            'command':     None,
            'volumes':     {},
            'workdir':     None
        }

        for term in self._flatten(terms[0]):

            items = []

            # Short syntax
            if isinstance(term, basestring):
                item = itemDefault.copy()

                item.update({
                    'image':       term.split(':')[0],
                    'application': ((term.split('/')[1]).split(':')[0])
                        if len(term.split('/')) > 1 else
                    (term.split(':')[0])
                })

                # Pattern
                if patterns.has_key(term.split(':')[0]):
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
                if not term.has_key('application'):
                    raise AnsibleError('Expect "application" key')

                if not term.has_key('image'):
                    raise AnsibleError('Expect "image" key')

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
