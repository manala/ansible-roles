from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text


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

    def run(self, terms, variables=None, **kwargs):

        results = []

        packages = self._recursive_flatten(terms[0])

        groups = []

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
                for i, group in enumerate(groups):
                    if group['package'] == item['package']:
                        groups[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    groups.append(item)

        # Groups
        for group in groups:
            # Deb packages could only be installed one by one
            if group['deb']:
                results.append(group)
            else:
                # If package share the previous one state, group them
                if results and not results[-1]['deb'] and group['state'] == results[-1]['state']:
                    results[-1]['package'].append(group['package'])
                else:
                    group.update({
                        'package': [group['package']]
                    })
                    results.append(group)

        return results
