from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError

ARCHITECTURE_MAP = {
    'x86_64': 'amd64',
    'aarch64': 'arm64',
}


def architecture(architecture):
    if architecture not in ARCHITECTURE_MAP:
        raise AnsibleFilterError('unsupported "%s" architecture' % architecture)
    return ARCHITECTURE_MAP[architecture]


class FilterModule(object):
    ''' Manala gomplate jinja2 filters '''

    def filters(self):
        filters = {
            'gomplate_architecture': architecture,
        }

        return filters
