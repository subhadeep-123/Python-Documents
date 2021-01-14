import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f',
                    '--foo',
                    nargs='*',
                    type=int)
args = parser.parse_args()
if args.foo:
    print(args.foo[0])
