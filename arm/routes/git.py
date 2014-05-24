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
    
    vcs = Git
    
    def __unicode__(self):
        return "git"
    
    def _uid(self, identifier):
        pattern_re = re.compile('%(fqdn)s\/%(owner)s\/%(repo)s' % ROUTE_REGEX)
        pattern_match = pattern_re.search(identifier)
        pattern_info = pattern_match.groupdict()
        return "%s.%s" % (pattern_info['owner'],pattern_info['repo'])

            
        
        
                                          
    
    
    