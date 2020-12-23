import argparse
import textwrap

"""
Generally, argument defaults are specified either by passing a default to add_argument() or by calling the set_defaults() 
methods with a specific set of name-value pairs. Sometimes however, it may be useful to specify a single parser-wide default for arguments. 
This can be accomplished by passing the argument_default= keyword argument to ArgumentParser. For example, to globally suppress
attribute creation on parse_args() calls, we supply argument_default=SUPPRESS:
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
    argument_default=argparse.SUPPRESS
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
