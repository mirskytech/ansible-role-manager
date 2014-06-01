import os
import shutil
from jinja2 import Environment, FileSystemLoader
from . import Command, CommandException
from arm.util import get_playbook_root
from arm.conf import settings

class init(Command):

    help = "initialize directory structure & files"    

    def __init__(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)	
        group.add_argument('-p','--playbook', help="create the recommended structure for a playbook")
        group.add_argument('-r','--role', help="within a playbook, create directory & file structure for role")
        group.add_argument('-m','--module', help="within a playbook, create the structure for a custom module")
        
        parser.add_argument('-e','--editable', action='store_true', help="create new role or module in library as dependency" )
    
    def run(self, argv):

        patterns = os.path.join(os.path.dirname(__file__),'init')
        current = os.getcwd()
        
        if argv.playbook and argv.editable:
            raise CommandException("combination of flags '-e' and '-p' not allowed.")
        
        def _default(item): return item if item else ''
        
        root = _default(get_playbook_root(current))

        playbook = _default(argv.playbook)
        role = _default(argv.role)
        module = _default(argv.module)

        sources = (
            os.path.join(patterns, 'playbook'), None,
            os.path.join(patterns, 'role'), os.path.join(patterns, 'role'),
            os.path.join(patterns, 'module'), os.path.join(patterns, 'module'),
        )
        
        destinations = (
            os.path.join(current, playbook),
            None,
            os.path.join(root, settings.paths.ansible_roles_dir, role),
            os.path.join(root, settings.paths.installed_roles_dir, role),
            os.path.join(root, settings.paths.ansible_modules_dir, module),
            os.path.join(root, settings.paths.installed_modules_dir, module)
        )

        links = (
            None, None,
            None, os.path.join(root, settings.paths.ansible_roles_dir, role),
            None, os.path.join(root, settings.paths.ansible_modules_dir, module)
        )
        
        def _eval(item,value): return bool(item) * value
                
        index = (_eval(playbook, 0) | _eval(role,2) | _eval(module,4)) + _eval(argv.editable,1)

        _source = sources[index]
        _destination = destinations[index]

        env = Environment(loader=FileSystemLoader(_source))

        def _install_template(_path):
            os.makedirs(os.path.join(_destination, _path))

            files = os.listdir(os.path.join(_source,_path))
            for f in files:
                _s = os.path.join(_source,_path,f)
                _d = os.path.join(_destination, _path, f)                    
                
                if os.path.isdir(_s):
                    # recurse through any subdirectory
                    _install_template(os.path.join(_path,f))
                elif '.armj2' in f:
                    # render template to _destination + _path +f
                    template = env.get_template(os.path.join(_path,f))
                    _d = _d.replace('.armj2','')
                    with open(_d, 'wb') as fh:
                        fh.write(template.render(name=_d))
                else:
                    # copy to _destination + _path + f
                    shutil.copy(_s,_d)

        _name = (
            'playbook',
            None,
            'role',
            'role',
            'module',
            'module'
        )


        if os.path.exists(_destination) or \
           (links[index] and os.path.exists(links[index])):
            raise CommandException("%s '%s' already exists." % (_name[index],os.path.basename(_destination)))
        _install_template('')
        if links[index]:
            os.symlink(
                os.path.relpath(_destination, os.path.dirname(links[index])),
                links[index])
                
        print "ansible %s created successfully" % (_name[index])
        return 0

            





