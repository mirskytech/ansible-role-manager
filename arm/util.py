import os, shutil
from git import Repo
from .odict import odict

def retrieve_role(identifier, dest=None):
    from routes import routes, RouteException
    for route in routes:
        if route.is_valid(identifier):
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
        
        roles = retrieve_all_roles(identifier, roles=roles )
        
    return roles
        


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


def get_playbook_root(path):

    if os.path.realpath(path) == '/':
        return False
    if os.path.exists(os.path.join(path, '.arm')):
        return os.path.realpath(path)
    elif os.path.exists(os.path.join(path, 'roles')):
        return os.path.realpath(path)
    return get_playbook_root(os.path.join(os.path.abspath(path), os.pardir))
