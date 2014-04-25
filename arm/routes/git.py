import re
from . import Route




class BaseRoute(Route):
    
    pattern = re.compile(r'^[a-z]+?\.[a-z]+?$')
    
    def __init__(self):
        pass
    
    def is_valid(self, identifier):
        return False
    
    
    def fetch(self, identifier):
        print "fetch from git"
    
    
    
    
    
    