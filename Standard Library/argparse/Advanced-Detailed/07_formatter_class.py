# ArgumentParser objects allow the help formatting to be customized by specifying an alternate formatting class. Currently,
# there are four such classes:

import argparse
import textwrap

"""
The 4 formatter class availabe in argparse
class argparse.RawDescriptionHelpFormatter
class argparse.RawTextHelpFormatter
class argparse.ArgumentDefaultsHelpFormatter
class argparse.MetavarTypeHelpFormatter
"""
# RawDescriptionHelpFormatter and RawTextHelpFormatter give more control over how textual descriptions are displayed. By default ArgumentParser objects line-wrap testual description
# and epilog texts in command-line help messages:

parser = argparse.ArgumentParser(
    prog="PROG",
    description=textwrap.dedent('''\
         Please do not mess up this text!
         --------------------------------
             I have indented it
             exactly the way
             I want it
         '''),
    epilog='''likewise for this epilog whose whitespace will
    be cleaned up and whose words will be wrapped
    across a couple lines
    ''',
    usage='%(prog)s [options]',
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.print_help()

# Passing RawDescriptionHelpFormatter as formatter_class= indicates
# that description and epilog are already correctly formatted and should not be line-wrapped:
