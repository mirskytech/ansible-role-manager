
import argparse


def main():
    
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help')
    
    # create the parser for the "a" command
    parser_a = subparsers.add_parser('a', help='this is a description of a')
    parser_a.add_argument('bar', type=int, help='bar help')
    
    # create the parser for the "b" command
    parser_b = subparsers.add_parser('b', help='b help')
    parser_b.add_argument('--baz', choices='XYZ', help='baz help')
    
    # parse some argument lists
    parser.parse_args(['a', '12'])
    parser.parse_args(['--foo', 'b', '--baz', 'Z'])
    parser.parse_args(['--help'])

main()