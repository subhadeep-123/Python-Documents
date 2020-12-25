# The name of this attibute is determined by the dest keyword argument of add_argument().
import argparse

"""
For optional argument actions, the value of dest is normally inferred from the option strings. 
ArgumentParser generates the value of dest by taking the first long option string and stripping 
away the initial -- string. If no long option strings were supplied, dest will be derived from 
the first short option string by stripping the initial - character. Any internal - characters will 
be converted to _ characters to make sure the string is a valid attribute name. 
The examples below illustrate this behavior:
"""
parser = argparse.ArgumentParser()
parser.add_argument('-f',
                    '--foo-bar',
                    '--foo',
                    dest='fobar')
parser.add_argument('-x',
                    '-y')
print(parser.parse_args(' -f 1 -x 2'.split()))

# For future reference try doing it without dest keyword
