'pip install http://someserver.org/packages/MyPackage-3.0.tar.gz'
import re
from . import Route




class URLRoute(Route):
    
    patterns = []
    
    def __init__(self):
        pass
    
    def __unicode__(self):
        return None
    
    def _uid(self):
        return None
    
    def is_valid(self, identifier):
        matches = [True for p in self.patterns if p.match(identifier)] 
        return len(matches) != 0
    
    
    def fetch(self, identifier):
        matches = [p.match(identifier).groupdict() for p in self.patterns if p.match(identifier)] 
        raise RouteException('fetch from tarball not yet implemented')