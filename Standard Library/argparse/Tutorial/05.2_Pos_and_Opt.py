import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",
                    type=int,
                    help="Display a Square of a given number")

parser.add_argument("-v",
                    "--verbosity",
                    type=int,
                    choices=[0, 1, 2],
                    help="Increase Output Verbosity")

args = parser.parse_args()
answer = args.square**2

if args.verbosity == 2:
    print(f"The Square of {args.square} equals {answer} ")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)
