import argparse

"""
Mutually exclusive meanes that events that cannot happed at the same time.
Creates mutually exclusive group. argparse will make sure that only one
of the arguments in the mutually exclusive group was present on the command line
"""
parser = argparse.ArgumentParser(prog='PROG')
# The relevance of required arg is atleast one of the mutually exclusive argument is required
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f',
                   '--foo',
                   action='store_true')
group.add_argument('-b',
                   '--bar',
                   action='store_false')
print(parser.parse_args(['-f']))  # This is Okay
print(parser.parse_args(['-f', '-b']))  # This is not Okay
