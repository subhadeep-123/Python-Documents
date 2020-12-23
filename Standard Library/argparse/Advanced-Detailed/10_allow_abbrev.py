import argparse
import textwrap

"""
Normally, when you pass an argument list to the parse_args() method of an ArgumentParser, it recognizes abbreviations of long options.

This feature can be disabled by setting allow_abbrev to False:
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
    allow_abbrev=False
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

args = parser.parse_args()
