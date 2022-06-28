# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: php_extensions
    author: Manala (@manala)
    short_description: returns a curated extensions list
    description:
      - Takes an extensions list and returns it curated and optionally state filtered.
    options:
      wantstate:
        description: filter list items by enabled
      wantenabled:
        description: filter list items by state
      wantmap:
        description: format result list as a map
'''


from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        if wantstate and wantstate not in ['present', 'absent']:
            raise AnsibleError('Expected a wanstate of "present" or "absent" but was "%s"' % to_text(wantstate))

        wantenabled = kwargs.pop('wantenabled', None)
        wantmap = kwargs.pop('wantmap', False)

        extensions = self._flatten(terms[0])
        extensionsAvailable = terms[1]

        sapisAvailable = terms[2]

        itemDefault = {
            'state': 'present',
            'enabled': None
        }

        for extension in extensions:

            items = []

            # Short syntax
            if isinstance(extension, string_types):
                item = itemDefault.copy()
                item.update({
                    'extension': extension
                })
            else:

                # Must be a dict
                if not isinstance(extension, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(extension))

                # Check index key
                if 'extension' not in extension:
                    raise AnsibleError('Missing "extension" key')

                item = itemDefault.copy()
                item.update(extension)

            # Extension known as a sapi ?
            if item['extension'] in sapisAvailable:
                raise AnsibleError('Extension "%s" is known as a sapi' % item['extension'])

            # Already embedded extension ?
            if item['extension'] in extensionsAvailable:
                continue

            if item['state'] not in ['present', 'absent', 'ignore']:
                raise AnsibleError('Expected a state of "present", "absent" or "ignore" but was "%s"' % to_text(item['state']))

            if item['state'] == 'ignore':
                continue

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['extension'] == item['extension']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        # Filter by state
        if wantstate is not None:
            results = [result for result in results if result.get('state') == wantstate]

        # Filter by enabled
        if wantenabled is not None:
            results = [result for result in results if result.get('enabled') == wantenabled]

        # Map
        if wantmap:
            results = [result.get('extension') for result in results]

        return results
