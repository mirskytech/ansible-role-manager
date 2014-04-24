import sys
import argparse
import os

def main():
    

    commands_dir = os.path.join(os.path.dirname(__file__),'commands')
    parser = argparse.ArgumentParser(prog=sys.argv[0])    
    subparsers = parser.add_subparsers()
    
    for module in os.listdir(commands_dir):
        if module == '__init__.py' or module[-3:] != '.py':
            continue
        command = module[:-3]
        
        module = __import__('commands.%s' % command, locals(), globals(),['object'],-1)

        cmd_parser = subparsers.add_parser(command, help=module.BaseCommand.help)
        cmd = module.BaseCommand(cmd_parser)
        cmd_parser.set_defaults(func=cmd.run)
        
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
    

    
    
        

    
