import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo',
                    default=42)
parser.add_argument('-l',
                    '--length',
                    default=10,
                    type=int)
parser.add_argument('-w',
                    '--width',
                    default=12.5,
                    type=float)
# args = parser.parse_args(['--foo',
#                           '2'])

# print(args)
# args = parser.parse_args([])
# print(args)
args = parser.parse_args()

if args.foo:
    print(args.foo)
elif args.length:
    print(args.length)
elif args.width:
    print(args.width)
elif (args.foo and args.length and args.width):
    print(args.foo, args.length, args.width)
