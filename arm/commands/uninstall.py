import os, shutil, sys, re, argparse, shutil
from . import Command
from arm.util import get_playbook_root
from git import Repo

from arm.prompt import query_true_false


class uninstall(Command):
        
    help = "remove a role from the library of dependencies"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('role', help='name of role to remove')
        parser.add_argument('-u','--unlink',action='store_true', help="remove link but leave in library")
        
    def run(self, argv):
        
        _root = get_playbook_root(os.getcwd())
        _role = os.path.join(_root, 'roles', argv.role)
        
        if not os.path.exists(_role):
            print "error :: the role `%s` does not exist in the playbook's library" % _role
            return 1

        if not os.path.islink(_role):
            print "error :: the role `%s` was not installed using ARM. refusing to delete." % _role
            return 1

        _library = os.path.join(os.path.realpath(_role))
        
        repo = Repo(_library)
        
        # check to see if the role in the library has non-committed changes
        if repo.git.status(porcelain=True).strip() != '':
            print "error :: the role `%s` has non-commited changes" % _role
            return 1

        # check to see if the library role has non-pushed changes
        # http://stackoverflow.com/questions/3844801
        def checkEqual(lst):
            return not lst or lst.count(lst[0]) == len(lst)
        
        if not checkEqual([ ref.commit for ref in repo.refs ] ):
            print "error :: the role `%s` has commits different from the origin"
            return 1
        
        for root, dir, files in os.walk(_library):
            if '.git' in root:
                continue
            for f in files:
                print "%s/%s" % (root, f)
                
        if query_true_false('Are you sure you want to remove `%s`?' % argv.role, default=True):
            os.unlink(_role)
            shutil.rmtree(_library)
        else:
            print "exiting"
                

        

                
        

        
        
