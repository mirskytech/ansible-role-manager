import sys, argparse, os
from routes import RouteException
from commands import Command, CommandException
from util import find_subclasses

# ----------------------------------------------------------------------

def main():
    '''
    Entry point function for the Ansible Role Manager.
    '''
    
    os.environ['COLUMNS'] = '100'
    
    # create command line argument parser and a sub-parser for the subcommands
    parser = argparse.ArgumentParser(prog=sys.argv[0])    
    subparsers = parser.add_subparsers()

    # find the subdirectory where all the ``arm `` commands are stored
    commands_dir = os.path.join(os.path.dirname(__file__),'commands')
    
    # import all the modules in the command directory
    for module in os.listdir(commands_dir):
        if module == '__init__.py' or module[-3:] != '.py':
            continue
        
        command_mod = __import__('arm.commands.%s' % module[:-3], locals(), globals(),['object'],-1)

        # add a subparser for each command
        '''
        Assumes that each command defines a ``BaseCommand`` which inherits from ``arm.commands.Command``     
        '''
        # search for all subclasses of ``arm.commands.Command``
        for command_name, command_class in find_subclasses(command_mod, Command):

            # attch the command
            command_parser = subparsers.add_parser(command_name, help=command_class.help)
            
            # instantiate the command and provide its ``run`` method as the callback
            command = command_class(command_parser)
            command_parser.set_defaults(func=command.run)
        
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

    
