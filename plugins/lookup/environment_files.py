# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: environment_files
    author: Manala (@manala)
    short_description: returns a curated files list
    description:
      - Takes a files list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        files = self._flatten(terms[0])
        patterns = terms[1]

        itemDefault = {
            'export': False
        }

        for file in files:

            items = []

            # Short syntax
            if isinstance(file, string_types):
                if file not in patterns:
                    raise AnsibleError('"%s" is not a valid pattern' % (file))

                item = itemDefault.copy()
                item.update(patterns.get(file))
                items.append(item)
            else:
                # Must be a dict
                if not isinstance(file, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(file))

                # Check index key
                if 'file' not in file:
                    raise AnsibleError('Missing "file" key')

                item = itemDefault.copy()
                item.update(file)
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

        return results
