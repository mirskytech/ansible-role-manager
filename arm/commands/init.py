import os
from shutil import copytree
from jinja2 import Environment, FileSystemLoader
from . import Command, CommandException

class BaseCommand(Command):

    help = "initialize directory structure & files"    

    def __init__(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)	
        group.add_argument('-p','--playbook', help="create the recommended structure for a playbook")
        group.add_argument('-r','--role', help="within a playbook, create directly & file structure for role")        
        group.add_argument('-m','--module', help="within a playbook, create the structure for a custom module")
        
    def run(self, argv):

        patterns = os.path.join(os.path.dirname(__file__),'init')

        source = None
        destination = None

        if getattr(argv, 'playbook', False):
            source = 'playbook'
            destination = argv.playbook
        elif getattr(argv, 'role', False):
            source = 'role'
            destination = os.path.join('roles',argv.role)
        elif getattr(argv, 'module', False):
            raise NotImplemented('todo')
        else:
            raise SyntaxError('invalid option in subcommand')
        
        _source = os.path.join(patterns,source)
        _destination = os.path.join(os.getcwd(),destination)
        
        if os.path.exists(_destination):
            raise CommandException('%s directory already exists: %s' % (source, _destination))

        #copytree(_source, _destination)

        env = Environment(loader=FileSystemLoader(_source))

        def _handle(_path):
            
            # create directory _destination + _path
            
            for root,dirs,files in os.walk(os.path.join(_source, _path)):
                
                for f in files:
                    if '.arm' in f:
                        env.get_template(os.path.join(_path,f))
                        # render to _destination + _path + f
                    else:
                        # copy to _destination + _path + f

                for d in dirs:
                    # create destination dir
                    _handle(os.path.join(_path,d))
            return
                            
        _handle('')        
        
        
        print "ansible %s created successfully" % (source)
        return 0

            





