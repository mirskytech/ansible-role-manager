from . import Command
from arm.util import retrieve_role

class BaseCommand(Command):
        
    help = "install playbook command"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('role', help='name of the role to install')
        
    def run(self, argv):
        
        _role = argv.role
        
        retrieve_role(_role)
        
        

        
        
