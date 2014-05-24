import re, os, shutil
from arm import Role
from . import Route, RouteException
import requests
from yaml import load, Loader
from arm.util import fetch_git_repository

GALAXY_SERVER_DEFAULT = 'galaxy.ansible.com'


class GalaxyRoute(Route):
    
    owner__name = r'(?P<owner>[a-zA-Z][\w_.-]+)\.(?P<name>[a-zA-Z][\w_.-]+)'
    version = r'v(?P<version>[0-9]\.[0-9]\.[0-9])'
    
    patterns = ( 
        re.compile(r'%s' % owner__name),
        re.compile(r'^%s,%s$' % (owner__name, version))
        )
    
    def __init__(self, api_server=GALAXY_SERVER_DEFAULT):
        super(GalaxyRoute,self).__init__()
        self.api_server = api_server
        
    def _uid(self, info):
        return "%s.%s" % (info['owner'],info['repo'])             
        
    def __unicode__(self):
        return "Galaxy"
        
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
            raise RouteException('galaxy could not find role `%s.%s`' % (d['owner'],d['name']) )
        
        data = r.json()
        
        if data['count'] > 1:
            raise RouteException('galaxy had too many results for %s.%s' %  (d['owner'],d['name']) )
        elif data['count'] < 1:
            raise RouteException('galaxy could not find role `%s.%s`' %  (d['owner'],d['name']) )
        
        role_info = data['results'][0]
        
        def _check_version(required, actual):
            
            if required and actual and required not in actual:
                raise RouteException('galaxy :: version is not available %s' % d['version'])
            
        _check_version(d.get('version', None),role_info.get('versions', None))
        
        location = fetch_git_repository('github.com', role_info['github_user'], role_info['github_repo'])    
        
        meta_path = os.path.join(location, 'meta/main.yml')
        if os.path.exists(meta_path):
            meta_info = load(open(meta_path, 'r'), Loader=Loader)
            _check_version(d.get('version', None), role_info.get('versions',None))
        

        return Role(location, **role_info)

    
        
        
        
        
        
    
    
    