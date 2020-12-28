import argparse

# Create Top Level Parser
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo',
                    action='store_true',
                    help='Foo help')
subparser = parser.add_subparsers(help='sub-command help')

# Create the parser for the "a" command
parser_a = subparser.add_parser('a',
                                help='a help')
parser_a.add_argument('bar',
                      type=int,
                      help='bar help')

# Create the parser for the "b" command
parser_b = subparser.add_parser('b',
                                help='b help')
parser_b.add_argument('--baz',
                      choices='XYZ',
                      help='baz help')

# Parse some argument lists
print(parser.parse_args(['a', '12']))
print(parser.parse_args(['--foo', 'b', '--baz', 'Z']))

# args = parser.parse_args()
