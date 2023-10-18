# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: apt_repositories
    author: Manala (@manala)
    short_description: returns a curated repositories list
    description:
      - Takes a repositories list and returns it curated and optionally state filtered.
    options:
      wantstate:
        description: filter list items by state
'''

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text

import os.path
import re

legacy_source_regex = r"(?P<type>deb(?:-src)?) (?:\[(?P<options>.*)\] )?(?P<uri>(?P<uri_scheme>file|cdrom|copy|http|https|ftp|ssh)://(?P<uri_domain>(?:(?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,6}))/[a-zA-Z0-1-_\./]+ (?P<suites>[a-z/-]+)(?:(?<!/) (?P<components>[a-z]+(?: [a-z]+)*))"

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        if wantstate and wantstate not in ['present', 'absent']:
            raise AnsibleError('Expected a wanstate of "present" or "absent" but was "%s"' % to_text(wantstate))

        repositories = self._flatten(terms[0])
        repositoriesPatterns = terms[1]
        keysPatterns = terms[2]
        preferences = terms[3]
        exclusives = self._flatten(terms[4])
        dir = terms[5]

        itemDefault = {
            'state': 'present'
        }

        # Mark exclusive repositories as absent
        for repository in exclusives:
            item = itemDefault.copy()
            item.update({
                'file': repository['path'],
                'state': 'absent'
            })
            results.append(item)

        # Handle repositories defined as reversed preferences
        for preference in preferences[::-1]:
            if 'repository' in preference:
                repositories.insert(0, preference['repository'])

        for repository in repositories:

            items = []

            item = itemDefault.copy()

            # Short syntax
            if isinstance(repository, string_types):
                item.update({
                    'repository': repository
                })
            else:
                # Must be a dict
                if not isinstance(repository, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(repository))

                item.update(repository)

                if item['state'] not in ['present', 'absent', 'ignore']:
                    raise AnsibleError('Expected a state of "present", "absent" or "ignore" but was "%s"' % to_text(item['state']))

                if item['state'] == 'ignore':
                    continue

            if 'repository' in item:
                repositoryPattern = item['repository']
                if repositoryPattern not in repositoriesPatterns:
                    raise AnsibleError('unable to find "%s" repository pattern' % repositoryPattern)
                item = {
                    # Guess file from repository pattern name
                    **{'file': item['repository'] + '.sources'},
                    **repositoriesPatterns[repositoryPattern],
                    **item,
                }

            # Legacy
            if 'source' in item:
                self._display.warning('Using a "source" repository key is deprecated, please provide "uris", "suites", and possibly "types" and "components" keys for repository "%s"' % item['source'])
                if 'file' not in item:
                    raise AnsibleError('Missing "file" key in legacy repository source "%s"' % item['source'])
                if not item['file'].endswith('.sources'):
                    raise AnsibleError('Invalid "file" key in legacy repository source "%s", must end with ".sources"' % item['source'])
                matches = re.search(legacy_source_regex, item['source'])
                if matches:
                    item.update({
                        'uris': matches.group('uri'),
                        'suites': matches.group('suites'),
                        'components': matches.group('components'),
                    })

            # Check index key
            if 'file' not in item:
                raise AnsibleError('Missing "file" key')

            # Check required keys
            if 'uris' not in item:
                raise AnsibleError('Missing "uris" key in repository file "%s"' % item['file'])
            if 'suites' not in item:
                raise AnsibleError('Missing "suites" key in repository file "%s"' % item['file'])

            if 'components' not in item and not item['suites'].endswith('/'):
                raise AnsibleError('If "components" key not present, "suites" key must end with a "/"')

            # Handle key
            if 'key' in item and isinstance(item['key'], string_types):
                keyPattern = item['key']
                if keyPattern not in keysPatterns:
                    raise AnsibleError('unable to find "%s" key pattern' % keyPattern)
                item.update({
                    'key': keysPatterns[keyPattern],
                })

            item.update({
                'file': os.path.join(
                    dir,
                    item['file']
                )
            })

            if 'legacy_file' in item:
                item.update({
                    'legacy_file': os.path.join(
                        dir,
                        item['legacy_file']
                    )
                })

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

        # Filter by state
        if wantstate:
            results = [result for result in results if result.get('state') == wantstate]

        return results
