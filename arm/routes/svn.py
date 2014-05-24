import re, os, shutil
from . import Route, ROUTE_REGEX
from arm.util import find_subclasses, fetch_svn_repository, get_playbook_root
from pip.vcs.subversion import Subversion
from arm import Role

# ----------------------------------------------------------------------

class SubversionRoute(Route):
    '''
    r'^svn\+(?P<protocol>svn)\:\/\/(%(user)s\@){0,1}%(fqdn)s\/%(owner)s\/%(repo)s%(tag)s
    '''    
    vcs = Subversion
    patterns = [   re.compile('^(%s)' % "|".join(vcs.schemes))   ]
    
       # re.compile(r'^svn\+(?P<protocol>http[s]{0,1}):\/\/%(fqdn)s\/%(owner)s\/%(repo)s+%(tag)s' % ROUTE_REGEX),
       # re.compile(r'^svn\+(?P<protocol>svn)\:\/\/(%(user)s\@){0,1}%(fqdn)s%(path)s/?' % ROUTE_REGEX),
    
    def __init__(self):
        pass
        
    def _uid(self, identifier):        
        
        path_re = re.compile('%(fqdn)s\/(?P<path>.+?)/?$'%ROUTE_REGEX)
        path_m = path_re.search(identifier)
        path_dict = path_m.groupdict()
        return path_dict['path'].replace('/','.').replace('\\','.')
    
    def __unicode__(self):
        return "svn"
    
    def is_valid(self, identifier):
        return super(SubversionRoute,self).is_valid(identifier)
    
    def fetch(self, identifier):
        
        _repo = self.vcs(identifier)
        _uid = self._uid(identifier)
        _destination = os.path.join(get_playbook_root(), '.cache', self._uid(identifier))
        if os.path.exists(_destination):
            shutil.rmtree(_destination)
            
        _repo.obtain(_destination)
                
        return Role(_destination,uid=_uid)


