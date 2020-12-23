import textwrap
import argparse

# ArgumentDefaultsHelpFormatter automatically adds information about default values to each of the argument help messages:
# It does not help in formatting the description or epilog of the argumentparser.

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
    usage='%(prog)s [options]',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('-f',
                    '--foo',
                    type=int,
                    default=42,
                    help='FOO!!')
parser.add_argument('bar',
                    nargs='*',
                    default=[1, 2, 3],
                    help='BAR!')
parser.print_help()
