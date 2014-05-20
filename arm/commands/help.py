import os, shutil, sys
from . import Command
from arm.util import get_playbook_root
import argparse

# ----------------------------------------------------------------------

class BaseCommand(Command):
        
    help = "an alias for calling `-h` on any subcommand"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('command', default=None, nargs='?')
        #parser.add_argument('command_name', nargs='?', help='name of command to get help')

        
    def run(self, argv):
        
        commands_dir = os.path.dirname(__file__)
        parser = argparse.ArgumentParser(prog=sys.argv[0])    
        subparsers = parser.add_subparsers()
        
        for module in os.listdir(commands_dir):
            if module == '__init__.py' or module[-3:] != '.py':
                continue
            command = module[:-3]
            
            cmd_mod = __import__('arm.commands.%s' % command, locals(), globals(),['object'],-1)
    
            cmd_parser = subparsers.add_parser(command, help=cmd_mod.BaseCommand.help)
            cmd = cmd_mod.BaseCommand(cmd_parser)
            cmd_parser.set_defaults(func=cmd.run)
            
        if getattr(argv, 'command',None):
            args = parser.parse_args([argv.command, '-h'])
        args = parser.parse_args(['-h'])
        
        
