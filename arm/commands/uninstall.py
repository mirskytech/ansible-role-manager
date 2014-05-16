import os, shutil, sys
from . import Command
from arm.util import get_playbook_root
import argparse
from git import Repo

class BaseCommand(Command):
        
    help = "remove a role"    
    
    def __init__(self, parser):
        parser.description = self.help
        #parser.add_argument('command_name', nargs='?', help='name of command to get help')
        parser.add_argument('-u','--unlink',action='store_true', help="remove link but leave in library")

        
    def run(self, argv):
        
        _root = get_playbook_root(os.getcwd())
        _roles_directory = os.path.join(_root, 'roles')
       
        for root, dir, files in os.walk(os.path.join(_root, 'library_roles/')):
            for f in files:
                print "r: %s/%s" % (root, f)
           
                
        

        
        
