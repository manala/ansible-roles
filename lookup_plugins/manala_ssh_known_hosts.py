from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        patterns = terms[1]

        for term in self._flatten(terms[0]):

            items = []

            if isinstance(term, basestring):
                # Short syntax
                item = patterns.get(term)
            else:
                # Must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')
                if not term.has_key('host'):
                    raise AnsibleError('Expect "host" key')
                item = term.copy()

            # File
            if item.has_key('file'):
                item.pop('key', None)
                # Relative
                if not item.get('file').startswith('/'):
                    item.update({
                        'file': variables['role_path'] + '/' + item.get('file')
                    })

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['host'] == item['host']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
