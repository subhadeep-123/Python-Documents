import argparse
# We can change the default message by `usage`
parser = argparse.ArgumentParser(prog='myprogram',
                                 usage='%(prog)s [options]')
parser.add_argument('--foo',
                    nargs='?',
                    help='foo help')
parser.add_argument('bar',
                    nargs='+',
                    help='bar help')
# args = parser.parse_args()
print(parser.print_help())
