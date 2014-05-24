import os, shutil
import inspect
from git import Repo
from .odict import odict
import hgapi
from pip.vcs.subversion import Subversion


def retrieve_role(identifier, dest=None):
    from routes import routes, RouteException
    for route in routes:
        if route.is_valid(identifier):
            print u"fetching `%s` from %s" % (identifier, route)
            
            return route.fetch(identifier)
        pass
    raise RouteException('Could not determine access point for `%s`' % identifier)
    
def retrieve_all_roles(identifier, alias=None, roles=odict()):
    
    if alias and alias in roles.keys():
        raise Exception("two roles have the same alias of '%s'" % alias)
    
    role = retrieve_role(identifier)
    
    if not alias:
        alias = role.get_name()
    
    if alias not in roles.keys():
        roles.update( { alias:role } )  
    
    for role in role.get_dependencies():

        if role in roles.keys():
            continue
        
        roles = retrieve_all_roles(role, roles=roles )
        
    return roles

def get_playbook_root(path=None):
    
    if not path:
        path = os.getcwd()

    if os.path.realpath(path) == '/':
        return False
    if os.path.exists(os.path.join(path, '.arm')):
        return os.path.realpath(path)
    elif os.path.exists(os.path.join(path, 'roles')):
        return os.path.realpath(path)
    return get_playbook_root(os.path.join(os.path.abspath(path), os.pardir))

def find_subclasses(module, clazz):

    for name in dir(module):
        o = getattr(module, name)
        try:
            if (o != clazz) and issubclass(o, clazz) and not inspect.isabstract(o):
                yield name, o
        except TypeError: pass