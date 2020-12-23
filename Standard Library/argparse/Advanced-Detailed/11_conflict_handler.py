import argparse
import textwrap

"""
ArgumentParser objects do not allow two actions with the same option string. By default, 
ArgumentParser objects raise an exception if an attempt is made to create an argument with an 
option string that is already in use:

Sometimes (e.g. when using parents) it may be useful to simply override any older arguments with the same option string. 
To get this behavior, the value 'resolve' can be supplied to the conflict_handler= argument of ArgumentParser:
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
    conflict_handler='resolve'
)
parser.add_argument('+f',
                    '--foo',
                    help='Old Foo!!')
parser.add_argument('--foo',
                    help="New Foo!!"
                    )
parser.add_argument('bar',
                    nargs='*',
                    default=[1, 2, 3],
                    help='BAR!')

args = parser.parse_args()
