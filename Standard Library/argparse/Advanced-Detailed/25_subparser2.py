import argparse


def foo(args):
    print(args.x * args.y)


def bar(args):
    print('((%s))' % args.z)


# Top level parser
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(title="SubCommands Demo",
                                  description="Shows how to use subparsers with two functions",
                                  help='Addidtional Help')

# Create the parser for the foo command
parser_foo = subparser.add_parser('--foo')
parser_foo.add_argument('-x',
                        type=int,
                        default=1)
parser_foo.add_argument('-y',
                        type=float)
parser_foo.set_defaults(func=foo)

# Create the parser for the "bar" command
parser_bar = subparser.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

# Parse the args and call whatever function was selected
# args = parser.parse_args('foo 1 -x 2'.split())
args = parser.parse_args()
print(args.func(args))
