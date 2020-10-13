from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        if wantstate and wantstate not in ['present', 'absent']:
            raise AnsibleError('Expect a wanstate of "present" or "absent" but was "%s"' % to_text(wantstate))

        wantdeb = kwargs.pop('wantdeb', None)
        wantmap = kwargs.pop('wantmap', False)

        packages = self._flatten(terms[0])

        itemDefault = {
            'state': 'present',
            'deb': False
        }

        for package in packages:

            items = []

            item = itemDefault.copy()

            # Short syntax
            if isinstance(package, string_types):
                item.update({
                    'package': package
                })
            else:

                # Must be a dict
                if not isinstance(package, dict):
                    raise AnsibleError('Expect a dict but was a %s' % type(package))

                # Check index key
                if 'package' not in package:
                    raise AnsibleError('Expect "package" key')

                item.update(package)

                if item['state'] not in ['present', 'absent', 'ignore']:
                    raise AnsibleError('Expect a state of "present", "absent" or "ignore" but was "%s"' % to_text(item['state']))

                if item['state'] == 'ignore':
                    continue

            # Is a .deb ?
            if item.get('package').endswith('.deb'):
                item.update({
                    'deb': True
                })

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['package'] == item['package']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        # Filter by state
        if wantstate:
            results = [result for result in results if result.get('state') == wantstate]

        # Filter by deb
        if wantdeb is not None:
            results = [result for result in results if result.get('deb') == wantdeb]

        # Map
        if wantmap:
            results = [result.get('package') for result in results]

        return results
