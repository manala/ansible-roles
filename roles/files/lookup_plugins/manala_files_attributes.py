from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

import re


class LookupModule(LookupBase):

    def _recursive_flatten(self, terms):
        if not isinstance(terms, list):
            raise AnsibleError('Expect a list but was a %s' % type(terms))
        ret = []
        for term in terms:
            if isinstance(term, (list, tuple)):
                ret.extend(
                    self._recursive_flatten(term)
                )
            else:
                ret.append(term)
        return ret

    def _default(self, defaults, path):
        result = {}
        for default in defaults:
            if ('path' not in default) or (re.search(default['path'], path)):
                result.update(default)
        return result

    def run(self, terms, variables=None, **kwargs):

        results = []

        attributes = self._recursive_flatten(terms[0])
        defaults = self._flatten(terms[1])

        itemDefault = {}

        for attribute in attributes:

            items = []

            # Must be a dict
            if not isinstance(attribute, dict):
                raise AnsibleError('Expect a dict but was a %s' % type(attribute))

            # Check path key
            if 'path' not in attribute:
                raise AnsibleError('Expect a "path" key')

            state = attribute.get('state')

            # Ignore
            if state == 'ignore':
                continue

            # Composite link
            if state in ['link_directory', 'link_file']:
                if 'src' not in attribute:
                    raise AnsibleError('Expect "src" key')

                # Composite
                item = itemDefault.copy()
                item.update(self._default(defaults, attribute['src']))
                item.update(attribute)
                item.update({
                    'path': item.pop('src'),
                    'state': state.split('_')[1]
                })
                items.append(item)

                # Link
                attribute['state'] = 'link'

            item = itemDefault.copy()
            item.update(self._default(defaults, attribute['path']))
            item.update(attribute)
            items.append(item)

            # Merge by path key
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
