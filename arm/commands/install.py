import os, shutil
from . import Command
from arm.util import retrieve_role, get_playbook_root

class BaseCommand(Command):
        
    help = "install playbook command"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('-U','--upgrade', action='store_true')        
        parser.add_argument('role', help='name of the role to install')
        
    def run(self, argv):
        
        _role = argv.role
        root = get_playbook_root(os.getcwd())
        if not root:
            print "can't find playbook. use arm init to create recommended structure."
            return 1
        
        source, name = retrieve_role(_role)

        library = os.path.join(root,'library_roles',name)
        destination = os.path.join(root, 'roles', name)
        if os.path.exists(library):
            
            if os.path.exists(destination) and not os.path.islink(destination):
                print "role '%s' already exists as a non-library role"
                return 1            
            
            if getattr(argv, 'upgrade', False):
                if os.path.exists(library): shutil.rmtree(library)
                if os.path.islink(destination):
                    print "unlinking: %s" % destination
                    os.unlink(destination)
            else:
                print "existing version already installed in library, use --upgrade to install latest"
                return 1                
                


        shutil.copytree(source, library)
        
        os.symlink(
            os.path.relpath(destination, 'roles/'),
            os.path.join('roles',os.path.basename(name))
            )
        print "role '%s' installed succesfully" % (argv.role)
        return 0
                
        
        

        
        
