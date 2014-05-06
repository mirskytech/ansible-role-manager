import os, shutil
from git import Repo

def retrieve_role(identifier, dest=None):
    from routes import routes    
    for route in routes:
        if route.is_valid(identifier):
            return route.fetch(identifier)
        pass
    
def retrieve_all_roles(identifier, needs={}):
    
    role = retrieve_role(identifier)
    
    needs.update( { role.get_name(): role } )
    
    for need in role['dependencies']:
        if need in needs:
            continue
        needs = retrieve_all_roles(identifier, needs)
        
    return needs
        


"""
        Description:
            fetch a git repository into playbook cache                
"""

def fetch_git_repository(server, user, repo, tag=None):
    
    _destination = '%s/.cache/%s' % (get_playbook_root(os.getcwd()), repo)
    if os.path.exists(_destination):
        shutil.rmtree(_destination)
    _url = "https://%s/%s/%s.git" % (server, user, repo)
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
