import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v",
                   "--verbose",
                   action="store_true")
group.add_argument("-q",
                   "--quiet",
                   action="store_true")
parser.add_argument("x",
                    type=int,
                    help="The Base")
parser.add_argument("y",
                    type=int,
                    help="The Exponent")
args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")

# So Now we need to add some description
