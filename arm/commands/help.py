import os, shutil
from . import Command
from arm.util import get_playbook_root

class BaseCommand(Command):
        
    help = "install playbook command"    
    
    def __init__(self, parser):
        parser.description = self.help

        
    def run(self, argv):
        
        print get_playbook_root(os.getcwd())
        
