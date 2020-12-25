import argparse

# This is a way to refer to each expected argument
"""
Note that metavar only changes the displayed name - the name of the attribute on the parse_args() object is still determined by the dest value.

Different values of nargs may cause the metavar to be used multiple times. Providing a tuple to metavar specifies a different display for each of the arguments
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo',
                    metavar='YYY')
parser.add_argument('bar',
                    metavar='XXX')
parser.add_argument('-x', nargs=2)
parser.add_argument('--foop',
                    nargs=2,
                    metavar=('bar', 'baz'))
# print(parser.parse_args('X --foo Y'.split()))
parser.print_help()
