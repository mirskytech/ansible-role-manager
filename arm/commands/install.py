import os, shutil
from . import Command
from arm.util import retrieve_role, retrieve_all_roles, get_playbook_root


class BaseCommand(Command):
        
    help = "install playbook role"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('-U','--upgrade', action='store_true')
        parser.add_argument('-n', '--no-dependencies', action='store_true')
        parser.add_argument('role', help='name of the role to install')
        
    def run(self, argv):
        
        role_ident = argv.role
        root = get_playbook_root(os.getcwd())
        if not root:
            print '''
            can't find playbook. 
            use `arm init` to create recommended structure.
            or use the `--no-dependencies` option.'''
            return 1
        
        roles = []
        if argv.no_dependencies:
            role = retrieve_roll(roll_ident)
            roles = [ role, ]
        else:
            roles = retrieve_all_roles(role_ident)
        
        for role in roles.itervalues():
            # #<alias name> or #alias=<alias name>
            # alias = name if not #alias but only applies to the first role
            # should assert that's the first in the role list)
            name = role.get_name()
            alias = role.get_name()

            source_path = role.get_path()
            library_path = os.path.join(root,'library_roles', name)
            link_path = os.path.join(root, 'roles', alias)
        
            if os.path.exists(library_path):
            
                if os.path.exists(link_path) and not os.path.islink(link_path):
                    print "role '%s' already exists as a non-library role"
                    return 1            
            
                if getattr(argv, 'upgrade', False):
                    if os.path.exists(library_path): shutil.rmtree(library_pathe)
                    if os.path.islink(link_path):
                        print "unlinking: %s" % link_path
                        os.unlink(link_path)
                else:
                    print "existing version already installed in library, use --upgrade to install latest"
                    return 1                
                
            shutil.copytree(source_path, library_path)
        
        
            os.symlink(
                os.path.relpath(library_path, 'roles/'),
                os.path.join('roles',os.path.basename(alias))
                )
            print "role '%s' installed succesfully" % (argv.role)
        return 0
                
        
        

        
        
