import os
from abc import ABCMeta, abstractmethod


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
    
    Subclass is required to have the name ``BaseCommand``. TODO : replace with 
    '''    
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass
    

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
        return False

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
    
commands_dir = os.path.dirname(__file__)
routes = []

for module in os.listdir(commands_dir):
    # skip this file and any other non-python file
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    # import route module
    route_mod = __import__('arm.routes.%s' % module[:-3], locals(), globals(),['object'],-1)
    
    # instantiate and append to ``routes`` list
    routes.append(route_mod.BaseRoute())    