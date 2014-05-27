import os, shutil, re
import inspect
from git import Repo
from .odict import odict
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
        
        opts = {}
        # dependency might have a '#alias='
        identifier, alias = split_alias_identifier(role)
        if alias:
            opts = {'alias':alias}
        
        roles = retrieve_all_roles(role, roles=roles, **opts)
        
    return roles


def split_alias_identifier(identifier):
    aliasRE = re.compile(r'^(?P<identifier>.+?)\#alias\=(?P<alias>[a-zA-Z][a-zA-Z0-9]+?)$')
    
    alias_match = aliasRE.match(identifier)
    
    if not alias_match:    
        return alias_match.groupdict()['identifier'], None
    alias_info = alias_match.groupdict()
    return alias_info['identifier'], alias_info['alias']

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


"""
        Description:
            fetch a git repository into playbook cache                
"""

def fetch_git_repository(server, owner, repo, user=None, tag=None, protocol='https'):
    
    _destination = '%s/.cache/%s' % (get_playbook_root(os.getcwd()), repo)
    if os.path.exists(_destination):
        shutil.rmtree(_destination)
    _url = "%s://%s/%s/%s.git" % (protocol, server, owner, repo)
    if user:
        _url = "%s://%s@%s/%s/%s.git" % (protocol, user, server, owner, repo)        
        
    repo = Repo.clone_from(_url, _destination)
    
    if tag:
        repo.git.checkout(tag)

    return _destination