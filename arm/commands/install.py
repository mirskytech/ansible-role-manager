from . import Command

class BaseCommand(Command):
        
    help = "install playbook command"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('role', help='name of the role to install')
        parser.add_argument('-f','--foo', help='the foo parameter')
        
    def run(self, argv):
        
        _role = argv.role
        
        

        
        
