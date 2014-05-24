import re, os
from . import VCSRoute, ROUTE_REGEX
from pip.vcs.git import Git




class GitRoute(VCSRoute):
    
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
    
    vcs = Git
    
    def __unicode__(self):
        return "git"
    
    def _uid(self, identifier):
        pattern_re = re.compile('%(fqdn)s\/%(owner)s\/%(repo)s' % ROUTE_REGEX)
        pattern_match = pattern_re.search(identifier)
        pattern_info = pattern_match.groupdict()
        

        return "%s.%s" % (pattern_info['owner'],pattern_info['repo'])

            
        
        
                                          
    
    
    