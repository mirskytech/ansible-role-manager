import re, os, shutil
from . import Route, RouteException
import requests
from yaml import load, Loader
#from arm.util import fetch_git_repository

GALAXY_SERVER_DEFAULT = 'galaxy.ansible.com'


class BaseRoute(Route):
    
    owner__name = r'(?P<owner>[a-z]+?)\.(?P<name>[a-z]+?)$'
    version = r'(?P<version>[0-9]\.[0-9]\.[0-9])'
    
    patterns = ( 
        re.compile(r'%s$' % owner__name),
        re.compile(r'%s,%s$' % (owner__name, version))
        )
    
    def __init__(self, api_server=GALAXY_SERVER_DEFAULT):
        self.api_server = api_server
    
    def is_valid(self, identifier):
        matches = [True for p in self.patterns if p.match(identifier)] 
        return len(matches) != 0
    
    def fetch(self, identifier):
        
        matches = [p.match(identifier) for p in self.patterns if p.match(identifier)]
        assert len(matches) != 0
    
        d = matches[0].groupdict()
        
        _url = 'https://%s/api/v1/roles/?owner__username=%s&name=%s' % (self.api_server,d['owner'],d['name'])
        r = requests.get(_url,verify=False)
        if r.status_code != 200:
            raise RouteException('galaxy :: could not find %s.%s' % (d['owner'],d['name']) )
        
        data = r.json()
        
        if data['count'] > 1:
            raise RouteException('galaxy :: too many results for %s.%s' %  (d['owner'],d['name']) )
        elif data['count'] < 1:
            raise RouteException('galaxy :: could not find %s.%s' %  (d['owner'],d['name']) )
        
        role = data['results'][0]
        
        if d.get('version', None) and role['versions'] and d['version'] not in role['versions']:
            raise RouteException('galaxy :: version is not available %s' % d['version'])
        
        location = fetch_git_repository('github.com', role['github_repo'], role['github_repo'])

        meta_path = os.path.join(location, 'meta/main.yml')
        if os.path.exists(meta_path):
            meta_info = load(open(meta_path, 'r'), Loader=Loader)
            print meta_info
            
        
        #shutil.copytree(location, os.path.join('roles'))
        
        
        
    
    
    