import logging

# ----------------------------------------------------------------------

'''
   Configuration for python logging
'''

class SingleLevelFilter(logging.Filter):
    def __init__(self, passlevel, reject):
        self.passlevel = passlevel
        self.reject = reject

    def filter(self, record):
        if self.reject:
            return (record.levelno != self.passlevel)
        else:
            return (record.levelno == self.passlevel)




logger = logging.getLogger('arm')
logger.setLevel(logging.INFO)


warn_handler = logging.StreamHandler()
warn_handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(levelname)s (ARM) :: %(message)s')
warn_handler.setFormatter(formatter)

info_handler = logging.StreamHandler()
info_handler.setLevel(logging.INFO)
info_filter = SingleLevelFilter(logging.INFO, False)
info_handler.addFilter(info_filter)
formatter = logging.Formatter('%(message)s')
info_handler.setFormatter(formatter)


logger.addHandler(warn_handler)
logger.addHandler(info_handler)

# ----------------------------------------------------------------------

class RoleException(Exception):
    '''
    Thrown by arm.Role when it encounters an error.
    '''
    pass


# ----------------------------------------------------------------------
class Role(object):
    '''
    Container object for an Ansible Role which holds meta information about the role
    '''    
    
    def __init__(self, local_store, *args, **kwargs):
        '''
        Constructor
        
        Arugments:
            * **local_store** :  Location of where this role is stored locally after being fetched
            * **kwargs** : A dictionary of any meta information about this role (following Ansible Galaxy's meta format)        
        '''            
        self.local_store = local_store
        for k,v in kwargs.iteritems():
            setattr(self, k, v)
            
    def get_name(self):
        '''
        Returns the named identifier of this role: <owner>.<repo name>
        '''
        if hasattr(self, 'github_user') and hasattr(self, 'github_repo'):
            return "%s.%s" % (getattr(self, 'github_user'), getattr(self, 'github_repo'))
        raise RoleException('Role does not have unique name')
        
    def get_path(self):
        '''
        Returns the location of where this role is stored locally
        '''
        return self.local_store
    
    def get_dependencies(self):
        '''
        Based on the meta information provided in ``meta/main.yml'', returns the list of other
        roles that this Role depends on. Warns (but doesn't fail) if a role doesn't define this information.
        '''
        needs = []
        
        # check if this Role has a ``dependencies`` property, warn if it doesn't
        if not hasattr(self, 'dependencies'):
            print "Warning : role's dependencies are not specified `%s`" % self.get_name()

        # check to make sure that each dependency is formatted corrected - ie. a string
        for dependency in getattr(self, 'dependencies',[]):
            if type(dependency) != str:
                print "Warning : '%s' has improperly defined dependencies." % self.get_name()
                continue
            needs.append(dependency)
        return needs

# ----------------------------------------------------------------------

# Playbook subdirectory which stores the role dependencies
# TODO : should be an option, which can be set in the ``.arm`` configuration file or on the cmd line
LIBRARY_ROLE_PATH = 'library_roles/'