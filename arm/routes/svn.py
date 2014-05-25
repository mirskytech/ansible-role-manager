import re, os, shutil
from . import VCSRoute, ROUTE_REGEX
from pip.vcs.subversion import Subversion
from arm import Role

# ----------------------------------------------------------------------

class SubversionRoute(VCSRoute):

    vcs = Subversion

    def __unicode__(self):
        return "svn"

    def _uid(self, identifier):        
        
        path_re = re.compile('%(fqdn)s\/(?P<path>.+?)/?$'%ROUTE_REGEX)
        path_m = path_re.search(identifier)
        path_dict = path_m.groupdict()
        return path_dict['path'].replace('/','.').replace('\\','.')
    



