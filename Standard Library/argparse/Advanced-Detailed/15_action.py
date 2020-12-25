import argparse


"""
ArgumentParser objects associate command-line arguments with actions. 
These actions can do just about anything with the command-line arguments associated with them, 
though most actions simply add an attribute to the object returned by parse_args(). 
The action keyword argument specifies how the command-line arguments should be handled. The supplied actions are:
"""
parser = argparse.ArgumentParser(conflict_handler='resolve')

# 'store' - This just stores the argument’s value. This is the default action. For example:
parser.add_argument('--foo')
print(parser.parse_args('--foo 1'.split()))

# 'store_const' - This stores the value specified by the const keyword argument. The 'store_const' action is most commonly used with optional arguments that specify some sort of flag. For example:
parser.add_argument('--foo',
                    action='store_const',
                    const=42)
print(parser.parse_args(['--foo']))

# 'store_true' and 'store_false' - These are special cases of 'store_const' used for storing the values True and False respectively.
# In addition, they create default values of False and True respectively. For example:
parser.add_argument('--foo',
                    action='store_true')
parser.add_argument('--bar',
                    action='store_false')
parser.add_argument('--baz',
                    action='store_false')
print(parser.parse_args('--foo --bar'.split()))

# 'append' - This stores a list, and appends each argument value to the list. This is useful to allow an option to be specified multiple times.
parser.add_argument('--foo', action='append')
print(parser.parse_args('--foo 1 --foo 2'.split()))

# 'append_const' - This stores a list, and appends the value specified by the const keyword argument to the list.
# (Note that the const keyword argument defaults to None.) The 'append_const' action is typically useful when multiple arguments need to store
# constants to the same list. For example:
parser.add_argument('--str',
                    dest='types',
                    action='append_const',
                    const=str)
parser.add_argument('--int',
                    dest='types',
                    action='append_const',
                    const=int)
print(parser.parse_args('--str --int'.split()))


# 'count' - This counts the number of times a keyword argument occurs. For example, this is useful for increasing verbosity levels:
parser.add_argument('--verbose',
                    '-v',
                    action='count',
                    default=0)
print(parser.parse_args(['-vvv']))
# The default will be None unless explictly set to 0.


# 'version' - This expects a version= keyword argument in the add_argument() call, and prints version information and exits when invoked:
parser.add_argument('--version',
                    action='version',
                    version='%(prog)s 2.0')
parser.parse_args(['--version'])

# 'extend' - This stores a list, and extends each argument value to the list. Example usage:
parser.add_argument("--foo",
                    action="extend",
                    nargs="+",
                    type=str)
print(parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"]))


# Arbitary action subclass or other objects that implements the same interface.
# The BooleanOptionalAction is available in argparse and adds support for boolean actions such as --foo and --no-foo.
parser.add_argument('--foo',
                    action=argparse.BooleanOptionalAction)
print(parser.parse_args(['--no-foo']))
