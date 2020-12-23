import argparse
# we can change the program name by `prog`
parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
