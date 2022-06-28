# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: ssh_known_hosts
    author: Manala (@manala)
    short_description: returns a curated known hosts list
    description:
      - Takes a known hosts list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        hosts = self._flatten(terms[0])
        patterns = terms[1]

        itemDefault = {}

        for host in hosts:

            items = []

            # Short syntax
            if isinstance(host, string_types):
                item = itemDefault.copy()
                item.update(patterns.get(host))
            else:

                # Must be a dict
                if not isinstance(host, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(host))

                # Check index key
                if 'host' not in host:
                    raise AnsibleError('Missing "host" key')

                item = itemDefault.copy()
                item.update(host)

            # File
            if 'file' in item:
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
