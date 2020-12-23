import argparse
import textwrap

# MetavarTypeHelpFormatter uses the name of the type argument for each argument as the display name for its values
# (rather than using the dest as the regular formatter does):

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
    formatter_class=argparse.MetavarTypeHelpFormatter
)
parser.add_argument('-f',
                    '--foo',
                    type=int)
parser.add_argument('bar',
                    type=float)
parser.print_help()
