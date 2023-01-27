# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: files_attributes
    author: Manala (@manala)
    short_description: returns a curated attributes list
    description:
      - Takes a attributes list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

import re


class LookupModule(LookupBase):

    def _default(self, defaults, path):
        result = {}
        for default in defaults:
            if ('path' not in default) or (re.search(default['path'], path)):
                result.update(default)
        return result

    def run(self, terms, variables=None, **kwargs):

        results = []

        attributes = self._flatten(terms[0])
        defaults = self._flatten(terms[1])

        itemDefault = {}

        for attribute in attributes:

            items = []

            # Must be a dict
            if not isinstance(attribute, dict):
                raise AnsibleError('Expected a dict but was a %s' % type(attribute))

            # Check path key
            if 'path' not in attribute:
                raise AnsibleError('Missing "path" key')

            state = attribute.get('state')

            # Ignore
            if state == 'ignore':
                continue

            # Composite link
            if state in ['link_directory', 'link_file']:
                if 'src' not in attribute:
                    raise AnsibleError('Missing "src" key')

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
