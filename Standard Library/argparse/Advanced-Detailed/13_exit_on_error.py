import argparse
import textwrap

"""
Normally, when you pass an invalid argument list to the parse_args() method of an ArgumentParser, it will exit with error info.

If the user would like catch errors manually, the feature can be enable by setting exit_on_error to False:
"""

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
    formatter_class=argparse.RawDescriptionHelpFormatter,
    argument_default=argparse.SUPPRESS,
    allow_abbrev=False,
    conflict_handler='resolve',
    exit_on_error=False
)
# parser.add_argument('+f',
#                     '--foo',
#                     help='Old Foo!!')
# parser.add_argument('--foo',
#                     help="New Foo!!"
#                     )
# parser.add_argument('bar',
#                     nargs='*',
#                     default=[1, 2, 3],
#                     help='BAR!')

# args = parser.parse_args()

parser.add_argument('--integers', type=int)

try:
    parser.parse_args('--integers a'.split())
except argparse.ArgumentError:
    print('Catching an argumentError')
