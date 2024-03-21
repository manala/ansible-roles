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
      wanttype:
        description: filter list items by type
'''

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text

import os.path
import re
import logging

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        # Logging
        logging.basicConfig(level=logging.INFO)
        log = logging.getLogger("apt_repo")

        results = []

        wanttype = kwargs.pop('wanttype', None)

        if wanttype and wanttype not in ['name', 'file']:
            raise AnsibleError('Expected a wanttype of "name" or "file" but was "%s"' % to_text(wanttype))

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
                    **{'name': item['repository']},
                    **repositoriesPatterns[repositoryPattern],
                    **item,
                }

            # Legacy
            if 'source' in item:
                raise AnsibleError('Using a "source" repository key is deprecated, please use deb822 notation. See manala.roles.apt README.md')

            # Check index key
            if 'name' not in item:
                raise AnsibleError('Missing "name" key')

            # Check required keys
            if 'uris' not in item:
                raise AnsibleError('Missing "uris" key')
            if 'suites' not in item:
                raise AnsibleError('Missing "suites" key')

            if 'components' not in item and not item['suites'].endswith('/'):
                raise AnsibleError('If "components" key not present, "suites" key must end with a "/"')

            # Handle key
            if 'key' in item and isinstance(item['key'], string_types):
                keyPattern = item['key']
                if keyPattern not in keysPatterns:
                    raise AnsibleError('unable to find "%s" key pattern' % keyPattern)
                item = {
                    **keysPatterns[keyPattern],
                    **item,
                }

            if 'legacy_file' in item:
                itemLegacy = itemDefault.copy()
                itemLegacy.update({
                    'file': os.path.join(
                        dir,
                        item['legacy_file']
                    ),
                    'state': 'absent',
                })
                results.append(itemLegacy)

            items.append(item)

            # Merge by index key
            for result in results:
                # Comes from exclusive
                if 'file' in result:
                    self._display.v('> ' + str(result))
                    file_name = os.path.basename(result['file'])
                    file_basename = os.path.splitext(file_name)[0]
                    file_extension = os.path.splitext(file_name)[1]
                    result['file_extension'] = file_extension
                    result['file_basename'] = file_basename
                    result['file_name'] = file_name
                    if file_extension == '.sources' and not '_' in file_name:
                        itemFound = False
                        for item in items:
                            self._display.v('   > ' + str(item))
                            #if file_basename == re.sub("_", "-", item['name']):
                            #    result['name'] = item['name']
                            #    itemFound = True
                            #    #break
                        if not itemFound:
                            result['name'] = file_basename
                        del result['file']

            # Merge by index key
            for item in items:
                itemFound = False
                # Comes from variables
                for i, result in enumerate(results):
                    if 'name' in result and 'name' in item:
                        if result['name'] == item['name']:
                            results[i] = item
                            itemFound = True
                            break

                if not itemFound:
                    results.append(item)

        # Filter by type
        if wanttype:
            results = [result for result in results if wanttype in result]

        return results
