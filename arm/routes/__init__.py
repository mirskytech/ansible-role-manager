import os, shutil, re
from abc import ABCMeta, abstractmethod, abstractproperty
from arm.util import find_subclasses, get_playbook_root
from arm import Role, Module
from pip.exceptions import InstallationError

# TODO : these should be case-insensitive (or search/match should ignore case)

ROUTE_REGEX =  {
    'user':'(?P<user>[a-z][a-z\d\-]+?)',
    'fqdn':'(?P<fqdn>([a-z][a-z\.\d\-]+)\.(?:[a-z][a-z\-]+)(?![\w\.]))',
    'owner':'(?P<owner>[a-z][a-z\.\-]+)',
    'repo':'(?P<repo>[a-z][\w\-_]+)',
    'tag': '(\@(?P<tag>[a-z]+)){0,1}',
    'path':'(\/(?P<path>[\w.-_]+))*'
}   

# ----------------------------------------------------------------------

class RouteException(Exception):
    '''
    Thrown by any arm.Route which encounters an issue during identifier validation or fetching.
    '''
    pass


# ----------------------------------------------------------------------

class Route(object):
    '''
    Abstract class which is used to implement the fetching of a role to local playbook.
    
    '''    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass
    
    @abstractmethod
    def _uid(self):
        return None
        
    @abstractmethod
    def __unicode__(self):
        return None

    @abstractmethod
    def is_valid(self, identifier):
        '''
        Required. Use provided identifier to determine if this route can fetch the necessary role.
    
        Arugments:
            * **identifier** :  See :doc:specifiers
    
        Returns: bool
        
        '''
        return False
    
    @abstractmethod
    def fetch(self, identifier):
        '''
        Required. Use provided identifer to fetch the role from this route.
        
        Arguments:
            * **identifiers** : See :doc:specifiers
            
        Returns: arm.Role with location of fetched role and meta information from ``meta/main.yml``
        
        '''   
        return None

# ----------------------------------------------------------------------

class VCSRoute(Route):

    __metaclass__ = ABCMeta

    @abstractproperty
    def vcs(self):
        return None

    def is_valid(self, identifier):
        pattern_match = re.compile('^(%s)' % "|".join(self.vcs.schemes))
        return bool(pattern_match.match(identifier))

    def fetch(self, identifier):

        _repo = self.vcs(identifier)
        _uid = self._uid(identifier)
        _destination = os.path.join(get_playbook_root(), '.cache', self._uid(identifier))
        if os.path.exists(_destination):
            shutil.rmtree(_destination)
        try:
            _repo.obtain(_destination)
        except InstallationError as e:
            raise RouteException("could not retrieve '%s' " % identifier)

        playbook_tests = ('roles', '.arm', 'group_vars', 'host_vars',)
        role_tests = ('tasks', 'meta', 'files', 'handlers')
        
        def _test_fetched(tests):
            return len([True for test in tests if os.path.exists(os.path.join(_destination, test))]) > 0
        
        is_playbook = _test_fetched(playbook_tests)
        is_role = _test_fetched(role_tests)
        
        if is_role:
            return Role(_destination, uid=_uid)
        elif is_playbook:
            return Playbook(_destination, uid=_uid)
        else:
            return Module(_destination, uid=_uid)
        
        
        #if is_role and type(pod) != Role:
            #print "Warning: potential install of module or playbook as role"
        #if is_playbook and type(pod) != Playbook:
            #print "Warning: potential install of module or role as playbook"
        #if not is_playbook and not is_role and type(pod) != Module:
            #print "Warning: potential install of role or playbook as module"

        return pod(_destination, uid=_uid)

# ----------------------------------------------------------------------

'''
   Find all the routes within this directory and import each.
   
   Assumes all commands are subclasses of ``arm.routes.Route`` and are called ``BaseCommand``
   
   TODO: allow arbitrary name as long as it inherits from ``arm.routes.Route``
   def find_subclasses(module, clazz):
       for name in dir(module):
           o = getattr(module, name)
           try:
               if (o != clazz) and issubclass(o, clazz):
                   yield name, o
           except TypeError: pass
'''
    
routes_dir = os.path.dirname(__file__)
routes = []

for module in os.listdir(routes_dir):
    # skip this file and any other non-python file
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    # import route module
    route_mod = __import__('arm.routes.%s' % module[:-3], locals(), globals(),['object'],-1)
    
    # search for all subclasses of ``arm.routes.Route``
    for route_name,route_class in find_subclasses(route_mod, Route):
        # instantiate and append to ``routes`` list
        routes.append(route_class())
        
