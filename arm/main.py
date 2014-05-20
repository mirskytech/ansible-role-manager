import sys
import argparse
import os
from routes import RouteException
from commands import CommandException

# ----------------------------------------------------------------------

def main():
    '''
    Entry point function for the Ansible Role Manager.
    '''
    
    # create command line argument parser and a sub-parser for the subcommands
    parser = argparse.ArgumentParser(prog=sys.argv[0])    
    subparsers = parser.add_subparsers()

    # find the subdirectory where all the ``arm `` commands are stored
    commands_dir = os.path.join(os.path.dirname(__file__),'commands')
    
    # import all the modules in the command directory
    for module in os.listdir(commands_dir):
        if module == '__init__.py' or module[-3:] != '.py':
            continue
        
        # command is named using its filename
        command = module[:-3]
        
        cmd_mod = __import__('arm.commands.%s' % command, locals(), globals(),['object'],-1)

        # add a subparser for each command
        '''
        Assumes that each command defines a ``BaseCommand`` which inherits from ``arm.commands.Command``
        TODO: allow arbitrary name for command as long as it inherits from ``arm.commands.Command``
        def find_subclasses(module, clazz):
            for name in dir(module):
                o = getattr(module, name)
                try:
                    if (o != clazz) and issubclass(o, clazz):
                        yield name, o
                except TypeError: pass        
        '''
        cmd_parser = subparsers.add_parser(command, help=cmd_mod.BaseCommand.help)
        
        # instantiate the command and provide its ``run`` method as the callback
        cmd = cmd_mod.BaseCommand(cmd_parser)
        cmd_parser.set_defaults(func=cmd.run)
        
    # parse the command line arguments
    args = parser.parse_args(sys.argv[1:])
    
    try:
        # execute the proper subcommand, passing in the parsed args
        args.func(args)

    # display errors from routes or commands
    except RouteException as e:
        print "\nError (fetch) :: %s\n" % e
        exit(1)
    except CommandException as e:
        print "\nError (command) :: %s\n" % e
        exit(1)
    
    # successful
    exit(0)

    
