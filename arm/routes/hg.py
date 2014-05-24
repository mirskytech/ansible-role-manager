import re, os
from . import VCSRoute, ROUTE_REGEX
from pip.vcs.mercurial import Mercurial

class MercurialRoute(VCSRoute):
        
    '''
    
    #### pip-style patterns
    hg+http://hg.myproject.org/MyProject
    hg+ssh://hg@myproject.org/MyProject
    
    #### all support
    @branch
    @commit (hexidecimal)
    @tag

    '''

    vcs = Mercurial
    
    def __unicode__(self):
        return "mercurial"
    
    def _uid(self, identifier):
        pattern_re = re.compile('%(fqdn)s\/%(owner)s\/%(repo)s' % ROUTE_REGEX)
        pattern_match = pattern_re.search(identifier)
        pattern_info = pattern_match.groupdict()
        return "%s.%s" % (pattern_info['owner'],pattern_info['repo'])   
            
            
        
        
                                          
    
    
    