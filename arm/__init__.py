class RoleException(Exception):
    pass


class Role(object):
    
    def __init__(self, local_store, *args, **kwargs):
        self.local_store = local_store
        for k,v in kwargs.iteritems():
            setattr(self, k, v)
            
    def get_name(self):
        if hasattr(self, 'github_user') and hasattr(self, 'github_repo'):
            return "%s.%s" % (getattr(self, 'github_user'), getattr(self, 'github_repo'))
        raise RoleException('Role does not have unique name')
        
    def get_path(self):
        return self.local_store
    
    def get_dependencies(self):

        needs = []
        
        if not hasattr(self, 'dependencies'):
            print "Warning : role's dependencies are not specified `%s`" % self.get_name()

        for dependency in getattr(self, 'dependencies',[]):
            if type(dependency) != str:
                print "Warning : '%s' has improperly defined dependencies." % self.get_name()
                continue
            needs.append(dependency)
            print "NEEDS : %s" % needs
        return needs

LIBRARY_ROLE_PATH = 'library_roles/'