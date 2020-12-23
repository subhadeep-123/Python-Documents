import argparse
import textwrap

# Most command-line options will use - as the prefix, e.g. -f/--foo.
# Parsers that need to support different or additional prefix characters,
# e.g. for options like +f or /foo, may specify them using the
# prefix_chars= argument to the ArgumentParser constructor:

parser = argparse.ArgumentParser(
    prog="PROG",
    description=textwrap.dedent('''\
         Please do not mess up this text!
         --------------------------------
             I have indented it
             exactly the way
             I want it
         '''),
    epilog='''\
    likewise for this epilog whose whitespace will
    be cleaned up and whose words will be wrapped
    across a couple lines
    ''',
    prefix_chars='-+',
    usage='%(prog)s [options]',
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument('+f',
                    '--foo',
                    type=int,
                    default=42,
                    help='FOO!!')
parser.add_argument('bar',
                    nargs='*',
                    default=[1, 2, 3],
                    help='BAR!')
parser.print_help()
