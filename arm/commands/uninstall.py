import os, shutil, sys, re
from . import Command
from arm.util import get_playbook_root
import argparse, os
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
    
        #import logging
        
        #logger = logging.getLogger('arm')    

        #logger.info('my arm message')
        #logger.warning('my arm warning')
        #for root, dir, files in os.walk(os.path.join(_root, 'library_roles/')):
            #if '.git' in root:
                #continue
            #for f in files:
                #print "%s/%s" % (root, f)
                
        from arm.prompt import menu
        my_menu = [
            { 'id':'id1',
              'name':'choice 1',
              'description':'this is choice 1',
              'callback':lambda a: "called back: %s" % a
            },
            { 'id':'id2',
              'name':'choice 2',
              'description':'this is choice 2',
              'callback':None
            },
            {
            'id':'id3',
            'name':'choice 3',
            'description':'this is choice 3'
            }
        ]

        
        menu(my_menu)
           
                
        

        
        
