import os


commands_dir = os.path.join(os.path.dirname(__file__),'routes')
routes = []

for module in os.listdir(commands_dir):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    route_mod = __import__('arm.routes.%s' % module[:-3], locals(), globals(),['object'],-1)
    
    routes.append(route_mod.BaseRoute())

def retrieve_role(identifier, dest=None):
    
    for route in routes:
        if route.is_valid(identifier):
            route.fetch(identifier)
            break
    return


def fetch_git_repository(server, user, repo, tag=None):
    
    return '.cache/%s' % repo
