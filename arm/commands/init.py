import os
from shutil import copytree
from . import Command, CommandException

class BaseCommand(Command):

    help = "initialize directory structure & files"    

    def __init__(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)	
        group.add_argument('-p','--project', help="create the recommended structure for a playbook")
        group.add_argument('-r','--role', help="within a playbook, create directly & file structure for role")        
        group.add_argument('-m','--module', help="within a playbook, create the structure for a custom module")
        
    def run(self, argv):

        patterns = os.path.join(os.path.dirname(__file__),'init')

        source = None
        destination = None

        if getattr(argv, 'project', False):
            source = 'project'
            destination = argv.project
        elif getattr(argv, 'role', False):
            source = 'role'
            destination = os.path.join('roles',argv.role)
        elif getattr(argv, 'module', False):
            raise NotImplemented('todo')
        else:
            raise SyntaxError('invalid option in subcommand')
        
        _source = os.path.join(patterns,source)
        _destination = os.path.join(os.getcwd(),destination)
        
        print "source: %s" % source

        if os.path.exists(_destination):
            raise CommandException('%s directory already exists: %s' % (source, _destination))
        
        copytree(_source, _destination)
        print "ansible %s created successfully" % (source)
        return 0

            





