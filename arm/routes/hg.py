import re, os
import hgapi
from . import Route, ROUTE_REGEX
from arm import Role
from arm.util import get_playbook_root
from arm.util import fetch_hg_repository
from yaml import load, Loader

class MercurialRoute(Route):
        
    '''
    
    #### pip-style patterns
    hg+http://hg.myproject.org/MyProject
    hg+ssh://hg@myproject.org/MyProject
    
    #### all support
    @branch
    @commit (hexidecimal)
    @tag
    
    #### and
    
    #alias=myalias

    '''

    patterns = [

        re.compile(r'^hg\+(?P<protocol>http[s]{0,1}):\/\/%(fqdn)s\/%(owner)s\/%(repo)s%(tag)s' % ROUTE_REGEX),
        re.compile(r'^hg\+(?P<protocol>ssh)\:\/\/(%(user)s\@){0,1}%(fqdn)s\/%(owner)s\/%(repo)s%(tag)s' % ROUTE_REGEX),

        ]
    
    def __init__(self):
        pass
    
    def __unicode__(self):
        return "Mercurial"
    
    def is_valid(self, identifier):
        matches = [True for p in self.patterns if p.match(identifier)] 
        return len(matches) != 0

    def _uid(self, info):
        return "%s.%s" % (info['owner'],info['repo'])
    
    def fetch(self, identifier):
        print "\nFetching `%s` from mercurial..." % identifier
        matches = [p.match(identifier).groupdict() for p in self.patterns if p.match(identifier)]
        
        info = matches[0]
        
        params = {
            'server':info['fqdn'],
            'owner':info['owner'],
            'repo':info['repo'],
        }
        
        if info.get('tag', None):
            params['tag'] = info['tag']
            
        if info.get('user', None):
            params['user'] = info['user']
            
        if info.get('protocol', None):
            params['protocol'] = info['protocol']
    
        location = fetch_hg_repository(**params)
        
        meta_path = os.path.join(location, 'meta/main.yml')
        if os.path.exists(meta_path):
            meta_info = load(open(meta_path, 'r'), Loader=Loader)
            meta_info.update({ 'github_user':info['owner'],'github_repo':info['repo']})
            
            return Role(location, **meta_info)
        
        print "WARNING : The role '%s' does not have a meta/main.yml. Role attributes & dependencies not available."
        return Role(location,{
            'github_user':info['owner'],
            'github_repo':info['repo']
        })
            
            
        
        
                                          
    
    
    