import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",
                    help="Display a Sq of a given number",
                    type=int)
parser.add_argument("-v",
                    "--verbose",
                    help="Increase Verbosity Output",
                    action="store_true")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"The square of {args.square} equals {answer}")
else:
    print(answer)
