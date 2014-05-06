



class Role(dict):
    
    def __init__(self, local_store, *args, **kwargs):
        self.local_store = local_store
        self.alias = alias
        super(Role, self).__init__(*args, **kwargs)
        
    
    def get_name(self):
        return "%s.%s" % (role_info['github_user'], role_info['github_repo'])
    
    def get_alias(self):
        if not self.alias:
            return self.get_name()
        return alias