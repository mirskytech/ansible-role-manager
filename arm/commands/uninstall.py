import os, shutil, sys, re
from . import Command
from arm.util import get_playbook_root
import argparse, os
from git import Repo

from arm.prompt import query_true_false


class BaseCommand(Command):
        
    help = "remove a role from the library of dependencies"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('role', help='name of command to get help')
        parser.add_argument('-u','--unlink',action='store_true', help="remove link but leave in library")

        
    def run(self, argv):
        
        _root = get_playbook_root(os.getcwd())
        _role = os.path.join(_root, 'roles', argv.role)
        
        if not os.path.exists(_role):
            print "the role `%s` does not exist in the playbook's library" % _role
            return 1

        if not os.path.islink(_role):
            print "the role `%s` was not installed using ARM. refusing to delete." % _role
            return 1

        _library = os.path.join(os.path.realpath(_role))
        
        # TODO : check to see if the library role has non-committed changes
        
        # TODO : check to see if the library role has non-pushed changes

        for root, dir, files in os.walk(_role):
            if '.git' in root:
                continue
            for f in files:
                print "%s/%s" % (root, f)
                
        if query_true_false('Are you sure you want to remove `%s`?' % argv.role, default=True):
            print "uninstall"
        else:
            print "exiting"
                

        

                
        

        
        
