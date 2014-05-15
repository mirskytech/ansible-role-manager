import os, shutil, sys
from . import Command
from arm.util import get_playbook_root
import argparse

class BaseCommand(Command):
        
    help = ""    
    
    def __init__(self, parser):
        parser.description = self.help
        #parser.add_argument('command_name', nargs='?', help='name of command to get help')

        
    def run(self, argv):
        
        root = get_playbook_root(os.getcwd())
        
        for item in os.listdir(root):
            print item
        

        
        
