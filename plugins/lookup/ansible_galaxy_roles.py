# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: ansible_galaxy_roles
    author: Manala (@manala)
    short_description: returns a curated roles list
    description:
      - Takes a roles list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        roles = self._flatten(terms)

        for role in roles:

            items = []

            # Short syntax
            if isinstance(role, string_types):
                items.append({
                    'src': role
                })
            else:

                # Must be a dict
                if not isinstance(role, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(role))

                # Check index key
                if 'src' not in role:
                    raise AnsibleError('Missing "src" key')

                items.append(role)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['src'] == item['src']:
                        results[i] = item
                        itemFound = True
                        break
                if not itemFound:
                    results.append(item)

        return results
