import argparse
import operator
parser = argparse.ArgumentParser()
"""
ArgumentParser objects usually associate a single command-line argument with a single action to be taken. 
The nargs keyword argument associates a different number of command-line arguments with a single action. 
The supported values are:
"""
# N (an integer). N arguments from the command line will be gathered together into a list. For example:
parser.add_argument('-f',
                    '--foo',
                    nargs=2,
                    type=int)
parser.add_argument('bar',
                    nargs=1)

args = parser.parse_args()

if args.foo:
    print(args.foo)
    print(sum(args.foo))

# '?' one argument will be consumed from the command line if possible, and produced as a single item.
# If no command-line argument is present, the value from default will be produced.
# Note that for optional arguments, there is an additional case - the option string is present but not followed by a command-line argument.
# In this case the value from const will be produced. Some examples to illustrate this:

parser.add_argument('--foo',
                    nargs='?',
                    const='c',
                    default='d')
parser.add_argument('bar',
                    nargs='?',
                    default='d')

args = parser.parse_args(['XX', '--foo', 'YY'])
if args.foo:
    print(args.foo)

# '*' All command line arguments present are gathered into a list.
#  Note that it generally does not make much sense to have more then one positional arguemetn with 'nargs="*"',
# but multiple optional arguments with nargs='*' is possible. For example"

parser.add_argument('-sm',
                    '--sum',
                    nargs='*',
                    default=0,
                    type=int,)
parser.add_argument('-sb',
                    '--sub',
                    nargs='*',
                    default=0,
                    type=int,)
args = parser.parse_args()

if args.sum:
    print(args.sum)
    print(sum(args.sum))
elif args.sub:
    print(args.sub)
else:
    print(args.sum)
    print(args.sub)

# '+'. Just like '*', all command-line args present are gathered into a list. Additionally, an error message will be generated if there wasn’t at least one command-line argument present. For example:
parser.add_argument('foo', nargs='+')
args = parser.parse_args(['a', 'b'])
# args = parser.parse_args()
print(args)
