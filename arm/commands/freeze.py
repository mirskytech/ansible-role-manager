import os, shutil, sys
from . import Command
from arm.util import get_playbook_root
import argparse
from git import Repo

class BaseCommand(Command):
        
    help = ""    
    
    def __init__(self, parser):
        parser.description = self.help
        #parser.add_argument('command_name', nargs='?', help='name of command to get help')

        
    def run(self, argv):
        
        _root = get_playbook_root(os.getcwd())
        _roles_directory = os.path.join(_root, 'roles')
        for _item in os.listdir(_roles_directory):
            _item = os.path.join(_roles_directory, _item)
            if not os.path.islink(_item):
                continue
            
            print "link : %s" % os.path.realpath(_item)
            repo = Repo(os.path.realpath(_item))
            for i in repo.remotes.origin.refs:
                for j in i.iter_items(repo):
                    print j
                
        

        
        
