import os, shutil, re
from . import Command, CommandException
from arm import LIBRARY_ROLE_PATH
from arm.odict import odict
from arm.util import retrieve_role, retrieve_all_roles, get_playbook_root


class BaseCommand(Command):
        
    help = "install playbook role"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('-U','--upgrade', action='store_true')
        parser.add_argument('-n', '--no-dependencies', action='store_true')
        
        group = parser.add_mutually_exclusive_group(required=True)               
        group.add_argument('-r', '--requirements')
        group.add_argument('role', nargs='?')

        # TODO : add argument of where the role is to be installed
        # TODO : add argument of where the installed role should be linked
        
    def run(self, argv):
        
        root = get_playbook_root(os.getcwd())

        if not root:
            print '''
            can't find playbook. 
            use `arm init` to create recommended structure.
            or use the `--no-dependencies` option.'''
            return 1
        
        roles = odict()
        
        if getattr(argv, 'requirements', ''):
            for role_ident in open(argv.requirements,'r'):
                roles = self._fetch(role_ident, argv.no_dependencies, roles)
        else:
            roles = self._fetch(argv.role, argv.no_dependencies, roles )
            
            
        for alias,role in roles.items():
            self._install_and_link(alias, role, getattr(argv, 'upgrade', False))
                   
        print "\nrole(s) '%s' installed succesfully.\n" % (", ".join(roles.keys()))
        return 0
            
    
    def _fetch(self, role_ident, no_dependencies, roles):
        
        aliasRE = re.compile(r'^(?P<ident>.+?)(\#alias\=(?P<alias>[a-zA-Z][a-zA-Z0-9]+?)){0,1}$')
        
        alias_match = aliasRE.match(role_ident)
        
        if not alias_match:
            print "error : could not find format"
            return 1
        
        role_ident = alias_match.groupdict()['ident']
        alias = alias_match.groupdict().get('alias',None)
                
        if no_dependencies:
            role = retrieve_roll(roll_ident, alias, roles)

            if alias:
                return roles.update( { alias:role } )
            
            return roles.update( { role.get_name():role } )

        return retrieve_all_roles(role_ident, alias, roles)

        
    def _install_and_link(self, alias, role, upgrade=False):
        
        root = get_playbook_root(os.getcwd())
        
        source_path = role.get_path()
        library_path = os.path.join(root, LIBRARY_ROLE_PATH, role.get_name())
        link_path = os.path.join(root, 'roles', alias)
    
        if os.path.exists(library_path):
        
            if os.path.exists(link_path) and not os.path.islink(link_path):
                raise Exception("role '%s' already exists as a non-library role")
        
            if upgrade:
                if os.path.exists(library_path): shutil.rmtree(library_path)
                if os.path.islink(link_path):
                    print "unlinking: %s" % link_path
                    os.unlink(link_path)
            else:
                raise CommandException("'%s' already installed in library, use --upgrade to install latest" % role.get_name())
            
        shutil.copytree(source_path, library_path)
        
        os.symlink(
            os.path.relpath(os.path.join(LIBRARY_ROLE_PATH,role.get_name()), 'roles/'),
            os.path.join(root,'roles',os.path.basename(alias))
            )
        

        
        

        
        
