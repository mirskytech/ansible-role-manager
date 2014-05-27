import os, shutil, re
from . import Command, CommandException
from arm.conf import settings
from arm.odict import odict
from arm.util import retrieve_role, retrieve_all_roles, get_playbook_root
from arm import Role, Module


class install(Command):
        
    help = "install playbook role" 
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('-U','--upgrade', action='store_true')
        parser.add_argument('-n', '--no-dependencies', action='store_true')
        
        group = parser.add_mutually_exclusive_group(required=True)               
        group.add_argument('-r',  '--requirements', nargs=1, help="install from requirements file (see `arm help freeze`)")
        group.add_argument('role', nargs='?', help="specifier of role to install locally")

        # TODO : add argument of where the role is to be installed
        # TODO : add argument of where the installed role should be linked


    def run(self, argv):
        print "installing"
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
        
        print "Roles to install: %s" % roles
            
        for alias,role in roles.items():
            self._install_and_link(alias, role, getattr(argv, 'upgrade', False))
                   
        print "\nrole(s) '%s' installed succesfully.\n" % (", ".join(roles.keys()))
        exit(0)
            
    
    def _fetch(self, role_ident, no_dependencies, roles):
        
        aliasRE = re.compile(r'^(?P<ident>.+?)(\#alias\=(?P<alias>[a-zA-Z][a-zA-Z0-9]+?)){0,1}$')
        
        alias_match = aliasRE.match(role_ident)
        
        if not alias_match:
            print "error : could not find format"
            return 1
        
        role_ident = alias_match.groupdict()['ident']
        alias = alias_match.groupdict().get('alias',None)
                
        if no_dependencies:
            
            role = retrieve_role(role_ident)

            if alias:
                roles.update( { alias:role } )
                return roles
            
            roles.update( { role.get_name():role } )
            return roles

        return retrieve_all_roles(role_ident, alias, roles)

        
    def _install_and_link(self, alias, rmp, upgrade=False):
        
        root = get_playbook_root(os.getcwd())
        source_path = rmp.get_path()
        library_path = None
        link_path = None
        if type(rmp) == Role:
            installed_rmp_dir = settings.installed_modules_dir
            ansible_rmp_dir = settings.ansible_modules_dir
            
            #library_path = os.path.join(root, settings.installed_roles_dir, rmp.get_name())
            #link_path = os.path.join(root, settings.ansible_roles_dir, alias)
        elif type(rmp) == Module:
            
            installed_rmp_dir = settings.installed_modules_dir
            ansible_rmp_dir = settings.ansible_modules_dir
            
        installed_rmp_path = os.path.join(installed_rmp_dir, rmp.get_name())
        library_path = os.path.join(root, installed_rmp_path)
        link_path = os.path.join(root, installed_rmp_dir, alias)
            
            
        # if the library path is also the role, local role dependency
        if os.path.realpath(link_path) == os.path.realpath(library_path):
            return
        
        if os.path.exists(library_path):
        
            if os.path.exists(link_path) and not os.path.islink(link_path):
                if type(rmp) == Role:
                    raise Exception("role '%s' already exists as a non-installed role")
                elif type(rmp) == Module:
                    raise Exception("module '%s' aleady exists as a non-installed role")
        
            if upgrade:
                if os.path.exists(library_path): shutil.rmtree(library_path)
                if os.path.islink(link_path):
                    print "unlinking: %s" % link_path
                    os.unlink(link_path)
            else:
                raise CommandException("'%s' already installed in library, use --upgrade to install latest" % rmp.get_name())

        shutil.copytree(source_path, library_path)
        ansible_rmp_path = os.path.join(root,ansible_rmp_dir)
        if not os.path.exists(ansible_rmp_path):
            os.mkdir(ansible_rmp_path)

        os.symlink(
            os.path.relpath(installed_rmp_path, ansible_rmp_dir),
            os.path.join(ansible_rmp_path,os.path.basename(alias))
            )

            
        

        
        

        
        
