import re, os
from . import Route, ROUTE_REGEX
from arm import Role
from arm.util import fetch_git_repository
from yaml import load, Loader



class GitRoute(Route):
    
    '''
    #### pattern one
    git://git.myproject.org/MyProject
    
    #### pattern two & three (pip style)
    git+http://git.myproject.org/MyProject
    git+ssh://git@myproject.org/MyProject
    
    #### pattern four & five (git style)
    
    http://git.myproject.org/MyProject.git    
    ssh://git@myproject.org:MyProject.git
    
    #### all support
    @branch
    @commit (hexidecimal)
    @tag

    '''


    patterns = [

        # pattern one
        re.compile('git\:\/\/(%(user)s\@){0,1}%(fqdn)s\/%(owner)s\/%(repo)s%(tag)s' % ROUTE_REGEX),
        
        # patterns two & three
        re.compile(r'^git\+(?P<protocol>http[s]{0,1}):\/\/%(fqdn)s\/%(owner)s\/%(repo)s%(tag)s' % ROUTE_REGEX),
        re.compile(r'^git\+(?P<protocol>ssh)\:\/\/(%(user)s\@){0,1}%(fqdn)s\/%(owner)s\/%(repo)s%(tag)s' % ROUTE_REGEX),
        
        # patterns four & five
        re.compile(r'^(?P<protocol>http[s]{0,1}):\/\/%(fqdn)s\/%(owner)s\/%(repo)s\.git%(tag)s' % ROUTE_REGEX),        
        re.compile(r'^(?P<protocol>ssh):\/\/(%(user)s\@){0,1}%(fqdn)s\:%(owner)s\/%(repo)s\.git%(tag)s' % ROUTE_REGEX),

        ]
    
    def __init__(self):
        pass
    
    def __unicode__(self):
        return "git"
    
    def is_valid(self, identifier):
        matches = [True for p in self.patterns if p.match(identifier)] 
        return len(matches) != 0
    
    
    def fetch(self, identifier):
        print "\nFetching `%s` from git..." % identifier
        matches = [p.match(identifier).groupdict() for p in self.patterns if p.match(identifier)]
        
        # TODO : is it ok if there are multiple messages
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
        
        location = fetch_git_repository(**params)
        meta_path = os.path.join(location, 'meta/main.yml')
        if os.path.exists(meta_path):
            meta_info = load(open(meta_path, 'r'), Loader=Loader)
            meta_info.update({ 'github_user':info['owner'],'github_repo':info['repo']})

            # TODO : could support version in this format:
            # http://git.myproject.org/MyProject.git==0.2 
            # would fail if the retrieved role doesn't line up. but could be useful if >= or <=
            #_check_version(d.get('version', None), role_info.get('versions',None))
            
            return Role(location, **meta_info)
        
        print "WARNING : The role '%s' does not have a meta/main.yml. Role attributes & dependencies not available."
        return Role(location,{
            'github_user':info['owner'],
            'github_repo':info['repo']
        })
            
            
        
        
                                          
    
    
    