import os


ROUTE_REGEX =  {
    'user':'(?P<user>[a-z][a-z\d\-]+?)',
    'fqdn':'(?P<fqdn>([a-z][a-z\.\d\-]+)\.(?:[a-z][a-z\-]+)(?![\w\.]))',
    'owner':'(?P<owner>[a-z][a-z\.\-]+)',
    'repo':'(?P<repo>[a-z][a-z\-]+)',
    'tag': '(\@(?P<tag>[a-z]+)){0,1}'
}   

class RouteException(Exception):
    pass





class Route(object):
    
    def __init__(self):
        pass
    
    def is_valid(self, identifier):
        return False
    
    
    def fetch(self, identifier):
        return False
    
    
    
commands_dir = os.path.dirname(__file__)
routes = []

for module in os.listdir(commands_dir):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    route_mod = __import__('arm.routes.%s' % module[:-3], locals(), globals(),['object'],-1)
    
    routes.append(route_mod.BaseRoute())    