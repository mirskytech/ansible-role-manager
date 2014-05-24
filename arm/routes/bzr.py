import re, os
from . import VCSRoute, ROUTE_REGEX
from pip.vcs.bazaar import Bazaar

class BazaarRoute(VCSRoute):
    
    '''
    uses pip specifiers

    '''
    
    vcs = Bazaar
    
    def __unicode__(self):
        return "bazaar"
    
    def _uid(self, identifier):
        pattern_re = re.compile('%(fqdn)s\/%(owner)s\/%(repo)s' % ROUTE_REGEX)
        pattern_match = pattern_re.search(identifier)
        pattern_info = pattern_match.groupdict()
        return "%s.%s" % (pattern_info['owner'],pattern_info['repo'])

            
        
        
                                          
    
    
    