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
        
        cmd_mod = __import__('arm.commands.%s' % command, locals(), globals(),['object'],-1)

        cmd_parser = subparsers.add_parser(command, help=cmd_mod.BaseCommand.help)
        cmd = cmd_mod.BaseCommand(cmd_parser)
        cmd_parser.set_defaults(func=cmd.run)
        
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
    

    
    
        

    
