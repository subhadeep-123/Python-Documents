import argparse
# We can add our own description of the program
parser = argparse.ArgumentParser(prog='myprogram',
                                 usage='%(prog)s [options]',
                                 description="A Program for argparse pratice")
parser.add_argument('--foo',
                    nargs='?',
                    help='foo help')
parser.add_argument('bar',
                    nargs='+',
                    help='bar help')
# args = parser.parse_args()
print(parser.print_help())
