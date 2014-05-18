import os, shutil, re
from . import Command
from arm import LIBRARY_ROLE_PATH
from arm.util import retrieve_role, retrieve_all_roles, get_playbook_root


class BaseCommand(Command):
        
    help = "install playbook role"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('-U','--upgrade', action='store_true')
        parser.add_argument('-n', '--no-dependencies', action='store_true')
        parser.add_argument('role', help='name of the role to install')
        # TODO : add argument of where the role is to be installed
        # TODO : add argument of where the installed role should be linked
        
    def run(self, argv):
        
        role_ident = argv.role
        root = get_playbook_root(os.getcwd())
        if not root:
            print '''
            can't find playbook. 
            use `arm init` to create recommended structure.
            or use the `--no-dependencies` option.'''
            return 1
        
        aliasRE = re.compile(r'^(?P<ident>.+?)(\#alias\=(?P<alias>[a-zA-Z][a-zA-Z0-9]+?)){0,1}$')
        
        alias_match = aliasRE.match(argv.role)
        
        if not alias_match:
            print "error : could not find format"
            return 1
        
        alias = alias_match.groupdict().get('alias',None)
        
        role_ident = alias_match.groupdict()['ident']
        
        roles = []
        if argv.no_dependencies:
            role = retrieve_roll(roll_ident)
            roles = [ role, ]
        else:
            roles = retrieve_all_roles(role_ident)
        
        def _install_and_link(role, alias=None):
            # #<alias name> or #alias=<alias name>
            # alias = name if not #alias but only applies to the first role
            # should assert that's the first in the role list)
            name = role.get_name()
            if not alias:
                alias = role.get_name()

            source_path = role.get_path()
            library_path = os.path.join(root,LIBRARY_ROLE_PATH, name)
            link_path = os.path.join(root, 'roles', alias)
        
            if os.path.exists(library_path):
            
                if os.path.exists(link_path) and not os.path.islink(link_path):
                    print "role '%s' already exists as a non-library role"
                    return 1            
            
                if getattr(argv, 'upgrade', False):
                    if os.path.exists(library_path): shutil.rmtree(library_path)
                    if os.path.islink(link_path):
                        print "unlinking: %s" % link_path
                        os.unlink(link_path)
                else:
                    print "existing version already installed in library, use --upgrade to install latest"
                    return 1                
                
            shutil.copytree(source_path, library_path)
            
            os.symlink(
                os.path.relpath(os.path.join(LIBRARY_ROLE_PATH,name), 'roles/'),
                os.path.join(root,'roles',os.path.basename(alias))
                )
        
        roles = roles.values()
        r = _install_and_link(roles[0], alias)
        if r:
            return r
        
        for role in roles[1:]:
            r = _install_and_link(role)
            if r:
                return r
            
        print "role '%s' installed succesfully as '%s'" % (role_ident, alias)
        return 0
                
        
        

        
        
