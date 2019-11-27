class FilterModule(object):
    def filters(self):
        return {
            'manala_bind_zone_file': self.manala_bind_zone_file
        }
 
    def manala_bind_zone_file(self, value):
        return 'db.' + value.replace('.in-addr.arpa', '')
