# ArgumentParser objects allow the help formatting to be customized by specifying an alternate formatting class. Currently,
# there are four such classes:

import argparse
import textwrap

"""
RawTextHelpFormatter maintains whitespace for all sorts of help text, 
including argument descriptions. However, multiple new lines are replaced with one. 
If you wish to preserve multiple blank lines, add spaces between the newlines.
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
    epilog='''likewise for this epilog whose whitespace will
    be cleaned up and whose words will be wrapped
    across a couple lines
    ''',
    usage='%(prog)s [options]',
    formatter_class=argparse.RawTextHelpFormatter
)
parser.print_help()
