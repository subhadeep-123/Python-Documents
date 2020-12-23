import argparse
import textwrap

"""
By default, ArgumentParser objects add an option which simply displays the parser’s help message. 
For example, consider a file named myprogram.py containing the following code:

If -h or --help is supplied at the command line, the ArgumentParser help will be printed:

Occasionally, it may be useful to disable the addition of this help option. 
This can be achieved by passing False as the add_help= argument to ArgumentParser:

The help option is typically -h/--help. The exception to this is if the prefix_chars= is specified and does not include -, 
in which case -h and --help are not valid options. In this case, the first character in prefix_chars is used to prefix the help options:
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
    add_help=False
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
parser.print_help()
