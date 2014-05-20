import os, shutil, sys
from . import Command
from arm.util import get_playbook_root
import argparse
from git import Repo as git_repo
from hgapi import Repo as hg_repo

class freeze(Command):
        
    help = "produces dependencies file for this playbook based on arm installed roles"    
    
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
                              
            # _item vs realpath(_item)
            alias = None
            if os.path.basename(_item) != os.path.basename(os.path.realpath(_item)):
                alias = os.path.basename(_item)
                
            
            # if git
            if os.path.exists(os.path.join(os.path.realpath(_item),'.git')):
                repo = git_repo(os.path.realpath(_item))
                origin = repo.remotes[0].config_reader.config.get('remote "origin"','url')
                commit = repo.head.commit.hexsha
                if not alias:
                    print "git+%s@%s" % (origin,commit)
                    continue
                print "git+%s@%s#alias=%s" % (origin,commit,alias)
            
            # if mercurial
            if os.path.exists(os.path.join(os.path.realpath(_item),'.hg')):
                repo = hg_repo(os.path.realpath(_item))
                
                print repo
                
                if not alias:
                    print "hg+%s@%s" % (origin,commit)
                    continue
                print "hg+%s@%s#alias=%s" % (origin,commit,alias)
                
                
        

        
        
