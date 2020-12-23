import argparse
# We can add additional description of the program after the description
parser = argparse.ArgumentParser(prog='myprogram',
                                 usage='%(prog)s [options]',
                                 description="A Program for argparse pratice",
                                 epilog="And it is the end of the help")
parser.add_argument('--foo',
                    nargs='?',
                    help='foo help')
parser.add_argument('bar',
                    nargs='+',
                    help='bar help')
# args = parser.parse_args()
print(parser.print_help())

# as with the description arg, the epilog= test is by default line wrapped but this behaviour can be adjusted with the formatter_class argument to ArgumentParser
