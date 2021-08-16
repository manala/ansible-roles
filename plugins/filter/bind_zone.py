from __future__ import absolute_import, division, print_function
__metaclass__ = type


def zone_file(value):
    return 'db.' + value.replace('.in-addr.arpa', '')


class FilterModule(object):
    ''' Manala bind jinja2 filters '''

    def filters(self):
        filters = {
            'bind_zone_file': zone_file,
        }

        return filters
